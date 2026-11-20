# Specification: four bargaining rules on a small noise-schedule model

This is a self-contained specification of a small economic simulation.
Implement it from this text alone and report the numbers requested at the end.

## The model

A delivery company can run deliveries in four time slots, t = M, D, E, N.
Running slot t earns the company `m * P[t]`, with `P = (4, 5.5, 4, 5)`.
The multiplier `m` is known only to the company and is drawn uniformly from [0.6, 1.4].

There are three households, i = Alice, Bob, Carol.
Each has a public exposure to each slot:

| | M | D | E | N |
|---|---|---|---|---|
| Alice | 0.5 | 0 | 0.5 | 1 |
| Bob | 1 | 1 | 0.5 | 0.5 |
| Carol | 0.5 | 0.5 | 1 | 2 |

Each household has a sensitivity `s_i`, known only to that household, drawn independently and uniformly from [0.5, 2.5].
If slot t runs, household i suffers harm `s_i * e[i][t]`.

Insulation (optional switch): any subset of households can be insulated.
Insulating household i halves its exposure in every slot and costs 2 per insulated household.
The cost is paid by whoever makes the offers (rules A and C) or by the company (rules B1, B2), and it is paid up front, whether or not any slot then runs.

Everything is measured as a gain over "no deal" (no slot runs, nobody pays anything, gain 0 for all).
Total gain = company profit from slots that run − households' harm from slots that run − insulation cost.

"The worked case" means `s = (1, 1, 2)` and `m = 1`.
In the worked case the best total gain is 6 without insulation (slots M, D, E) and 7.5 with it (all four slots, Carol insulated).

## The accuracy dial

A party that makes offers does not know the others' private values.
It holds a noisy signal of each: `signal = true value + sigma * z` for a household's sensitivity, and `signal = m + 0.4 * sigma * z` for the company's multiplier, with `z` standard normal, independent across parties and observers.
Its belief is the Bayesian posterior given the uniform prior and that signal (a normal truncated to the prior's support).
`sigma = inf` means it knows only the prior; `sigma = 0` means it knows the value exactly.

## The four rules

**Rule A, tailored offers by the company.**
The company knows its own `m`.
It chooses a set of households to insulate, and, for each slot independently, either makes no offer or offers each exposed household i a rate `r[i][t]`.
All offers are made simultaneously, before any answers.
Household i accepts the slot-t offer exactly when `r[i][t] >= s_i`.
Slot t runs only if every household with non-zero exposure to it accepts; then the company pays household i `r[i][t] * (its exposure after insulation)`.
A household with zero exposure to a slot is not asked and not paid.
The company chooses insulation and rates to maximize its expected profit given its beliefs.

**Rule C, lottery over who makes the offers.**
With probability 1/4 each, the company or one of the three households is the offer-maker.
If the company is drawn, rule A applies.
If household j is drawn, it knows its own `s_j`, and it chooses the insulation set and, for each slot independently, either no offer, or: a price `d[t] * P[t]` demanded from the company, and a rate `r[i][t]` for each other exposed household.
The company accepts slot t exactly when `m >= d[t]`; the other households accept as under rule A.
Slot t runs only if the company and every other exposed household accept.
Household j then receives `d[t] * P[t]` from the company, pays the other households their rates times exposure, and bears its own harm; it also pays for any insulation.
It maximizes its expected gain given its beliefs.
Report also "household seat": the average over j of the outcome when household j is the offer-maker (that is, rule C restricted to the three household draws, each with probability 1/3).

**Rule B1, one uniform rate, consent kept.**
A rate `r` per unit of exposure is fixed in advance and is the same for every household and slot.
Each household vetoes every slot it is exposed to if `s_i > r`, and no slot otherwise.
The company, knowing `m` and the vetoes, picks the insulation set and the set of non-vetoed slots that maximize `m * P·x − r * (total exposure after insulation of the slots run) − insulation cost`.
If it is indifferent about a slot it runs it.
Each household is paid `r` times its exposure after insulation in the slots run.

**Rule B2, one uniform rate, no individual consent.**
As B1 but nobody can veto: the company may run any slot provided it pays the rate.

## What to compute

Use Monte Carlo over the population (draw `s`, `m`, and the signals), at least 3,000 draws, and report means with standard errors.
For rules A and C the offer-maker's problem is an optimization over rates (and over `d`); solve it by whatever method you trust, and say what you did.
Use a method that does not restrict offers to a coarse fixed grid, or show that refining the grid does not move the answer.

Report, for the population, both with insulation switched off and with it on:

1. The best achievable total gain (the full-information optimum), mean over draws.
2. Rule A at sigma = inf, 0.3, 0.1 and 0: mean total gain, company gain, and summed household gain.
3. Household seat at sigma = 0.3 and 0: the same three numbers.
4. Rule C with every offer-maker at sigma = 0.3: the same three numbers.
5. Rules B1 and B2 at r = 1.5, 1.9, 2.0 and 2.5: the same three numbers, and for B2 the probability that a given household's gain is negative.

And for the worked case (`s = (1,1,2)`, `m = 1`, averaging over signals only):

6. Rule A at sigma = 0.3 and 0.1, with insulation off and on: mean total gain, company gain, and each household's gain.
7. Rules B1 and B2 at r = 1.9, 2.0 and 2.5, insulation off and on: total, company, and each household's gain.
