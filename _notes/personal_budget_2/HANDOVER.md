# Handover: "The compute budget of a Coasean principal"

Written 2026-11-20 for an agent picking this work up in a new repository, with none of the earlier conversation.
Read the article first; this note covers what the article does not say about itself.

## What this is

Dan MacKinlay asked for a serious academic article responding to Séb Krier, ["Coasean bargaining at scale"](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale).
His brief: every principal (person, firm) has a compute budget correlated with its endowment, is party to many bargains at once, and faces selfish opponents whose perfectly aligned agents compute up to their own limits; gains can be spent on compute or on ordinary things.
The special angle is the principal's **production function** in compute and initial endowment, compared with the one that Krier's good outcome presumes.
Claims must be stated in symbols ("waste is $r/2$ of the surplus", never "it is hard" without saying hard in what).

## Files

Everything was moved (not copied) on 2026-11-20 from `~/Source/livingthing` into this folder, `_notes/personal_budget_2/`.
The folder convention is in the repository README.

| File here | What it is | Path in livingthing before the move |
|---|---|---|
| `draft.md` | The article, about 11,300 words, one sentence per line | `_plans/hyperscaling_coase_personal_budget_2.qmd` |
| `check_closed_forms.py` | Numerical check of every closed form in the article, plus the wealth simulation behind its table; about 5 s | `_plans/hyperscaling_coase_personal_budget_2_sim.py` |
| `check_pending_derivations.py` | Checks for four derivations that are **not yet in the article** (see "Derived but not written up") | `_plans/hyperscaling_coase_personal_budget_2_pending_checks.py` |
| `HANDOVER.md` | This note | `_plans/hyperscaling_coase_personal_budget_2_HANDOVER.md` |
| `brief_v1.md` | Brief for the first Opus draft: the models, results, sources and constraints | `_tmp/coase_budget2/brief.md` |
| `brief_v2.md` | Rulings on the first cold read, for the first revision | `_tmp/coase_budget2/revision.md` |
| `brief_v3.md` | Brief for the second revision: named worlds, stance, contract plus circumstances, the risk note | given inline to the drafter, never a file |
| `brief_v4.md` | Rulings on the second cold read | given inline to the drafter, never a file |

Run the scripts from the repository root:
`uv run --no-project --with numpy --with scipy python _notes/personal_budget_2/check_closed_forms.py` (likewise `check_pending_derivations.py`).
Both ran clean here after the move.

The article is byte-identical to the `.qmd` it was, except for two lines: the script path named in its Summary, and the closing comment about moving citations into Zotero.
The scripts differ from their livingthing versions only in their docstrings.
The briefs are unedited records and still use the old livingthing paths and old terms.
`brief_v1.md` is the only record of which claim rests on which source; it asks for *-ise* spelling and a length limit, both since overruled (the article uses *-ize*, and Dan wants no length limits yet).
`brief_v1.md` and `brief_v2.md` had been deleted from disk in livingthing and were recovered from the session transcript.

**Git state.** In `~/Source/livingthing`, commit `7a001e10aa` holds the article, both scripts and this note as they were just before the move; a following commit there removes them.
Nothing has been rendered through Quarto or put in Zotero.
Citations are hyperlinks; Dan has said that is fine for now.
`_plans/hyperscaling_coase_personal_budget.qmd` and its `_sim.py` in livingthing (no `_2`) belong to a different session's attempt, which this work never read.

## The article in one paragraph

Two worlds are named.
The **sufficiency world** is the one Krier's essay suggests without stating: a fixed amount of compute per matter is enough, more adds nothing, and the opponent's compute does not matter (four properties: satiation, no rivalry, compute only creates surplus, cheap floor).
The **contest world** is what board-game evidence on compute suggests: a principal's share of a matter depends on its compute relative to its opponent's, through a Tullock contest success function with decisiveness $r$.
Under perfect enforcement, loyal agents and one price $p$ for compute, the contest world gives: waste of $r/2$ of every evenly matched surplus at any $p$ (Results 1, 2); wealth buys nothing above a parity threshold $Rw_i\ge rE_i/4$ that is fixed in dollars, not in compute (Result 3); below it the share is $\sqrt{Rw_i/E_i}$ at $r=1$ (Result 4); waste on a lopsided matter equals the weaker side's share (Result 5); the parity subsidy is $(rE_i/4R-w_i)^+$ (Result 6); a poverty trap once subsistence is added (Result 7); a repeat player's share $M^{\phi r}/(1+M^{\phi r})$ (Result 8); sufficiency does hold on any matter both sides can solve outright (Result 9, resting on an assumed cost $G(n)=G_0\gamma^n$); manufactured threats pay when $h/\kappa>(2+r)/(2-r)$ (Result 10).
The article ends with a "Cruxes" section listing the quantities that decide which world a matter is in.

## Decisions Dan has made

- **Stance.** Productive engagement, not adversarial: "inspired by Krier", asking what his method assumes about the world, in order to find cruxes. Never call the benchmark "what Krier said"; it is the named sufficiency world, and he may reject some of its properties.
- **Contract and circumstances.** What must be simple for compute to stop mattering is the matter as a whole, contract terms plus circumstances. The model collapses both into detail $n$, with $n_0$ the part set by circumstances.
- **No word limits during ideation.** Do not cut for length and do not give drafters length targets; delete only what is wrong or impairs reasoning.
- **Citations as links are fine for now.**
- **Kelly-style optimum: pinned**, not to be pursued yet (see below).
- **He has not yet answered** whether to go ahead with extensions 1 to 3 below. He asked whether each is worth doing; my answer was yes to all of them.
- **The mapping from compute to effort (item 5 below): wanted in the article**, but without disturbing the narrative (2026-11-20). Item 5 says where it goes.

## Derived but not written up

Items 1 to 3 are checked numerically in `check_pending_derivations.py`, at $r=1$ and $R=1$; item 4 is an unverified argument; item 5 is algebra with no numerical check.
None has been through a drafter or a cold reader.

1. **A family that nests both worlds (Dan's question: under what conditions does a compute advantage shift the deal?).**
   Let effective compute be $\min\{c,G_m\}$, where $G_m$ is the compute that solves matter $m$ outright.
   Unconstrained parties want to spend $pc^*=rS_m/4$ each, so both stop at $G_m$ exactly when $pG_m<rS_m/4$.
   Then waste is $2pG_m$, which does vanish as $p\to0$.
   So a matter is in the sufficiency world iff $r=0$ or $pG_m<rS_m/4$: the cost of solving it is below what the contest would have each side spend.
   For a fixed matter Krier's claim holds in the limit; the contest world persists only if $G_m$ grows as fast as $1/p$, that is, if matters get more complex as compute gets cheaper (the drafter adding detail, or circumstances becoming richer).
   This turns the first two cruxes into one inequality and should probably restructure the article around it.
   The cold reader independently flagged that the article's two routes to sufficiency ($r=0$, and solvability) were being treated as one; the wording is fixed but the inequality is not yet in.

   **Complexity chosen by the participants (Dan's follow-up, 2026-11-20).**
   Dan's remark on the sentence above was a fragment, "Not be chosen by the participants in the market."
   I read it as: how complex a matter is would be chosen by the participants, so it is an equilibrium quantity and not a free parameter. Confirm that reading with him.
   Check 4 in `check_pending_derivations.py` takes the article's $S(n)=\bar S(1-\delta^n)$ and $G(n)=G_0\gamma^n$ and lets a drafter facing an equally resourced, unconstrained opponent choose $n$.
   Its payoff is $S(n)/2-pG(n)$ on a solved matter and $S(n)(\tfrac12-\tfrac r4)$ on an unsolved one.
   Above a threshold price it picks an unsolvable matter and the contest; below it, it picks a solvable one, with detail growing like $\log(1/p)/\log(\gamma/\delta)$ and waste falling to zero ($\bar S=G_0=1$, $\delta=0.7$, $\gamma=2$, $r=1$: contest at $p\ge10^{-2}$, solved from $p=10^{-3}$, waste 9% there and 0.07% at $p=10^{-9}$).
   So between evenly resourced parties, chosen complexity ends in the sufficiency world as compute gets cheap, because the value of extra detail saturates while the cost of solving it grows exponentially.
   That is a result in Krier's favour and should be stated as one.
   The contest then survives only through (a) unequal resources, where the drafter gains share by exceeding what the other side can solve (the constrained or scale-disadvantaged opponent of Results 4, 8 and 9), (b) complexity set by circumstances, $n_0$, which nobody chooses, (c) returns to detail that do not saturate, and (d) manufactured threats.
   Not yet done: the drafter's choice against a liquidity-constrained opponent, which is where (a) needs its own formula.

2. **Lending against bargaining gains, as one parameter (Dan: "a thicket of branching paths … some kind of simple approximation").**
   Let a fraction $\psi\in[0,1]$ of a principal's bargaining gain be pledgeable to a lender.
   Its spending is $Rw_i+\psi s_iE_i$, and with the square-root law the share solves $s^2-\psi s-\rho_i=0$, so $s=\tfrac12\big(\psi+\sqrt{\psi^2+4\rho_i}\big)$ up to $\tfrac12$.
   Parity is reached iff $\psi\ge r/2-2\rho_i$: a principal with no wealth needs half its gains pledgeable at $r=1$.
   A principal with no wealth gets share $\psi$, and $s=0$ is also an equilibrium (the lender expects nothing and lends nothing).
   $\psi=0$ is the current article; $\psi=1$ is full credit.
   The three frictions in the article (non-monetary gains, unverifiable stakes, funder with scale) each lower $\psi$.
   To probe the approximation: derive results as functions of $\psi$; micro-found $\psi$ with a costly-state-verification model; calibrate against which legal claims contingency lawyers and litigation funders take today (contingency fees are commonly about a third, and funders are said to avoid small claims; both from memory, unverified).
   Use a symbol other than $\lambda$, which the article uses for the shadow price.

3. **Optimal subsidy (Dan: is there a conveniently affordable subsidy that is net beneficial by some equity metric?).**
   On a matter between a constrained $i$ and an unconstrained $j$, total net surplus is $S(1-s_i)$, so on efficiency alone the best subsidy is zero.
   Per subsidy dollar, the recipient gains $1/(2s)$, the opponent loses $(1-s)/s$ and the payer loses 1, so **everyone else loses two dollars for each dollar the recipient gains**, at every $s<\tfrac12$.
   A constrained principal spends cash on compute too, so cash transfers leak identically.
   An equity criterion follows: subsidize while the social weight on the recipient's marginal dollar is more than twice the payers'; under log utility, while the recipient's income is below half the payers'.
   The dynamic case is where a cheap subsidy may exist: lifting a principal over the trap threshold $w_-$ is a one-off cost (0.27 against a parity threshold of 2 at mean stakes in the simulation), after which it grows unaided.
   Not yet done: funding the subsidy by a tax inside the simulation, general $r$, and comparison with rules that cut waste directly (standard forms, compute caps).

4. **Kelly (pinned).**
   Dan's intuition: spending all savings on compute looks like an all-or-nothing bet with a different optimum.
   The models treat the share as a division of surplus, which equals a win probability only under risk neutrality or many small independent matters.
   With win/lose outcomes and log utility the constrained principal would spend less than everything.
   By scale invariance (the share depends on the ratio of dollars spent, and CRRA utility is homogeneous), the parity threshold should remain a fixed fraction of stakes, independent of $p$, but a larger fraction than $r/4$.
   That argument is unverified. The article records the question in "Limitations and tests".

5. **The mapping from compute to effort (Dan, 2026-11-20: "we have to choose a mapping from 'compute' to 'effort' in their sense?").**
   Skaperdas's axioms are about effort in some unit; they say the outcome does not depend on the unit, not which physical quantity is the effort.
   Write effort as $e=g(c)$ and apply the ratio form to $e$.
   If $g(c)=c^a$ the share is the ratio form in compute with exponent $ra$, the price of compute cancels, and every result in the article stands.
   If $g(c)=\exp(kc)$ the share depends on the difference $c_A-c_L$, which is $(x_A-x_L)/p$ in dollars, so cheaper compute makes a dollar gap more decisive.
   If $g(c)=\log c$ the share tends to the merit share as $p\to0$ at any fixed dollar ratio, so cheaper compute makes money less decisive.
   $g(c)=\min\{c,G\}$ is item 1.
   The parity threshold does not need the Tullock form: for any share $f(x_A/x_L)$ with $f(1)=\tfrac12$, unconstrained symmetric spending is $x=S\,f'(1)$, and $f'(1)=r/4$ for Tullock.
   The square-root law does need it, at $r=1$.
   So the assumption carrying "parity costs a fixed fraction of stakes at any $p$" is that the share depends on the compute ratio alone.
   The article's support for that is the Elo evidence (rating linear in log compute gives win odds $(c_A/c_L)^r$), not the axioms; the draft presents the two as parallel supports.
   Two weaknesses to state: the log-linear fit holds over the range tested (Elo per doubling is said to fall at long time controls; from memory, unverified), and it is a win probability in board games read as a share of a bargaining surplus (the same gap as item 4).
   A direct test, separate from measuring $r$: hold the compute ratio fixed, scale both sides up, and see whether the split moves.

   **Where it goes in the draft, to disturb least.** No new section and no new coined term.
   (a) In "Compute in games against an opponent", reword the two Skaperdas sentences in place so they claim only that the ratio form follows once the unit of effort is chosen, and add one sentence saying the Elo evidence in the next paragraph is what chooses compute as that unit.
   (b) In "Cruxes", one new item in the first group (which world a matter is in), with the scaling test.
   (c) In "Limitations and tests", one sentence on the range of the log-linear fit.
   Do (b) in the same revision as item 1, which rewrites that group of cruxes anyway; doing it separately means editing the same list twice.

## Other open items

- Solve $r>1$, where Jones's fitted value (about 1.3) lies; the allocation problem is then not concave and the first-order conditions fail.
- The literal `TODO:` in the article: whether the standard-form remedy deserves its own model.
- Literature claims are from memory except for the sources actually opened (Krier, Jones 2021, Project Deal, abstracts of Zhu et al., Shahidi et al., Tirole, Sharp et al.). Every DOI resolves to the right paper, but what Sandholm et al., Mailath–Postlewaite, Arora et al., Hirshleifer and Skaperdas are said to show needs checking before publication.
- Overlap with Dan's own earlier hyperscaling-Coase essays and with published critiques other than those cited is unchecked, on his instruction not to read them "for this round". Ask whether that still holds.
- The simulation is one parameter set, with an unfunded allowance.

## How Dan wants the work done

- Prose is drafted by an Opus-class subagent briefed for clear, human presentation, then read cold by a second Opus that sees only the draft and lists undefined terms, insider shorthand and attributions the page does not support; fix those before showing Dan. Models and checks are the lead agent's job.
- Reports to Dan: plain language, terms defined, findings first. He reads replies as a document and answers by quoting passages.
- Define every coined term at first use and keep one term per concept. Current terms: sufficiency world, contest world, matter, surplus, stakes, merit share, decisiveness, strength, satiation level, parity threshold, trap threshold, waste, detail.
- Running cast for examples: Alice (tenant, $160 savings), Bob (neighbour), the landlord. Tenancy surplus $4,000.
- Spelling: Oxford -ize, otherwise British. No colons in headings. "I" for the author's own judgements.
- In livingthing the article passed `vale` (config `.vale.ini`, rules under `styles/livingthing/`) and `uv run format-sentences --diff` with no changes; both tools belong to that repo and are not set up in this one.
- Commands handed to Dan must be valid fish. Never run whole-tree git commands; commit only when asked, by named path.
