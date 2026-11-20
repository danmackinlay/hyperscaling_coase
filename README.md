# notes_on_agency

A Quarto **website** (blog) on mechanized causal graphs, decision theory, and agency
(MacDermott et al. framing). Each topic is a top-level `<name>.qmd`. See `CLAUDE.md` for
build and authoring specifics.

## Building without a TeX install

`quarto render` and `quarto preview` work with **no LaTeX on your machine**. The
TikZ diagrams are pre-rendered to SVG and the results are committed under
`.tikz-cache/`; the diagram filter reads them straight from there.

You only need TeX (plus `pdftocairo`) if you *change the source of a diagram* —
i.e. edit a ```` ```{.tikz} ```` block or `cid_styles.tex`. Editing prose,
adding posts, or changing anything else never touches the cache. If you do edit
a diagram without TeX installed, the render still completes, but that one figure
is dropped and Quarto prints a loud
`ERROR … pdflatex not found on PATH`. Either install TeX, or ask someone who has
it to re-render and commit the new `.tikz-cache/` entry.

On macOS the full toolchain is:

```sh
brew install --cask mactex-no-gui && brew install poppler
```

See `CLAUDE.md` for why the cache is committed rather than rendered on demand.

## Working notes (`_notes/`)

Essays here are worked out by several agents at once, each on its own line of
argument. Their working material lives under `_notes/`, apart from the site.

- **One folder per line of work:** `_notes/<slug>/`. The slug is a short
  snake_case name for the line of argument, with a round number when there has
  been more than one attempt, e.g. `_notes/constitutional_complexity_2/`. An
  agent starting a new line of work makes a new folder; it does not add files to
  another agent's folder.
- **Everything in `_notes/` is a note, and notes are `.md`**, full drafts
  included. A draft becomes a top-level `<slug>.qmd` only when it is being
  written up as the actual essay. Quarto renders top-level `*.qmd` only and
  skips `_`-prefixed folders, so nothing under `_notes/` reaches the site or the
  home-page listing.
- **Short file names; the folder carries the slug.** Standard names:

  | File | Purpose |
  |---|---|
  | `HANDOVER.md` | Entry point. What exists, what is verified, what is weak, what Dan has decided. Read this first; keep it current. |
  | `draft.md` | The current draft, if there is one. |
  | `brief_v<n>.md` | Briefs given to drafting agents, numbered in order and never edited after use. |
  | `check_<what>.py`, `sim_<what>.py` | Scripts, named for what they check or simulate. |

  Anything else (critiques, claim ledgers, red-team reports) gets a plain
  descriptive name in the same folder.
- **Scripts run without touching the project environment:** from the repository
  root, `uv run --no-project --with numpy --with scipy python _notes/<slug>/<script>.py`,
  listing whatever packages the script imports. `pyproject.toml` holds only what
  the site and `zot_coll_copy.py` need.
- **Moved files keep a paper trail.** When material is moved in from another
  repository, `HANDOVER.md` has a table mapping each file to its old path, since
  older notes will still refer to the old names.

## References and Zotero

Zotero is the only source of bibliographic data; no bibliography file is edited
by hand.

- **This repository's references live in the Zotero group `hyperscaling_coase`
  (groupID 6771791).** Every command below passes it explicitly, because the
  tools default to the personal library. Writes have not yet been tested
  against this group.
- **One Zotero collection per essay,** named after the essay's slug unless the
  frontmatter says otherwise with `zotcollpath`.
- **The reference tools are run from the livingthing checkout, not copied
  here.** `ref-cite` and `zotero-export-bibs` live in `~/Source/livingthing`.
  With the modules they import they come to about 5,000 lines, which a copy
  would have to keep in step by hand. If someone without a livingthing checkout
  needs them, extract them into a package both repositories depend on; don't
  copy the code here or declare the blog as a dependency.
  `direnv exec ~/Source/livingthing` supplies the blog's credentials and
  translation-server settings; this repository's own `.env` is not used.
- **Notes cite by inline link.** A draft under `_notes/` cites each source as a
  hyperlink to its DOI or arXiv page, with citation-shaped link text such as
  `[Segal (1999)](https://doi.org/…)`. That is the form `ref-cite` reads.
- **Ingest with `ref-cite`.** It resolves each link to metadata, creates the
  items in a Zotero collection, and with `-i` rewrites the links in place as
  `[@citekey]`. It reads `.md` and `.qmd` alike. Dry-run first:

  ```sh
  direnv exec ~/Source/livingthing uv run --project ~/Source/livingthing ref-cite _notes/<slug>/draft.md -c <collection> --library group:6771791 --dry-run --unresolved-report ""
  ```

  Drop `--dry-run` to write to Zotero; add `-i` to rewrite the links, which
  needs Zotero running with Better BibTeX. Check the dry-run listing for wrong
  metadata (a reprint's editors in place of the author, a revision date in place
  of the publication date) and fix those items in Zotero afterwards.
- **Bibliographies are per-document YAML, exported from Zotero.** When a draft
  is written up as a top-level `<slug>.qmd`, put `zotlibrary: group:6771791` in
  its frontmatter (beside `zotcollpath`, if any) so that both
  `zotero-export-bibs <slug>.qmd` and `ref-cite -f <slug>.qmd` use the group
  without a flag. Then, from the repository root:

  ```sh
  uv run --project ~/Source/livingthing zotero-export-bibs <slug>.qmd
  ```

  This needs Zotero running with Better BibTeX, with the group synced, and no
  credentials. It writes `<slug>.yaml` beside the post, sets `bibliography`,
  `csl: minimalist.csl`, `link-citations`, `nocite: '@*'` and
  `reference-section-title` in the frontmatter, and appends a `## References`
  section if there is none. With `nocite: '@*'` the reference list shows the
  whole collection, cited or not.
  **Always name the file.** Run bare, it globs every `.qmd` in the tree, and for
  a post whose collection does not exist it strips the bibliography keys from
  the frontmatter. It skips `_`-prefixed folders, so it never touches `_notes/`.
- **`zotero-cli` has no `--library` flag; set the library per command** with
  the group's environment variables, which override the stored config:

  ```sh
  direnv exec ~/Source/livingthing env ZOTERO_LIBRARY_ID=6771791 ZOTERO_LIBRARY_TYPE=group zotero-cli search "…"
  ```

  This is valid in both fish and POSIX shells. For a longer session in fish,
  `set -x ZOTERO_LIBRARY_ID 6771791; set -x ZOTERO_LIBRARY_TYPE group` scopes
  that shell instead. Don't use `zotero-cli library switch`: it lasts only for
  the command that runs it. Check which library a command will use with
  `zotero-cli config`.
- **`zot_coll_copy.py`** copies an existing collection between the personal
  library and a group, in either direction. See
  `direnv exec . uv run zot_coll_copy.py --help`.
- **`references.bib` is a leftover.** The `bibliography: references.bib` line in
  `_quarto.yml` belongs to an earlier plan; the file no longer exists. It comes
  out when the first essay moves to per-document YAML.
- **The `dan-lit-search` skill is not installed here.** It lives in the blog's
  `.claude/skills/`. The commands above are what it would run.
