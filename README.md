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

The repository also contains a small standalone utility,
`zot_coll_copy.py` (a Zotero collection copier between personal and group
libraries, in any direction); its
documentation is in the command `--help` output, e.g.
`direnv exec . uv run zot_coll_copy.py --help`.
