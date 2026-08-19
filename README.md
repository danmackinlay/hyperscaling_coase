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

The repository also contains a small standalone utility,
`zot_coll_copy.py` (a Zotero collection copier between personal and group
libraries, in any direction); its
documentation is in the command `--help` output, e.g.
`direnv exec . uv run zot_coll_copy.py --help`.
