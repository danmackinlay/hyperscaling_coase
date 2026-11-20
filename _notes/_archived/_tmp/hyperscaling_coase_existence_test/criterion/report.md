# Criterion agent's report (Opus), existence-test round, 2026-10-21

Saved verbatim by the session from the agent's final message; the agent's own write of this file was refused by the harness. The two scripts `criteria.py` and `row1_grid.py` are the agent's; run from the repo root with `uv run python -I <path>`. The Monte Carlo uses seed 0 and 400,000 draws, so third decimals can move by about 0.002.

Payoffs are on the model's own scale: u_f = πx − Σt, u_i = t_i − h_i·x. That puts the clean river with no transfers at (0;0,0,0) under every rule. Vectors are written (factory; r1, r2, r3), with harms (2, 3, 9).

## (a) Answer on the river's numbers

Define "better" as a higher **floor**: the lowest expected payoff among the four parties. The benchmark is the equal split of the efficient total: 1.5 each at π=20, 0 each at π=10. On that measure, more compute improves the outcome in only two places:

- **Fast offers against private harms.** Fast offers erode the uninformed factory's power. If each harm is known only to within ±1.5, the floor rises from 0.88 to 1.5. If the range is ±2, the floor falls instead, to 0, because the factory is squeezed to nothing.
- **Take-it-or-leave-it up to a middling budget.** Better estimation cuts failed deals. The floor rises from 0.48 to 0.80 as the factory's error falls from 1.5 to 0.76 slices.

Everywhere else more compute lowers the floor or leaves it where the rules put it:

- **Take-it-or-leave-it past that budget.** The offerer takes nearly all of the 6. At error 0.01 the floor is 0.033, whichever side makes the offer.
- **Sealed commitment.** Cheap but slightly unreliable commitment turns 1.5 each into a standoff 81% of the time at q=0.9, and the floor falls to 0.195.
- **Sequence, better agent, adaptation.** Publication in sequence, a better agent on one side, or one side adapting while the other stays rigid each move the floor from 1.5 (1 for a coin flip over who publishes first) to between 1.3 and 0. The gain goes to whoever publishes first, has the better agent, or stays rigid.
- **Equilibrium sets.** When instructions read each other, or under patient repeated play, the floor can land anywhere from 0 to 1.5. A focal rule or the first convention decides where, not compute.
- **k=1 at π=10.** The floor is −9 (resident 3) whatever anyone spends.

For whom: the gains go to the side that commits, publishes or stays rigid. On the river that is the factory whenever one principal moves faster than three. Residents gain from compute only through the speed of the factory's own offers, when their harms are private.

## (b) Delta

`Delta to state, 2026-10-21:`

**Rows changed.** Every row's equity column is re-headed "Floor before → after on the row's dial (for whom)" and takes the values in table C2. Unless marked otherwise, each row's status is "computed by the criterion agent's script, not yet re-run by the collator". Source: `_tmp/hyperscaling_coase_existence_test/criterion/criteria.py`. Changes beyond the re-heading:

- **Take-it-or-leave-it by the factory.**
  - The factory's profit-maximising margin reproduces the row's deal rates: 33.3% at error 1.5 (the row says 34%; a margin of 0.778 gives 34.06%) and 99.85% at error 0.01.
  - Equity becomes "floor 0.48 → 0.80 at error 0.76 → 0.033 at error 0.01". Each resident goes from 0.52 to 0.033 and the factory from 0.48 to 5.89.
  - At error 1.5 the floor is the factory's: it overpays, and 7.2% of all draws leave it below no deal.
- **Take-it-or-leave-it by the residents.**
  - Efficiency is not "mirror of the above". The deal rate goes from 87% to 99.95% as error falls from 1.5 to 0.01, because one acceptance decides the deal, not three.
  - Equity: floor 1.14 → 0.033 under an equal-gains internal split, and 0.49 → 0.033 under a split proportional to harm. In both, the factory ends as the floor.
- **Haggling, all known.**
  - The floor stays at 1.5 under a symmetric upgrade.
  - It falls to 1.3 if the factory's agent is better by 0.6 (a tenth of the pie), and to 0.9 if one resident's agent is worse by 0.6.
  - The 0.6 is an assumption. Project Deal measured about an eighth of the mean item price [sure], which does not map directly onto a share of the pie.
- **Haggling, private harms, fast offers.**
  - With each harm private and uniform within ±1.5 of its true value, the floor goes 0.88 → 1.5. Within ±2 it goes 0.63 → 0, with the factory squeezed to nothing. The crossover is near ±1.75.
  - Status: computed under an assumed prior. Applying the Coase conjecture to three complementary consents is [unsure].
- **Both commit, sealed.** Floor 1.5 → 0.195 at q=0.9, with a standoff 81% of the time. At q=1 each of the three outcomes has floor 0. Ellingsen–Miettinen read this session [sure].
- **Sequence.** Floor 1 (coin flip for who publishes first, ex ante) → 0, with the factory taking 6.
- **Instructions read each other.** Floor 0.195 (sealed, q=0.9) → anywhere in [0, 1.5]. The best needs a symmetric focal rule; the worst is no deal.
- **Unanimity with binding declarations.**
  - Floor 1.5 → 1.5ρ, where ρ is the share of the pie that survives the delay. ρ is not computed: only the abstract was read [sure for the abstract].
  - Add to the row: the paper's "fully efficient under every other rule" does not carry over to the river. At k=2 the resident who does not consent bears the harm uncompensated: illustratively a total of 6 but a floor of −9. Status: argued.
- **Repeated play.** Per-period floor in [0, 1.5]. Lock-in keeps it wherever the first convention put it; a tilt lowers it (illustratively to 1.3).
- **k=1, π=10.** Floor −9 under every dial. The contest variants give −5.94 and −6.98, and neither moves with the price of compute.
- **One side adapts.** Floor 1.5 → 0; the rigid side takes 6.
- **Liability rule.** The floor is whatever the statute sets: 0 under compensatory damages, 1.5 under damages of h_i+1.5. Better court estimation raises only the ex post floor, from −1.28 to −0.01.

**Rows added.** None.

**Rows retired.** The open row "The welfare criterion itself" moves to the mission.

**Mission touched: yes**, because "better" needs a definition and the measures are the mission's. Replace the "Outcome measures" section with this text:

> **Outcome measure.** "Better" means a higher **floor**: the lowest expected payoff among the four parties, with the factory and each resident counted once and alike. Payoffs are on the model's own scale (u_f = πx − Σt_i, u_i = t_i − h_i·x, so the clean river with no transfers is 0 for everyone under every rule), never gains over a rule's no-deal point. A party's payoff is its expectation over the row's uncertainty, with a failed deal at its no-deal payoff. Ties are broken by the next-lowest payoff, and so on (leximin). The benchmark is the equal split of the efficient total: 1.5 each at π=20, 0 each at π=10. "Just under the criterion" in the existence test means a floor near that benchmark.
>
> Always report alongside it, never instead of it:
>
> - the expected payoff vector, which says for whom;
> - the efficient-action rate and the expected total, as the efficiency placeholder;
> - the ex post floor (the expected value of the realised minimum), where it differs;
> - whether anyone ends below no deal, as a flag rather than a criterion;
> - the Kolm–Pollak equally-distributed equivalent at α = 0.5 and 1 per slice, wherever its sign differs from the floor's, so that a verdict that rests on how much inequality aversion we assume says so.
>
> Where an outcome is a set, report the best, worst and focal floor, and name the rule that picks each.
>
> Rejected:
>
> - the Nash product of gains: its zero is the rule's own no-deal point, and it is undefined below that point;
> - "nobody below no deal": weaker than Pareto, since it passes a failed deal;
> - power means: they need wealth levels that the model leaves out.

## (c) Working

### C1. The criterion and its defence

The proposal is leximin on expected payoffs, on the model's own scale, with the factory counted as one party. In practice that means the floor, with ties broken from the bottom up.

On the river it does what the question asks of it:

- **It sees the split among residents.** In the residents' take-it-or-leave-it row at error 1.5, the residents' total share S=3.43 is the same under both internal rules. The floor is 1.14 with equal gains and 0.49 with gains proportional to harm.
- **It sees a failed deal.** A deal that gives the factory all 6 beats no deal on the tie-break, though both have floor 0.
- **It ranks a deal against the clean river at π=20.** The equal split scores 1.5 against 0.
- **It ranks pollution against the clean river at π=10, and pollution outcomes against each other.** Pollution scores −9 against 0. Between two pollution outcomes, buying out resident 1 beats the k=1 race on the third-lowest payoff (0.5 against −1.99).
- **It treats the factory as a resident.** Concentrating the pie on the residents is as bad as concentrating it on the factory: when the residents publish first or stay rigid, the floor is the factory's 0. That keeps the criterion fair to the foil.
- **It needs no parameter.** A reader can check every value by sorting four numbers.

The alternatives each fail on the river:

- **The bare minimum.** It gives every value in C2 the same as leximin, but it ties a failed deal with a deal that hands one party everything.
- **The Nash product of gains over no deal.**
  - It is also zero for both a failed deal and a lopsided one.
  - It is undefined below no deal. Truncated to −∞ there, it cannot order the outcomes at π=10 or k=1. Left raw, it misranks: polluting at π=10 with resident 1 bought for 2.5 scores 7.5×0.5×(−3)×(−9) = +101, above the clean river's 0, because two of the factors are negative.
  - It measures from the rule's own no-deal point, so it inherits the entitlement the essay is asking about. At k=0, residents paying (1, 2, 7) to keep the river clean gain (0; 1, 1, 2) over pollution, and the Nash product rates that outcome no better than no deal. On the model's scale the same outcome is (10; −1, −2, −7), with floor −7.
  - It is flat to first order at the symmetric split. A better agent taking 0.6 costs it 9%, against the floor's 13%. When the 0.6 comes from a single resident, it costs 16% against 40%.
- **"Nobody below no deal".** This is a constraint, not an ordering, and it is weaker than Pareto. It passes the failed deal, the standoff and every all-to-one split, and it cannot rank a deal at π=20 against the clean river. At π=10 it flags pollution but cannot say by how much. Under court error it reads 87% below no deal at errors of both 1.5 and 0.01, although the realised floor goes from −1.28 to −0.01.
- **Power means (Atkinson).** They need positive levels. The river's payoffs are negative wherever pollution goes uncompensated, so an endowment would have to be invented, and that number would then set the inequality aversion.
- **Kolm–Pollak.** It works on any real payoffs, and it is the honest sensitivity check. But its parameter α is in units of 1/slice, and its sign on rows 1, 2 and 4 flips between α = 0.5 and α = 1. A reader cannot check a verdict that rests on a parameter the essay chose.

Leximin has a known cost: it is the most inequality-averse member of the family. It rates row 1 at error 0.01 (total 5.99, residents on 0.033 each) below row 1 at error 1.5 (total 2.04, floor 0.48), and a utilitarian would call that perverse. The essay should say plainly which claims need that much aversion: only rows 1 and 2 (see C3).

Expected payoffs rather than realised ones: the brief asks for expectations, and a reader can check them. A fair lottery over who takes everything is fair ex ante (Diamond's 1967 point [sure]) and maximally unequal ex post. So the ex post floor goes in its own column. In C2 it never turns a loss into a gain; in row 6 it turns a loss into no change.

Blind spots on the river:

| Question (river instance) | Floor | Leximin (proposed) | Nash product of gains | Nobody below no deal | Kolm–Pollak, α=1 | Total (placeholder) |
|---|---|---|---|---|---|---|
| Split among residents (row 2, error 1.5: equal gains vs proportional to harm, S=3.43 both) | 1.14 vs 0.49: yes | yes | 2.64 vs 1.40: yes | pass/pass: no | 1.27 vs 1.07: yes | 5.19/5.19: no |
| Failed deal vs all-to-factory, (0;0,0,0) vs (6;0,0,0) | 0 vs 0: no | yes | 0 vs 0: no | pass/pass: no | 0 vs 0.29: yes | 0 vs 6: yes |
| Equal deal vs clean river, π=20 | 1.5 vs 0 | yes | 5.06 vs 0 | pass/pass: no | 1.5 vs 0 | 6 vs 0 |
| Pollution vs clean river, π=10 (race (9.99; −1.99, −3, −9)) | −9 vs 0 | yes | −∞ (truncated); raw sign arbitrary | fail vs pass, no magnitude | −7.62 vs 0 | −4 vs 0 |
| Among pollution outcomes (race vs r1 bought at 2.5) | −9 = −9: no | yes, third-lowest 0.5 > −1.99 | −∞ = −∞; raw +101 > 0 misranks | fail = fail | −7.62 vs −7.62 (tie at 2 d.p.) | −4 = −4 |
| Rule-independent zero (k=0 deal paying 1, 2, 7) | −7 | −7 | 0 (gains over pollution) | pass | −5.62 | 0 |
| Factory treated as a resident | yes | yes | yes | yes | yes | yes |
| Parameter-free | yes | yes | yes | yes | no (α) | yes |

### C2. Every row, every candidate, before → after on the row's own dial

Signs: + better, − worse, = unchanged. "Nash" is the product of expected gains (gains equal payoffs here, because no deal is 0 at k=3), set to −∞ if any expected gain is negative. "Below" is the probability that someone ends strictly below no deal. KP is Kolm–Pollak, −(1/α)·ln((1/4)·Σ_j exp(−α·E u_j)). "Total" is the expected sum of payoffs, the efficiency placeholder.

| Row; dial; before → after | E[u] before → after | **Floor (proposed)** | Ex post floor | Nash | Below | KP α=1 | KP α=0.5 | Total |
|---|---|---|---|---|---|---|---|---|
| 1 TIOLI factory; estimation; error 1.5 → 0.01; margin 0.778 → 0.033; deal 34.1% → 99.85% | (0.48; 0.52 ×3) → (5.89; 0.033 ×3) | 0.48 → 0.033 **−** (peak 0.80 at 0.76) | 0.032 → 0.024 − | 0.068 → 0.0002 − | 7.2% → 0 + | 0.51 → 0.32 − | 0.51 → 0.57 + | 2.04 → 5.99 + |
| 2a TIOLI residents, equal-gain split; estimation; error 1.5 → 0.01; margin 1.66 → 0.033; deal 86.6% → 99.95% | (1.76; 1.14 ×3) → (0.033; 1.99 ×3) | 1.14 → 0.033 **−** | 0.85 → 0.033 − | 2.64 → 0.26 − | 0.19% → 0 + | 1.27 → 1.07 − | 1.28 → 1.30 + | 5.19 → 6.00 + |
| 2b same, split ∝ harm | (1.76; 0.49, 0.74, 2.21) → (0.033; 0.85, 1.28, 3.83) | 0.49 → 0.033 **−** | 0.44 → 0.033 − | 1.40 → 0.14 − | 0.19% → 0 + | 1.07 → 0.86 − | 1.18 → 1.10 − | 5.19 → 6.00 + |
| 3 Haggling, known; capability; symmetric upgrade | (1.5 ×4) → same | 1.5 → 1.5 = | = | = | = | = | = | = |
| 3′ factory's agent better by 0.6 | → (2.1; 1.3 ×3) | 1.5 → 1.3 **−** | same | 5.06 → 4.61 − | 0 → 0 = | 1.5 → 1.45 − | 1.5 → 1.47 − | 6 → 6 = |
| 3″ r1's agent worse by 0.6 | → (2.1; 0.9, 1.5, 1.5) | 1.5 → 0.9 **−** | same | 5.06 → 4.25 − | = | 1.5 → 1.41 − | 1.5 → 1.46 − | = |
| 4a Private harms ±1.5; speed; one-shot offer → fast-offer limit | (1.76; 0.88 ×3) → (1.5; 1.5 ×3) | 0.88 → 1.5 **+** | 0.44 → 0.70 + | 1.20 → 5.06 + | 0 → 0 = | 1.04 → 1.5 + | 1.07 → 1.5 + | 4.40 → 6 + |
| 4b same, ±2 | (1.27; 0.63 ×3) → (0; 2 ×3) | 0.63 → 0 **−** | 0.32 → 0 − | 0.32 → 0 − | = | 0.76 → 1.05 + | 0.77 → 1.29 + | 3.16 → 6 + |
| 5 Sealed commitment; commitment; too costly (nobody commits) → cheap, q=0.9 | (1.5 ×4) → (0.555; 0.195 ×3) | 1.5 → 0.195 **−** | 1.5 → 0.015 − | 5.06 → 0.004 − | 0 → 0 = | 1.5 → 0.27 − | 1.5 → 0.28 − | 6 → 1.14 − |
| 5′ q=1: conflict / factory all / residents all | (0;0,0,0) / (6;0,0,0) / (0;2,2,2) | 0 / 0 / 0 | 0 | 0 | = | 0 / 0.29 / 1.05 | 0 / 0.54 / 1.29 | 0 / 6 / 6 |
| 6 Sequence; speed; coin flip for first → factory faster | (3; 1 ×3) → (6; 0 ×3) | 1 → 0 **−** | 0 → 0 = | 3 → 0 − | = | 1.24 → 0.29 − | 1.34 → 0.54 − | 6 → 6 = |
| 7 Instructions read each other; verification; sealed q=0.9 → program-equilibrium set | (0.555; 0.195 ×3) → set | 0.195 → [0, 1.5]: best equal split, worst no deal | 0.015 → [0, 1.5] | 0.004 → [0, 5.06] | = | 0.27 → [0, 1.5] | 0.28 → [0, 1.5] | 1.14 → [0, 6] |
| 8 Unanimity, binding declarations; commitment; never bind → bind with probability p | (1.5 ×4) → (1.5ρ ×4) | 1.5 → 1.5ρ **−** (ρ unread) | same | 5.06 → 5.06ρ⁴ − | = | 1.5 → 1.5ρ − | same | 6 → 6ρ − |
| 8′ k=2 on the river (illustrative) | (12; 1.5, 1.5, −9) | −9 | −9 | −∞ | 100% | −7.61 | −6.25 | 6 |
| 9 Repeated, patient; adaptation/estimation; equal agents → better agents lock in and tilt | per period: set → first convention, tilted (illustrative (2.1; 1.3 ×3)) | [0, 1.5] → locked; 1.3 if tilted **−** | same | [0, 5.06] → 4.61 | = | [0, 1.5] → 1.45 | [0, 1.5] → 1.47 | 6 per period (0 if no deal is the convention) |
| 10 k=1, π=10, race; any dial | (9.99; −1.99, −3, −9) both | −9 → −9 **=** | −9 = | −∞ = | 100% = | −7.62 = | −6.38 = | −4 = |
| 10′ contest if spending is chosen: residents as a bloc / r3 alone; same under any price of compute | (1.74; −1.32, −1.98, −5.94) / (2.77; −1.05, −1.58, −6.98) | −5.94 / −6.98 = | same | −∞ | 100% | −4.58 / −5.60 | −3.63 / −4.45 | −7.5 / −6.84 |
| 11 One adapts; adaptation; symmetric → residents adapt, factory rigid | (1.5 ×4) → (6; 0 ×3) | 1.5 → 0 **−** | same | 5.06 → 0 − | = | 1.5 → 0.29 − | 1.5 → 0.54 − | 6 → 6 = |
| 11′ → factory adapts, residents rigid | → (0; 2 ×3) | 1.5 → 0 **−** | same | 5.06 → 0 − | = | 1.5 → 1.05 − | 1.5 → 1.29 − | = |
| 12 Liability, compensatory damages; court estimation; error 1.5 → 0.01 | ≈ (6; 0 ×3) both | 0 → 0 **=** (1.5 under a schedule of h_i+1.5) | −1.28 → −0.01 + | ≈0 = | 87% → 87% = | 0.29 = | 0.54 = | 6 = |

**Sets, and which rule picks which.**

- **Row 7.** By Tennenholtz [sure], every individually rational division is a program-equilibrium outcome.
  - The floor's best is the equal split, 1.5 each. Nash, Kalai–Smorodinsky and equal division all give it here, because utility is transferable and the parties are symmetric. It is picked when the shared protocol codes a symmetric bargaining solution as the default: a rule.
  - The worst deal gives one side everything (floor 0), as in row 11: the side whose conditional program is the template takes the pie, against an adapting counterpart.
  - The worst outcome overall is no deal (floor 0, last on the tie-break). It happens when no one coordinates on the programs.
  - Better verification enlarges the set but chooses nothing within it.
- **Row 9.** By the folk theorem [sure], each period's floor can be anything from 0 (perpetual no deal, or all to one side) to 1.5. The pick is the first convention; better agents lock it in [sure] and tilt it toward the better-informed side [likely]. The tilt of 0.6 is illustrative, since the row's thresholds are unchecked.

**Arithmetic, row by row.** Φ and φ are the standard normal CDF and density, and z = m/σ.

- **Row 1.** Each resident is offered ĥ_i+m with ĥ_i = h_i+ε_i, ε_i ~ N(0,σ²), and accepts iff ε_i ≥ −m.
  - Deal rate Φ(z)³. E u_i = Φ²(mΦ+σφ). E u_f = Φ³(6−3m) − 3Φ²σφ.
  - Margin assumption: m = σ·Φ⁻¹(rate^(1/3)), which gives 0.778 at error 1.5 for 34% and 0.0329 at error 0.01 for 99.85%. The factory's optimal margins are 0.759 and 0.033, so the row's rates are the factory's own choice.
  - At error 1.5: z=0.519, Φ=0.698, φ=0.349, so E u_i = 0.487×(0.543+0.523) = 0.519 and E u_f = 0.340×3.666 − 0.765 = 0.482.
  - Peak: floor 0.800 at error 0.76 (margin 0.958, deal 72%), where the residents' gain also peaks.
- **Row 2.** The residents demand π̂−m, and the factory accepts iff ε ≤ m.
  - E u_f = mΦ+σφ. Residents' total = Φ(6−m) − σφ.
  - At error 1.5 with m=1.659: Φ=0.866, φ=0.217, so E u_f = 1.436+0.325 = 1.761 and the residents' total is 3.758−0.325 = 3.433.
  - Ending below no deal requires ε < m−6 = −4.34, which has probability 0.19%.
- **Row 3.** (1.5+d; 1.5−d/3 ×3), or (1.5+d; 1.5−d, 1.5, 1.5), with d=0.6. Nash: 2.1×1.3³ = 4.61 and 2.1×0.9×2.25 = 4.25.
- **Row 4.** H_i ~ U[h_i−a, h_i+a], private.
  - One-shot: the factory posts p_i = h_i−a+y with y* = min((6+3a)/4, 2a). Each resident accepts with probability y/2a. The factory nets 6+3a−3y in a deal. A resident's expected gain is (y²/4a)·(y/2a)².
  - At a=1.5: y=2.625, acceptance 0.875, deal rate 0.670, factory 0.670×2.625 = 1.759, resident 1.148×0.766 = 0.879.
  - Fast-offer limit in the gap case (20 ≥ Σ(h_i+a)): the factory pays the top of each support, so it gets 6−3a and each resident a.
  - At a=1 the one-shot offer already pays the top, so speed changes nothing.
- **Row 5.**
  - Before: commitment cost above q(1−b_i), so nobody commits, and the residents' bargaining share without commitment is b_R = 3/4 (1.5 each).
  - After: c→0 at q=0.9, so both commit to the whole pie. Probabilities: conflict 0.81, factory takes all 0.09, residents take all 0.09 (2 each), neither commitment sticks 0.01 (1.5 each).
  - E u_f = 0.09×6 + 0.01×1.5 = 0.555. E u_i = 0.09×2 + 0.01×1.5 = 0.195. Ex post floor = 0.01×1.5 = 0.015.
- **Row 6.** 0.5×(6;0,0,0) + 0.5×(0;2,2,2) = (3;1,1,1).
- **Row 8′.** The factory buys residents 1 and 2 at harm plus 1.5: 20−3.5−4.5 = 12, and resident 3 bears −9.
- **Row 10.** The race: (10−ε; ε−2, −3, −9) with ε=0.01.
  - Contest: Tullock lottery with stakes V_f=10 and V_R. Efforts x_f = V_f²V_R/(V_f+V_R)² and x_R = V_f·V_R²/(V_f+V_R)²; pollution happens with probability V_f/(V_f+V_R).
  - Bloc (V_R=14): x_f=2.43, x_R=3.40 split in proportion to harm, P=0.417.
  - Resident 3 alone (V_R=9): x_f=2.49, x_3=2.24, P=0.526.
  - The lottery contest is unchanged when the cost of effort is scaled [sure], so the price of compute does not enter.
- **Row 12.** Damages are h_i+ε_i, so a resident's realised gain is ε_i. The expected minimum of three draws is about −0.846σ: −1.27 at error 1.5 and −0.0085 at 0.01. Below no deal = 1−(1/2)³ = 0.875 at any σ>0.

### C3. Sign changes

The rows fall into four classes. The class, not the choice among inequality-averse criteria, decides the sign.

1. **Pareto-worse, or stuck below the benchmark.** Row 5 is worse under every candidate except "nobody below", which shows no change. Row 10 has the same bad value under every candidate, before and after.
2. **Same total, more unequal.** Rows 3′/3″, 6, 11 and the tilt in 9 are worse under every strictly inequality-averse criterion (floor, leximin, Nash, KP at any α) [sure: an equal split beats every unequal split of the same total under strict Schur-concavity]. They show no change under total surplus and under "nobody below". Row 6 also shows no change under the ex post floor.
3. **More total, more unequal.** Rows 1 and 2, and 4b. The sign rests on the degree of aversion.
   - Row 1: worse under the floor, Nash and KP α=1; better under KP α=0.5, total and "nobody below".
   - Row 2a: the same pattern, but KP α=0.5 is only barely better (1.28 → 1.30). Row 2b is worse under KP α=0.5 as well.
   - Row 4b: worse under the floor and Nash, better under both KP values and total.
   - Row 1 is also non-monotone: every candidate improves from error 1.5 to about 0.76, and the floor, Nash and KP α=1 then fall.
4. **More total, more equal.** Row 4a, and row 12's ex post floor, are better under every candidate.

Rows 7 and 9 are sets. Every candidate's range covers the benchmark and the worst case, and the dial does not choose between them.

### C4. Does the existence test's verdict depend on the choice?

No. The null fails under every candidate:

- under every candidate through row 10, which stays below the benchmark whatever is spent, with the clean river reachable only by an imposed pact or a different k: a rule;
- under every candidate except "nobody below" through row 5;
- under every strictly inequality-averse candidate through rows 3, 6 and 11.

Only "nobody below no deal" hangs the verdict on row 10 alone. That criterion is weaker than Pareto and so fails the mission's own requirement.

What does depend on the choice is the thesis rather than the verdict. The incumbent reading, that compute moves the split toward whoever already holds a position, is invisible under total surplus and under "nobody below": both show rows 3, 6 and 11 as unchanged and rows 1 and 2 as improvements. It shows under any strictly inequality-averse criterion that counts the factory as a party and is defined below no deal. Within that family, rows 1 and 2 need strong aversion (the floor, or KP at α ≥ 1 per slice), and rows 3, 5, 6, 10 and 11 need only that the criterion be strictly inequality-averse. The essay should rest its spine on rows 5, 6, 10 and 11, with row 3 beside them, and present rows 1 and 2 as "past a middling budget, under strong aversion".

**Is the question answerable in a form a reader can check?** Yes. Every row reduces to a payoff vector or a lottery of at most four, and the criterion is the lowest entry of the expected vector. A reader can check rows 3, 5, 6, 7, 9, 10, 11 and 12 by hand, and rows 1 and 2 with the normal CDF and the formulas above. Two inputs remain assumptions: row 4 rests on an assumed prior width, and row 8 on an unread delay factor.

**The answer in one sentence:** on the river, more compute raises the worst-off party's expected payoff only where it eliminates failed deals up to a middling budget or erodes the power of an uninformed offerer, and wherever it buys commitment, speed or adaptation it lowers that floor from the equal split's 1.5 toward 0 by handing the pie of 6 to whichever side commits, publishes or stays rigid first, while at k=1 the floor stays at −9 whatever is spent.

### Sources

- Ellingsen & Miettinen 2008, AER 98(4), read this session [sure]. With a small commitment cost and q<1, both sides commit to the whole surplus, and conflict occurs with probability q² even for large q. At q=1 there is the conflict outcome plus equilibria in which one side takes everything, and efficient compromise is unattainable. With a commitment cost of zero and q>1/2, an efficient equilibrium exists (Crawford's case), but it vanishes for any small positive cost.
- Miettinen & Vanberg 2025, AEJ Micro (working paper 2024), abstract only [sure for the abstract]. Declarations bind with an exogenous probability; unanimity is uniquely inefficient; every other q-majority rule is fully efficient. The size of the delay was not read.
- Anthropic, Project Deal, April 2026, read this session [sure]. On the same items, Opus did about $2.68 better than Haiku as a seller and $2.45 better as a buyer; the mean price was $20.05; perceived fairness was essentially identical (4.05 against 4.06).
- Gul–Sonnenschein–Wilson 1986, the Coase conjecture with a gap [sure for one seller and one buyer]. Its extension to three complementary consents is [unsure].
- Tennenholtz 2004 on program equilibrium [sure]. The folk theorem [sure]. The lottery-contest equilibrium and its scale invariance [sure]. That only the highest-stake member of a group spends in a group contest (Baik) [likely]. Diamond 1967 on fair lotteries [sure].
