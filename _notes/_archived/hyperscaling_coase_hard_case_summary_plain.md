# What more compute does for bargaining agents, in plain words

## The two models

The first model is a river. A factory can pollute it for a profit of 20 or of 10. Three residents downstream are harmed by 2, 3 and 9 if it does. Pollution needs the consent of all three, and money can pass between any parties. At a profit of 20, pollution creates 6 more than it destroys. That 6 is the surplus: the total gain from a deal over no deal, which the four parties divide. At a profit of 10 the clean river is efficient. If bargaining fails the river stays clean, so every gain is measured from zero.

The second model is a noise schedule. A delivery fleet chooses which of four time slots to run: morning, midday, evening and night, with profits 4, 5.5, 4 and 5. Three residents each have a known exposure to each slot and a private sensitivity, 1, 1 and 2. A resident's harm is her sensitivity times her exposure, summed over the slots run. The efficient schedule runs morning, midday and evening, so the surplus is again 6. Each of these switches removes one feature that made the river easy:

- non-additive harm: resident 3's harm rises by 1.5 whenever morning and evening both run, which makes morning plus midday efficient and cuts the surplus to 5;
- repeated play, with the future discounted by 0.5, 0.8 or 0.95 per period;
- unequal wealth with concave utility: utility is the logarithm of wealth, from 100 for the fleet, 10 for residents 1 and 2, and 2 for resident 3;
- no enforcer: a pact among residents must enforce itself, or a platform enforces it and fixes the menu of clauses;
- finite estimation budgets: the estimation budget is the compute a side spends estimating what it does not know, and the three tested leave an error of 1, 0.3 or 0.1, called a coarse, a middling and a fine estimation budget;
- insulation, halving one resident's exposure at a cost of 2;
- consent of two residents rather than three;
- a reroute option, letting the fleet serve any slot another way at a cost of 3.

## What counts as better

An outcome is better when the Nash product, the product of every party's gain over no deal, is higher, with the worst-off party's gain, called the floor, as a check. The product is 0 when any party gains nothing and undefined when any party loses. The best outcome on both models is the equal split: the surplus of 6 divided as 1.5 to each party, a product of 5.06. More compute buys four separate things, called dials: estimation, speed in publishing a binding position, cheap and reliable commitment, and adaptation to the other side's play.

## The question and the answer

The agenda under test is Krier's: cheap, capable negotiating agents let private bargaining replace regulation and reach good outcomes by default. Petel and Snow have published critiques. The question is under which conditions more computation for bargaining agents produces better outcomes, and for whom.

More compute raises the Nash product for everyone only where rules from outside the bargain already make the end point symmetric: a veto for every resident, a proposer drawn at random by party, payments tailored to each resident, a contract form and preference model that carry every harm, verified harms, no outside option for one side, linear money, and one agent per person. Where the right to propose is fixed, compute helps the residents up to a middling estimation budget and its holder beyond. Wherever another condition is missing, compute helps whoever holds a dial, the outside option or the contract form. The cost falls on resident 3, the most harmed, the poorest and the one whose harm is not a simple sum.

## A veto for everyone and no fixed proposer

With every resident holding a veto and the right to propose drawn at random among the four parties, capable agents reach the equal split. Unanimity stops the fleet playing one resident against the others. A random proposer averages out the advantage of proposing. The equal split is the symmetric bargaining solution (Nash 1950); it is the long-run outcome of adaptive play with equal memories (Young 1993); and each party expects it when commitments are attempted in random order (Hang and Wen 2026).

On the noise schedule the product rises from 0.54 to 3.41 to 4.71 as estimation budgets grow, and nobody loses at any step. On either model, an asymmetry breaks the result in favour of its holder:

- proposer drawn by side, fleet against residents: fleet 3, each resident 1;
- factory remembering ten times the past play each resident does: factory 4.62, each resident 0.46;
- factory always first to commit: factory 5.4, residents 0.54, 0.054 and 0.006.

The best reply is Krier's: agent vouchers and compute credits equalise capability. It concedes that vouchers equalise estimation alone, not speed, memory or the entitlement, and that a random order is a rule someone imposes.

## A fixed offer seat

The offer seat is the right to make a final offer that the other side can only accept or refuse. Its holder takes the whole surplus as estimation becomes exact. A proposer unsure of the responders' harms must leave a margin to be accepted, and that margin is their gain. At a coarse estimation budget many offers are still refused, so most of the loss is destroyed rather than transferred. At a middling estimation budget deals close and the margin is still large. At a fine estimation budget it vanishes.

Under the fleet's offer the product goes 0.002, 0.33, 0.22 across the three estimation budgets. The residents' expected take, counting failed deals as zero, goes 0.87, 1.56, 1.15. In the limit the fleet takes all 6; with the residents holding the seat as one bloc, each takes 2 and the fleet nothing. The night slot never runs under the fleet's offer, because a proposer who must be accepted avoids a slot that invites refusal.

The residents gain up to a middling estimation budget and the seat holder beyond it. The best reply is that the responders' agents estimate too. It concedes that in a one-round offer the responder's estimation budget buys nothing, and that only a seat rotated by rule restores symmetry.

## Consent of two residents out of three

When two consents suffice, no pact among residents survives a fleet that plays the repeated game, at any discount, and resident 3 is left out. A pact is an agreement among residents on how they bargain and divide. The fleet needs two signatures, so it pays the cheapest pair a little more than the pact does and runs its schedule over the third's objection. A pair with the fleet can claim more than the whole surplus, because the excluded resident's harm drops out of their accounts. All three pairs' claims can be met only if the fleet alone holds 17.5, more than the surplus of 6, so no division meets them. Repetition does not help, since the defecting pair is paid every period too.

With consents competing to a zero price, the fleet runs all four slots and takes 18.5, leaving the residents at −2, −3 and −8. The fleet's compute finds the cheap pair faster: a pact's expected life falls from 0.66 to 0.03 periods as the fleet's error falls. At three consents every pact holds on its own.

The best reply is to hire an enforcer. It concedes that whoever enforces must itself be bound (Cooter 1982; Acemoglu 2003), and a monopoly enforcing platform takes 17 a period. Someone outside the bargain must require three consents or enforce the pact.

## A harm that is not a simple sum

An agent that models each resident by one sensitivity summed over slots drives resident 3 to zero gain once her harm depends on the combination, however much it computes. No data inside that model reveals the extra harm from morning plus evening. The fleet settles on morning, midday and evening, which realises a surplus of 4.5 rather than 5, and underpays resident 3 by 1.5. Under its offer the deal rate falls from 54% to 0% as its estimation budget grows. In the limit nobody captures the loss: the fleet's own gain falls to 0 as well.

An agent that carries the full table, one entry per possible schedule, reaches the best product here, 2.44. It needs 17 numbers rather than 3, about 5.7 times the estimation budget. With two or more parties whose preferences are unrestricted, reaching the efficient schedule needs a number of bits that doubles with each added slot (Segal 2007; Nisan and Segal 2006): 6 at four slots, about 7 million for an hourly day. Real noise preferences, expressed as indices and event counts, fall between the extremes.

Resident 3 loses when the other side estimates her harm and gains when she reports or proposes. The best reply is to carry the full table. It concedes that someone chooses the model, and that the fix is a rule giving the informed side the report or the offer.

## Who writes the clauses

Whoever fixes the contract's clause language, meaning which combinations of slots can be agreed separately, fixes the surplus. Without and with resident 3's combination harm, the surplus is:

- every slot separately: 6 and 5;
- morning-and-midday, evening-and-night: 5.5 and 5;
- morning-to-evening, night: 6 and 4.5;
- one all-or-nothing clause: 5.5 and 4.

No two-clause menu loses nothing in both cases, and which one does depends on resident 3's private harm.

Fixing the payment form as well makes the author a party to the division. Krier's bargaining club pays every member one common price. To buy resident 3's consent that price must cover her harm of 4, so at least 12 in all against a profit of 13.5; at that bare price resident 3 gains nothing and the product is 0. At the common price that does best under the criterion, 4.28 a head, the fleet gains 0.67 and the residents 3.28, 1.78 and 0.28, a product of 1.08 against 5.06 for tailored payments. A coarse menu with one price closes no deal. The low-harm residents gain and resident 3 loses.

The best reply is that the club clears here, where on the river it needed 27 against 20. It concedes that Krier leaves the protocols to be designed elsewhere, and Petel expects platforms to set them by default, so the author is chosen before the bargain.

## Private sensitivities

Now each sensitivity is 1 or 2 with equal chance, known only to its holder, and called her type. A pact is incentive compatible when nobody gains by misreporting. Efficient incentive-compatible pacts exist, but none gives the equal split at any estimation budget. A low type must be paid what claiming high would bring her, her information rent, and a high type just enough to agree. Asking for more proves nothing, since a low type would ask the same (Myerson 1983). A pact must also be durable: no type would vote to return to the rule in force, the entitlement (Holmström and Myerson 1983).

The fleet's best pact gives the fleet 3.19, residents 1 and 2 rents of 1.0 and 2.25, and resident 3 exactly 0. The best product any such pact reaches is 3.16 to 3.82, against 5.06. Resident 3 stays at 0 at every estimation budget, and a symmetric durable pact's product falls from 3.23 to 1.99 as the fleet's estimates improve.

The best reply is a veil: a standing instruction fixed before anyone knows her type. All accept it in advance, raising the expected product from 3.65 to 3.91. It concedes that the veil takes from whoever turns out high: resident 3 at sensitivity 2 ends at −1.05. It works only where types are drawn afresh after the instruction, never for a lasting trait.

## Many residents

At scale under unanimity, voluntary efficient deals vanish only where no slot's margin, its profit per resident less the largest harm per resident it could cause, can carry the others. The chance that a voluntary, self-financing, truthful mechanism reaches the efficient decision falls to zero as numbers grow, when even the lowest possible valuations leave a shortfall per head (Mailath and Postlewaite 1990). With sensitivities uncertain within a factor of two, the chance of the efficient schedule falls from 1.0 to 0.54 between 3 and 300 residents, yet 5.25 of the 6 is still kept. Estimation restores efficiency at every scale, but moves the rents from the residents to the fleet.

The fleet's reroute option removes the margins: the share of the efficient surplus kept falls from 1.0 to 0.0008 across the same range. The best reply is that real margins are often wide. It concedes that an outside option makes them thin, and that the compute which repairs efficiency pays the fleet.

## An outside option for the fleet

An outside option shrinks the surplus from 6 to 1.5 and favours its holder at any estimation budget. With the reroute, the fleet's payoff from no deal rises from 0 to 6.5. Symmetric bargaining gives each party 0.375, so the product falls from 5.06 to 0.02, while the fleet ends at 6.875 in total.

The residents' estimation becomes worthless, because the fleet's willingness to pay is now the public reroute cost: a bloc offer gives each resident 0.5 at every estimation budget. The best reply is Krier's option fee. It concedes that the fee prices the threat without removing it, and that a threat point is not one of the four dials.

## Unequal wealth

Whether harm is a loss of money or of utility decides the result. Read as money, the efficient schedule is the same under every entitlement. But in utility units the criterion pays the poorest resident least: its best division gives resident 3 1.296, against 1.535 for residents 1 and 2 and 1.634 for the fleet. This direction is known (Kihlstrom, Roth and Schmeidler 1981). In money units the criterion gives the equal split.

Read as utility loss, the schedule follows the entitlement. If the residents hold the right only midday runs, since resident 3 alone would need 12.78 to accept the efficient schedule. If the fleet holds it, all four slots run, because the residents together can offer only 3.17 for relief. Krier makes this point himself, with a poor farmer who sells cheaply for cash now; Petel repeats it. Under every arrangement resident 3 takes the least money.

Dan, you need to choose the units: money, money-equivalent gains at the no-deal point, or utility from a common start. The money reading also leaves resident 3 with negative wealth when the fleet holds the right.

Money units and money-equivalent gains can differ. Money units take each party's money gain: payment received less harm. A party's money-equivalent gain is the sum of money that, received at her no-deal wealth, would change her utility as much as the outcome she actually gets. The two coincide when every payoff is money and certain. They come apart when harm is a disutility rather than a cash loss, or when the outcome is risky. Take harm as a disutility, calibrated so that a small harm is worth its money value at the no-deal wealth. At the efficient schedule, pay the residents 2.49, 4.00 and 5.43. Their money gains are 1.49, 1.50 and 1.43. Their money-equivalent gains are 1.36, 1.20 and 0.48. A money gain that comes with a harm is worth, in money-equivalent terms, the gain times wealth divided by wealth plus harm. So a harm counts for more the poorer the party is relative to it. Resident 3, with wealth 2 and harm 4, keeps only a third of her money gain. The fleet bears no harm, so its money-equivalent gain equals its money gain, 1.58. Under a finite estimation budget the outcome is a lottery over deals and refusals. For any party with concave utility, the money-equivalent of a risky gain is below its expected money value, and further below for the poorer party. The choice of units therefore decides whether the criterion sees resident 3's poverty at all.

## Seat and dial, not entitlement

Compute moves the division toward whoever holds the offer seat or a dial, not toward the holder of the entitlement. At three consents the residents hold the veto, yet the fleet's offer drives them to about 0.03 each. At two consents the proposer assigns the entitlement by excluding someone, and resident 3 is excluded under every proposer but herself. Residents with ten times the fleet's estimation budget but no seat gain nothing from it. The entitlement fixes the no-deal point and, under the utility reading of wealth, the schedule.

A household that splits into several agents takes more. Under unanimity with agents counted, resident 2 running three agents takes 3.0 of the 6. The product per person falls from 5.06 to 0.45 at ten agents. If consent is set at three of five agents, resident 2 becomes the only resident whose consent counts, gaining 7.75 while resident 3 falls to −8. The criterion counts parties too, so it needs the rule Petel calls one human, one principal, one agent. The best reply is that such a rule can be adopted. It concedes that the rule comes from outside the bargain.

## Bundling as commitment

Snow's bike-lane case points to bundling consents into one agreement. A bundle priced over all sixteen schedules captures the combination harm, where slot-by-slot agreement finds the right schedule only half the time. A bundle also commits: reopening one slot after agreement costs a resident her stake in the rest of the bundle times the cost of delay. Dropping the evening costs 0.875 when the future is discounted at 0.5 and 0.31 at 0.95, against 0.25 slot by slot. As renegotiation becomes instant the cost goes to 0.

The bundle binds each party in proportion to its stake. Under the fleet's bundled offer the residents hold nothing, so it binds only the fleet. The fleet takes more slot by slot at every estimation budget, so a bundle must be imposed by the form. The best reply is that bundling finds the combination harm. It concedes that the commitment lasts only while renegotiation is slow, and that it fixes whatever terms were agreed.

## Two conditions in the agenda's favour

The first is carrying a full table of preferences: it reaches the right schedule under any preferences, where a one-number agent fails at every estimation budget. The second is searching schedule and insulation together. Insulating resident 3 makes the night slot worth running, and all four slots plus insulation raise the surplus from 6 to 7.5. Decided alone, insulation is never bought, since resident 3 saves exactly its cost of 2. Only a search over all 128 combinations finds the extra 1.5, which an agent does easily and a person does not. Under the equal split every party gains 0.375 more, and the product reaches 12.36. Under the fleet's offer at a middling estimation budget the residents take 2.10, their best wherever the fleet holds the seat.

## The cases that work under symmetry

Four settings reach the equal split with no rule supplied. Each needs something that giving everyone an agent does not supply.

- Haggling under recurrent adaptive play. When each side bases its demands on a sample of past play and the samples are equal in size, the equal split is the long-run outcome (Young 1993). It needs equal memory, which a repeat player facing one-off residents does not have.
- Short-lived commitments attempted one at a time in a random order. Each party then expects a quarter of the surplus (Hang and Wen 2026). It needs a random order, which an institution imposes when speed is unequal, as it is when one principal faces three who must first agree.
- Patient repeated play. The equal split is sustainable each year once the discount factor is at least 0.75. It needs patience, and a deterrent to the fleet reneging on the agreed split.
- On the noise schedule, a proposer drawn at random by party at finite estimation budgets. The product rises from 0.54 to 3.41 to 4.71 toward 5.06, and nobody loses at any step. It needs a seat drawn by party rather than by side; drawn by side, the fleet takes 3 and each resident 1.

Dan, two decisions are yours before anything is drafted: whether the four cases in this section count for the essay or for Krier, and the units under unequal wealth.

## The sampling round

The sampling round ran twelve independent searches for conditions the agenda needs and does not supply, each from a starting point dealt to it. An adversarial reader rebuilt the strongest findings from their own descriptions.

The round also measured outcomes against the ordinance, the regulation in force, which closes the night slot and lets the other three run unpaid, leaving residents 1, 2 and 3 at −1, −2.5 and −4.

Consent of two residents out of three takes resident 3 below the ordinance with no compute. The fleet offers each resident a token for signing if all three sign, and her full harm only if hers is the deciding signature. Whatever the others do, a resident does no worse by signing, so all three sign, nobody is paid, all four slots run, and the residents end at −2, −3 and −8. The clause needs no estimate of anyone's harm. Going door to door, the fleet buys the deciding signature in full and the other near its fallback, never approaching resident 3; its speed decides only which of residents 1 and 2 is squeezed. Under every reading checked, resident 3 ends at −8, twice her harm under the ordinance. Only a club whose members are bound all-or-none before any offer, binding with probability above 0.92, reaches her, restoring 1.5 each. A club with a common minimum but no all-or-none terms leaves her at −8, and a club at one price lifts her only to −5. Nor is a club a default: merging buyers can help or hurt them (Chipty and Snyder 1999), and here a club helps the residents when two consents suffice and costs them 1.5 when all three are needed.

The fleet's reach beyond one neighbourhood takes the residents' share without taking anyone below the ordinance. With several neighbourhoods to choose from, the fleet offers all but one no more than their harms, so a neighbourhood's commitment protects its share only while every other's holds too. If each resident's commitment binds with probability q, a neighbourhood's residents take 4.5(1−(1−q)^3)^(K−1) among K neighbourhoods, falling geometrically with K, and nothing unless q is at least 0.37. When the fleet meets neighbourhoods in turn with its record public, the chain-store argument of Kreps and Wilson (1982) applies: a fleet that never raises an offer after a refusal turns any positive belief that its final offer binds into a reputation. At a belief of one in a hundred, a neighbourhood's residents take 1.49 when the fleet deals with one neighbourhood and 0.17 with a thousand. Both assume fixed take-it-or-leave-it offers and no pooling across neighbourhoods; repairs are a club spanning every neighbourhood, formed before the first offer, or a hidden record. Scale also removes Krier's club: at one price it must pay every household the largest harm among them, so against a cheaper detour it closes nothing from thirty households up, leaving house-by-house pricing, which the fleet's estimation budget takes.

The fleet's private margin takes above the fair share only in a narrow window. With the proposer drawn by party, one-shot offers and unanimity, a resident who proposes must shade her demand by her error about the fleet's profit, and the fleet keeps that margin. The fleet takes more than 1.5 only while its error about the residents' sensitivities is below about 0.2 against their 0.316 about its profit, or at a hundred-to-one estimation ratio, where it takes 1.81; at equal compute it earns what each resident earns. Opening the books caps the fleet at 1.5 by construction: residents who know its margin leave it nothing when they propose, and it takes at most the whole 6 in the one draw in four when it does. Disclosure by one side only reverses the asymmetry, giving each resident 1.53 and the fleet 0.71. The asymmetry lies in whose number is private, not in how often each side proposes.

When a shock to one slot's profit reopens the bargain, one contract covering every slot is reopened whole, and each reopening favours the side quicker to propose, so the fair deal erodes faster when the residents' agents are slower. At a ten-to-one speed ratio the residents take 0.69 a period under one contract against 1.01 under four. The fair deal's half-life is 3.5 periods under one contract and four times that for each slot under four; long-run shares are equal, so the loss falls over the contract's lifetime. No reader rebuilt this single search.

A fleet fielding many agents is a platform rule, not a compute result. If the platform divides by registered agent and prices extra agents cheaply, the fleet's 21 agents take 4.65 of the 6 at a ten-to-one compute ratio; the reader found no source for that rule in the agenda, and divided per person nothing moves. What survives is that if agents are counted the side with cheaper agents wins, and that one human, one principal, one agent has no default reading for a firm.

Every finding after the first takes the fair deal's share and leaves nobody below the ordinance, so neither the floor nor a comparison with regulation detects it, and the first needs no compute. So the agenda fails against regulation only where the consent rule already fails, and against its own promise wherever compute is unequal; the third list, of conditions under which more compute for one side takes value from the other, is short and shares-only.

## Whether there is an essay

The test was whether capable agents for everyone make outcomes converge, unaided, to something just under the criterion. It fails on both models, so there is an essay. Its spine is two lists. The first is the symmetries the agenda presupposes without supplying: equal memory, equal reliability, nobody always first, a proposer drawn by party, one agent per person. The second is the settings where even symmetry fails, each with its repair: unanimity set from outside, tailored payments, a full preference model, verified harms, no one-sided outside option. Each repair carries a distributional choice made before the bargain, such as who joins the club, who writes the form, who counts as one principal and which damages a court uses. Compute then pushes the outcome further in the direction that choice set. The sampling round looked for a third list, the conditions under which more compute for one side takes value from the other, and found it short and shares-only: none of its items takes anyone below the ordinance, and the one failure that does, consent below unanimity, needs no compute. So against regulation the agenda fails only where the consent rule already fails, and against its own promise wherever compute is unequal.

## What the closed models leave out

Both models are closed: one fleet, one neighbourhood, one bargain. Deployed agents take part in many bargains at once. Each case below adds one feature of that world. The first two were computed in the sampling round; the rest were worked out once by hand, unchecked.

One fleet facing many neighbourhoods in turn, with its record public, is the chain-store setting. The fleet approaches the payoff of a commitment that never breaks: all 6 in every neighbourhood, residents at 0. Equal memory and nobody always first become unavailable: the party in many bargains has the history.

Two identical neighbourhoods competing for the same deliveries undercut each other to their joint harm. Residents gain 0 with every veto intact. Unanimity protects nothing once the fleet can shop between counterparties.

Computed, both cases hold as limits and neither takes anyone below the ordinance. With its record public, the fleet's take in each neighbourhood rises from 1.54 to 5.42 as the neighbourhoods go from one to a thousand, at a belief of one in a hundred that its final offer binds, and hiding the record restores the equal split. Between competing neighbourhoods the residents' take falls geometrically with their number and is zero unless each resident's commitment binds with probability at least 0.37.

A fleet that also serves the residents can withhold service worth 1, 1 and 3 to them. The equal split of the bundled surplus of 11 leaves resident 3 at −0.25 in money against a clean schedule with service, while the product rises from 5.06 to 57. The no-deal point the criterion measures from is chosen by the party with more than one thing to trade.

A reputation system that costs a refusing resident 1 in other bargains lets the fleet offer each resident her harm less 1, so every resident ends at −1. The scoring is asymmetric: many one-shot residents score the fleet, while a few platforms that see every bargain score each resident, to the fleet's benefit.

One vendor representing all three residents, paid per closed deal, accepts any offer that leaves its clients at no deal. The fleet takes 6 and each resident 0: the veto is gone with no change to the consent rule. A vendor paid by client wealth gives up resident 3's claim first, which favours the richer residents.

The estimation budget ratio is earned, not chosen. A party in ten bargains of one kind has ten times the samples, and one in several bargains at once splits its estimation budget among them. A ten-to-one ratio for the fleet is what ten neighbourhoods give it.

If the reroute cost of 3 is partly harm to a neighbourhood with no say, then at a fleet cost of 1.5 per slot the four parties reroute everything. The apparent surplus is 12.5, the true surplus 6.5, so harm of 6 is exported. The product among the parties rises with every unit exported, which benefits the fleet most, since rerouting is its option.

The platform that writes the form and sets the consent rule has its own payoff and carries its choice to the next neighbourhood. Paid per closed deal, it prefers the menu and rule that close the most deals, not those that do best under the criterion, which suits its repeat customer, the fleet.

A resident may move away at a cost of 3, paid from her wealth. Residents 1 and 2 gain a floor of −3; resident 3, with wealth 2, does not.

The closed models find the symmetric end point available only under rules. The open cases make the asymmetries arise by arithmetic rather than by assumption, and in every one the party in many bargains, here the fleet, is favoured.
