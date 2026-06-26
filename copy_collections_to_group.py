"""Copy Zotero collections from a personal library into a group library.

This is a deliberately specific tool: it deep-copies whole collections (their items, and
optionally child notes and file attachments) from your personal ("user") library into a
shared group library. Zotero keys are per-library, so items are *recreated* in the target
-- a copy, not a move.

Credentials come from the environment (loaded by direnv from .env), so run via direnv:

    direnv exec . uv run copy_collections_to_group.py <command> [options]

Required environment variables:
    ZOTERO_LIBRARY_ID   your personal ("user") library id
    ZOTERO_API_KEY      an API key with WRITE access to the target group
                        (grant per-group/all-group access at zotero.org/settings/keys)

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
            f"`direnv exec . uv run copy_collections_to_group.py ...` so .env is loaded."
        )


def _source():
    return zotero.Zotero(_env("ZOTERO_LIBRARY_ID"), "user", _env("ZOTERO_API_KEY"))


def _target(group_id):
    return zotero.Zotero(str(group_id), "group", _env("ZOTERO_API_KEY"))


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
def _source_uri(uid, key):
    return f"http://zotero.org/users/{uid}/items/{key}"


def _sameas_keys(relations, uid):
    """Source item keys recorded in an owl:sameAs relation (value may be a str or a list)."""
    val = (relations or {}).get("owl:sameAs")
    if not val:
        return set()
    vals = val if isinstance(val, list) else [val]
    prefix = _source_uri(uid, "")
    return {v[len(prefix):] for v in vals if isinstance(v, str) and v.startswith(prefix)}


# --------------------------------------------------------------------------- item transforms
def _clean_item(data, new_collection_keys, uid):
    """Strip per-library fields, remap collections, stamp owl:sameAs provenance."""
    d = dict(data)
    old_key = d.get("key")
    for f in STRIP_FIELDS:
        d.pop(f, None)
    d["relations"] = {"owl:sameAs": _source_uri(uid, old_key)}
    d["collections"] = list(new_collection_keys)
    return d


def _clean_child(data, uid):
    """Prepare a child note/attachment for recreation under a new parent (via parentid)."""
    d = dict(data)
    old_key = d.get("key")
    for f in STRIP_FIELDS:
        d.pop(f, None)
    d.pop("parentItem", None)
    d["relations"] = {"owl:sameAs": _source_uri(uid, old_key)}
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


def _ensure_collections(tgt, to_copy, by_key, reuse, dry_run):
    """Recreate the collection subtree in the target, parents first.

    Returns old_collection_key -> new_collection_key. With `reuse`, an existing target
    collection with the same name under the same (mapped) parent is reused, not duplicated.
    """
    existing = {}
    if reuse and not dry_run:
        for c in _paginate(tgt.collections):
            d = c["data"]
            existing[(d.get("parentCollection") or None, d["name"])] = d["key"]

    col_map = {}
    for old in sorted(to_copy, key=lambda k: _depth(k, by_key)):
        name = by_key[old]["name"]
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


def _already_copied(tgt, new_collection_keys, uid):
    """{source_key: target_key} for items already present in the target collections."""
    mapping = {}
    for col in set(new_collection_keys):
        for it in _paginate(tgt.collection_items_top, col):
            for sk in _sameas_keys(it["data"].get("relations"), uid):
                mapping[sk] = it["data"]["key"]
    return mapping


def _copy_items(src, tgt, items_by_key, membership, col_map, uid, skip_existing, dry_run):
    """Create (or locate) target items. Returns (item_map, created, skipped).

    item_map maps EVERY copied source item key -> its target key, including items that
    already existed (so the child phase can top up their notes/files without duplicating
    the parent record).
    """
    already = (
        _already_copied(tgt, set(col_map.values()), uid)
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
        to_create.append((k, _clean_item(it["data"], membership[k], uid)))

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
def _copy_children(src, tgt, item_map, uid, with_notes, with_files, skip_existing):
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
                seen_sameas |= _sameas_keys(cd.get("relations"), uid)
                if cd.get("itemType") == "attachment":
                    seen_files.add(cd.get("filename") or cd.get("title") or "")
            existing[old_k] = (seen_sameas, seen_files)

    notes_made = files_made = files_skipped = 0
    for old_k, new_k in item_map.items():
        seen_sameas, seen_files = existing.get(old_k, (set(), set()))
        children = src_children[old_k]

        if with_notes:
            notes = [
                _clean_child(ch["data"], uid)
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
                        resp = tgt.create_items([_clean_child(cd, uid)], parentid=new_k)
                        files_made += len(_success_map(resp))
                except Exception as exc:  # noqa: BLE001 - report and keep going
                    click.echo(f"  ! attachment '{name}' failed: {exc}", err=True)
    return notes_made, files_made, files_skipped


# --------------------------------------------------------------------------- CLI
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """Copy Zotero collections from your personal library into a group library.

    Credentials are read from the environment (loaded by direnv from .env), so run every
    command through direnv + uv:

        direnv exec . uv run copy_collections_to_group.py <command>

    Required env vars: ZOTERO_LIBRARY_ID (your personal/user id) and ZOTERO_API_KEY (a key
    with WRITE access to the target group -- grant it at zotero.org/settings/keys).

    Typical workflow:

        ... list-groups                              # find the target group id
        ... list-collections                         # find the collection keys to copy
        ... copy KEY1 KEY2 --to-group GID --dry-run  # preview, write nothing
        ... copy KEY1 KEY2 --to-group GID            # do it
    """


@cli.command("list-groups")
def list_groups():
    """List group libraries this API key can access (find the target group id here).

    Note: a private group only appears once the key has been granted access to it.
    """
    for g in _source().groups():
        d = g["data"]
        click.echo(
            f"{d['id']}\t{d['name']}"
            f"\t(libraryEditing={d.get('libraryEditing')}, fileEditing={d.get('fileEditing')})"
        )


@cli.command("list-collections")
def list_collections():
    """Show your personal-library collections as an indented tree.

    The leading 8-character key on each line is what you pass to `copy`.
    """
    src = _source()
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
@click.option("--to-group", required=True, metavar="GROUP_ID", help="Target group library id.")
@click.option("--all", "copy_all", is_flag=True, help="Copy every collection in the personal library.")
@click.option("--recursive/--no-recursive", default=True, help="Include sub-collections (default: yes).")
@click.option("--with-notes/--no-notes", default=True, help="Copy child notes (default: yes).")
@click.option("--with-files", is_flag=True, help="Also download+upload file attachments (uses group storage).")
@click.option("--skip-existing/--no-skip-existing", default=True, help="Make re-runs idempotent (default: yes).")
@click.option("--dry-run", is_flag=True, help="Show what would happen without writing anything.")
@click.option("--yes", "-y", is_flag=True, help="Skip the confirmation prompt.")
def copy(collection_keys, to_group, copy_all, recursive, with_notes, with_files, skip_existing, dry_run, yes):
    """Copy COLLECTION_KEYS (or --all) into the target group library.

    Items are deep-copied: Zotero keys are per-library, so this recreates them in the group
    (a copy, not a move). Tags, creators and the `extra` field -- including Better BibTeX
    citation keys -- are preserved. Sub-collections and child notes come along by default;
    file attachments only with --with-files (they consume the group's storage quota and use
    pyzotero's beta upload API; HTML snapshots transfer imperfectly, as zips).

    Safe, incremental re-runs (default --skip-existing): every copy carries a hidden
    `owl:sameAs` relation back to its source item, existing target collections are reused by
    name, and already-copied items are reused rather than duplicated. Crucially, a re-run
    also TOPS UP whatever is newly requested or newly present -- e.g. adding --with-files on
    a second run uploads the PDFs onto the already-copied items WITHOUT creating duplicate
    records, and notes added in the source since the last run get synced. File
    de-duplication is by filename within each parent item.

    Standalone attachments sitting directly in a collection (no parent item) are not copied;
    attach files to a bibliographic item instead.

    Examples:

        ... copy Q8FKSMLQ --to-group 6598607 --dry-run
        ... copy Q8FKSMLQ ZLDYV7BR --to-group 6598607
        ... copy --all --to-group 6598607 --with-files
    """
    if not collection_keys and not copy_all:
        raise click.ClickException("Give one or more collection keys, or pass --all.")

    src = _source()
    tgt = _target(to_group)
    uid = _env("ZOTERO_LIBRARY_ID")

    gname = next((g["data"]["name"] for g in src.groups() if str(g["data"]["id"]) == str(to_group)), None)
    if gname is None:
        click.echo(f"! Warning: group {to_group} not visible to this API key — writes may fail.", err=True)

    by_key = _collections_by_key(src)
    if copy_all:
        seeds = set(by_key)
    else:
        unknown = [k for k in collection_keys if k not in by_key]
        if unknown:
            raise click.ClickException(f"Unknown collection key(s): {', '.join(unknown)}")
        seeds = set(collection_keys)
    to_copy = _descendants(seeds, by_key) if recursive else seeds

    click.echo(f"Target group: {to_group} ({gname or 'unknown'})")
    click.echo(
        f"Collections to copy: {len(to_copy)}"
        + ("  [DRY RUN]" if dry_run else "")
        + f"  notes={'on' if with_notes else 'off'} files={'on' if with_files else 'off'}"
        + f" skip-existing={'on' if skip_existing else 'off'}"
    )
    if not dry_run and not yes:
        click.confirm("Proceed?", abort=True)

    col_map = _ensure_collections(tgt, to_copy, by_key, reuse=skip_existing, dry_run=dry_run)
    items_by_key, membership = _gather_items(src, to_copy, col_map)
    item_map, created, skipped = _copy_items(
        src, tgt, items_by_key, membership, col_map, uid, skip_existing, dry_run
    )

    notes_made = files_made = files_skipped = 0
    if item_map and (with_notes or with_files):
        notes_made, files_made, files_skipped = _copy_children(
            src, tgt, item_map, uid, with_notes, with_files, skip_existing
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
