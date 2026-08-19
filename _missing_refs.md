# Reference ingestion — DONE (2026-08-19)

All 20 references below are now in Zotero, filed in collection
**`informational_empowerment`** (key `A7FVYJZ2`).

Note the collection differs from what this file originally specified
(`what_does_empowerment_approximate`) — Dan directed the ingest to
`informational_empowerment` instead.

Every identifier was verified before ingest: DOIs against CrossRef, arXiv IDs
against the arXiv API, ISBNs against Open Library. All four items this file
flagged as uncertain checked out — see "Verification outcomes" below.

**Never hand-edit `references.bib`.** Regenerate it from Zotero. The Zotero
local DB lags cloud writes, so poll for the new item count before exporting or
the bibliography comes out short.

## Translation table

Swap each `^[TODO cite: …]` footnote for the BibTeX key in column 2.

| # | Reference | BibTeX key | Zotero key | Status |
|---|---|---|---|---|
| 1 | Ashworth 1980, *Trench Warfare 1914–1918* | `Ashworth1980Trench` | `UGEHESE4` | new |
| 2 | Axelrod 1984, *The Evolution of Cooperation* | `Axelrod1984Evolution` | `WTIXGNQU` | already in library |
| 3 | Friedman 1971, "A Non-cooperative Equilibrium for Supergames" | `Friedman1971Noncooperative` | `RRU65IEX` | new |
| 4 | Fudenberg & Maskin 1986, "The Folk Theorem in Repeated Games…" | `Fudenberg1986Folk` | `KG4J5CD6` | already in library |
| 5 | Press & Dyson 2012, "Iterated Prisoner's Dilemma contains strategies…" | `Press2012Iterated` | `JP798UC5` | already in library |
| 6 | Dafoe et al. 2020, "Open Problems in Cooperative AI" | `Dafoe2020Open` | `W2PB2N25` | already in library |
| 7 | Salge & Polani 2017, "Empowerment as Replacement for the Three Laws…" | `salge2017empowerment` | `HQI7RGZG` | already in library |
| 8 | Du et al. 2020, "AvE: Assistance via Empowerment" | `Du2020AvE` | `JWP7M8XA` | already in library |
| 9 | Guckelsberger, Salge & Colton 2016, "…Coupled Empowerment Maximisation" | `Guckelsberger2016Intrinsically` | `TUGG35YH` | already in library |
| 10 | Myers et al. 2024, "Learning to Assist Humans without Inferring Rewards" | `Myers2024Learning` | `TUI8ZKPF` | new (PDF attached) |
| 11 | Ellis et al. 2025, "Training LLM Agents to Empower Humans" | `Ellis2025Training` | `GBSWCEFZ` | new (PDF attached) |
| 12 | Yang et al. 2025, "When Assisting One Disempowers Another" | `Yang2025When` | `VVMUZFNQ` | new (PDF attached) |
| 13 | Krakovna et al. 2018, "Penalizing Side Effects using Stepwise Relative Reachability" | `Krakovna2019Penalizing` | `HYL6JAIC` | already in library |
| 14 | Krakovna et al. 2020, "Avoiding Side Effects By Considering Future Tasks" | `Krakovna2020Avoiding` | `AHQTTXUZ` | already in library |
| 15 | Schelling 1960, *The Strategy of Conflict* | `Schelling1960Strategy` | `EG4447VN` | already in library |
| 16 | Elster 1979, *Ulysses and the Sirens* | `Elster1979Ulysses` | `TVU4VRX2` | new |
| 17 | Bratman 1987, *Intention, Plans, and Practical Reason* | `Bratman1987Intention` | `AM29PS3M` | new |
| 18 | Pattanaik & Xu 1990, "On Ranking Opportunity Sets…" | `Pattanaik1990Ranking` | `8695ZXAV` | new |
| 19 | Sen 1988, "Freedom of choice: Concept and content" | `Sen1988Freedom` | `IXTUX2RT` | new |
| 19b | Sen 1991, "Welfare, preference and freedom" | `Sen1991Welfare` | `BJ6H5NV7` | new (see note) |

### Traps in that table

- **`Krakovna2019Penalizing`, not `Krakovna2018`.** BetterBibTeX keyed the item
  off the arXiv v2 date (2019-03-08), not the v1 date this file cites it by.
- **`salge2017empowerment` is lower-case**, unlike every other key here — it
  predates the current BBT key format. Copy it verbatim.
- **`Du2020AvE` and `Krakovna2020Avoiding` are `@inproceedings`**, not
  `@misc` — they were ingested as NeurIPS papers, not preprints.

## Verification outcomes

Everything this file flagged as uncertain was checked and confirmed:

- **Guckelsberger DOI** — `10.1109/CIG.2016.7860406` resolves to the stated
  paper (IEEE CIG 2016). The guess was right.
- **Krakovna 2020 arXiv number** — `2010.07877` is indeed "Avoiding Side
  Effects By Considering Future Tasks". Right.
- **Ellis 2025 author list** — full list is Evan Ellis; Vivek Myers; Jens
  Tuyls; Sergey Levine; Anca Dragan; Benjamin Eysenbach. Zotero has it from
  arXiv, so nothing was ingested from memory.
- **Yang et al. v2 title** — "When Assisting One Disempowers Another" is
  correct for arXiv 2511.04177 (v2 dated 2026-07-06). Ingested under the v2
  title as instructed.

All other DOIs (Friedman, Fudenberg & Maskin, Press & Dyson, Salge & Polani,
Sen 1988) resolved to the stated works with the stated volume/page data.

### Metadata repaired after ingest

- **Sen 1988** — CrossRef returns the title truncated to "Freedom of choice";
  restored to "Freedom of choice: Concept and content".
- **Bratman 1987** — Open Library supplied a spurious `Nov 12, 1987` date and
  dropped the middle initial; now `1987` and `Michael E. Bratman`.

### Sen 1988 vs Sen 1991

Both were ingested, per this file's own instruction to do so if 1991 looked
like the better fit for the anti-cardinality argument. It is:

- **`Sen1991Welfare`** (*J. Econometrics* 50(1–2):15–29) is the direct reply to
  the cardinality axiomatization — the argument that an opportunity set's value
  cannot be preference-independent. Use this one against Pattanaik & Xu.
- **`Sen1988Freedom`** (*Eur. Econ. Review* 32(2–3):269–294) is the Alfred
  Marshall Lecture: broader, more programmatic, and the better cite if the
  prose wants the general concept-and-content framing rather than the specific
  rebuttal.

## Already in `references.bib` — do NOT re-ingest

`Franzmeyer2021Learning`, `Turner2021Optimal`, the Everitt reward-tampering
pair, `Williams2010Nonnegative`.

## Remaining work — DONE (2026-08-19)

- ~~Swap the `^[TODO cite: …]` footnotes~~ — all 19 footnotes in
  `what_does_empowerment_approximate.qmd` replaced with `[@Key]` citations;
  zero `TODO cite` markers remain, and `quarto render` resolves every key.
- ~~Regenerate `references.bib`~~ — already regenerated; every key above
  resolves except as noted in the correction below.
- Ref 6 (Dafoe) is now cited in prose, in the cooperative-AI paragraph of
  "Where this leaves the program".
- Ref 19b (Sen 1991) is cited alongside Sen 1988 on the anti-cardinality
  sentence: `[@Sen1991Welfare; @Sen1988Freedom]`, 1991 first as the direct
  rebuttal to Pattanaik & Xu.

### Correction to the trap list

- **`Salge2017Empowerment`, not `salge2017empowerment`.** The regenerated bib
  keys it in the current BBT format like everything else; the lower-case form
  predicted above does not exist in `references.bib`.
