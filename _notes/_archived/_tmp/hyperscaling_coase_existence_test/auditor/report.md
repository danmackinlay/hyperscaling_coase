# Row auditor's report (Opus), existence-test round, 2026-10-21

Saved verbatim by the session from the agent's final message; the agent's own write of this file was refused by the harness ("Subagents should return findings as text, not write report files"). The three scripts behind it, `river_checks.py`, `river_checks2.py` (row 1 with a separate margin per resident) and `river_checks3.py` (row 1 with the margin set after the factory sees its estimates), are the agent's; run from the repo root with `uv run python -I <path>`. Under the mission's rules a number of the agent's counts as "computed" only once the collator re-runs these scripts; the collator re-ran all three on 2026-10-21 and the figures below reproduce.

# Row audit of the hyperscaling_coase state table, 2026-10-21

## (a) Answer on the river's numbers

More compute produces better outcomes under an inequality-sensitive criterion in only two places: where a rule already protects the worst-off, and where the compute is in neutral hands. Everywhere else it raises efficiency and hands the pie to whichever side the rules let commit. Unanimity (k=3) is the only rule that keeps every resident at or above 0.

- **k=3, factory commits (take-it-or-leave-it).** More estimation compute raises the deal rate from 33–34% to 99.9%, and total expected surplus rises steadily from 2.0 to 6.0. The residents' expected take rises to a peak of about 2.0–2.3, at noise σ of 0.5 to 1.0, then falls to 0.1. Each resident's expected payoff peaks at 0.6–0.76 and falls to 0.03.
- **k=3, residents commit as one bloc.** The same compute moves the pie the other way: the bloc's take goes from 3.4 to 5.96. How it is shared among residents depends on an internal rule that compute does not supply: equal gains (2, 2, 2) or in proportion to harm (0.86, 1.29, 3.86).
- **k=3, both sides commit at once and commitments usually stick (q=0.9).** The pie is lost 81% of the time.
- **Liability rule.** Estimation compute held by the assessor of damages helps the worst-off. The expected lowest resident moves from −1.27 (σ=1.5) to −0.01.
- **Any k below 3 (k = 0, 1 or 2).** Compute is beside the point. Residents can end at (−2, −3, −9) with the factory at 10 or 20. This happens in the one-shot game, and every year in a repeated equilibrium that exists at every level of patience.
- **k=1 with π=20.** That same outcome is efficient: it passes the efficiency test and the Pareto test while all three residents lose, resident 3 by 9.

Who gains: whoever commits first or is cheapest to commit, the factory whenever consent is not unanimous, and, within the residents, whoever is hardest to measure. The rule that protects the residents, unanimity, is also the rule under which simultaneous commitment is inefficient.

## (b) Delta block

`Delta to state, 2026-10-21:`

**Rows changed**

- **Row 1, take-it-or-leave-it by the factory.**
  - Status: computed. I re-ran it and got 33.4% (margin fixed in advance) or 33.7% (margin set after the factory sees its estimates) at σ=1.5, and 99.86% or 99.89% at σ=0.01. These agree with the row's 34% and 99.85% to rounding.
  - Wording: "expected surplus peaks at middling budgets" becomes "the residents' expected surplus peaks (2.27 at σ=1.0, or 2.02 at σ=0.5); total expected surplus rises steadily from 2.0 to 6.0".
  - State k=3 and the noise model.
  - Source: the script spec, plus Snow 2025 as the published precursor.
- **Row 2, take-it-or-leave-it by the residents.**
  - Status for the bloc: computed by me. It is not a mirror of row 1: the deal rate is 86.6% at σ=1.5 against row 1's 33–34%, because the bloc needs one acceptance where the factory needs three.
  - Status for the internal split: argued, with no reviewer count.
  - Source: Dixit & Olson 2000 for the bloc's participation problem [sure]. Remove Miettinen–Vanberg 2025 from this row; it models simultaneous individual declarations, not a bloc's take-it-or-leave-it offer [sure, abstract].
- **Row 3, haggling with everything known.**
  - Status: theorem for the 1.5-each benchmark once Nash 1950 and Shapley 1953 are read; empirical, one study, for the capability gap.
  - Source: Anthropic 2026, "Project Deal" [sure, read], instead of "findings".
  - Replace "theory of which equilibrium is open": with three or more players any division is a subgame-perfect equilibrium when players are patient (Shaked, reported in Osborne & Rubinstein 1990, §3.13 [likely]), and the stationary equilibrium is unique (Baron & Ferejohn 1989 [sure]).
- **Row 4, haggling with private harms and fast offers.**
  - Status: demote from theorem to "argued, 1 reviewer (economist); contradicted by the primary". Gul & Sonnenschein 1988 [sure, read] prove that delay vanishes as the time between offers shrinks, so "deals close late" is the opposite of the Coase conjecture.
  - Restate as: with one side uninformed, deals close fast and the informed residents keep information rents.
  - If the residents also do not know π, as in the essay's private setting, the uncertainty is two-sided and delay can persist: Cramton 1992 [likely].
  - Both papers are two-player. Equity cannot be computed until a harm distribution F is fixed.
- **Row 5, both commit, sealed, once.**
  - Status: theorem, kept. I read part of the text this session: q² and three outcomes at q=1 confirmed [sure].
  - Restate the condition as "the factory against a residents' bloc whose internal split is fixed". The result is bilateral; the four-player version is row 8.
  - Add the river's numbers, and Ngo 2026 as the precursor.
- **Row 6, both commit, publication in sequence.**
  - Status: argued, six of six, kept for "one claimant beats three". Add "theorem in its own model" for "the first committer wins": Hang & Wen 2026, multilateral, unanimity, sequential commitment [sure, abstract and introduction read; full text needed].
  - Narrow the claim: the first successful committer becomes the proposer, and the others keep their continuation values. On the river that gives the first committer 6 − 4.5δ and each other party 1.5δ, so 1.95 against 1.35 each at δ=0.9 [likely]. "Takes the pie" holds only when δ is near 0.
  - Restrict the Information column to transparent. With noisy estimates this row is row 1.
  - Cite Schelling 1956, and Ngo, Snow and Petel.
- **Row 7, instructions read each other.**
  - Status: theorem for two players only. Kalai et al. 2010 is explicitly two-person [sure, abstract]; Tennenholtz 2004 is two-player [likely]. Applying it to four players is argued, with no reviewer count.
  - Equity: "individually rational" means at or above each party's minmax. That is 0 at k=3 and (−2, −3, −9) at k<3, so at k<3 a resident can be held at −h_i in equilibrium.
  - Retire "verification capacity enlarges the set" until a source is found; DiGiovanni & Clifton 2023 is a candidate [unsure].
- **Row 8, many residents under unanimity, binding declarations.**
  - Status: demote from "theorem, abstract read" to "theorem in its own model, abstract only; applies to the river at k=3 only". The model is pure division of a pie: nobody outside the winning coalition is harmed. On the river at π=10, k=1 and k=2 pollute although pollution is inefficient, so "efficient under every other rule" does not transfer.
  - Add Hang & Wen 2026: the inefficiency comes from simultaneous timing, not from unanimity.
  - Source: Miettinen & Vanberg 2025, read in full.
- **Row 9, repeated play, patient parties.**
  - Status: split it.
    - Folk theorem: theorem once Fudenberg & Maskin 1986 is read. Its application to a bargaining stage game is argued.
    - "Lock-in": no primary given. Young 1993 has long-run selection of a weighted Nash split, not lock-in [likely].
    - "Tilt": theorem once Young 1993 is read. A side's sample size of past play is its weight in the Nash product [likely].
    - Thresholds: computed by me for one stage game, δ ≥ g/2.
  - Add Pei 2025 as a counter-model: fair division in repeated bargaining with a status quo [sure, abstract].
  - Source: these primaries, not "repeated-games theorist".
- **Row 10, divide and conquer, k=1, π=10.**
  - Status: computed. I re-ran it: core deficit 16; payoffs (−2, −3, −9) for the residents and 10 for the factory; welfare −4.
  - The Tullock mapping is demoted from the economist's say-so to "computed by me on Baik 2008 [sure, abstract]". If residents spend separately, only resident 3 spends, so the contest is 9 against 10, not 14 against 10. The residents then win with probability 0.474, not 0.583.
  - Source: Segal 1999; Tullock 1980; Baik 2008.
- **Row 11, one side adapts, the other is fixed.**
  - Status: theorems for two players (Press & Dyson 2012 [sure]; Deng, Schneider & Sivan 2019 [sure]). The river application is argued, with no reviewer count.
  - Add the bargaining-specific primaries Ellingsen 1997 [unsure on its result] and Abreu & Gul 2000 [sure, abstract].
- **Row 12, liability rule in statute.**
  - Status: "by construction" is not a status. Make it computed by me.
  - Equity at π=20: with damages equal to each resident's own harm, residents end at (0, 0, 0) and the factory at 6. With a uniform 14/3 per resident, residents end at (+2.67, +1.67, −4.33). With noisy damages assessed per resident, the expected lowest resident is −0.85σ.
  - "Compute irrelevant" is false where the assessor's estimates are what compute buys.
  - Source: Calabresi & Melamed 1972 for the definition; Kaplow & Shavell 1996 for efficiency with estimated damages; Petel 2025 as the precursor.

**Rows added**

- **A k column on every row.** Every row except row 10 is silently k=3.
- **M1, renewed consents by k.**
  - At k=3 no resident can be held below 0 in any year (computed by me; trivial veto).
  - At k ∈ {0, 1, 2} the one-shot outcome (−2, −3, −9) repeated every year is a subgame-perfect equilibrium at every δ (theorem: repeating a stage-game equilibrium is subgame-perfect [sure]).
  - Factory take-it-or-leave-it at k=3 sustains a premium g for each resident only if δ ≥ g/2 (computed by me).
  - Status: computed and theorem as marked. Sources: Fudenberg & Maskin 1986; Fudenberg & Levine 1989; Pei 2025.
- **M2, the open system.**
  - Status: argued, 1 reviewer (me). It cannot be computed on the closed river.
  - Sources: Fudenberg & Levine 1989; Kreps & Wilson 1982; Bernheim & Whinston 1986 and 1990; Snow 2025; Petel 2025.
- **M3, divide and conquer at k=1 or 2 with π=20, where pollution is efficient.**
  - Efficient, yet residents end at (−2, −3, −9) and the factory at 20.
  - Status: computed by me (k=1); k=2 [likely]. Source: Segal 1999; Segal 2003.
- **M4, private harms at k=3 under a mechanism.**
  - No efficient mechanism exists that is voluntary, balances its budget and makes truth-telling pay; compute does not enter.
  - Status: theorem once Mailath & Postlewaite 1990 is read. It is already in the essay and missing from the table; the essay's Myerson–Satterthwaite citation is two-player.
- **M5, k=0, π=10, with and without an assurance contract.**
  - Without one, contributions can collapse to (−2, −3, −9), with the factory at 10.
  - With a refund-if-short contract, the stable outcomes are core allocations: the factory keeps 10 and the residents share 4.
  - Status: theorem once Bagnoli & Lipman 1989 is read [likely]; the numbers computed by me.

**Rows retired**

- None outright.
- Row 4's "deals close late" clause.
- Row 7's "verification capacity enlarges the set" clause.

**Mission touched: no.** One observation for Dan. With row 2, the noisy-assessor liability rule and M5 included, the state's sentence "in every row where compute changes the split, it changes it toward the party that already holds a position" holds only if "position" includes "is allowed to commit". Read that way the thesis is close to circular, and the essay should state it as "toward whoever the rules let commit".

## (c) Working

The river throughout: π ∈ {10, 20}; harms h = (2, 3, 9), summing to 14; pie 6 at π=20 and k=3; no-deal payoff 0 for every party. "Worst-off" means the lowest expected payoff.

### Row 1. Take-it-or-leave-it by the factory

**1. Status.** "Computed, collator re-ran" is a claim I cannot inspect. Its source points to findings I was barred from opening. I reconstructed the computation:

- Each resident's harm is estimated as ĥ_i = h_i + e_i, with e_i ~ N(0, σ²) independent across residents.
- The factory offers ĥ_i + m; resident i accepts if the offer is at least h_i; the factory picks m to maximise expected profit at k=3.

Two versions:

| σ | Deal rate, margin fixed in advance | Deal rate, margin set after the factory sees ĥ |
|---|---|---|
| 1.5 | 33.4% | 33.7% |
| 0.01 | 99.86% | 99.89% |

The row's 34% and 99.85% agree to rounding, so "computed" stands. The row must still name its specification, since the two versions give different answers to "who ends lowest" (point 3). The unit "slices" is undefined in the row; my reconstruction matches only if a slice is one unit of harm.

**2. Source.** "findings, In cell B the margin" is acceptable for a computed row. There is no theorem to source. The row must state k=3: at k<3 a take-it-or-leave-it factory buys the cheapest consents and the residents who do not sign carry their harm uncompensated (row M3).

**3. Equity.** "Expected surplus peaks at middling budgets" is wrong as written. Total expected surplus, 6 × deal rate, rises steadily: 2.00, 3.55, 5.07, 5.89 and 5.99 at σ = 1.5, 1.0, 0.5, 0.1 and 0.01. What peaks is the residents' expected take.

| σ | Residents' expected take, margin fixed | Residents' expected take, margin after seeing ĥ |
|---|---|---|
| 1.5 | 1.52 | 1.07 |
| 1.0 | 2.27 | 1.79 |
| 0.5 | 2.18 | 2.02 |
| 0.1 | 0.74 | 0.73 |
| 0.01 | 0.10 | 0.10 |

The residents' share of each deal falls from 0.76 to 0.017 (margin fixed).

Who ends lowest:

- No resident ever ends below 0, ex post or in expectation, because a resident accepts only an offer at or above their harm.
- At σ=1.5 the identity of the lowest party depends on the version. With the margin fixed in advance, the factory is lowest (0.48 against 0.51 for each resident). With the margin set after seeing ĥ, each resident is lowest (0.36 against 0.95 for the factory).
- At σ ≤ 1.0 the residents are lowest in both versions.
- The minimum payoff peaks at middling compute: 0.36, 0.60, 0.67, 0.24 and 0.03 at σ = 1.5, 1.0, 0.5, 0.1 and 0.01 (margin after seeing ĥ). On the Rawlsian stand-in, then, more compute is good up to σ≈0.5 and bad after it.

The split among residents is hidden by the share S:

- With equal σ, each resident gets the same absolute rent (0.51 at σ=1.5). That is 25% of resident 1's harm and 6% of resident 3's.
- When the noise is proportional to harm, resident 3 gets most (0.33, 0.41, 0.99 at mean σ 1.5, with one common margin).
- "A floor set by unmeasurable harm" needs a specification. I added an unmeasurable part with sd 1.0 to resident 3's harm and let the factory set a margin per resident. At σ=0.01 the deal rate levels off at 91.5%, and the residents get (0.03, 0.03, 1.42) against 4.02 for the factory. The floor is a rent for whichever resident is least measurable, not a floor on S in general; S per deal is 0.27 there.

Within the residents, compute takes from the measurable and leaves rent with the opaque.

**5. Prior critics.** Snow 2025 made the qualitative point first: inferred minima and a "calculated lowball". Cite him. The essay's own contribution: the deal-rate curve, the hump in the residents' take and the steadily rising total, the minimum payoff peaking at middling compute, and rent going to whoever is least measurable. Older source: first-degree price discrimination and the monopsony screening textbook result, as in Tirole 1988, *The Theory of Industrial Organization*, ch. 3 [sure]. With perfect information the monopsonist pays each seller its reservation price.

### Row 2. Take-it-or-leave-it by the residents

**1. Status.** "Argued" with no reviewer count breaks the rule. The bloc half is computable, and I re-ran it:

- The residents demand π̂ − m, where π̂ = π + e with e ~ N(0, σ²).
- The factory accepts if the demand is at most π.
- The deal rate is 86.6%, 91.7%, 96.3%, 99.4% and 99.95% at σ = 1.5, 1.0, 0.5, 0.1 and 0.01.

"Mirror of the above" is false. At the same σ the bloc closes 87% of deals where the factory closes 34%, because one acceptance is needed instead of three. This is the one-against-three asymmetry showing up in estimation as well as in commitment. Promote the bloc half to computed once the collator re-runs it. The internal split stays argued until counted.

**2. Source.** Miettinen–Vanberg 2025 is a model of simultaneous probabilistic declarations by every member under q-majority rules [sure, abstract read]. It is not about how a bloc forms or splits internally. The primary for "the internal split is the hard part" is Dixit, A. & Olson, M. (2000), "Does voluntary participation undermine the Coase Theorem?", *Journal of Public Economics* 76(3): 309–335 [sure]: when participation in the bargaining coalition is voluntary, the coalition often fails to form. Also relevant is the k=3 holdout inside the bloc. Each resident's veto over the bloc's offer reproduces row 8 one level down.

**3. Equity.** The factory's expected payoff falls from 1.76 to 0.03 as σ goes from 1.5 to 0.01; its share of each deal falls from 0.34 to 0.006. The residents' take, 3.43 rising to 5.96, is split by the internal rule. At σ→0 the bloc takes 6, which equal gains split (2, 2, 2) and harm proportions split (0.86, 1.29, 3.86). The worst-off party is then the factory, at 0, which is its no-deal payoff and not below it. The column should carry the two candidate splits; "set by the internal rule" hides a factor of 4.5 between resident 1 and resident 3 under the proportional rule.

**5. Prior critics.**

- Snow: "you cannot change the leverage of the user". The bloc changes the leverage, which answers him with a number.
- Petel: a bargaining club "can become a cartel with better UX".
- Snow: the club's opt-in recreates the holdout. This applies to the internal split.

Cite all three. Older source: Dixit & Olson 2000; Olson 1965.

### Row 3. Haggling, everything known

**1. Status.** "Empirical, one study" is honest for the capability gap, but the source should name the study: Anthropic (2026-04-24), "Project Deal: our Claude-run marketplace experiment", <https://www.anthropic.com/features/project-deal> [sure, read this session]. Its numbers:

- Opus 4.5 against Haiku 4.5: as seller, Opus got $2.68 more for the same item; as buyer, it paid $2.45 less.
- Median price $12, mean $20.05.
- Of 28 participants who had Haiku in one mixed run and Opus in the other, 17 ranked the Opus run higher and 11 ranked the Haiku run higher. Perceived fairness was 4.05 against 4.06.

The benchmark "1.5 each" is a theorem: the four-player Nash bargaining solution with disagreement at 0, and the Shapley value of v(N)=6, v(S)=0 otherwise, both give 1.5 to each party [sure, standard]. Primaries: Nash, J. (1950), "The bargaining problem", *Econometrica* 18(2): 155–162; Shapley, L. (1953), "A value for n-person games", *Annals of Mathematics Studies* 28: 307–317.

"Theory of which equilibrium is open" overstates the gap:

- In multilateral alternating offers under unanimity with three or more players, any division is a subgame-perfect equilibrium for patient players (Shaked's construction, in Osborne & Rubinstein 1990, *Bargaining and Markets*, §3.13 [likely]).
- The stationary equilibrium is unique: under unanimity with equal recognition, the proposer gets 6 − 4.5δ and each of the others 1.5δ, which tends to 1.5 each [likely] (Baron, D. & Ferejohn, J. (1989), "Bargaining in legislatures", *APSR* 83(4): 1181–1206).

So the theory is not open. It says "1.5 each if stationary, anything if not".

**2. Source.** Project Deal is a multi-buyer, multi-seller market of two-party trades. It is not a four-party unanimity game, and its "better agent" is a model-tier gap (Opus against Haiku), not a compute budget within one model. Carrying it to the river is argued.

**3. Equity.** On the symmetric solution: transfers to the residents are (3.5, 4.5, 10.5); the factory keeps 1.5; every party nets +1.5. The share S = 0.75 hides that equal absolute gains are 75%, 50% and 17% of each resident's harm. A harm-proportional split of the residents' 4.5 would give (0.64, 0.96, 2.89). Nobody ends below 0. The size of "the better agent takes more" cannot be computed on the river: Project Deal reports price differences, not shares of surplus, since buyers' valuations are unobserved.

**5. Prior critics.** Snow, "models exchanging predictions", where the clearing price is an artefact of the models. Cite him. The essay's addition is the four-party benchmark and Project Deal's numbers. Older sources: Nash 1950; Shapley 1953.

### Row 4. Haggling, private harms, fast offers

**1. Status.** "Theorem" with source "economist" breaks the rule twice: the source is a reviewer, and the stated result contradicts the primary. Gul, F. & Sonnenschein, H. (1988), "On delay in bargaining with one-sided uncertainty", *Econometrica* 56(3): 601–611 [sure, read this session], proves that "in all of the equilibria the market will close quickly when the time between offers is sufficiently small". The underlying Coase conjecture result is Gul, F., Sonnenschein, H. & Wilson, R. (1986), "Foundations of dynamic monopoly and the Coase conjecture", *JET* 39(1): 155–190 [sure].

So "deals close late" is wrong under the Coase conjecture. Demote to "argued, 1 reviewer". To promote to theorem, restate the row as "one-sided: deals close fast, and the uninformed party that makes the offers loses its power to the informed residents", then read GSW 1986.

**2. Source.** Two problems.

- Both theorems are two-player: one buyer and one seller. On the river the factory faces three sellers of complementary consents. The three-seller dynamic version with private harms has no primary here; the land-assembly holdout literature is the place to look (e.g. Menezes & Pitchford, "A model of seller holdout", *Economic Theory* 2004 [likely]), and none was read.
- The essay's private setting has residents ignorant of π as well. That is two-sided uncertainty, and there delay can survive fast offers: Cramton, P. (1992), "Strategic delay in bargaining with two-sided uncertainty", *Review of Economic Studies* 59(1): 205–225 [likely]; Gul–Sonnenschein's own footnote 2 says the same [sure]. If the row means two-sided, "deals close late" may be right, but under Cramton, not under Coase.

**3. Equity.** The column cannot be computed: the information rents depend on the harm distribution F, which the river leaves unspecified. A computable specification: each h_i independent and uniform on {2, 3, 9}, π=20, and the factory offering a personal price path to each resident.

Note the structure. The top harm 9 times three residents is 27, which exceeds 20. So the factory cannot afford to pay every resident the highest possible harm. This is the "no gap" case, where Coasian logic does not deliver a deal for certain.

Who ends lowest cannot be said until this is run. Only the factory can end below 0 in expectation: residents accept only offers at or above their harm.

**5. Prior critics.** None of Snow, Petel or Ngo. Textbook source: Coase, R. (1972), "Durability and monopoly", *JLE* 15(1): 143–149 [sure]; GSW 1986.

### Row 5. Both commit, sealed, unconditional, once

**1. Status.** "Theorem, read in full" names a primary, and I confirmed the core statements from the text this session [sure]. When commitment is cheap and sticks with probability q<1, the unique outcome is that both try to commit to the whole surplus, so conflict happens with probability q². That outcome survives iterated elimination of strictly dominated strategies. At q=1 there are also equilibria in which one party takes everything, and the game becomes Chicken. Ellingsen, T. & Miettinen, T. (2008), "Commitment and conflict in bilateral bargaining", *AER* 98(4): 1629–1635. Status stands.

**2. Source.** Bilateral. On the river, "both" must mean the factory and a residents' bloc whose internal split is already fixed, which is row 2's hard part. With four separate committers, the right primary is row 8's Miettinen–Vanberg. My crude four-player version, in which any two incompatible commitments sticking means conflict, gives conflict probability 0.69 at q=0.5 and 0.996 at q=0.9 [illustrative, not a theorem]. "Any information" is right for the bilateral result: estimation does not enter.

**3. Equity on the river.** Factory against bloc, pie 6, with a fallback split b when neither commitment sticks:

| q | Conflict | Exactly one commitment sticks (that side takes 6) | Neither sticks | Expected payoff, each side |
|---|---|---|---|---|
| 0.9 | 81% | 18% | 1% | about 0.57 |
| 0.5 | 25% | 50% | 25% | 2.25 (b = 3 each) |

Nobody ends below 0 (k=3). The column's "no pie" hides two things. The outcomes other than conflict are winner-take-all (6 against 0). And the residents' expected share is split by the same unspecified internal rule.

**5. Prior critics.** Ngo: commitments and disagreement points decide the outcome, and standard theory under-weights threats. Cite him. The essay's additions: Ellingsen–Miettinen stated correctly, q² on the river, the move from Chicken to a Prisoner's Dilemma. Older sources: Schelling, T. (1956), "An essay on bargaining", *AER* 46(3): 281–306; Crawford, V. (1982), "A theory of disagreement in bargaining", *Econometrica* 50(3): 607–637 [both sure].

### Row 6. Both commit, publication in sequence

**1. Status.** "Argued, six of six" has the right form. There is now a primary for the multilateral version, which the row lacks: Hang, Z. & Wen, Q. (2026), "On unanimity bargaining with commitment", *Economic Theory Bulletin* 14: article 5, doi:10.1007/s40505-026-00309-4 [sure, abstract and introduction read this session]. Under unanimity with sequential commitment attempts, the unique stationary Markov-perfect equilibrium has immediate, efficient agreement. "The first successful committer effectively becomes the proposer", and later players demand no more than their continuation values.

Proposed: promote "first committer wins, deal closes" to theorem after a full read. Keep "one claimant beats three" as argued, six of six. The "Chicken risk dominance" clause needs Harsanyi, J. & Selten, R. (1988), *A General Theory of Equilibrium Selection in Games*, MIT Press, named in the Source column [sure].

**2. Source.** Hang & Wen narrows the row. The first committer gets the proposer's advantage, not the pie. In the stationary unanimity game with four parties and pie 6, the proposer gets 6 − 4.5δ and each other party 1.5δ [likely]: 6 against 0 at δ=0, 3.75 against 0.75 at δ=0.5, 1.95 against 1.35 at δ=0.9. "Takes the pie" is the δ→0 limit. The table's "once" must say whether it means one round (δ=0) or one negotiation with rounds inside it.

"Any" information is wrong. With noisy estimates, a first-moving factory is a take-it-or-leave-it offerer, and the deal closes 34% of the time at σ=1.5 (row 1), not always.

**3. Equity.**

- Factory first, δ=0: the factory gets 6 and the residents (0, 0, 0).
- Bloc first: the bloc gets 6, split (2, 2, 2) or (0.86, 1.29, 3.86).
- One resident first, among four separate committers under Hang & Wen at δ=0.9: that resident gets 1.95 and every other party 1.35.

Nobody ends below 0 at k=3. The column's "toward the concentrated side" should carry these numbers.

**5. Prior critics.** Ngo (commitment) and Snow (leverage) for "commitment decides". Petel's "one human, one principal, one accountable agent" for one against three. Petel's opposite sign (commitment as a friction that agents remove) should be stated with his name. Older source: Schelling 1956, where the first to commit wins.

### Row 7. Both commit, instructions read each other

**1. Status.** "Theorem" with primaries named; the Source column is correct.

**2. Source.** Both results are two-player:

- Kalai, A. T., Kalai, E., Lehrer, E. & Samet, D. (2010), "A commitment folk theorem", *GEB* 69(1): 127–137. The abstract says "All feasible and individually rational payoffs of a two-person strategic game" [sure, read].
- Tennenholtz, M. (2004), "Program equilibrium", *GEB* 49(2): 363–373 [likely two-player].

Applying them to four players is argued. Nash-style program equilibrium in a four-player game also ignores deviations by coalitions. On the river at k<3, the factory and a single resident can gain jointly by deviating, which is exactly the empty-core problem of row 10.

"Verification capacity enlarges the set" has no source in either paper. Retire it, or source it, for example to DiGiovanni, A. & Clifton, J. (2023), "Commitment games with conditional information disclosure", AAAI [unsure that it supports this].

**3. Equity.** "Individually rational" means at or above each party's minmax:

- At k=3 every party's minmax is 0, so any division of 6 with every share at least 0 is supported, including factory 6 and residents (0, 0, 0).
- At k=1 or k=2 a resident's minmax is −h_i, because others can consent without them. So the factory at 20 with residents at (−2, −3, −9), at π=20, is an equilibrium of the conditional-commitment game.

The column's "undetermined" hides that a resident can be held below no deal, by up to 9.

**5. Prior critics.** None of the three. Older source: the folk theorem generally, and Schelling 1960 for focal points.

### Row 8. Many residents under unanimity, binding declarations

**1. Status.** "Theorem, abstract read" fails the rule, which requires the primary text. I also read only the abstract (Miettinen, T. & Vanberg, C. (2025), "Commitment and conflict in unanimity bargaining", *AEJ: Microeconomics* 17(1): 206–237, doi:10.1257/mic.20230208 [sure, abstract]). The full text was blocked by bot protection on both open-access copies. Demote to "theorem in its own model, abstract only" until it is read in full.

**2. Source.** The abstract describes "a distributive multilateral bargaining model". Before each round, players may declare a minimum share, which binds with a given probability. The paper characterises the stationary subgame-perfect equilibria under all q-majority rules: "unanimity rule is uniquely inefficient", and all other rules are "fully efficient".

On the river this holds at k=3 only, as a four-party division of 6. At k<3 the river is not a pure division game: those left out of the winning coalition are harmed. At π=10:

- k=2: {factory, 1, 2} pollute for a joint 10 − 5 = 5, leaving resident 3 at −9 and welfare at −4.
- k=1: {factory, 1} pollute for a joint 8.

Both pollute although pollution is inefficient. "Efficient under every other rule" must be cut to "in a pure division game".

Hang & Wen 2026 adds that the unanimity inefficiency comes from simultaneous timing; sequential commitment under unanimity is efficient. The pair of rows 6 and 8 is that paper's result. "Once or repeated" in the row should read "rounds until agreement, discounted", since Miettinen–Vanberg is not a renewal game.

**3. Equity.** "The split among residents is where the fight is" carries no number. It cannot be computed until the stationary equilibrium is read from the full text. Specification: n=4, unanimity, pie 6, commitment success probability p, discount δ; report the expected delay and each party's expected payoff. In expectation nobody ends below 0 at k=3.

**5. Prior critics.** Snow: the club's opt-in recreates the holdout. Cite him. The essay's additions are the arithmetic and the theorem that unanimity alone is inefficient. Older source: Buchanan, J. & Tullock, G. (1962), *The Calculus of Consent*, on the decision costs of unanimity [sure].

### Row 9. Repeated play, patient parties

**1. Status.** The bracketed confidence marks are not statuses, and the source is a reviewer plus "Dan's objection", neither of which is a primary.

- Folk theorem: Fudenberg, D. & Maskin, E. (1986), "The folk theorem in repeated games with discounting or with incomplete information", *Econometrica* 54(3): 533–554 [sure]. That is a normal-form result; using it on a bargaining stage game is argued.
- Lock-in: no primary named. The obvious candidate says the reverse over the long run. Young, H. P. (1993), "An evolutionary model of bargaining", *JET* 59(1): 145–168: precedent locks in a convention without noise, but with small noise the long run selects the Nash solution, and a split of 50:50 when the classes mix [sure, abstract read]. Lock-in holds only over a medium horizon.
- Tilt: Young's model, where each side's sample size of past play is the exponent on its utility in the Nash product [likely, from Wallace & Young 2015's survey, not the primary]. That is a theorem about the estimation dial.
- Thresholds: I computed one. With factory take-it-or-leave-it as the stage game at k=3, and the residents punishing any deviation by refusing forever (which costs them nothing), a premium g for each resident is sustainable if δ ≥ g/2. The equal split, g=1.5, needs δ ≥ 0.75; g=1.9 needs δ ≥ 0.95; the residents can never take all 6.
- Counter-model to "no convergence": Pei, H. (2025), "Commitment, conflict, and status quo in bargaining", arXiv:2503.01053 [sure, abstract]. In two-player repeated bargaining where the status quo is the last split that held, patient players with cheap commitment have Markov-perfect equilibria that are close to efficient and fair.

**2. Source.** Pei and Young are two-player or two-class. Fudenberg–Maskin is n-player but normal-form.

**3. Equity.** Who ends lowest per year:

- k=3: at or above 0 for every resident, in every equilibrium.
- k<3: as low as (−2, −3, −9).

With a Young-style tilt, linear utility and the pie of 6:

| Sample sizes | Factory | Each resident |
|---|---|---|
| Equal | 1.5 | 1.5 |
| Factory's 3 times each resident's | 3.0 | 1.0 |
| Factory's 10 times each resident's | 4.62 | 0.46 |

Across residents, the one with the weakest agent (smallest sample) gets least. The column reports none of this.

**5. Prior critics.** Ngo's "Schelling fence" touches convention as a precommitment, partly. Otherwise none. Older sources: Friedman, J. (1971), "A non-cooperative equilibrium for supergames", *RES* 38(1): 1–12 [sure]; Lewis, D. (1969), *Convention*, Harvard UP [sure]; Young 1993. "Better agents lock in the first convention" is the textbook path-dependence result under a new name.

### Row 10. Divide and conquer, k=1, π=10

**1. Status.** "Computed" is verified. I re-ran it:

- Payoffs: factory 10, residents (−2, −3, −9), with the signer getting a token ε more; welfare −4.
- Core: the residents together guarantee 0, and the grand coalition's best is 0, so the factory's payoff is 0. Each resident then needs 10 − h_i, that is 8, 7 and 1, summing to 16 against a pot of 0.

The Tullock part, "the economist's", is not a primary and has no count. I computed it two ways:

- With the residents' stakes pooled: a stake of 14 against the factory's 10 gives the residents a win probability of 0.583.
- With residents spending separately: in a group contest for a prize that is a public good within each group, only the member who values the prize most spends anything. Baik, K. H. (2008), "Contests with group-specific public-good prizes", *Social Choice and Welfare* 30: 103–117 [result sure from the abstract; pages likely]. So only resident 3 spends, the contest is 9 against 10, and the residents win with probability 0.474. Equilibrium efforts are 2.24 against 2.49.

Stakes still decide, but the one-against-three asymmetry appears here too: free-riding among residents costs them about 11 points of win probability.

**2. Source.** Segal, I. (1999), "Contracting with externalities", *QJE* 114(2): 337–388, is a theorem for one principal and many agents, so it fits four players [sure]. Also Aivazian, V. & Callen, J. (1981), "The Coase theorem and the empty core", *JLE* 24(1): 175–181 [sure]. Tullock, G. (1980), "Efficient rent seeking", in Buchanan, Tollison & Tullock (eds.), *Toward a Theory of the Rent-Seeking Society*, Texas A&M UP, 97–112 [sure].

**3. Equity.** Who ends lowest: resident 3, at −9. All three residents end below 0, at −2, −3 and −9. The column says "all three below no deal" without the numbers; it should carry them. The within-residents split is reported only implicitly.

**5. Prior critics.** Petel's flash-coalition griefing, with the sign reversed, is adjacent (as the overlap table says). No critic made the divide-and-conquer point. Textbook sources: Rasmusen, E., Ramseyer, J. M. & Wiley, J. (1991), "Naked exclusion", *AER* 81(5): 1137–1145; Segal 1999. The essay's addition is the river's arithmetic and the Baik correction.

### Row 11. One side adapts, the other is fixed

**1. Status.** "River application argued" has no count. The source is a reviewer, though the primaries are named in brackets:

- Press, W. & Dyson, F. (2012), "Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent", *PNAS* 109(26): 10409–10413 [sure].
- Deng, Y., Schneider, J. & Sivan, B. (2019), "Strategizing against no-regret learners", NeurIPS 32, arXiv:1909.13861: an optimiser facing a no-regret learner can secure at least its Stackelberg value [sure].

Move these into the Source column. The status should read "theorems in their own two-player settings; river application argued, count needed".

**2. Source.** Both are two-player and neither is a bargaining game. Bargaining primaries to read:

- Ellingsen, T. (1997), "The evolution of bargaining behavior", *QJE* 112(2): 581–602, on obstinate against sophisticated (adaptive) bargainers [sure the paper exists; unsure of its exact share result].
- Abreu, D. & Gul, F. (2000), "Bargaining and reputation", *Econometrica* 68(1): 85–118. With a small probability of inflexible types and frequent offers, equilibrium is unique and involves delay, and limit payoffs are inversely proportional to the parties' discount rates [sure, abstract].

All are two-player.

**3. Equity.** On the river at k=3:

- A rigid factory demanding the whole 6 against adaptive residents: factory 6, residents (0, 0, 0).
- A rigid bloc against an adaptive factory: bloc 6, factory 0.
- Residents rigid separately, each demanding all of 6: no deal, as in row 5.

Who ends lowest is the adapting side, at exactly 0; never below 0 at k=3. At k<3 the adapting residents fall to (−2, −3, −9). The column reports none of these.

**5. Prior critics.** Ngo: credible threats and following through on commitments. Snow: leverage, not strategy. Cite both. Older sources: Schelling 1960 on the "rationality of irrationality"; von Stackelberg 1934.

### Row 12. Liability rule in statute

**1. Status.** "By construction" is not one of the three statuses. The definition is Calabresi, G. & Melamed, A. D. (1972), "Property rules, liability rules, and inalienability: one view of the cathedral", *Harvard Law Review* 85(6): 1089–1128 [sure]. "Efficient if the price is right" is a theorem in Kaplow, L. & Shavell, S. (1996), "Property rules versus liability rules: an economic analysis", *Harvard Law Review* 109(4): 713–790 [sure]: damages need only be right on average for the polluter's decision to be efficient. The equity numbers are computed (I re-ran them).

**2. Source.** These are not game results, so player count does not arise. But "compute irrelevant" is false once the damages are assessed rather than known. The assessor's estimation compute is the estimation dial in neutral hands.

**3. Equity at π=20.**

- Damages equal to each resident's own harm: residents (0, 0, 0), factory 6, nobody below 0.
- A uniform statutory schedule of 14/3 per resident: residents (+2.67, +1.67, −4.33), factory 6. Resident 3 ends 4.33 below no deal. The column's "whatever the statute sets" hides this.
- Damages assessed per resident with noise σ: the expected lowest resident is −0.85σ, which is −1.27 at σ=1.5 and −0.008 at σ=0.01. The chance that at least one resident ends below 0 stays at 87.5% while the size of the shortfall shrinks. Pollution is still chosen 99% of the time at σ=1.5.

This row is a counterexample to the table's one-sentence answer: here more estimation compute helps the worst-off.

**5. Prior critics.** Petel: Calabresi–Melamed, and software's preference for liability rules. Cite him. The essay's additions: the uniform-schedule numbers, the noisy-assessor result, and the point that a liability rule changes the entitlement.

### Proposed row M1. Renewed consents (the repetition column, by k)

| Condition | Information | Repetition | Who can commit | Efficiency | Equity | Status | Source |
|---|---|---|---|---|---|---|---|
| Same parties set terms every year, at k=3 | transparent | renewed each year, discount δ | factory (stage game: take-it-or-leave-it) | deal every year | Impatient: factory 6 per year, residents 0. Patient: premium g per resident sustainable if δ ≥ g/2 (1.5 each needs δ ≥ 0.75); no resident is ever below 0 | computed (me); folk theorem pending a read | Fudenberg & Maskin 1986; Pei 2025 |
| Same, at k ∈ {0, 1, 2} | transparent | renewed each year | factory | pollution every year, efficient at π=20, inefficient at π=10 | Residents (−2, −3, −9) per year, the factory 10 or 20, at every δ | theorem (repeating a stage equilibrium is subgame-perfect [sure]); numbers computed | Segal 1999 for the stage game |
| Same, with turnover among residents, or a factory with a reputation | any | factory long-run, residents short-run | factory, through reputation | deal | The factory approaches its commitment payoff of 6 per year at k=3; residents 0 | theorem in its own setting [sure]; river application argued | Fudenberg & Levine 1989, *Econometrica* 57(4): 759–778; Kreps & Wilson 1982, *JET* 27(2): 253–279 |

Can a resident be held below no deal in a repeated equilibrium? At k=3, no: each resident can refuse every year and get 0. At k<3, yes, at every δ.

I also checked whether patient residents can sustain a clean river at k=1, π=10, using the stage outcome as the punishment. They cannot. The factory will pay up to 10/(1−δ) for one signature, since the punishment phase pays it 10 a year. Resident 1's price is only 2/(1−δ). So the factory buys resident 1 at every δ. Whether a harsher self-enforcing punishment exists is unresolved (my derivation, unchecked).

To compute the remaining cells on the river: fix the stage game (factory take-it-or-leave-it, or alternating offers within each year); set δ from 0.5 to 0.99; for each k, compute (i) the best and worst stationary payoffs, and (ii) the set sustainable by the harshest punishment that enforces itself.

**Prior critics.** Ngo's commitments and Schelling fences, partly. Pei 2025 is newer than all three.

### Proposed row M2. The open system

| Condition | Information | Repetition | Who can commit | Efficiency | Equity | Status | Source |
|---|---|---|---|---|---|---|---|
| Agents in many bargains at once; reputation and the vendor's incentives carry across principals | reputations visible across bargains | many rivers, in sequence or in parallel | whoever is in many bargains: the factory's agent, or a vendor serving many principals | deals close | The party in many bargains becomes a long-run player and gets close to its commitment payoff; on the river, the factory's 6 per river at k=3, with residents at 0. A vendor representing several principals has its own payoff and can trade one principal's outcome for another's. Linking bargains pools incentive constraints and makes collusion between agents easier | argued, 1 reviewer (me) | Fudenberg & Levine 1989; Kreps & Wilson 1982; Bernheim & Whinston 1986, "Common agency", *Econometrica* 54(4): 923–942; Bernheim & Whinston 1990, "Multimarket contact and collusive behavior", *RAND JE* 21(1): 1–26 [all sure] |

It cannot be computed on the closed river. A minimal computable version, which is a second model and so a sequel by the mission's rule, is a chain store. The river is played M times in sequence, against fresh residents each time, by one factory agent that has a prior μ of being a commitment type offering exactly h_i. Compute the factory's equilibrium payoff and the residents' as functions of M, μ and δ, in the finite-horizon Kreps–Wilson way.

**Prior critics.**

- Snow's bundling vignette (47 deals overnight; overriding one costs £120 because the bundle must be renegotiated) is an open-system observation. Cite him.
- Petel: "one human, one principal, one accountable agent"; platform defaults as hidden planners; a cartel with better UX. Cite him.

The essay's addition would be that reputation turns the party in many bargains into the committer, which on the river is the factory.

### Proposed row M3. Divide and conquer when pollution is efficient (k=1 or 2, π=20)

| Condition | Information | Repetition | Who can commit | Efficiency | Equity | Status | Source |
|---|---|---|---|---|---|---|---|
| k=1 (or 2), π=20, consents bought one by one | transparent | once | factory | efficient: pollution happens, total surplus 6 | Factory 20; residents (−2, −3, −9); all three below 0, resident 3 by 9 | computed (me) for k=1; k=2 [likely] | Segal 1999; Segal, I. (2003), "Coordination and discrimination in contracting with externalities: divide and conquer?", *JET* 113(2): 147–181 [likely] |

This is the cleanest case on the river where efficiency and Pareto tests pass and the inequality-sensitive test fails. Compute plays no part: the price of a signature falls to 0 at any estimation budget. No published critic made it first. Textbook source: Segal 1999.

### Proposed row M4. Private harms at k=3, mechanism design

| Condition | Information | Repetition | Who can commit | Efficiency | Equity | Status | Source |
|---|---|---|---|---|---|---|---|
| k=3, harms private | each resident knows own harm, drawn from F | once | a mechanism designer | no mechanism that is voluntary, balances its budget and rewards honesty is efficient for certain; the chance of efficiency falls as n grows | depends on F; the information rents go to residents | theorem once read | Mailath, G. & Postlewaite, A. (1990), "Asymmetric information bargaining problems with many agents", *RES* 57(3): 351–367 [sure]; Rob, R. (1989), "Pollution claim settlements under private information", *JET* 47(2): 307–333 [likely] |

The essay already makes this claim, but cites Myerson & Satterthwaite 1983 (*JET* 29(2): 265–281), which is a two-player theorem being applied to a four-player game; Mailath & Postlewaite is the n-agent version.

To compute it at n=3: set F, for example each h_i independent and uniform on [0, 9], with π=20. Solve the second-best mechanism: pollute if π exceeds the sum of h_i + λ·F(h_i)/f(h_i), with λ set so the budget balances. Report the probability of the efficient action and each resident's expected rent.

Compute's effect: none, unless compute removes the privacy, in which case this row becomes row 1. No published critic made it first.

### Proposed row M5. k=0, π=10, with and without an assurance contract

| Condition | Information | Repetition | Who can commit | Efficiency | Equity | Status | Source |
|---|---|---|---|---|---|---|---|
| k=0, residents pay the factory to abate, voluntary contributions | transparent | once | nobody | contributions can collapse (residents 1 and 2 free-ride; resident 3 can raise only 9 of the 10 needed): pollution, welfare −4 | Residents (−2, −3, −9), factory 10 | computed (me; the essay's numbers) | Olson 1965; Bergstrom, Blume & Varian (1986), *J Pub Econ* 29(1): 25–49 [sure] |
| Same, with a contract that refunds everyone unless 10 is raised | transparent | once | the contract | stable outcomes are core allocations: abatement | Factory 10; residents share the surplus of 4, e.g. contributions (1, 2, 7) leave residents (+1, +1, +2); every resident at or above 0 | theorem once read [likely] | Bagnoli, M. & Lipman, B. (1989), "Provision of public goods: fully implementing the core through private contributions", *RES* 56(4): 583–601; Tabarrok, A. (1998), "The private provision of public goods via dominant assurance contracts", *Public Choice* 96: 345–362 [likely] |

Here cheap contract machinery, which is what software agents supply, improves the outcome for every resident. It is a smuggled condition with a positive sign, and the table needs one to treat the foil fairly. No published critic made it first.

### Unaudited issues for the collator

- The one-sentence answer says "every repeated one adds only lock-in". Young 1993 (long-run selection) and Pei 2025 (fair equilibria) each contradict that in one model.
- Several rows say "once" while relying on multi-round results (rows 6, 8). The Repetition column needs to separate rounds within a negotiation (δ) from renewal of consents (M1).
