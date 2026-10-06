# notes_on_agency

Quarto **website** (blog) on mechanized causal graphs, decision theory, and agency (MacDermott et al. framing). Output: HTML with Hypothesis annotations. Output dir: `_site/`.

Each topic is a post: a top-level `<slug>.qmd` at the repo root (e.g. `decision-theories.qmd`). `index.qmd` is the listing/home page; project-wide settings (`bibliography`, `filters`, `format`) live in `_quarto.yml`. The listing auto-discovers root posts via `contents: ["*.qmd", "!index.qmd"]`, while `project.render` is limited to `*.qmd` so `CLAUDE.md`/`README.md` stay out of the site. To add a post: create `<slug>.qmd` at the repo root with `title`, `date`, `categories`, and `author` front-matter and it appears on the home page automatically.

## Diagram rendering — TikZ

Custom TikZ filter: `_extensions/danmackinlay/tikz/` ([danmackinlay/quarto_tikz](https://github.com/danmackinlay/quarto_tikz) v1.4.0, Lua-based).

**Usage pattern** (see `decision-theories.qmd`):

```qmd
::: {#fig-label .figure fig-align="center"}
```{.tikz}
%%| filename: label

\usetikzlibrary{bayesnet,positioning,fit}
\begin{tikzpicture}[scale=2, transform shape]
% ... TikZ code ...
\end{tikzpicture}
```
:::
```

- Code fence is `{.tikz}` — this is a Lua filter, not a knitr engine. No `r`/`python`.
- Figure label, caption, and alignment go on the outer `:::` div, not inside the block.
- **`%%| filename: <label>` is the canonical labeling syntax** and every block here
  uses it. The fence-attribute form (`{.tikz filename='label'}`) is the deprecated
  pre-1.0 spelling; if a block sets both, the `%%|` directive wins and the filter
  warns. Don't reintroduce the fence form.
- The label names the cache entry (`<label>.<short-hash>.svg`); it does **not**
  replace the hash. See the caching section below for what the hash keys on and
  why the label alone can't carry the cache identity.
- `\input{cid_styles}` pulls in the shared node styles (`latent`, `mechanism`, `decision`, `obsdecision`, `utility`) from `cid_styles.tex` at the **repo root** (beside `decision-theories.qmd`). The filter puts each source `.qmd`'s own directory on `TEXINPUTS`, so the styles file must live in the same directory as the post that uses it — *not* in the extension dir (a `quarto update` would clobber it). If posts ever move into subdirectories, keep `cid_styles.tex` beside them, or promote it to a preamble via the filter's `tikz: tex-template:` option.

**bayesnet library** — key commands for causal graphs:
- `\node[obs] (X) {$X$}` — observed variable (shaded circle)
- `\node[latent] (W) {$W$}` — latent variable (open circle); redefine style if needed: `\tikzstyle{latent}=[circle, draw, thick, minimum size=1cm]`
- `\edge {A} {B}` — directed edge A → B
- `\plate {name} {(node1)(node2)} {label}` — plate notation

**Rendering pipeline:** pdflatex → SVG via `pdftocairo`. Configured in `_quarto.yml` under `tikz:`.

### Cache is committed — contributors do not need LaTeX

`cache-dir: .tikz-cache` (project-relative, *not* the filter's default
`~/.cache/tikz-diagram-filter/`) and `.tikz-cache/` is deliberately **not**
gitignored. The rendered SVGs are checked in, so `quarto render` succeeds with
no TeX toolchain at all — verified by rendering the whole site with `pdflatex`,
`inkscape`, `dvisvgm` and `pdftocairo` all absent from `PATH`.

Consequences to respect:

- **`tex-engine` and `svg-engine` are pinned explicitly in `_quarto.yml`.** The
  cache key is `sha1(block source .. stringify(options))` and those engine names
  are folded into the options. Leaving them to the filter's defaults would mean
  an upstream default change silently invalidates every committed entry. Don't
  un-pin them, and don't change them casually — either invalidates all 8 files.
- **Editing a `.tikz` block or `cid_styles.tex` requires LaTeX**, because it
  changes the cache key. After editing, re-render *with* TeX and commit the new
  `.tikz-cache/*.svg` alongside the `.qmd` change. Stale entries are not
  garbage-collected; delete the orphan by hand.
- On a cache miss without TeX the render does **not** hard-fail: the affected
  figure is dropped and Quarto logs
  `ERROR … pdflatex not found on PATH`. Loud, but non-fatal — check the log.
- **The label is not a substitute for the hash.** `%%| filename:` sets only the
  `<label>` prefix of `<label>.<short-hash>.svg`; it never feeds the hash. Making
  entries `<label>.svg` outright would drop the staleness check: editing a block
  on a TeX-less machine would then *silently* serve the previous diagram, instead
  of the current loud miss. Stable filenames would need the cache key stored
  inside the file and verified on read — an upstream change to `quarto_tikz`,
  not something configurable here.
- This is upstream's documented "cached deployment to a build host without
  TeX/Inkscape" recipe; the extension README carries the same workflow.

### Why `pdftocairo` and not `dvisvgm`

`dvisvgm` produces a **41% smaller** cache (109 KB vs 185 KB across the 8
diagrams, measured) because it consumes the DVI directly and embeds fonts as WOFF
instead of outlining every glyph to a path. Measured, rendered, and visually
verified — then **rejected**. Two reasons:

- Its headline advantage does not apply here. Quarto embeds these diagrams as
  `<img src="….svg">`, which renders SVG in *secure static mode*: the text inside
  is unreachable from the page DOM, so it is neither selectable nor findable with
  the browser's search, and screen readers do not read into it. Verified in a
  browser — `img.contentDocument` is null and the page text contains none of the
  node labels. dvisvgm's real `<text>` elements buy nothing through an `<img>`.
- What remains is ~76 KB across the whole site, against re-coupling the build to
  a separate `brew` formula — the one that was silently broken here until
  2026-08-17 (see below). `brew`'s `texlive` does *not* bundle `dvisvgm`, so on
  this machine it stays a distinct dependency.

`pdftocairo` is pure poppler, needs no TeX integration at all, and is present on
both a brew macOS box and the `ubuntu-latest` GH Actions runner. If the figures
ever become inline `<svg>` rather than `<img>` (Quarto's `embed-resources`, or a
filter change), re-run this comparison — the accessibility argument would then
become real and would likely flip the decision.

**Historical note, since the failure is confusing if you meet it again.** Homebrew's
`dvisvgm` before `3.6.1_1` could not read a brew-installed TeX Live at all:

- `dvisvgm` links kpathsea, which finds `texmf.cnf` by walking up from the
  *resolved* path of the running binary (`$SELFAUTOLOC` → `$SELFAUTODIR` → …).
  The brew formula installs to its own Cellar prefix, so that walk never reaches
  TeX Live → `kpathsea: configuration file texmf.cnf not found`. Symlinking does
  not help: kpathsea resolves symlinks *before* walking, which is exactly why
  `/opt/homebrew/bin/pdflatex` works — it resolves into `Cellar/texlive/<ver>/bin/`.
- Setting `TEXMFCNF` alone is **not** enough, because brew also patches
  `texmf.cnf` itself — line 62 reads `TEXMFROOT = $SELFAUTODIR/share` where
  upstream TeX Live has `$SELFAUTOPARENT`. The file is then found but every tree
  still resolves against `dvisvgm`'s own prefix, giving
  `WARNING: none of the default map files could be found` and missing `.pro`
  prologues. Both `TEXMFCNF` and `TEXMFROOT` are required.

homebrew-core fixed this on 2026-08-17 ("dvisvgm: point kpathsea at texlive",
`revision 1`) by moving the binary to `libexec/` and wrapping `bin/dvisvgm` in a
`write_env_script` that sets both variables. `3.6.1_1` therefore works with no
configuration — the failure above is history, not a live constraint. It is simply
not worth adopting, for the reasons above.

### Why not TikZJax

`renderer: tikzjax` (browser WebAssembly, no LaTeX at read time) is a supported
option of the filter and **does not work for this project**. TikZJax ships a
fixed TeX filesystem; unpacking its dump shows `bayesnet` is absent (only the
stock libraries — `positioning`, `fit`, `shapes.*`, `calc`, … — are bundled).
Every diagram here depends on `bayesnet` for `\edge`, `\plate` and the `obs`
style, and on `\input{cid_styles}`, which cannot resolve in a browser at all.
The blocks silently emit nothing. Adopting it would mean hand-writing a
`\edge`/`\plate` shim, inlining `cid_styles` into every block, a ~10 MB WASM
download per reader, and no non-HTML output. Not worth it; the committed cache
solves the same problem with none of the cost.

## Execution / freeze

`execute: freeze: true` in `_quarto.yml` — all cell outputs are cached. To regenerate: delete `_freeze/` directory or run `quarto render --no-cache`.

## Bibliography

`references.bib` is autogenerated by Zotero — **never edit directly**. To add a reference, use the `dan-lit-search` skill (uploads to Zotero first, which syncs the bib). Cite as `[@CitationKey]`.

## Build

```sh
quarto preview          # live website preview
quarto render           # render site → _site/
quarto render --to html # single format
```
