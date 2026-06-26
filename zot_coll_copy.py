"""Copy Zotero collections between libraries (personal/user and group), in any direction.
(Script file: zot_coll_copy.py.)

This is a deliberately specific tool: it deep-copies whole collections (their items, and
optionally child notes and file attachments) from one Zotero library into another -- user to
group (the common case), group to user, or group to group. Zotero keys are per-library, so
items are *recreated* in the target -- a copy, not a move. Collections may be renamed on the
way across.

Credentials come from the environment (loaded by direnv from .env), so run via direnv:

    direnv exec . uv run zot_coll_copy.py <command> [options]

Required environment variables:
    ZOTERO_LIBRARY_ID   your personal ("user") library id (used as the default source and for
                        account/group discovery)
    ZOTERO_API_KEY      an API key with READ access to the source and WRITE access to the
                        target (grant per-group/all-group access at zotero.org/settings/keys)

User-facing documentation lives in the command docstrings below; run any command with
--help to read it.
"""

import os
import tempfile
from collections import defaultdict

import click
from pyzotero import zotero

STRIP_FIELDS = ("key", "version", "dateAdded", "dateModified")


# --------------------------------------------------------------------------- connections
def _env(name):
    try:
        return os.environ[name]
    except KeyError:
        raise click.ClickException(
            f"${name} is not set. Run via "
            f"`direnv exec . uv run zot_coll_copy.py ...` so .env is loaded."
        )


def _parse_ref(spec):
    """Parse a library spec into (library_type, library_id).

    Accepts 'user', 'user:<id>' or 'group:<id>'. Bare 'user' resolves to ZOTERO_LIBRARY_ID.
    """
    s = (spec or "").strip()
    if s in ("", "user"):
        return ("user", _env("ZOTERO_LIBRARY_ID"))
    kind, sep, rid = s.partition(":")
    kind, rid = kind.strip().lower(), rid.strip()
    if sep and kind in ("user", "group") and rid:
        return (kind, rid)
    raise click.ClickException(
        f"Bad library spec {spec!r}; use 'user', 'user:<id>', or 'group:<id>'."
    )


def _client(ref):
    library_type, library_id = ref
    return zotero.Zotero(str(library_id), library_type, _env("ZOTERO_API_KEY"))


def _account():
    """A user-bound client, used for key_info()/groups() discovery (group-bound groups() is
    unreliable)."""
    return zotero.Zotero(_env("ZOTERO_LIBRARY_ID"), "user", _env("ZOTERO_API_KEY"))


def _can(access, ref, mode):
    """Whether the key's access map (from key_info) permits `mode` ('read'/'write') on ref."""
    if ref[0] == "user":
        u = access.get("user", {}) or {}
        return bool(u.get("write")) if mode == "write" else bool(u.get("library") or u.get("write"))
    g = access.get("groups", {}) or {}
    perms = g.get("all") or g.get(str(ref[1])) or {}
    return bool(perms.get("write")) if mode == "write" else bool(perms.get("library") or perms.get("write"))


def _ref_label(ref, groups_by_id):
    if ref[0] == "user":
        you = " (you)" if str(ref[1]) == _env("ZOTERO_LIBRARY_ID") else ""
        return f"user:{ref[1]}{you}"
    return f"group:{ref[1]} ({groups_by_id.get(str(ref[1])) or 'unknown / not visible'})"


# --------------------------------------------------------------------------- pagination
def _paginate(zot_method, *args, max_items=None, **kwargs):
    """Fetch all results from a pyzotero read method via manual start/limit pagination.

    Avoids zot.everything(), which can trip RLock pickling in some (e.g. MCP) contexts.
    """
    items, start, page_size = [], 0, 100
    while True:
        batch = zot_method(*args, start=start, limit=page_size, **kwargs)
        if not batch:
            break
        items.extend(batch)
        if len(batch) < page_size:
            break
        start += page_size
        if max_items and len(items) >= max_items:
            return items[:max_items]
    return items


# --------------------------------------------------------------------------- response helpers
def _success_map(resp):
    """{batch_index(int): new_key(str)} from a create_items / create_collections response."""
    out = {}
    succ = resp.get("success")
    if succ:
        for idx, key in succ.items():
            out[int(idx)] = key
    else:  # tolerate the verbose `successful` shape some versions return
        for idx, item in (resp.get("successful") or {}).items():
            out[int(idx)] = item.get("key") if isinstance(item, dict) else item
    return out


def _report_failures(resp, label):
    for idx, info in (resp.get("failed") or {}).items():
        click.echo(f"  ! {label} #{idx} failed: {info}", err=True)


def _count_uploads(res, name):
    """Count successful attachment uploads from an attachment_simple/upload response."""
    if isinstance(res, dict):
        made = len(res.get("success", []) or []) + len(res.get("unchanged", []) or [])
        for f in res.get("failure", []) or []:
            click.echo(f"  ! attachment '{name}' upload failed: {f}", err=True)
        return made
    return 1


def _chunks(seq, n=50):
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


# --------------------------------------------------------------------------- provenance
def _item_uri(ref, key):
    """Zotero item URI for provenance, e.g. http://zotero.org/users/2862/items/ABCD1234 or
    http://zotero.org/groups/6598607/items/ABCD1234."""
    seg = "groups" if ref[0] == "group" else "users"
    return f"http://zotero.org/{seg}/{ref[1]}/items/{key}"


def _sameas_keys(relations, src_ref):
    """Source item keys recorded in an owl:sameAs relation (value may be a str or a list)."""
    val = (relations or {}).get("owl:sameAs")
    if not val:
        return set()
    vals = val if isinstance(val, list) else [val]
    prefix = _item_uri(src_ref, "")
    return {v[len(prefix):] for v in vals if isinstance(v, str) and v.startswith(prefix)}


# --------------------------------------------------------------------------- item transforms
def _clean_item(data, new_collection_keys, src_ref):
    """Strip per-library fields, remap collections, stamp owl:sameAs provenance."""
    d = dict(data)
    old_key = d.get("key")
    for f in STRIP_FIELDS:
        d.pop(f, None)
    d["relations"] = {"owl:sameAs": _item_uri(src_ref, old_key)}
    d["collections"] = list(new_collection_keys)
    return d


def _clean_child(data, src_ref):
    """Prepare a child note/attachment for recreation under a new parent (via parentid)."""
    d = dict(data)
    old_key = d.get("key")
    for f in STRIP_FIELDS:
        d.pop(f, None)
    d.pop("parentItem", None)
    d["relations"] = {"owl:sameAs": _item_uri(src_ref, old_key)}
    d["collections"] = []
    return d


# --------------------------------------------------------------------------- collection tree
def _collections_by_key(src):
    """{key: data-dict} for every collection in the source library."""
    return {c["data"]["key"]: c["data"] for c in _paginate(src.collections)}


def _descendants(seed_keys, by_key):
    children = defaultdict(list)
    for k, d in by_key.items():
        parent = d.get("parentCollection")
        if parent:
            children[parent].append(k)
    out, stack = set(), list(seed_keys)
    while stack:
        k = stack.pop()
        if k in out:
            continue
        out.add(k)
        stack.extend(children.get(k, []))
    return out


def _depth(key, by_key):
    d, cur = 0, by_key[key].get("parentCollection")
    while cur and cur in by_key:
        d += 1
        cur = by_key[cur].get("parentCollection")
    return d


def _ensure_collections(tgt, to_copy, by_key, rename, reuse, dry_run):
    """Recreate the collection subtree in the target, parents first.

    Returns old_collection_key -> new_collection_key. `rename` maps a source collection key to
    a new target name (others keep their source name). With `reuse`, an existing target
    collection with the same (target) name under the same (mapped) parent is reused, not
    duplicated.
    """
    existing = {}
    if reuse and not dry_run:
        for c in _paginate(tgt.collections):
            d = c["data"]
            existing[(d.get("parentCollection") or None, d["name"])] = d["key"]

    col_map = {}
    for old in sorted(to_copy, key=lambda k: _depth(k, by_key)):
        name = rename.get(old) or by_key[old]["name"]
        src_parent = by_key[old].get("parentCollection")
        new_parent = col_map.get(src_parent) if src_parent in to_copy else None
        where = f"under {new_parent}" if new_parent else "top-level"

        if dry_run:
            col_map[old] = f"<new:{old}>"
            click.echo(f"  + collection '{name}' ({where})")
            continue

        key = existing.get((new_parent, name)) if reuse else None
        if key:
            col_map[old] = key
            click.echo(f"  = reuse collection '{name}' ({key})")
            continue

        payload = {"name": name}
        if new_parent:
            payload["parentCollection"] = new_parent
        resp = tgt.create_collections([payload])
        new_key = _success_map(resp).get(0)
        if not new_key:
            _report_failures(resp, "collection")
            raise click.ClickException(f"Failed to create collection '{name}'")
        col_map[old] = new_key
        existing[(new_parent, name)] = new_key
        click.echo(f"  + collection '{name}' ({new_key})")
    return col_map


# --------------------------------------------------------------------------- item copy
def _gather_items(src, to_copy, col_map):
    """Unique top-level items across all copied collections, with remapped memberships.

    Returns (items_by_key, membership), membership mapping item key -> list of *new*
    collection keys (handles items belonging to several copied collections).
    """
    items_by_key, found_in = {}, defaultdict(set)
    for old_col in to_copy:
        for it in _paginate(src.collection_items_top, old_col):
            k = it["data"]["key"]
            items_by_key.setdefault(k, it)
            found_in[k].add(old_col)

    membership = {}
    for k, it in items_by_key.items():
        old_cols = {c for c in it["data"].get("collections", []) if c in col_map} | found_in[k]
        membership[k] = [col_map[c] for c in old_cols if c in col_map]
    return items_by_key, membership


def _already_copied(tgt, new_collection_keys, src_ref):
    """{source_key: target_key} for items already present in the target collections."""
    mapping = {}
    for col in set(new_collection_keys):
        for it in _paginate(tgt.collection_items_top, col):
            for sk in _sameas_keys(it["data"].get("relations"), src_ref):
                mapping[sk] = it["data"]["key"]
    return mapping


def _copy_items(src, tgt, items_by_key, membership, col_map, src_ref, skip_existing, dry_run):
    """Create (or locate) target items. Returns (item_map, created, skipped).

    item_map maps EVERY copied source item key -> its target key, including items that
    already existed (so the child phase can top up their notes/files without duplicating
    the parent record).
    """
    already = (
        _already_copied(tgt, set(col_map.values()), src_ref)
        if (skip_existing and not dry_run)
        else {}
    )

    item_map = {}
    to_create, skipped, attach_top = [], 0, 0
    for k, it in items_by_key.items():
        if it["data"].get("itemType") == "attachment":
            attach_top += 1  # standalone top-level attachment -> not handled (see copy --help)
            continue
        if k in already:
            item_map[k] = already[k]  # reuse existing record; children may still be topped up
            skipped += 1
            continue
        to_create.append((k, _clean_item(it["data"], membership[k], src_ref)))

    if attach_top:
        click.echo(f"  · skipping {attach_top} standalone top-level attachment(s) "
                   f"(not supported; attach PDFs to a parent item instead)")

    if dry_run:
        click.echo(f"  · would create {len(to_create)} item(s); {skipped} already present")
        return {}, 0, skipped

    created = 0
    for batch in _chunks(to_create):
        resp = tgt.create_items([d for _, d in batch])
        smap = _success_map(resp)
        for idx, new_key in smap.items():
            item_map[batch[idx][0]] = new_key
        created += len(smap)
        _report_failures(resp, "item")
    return item_map, created, skipped


# --------------------------------------------------------------------------- child copy
def _copy_children(src, tgt, item_map, src_ref, with_notes, with_files, skip_existing):
    """Top up child notes and/or file attachments under each copied parent.

    Runs for every item in item_map (newly created AND pre-existing), so notes/files can be
    added to an already-copied collection on a later run. ALL reads (source children, and the
    existing target children used for de-duplication) happen up front, before ANY writes: a
    pyzotero client object does not tolerate interleaving paginated reads with writes, and
    doing so was causing missed de-dup scans (hence duplicate notes). De-duplication is by
    owl:sameAs provenance for notes and by filename (within the parent) for attachments.
    """
    src_children = {old_k: _paginate(src.children, old_k) for old_k in item_map}

    existing = {}
    if skip_existing:
        for old_k, new_k in item_map.items():
            seen_sameas, seen_files = set(), set()
            for ch in _paginate(tgt.children, new_k):
                cd = ch["data"]
                seen_sameas |= _sameas_keys(cd.get("relations"), src_ref)
                if cd.get("itemType") == "attachment":
                    seen_files.add(cd.get("filename") or cd.get("title") or "")
            existing[old_k] = (seen_sameas, seen_files)

    notes_made = files_made = files_skipped = 0
    for old_k, new_k in item_map.items():
        seen_sameas, seen_files = existing.get(old_k, (set(), set()))
        children = src_children[old_k]

        if with_notes:
            notes = [
                _clean_child(ch["data"], src_ref)
                for ch in children
                if ch["data"].get("itemType") == "note"
                and ch["data"]["key"] not in seen_sameas
            ]
            for batch in _chunks(notes):
                resp = tgt.create_items(batch, parentid=new_k)
                notes_made += len(_success_map(resp))
                _report_failures(resp, "note")

        if with_files:
            for ch in children:
                cd = ch["data"]
                if cd.get("itemType") != "attachment":
                    continue
                name = cd.get("filename") or cd.get("title") or cd["key"]
                if cd["key"] in seen_sameas or name in seen_files:
                    files_skipped += 1
                    continue
                try:
                    if cd.get("linkMode") in ("imported_file", "imported_url"):
                        # dump() returns None in some pyzotero versions; fetch bytes via file()
                        with tempfile.TemporaryDirectory() as td:
                            path = os.path.join(td, name.replace("/", "_"))
                            with open(path, "wb") as fh:
                                fh.write(src.file(cd["key"]))
                            res = tgt.attachment_simple([path], parentid=new_k)
                        files_made += _count_uploads(res, name)
                    else:  # linked_url / linked_file: recreate the link item, no bytes
                        resp = tgt.create_items([_clean_child(cd, src_ref)], parentid=new_k)
                        files_made += len(_success_map(resp))
                except Exception as exc:  # noqa: BLE001 - report and keep going
                    click.echo(f"  ! attachment '{name}' failed: {exc}", err=True)
    return notes_made, files_made, files_skipped


# --------------------------------------------------------------------------- CLI
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """Copy Zotero collections between libraries (user <-> group, group <-> group).

    Credentials are read from the environment (loaded by direnv from .env), so run every
    command through direnv + uv:

        direnv exec . uv run zot_coll_copy.py <command>

    Required env vars: ZOTERO_LIBRARY_ID (your personal/user id) and ZOTERO_API_KEY (a key
    with READ on the source and WRITE on the target -- grant group access at
    zotero.org/settings/keys).

    Typical workflow:

        ... list-groups                                  # find a group library id
        ... list-collections --from group:6598607        # find source collection keys
        ... copy KEY1 KEY2 --to group:6598607 --dry-run  # preview, write nothing
        ... copy KEY1 KEY2 --to group:6598607            # do it
    """


@cli.command("list-groups")
def list_groups():
    """List group libraries this API key can access (find a group library id here).

    Note: a private group only appears once the key has been granted access to it.
    """
    for g in _account().groups():
        d = g["data"]
        click.echo(
            f"{d['id']}\t{d['name']}"
            f"\t(libraryEditing={d.get('libraryEditing')}, fileEditing={d.get('fileEditing')})"
        )


@cli.command("list-collections")
@click.option("--from", "from_", default="user", metavar="SPEC",
              help="Library to list: user | user:<id> | group:<id> (default: user).")
def list_collections(from_):
    """Show a library's collections as an indented tree.

    The leading 8-character key on each line is what you pass to `copy`. Use --from to browse
    a group library (e.g. `--from group:6598607`) so you can copy *out* of a group.
    """
    src = _client(_parse_ref(from_))
    full = {c["data"]["key"]: c for c in _paginate(src.collections)}
    kids, roots = defaultdict(list), []
    for k, c in full.items():
        parent = c["data"].get("parentCollection")
        (kids[parent] if parent else roots).append(k)

    def walk(k, depth):
        d = full[k]["data"]
        n = full[k].get("meta", {}).get("numItems", "?")
        click.echo(f"{'  ' * depth}{d['key']}  {d['name']}  ({n} items)")
        for child in sorted(kids[k], key=lambda x: full[x]["data"]["name"].lower()):
            walk(child, depth + 1)

    for r in sorted(roots, key=lambda x: full[x]["data"]["name"].lower()):
        walk(r, 0)


@cli.command()
@click.argument("collection_keys", nargs=-1)
@click.option("--from", "from_", default="user", metavar="SPEC",
              help="Source library: user | user:<id> | group:<id> (default: user).")
@click.option("--to", "to_spec", metavar="SPEC", default=None,
              help="Target library: user | user:<id> | group:<id>.")
@click.option("--to-group", metavar="GROUP_ID", default=None,
              help="Deprecated alias for --to group:<id>.")
@click.option("--all", "copy_all", is_flag=True, help="Copy every collection in the source library.")
@click.option("--as", "as_name", metavar="NAME", default=None,
              help="Rename the single copied collection to NAME (errors if >1 key or --all).")
@click.option("--rename", "rename_opt", metavar="KEY=NAME", multiple=True,
              help="Rename source collection KEY to NAME in the target (repeatable).")
@click.option("--recursive/--no-recursive", default=True, help="Include sub-collections (default: yes).")
@click.option("--with-notes/--no-notes", default=True, help="Copy child notes (default: yes).")
@click.option("--with-files", is_flag=True, help="Also download+upload file attachments (uses target storage).")
@click.option("--skip-existing/--no-skip-existing", default=True, help="Make re-runs idempotent (default: yes).")
@click.option("--dry-run", is_flag=True, help="Show what would happen without writing anything.")
@click.option("--yes", "-y", is_flag=True, help="Skip the confirmation prompt.")
def copy(collection_keys, from_, to_spec, to_group, copy_all, as_name, rename_opt,
         recursive, with_notes, with_files, skip_existing, dry_run, yes):
    """Copy COLLECTION_KEYS (or --all) from the source library into the target library.

    Direction is set by --from (default: your personal `user` library) and --to, each a
    library spec: `user`, `user:<id>`, or `group:<id>`. So user->group, group->user and
    group->group all work; copying a library onto itself is refused.

    Items are deep-copied: Zotero keys are per-library, so this recreates them in the target
    (a copy, not a move). Tags, creators and the `extra` field -- including Better BibTeX
    citation keys -- are preserved. Sub-collections and child notes come along by default;
    file attachments only with --with-files (they consume the TARGET's storage quota and use
    pyzotero's beta upload API; HTML snapshots transfer imperfectly, as zips).

    Renaming: --as NAME renames the single collection being copied; --rename KEY=NAME renames
    specific collections (repeatable, works on sub-collections too). Unlisted collections keep
    their source names.

    Safe, incremental re-runs (default --skip-existing): every copy carries a hidden
    `owl:sameAs` relation back to its source item, existing target collections are reused by
    (target) name, and already-copied items are reused rather than duplicated. A re-run also
    TOPS UP whatever is newly requested or present -- e.g. adding --with-files on a later run
    uploads PDFs onto already-copied items WITHOUT creating duplicate records. File
    de-duplication is by filename within each parent item.

    Standalone attachments sitting directly in a collection (no parent item) are not copied;
    attach files to a bibliographic item instead.

    Examples:

        ... copy Q8FKSMLQ --to group:6598607 --dry-run
        ... copy Q8FKSMLQ --to group:6598607 --as 4d_data
        ... copy AAAAAAAA BBBBBBBB --to group:6598607 --rename AAAAAAAA="Renamed"
        ... copy CCCCCCCC --from group:6598607 --to user             # group -> personal
        ... copy DDDDDDDD --from group:111 --to group:222 --with-files
    """
    if not collection_keys and not copy_all:
        raise click.ClickException("Give one or more collection keys, or pass --all.")

    if to_group and not to_spec:
        to_spec = f"group:{to_group}"
    if not to_spec:
        raise click.ClickException("Specify a target with --to (e.g. --to group:6598607).")

    src_ref = _parse_ref(from_)
    tgt_ref = _parse_ref(to_spec)
    if src_ref == tgt_ref:
        raise click.ClickException(
            f"Source and target are the same library ({src_ref[0]}:{src_ref[1]}); "
            "same-library duplication isn't supported."
        )
    src, tgt = _client(src_ref), _client(tgt_ref)

    # Permission pre-check + labels via a single account client.
    acct = _account()
    access = acct.key_info().get("access", {})
    groups_by_id = {str(g["data"]["id"]): g["data"]["name"] for g in acct.groups()}
    if not _can(access, tgt_ref, "write"):
        raise click.ClickException(
            f"API key lacks WRITE access to {_ref_label(tgt_ref, groups_by_id)}. "
            "Grant it at https://www.zotero.org/settings/keys."
        )
    if not _can(access, src_ref, "read"):
        click.echo(
            f"! Warning: key may lack read access to {_ref_label(src_ref, groups_by_id)} "
            "— reads may fail (ok if it's a public library).", err=True
        )

    by_key = _collections_by_key(src)
    if copy_all:
        seeds = set(by_key)
    else:
        unknown = [k for k in collection_keys if k not in by_key]
        if unknown:
            raise click.ClickException(f"Unknown collection key(s): {', '.join(unknown)}")
        seeds = set(collection_keys)
    to_copy = _descendants(seeds, by_key) if recursive else seeds

    rename = {}
    for spec in rename_opt:
        k, sep, nm = spec.partition("=")
        k, nm = k.strip(), nm.strip()
        if not sep or not nm:
            raise click.ClickException(f"--rename expects KEY=NewName, got {spec!r}.")
        rename[k] = nm
    if as_name is not None:
        if copy_all or len(collection_keys) != 1:
            raise click.ClickException(
                "--as only works when copying exactly one collection key "
                "(use --rename KEY=NAME for multiple)."
            )
        rename[collection_keys[0]] = as_name
    stray = [k for k in rename if k not in to_copy]
    if stray:
        click.echo(f"! Warning: rename key(s) not in the copy set: {', '.join(stray)}", err=True)

    click.echo(f"Copy: {_ref_label(src_ref, groups_by_id)} -> {_ref_label(tgt_ref, groups_by_id)}")
    click.echo(
        f"Collections to copy: {len(to_copy)}"
        + ("  [DRY RUN]" if dry_run else "")
        + f"  notes={'on' if with_notes else 'off'} files={'on' if with_files else 'off'}"
        + f" skip-existing={'on' if skip_existing else 'off'}"
        + (f" rename={len(rename)}" if rename else "")
    )
    if not dry_run and not yes:
        click.confirm("Proceed?", abort=True)

    col_map = _ensure_collections(tgt, to_copy, by_key, rename, reuse=skip_existing, dry_run=dry_run)
    items_by_key, membership = _gather_items(src, to_copy, col_map)
    item_map, created, skipped = _copy_items(
        src, tgt, items_by_key, membership, col_map, src_ref, skip_existing, dry_run
    )

    notes_made = files_made = files_skipped = 0
    if item_map and (with_notes or with_files):
        notes_made, files_made, files_skipped = _copy_children(
            src, tgt, item_map, src_ref, with_notes, with_files, skip_existing
        )

    click.echo(
        "\nDone."
        + f" collections={len(col_map)}"
        + f" items:+{created}/skip{skipped}"
        + (f" notes:+{notes_made}" if with_notes else "")
        + (f" files:+{files_made}/skip{files_skipped}" if with_files else "")
    )


if __name__ == "__main__":
    cli()
