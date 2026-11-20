# Handover: personal_budget

Line of work: what individual principals end up with when every one of them bargains through an AI agent on a limited compute budget.
Draft title: "Bargaining budgets when every principal has an AI agent".
Last updated 2026-11-20, when the files moved here from livingthing.

Read this file, then `draft.md`.

## The commission

Dan asked for a serious academic article responding to Seb Krier's essay [Coasean bargaining at scale](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale).
In substance:

- Explore the equilibria individual principals find themselves in, in an actually-existing Coasean-bargaining world.
- Every principal (human, corporation) has a computational budget correlated with its current endowment. Consider how many matters it must contract over and how it best allocates compute across all of them.
- Other principals are selfish, adversarial, and represented by perfectly aligned agents that compute up to their own, different, limits. Winnings may be spent on compute or on object-level costs.
- "I am suspicious that the world this leads to is recognisably a good one, but this needs testing, which is your job."
- Push Krier's model to its limits with toy mathematical models, taking existing ones from the literature where possible. A reasonable constitution may be fixed.
- Use symbols when making claims: say what something is hard in, convex in, a threshold in.
- "For this round do not bias yourself by reading my other essays on hyperscaling coase."
- Delegate the write-up to an Opus agent told to write clearly and humanly, then have a second, contextless Opus agent cold-read it for nerdview and undefined references, and fix those before showing Dan.

## What exists

| File | What it is | Path in livingthing before the move |
|---|---|---|
| `draft.md` | The article, about 15,400 words with appendix | `_plans/hyperscaling_coase_personal_budget.qmd` |
| `check_budget_contests.py` | Checks every closed form and table in the draft against direct numerical computation; sections A to H; exits 0 in a few seconds | `_plans/hyperscaling_coase_personal_budget_sim.py` |
| `brief_v1.md` | Brief the first-round writer worked from | `_tmp/coase_budget/brief.md` (scratch, deleted there; recovered from the session transcript as it stood when used) |
| `brief_v2.md` | Brief for the three-worlds revision | `_plans/hyperscaling_coase_personal_budget_three_worlds_brief.md` |
| `HANDOVER.md` | This file | `_plans/hyperscaling_coase_personal_budget_HANDOVER.md` (rewritten on the move) |

The briefs are as used and still name the old paths.
None of these files was ever tracked in livingthing.
Here, the first commit holds the draft as Dan first read it, the second holds the three-worlds revision, and the third moves the saturation test beside the three-worlds results, so `git diff` between them shows exactly what each step changed.

Run the script from the repository root:

```
uv run --no-project --with numpy --with scipy python _notes/personal_budget/check_budget_contests.py
```

`_notes/personal_budget_2/` is a separate line of work by another session.
This session did not read it and does not know how it relates to this draft.
Dan's other hyperscaling-Coase notes were not read either, on his instruction.

## What the draft says

It grants Krier's institutions, writes them down as a constitution, and adds one thing: each principal has a budget for bargaining compute, and loyal agents spend against each other to divide a surplus.
The workhorse is the Tullock contest, share $x_i^r/(x_i^r+x_j^r)$ with decisiveness $r$, on a network of bilateral matters with one budget per principal.

Round one (non-saturating matters, where only the compute ratio counts):

1. Taking part in a bargain gets cheap with compute. Dividing a surplus does not: two unconstrained sides spend $rV/2$ dollars whatever compute costs.
2. With many matters and one budget, each principal has a strength $s_i\in(0,1]$ and shares are $s_i^r/(s_i^r+s_j^r)$. For $r=1$ this is Lemma 1 of Díaz-García, Bullo and Marden (2024, arXiv:2408.00883), credited in the text; the extensions are an outside use for money and general $0<r\le1$.
3. A budget-limited principal against unconstrained ones gets a share $\sqrt{B/S}$ at $r=1$. Asha, the running example, gets about an eighth.
4. More matters thin the budget; the share falls as $S^{-1/2}$.
5. At $r=1$, against unconstrained counterparties, the dissipated fraction equals the weaker side's share, so a voucher that evens shares raises waste one for one.
6. A binding budget makes the marginal budget dollar worth several dollars of surplus.
7. Repeat players gain a $\sqrt N$ advantage; coalitions cancel it.
8. If existing entitlements are contestable and the challenge fee is low, an entitlement is safe only up to a multiple of the fee, and cash-poor holders can end up worse off than with no bargaining.
9. If winnings are cash and reinvested in full the budget shortfall cures itself in about two periods; with a drain there is a threshold below which it does not.

Round two (three worlds), added after Dan pressed on the saturation caveat:

10. Diminishing returns to compute is not saturation. A matter saturates if decisiveness $r(q)$ falls to zero as both sides' compute $q$ grows over the range the parties will use.
11. A test for which matters saturate. If a decider compares the two sides' best candidates with error of fixed size, the upper tail of candidate quality decides: bounded tails saturate (spend falls as $\sqrt p$); exponential tails give the draft's contest exactly; Gaussian tails lose decisiveness so slowly (0.44 at $q=10$, 0.19 at $q=10^6$) that they count as non-saturating; power-law tails push decisiveness to 1. If whoever is ahead by any margin wins, nothing saturates. Saturation needs both a best answer and a decider that ignores small gaps.
12. Saturating world: a depth cap binds the stronger side first, so falling compute prices raise Asha's share from 12.6% to 50% before they cut her own bill. Krier is right there on cost and on distribution.
13. Mixed world: with a fraction $\phi$ of her stakes non-saturating, Asha's overall share is $(1-\phi)/2+\sqrt{\phi B/S}$; about \$11,400 at $\phi$ of a fifth, against about \$3,200 when nothing saturates. Within the non-saturating part every round-one result holds with $S$ replaced by $\phi S$.
14. Who chooses: a firm that can set depth at no cost prefers a non-saturating matter exactly when the household's share there would be under 29% ($r=1$), which is when its budget is under 8.6% of its non-saturating stakes. The choice reinforces itself across firms, so one household's dealings tip to all saturating or none. Well-funded households get the saturating world, poorly funded ones the non-saturating world, and Asha's \$11,400 is then not available to her.

Running cast, used in every example: Asha (nurse, \$400 a year for compute, \$25,000 a year at issue), Meridian (the firms opposite her, never budget-limited), Bram (her neighbour), Odile (homeowner, asset-rich and cash-poor).

## What is verified

- Every closed form, table and quoted figure in the draft is reproduced by the script, including a check that no principal can gain by deviating from the computed network equilibrium.
- A contextless cold reader recomputed the closed-form numbers independently after the revision and found no arithmetic errors.
- Round-one citations were each checked against a source; where only an abstract or a secondary source was read, the draft's wording is limited to match (Tullock's chapter, Hirshleifer 1991, Tirole 2009, Cooter). Calabresi and Melamed is cited without a link.
- Budish, Cramton and Shim (2015), the one citation added in round two, was checked at abstract level only.
- Before the move, with the file still a `.qmd` in livingthing: `format-sentences --check` passed, and Vale gave two warnings (the word "you" inside the quoted title of Petel's critique) and one suggestion.

Not verified: the tail-of-quality table and the "who chooses" result are this session's own derivations, checked numerically but not against the literature.
The draft says the table is not a published result.

## What is weak

Carried from round one:

- The split is decided by compute alone. Competition among employers or landlords enters only as a smaller stake.
- The hard budget is assumed. Credit gets one paragraph.
- The entitlement results depend on reading Krier's "automated dispute resolution" as lowering the cost of a challenge; the draft flags this as its own reading. The entitlement contest is solved for $r=1$ only and for a non-saturating challenge only.
- "A small contestable fraction is enough" rests on two illustrative inputs.
- $1<r\le2$ is not covered.
- The self-curing path has Asha reinvest her whole take each year.

From round two and its cold read, not yet acted on:

- The draft does not say which world most real stakes are in. It says why not (nobody has measured $r(q)$ by type of matter, or who sets depth), and a reader may still want a view.
- "Who chooses" assumes raising depth costs the firm nothing, assumes an even split on saturated matters, sets aside Asha's matters with neighbours, and its worked example is $r=1$.
- The budget-limited case is computed for a fixed depth only. For gradual saturation the draft states an expectation, not a result.
- Structure. The cold reader thought the saturation test sat too early, in "The model". At Dan's request the test (the tail-of-quality table) and the argument that complexity is chosen were moved into the three-worlds section, as "Which matters saturate" and the opening of "Who chooses the world"; "The model" keeps only the definitions. No cold read has been run since that move, so the order of definitions around it is unchecked.
- A few first-round sentences the cold reader called slogans or figurative ("puts everything else on sale", "blunt instruments", "does real work") were left as they are.
- Smaller claims the cold reader thought outrun their support: Wallis and North as evidence for the mechanism; the Mailath–Postlewaite reading of Krier's bargaining club; "the side that can compute more can steer an approximate mechanism".
- The approximation $d^2/S$ for the drain threshold is rough for the larger drain (360 against an exact 486).

## What Dan has decided

- Round one, on being asked whether to ingest the references into Zotero: "Not now". Citations stay as hyperlinks on author–year text. Do not ingest until he asks.
- On saturation, after the round-one report:

  > Right, we actually have two conditions. One in which the returns to compute are diminishing, and one in which they are not. It seems reasonable to... Why does one seem more reasonable than the other? So if I mean the average return to compute is diminishing, but the tails of all the possible bargains do not, then am I in a different world?

  > I think we don't want to drop any of the cases yet. So should we have all three?

  That is the origin of the three worlds. Nothing was to be cut, and nothing was.
- He chose to have the revision done before the move ("Revise here first"), then asked for the files to be moved here and committed.
- Asked whether to move the saturation test next to the three-worlds results: "Yes, move it". Done in the third commit.
- He has not yet read the revised draft, and has seen the "who chooses" result only as a short chat summary.

## How Dan wants this done

From his instructions and standing preferences in livingthing, restated because this repository may not carry them:

- Drafting that needs taste goes to an Opus agent; a second, cold Opus agent then lists the draft's problems.
- While an essay is still being worked out, no length targets and no cutting. Fix only what impairs the reasoning.
- Define every coinage at first use, one term per concept, and coin nothing mid-analysis.
- Plain literal phrasing. No strained or mixed metaphors, no rhetorical beats. Round numbers in prose.
- Toy-model findings reach him as stories about the running cast, with numbers as grounding.
- Symbols in every technical claim.
- Prose is one sentence per line.
- Final reports to him are written from a fresh, low-context read of the deliverable.
- Never write `<!-- sem -->` markers; they are his.
- Commit only when asked, by named path.

The voice and slop references the writer agents read are in livingthing: `/Users/dan/Source/livingthing/_voices/dan_voice.md` and `_voices/slop_patterns.md`.

## Next steps

1. Have a contextless reader check the draft from "The model" to the end of the three-worlds section for terms used before they are defined and references that point the wrong way after the move. Fix what it finds.
2. Dan reads the revised draft, or the diffs between the commits here.
3. If the draft is to become the essay, it becomes a top-level `<slug>.qmd`, and its citations move from hyperlinks to `[@Key]` through Zotero, as this repository's `CLAUDE.md` requires.

The original conversation is on Dan's machine at `/Users/dan/.claude/projects/-Users-dan-Source-livingthing/d630c307-1ca3-4346-95b6-df2f3f07beff.jsonl`.
It holds the literature-verification notes, which are not reproduced here.
