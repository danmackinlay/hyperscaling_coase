# Which rules protect a household from the company's predictions, and what each costs

Written 2026-11-18.

## The idea tested

Bargaining in Krier's world has two phases. In the *rule-choosing* phase the parties settle the rules: who may make offers, whether offers may differ between households, whether a household may refuse. In the *deal-making* phase their agents agree, under those rules, which deliveries run and who is paid what.

The idea was that, in deal-making, two things pull against each other: pricing each household by its own circumstances, and the household keeping a share of the gain. An agent that can predict the least a household will accept can offer exactly that. A price that is the same for everyone cannot be aimed at anyone, but it fits nobody exactly.

This note computes deal-making under four fixed rules to see whether that trade-off is real and how large it is. A later section plays the first rule twice with the same households, to see whether a household can protect itself by refusing an offer. The note does not model rule-choosing.

## The model

A delivery company can run deliveries in four slots. Three households are exposed to each slot by a publicly known amount:

| | Morning | Midday | Evening | Night |
|---|---|---|---|---|
| Company's profit if the slot runs | 4 | 5.5 | 4 | 5 |
| Alice's exposure (out by day) | 0.5 | 0 | 0.5 | 1 |
| Bob's exposure (home all day) | 1 | 1 | 0.5 | 0.5 |
| Carol's exposure (beside the road) | 0.5 | 0.5 | 1 | 2 |

Each household has a private *sensitivity*. Its harm from a slot is its sensitivity times its exposure. A slot is worth running when the company's profit exceeds the sum of the three harms. The *total gain* is the profit from the slots that run minus the harm they cause; it is measured against no deliveries and no payments, as is each party's own gain.

In the worked case the sensitivities are 1, 1 and 2. The morning, midday and evening slots are then worth running and the total gain available is 6. This is the model of the earlier rounds.

Two things are new here.

- **Sensitivities come from a population.** Each household's sensitivity is drawn evenly from 0.5 to 2.5, and results are averages over 4,000 simulated streets, so they are not accidents of one street.
- **The company's profit is private too.** Each street's profits are the figures above times a factor drawn evenly from 0.6 to 1.4, known only to the company.

One switch is used in result 6. *Insulation* halves one household's exposure in every slot at a cost of 2. Whoever makes the offers decides who is insulated and pays for it before the answers come in; under a uniform rate the company decides and pays.

## What is varied

Whoever makes offers has an estimate of each other party's private number. Its *prediction error* is the standard deviation of that estimate around the truth (normal noise). "Population only" means it knows the range and nothing about the particular party. "Exact" means it knows the number. An error of 0.3 on a sensitivity is about a seventh of the range. When a household makes offers, its error about the company's factor is scaled to that factor's narrower range.

## The four rules

- **Company offers.** The company's agent offers each household a payment rate per unit of exposure, for each slot, once and finally. Rates may differ between households and slots. A household accepts a rate at or above its sensitivity. A slot runs only if every exposed household accepts.
- **Uniform rate, veto kept.** One rate per unit of exposure, the same for every household and slot, is fixed beforehand by someone who knows only the population. A household refuses every slot if the rate is below its sensitivity. The company runs whichever permitted slots still pay. Nobody's prediction enters.
- **Uniform rate, no veto.** The same, but no household can refuse: the company may run any slot it pays the rate for.
- **Lottery.** A fair draw picks one of the four parties to make the offers. If the company wins, this is the first rule. If a household wins, say Bob, then for each slot Bob names a price the company must pay and a rate for each neighbour; the slot runs if the company and the neighbours all accept; Bob keeps the company's price, less what he pays the neighbours, and bears his own harm.

## Results

Averages over the population, rounded to one decimal, so a row can differ from its sum by 0.1. The best total gain possible, with every private number known, is 6.2. The standard error of a total is about 0.06.

| Rule | Prediction error of whoever makes offers | Total gain | Households | Company |
|---|---|---|---|---|
| Company offers | population only | 4.6 | 2.0 | 2.5 |
| | 0.3 | 5.4 | 1.6 | 3.8 |
| | 0.1 | 5.9 | 1.0 | 5.0 |
| | exact | 6.2 | 0 | 6.2 |
| Uniform rate 2.5, veto kept | none needed | 4.0 | 2.1 | 1.9 |
| Uniform rate 1.5, no veto | none needed | 5.9 | 0.0 | 5.8 |
| Uniform rate 2.0, no veto | none needed | 5.1 | 1.8 | 3.4 |
| Lottery | all four population only | 3.7 | 2.5 | 1.3 |
| | company exact, households population only | 4.1 | 2.0 | 2.2 |
| | company exact, households 0.3 | 5.2 | 2.9 | 2.3 |
| | company exact, households 0.1 | 5.8 | 3.7 | 2.1 |
| | all four exact | 6.2 | 4.7 | 1.6 |

The uniform rates shown were picked from these:

| Uniform rate | Veto kept: total | Veto kept: households | No veto: total | No veto: households | No veto: households paid less than their harm | by, on average |
|---|---|---|---|---|---|---|
| 1.5 | 1.6 | 0.5 | 5.9 | 0.0 | 47% | 1.1 |
| 2.0 | 3.0 | 1.3 | 5.1 | 1.8 | 21% | 0.35 |
| 2.25 | 3.7 | 1.8 | 4.7 | 2.2 | 9% | 0.2 |
| 2.5 | 4.0 | 2.1 | 4.0 | 2.1 | 0 | – |
| 3.0 | 2.9 | 1.7 | 2.9 | 1.7 | 0 | – |

With the veto kept, 2.5 gives both the highest total and the highest households' gain. It is the top of the population's range, the lowest rate nobody refuses.

1. **When the company always makes the offers, better prediction does two things at once.** As its error falls from population-only to exact, the total gain rises from 4.6 to 6.2, because it finds more slots worth running, and the households' gain falls from 2.0 to nothing. The company's own gain rises by 3.7, of which about 1.6 is new gain and 2.0 is taken from the households.

2. **A uniform rate with the veto kept makes the households' gain independent of anyone's prediction, and loses about a third of the total gain.** The total is 4.0 of 6.2 and the households get 2.1. The households do about as well as under the first rule when the company knows only the population (2.0), and the total is lower (4.0 against 4.6).

3. **Without the veto, a uniform rate keeps most of the total gain and pays some households less than their harm.** At the population's average sensitivity, 1.5, the total is 5.9, the households gain nothing on average, and 47% of them are paid less than their harm. Raising the rate lowers that share and the total together, until at 2.5 nobody is underpaid and the outcome is that of result 2.

4. **The lottery keeps tailored offers. In the households' worst case it gives them what the uniform rate with a veto does, and it gives more as their own agents improve.** The worst case computed is the company predicting exactly while the households' agents know only the population: households 2.0, total 4.1. Holding the company at exact, the households' gain is 2.0, 2.9, 3.7 and 4.7 as their own agents' error goes from population-only through 0.3 and 0.1 to exact, and the total rises from 4.1 to 6.2.

5. **A household's own agent is worth nothing under the first rule and up to 2.7 under the lottery.** The first half is true by construction: under the first rule the household's agent only answers yes or no, so its predictions are never used. The second half is the series in result 4 (2.0 to 4.7). Over that series the total rises by 2.1, so most of what the households' agents earn them is new gain.

6. **A uniform rate keeps the benefit of searching over combinations of slots and insulation.** With insulation available the best possible total rises from 6.2 to 7.1, and finding it means comparing every set of slots with every set of insulated households.

    | With insulation available | Total gain | Households |
    |---|---|---|
    | Best possible | 7.1 | |
    | Company offers, exact | 7.1 | 0 |
    | Lottery, all four exact | 7.1 | 5.3 |
    | Uniform rate 2.5, veto kept | 5.6 | 2.7 |
    | Uniform rate 1.5, no veto | 6.6 | 0.0 |

    Under a uniform rate the company still runs that search, against the posted rate. The total rises from 4.0 to 5.6 with the veto and from 5.9 to 6.6 without. What a uniform rate gives up is fitting each household's payment to its sensitivity.

A second population, with sensitivities bunched low and a long upper tail, gives the same pattern: the best uniform rate with a veto keeps 65% of the best possible total (4.4 of 6.8), and the lottery's worst case for households is again about equal to it (households 2.0 against 2.1).

## The same results on Alice, Bob and Carol

Sensitivities 1, 1 and 2; total gain available 6. Averages are over the offer-maker's estimates only.

- **Company offers, error 0.3.** The morning, midday and evening slots usually run. Total 5.2. The company keeps 3.6; Alice gets 0.3, Bob 0.8 and Carol 0.5.
- **Company offers, error 0.1.** Total 5.8. The company keeps 4.7; Alice gets 0.2, Bob 0.5 and Carol 0.4.
- **Uniform rate, veto kept.** At any rate below 2 Carol refuses every slot, since she is exposed to all four, and nothing runs. At 2.5 nobody refuses, but only the midday slot still pays the company. Total 3.5: the company 1.75, Bob 1.5, Carol 0.25, and Alice nothing, because she is out at midday.
- **Uniform rate 1.5, no veto.** The three slots run and the total is 6. The company keeps 5.25, Alice gets 0.5 and Bob 1.25. Carol is paid 3 for harm of 4.
- **Lottery, all four at error 0.1.** Total 5.6. Averaged over the draw, the company gets 1.8, Alice 1.1, Bob 1.4 and Carol 1.3. In any single draw the winner takes most of the gain.

## Can a household protect itself by refusing, when the parties deal twice?

Under the first rule a household's agent answers yes or no, once. If the same parties deal again, an answer also tells the company something: a household that accepts a rate has shown that its sensitivity is at or below that rate, and the company can offer it less next time. A household's agent that expects this can refuse a rate that covers the household's harm, giving up this round's payment in order to be offered more in the next. This section computes how much that protects the households.

**Setup.** The first rule, for two rounds, with the same slots, households and sensitivities in both. In each round the company names the slots it wants to run and offers each household a rate. It cannot bind itself in round one to what it will offer in round two. Gains are the average of the two rounds, so they compare with the one-round figures. Three cases:

- **No memory.** The company's round-two offers may not depend on the round-one answers. Each round is then the one-round deal.
- **Memory, naive households.** The company uses the round-one answers. A household accepts any rate at or above its sensitivity, in both rounds.
- **Memory, strategic households.** The company uses the round-one answers, and each household answers in round one knowing that it will. The outcome computed is an equilibrium: the company's offers are its best given how the households answer, and each household's answer is its best given what the company will do with it.

Three things differ from the one-round model.

- The company offers each household one rate for all the slots it names, where before it could offer a different rate for each slot. With the company knowing only the population this lowers the one-round figures, to 1.8 for the households and 3.9 in total, against 2.0 and 4.6 in the main table. At smaller errors the two versions are close (households 1.6 in both at an error of 0.3).
- The company's profit factor and its estimates of the households are known to everyone. Only the sensitivities are private.
- As before, the company combines its estimate of a household with what it knows of the population. An error of 1.0 is therefore a weak hint, not something worse than no estimate.

Averages over the population, per round:

| Company's prediction error | Households: no memory | Households: memory, naive | Households: memory, strategic | Company: no memory | Company: memory, strategic households |
|---|---|---|---|---|---|
| population only | 1.8 | 1.5 | 2.1 | 2.1 | 2.1 |
| 1.0 | 1.8 | 1.6 | 2.1 | 2.5 | 2.3 |
| 0.3 | 1.6 | 1.4 | 2.0 to 2.1 | 3.6 | 3.3 |
| 0.1 | 1.0 | 0.9 | 1.3 to 1.5 | 4.8 | 4.5 to 4.6 |
| 0.03 | 0.4 | 0.4 | 0.5 to 0.6 | 5.7 | 5.5 to 5.6 |

Where a cell shows a range, I computed the strategic case two ways, and they bracket the answer I could not compute exactly. The end better for the households is an equilibrium in which the company is restricted in what it may offer; the end better for the company drops that restriction and is not an equilibrium. "How far to trust the strategic column", below, explains. With exact prediction every cell for the households is zero by construction: the company already knows each sensitivity, so no answer tells it anything.

7. **In this calculation, refusing does protect a household.** With memory, strategic households get 0.4 to 0.7 more per round than naive ones at every error from population-only to 0.1. They also get more than under no memory: 0.2 more when the company knows only the population (2.07 against 1.84 before rounding), and 0.3 to 0.5 more at errors of 0.3 and 0.1. The sizes on the street depend on the bracketing just described. The one-household table below does not.

8. **It does not stop the households' gain falling as the company predicts better.** With strategic answers the households' gain is 2.1 when the company knows only the population, 1.3 to 1.5 at an error of 0.1, 0.5 to 0.6 at 0.03, and nothing at exact. My reading of why: a refusal can hide only what the company would have learned from the answer, and hides nothing the company has already estimated from elsewhere. The calculation shows the fall; it does not separately measure those two sources of the company's knowledge.

9. **A naive household loses from being remembered; a strategic one gains, and the company loses.** At population-only, memory moves the households from 1.8 to 1.5 if they answer naively and to 2.1 if they answer strategically. Against strategic households the company does no better with memory than without at population-only (2.1 in both) and worse at smaller errors (3.3 against 3.6 at an error of 0.3). A rule forbidding the company to use earlier answers would therefore protect naive households and cost strategic ones. My reading, since rule-choosing is not modelled: the company would have no reason to oppose such a rule if the households' agents are strategic.

10. **In round one the company often does not try to learn.** With the company knowing only the population, in round one 46% of households, pooled over streets, are offered the top of the range, 2.5, which every household accepts and which therefore tells the company nothing. Another 8% are not asked. Of all households, 7% refuse a round-one rate that covers their harm. An example, on a street with the average profit factor: in round one the company names the morning and midday slots. It offers the household in Carol's position 2.5. It offers the household in Bob's position 2.4, and that household accepts only if its sensitivity is below 2.1; with a sensitivity between 2.1 and 2.4 it refuses a rate that covers its harm, because accepting would cost it more in round two than it gains in round one. It offers the household in Alice's position 1.2, accepted below 1.1.

**One household, one slot.** The same calculation for a household in Carol's position alone with the night slot (profit 5, exposure 2). Here the two ways of computing the strategic case give the same answer, so there are no ranges:

| Company's prediction error | Carol: no memory | Carol: memory, naive | Carol: memory, strategic |
|---|---|---|---|
| population only | 0.54 | 0.47 | 0.71 |
| 0.3 | 0.45 | 0.38 | 0.55 |
| 0.1 | 0.27 | 0.23 | 0.33 |
| 0.03 | 0.11 | 0.10 | 0.14 |

The pattern is the same. Strategic refusal adds a fifth to a third to what Carol gets under no memory at every error, and what she gets falls by four fifths between population-only and 0.03 whichever way she answers.

**On Alice, Bob and Carol** (sensitivities 1, 1 and 2). With the company's error at 0.3 and no memory, the households get 1.7 per round: Alice 0.3, Bob 0.85, Carol 0.6. With memory and strategic answers they get 2.2 to 2.5. At an error of 0.1 the figures are 1.1 and 1.3 to 1.6. These are the least reliable figures in the section, for the reason given in the last paragraph.

**A second population, and a lighter second round.** In the population with sensitivities bunched low and a long upper tail, strategic refusal is worth more. With the company knowing only the population, strategic households get 2.4 to 2.8 against 1.6 under no memory, and the company gets 2.0 to 2.1 against 2.5. The households' gain still falls as the company predicts better: 1.5 to 1.7 at an error of 0.1 and 0.6 to 0.7 at 0.03. Back in the first population, with round two given half the weight of round one (gains are then the weighted average of the two rounds), refusal is worth less: strategic households get 2.0 against 1.8 at population-only, and 1.9 against 1.6 at an error of 0.3. These figures are in the result files listed at the end, not in a table here.

**How far to trust the strategic column.** I looked only for equilibria of one shape: each household accepts in round one when its sensitivity is below some cutoff, and refuses above it. A candidate round-one offer is a set of slots and, for each household, one of thirteen choices: no offer, the top rate, or a rate that puts the cutoff at one of eleven points across the range. For each candidate I checked whether households of every sensitivity would in fact follow the cutoffs. For Carol alone, every candidate passed. On the street most fail, because a household's acceptance pays only if its neighbours also accept: when a deal is more likely in round two than in round one, a low-sensitivity household can prefer to refuse and a high-sensitivity one to accept. On the street 7% to 21% of candidates pass, fewer as the company's error falls, and on the street of Alice, Bob and Carol 2% to 5%. In the equilibrium I report, the company chooses only among candidates that pass. That restricts the company, and I expect it to flatter the households. The other end of each range lets the company choose among all candidates as if the households followed the cutoffs anyway. I expect an unrestricted equilibrium to lie in or near the range. I have not computed one.

**Published work this resembles.** Results 7 and 9 are not new in kind. I read the abstracts only of two papers. Bonatti and Cisternas, "Consumer Scores and Price Discrimination" (Review of Economic Studies, 2020), study a consumer whose purchase history is summarised in a score that firms use to set prices; a strategic consumer buys less in order to manipulate the score, and scores hidden from the consumer lower consumer surplus, which bears on the assumption here that households know the company's estimates. Devanur, Peres and Sivan, "Perfect Bayesian Equilibria in Repeated Sales" (2015), study a seller and one buyer over many rounds, where the seller tries to learn the buyer's value and the buyer to hide it. From memory, not checked: Taylor (2004) and Acquisti and Varian (2005) on pricing from purchase history, and Hart and Tirole (1988) on dealing repeatedly without commitment. What I have not seen in these is the company's outside estimate as the thing varied, which is result 8; I have not searched for it.

## What this does to the idea

- **The trade-off is real when the company always makes the offers.** Results 1 and 2 put sizes on it: exact prediction by the company is worth 1.6 in total gain and costs the households 2.0; the uniform rate with a veto gives the households 2.1 whatever the company can predict and costs 2.2 in total gain against exact prediction.
- **The trade-off is not forced.** The lottery keeps tailored offers and, in this model, gives households in their worst case what the uniform rate gives them. Among these four rules, what moves the households' share most is who makes the offers.
- **The two protections ask for different things.** The uniform rate asks nothing of the households' agents. Under the lottery the households' gain runs from 2.0 to 4.7 with their own agents' accuracy.

- **Dealing repeatedly does not rescue the households under the first rule.** Strategic refusal gives the households 0.1 to 0.5 more per round than they get under no memory, while their gain falls by about 1.5 as the company's error goes from population-only to 0.03 (results 7 and 8). My reading: under the first rule a household's gain comes from what the company does not know about it. A household's agent can defend what the company would learn from the household's own answers. It cannot defend what the company estimates from elsewhere.

Two readings of mine, not computed:

- **Rule-choosing.** When everyone predicts exactly, the first rule and the lottery give the same total (6.2), and the company gets 6.2 under one and 1.6 under the other. A choice between them then changes only the division, by 4.6, and creates no gain that could be offered to the company for giving up the right to make the offers. With poor prediction the totals differ (4.6 against 3.7 at population-only), because a household making offers also has to guess the company's profit.
- **Krier's essay** describes three of these arrangements without choosing among them: a developer's agent that finds each homeowner's price, a residents' club that makes one offer at a common price, and a posted fee for driving through a neighbourhood that no single resident can refuse.

## Limits

- **One round, except for the first rule.** The four-rule comparison is one round. Only the first rule is played twice. A uniform rate fixed beforehand for both rounds does not depend on anyone's answers, so by construction an answer has no later consequence; I did not run it. The lottery played repeatedly is not computed.
- **Two rounds, not many.** With more rounds a household has longer to benefit from hiding and the company longer to benefit from learning. I have not computed more than two.
- **The households know the company's estimates of them.** If the estimates were hidden, a household's agent would have to guess how much the company already knows. I expect that to cost the households. Not computed.
- **Simple offers.** The offer-maker names one rate per household per slot (one rate per household in the two-round section). I expect a more elaborate offer to raise the offer-maker's take at middling errors; it cannot change the exact-prediction row. Not computed.
- **The lottery is an average.** One party takes most of each deal. Over many small deals that evens out; in one large deal it does not.
- **The company's private range is narrower than the households'.** I expect a wider range to lower the households' gain when they make the offers. Not computed.
- **Insulation is paid for up front.** An offer-maker who could make it conditional on acceptance would do a little better at high error. Not computed.
- **Four rules, one model, built by me.** The results show the logic is consistent and give sizes inside the model. They are not evidence about what agents will do.

## Checks

- **Independent re-implementation.** A separate agent wrote its own version from a written specification (`_tmp/coase_rule_tradeoff/spec.md`) without seeing the first program or its results. It finds each offer-maker's best offer by solving the optimality conditions directly, where the first program searches a grid. Its code and output are in `_tmp/coase_rule_tradeoff/check/`. Every figure it was asked for agrees with the first program within simulation error: for example best possible total 6.1 against 6.2, company offers at error 0.3 giving 5.3 / 1.55 against 5.4 / 1.56 (total / households), uniform rate 2.5 with a veto 4.0 / 2.1 against 4.0 / 2.1, and the 47% and 21% underpaid shares exactly.
- **What it covered.** Best possible totals; company offers at population-only, 0.3, 0.1 and exact; a household making the offers at 0.3 and exact; the lottery with all four at 0.3; both uniform-rate rules at four rates; all with insulation off and on; and the Alice, Bob and Carol figures for company offers and uniform rates.
- **What it did not cover.** The lottery rows with the company exact and the households at other errors (these are assembled from the same parts it did check), the errors 1.0 and 0.03, and the second population.
- **Two things it found.** With insulation paid up front, an offer-maker ends below no-deal in 1% to 4% of streets, because it insulates and is then refused. And at a uniform rate of exactly 2.0 with insulation available, the company is often indifferent about insulating, and the total depends on how that tie is broken (6.3 or 6.0 without a veto). No figure quoted above uses that case.
- **Bounds.** In neither program does any street's total exceed the best possible, and no household holding a veto ends below no-deal.
- **Cold read.** A reader given only an earlier draft of this note listed what it could not follow and which statements were not in a table; the note was rewritten from that list. The rewritten version has not been read cold.
- **Dealing twice: a textbook case.** With one household, one slot and the company knowing only the population, the two-round equilibrium can be worked out by hand. For a household with exposure 1 and sensitivity drawn evenly from 0.5 to 2.5, and a slot worth 3 to the company, the company's best round-one offer is a rate of 2.25, accepted below a sensitivity of 1.5, and its profit over the two rounds is 1.406. The program gives the same rate and cutoff and a profit of 1.407.
- **Dealing twice: independent re-implementation.** A separate agent wrote its own version from a written specification (`_tmp/coase_rule_tradeoff/check_repeat/spec.md`) without seeing the program, integrating exactly where the program samples. It covered Carol alone at three errors and the full street with the company knowing only the population. Both were run at the average profit factor only, so its figures are not the population averages in the tables above and are compared here with the program's figures for the same case. Its first comparison showed that two of my search grids were too coarse and overstated what the households get by up to 0.08. I refined both and reran everything; the figures above are from the rerun. After that the two agree: for Carol alone, to 0.01 on every figure (for example strategic Carol 0.65, 0.57 and 0.35 at the three errors in both); on the street, to 0.01 for no memory and for naive households, and for strategic households 1.64 against its 1.62, with the company at 1.78 in both.
- **Dealing twice: one equilibrium checked independently.** The same agent was given one of the program's street equilibria, from before the grids were refined, and asked to test with its own code whether it is one. It is, to within the grid: each round-two offer is within 0.002 of the company's best, each round-one rate leaves a household exactly at its cutoff indifferent between accepting and refusing, as it should, and no household of any sensitivity gains by answering differently in round one.
- **Dealing twice: cold read.** A reader given only this note listed what it could not follow or check in the new section, and the section was rewritten from that list. The rewrite has not been read cold.
- **Dealing twice: not covered by the independent check.** Streets where the company has an estimate of each household (errors 1.0 to 0.03), profit factors other than the average, the second population, and the lighter second round. These use the same program on different inputs.

## Where each number comes from

All from `_tmp/coase_rule_tradeoff/results_uniform.json`, produced by `rules.py` and printed by `tables.py` in the same directory. Keys are under `population/schedule_only` unless stated.

| Statement | Key |
|---|---|
| Best possible total 6.2; 7.1 with insulation | `first_best`; same under `population/with_insulation` |
| Company offers, by error | `A sigma=inf`, `0.3`, `0.1`, `0.0` |
| Uniform rate, veto kept | `B1 r=…` |
| Uniform rate, no veto; share underpaid and by how much | `B2 r=…`; `p_household_worse_off`, `mean_loss_if_worse_off` |
| Lottery rows | `C company=… households=…` |
| Insulation table | the same keys under `population/with_insulation` |
| Alice, Bob and Carol | the same keys under `instance/schedule_only` |
| Second population | `results_lognormal.json` |

The section on dealing twice comes from `repeat.py` in the same directory, printed by `repeat_tables.py`. One file per case: `repeat_population_uniform_sigma<error>_delta1.0.json` for the main table (in file names "uniform" is the first population, not a uniform rate) (`forget` is no memory, `myopic` is naive households, `strategic` is strategic households, `unchecked` is the version without the restriction: the lower end of each households' range and the upper end of each company's range), `repeat_solo_…` for Carol alone, `repeat_instance_…` for Alice, Bob and Carol, `repeat_population_lognormal_…` for the second population, and `…_delta0.5.json` for the lighter second round. `share_all` is the share of households offered a rate everyone accepts, and `hiding_rate` the share refusing a rate that covers their harm.
