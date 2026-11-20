# Hard-case instance: the noise schedule

Stage 0 of the hard-case round, 2026-10-21. Every agent in the round computes on these numbers and no others. Dan signs this off before stage 1 starts. The river's numbers (harms 2, 3, 9; profit 10 or 20) are not used here except for comparison.

## The baseline (all switches off: parametric, once, linear money, enforcer assumed, closed)

A fleet chooses which of four slots to run deliveries in: morning M, midday D, evening E, night N. Schedule $x\in\{0,1\}^4$. Profit per slot used: $p=(4,\ 5.5,\ 4,\ 5)$.

Three residents with public exposure profiles over the slots, $e_i$, and a private sensitivity $s_i$; harm $h_i(x)=s_i\sum_t e_{it}x_t$.

| Resident | Exposure $e_i$ (M, D, E, N) | Sensitivity $s_i$ (private) | Reading |
|---|---|---|---|
| 1 | (0.5, 0, 0.5, 1) | 1 | out by day, home at night |
| 2 | (1, 1, 0.5, 0.5) | 1 | home all day |
| 3 | (0.5, 0.5, 1, 2) | 2 | near the road, sleeps badly |

Total harm per slot used, $\sum_i s_ie_{it}$: (2.5, 2, 3, 5.5). Surplus per slot, $p_t$ minus that: (1.5, 3.5, 1, −0.5).

Efficient schedule: M, D and E, not N. Profit 13.5, harms (1, 2.5, 4), total 7.5, **pie 6**, the river's pie. Running all four slots gives profit 18.5 against harms (2, 3, 8) and a pie of 5.5, so an all-or-nothing contract leaves half a unit on the table; the clause menu is worth 0.5 here. Consent rule $k=3$ at baseline.

## The switches (each on in some arm of the round)

- **Arbitrary preferences.** Resident 3's harm becomes a table over the 16 schedules: the additive value above plus 1.5 whenever M and E are both used (no midday rest). Residents 1 and 2 stay additive. The efficient schedule then changes to M and D only, profit 9.5, harms (0.5, 2, 2), **pie 5**; the parametric optimum M, D, E now yields only 4.5. So one private interaction term flips the decision, and the information that flips it is not a scalar. Agents who need a harder version may let all three residents carry interaction terms; say so if they do.
- **Recurring.** The schedule is renegotiated every period; discount factor $\delta\in\{0.5,\ 0.8,\ 0.95\}$.
- **Wealth effects.** Utility of money $u(w)=\log(w_0+w)$ with endowments $w_0=(10,\ 10,\ 2)$ for the residents and $100$ for the fleet; resident 3 is poor.
- **No enforcer.** Either any pact among residents must be self-enforcing in the repeated game, or a platform enforces and also fixes the clause language: four slots, or two (day and night), or one (all or nothing).
- **Finite budgets.** The fleet estimates each $s_i$ with error $\sigma/\sqrt{c_f}$; the residents estimate each $p_t$ with error $\sigma/\sqrt{c_N}$; $\sigma=1$; budget ratios $c_f:c_N\in\{1{:}1,\ 10{:}1,\ 1{:}10\}$ at levels giving errors of 1, 0.3 and 0.1.
- **Remediation.** Insulation for resident $i$ halves $e_i$ at a public cost of 2, decided with the schedule.
- **Consent rule.** $k=2$ as an alternative to $k=3$.
- **Outside option.** The fleet can reroute at a cost of 3 per slot, as an alternative to no deal.

## Measures, reported for every arm

**Primary criterion, locked in by Dan 2026-10-21: the Nash product of gains over no deal**, equivalently the sum over the four parties of the logarithm of each party's gain, with no deal as the origin; in utility units, $u(w_0+\text{payoff})-u(w_0)$, when the wealth-effects switch is on. "Better" in the mission question means higher under this criterion. **Floor check:** the worst-off party's gain over no deal. **Reported but not part of "better":** the pie realised against the maximum (6 parametric, 5 arbitrary), the residents' share of it, and the split among the three residents. At finite budgets, report the expected values of all of these counting failed deals as zero, beside the limit.

## Why these numbers

Chosen so that: the parametric pie equals the river's 6, for comparison; the night slot is inefficient by a small margin, so that estimation error at finite budgets can flip it; the arbitrary interaction is a single, plausible term (sleep) that changes the efficient decision; resident 3 is the most harmed and the poorest, so that the incumbent reading and the wealth-effects switch act on the same person; and everything is small enough to enumerate by hand (16 schedules).
