# Specification: two rounds of company-made offers

This is a self-contained specification of a small game-theory calculation.
Implement it from this text alone, in a new directory, and report the numbers requested at the end.
The only other file you may read is `claimed_equilibrium.json` beside it; do not read anything in the parent directory.

## The street

A delivery company can run deliveries in four time slots, t = M, D, E, N.
Running slot t earns the company `m * P[t]`, with `P = (4, 5.5, 4, 5)`.
The multiplier `m` is public.

There are three households, i = Alice, Bob, Carol.
Each has a public exposure to each slot:

| | M | D | E | N |
|---|---|---|---|---|
| Alice | 0.5 | 0 | 0.5 | 1 |
| Bob | 1 | 1 | 0.5 | 0.5 |
| Carol | 0.5 | 0.5 | 1 | 2 |

Each household has a sensitivity `s_i`, known only to that household, drawn independently and uniformly from [0.5, 2.5].
If slot t runs, household i suffers harm `s_i * e[i][t]`.
The sensitivities are the same in both rounds.

There is also a second, smaller configuration, "Carol alone": one household (Carol), one slot (N), `P_N = 5`, exposure 2.
Everything below applies to it with the other households and slots removed.

## What the company knows

Before round one the company holds a public signal about each household: `x_i = s_i + sigma * z_i`, `z_i` standard normal and independent.
Its belief about `s_i` is the Bayesian posterior given the uniform prior and `x_i` (a normal truncated to [0.5, 2.5]).
`sigma = inf` means it knows only the prior.
The signals, `m`, `sigma`, and every offer and answer are common knowledge; only each `s_i` is private.

## One round

The company names a set of slots and offers each household it chooses to ask one rate `r_i` per unit of exposure (the same rate for every named slot).
Households answer simultaneously, accept or refuse.
A named slot runs if every household with non-zero exposure to it accepted.
If slot t runs, the company earns `m * P[t]` and pays each accepting household `r_i * e[i][t]`; household i gains `(r_i - s_i) * e[i][t]`.
A household not asked counts as refusing.

## Two rounds

The game is one round, then a second round, with gains added and the second round weighted by `delta` (1 unless stated).
The company cannot commit in round one to its round-two offers.
Report all gains as per-round averages: (round one + delta * round two) / (1 + delta).

Three regimes:

**Forget.**
The company's round-two offers ignore the round-one answers, and everyone knows this.
Each round is then the one-round game with the pre-round-one beliefs: the company chooses the named slots and rates to maximise its expected profit, and household i accepts exactly when `r_i >= s_i`.

**Myopic.**
The company updates its beliefs on the round-one answers and makes round-two offers that are optimal given the updated beliefs.
Households do not anticipate this: in each round household i accepts exactly when `r_i >= s_i`.
The company chooses its round-one offers to maximise expected profit over both rounds, knowing all this.

**Strategic.**
As myopic, but households anticipate the round-two consequences of their round-one answers and answer to maximise their own expected gain over both rounds.
Solution concept: perfect Bayesian equilibrium in cutoff strategies.
In round one each asked household i accepts exactly when `s_i <= c_i`.
After acceptance the company's belief about `s_i` is its prior belief truncated to `s_i <= c_i`; after refusal, truncated to `s_i > c_i`.
Round two is the one-round game under those beliefs (household i accepts exactly when `r_i >= s_i`, since nothing follows).
The round-one rate that supports cutoff `c_i` makes type `c_i` indifferent:

`(r1_i - c_i) * E_i = delta * G_i`

where `E_i` is household i's expected exposure in round one if it accepts (the sum over named slots it is exposed to of `e[i][t]` times the probability that every other exposed household accepts), and `G_i` is the expected round-two gain of a household of type `c_i` that refused (expectation over the other households' round-one answers and round-two answers, using the public beliefs about them).
A type-`c_i` household that accepted gains nothing in round two, because the company never offers it more than `c_i`.

A cutoff profile is an equilibrium only if, for every asked household, every type below the cutoff weakly prefers accepting and every type above weakly prefers refusing, given the round-two play that follows each answer.
Check this; do not assume it.
(It fails when the household's expected exposure after refusing exceeds its expected exposure in round one.)

Two further round-one choices are available to the company for each household: not asking it, and asking it at the top of the support of its belief, which every type accepts; after either, the company's belief about that household is unchanged (for the second, a refusal is off the equilibrium path and is assumed to leave the belief unchanged).

The company chooses, among round-one offers for which a cutoff equilibrium exists, the one that maximises its expected profit over both rounds.
This restriction is part of the specification.

## What to compute

Part A, "Carol alone", `m = 1`, averaging over Carol's sensitivity and the signal, for `sigma = inf, 0.3, 0.1`:
for each regime, the per-round average of total gain, company gain, and Carol's gain.
Here the cutoff is one-dimensional, so solve it finely (a cutoff grid of at least 200 points, or a continuous optimiser) and say what you did.
Also report, for the strategic regime at `sigma = inf`, the company's chosen cutoff and round-one rate.

Part B, the street, `m = 1`, `sigma = inf`, averaging over the sensitivities:
1. Forget: per-round total, company, and summed household gain.
2. Myopic: the same three numbers, and the company's round-one offer (named slots, rate per household).
3. Strategic: the same three numbers, the company's round-one offer and the cutoffs, and the share of the cutoff profiles you examined that passed the equilibrium check.
   Let each household's cutoff range over at least these quantiles of the prior: 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 0.97, 0.99, plus "not asked" and "asked at the top".
   A finer grid is welcome; if you use one, report both.

Part C, a verification task.
The file `claimed_equilibrium.json` next to this specification describes one claimed strategic equilibrium on the street (`m = 1`, `sigma = inf`): the round-one named slots, rates and cutoffs, and the round-two offers after each pattern of answers.
Check independently whether (a) each round-two offer is optimal for the company given the truncated beliefs, to within 0.02 of expected profit, (b) each round-one rate satisfies the indifference condition, and (c) no household type gains by deviating in round one.
Report what you find, including any discrepancy however small.

For the one-round optimisations, do not restrict rates to a coarse fixed grid, or show that refining the grid does not move the answer.
Report means with standard errors where you use Monte Carlo, and say where you integrated exactly.
