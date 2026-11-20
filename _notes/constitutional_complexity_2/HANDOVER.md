# Handover: "Delegated agent constitutional negotiation favours the incumbents"

Written 2026-11-20 by the session that produced the article, for an agent picking it up in a new repository.
You have none of this session's history, memory or repo instructions, so everything you need is here or in the files listed below.
Where this note and the article disagree, the article is right.

## What exists

Dan asked for a serious academic article, under that title, responding to Seb Krier's essay "Coasean Bargaining at Scale" (<https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale>).
He suggested the computational-complexity and incomplete-contracts literatures as angles of attack.

The article is a complete draft of about 9,400 words (`wc -w`, including frontmatter and maths).
It has had three Opus drafts and three cold reads; after the third read I fixed the remaining problems by hand, and that last set of 35 edits has not itself been cold-read.
Dan has not yet given feedback on the current version.
His only comment on content so far is the aligned-agents point under "Dan's input" below.

## Files

Everything from the old session was moved (not copied) on 2026-11-20 from `~/Source/livingthing` into this folder, `_notes/constitutional_complexity_2/`.
The folder convention is described in the repository README.

| File here | What it is | Path in livingthing before the move |
|---|---|---|
| `draft.md` | The article | `_plans/hyperscaling_coase_constitutional_complexity_2.qmd` |
| `check_contest_model.py` | Numerical check of the main result | `_plans/hyperscaling_coase_constitutional_complexity_2_check.py` |
| `HANDOVER.md` | This note | `_plans/hyperscaling_coase_constitutional_complexity_2_handover.md` |
| `brief_v1.md` | First drafting brief | `_tmp/coase_constitutional_2/brief.md` |
| `brief_v2.md` | Second drafting brief | `_tmp/coase_constitutional_2/brief_v2.md` |
| `brief_v3.md` | Third drafting brief | `_tmp/coase_constitutional_2/brief_v3.md` |

The article is a `.md` note for now, by Dan's decision: "we'll move to `.qmd` as we write the actual essay."
Its content is byte-identical to the `.qmd` it was; only the name changed.

The briefs are needed together: v3 is a revision brief that refers back to v1 for the hard constraints and to v2 for what each cited paper shows.
They are the only record of which claim rests on which source and of what I checked each source says.
They refer to each other and to the article by the old livingthing paths in the table above; I left them unedited as a record.

**Git state.** In `~/Source/livingthing`, commit `925143ee93` holds the article, check script and handover as they were just before the move, so the history there has the current draft.
(The older commit `f5fa2e4224` holds the first draft, which has a different structure and a main result that does not hold as stated. Do not work from it.)
The briefs were gitignored there and exist only here.
The move is committed on both sides: the removal in livingthing, and this folder here in the commit titled "Notes: constitutional_complexity_2 moved from livingthing".

## What I have not read, on purpose

Dan's instruction was: "For this round do not bias yourself by reading my other essays on hyperscaling coase."
I read no other file with `hyperscaling_coase` in its name and none of his other writing on Coase, agents or institutions.
Consequences you should know about:

- A third round of this article, `hyperscaling_coase_constitutional_complexity_3.qmd`, and its own handover appeared in livingthing's `_plans/` during this session, written by another session. I do not know whether it supersedes, extends or competes with this article. Other sessions are moving their files here too, so it may now sit in a sibling folder under `_notes/`.
- Dan keeps a list of published critics of Krier's essay (in livingthing, `_plans/hyperscaling_coase_prior_critiques.md`) and wants critiques that reprise a published one to cite it. I did not read it, and a web search found no overlapping critique, so overlap with published critics is unchecked.
- **The instruction still holds.** I asked Dan on 2026-11-20 whether it had lapsed and he answered "not yet". Do not read the sibling essays, their handovers or the prior-critiques file until he says so.

## The argument as it stands

Krier's case is granted inside given rules. The article asks what happens when faithful agents negotiate the rules themselves.
Krier concedes that the initial allocation of rights is "a constitutional choice, not a technicality", and offers two routes for changing it: voluntary renegotiation, and democratic amendment made cheaper by agents.

**Benchmark.** Position-independence: sides with equal stakes and equally capable agents should do equally well whatever positions they hold when negotiation starts.

**Four positions.** Entitlement holder, organized party, drafter, residual controller (the one who decides where the text is silent).
"Incumbents" means holders of these positions, who need not be defenders of the status quo. The title invites the narrower reading, and the article defines the term early for that reason.

**Two routes, two predictions.** On the voluntary route the status quo tends to stay. On the democratic route rules change in the direction organized parties and proposers want.

**Claims, with the strength the article gives each.**

1. *Cheap purchased effort* (a theorem inside the model). A factory with stake $v$ buys effort $B$ at price $c$. Each of $n$ residents has stake $v/n$, supplies personal effort $a$ at cost $a^{1+\alpha}/(1+\alpha)$, and may also buy effort at $c$. The residents win with probability $p = A/(A+B)$. With $r = B/A$, $p = 1/(1+r)$, and while $r < n$, $r^{1/\alpha}(1+r)^2 = v\,n^{1/\alpha - 1}\,c^{-(1+1/\alpha)}$. As $c$ falls $p$ falls, to a floor of $1/(n+1)$ reached at $c^* = \big(v/(n(n+1)^2)\big)^{\alpha/(1+\alpha)}$, equivalently for stakes above $v^* = n(n+1)^2 c^{(1+\alpha)/\alpha}$. So large-stake contests are at the floor already and cheaper cognition extends the floor to small local ones. One against one, the floor is even odds. Illustration, as the article gives it, with $v=100$, $n=20$, $\alpha=1$: $p \approx 0.18$ at $c = 0.85$, about $0.10$ at $0.33$, and the floor of about $0.05$ from $c \approx 0.11$ down.
2. *The audit burden* (a conjecture by analogy). If cheap cognition makes rules more detailed, which is Krier's own premise, the drafter can plant structure that the other side must search for. The analogy is to Arora, Barak, Brunnermeier and Ge (2011) on planted structure in financial products.
3. *The weakening of explicit text* (an extrapolation). More contingencies shift weight from what the text says to who decides the rest, extrapolating from Segal (1999), which is a two-party model.

Supporting pieces: a lemma that a contest between two buyers of effort at the same price is decided by stakes alone and wastes the same amount whatever the price; and a result on earmarked compute credits ($p = \sqrt{nq/v}$ for credit $q$ each, so even odds need $nq = v/4$).

The closing position is that the remedies these models point to are non-voluntary.

## What is verified and what is not

- The main result is checked numerically: `check_contest_model.py` solves the equilibrium by best-response iteration and compares it with the closed form for three values of $\alpha$. They agree to four decimal places. It needs numpy and scipy, which this repository's `pyproject.toml` does not declare, so from the repository root run `uv run --no-project --with numpy --with scipy python _notes/constitutional_complexity_2/check_contest_model.py`. I re-ran it that way after the move.
- The third cold reader re-derived all the algebra in the article and found no errors.
- The lemma and the credits result were checked numerically by an earlier script that I did not keep; the third reader's re-derivation covers them.
- DOIs were confirmed against Crossref. Recent or less familiar sources were checked against abstracts or primary text. The classic literature is characterized from memory.
- **Lee and Sabourian (2007) is taken from its abstract and a companion working paper.** I never obtained the full text and have not checked the proof. A footnote in the article says so.

## Known weaknesses, most important first

1. **The contest model of the democratic route is an assumption.** It treats influence over a decision as proportional to effort. The article defends this (nearly indifferent deciders can be moved; delegates are targets) and says where it fails: if only the directly affected vote, with equal votes, numbers win and claim 1 does not apply. A reader sympathetic to Krier can reject the main result at this step.
2. Claims 2 and 3 are an analogy and an extrapolation. They are labelled as such, but neither has a model of its own.
3. The model's units are uncalibrated. Nothing says where real contests sit relative to $v^*$.
4. Points from the third cold read that I left: the Summary assigns roles to results before the terms are defined; some details of Krier's essay are reported and never used; the section "Who the incumbents are" adds little; one part of the costly-negotiation argument rests on the unchecked Lee and Sabourian proof.
5. Citations are 45 inline hyperlinks, not citekeys. Nothing has been added to Zotero. The comment under the draft's frontmatter gives an ingestion command with the old path; the working command is in the repository README under "References and Zotero". A dry run of it from this repository resolved 43 of the 45 links, the other two being Krier's essay and Anthropic's Project Deal page, which are not papers. Three items will need their metadata fixed in Zotero after a real ingest: Tullock (1980) resolves to the 2001 reprint volume with its editors as authors, Buchanan and Tullock comes back dated 1960 where the article cites 1962, and Goldwasser et al. takes its 2024 arXiv revision date where the article cites 2022. Dan has not said which Zotero collection the references belong in.
6. Krier is quoted verbatim once, in a phrase of six words, and otherwise paraphrased. I asked Dan whether an academic reply should quote him more and the answer was no; see "Dan's input".

## Dan's input

On an early draft Dan objected to a paragraph that located the drafting advantage in agents that might not be faithful to their principals.
His point: the advantage arises with every agent fully aligned, for example when a factory and the wider society negotiate a constitution and the factory's faithful agents choose rules that favour factories in the negotiations factories tend to be in.
The section was rebuilt around that case. Provider backdoors are now one footnote. Keep it that way.

On tone, when I asked whether to quote Krier more (2026-11-20): "No, we are not aiming to rip him into shreds but rather to constructively engage."
The article already grants Krier's argument inside given rules and ends with tests that could count against its own claims.
No draft or cold read was briefed on tone, though, so check the next revision against this: the aim is to extend Krier's programme by showing where it needs non-voluntary support, not to refute him.

## How Dan wants this kind of work done

These are stored as memories keyed to the old repository's path, so they will not load in the new one.

- **Opus drafts the prose.** The working agent builds the argument, derivations and sources into a brief; an Opus subagent writes from it. Dan finds Opus prose closer to his voice than Fable's.
- **A second, cold Opus then reads the draft** with nothing else (no brief, no history) and lists its problems, "especially insufficiently explained concepts and poor narrative structuring" (Dan's words). The problems get fixed before the draft is called done, and Dan is told what the read found. He accepted these mechanics as "good enough to go on with".
- **No word limits while an essay is still being worked out** (Dan, 2026-11-20, on a sibling essay). Do not give drafters a length target and do not cut for length; remove only what is wrong or confusing. My third brief set a 7,000 to 8,000 word target before this preference existed, and the drafter cut to meet it. Do not treat the current length as a defect.
- **Voice.** Oxford `-ize` spelling; "I" for Dan's own views and "we" for writer plus reader, never an indefinite "you"; no colons in headings; plain literal phrasing; every coined term defined at first use and one term per concept; link text names the concept, not the page.
- **Format.** One sentence per line in `.qmd` prose. Bibliography files are generated from Zotero and never edited by hand.

## Tooling the article depended on

All of it lives in `~/Source/livingthing` and none of it exists in this repository:

- `uv run format-sentences <file>` for one sentence per line (the article passed unchanged before the move).
- `vale <file>` with the config in `.vale.ini` and `styles/livingthing/` (0 errors, 0 warnings, 1 suggestion before the move).
- `_voices/dan_voice.md`, the full voice rules.
- `uv run ref-cite` for moving hyperlink citations into Zotero.

I have not tried running any of these against a file outside livingthing.

## When the draft becomes the essay

This repository renders every top-level `<slug>.qmd` as a post and lists it on the home page.
Its `CLAUDE.md` asks for `title`, `date`, `categories` and `author` in the frontmatter; the draft has `title`, `date` and `abstract` only.
I have not rendered the draft with Quarto here.

## What went wrong, so you can avoid it

The main result was wrong in the first two drafts.
Both compared a linear-cost model with a quadratic-cost one and read the difference as the effect of cheaper cognition; but giving residents a new option cannot by itself make them worse off.
The fix was one model with the price as a parameter.
Neither I nor the drafter caught this; the second cold reader did.
Check any new derivation numerically before handing it to a drafter, and expect the cold read to find faults in the argument as well as the prose.

The work cost roughly 1.5 million subagent tokens over three drafts, one section rework and three cold reads.
