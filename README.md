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

Decisions as of 2026-11-20. Zotero is the only source of bibliographic data;
no bibliography file is edited by hand.

- **The reference tools are run from the livingthing checkout, not copied
  here.** `ref-cite` and `zotero-export-bibs` live in `~/Source/livingthing`
  (the blog). Together with the modules they import they come to about 5,000
  lines, and a copy would have to be kept in step by hand. Both work on files
  outside the blog, which was tested on this repository before deciding. If
  someone without a livingthing checkout needs them, the move is to extract them
  into a package of their own that both repositories depend on; copying the
  code here, or declaring the blog as a dependency, are both ruled out.
- **Notes cite by inline link.** A draft under `_notes/` cites each source as a
  hyperlink to its DOI or arXiv page, with citation-shaped link text such as
  `[Segal (1999)](https://doi.org/…)`. That is the form `ref-cite` reads.
- **Ingest with `ref-cite`.** It resolves each link to metadata, creates the
  items in a Zotero collection, and with `-i` rewrites the links in place as
  `[@citekey]`. It reads `.md` and `.qmd` alike. Dry-run first:

  ```sh
  direnv exec ~/Source/livingthing uv run --project ~/Source/livingthing ref-cite _notes/<slug>/draft.md -c <collection> --dry-run --unresolved-report ""
  ```

  Drop `--dry-run` to write to Zotero; add `-i` to rewrite the links, which
  needs Zotero running with Better BibTeX. `direnv exec ~/Source/livingthing`
  supplies the blog's credentials and translation-server settings; this
  repository's own `.env` is not used. Check the dry-run listing for wrong
  metadata (a reprint's editors in place of the author, a revision date in place
  of the publication date) and fix those items in Zotero afterwards.
- **Items go into the personal library unless `--library` names a group.**
  Both tools address "My Library" by default and take
  `--library group:<id-or-name>`, the group's numeric id or its exact name, to
  read from and write to a group library instead. A top-level `<slug>.qmd` can
  say it once in its frontmatter with `zotlibrary: group:<id-or-name>`, beside
  `zotcollpath`: `zotero-export-bibs <slug>.qmd` and `ref-cite -f <slug>.qmd`
  then use that group, and the flag overrides the frontmatter. A draft under
  `_notes/` has no frontmatter, so pass the flag. The group has to be synced
  into the running Zotero. `zot_coll_copy.py` (below) is now needed only to move
  a collection that already exists from one library to another.
- **One Zotero collection per essay,** named after the essay's slug unless the
  frontmatter says otherwise with `zotcollpath`.
- **Bibliographies will be per-document YAML, exported from Zotero.** When a
  draft is written up as a top-level `<slug>.qmd`, run from the repository root:

  ```sh
  uv run --project ~/Source/livingthing zotero-export-bibs <slug>.qmd
  ```

  This needs Zotero running with Better BibTeX and no credentials. It writes
  `<slug>.yaml` beside the post, sets `bibliography`, `csl: minimalist.csl`,
  `link-citations`, `nocite: '@*'` and `reference-section-title` in the
  frontmatter, and appends a `## References` section if there is none. With
  `nocite: '@*'` the reference list shows the whole collection, cited or not.
  **Always name the file.** Run bare, it globs every `.qmd` in the tree, and for
  a post whose collection does not exist it strips the bibliography keys from
  the frontmatter. It handles `.qmd` only and skips `_`-prefixed folders, so it
  never touches `_notes/`.
- **`references.bib` is a leftover.** The `bibliography: references.bib` line in
  `_quarto.yml` belongs to an earlier plan; the file no longer exists. It comes
  out when the first essay moves to per-document YAML.
- **The `dan-lit-search` skill is not installed here.** It lives in the blog's
  `.claude/skills/`. The two commands above are what it would run.

The repository also contains a small standalone utility,
`zot_coll_copy.py` (a Zotero collection copier between personal and group
libraries, in any direction); its
documentation is in the command `--help` output, e.g.
`direnv exec . uv run zot_coll_copy.py --help`.
