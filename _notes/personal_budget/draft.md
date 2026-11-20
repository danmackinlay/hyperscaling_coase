---
title: Bargaining budgets when every principal has an AI agent
date: '2026-11-19'
categories: [economics, cooperation, AI]
description: A test of Seb Krier's case for Coasean bargaining through personal AI agents, using contest models in which each principal has a budget for bargaining compute.
---

Seb Krier's essay [Coasean bargaining at scale](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale) proposes that personal AI agents will make private bargaining over externalities cheap enough to replace much of what regulation now does.
Every household, firm and state would be represented by a loyal agent that finds the parties a decision affects, states terms and closes a deal, at a cost counted in compute rather than in lawyers' hours.
This article tests that proposal with a small family of game-theoretic models.
We grant Krier his institutions and write them down as explicit assumptions.
We add one feature his essay does not model: each principal has a budget for bargaining compute that rises with its wealth, and each faces counterparties whose agents spend up to their own limits to win a larger share.
We then ask what each principal ends up with in equilibrium.
We judge the resulting world by three things: whether anyone ends up worse off than without bargaining, how the surplus is divided, and how much of it is spent on the bargaining itself.

The models were built to test a suspicion that this world is worse than Krier expects.
They confirm it only in part.
Under some assumptions Krier is right, and the verdict says which assumptions those are and what evidence would tell us whether they hold.

## What we found

Cheap compute makes it cheap to take part in a bargain.
Finding the counterparty, reading the terms and stating a price all cost compute in fixed quantities, so their dollar cost falls with the price of compute.
This is the cost Krier has in mind, and on it he is right in every model here.

Cheap compute need not make it cheap to divide a surplus once one exists.
When two loyal agents contest the split of a sum at issue between their principals, each buys compute until the last dollar stops paying for itself.
In the contest model that economists use for lobbying and litigation, the total they spend is a fixed fraction of the sum at issue, whatever compute costs.
A fall in the price of compute buys more computation for the same dollars.

Whether that spending ever stops depends on the matter being bargained over.
In some matters the effect of extra compute fades to nothing as both sides use more of it, in the simplest case because there is a level of compute beyond which more changes nothing; we call these *saturating*.
Once compute is cheap enough both sides reach that level, the dollars spent fall with the price of compute, and the split no longer depends on who has more compute.
In other matters the ratio of the two sides' compute goes on moving the split however much both use; we call these *non-saturating*, and in them spending does not fall.
Extra compute can have diminishing returns and still be non-saturating.
In a model in which agents search for the best argument or clause, a matter saturates only if a best answer exists and whoever decides the matter treats small differences between the two sides' answers as ties.
We carry three cases through the article.
In the *saturating world* every matter saturates, and Krier is right about cost and also about how the surplus is divided.
In the *non-saturating world* no matter saturates; this is our main case, and the findings below are for it unless we say otherwise.
In the *mixed world* a fraction of a principal's stakes, which can differ from one principal to the next, is in non-saturating matters, and those findings hold for that fraction.

What a principal gets is set by its budget relative to everything it has at issue in non-saturating matters.
Our central case is a contest in which a side's chance of prevailing is proportional to the compute it spends, between a household whose budget runs out and firms whose budgets do not.
In it, a nurse with \$400 a year for agent compute and \$25,000 a year of surplus at issue, mostly with such firms, gets about an eighth of that surplus, about \$3,200, if none of her matters saturates.
If a fifth of her stakes never saturates and the rest saturates, she gets about \$11,400, because she takes half of everything that saturates and concentrates her budget on the rest.
That figure supposes that which of her matters saturate is fixed by the matters themselves or by a protocol, and is not chosen by the firms she faces.
She is better off than with no bargaining at all, as Krier argues.
The Coasean programme multiplies the bargains she is party to without raising her budget, so her share of each non-saturating one falls.

Even shares and low waste trade off against each other.
In the central case the fraction of the sum at issue that is spent on compute equals the weaker side's share of it.
Krier proposes a publicly funded compute voucher for people who cannot afford a good agent.
In the central case a voucher large enough to give a household an even split with the firms it faces has to bring its budget up to a quarter of everything the household has at issue, a sum that does not shrink as compute gets cheaper, and it raises spending on compute as fast as it raises the household's share.

Where Krier's assumptions hold in full, the models support him on the main point.
If property is perfectly secure and bargains are over new surplus, nobody ends up worse off than without bargaining.
If in addition winnings are paid in cash and reinvested in full, and nothing else drains the budget, a household's shortage of budget cures itself within a few years.

The assumption of secure property carries a great deal.
If cheap search also makes it cheap to find ambiguities in existing entitlements, and nothing but a fee stands in the way of challenging them, then an entitlement is safe only up to a multiple of that fee.
Cash-poor holders then lose holdings to challengers, and can end up worse off than with no bargaining.

Which world a principal is in may itself be chosen.
If the stronger side can make a matter non-saturating at no cost, for example by adding clauses, a firm gains by doing so against a household whose budget is small relative to its non-saturating stakes, and gains by letting the matter saturate against a well-funded one.
On that assumption well-funded households end up in the saturating world and poorly funded ones in the non-saturating world.
A household with the nurse's budget is then in the non-saturating world, and the \$11,400 above is not available to her.

Krier's picture comes closer to holding the more weakly extra compute moves the split of a bargain, since spending and the inequality of shares both shrink with it.
It holds on cost if the returns to compute in bargaining run out in the matters that carry most of each principal's stakes.
Neither how strongly extra compute moves the split as both sides use more of it, nor the fraction of stakes that is in non-saturating matters, has been measured, and we describe at the end the experiment that would measure them.

## Krier's proposal

Krier's thesis is that transaction costs are the reason societies fall back on blunt regulation.
Finding the affected parties, negotiating with them and enforcing what was agreed has been too expensive, so a planner decides instead.
Personal agents could cut those costs far enough that Coase-style private bargaining over externalities becomes feasible at scale, which he calls "hyper-granular contracting".
His examples include a delivery truck whose agent pays a clean-air fee to a street where a child has asthma, a developer whose agent must find the price at which every homeowner on the block agrees, and taxis paying a fee to cut through a low-traffic neighbourhood.

He anticipates the obvious objections.
He concedes that the costs shift to compute, but argues the reduction is large: a legal bill of \$10,000 today might cost a few cents in compute.
He adds that a billionaire's phone is no better than anyone else's, which suggests that agents too will be much the same for rich and poor.
He treats inequality as a short-run concern, to be handled by publicly funded baseline agents "similar to public defenders", by agent vouchers, or by a universal allocation of compute, and he expects the cost of this to tend to zero as agents become commodities.
He accepts that the default allocation of rights is a constitutional choice rather than a technicality, proposes to start from existing jurisprudence, and says agents make the baseline "explicit, contestable, and cheap to renegotiate".
He notes that a poor farmer may sell his pollution rights cheaply to a rich factory because he needs cash now.
He worries that constant renegotiation of property rights would destroy investment incentives, and expects agents to settle on stable arrangements because "constant renegotiation is expensive even for AGI".
For holdouts in many-party bargains he proposes a voluntary bargaining club, in which each homeowner privately enters a minimum price, the software makes one take-it-or-leave-it offer, and all are paid a common clearing price; he argues that truthful reporting is then each member's best strategy.
He adds a fee on people who name absurd prices, charged as a percentage of the price they claim (a Harberger tax), and coalitions formed in an instant, such as 10,000 residents forming a "digital union" against a polluter.
The state, on this account, stops planning and becomes the guarantor of the framework: it keeps property rights, contract enforcement, courts, criminal law and bans on catastrophic risks.
An agent serves its user, within the terms set by the company that provides it, and both within the law.

He also separates two modes of agent negotiation.
In the economic mode willingness to pay decides; in the democratic mode each person has an equal vote whatever their wealth.
Everything below concerns the economic mode, which is where his externality examples sit.

Three things are absent from the essay.
It does not treat bargaining between agents with unequal compute as a contest in which spending moves the outcome.
It wants baseline entitlements to be contestable, but does not discuss what it costs a holder to defend one.
It does not ask what happens to total spending on negotiation when the unit price of negotiating falls.
There is also a tension inside the stability argument: the force he relies on to stop endless renegotiation is the cost he expects to vanish.

### The constitution we hold fixed

We take Krier's institutions as given and state them as six assumptions.

- *Entitlements.* Every entitlement has an owner, as inherited from existing law.
- *Voluntary exchange.* No entitlement changes hands unless its owner's agent agrees.
- *Enforcement.* The state enforces contracts and adjudicates disputes, and fraud and violence are excluded.
- *Loyal agents.* Each agent maximizes its own principal's payoff and nothing else; we assume alignment is perfect.
- *Coalitions.* Coalitions are legal and cost nothing to form.
- *Voucher.* The state may pay each person a compute voucher $\underline{B}$, a floor under their bargaining budget, as Krier proposes.

Three questions are left open by this constitution, and the results turn on them.
The first is *decisiveness*, written $r$: how strongly out-computing the other side moves the split.
The second is how secure entitlements are, which we describe by the *contestable fraction* $\kappa$, the share of an entitlement's value that an ambiguity in its definition leaves open to challenge, and by the *challenge fee* $f$, the cost of bringing a challenge whatever its source (a court fee, delay, human attention).
The third is liquidity: whether a principal can pay for compute out of winnings it has not yet collected.

## The model

A *principal* is a household, firm or state with one loyal agent.
A *matter* is one bargain between two principals $i$ and $j$, and its *stake* $V_{ij}$ is the dollars of surplus, or of contested entitlement, at issue in it.
The surplus is measured over what each side could get elsewhere, so competition among employers for a worker or among landlords for a tenant shows up as a smaller stake and not as a different rule for dividing it.
A principal's *total stakes* $S_i=\sum_j V_{ij}$ are everything it has at issue in a period, spread over $m_i$ matters.
Compute costs $p$ dollars per unit.
Principal $i$'s *spend* $x_{ij}$ is the dollars of compute it puts into its matter with $j$, and its *budget* $B_i$ is the dollars it can spend on bargaining compute in a period, which rises with wealth.

### Two uses of compute

Compute enters a bargain in two ways, and they respond differently to a fall in its price.

The first is showing up.
Taking part in a matter at all requires finding the counterparty, parsing the matter, modelling the other side and stating terms.
We call the dollar cost of this the *showing-up cost* $c_0$.
It is a fixed requirement measured in units of compute, so $c_0$ falls in proportion to $p$.
This is the cost Krier is writing about, and he is right that it falls.

The second is claiming.
Once a surplus exists, it has to be divided, and each loyal agent wants more of it for its principal.
We model the division as a contest.
Principal $i$'s *share* of the stake in its matter with $j$ is

$$
\sigma_{ij} = \frac{x_{ij}^r}{x_{ij}^r + x_{ji}^r},
$$

the contest success function introduced by [Tullock (1980)](https://www.gbv.de/dms/zbw/02063613X.pdf) in his chapter "Efficient rent seeking" in the volume *Toward a Theory of the Rent-Seeking Society*.
With $r=1$, a side that spends twice as much as its opponent gets two thirds of the stake.
The money both sides together spend on compute to divide a stake we call *dissipation*.

We use this form for three reasons.
It has a search foundation that fits how agents work.
Suppose each unit of compute buys one independent draw of a candidate argument, contract clause or counter-proposal from a common continuous distribution, and the side holding the single best draw prevails.
If $i$ buys $q_i$ draws and $j$ buys $q_j$, the chance that $i$ holds the best of them is $q_i/(q_i+q_j)$ whatever the distribution, because each draw is equally likely to be the best.
Both sides pay the same price per draw, so this is also the ratio of dollars spent, and it is the contest with $r=1$.
Generating many candidates and keeping the best is a common way to run language-model agents.
The search story gives $\sigma_{ij}$ as a probability of taking the whole stake, and we use it as a share; for principals who care only about expected dollars the two are the same.
[Baye and Hoppe (2003)](https://ideas.repec.org/a/eee/gamebe/v44y2003i2p217-226.html) show that a tournament in which firms buy independent draws of ideas and the best idea wins is strategically equivalent to a Tullock game, and [Jia (2008)](https://doi.org/10.1007/s11127-007-9242-1) derives the ratio form from random shocks to performance.
The power form is also the member of the family axiomatized by [Skaperdas (1996)](https://doi.org/10.1007/BF01213906) for which only the ratio of efforts matters, so that multiplying every effort by the same factor changes nothing.
And it is a standard model of litigation spending; [Hirshleifer and Osborne (2001)](https://doi.org/10.1023/A:1017520505573) treat a legal battle as a contest in which success depends on the merits and on each side's effort.

### Decisiveness

The exponent $r$ is decisiveness.
As $r\to0$, extra compute does not move the split at all, which describes a solved bargaining problem or a protocol that ignores cleverness.
At $r=1$ we have the search benchmark above.
Values $r>1$ would mean increasing returns, for example if a model twice as large drew from a better distribution as well as drawing more often.
Our general results cover $0<r\le1$.

Decisiveness can be measured.
It is the slope of $\log\bigl(\sigma/(1-\sigma)\bigr)$ on $\log(x_i/x_j)$ in experiments where agents negotiate against each other with controlled compute ratios.
Nobody has reported that slope.
The evidence so far shows only that $r$ is positive and finite.
In Anthropic's [Project Deal (2026)](https://www.anthropic.com/features/project-deal), 69 agents made 186 deals; where the same item sold more than once, a seller represented by the stronger model got about \$2.70 more and a buyer represented by it paid about \$2.50 less, against a median price of \$12.
People represented by the weaker model rated the fairness of their deals the same as those represented by the stronger one (4.06 against 4.05 on a seven-point scale), so the losing side did not notice it was losing; the sample is small, as Anthropic says.
A stronger model is not the same thing as more compute, but it is what a larger budget buys, so we read this as evidence about the sign of $r$ and no more.
[Zhu et al. (2025)](https://arxiv.org/abs/2506.00073) describe agent-to-agent deal-making as "an inherently imbalanced game".
[Davidson et al. (2024)](https://arxiv.org/abs/2401.04536) find that even the strongest models sometimes lose to weaker ones, so the outcome is noisy and $r$ is not infinite.
[Imas and Misra (2026)](https://www.chicagobooth.edu/research/center-for-applied-artificial-intelligence/research/our-faculty-research/2026/agentic-interactions) find that outcomes also track the skill of the person who wrote the agent's instructions, and [Sharp et al. (2025)](https://arxiv.org/abs/2510.16853) discuss unequal agent quality and quantity as a source of stratification.

### Saturation {#saturation}

Suppose a bargaining problem had a finite *depth* $\bar q$, a number of units of compute beyond which more thinking adds nothing.
Then once compute is cheap enough both sides reach $\bar q$ and together spend $2p\bar q$ dollars, which goes to zero with $p$.
We assume they then split the stake evenly; more carefully stated, the split is whatever the merits and the two sides' outside options give, and compute no longer moves it.
Call this saturation.
A fixed finite depth is its simplest form, and below we widen the definition to any matter in which the effect of extra compute fades to nothing as both sides use more of it; a matter of either kind is a *saturating matter*.
If every matter saturates, Krier is simply right about cost, and most of what follows does not apply.

Saturation is not the same thing as diminishing returns.
For any $r\le1$ the contest above already has diminishing returns to a side's own spend, and yet, as the [first result](#claiming) shows, dissipation in a matter is $rV/2$ whatever compute costs.
What makes dissipation independent of the price $p$ is that only the ratio of the two sides' spends matters.
Saturation is a different property, the existence of an absolute level of compute beyond which nothing changes.
So the question to ask of a matter is whether it has an absolute scale or only a relative one.
A *non-saturating matter* is one in which the ratio of the two sides' compute goes on moving the split however much compute both use.
The contest above, in which only the ratio matters at every scale, is the leading case.

The search story above gives a test for which matters saturate.
Each unit of compute buys one independent draw of a candidate argument, clause or counter-proposal, and a side uses its best draw.
If whoever holds the single best draw prevails, the chance of prevailing is $q_i/(q_i+q_j)$ whatever the distribution of candidate quality, as we saw.
That is $r=1$ at every scale, with no saturation, even if quality is bounded.
Now suppose instead that whoever decides the matter, whether a court, an arbitration protocol or the other side's own assessment, compares the two best draws with an error of fixed size, so that a small enough gap between them is as good as a tie.
Then what happens as both sides' compute grows depends on the upper tail of the distribution of candidate quality, which is to say on how fast the best of many draws improves as the number of draws rises.

To describe this we let decisiveness depend on the level of compute.
We write $r(q)$ for the decisiveness measured when both sides use $q$ units of compute, that is, the slope of the log-odds of prevailing on the log of the compute ratio, defined above, taken at equal compute $q$.
A fixed depth is the extreme case, in which $r(q)$ is zero beyond $\bar q$.
More generally we say a matter saturates if $r(q)$ falls to zero as $q$ grows over the range of compute the parties will use.
Between two unconstrained sides each side's equilibrium spend is $Vr(q)/4$, which then goes to zero with the price of compute.
A matter is non-saturating if $r(q)$ stays away from zero over that range.
The table gives $r(q)$ for four kinds of upper tail, when the decider's error has a logistic distribution whose scale parameter, which we write $\varsigma$, equals one standard deviation of a single draw.
We derived it for this article and checked it numerically with the script described in the [appendix](#app-script); it is not a published result.

| Upper tail of candidate quality | $r(10)$ | $r(100)$ | $r(1{,}000)$ | $r(10{,}000)$ | $r(10^6)$ | Reason |
|---|---|---|---|---|---|---|
| bounded (uniform), so a best answer exists | 0.27 | 0.034 | 0.0035 | 0.0003 | 0.0000 | the gap between the two bests shrinks like $1/q$, and $r(q)\approx 1/(\varsigma q)$ for large $q$ |
| exponential | 0.65 | 0.66 | 0.67 | 0.67 | 0.67 | the gap depends only on $\log(q_i/q_j)$, so $r$ is constant, and the matter is the contest of this article with $r=2/3$ |
| Gaussian | 0.44 | 0.33 | 0.27 | 0.24 | 0.19 | the gap shrinks like $1/\sqrt{2\ln q}$, so $r$ falls, but slowly |
| power law (index 3) | 0.62 | 0.83 | 0.94 | 0.99 | 1.00 | the gap grows with $q$, the decider's error stops mattering, and $r\to1$ |

The same calculation gives each side's equilibrium spend on a \$10,000 stake as the price of a draw falls from \$1 to 1 cent to a hundredth of a cent.
With a bounded tail the spend falls from \$92 to \$9.30 to \$0.93, in proportion to $\sqrt p$.
With an exponential tail it is \$1,667 at every price.
With a Gaussian tail it falls from \$698 to \$542 to \$457, so a ten-thousandfold fall in price cuts spend by about a third.

Saturation therefore needs two things together, a best answer that exists and a decider that ignores small gaps.
Bounded quality alone is not enough.
High-frequency trading is an example of bounded quality without saturation.
The speed differences between traders are tiny and bounded below by physics, but a trade goes to whoever is ahead by any margin.
[Budish, Cramton and Shim (2015)](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1547-1621.html) find that competition did not change the size or frequency of the arbitrage opportunities and only raised how fast a trader must be to capture them.
Their remedy, frequent batch auctions, works by making time discrete, so that tiny speed advantages stop mattering.

The Gaussian row shows that returns which diminish on average can still fail to saturate over any range of compute that will be observed.
Between $q=10$ and $q=10^6$ its $r(q)$ falls only from 0.44 to 0.19.
Its $r(q)$ does reach zero in the limit, but so slowly that by our definition a matter of this kind is non-saturating, with decisiveness that drifts down as compute grows.
The bounded, exponential and power-law rows are the three kinds of limit that the best of many independent draws can approach, a standard result of extreme value theory (the Fisher–Tippett–Gnedenko theorem).
The Gaussian tail approaches the same kind of limit as the exponential one.
Its row differs because the spread of its best draw narrows as the number of draws grows.
We know of no published version of this table; the nearest published result we know of is the derivation by [Jia (2008)](https://doi.org/10.1007/s11127-007-9242-1), cited above, of the ratio form from random shocks to performance.

We carry three cases through the rest of the article.
In the *saturating world* every matter is a saturating matter.
In the *non-saturating world* every matter is non-saturating; this is our main case, and most of the results are derived for it.
In the *mixed world* a fraction $\phi$ of a principal's total stakes $S_i$ is in non-saturating matters, and the rest is in saturating ones.
The fraction can differ between principals, and we write $\phi$ for whichever principal is under discussion.

We doubt that every matter saturates for one further reason, which is an argument and not a theorem.
The complexity of a contract is chosen by the parties.
Checking a contract with $K$ interacting clauses means checking $K(K-1)/2$ pairwise interactions, a number that grows as $K^2$, and a contract conditioned on $C$ yes-or-no contingencies has $2^C$ states to consider.
The side with more compute can add clauses until the other side cannot verify them.
The weaker side may refuse what it cannot verify, but then it forgoes the deal or settles for a simpler and less valuable one, so the difference in what the two sides can verify still moves the split.
Deliberate complexity of this kind survives competition in consumer markets: [Carlin (2009)](https://ideas.repec.org/a/eee/jfinec/v91y2009i3p278-287.html) shows firms adding price complexity to keep some consumers uninformed, with prices that may rise as firms enter, and [Gabaix and Laibson (2006)](https://ideas.repec.org/a/oup/qjecon/v121y2006i2p505-540..html) show shrouded add-on prices persisting in highly competitive markets.
[Bakos, Marotta-Wurgler and Trossen (2014)](https://doi.org/10.1086/674424) found that only one or two shoppers in a thousand open the licence agreement they accept.
If complexity rises as compute gets cheaper, the depth $\bar q$ is not fixed and saturation does not arrive.
The [section on the three worlds](#three-worlds) works out when the stronger side gains by doing this.
Computation as part of bargaining strategy has a literature of its own: [Larson and Sandholm (2001)](https://www.sciencedirect.com/science/article/pii/S0004370201001321) find that equilibria of bargaining with limited computation can be inefficient, in the sense that another outcome would leave one side better off and neither worse off, and [Halpern and Pass (2015)](https://arxiv.org/abs/1412.2993) build game theory with costly computation from the ground up.
Which matters between agents saturate is an empirical question, and the experiment that measures $r$ would answer it, matter type by matter type: saturation shows up as $r(q)$ falling towards zero as both sides' compute $q$ grows.

### Symbols and the people in the stories

Four principals recur in the examples.
*Asha* is a nurse who rents.
She has \$25,000 a year of surplus at issue: about \$12,000 in her employment contract, \$6,000 in her lease, \$2,000 with her insurer, \$1,000 with platforms, and \$4,000 spread over a couple of hundred small matters with neighbours.
She can spend \$400 a year on agent compute.
*Meridian* stands for the firms on the other side of her large matters, her employer, landlord and insurer; its budget never runs out and it deals with many households on the same terms.
*Bram* is Asha's neighbour, with a budget like hers.
*Odile* is a retired homeowner with a house worth \$500,000, a pension, and \$400 a year for agent compute.

| Symbol | Name | Meaning | In the stories |
|---|---|---|---|
| $V_{ij}$ | stake | dollars at issue in the matter between $i$ and $j$ | the \$6,000 of surplus in Asha's lease; the \$10,000 of Odile's property a challenge puts at issue |
| $S_i$ | total stakes | the sum of $i$'s stakes over all its matters | Asha's \$25,000 a year |
| $m_i$ | number of matters | how many matters $i$ is party to in a period | Asha's few large matters plus a couple of hundred small ones |
| $B_i$ | budget | dollars $i$ can spend on bargaining compute in a period | Asha's \$400 a year; Odile's \$400 |
| $x_{ij}$ | spend | dollars of compute $i$ puts into its matter with $j$ | what Asha's agent spends on her lease; what Meridian spends against her |
| $p$ | price of compute | dollars per unit of compute | falls over time in every story |
| $r$ | decisiveness | how strongly outspending the other side moves the split | how much Meridian gains by out-computing Asha |
| $\bar q$ | depth | units of compute in a matter beyond which more adds nothing; a non-saturating matter has none, or has one too large to be reached at current prices | the compute beyond which more argument about Asha's lease would change nothing, if her lease saturates |
| $\phi$ | fraction of stakes in non-saturating matters | the part of $S_i$ in matters that never saturate | 100% of Asha's \$25,000 in the non-saturating world; a fifth of it in one mixed-world example |
| $\sigma_{ij}$ | share | the fraction of the stake that $i$ gets | the fraction of the lease surplus that ends up with Asha |
| $\lambda_i$ | value of a budget dollar | surplus $i$ gains from one more dollar of spend; at least 1 | nearly 7 for Asha |
| $s_i$ | strength | $1/\lambda_i$; equal to 1 when the budget does not bind | 1 for Meridian; about 0.14 for Asha |
| $c_0$ | showing-up cost | dollars needed to take part in a matter at all | what it costs Asha's agent to read a matter and state terms |
| $E$ | entitlement value | what an entitlement is worth in dollars to its holder | Odile's \$500,000 house |
| $\kappa$ | contestable fraction | the share of $E$ that a challenge can put at issue | the 2% of Odile's house value an old easement leaves open |
| $\theta$ | defender advantage | how many of a challenger's dollars one defender's dollar is worth | 3 in Odile's case |
| $f$ | challenge fee | what it costs a challenger to bring a challenge | \$1,000 in Odile's case |
| $V^\ast(B)$ | safe stake | the largest contestable stake nobody gains by challenging, for a holder with budget $B$ | the largest piece of Odile's property nobody finds it worth challenging |
| $\underline B$ | voucher | a state-paid floor under budgets | a state top-up to Asha's budget |
| $N$ | number of similar matters | matters across which a firm can reuse the same work | the households on Meridian's standard lease |

The strength $s_i$, the defender advantage $\theta$ and the safe stake $V^\ast$ are derived in the sections that use them.
Symbols that appear in only one section are defined there.

## Results

Every section of the results except one is derived for non-saturating matters, which is to say for the non-saturating world.
A few of those sections add one sentence on what changes in the mixed world.
The exception is the [section on the three worlds](#three-worlds), which follows the section on more matters; it works out what changes in the saturating and mixed worlds, and asks who chooses whether a matter saturates.

### Cheap compute does not make claiming cheap {#claiming}

Take one matter, a stake $V$, and two sides with no budget limit.
Each chooses its spend to maximize $V\sigma_{ij}-x_{ij}$.
In equilibrium, where neither side can gain by changing its spend given what the other spends, each spends $x^\ast=rV/4$ dollars, that is $q^\ast=rV/(4p)$ units of compute, and dissipation is $rV/2$ dollars.
The price of compute $p$ appears only in the number of units bought.
Halve the price of compute and both sides buy twice as much, and the dollars spent do not change.

So in the claiming part of a bargain the transaction cost of a matter is $rV/2$, proportional to the stake.
A \$10,000 legal fight over a \$40,000 stake with $r=0.5$ stays a \$10,000 fight when compute becomes cheap; it just contains more computation.
Krier's phone analogy does not carry over.
A phone is not used against anyone, so a cheaper phone is simply cheaper.
Bargaining compute is used against someone who also has it, and what each side buys is set by what the other side buys.

For $0<r\le1$ each side's payoff is concave in its own spend $x_{ij}$, and in equilibrium neither side randomizes.
We do not cover $1<r\le2$.
For $r>2$ the two sides randomize their spending in equilibrium and, when spending can be any amount, the whole stake is dissipated on average, though never more than the stake ([Baye, Kovenock and de Vries (1994)](https://doi.org/10.1007/BF01053238)).

The history of transaction costs is consistent with this, though it does not test it.
[Wallis and North (1986)](https://www.nber.org/system/files/chapters/c9679/c9679.pdf) measured the transaction sector of the US economy (lawyers, finance, trade, clerical work) growing from about a quarter of national product in 1870 to over half in 1970 on their broader definition, over a century in which the cost of each transaction fell.

### Many matters and one budget give each principal a strength {#strength}

Asha does not have one matter.
She has a large one with her employer, smaller ones with her landlord and insurer, and many small ones with neighbours, and she pays for all of them from one budget of \$400.
Meridian's firms are in the same position with respect to their own matters, except that their budgets are large enough never to run out.

Formally, principal $i$ chooses spends $x_{ij}\ge0$ on all its matters to maximize $\sum_j\bigl(V_{ij}\sigma_{ij}-x_{ij}\bigr)$ subject to $\sum_j x_{ij}\le B_i$.
Let $\lambda_i\ge1$ be the value to $i$ of one more dollar of bargaining spend, holding everyone else's spending fixed.
When the budget is slack $\lambda_i=1$, because the marginal dollar spent then returns one dollar; when it binds, $\lambda_i>1$.
We define $i$'s *strength* as $s_i=1/\lambda_i$, a number in $(0,1]$ that equals 1 when the budget does not bind.
Each side spends on a matter up to the point where its last dollar there returns $\lambda$ dollars of the stake.
Writing that condition for both sides of the same matter gives $x_{ji}/x_{ij}=\lambda_i/\lambda_j$, and so, for $0<r\le1$,

$$
\sigma_{ij} = \frac{s_i^r}{s_i^r+s_j^r},\qquad x_{ij} = r\,V_{ij}\,\sigma_{ij}\,\sigma_{ji}\,s_i .
$$

Principal $i$ has $s_i=1$ if $r\sum_j V_{ij}\sigma_{ij}\sigma_{ji}\le B_i$, and otherwise $s_i<1$ solves $\sum_j x_{ij}=B_i$.
The equilibrium of the whole economy is the vector of strengths $(s_1,\dots,s_n)$ solving these $n$ equations.
The derivation is in the [appendix](#app-strength).

The outcome of every matter depends on the two parties' strengths and on nothing else about them, in the same form as a chess rating, where a player's expected score against any opponent follows from the two ratings (statisticians call this a Bradley–Terry model).
Strength is not wealth.
It measures how far a principal is from running out of budget, given everything it has at issue.

The formula is not new for $r=1$.
For $r=1$ and budgets that must be spent in full, it is Lemma 1 of [Díaz-García, Bullo and Marden (2024)](https://arxiv.org/abs/2408.00883), who study budget-limited players in bilateral lottery contests on the edges of a graph and replace each budget with a multiplier $\lambda_i$; written in $s_i=1/\lambda_i$ their result is ours.
We add three things to it.
Money here has an outside use, so $\lambda_i\ge1$ and a principal whose budget is large enough is unconstrained, with $s_i=1$.
The formula is extended from $r=1$ to any $0<r\le1$.
And the sections that follow work out what the formula implies for shares, dissipation, vouchers and coalitions.
[Friedman (1958)](https://doi.org/10.1287/opre.6.5.699) had earlier shown that two budget-limited players facing many lottery contests can allocate in proportion to the value of each contest in equilibrium.
[Franke and Öztürk (2015)](https://doi.org/10.1016/j.jpubeco.2015.04.002) prove a unique interior equilibrium for bilateral contests on a network with a convex cost of total spending, and [Xu, Zenou and Zhou (2022)](https://cepr.org/system/files/publication-files/DP13647.pdf) prove existence and, under a further condition on costs, uniqueness for general conflict structures.
Neither covers a hard budget combined with an outside value of money, so we do not claim a uniqueness theorem.
The script described in the [appendix](#app-script) computes the strengths by iterating on these equations.
We checked with it, on random networks mixing constrained and unconstrained principals and for $r\in\{0.25,0.5,1\}$, that no principal can gain by deviating from the computed equilibrium (the largest relative gain found was $2\times10^{-12}$), and that the iteration reaches the same strengths from 20 random starting points.

The case that carries most of this article is Asha's: one constrained principal whose counterparties are all unconstrained.
This treats the \$4,000 she has at issue with neighbours of her own strength as if it too were at issue with unconstrained counterparties, which changes the figures little, and it assumes Meridian's agent works on her matters alone, an assumption the [section on repeat players](#repeat-players) removes.
With $s_j=1$ for every counterparty and $r=1$, and with $B_i<S_i/4$, Asha's share in every matter is $\sigma_i=\sqrt{B_i/S_i}$.
She takes $\sqrt{B_iS_i}$ in total.
Her counterparties together spend $\sqrt{B_iS_i}-B_i$ against her and net $\bigl(\sqrt{S_i}-\sqrt{B_i}\bigr)^2$.
She splits her budget across matters in proportion to their stakes, as in Friedman's result.
If $B_i\ge S_i/4$ her budget does not bind, she gets half of everything, and she spends $S_i/4$.
For general $r$ the threshold is $rS_i/4$, and below it her strength $s$ solves $rS_is^{1+r}/(1+s^r)^2=B_i$, with share $\sigma=s^r/(1+s^r)$.

In Asha's case the threshold is \$6,250 at $r=1$, more than fifteen times her budget.
She gets about an eighth of her surplus, roughly \$3,200 of the \$25,000, while Meridian spends about \$2,800 against her and nets about \$19,000.
Lower decisiveness helps her a lot: at $r=0.25$ she gets over 40%.

| | $r=1$ | $r=0.5$ | $r=0.25$ |
|---|---|---|---|
| budget needed for an even split, $rS/4$ | \$6,250 | \$3,125 | \$1,562 |
| Asha's share | 12.6% | 28.4% | 41.7% |
| Asha takes | \$3,162 | \$7,101 | \$10,433 |
| Meridian spends against her | \$2,762 | \$2,542 | \$1,520 |
| Meridian nets | \$19,075 | \$15,358 | \$13,047 |
| dissipated fraction of $S$ | 12.6% | 11.8% | 7.7% |

At $r=1$ Asha nets about \$2,800 after paying for her \$400 of compute, which is more than the nothing she would get without bargaining.
That is Krier's point, and the model supports it.
The model adds that she gets about an eighth of the surplus and Meridian most of the rest.

Between unequal constrained principals the formula says where each spends.
The product $\sigma_{ij}\sigma_{ji}$ is largest at an even match, so a principal spends most where stakes are large and the opponent is close to its own strength.
Asha and Bram have similar strengths, so each gets about half of their shared matters, and Asha spends more per dollar of stake on her matters with Bram than on those with Meridian.
Against counterparties much stronger than herself she rationally concedes most of the surplus and saves her budget for matters where it buys more.

To see the formula at work across a population we ran a numerical experiment, to which later sections return.
It has 3,000 households with log-normal budgets of median \$400 (10th percentile \$58, 90th \$2,675, 99th \$12,906).
Each household has \$20,000 a year at issue with unconstrained firms and about 20 matters of \$250 each with randomly chosen other households.
At $r=1$, 96% of the households are constrained.
Households in the bottom tenth by budget get on average about 3% of the surplus in their matters with firms, those in the middle tenth about 12% and those in the top tenth about 44%.
Households as a group keep about a fifth of all surplus after paying for their compute, firms keep about two thirds, and the rest is dissipated.

### More matters stretch the budget thinner {#more-matters}

Krier's world multiplies the matters each principal is party to.
With $n$ principals there can be up to $n-1$ bilateral matters per principal and $n(n-1)/2$ overall, which is $O(n^2)$ in $n$, before counting matters with more than two parties.
Every potential bargain with a stake above the showing-up cost becomes worth opening to any principal with budget to spare.
In the mixed world only the non-saturating matters count towards $S_i$ in what follows, because a saturating matter is split evenly at negligible cost once compute is cheap, and so takes next to nothing from the budget; the [next section](#three-worlds) works this out.

If Asha's stakes double to \$50,000 and her budget stays at \$400, her share falls from about 13% to about 9% while her take rises from about \$3,200 to about \$4,500.
With $B_i$ fixed and $r=1$ her share falls as $S_i^{-1/2}$ in total stakes $S_i$.
With stakes of \$250 per matter and a \$400 budget, ten matters give a share of 40%, a hundred give 12.6%, a thousand give 4% and ten thousand give 1.3%.

New matters also draw budget away from old ones.
In the population experiment of the [section on strength](#strength), multiplying the matters between households tenfold cuts the median household's share against firms from 11.5% to 4.0%.
Its take on the unchanged \$20,000 of matters with firms falls from about \$2,300 to about \$800, because its budget moved to the new matters.
The household gains more than that on the new matters, as long as they are new surplus; the [section on contestable entitlements](#entitlements) treats the case where they are not.

The showing-up cost sets how many matters a principal can attend at all.
Suppose each matter costs $c_0$ to attend and has stake $V$, and a constrained principal faces unconstrained counterparties.
It attends $k^\ast=\min(m,B/(2c_0))$ matters, spending half its budget on turning up and half on contesting, and takes $(B/2)\sqrt{V/c_0}$ in total.
The number of bargains a principal can attend is proportional to its budget $B$, and on the rest it gets whatever it would get with no bargain at all.

If stakes are heavy-tailed, so that $M(v/v_0)^{-\alpha}$ matters have stake above $v$, with $\alpha>1$ (many small matters, few large ones), the best fraction of the budget to spend on showing up is $(\alpha-1)/(2\alpha-1)$, and the stakes in play grow without bound as $c_0\to0$.
With $\alpha=1.5$, $M=50$ matters above $v_0=\$250$, the same power law continuing down to smaller stakes, and a \$400 budget, as $c_0$ falls from \$20 to \$0.02, the matters attended rise from 5 to 5,000, the stakes in play from about \$17,000 to about \$174,000, the share falls from 13% to 4% and the take rises from about \$2,300 to about \$7,200.
Cheap compute does to $c_0$ what Krier says it does, and the consequence is a larger $S_i$ set against the same $B_i$.

### Saturating, non-saturating and mixed worlds {#three-worlds}

The sections so far assume that no matter saturates.
Here we take Asha through each of the three worlds defined in the [section on saturation](#saturation), keeping $r=1$, her total stakes $S=\$25{,}000$ and her budget $B=\$400$.

#### The saturating world

Take one matter with stake $V$ and depth $\bar q$ between two unconstrained sides.
Neither side gains from compute beyond $\bar q$, so each side's spend is capped at $p\bar q$, and together they spend $\min(rV/2,\;2p\bar q)$ dollars (derivation in the [appendix](#app-saturation)).
While the cap is above what each would spend without it, the [first result](#claiming) stands; once the price of compute falls far enough, spending falls in proportion to $p$.

A fixed depth is saturation in its simplest form.
In the bounded row of the table in the [section on saturation](#saturation) saturation is gradual, and spend falls as $\sqrt p$ and not in proportion to $p$.
We work the budget-limited case for a fixed depth only.
For gradual saturation we expect the same direction of change, since there decisiveness itself falls as compute grows and lower decisiveness evens shares, as Asha's table in the [section on strength](#strength) shows; we have not computed it.

For Asha we take the depth of each of her matters to be proportional to its stake, so that each side's total spend over all her matters is capped at $c$ dollars, and we let $c$ fall with the price of compute.

| cap $c$ on each side's spend | Asha spends | firms spend | Asha's share | dissipated fraction of $S$ |
|---|---|---|---|---|
| \$2,762 or more (the cap does not bind) | \$400 | \$2,762 | 12.6% | 12.6% |
| \$1,600 | \$400 | \$1,600 | 20% | 8.0% |
| \$800 | \$400 | \$800 | 33% | 4.8% |
| \$400 | \$400 | \$400 | 50% | 3.2% |
| \$100 | \$100 | \$100 | 50% | 0.8% |
| \$10 | \$10 | \$10 | 50% | 0.08% |

While $B<c<\sqrt{BS}-B$ the cap binds the firms but not Asha, and her share is $B/(B+c)$.
Once $c\le B$ both sides are at the cap and split evenly.
The cap binds the stronger side first, so falling compute prices first raise Asha's share and only then cut her own bill.
In this world Krier is right about cost and also about distribution, because the split stops depending on compute.
That the two sides split a saturated matter evenly is the assumption we made in the [section on saturation](#saturation); more carefully stated, the split is whatever the merits and the two sides' outside options give, and compute no longer moves it.

#### The non-saturating world

The non-saturating world is the one every other section of these results describes.
In it Asha gets about an eighth of her surplus.

#### The mixed world

Now suppose a fraction $\phi$ of Asha's stakes is in non-saturating matters, and the rest saturates at negligible cost and is split evenly.
She then puts her whole budget into the non-saturating part, so every formula of the [section on strength](#strength) and the [section on more matters](#more-matters) holds there with $S$ replaced by $\phi S$.
For $r=1$ and $B<\phi S/4$, her share in non-saturating matters is $\sqrt{B/(\phi S)}$, her overall share of $S$ is $(1-\phi)/2+\sqrt{\phi B/S}$, and the dissipated fraction of $S$ is $\sqrt{\phi B/S}$.
If $\phi\le 4B/S$, which is 6.4% for Asha, her budget covers an even fight over all of the non-saturating part and she gets half of everything.

| $\phi$ | share in non-saturating matters | Asha takes | overall share | dissipated fraction of $S$ |
|---|---|---|---|---|
| 100% (non-saturating world) | 12.6% | \$3,162 | 12.6% | 12.6% |
| 50% | 17.9% | \$8,486 | 33.9% | 8.9% |
| 20% | 28.3% | \$11,414 | 45.7% | 5.7% |
| 6.4% | 50% | \$12,500 | 50% | 3.2% |
| 2% | 50% | \$12,500 | 50% | 1.0% |

We also checked this directly with her actual matters.
If only the lease, \$6,000 of surplus, is non-saturating, and each of her other four groups of matters (job, insurer, platforms, and the small matters with neighbours taken as one) saturates at \$5 a side, the computed equilibrium gives her 25.2% of the lease surplus and \$11,010 in all.
That matches the closed form $\sqrt{380/6000}$ for her lease share, \$380 being what is left of her \$400 after \$5 on each of the other four.

The mixed world is much better for Asha in total than the non-saturating world, because she gets half of everything that saturates.
Within the non-saturating part nothing in the results changes in kind.
Her share there still falls as non-saturating stakes multiply, the voucher that buys her parity there costs $r\phi S/4$ (see the [section on dissipation](#dissipation)), and even shares there still come at the cost of more dissipation.
So in the mixed world what matters for every result is the stake-weighted fraction $\phi$, and not the number of matters that saturate.

Stakes are plausibly heavy-tailed, and then a few matters hold a large part of the total stake, so whether those few saturate has a large effect on $\phi$.
With stakes following the power law of index $\alpha$ in the [section on more matters](#more-matters), the largest 1% of matters hold a fraction $0.01^{1-1/\alpha}$ of total stake, about 10% at $\alpha=2$ and about 21% at $\alpha=1.5$; a simulation in the script agrees.
The formula $\min(rV/2,\;2p\bar q)$ also says which matters saturate as compute gets cheaper.
With a common depth, the matters with the largest stakes saturate first as $p$ falls.
A matter with a fixed depth behaves as a non-saturating one until the price of compute falls far enough for its cap to bind, and it goes on doing so as $p$ falls only if its depth grows at least as fast as $1/p$.
A matter that stays non-saturating however cheap compute becomes is therefore one whose depth is unbounded, or one whose depth some party chooses.

#### Who chooses the world

The [section on saturation](#saturation) argued that the stronger side can add clauses until the weaker side cannot verify them, so that depth can be chosen.
Suppose a firm can choose whether its matter with a household saturates or does not.
If the matter saturates, the split is even by our assumption, spending is negligible, and the firm nets $V/2$.
At $r=1$, against a household of strength $s$, the firm nets $V/(1+s)^2$ on a non-saturating matter ([appendix](#app-saturation)).
So it prefers the non-saturating matter when the household's share there would be below $1-1/\sqrt2$, about 29%, which is when the household's budget is below $(1-1/\sqrt2)^2$, about 8.6%, of its non-saturating stakes.
For $r=0.5$ the thresholds are a share of 38% and a budget of 4.5% of those stakes, and for $r=0.25$ they are 44% and 2.3%.
Against an unconstrained opponent the firm nets $V/4$, less than $V/2$, and prefers the matter to saturate.
So in this model, where raising the depth of a matter costs the firm nothing, complexity is chosen against counterparties who cannot afford the contest, and not against equals.

The choice reinforces itself across firms, because every additional non-saturating matter spreads the household's budget over more stakes and lowers its share in all of them.
We took Asha's matters with firms (\$12,000 with her employer, \$6,000 with her landlord, \$2,000 with her insurer and \$1,000 with platforms, \$21,000 in all), left aside her small matters with neighbours, and let the firms revise their choices in turn until none wanted to change.

| household budget | starting with every matter saturating | starting with none saturating |
|---|---|---|
| \$400 (Asha) | all four end non-saturating | all four stay non-saturating |
| \$1,500 | all four stay saturating | all four stay non-saturating |
| \$3,000 | all four stay saturating | all four end saturating |

Every matter saturating is an equilibrium when the household's budget is at least 8.6% of its largest single stake with a firm, \$1,030 here.
No matter saturating is an equilibrium when the budget is below 8.6% of all its stakes with firms, \$1,800 here.
Between the two, both are equilibria, and which one the household ends up in depends on where it starts.
Asha's \$400 is below 8.6% of her job stake alone, so her employer makes that matter non-saturating whatever the others do, and the other firms follow.

These conclusions assume that the depth of a matter is the stronger side's choice and costs nothing to raise.
On that assumption, the mixed world does not last within one household's dealings with firms; as the firms revise their choices it ends with every matter saturating or with none.
Across the population the outcome is then a division by budget, which is not the mixed world as we defined it: well-funded households are in the saturating world and poorly funded ones in the non-saturating world.
A household's own mixed world survives where depth is fixed by the nature of the matter or by a protocol the firm cannot alter.
So neither the saturating world nor the non-saturating world is the right assumption for everyone, and which one holds for a given principal depends on its budget and on who sets the depth.

### At $r=1$ the weaker side's share equals the fraction dissipated {#dissipation}

When Asha and Meridian bargain, the compute they burn between them comes to about 13% of the stake, the same as Asha's share.
If Asha were funded to parity, each side would net \$6,250 and half the stake would go on compute.
The more evenly matched they are, the more of the surplus they burn.

Dissipation in a matter is $x_{ij}+x_{ji}=rV\sigma_{ij}\sigma_{ji}(s_i+s_j)$.
For $r=1$ this is $Vs_is_j/(s_i+s_j)$, and against an unconstrained counterparty ($s_j=1$) it equals $V\sigma_{ij}$.
The fraction of the stake dissipated is then the weaker side's share, and what is left after compute is $V(1-\sigma_{\text{weak}})$.

Dissipation is largest between equals, half the stake at $r=1$, and goes to zero as one side becomes too poor to contest.
For Asha against Meridian 12.6% is dissipated and total surplus net of compute is about \$21,800 of \$25,000.
With Asha funded to parity the total net surplus is \$12,500.

A planner who maximizes total surplus net of costs, which is the criterion Coasean reasoning uses, therefore prefers Asha weak.
In this model, maximizing wealth and splitting evenly pull in opposite directions.
At $r=1$ the exchange is one point of share for one point of dissipation.
At lower $r$ dissipation still rises as the weaker side gains strength, but it rises more slowly and ends lower: at $r=0.25$ a household funded to parity has half the surplus with an eighth of it dissipated.
[Che and Gale (1997)](https://doi.org/10.1023/A:1017937708549) found related behaviour in Tullock contests with budget-limited players, where a lower exponent can produce more dissipation than a higher one and rents stay under-dissipated.

This identity puts a price on Krier's voucher.
To give a household an even split the voucher must raise its budget to $rS_i/4$, which at $r=1$ is a quarter of its stakes.
That is a fraction of stakes, fixed in dollars, and it does not fall when compute gets cheaper.
In the mixed world only the non-saturating stakes need contesting, so the voucher that gives parity costs $r\phi S_i/4$, still a fixed fraction of stakes.
Firms answer the voucher by spending more, since a firm's spend against household $i$ rises as $s_i$ rises towards 1.

The table takes the population experiment of the [section on strength](#strength) through four scenarios: the baseline, two sizes of voucher, and lower decisiveness with no voucher.
"Household side, net" is what households end up with after all compute spent on their behalf, including any part the state paid for through the voucher; it, the firms' net and dissipation sum to 100% of surplus.
"State pays" is the voucher's cost, and "households privately keep" adds it back to show what households keep from their own pockets.

| scenario | households constrained | bottom-decile share vs firms | median share vs firms | top-decile share vs firms | dissipated | household side, net | firms, net | state pays | households privately keep |
|---|---|---|---|---|---|---|---|---|---|
| baseline, $r=1$ | 96.1% | 2.6% | 11.5% | 44% | 14.5% | 20.5% | 65.0% | 0% | 20.5% |
| voucher floor \$2,000 | 96.5% | 27.7% | 27.7% | 43% | 28.3% | 27.0% | 44.7% | 5.8% | 32.8% |
| voucher floor \$6,250 | 41% | 49.7% | 49.7% | 50% | 49.7% | 27.8% | 22.5% | 23.5% | 51.3% |
| $r=0.25$, no voucher | 82% | 28.1% | 41.7% | 50% | 8.0% | 45.0% | 47.0% | 0% | 45.0% |

The \$2,000 voucher costs the state about 6% of total surplus and raises dissipation by about 14 points.
The household side's net take rises by about 6.5 points and the firms' falls by about 20.
The parity voucher of \$6,250 costs the state nearly a quarter of total surplus, and half of everything is dissipated.
Moving from no voucher to parity lowers the firms' net by 42.5 points of surplus.
The household side, with the cost of the voucher counted against it, gains 7.3 of those points, and the other 35.2 are dissipated.
Most of what the voucher takes from firms is spent on compute and does not reach households.
The share of households that are constrained rises slightly under the smaller voucher because each household's neighbours are now stronger, which raises what it must spend to hold its position against them.
The last row is a contrast: lowering decisiveness from $r=1$ to $r=0.25$ with no voucher gives households 45% of surplus and dissipates 8%.

### A binding budget puts everything else on sale {#liquidity}

Asha's \$400 is worth far more to her than \$400.
Once Meridian's firms have adjusted to her budget, one more dollar of it brings her nearly \$4 of surplus.
So she gains by selling small things she owns for cash at any price above roughly a quarter of what they are worth to her, and putting the cash into her agent.
The figure applies to the next dollar, and each further dollar of budget is worth a little less.

In equilibrium, with counterparties anticipating the budget, a constrained principal's take is $\sqrt{B_iS_i}$, so one more dollar of budget is worth $\tfrac12\sqrt{S_i/B_i}$ dollars of surplus, about \$3.95 for Asha.
Holding the opponents' spending fixed instead, the marginal dollar is worth $\lambda_i=\sqrt{S_i/B_i}-1$, nearly \$7 for Asha; the smaller figure lets the opponents respond.
Krier's poor farmer sells his pollution right cheaply because he needs cash now.
The model supplies one reason cash can be worth that much to him: a dollar of it brings several dollars in his other bargains.
The more matters the Coasean world opens, the larger $S_i$ becomes, the higher that premium, and the cheaper constrained principals sell.

If principals could borrow freely against expected winnings, nobody would be constrained.
Every share would be one half and dissipation would be $rV/2$ in every matter.
Third-party funders already do this for lawsuits, taking a share of the proceeds.
Credit therefore moves the economy from the unequal, low-dissipation outcome to the equal, maximum-dissipation one.
Neither is the frictionless Coasean outcome in which the whole surplus goes to the parties.

### Repeat players and what a coalition buys {#repeat-players}

Meridian uses one lease form for thousands of tenants.
An argument its agent finds about that lease works in every one of those matters, so compute spent once counts many times.
Each tenant's agent works alone.

Suppose a firm has the same matter with $N$ households, the stake per household is $V$, and each household spends $b$, which we hold fixed here.
The firm spends $X=\sqrt{NVb}-b$ once, and an isolated household's share is

$$
\sigma=\sqrt{\frac{b}{NV}},
$$

which falls as $N^{-1/2}$ in the number of households $N$.
With $b=\$100$ and $V=\$6{,}000$, roughly what Asha's agent spends on her lease and what is at issue in it, the share is about 13% at $N=1$, 1.3% at $N=100$ and 0.13% at $N=10{,}000$.
If all $N$ households pool their budgets into one shared argument the share returns to $\sqrt{b/V}$, about 13%.
Asha's eighth in the earlier sections assumed that Meridian's agent works on her matter alone.
If it reuses its work across $N$ tenants and they do not pool, her share of the lease surplus is smaller by the factor $N^{-1/2}$.

Krier's digital union therefore does real work in the model: it cancels the repeat player's economy of scale.
It returns the household to its position in the [section on strength](#strength), and it does not take the household past $\sqrt{b/V}$.
It works only for stakes common to all members, such as a shared lease, and not for the bespoke matters that hyper-granular contracting is meant to create.
[Galanter (1974)](https://www.cambridge.org/core/journals/law-and-society-review/article/8A16E3B6212A1A61E196841F092CF428) gives the classical account of repeat players against one-shot litigants.
A coalition that declares its price non-negotiable meets a further limit: the polluter's agent can commit too, and [Ellingsen and Miettinen (2008)](https://doi.org/10.1257/aer.98.4.1629) show that when commitment is cheap, bilateral bargaining produces either one-sided outcomes or a high probability of conflict.

### Entitlements are only as secure as the friction protecting them {#entitlements}

So far every stake has been new surplus, and under voluntary exchange nobody can end up below where they started.
That conclusion needs entitlements to be perfectly specified, and they are not.
Every legal entitlement is a finite text about an open-ended world.
[Battigalli and Maggi (2002)](https://doi.org/10.1257/00028280260344470) trace contractual incompleteness to the cost of describing the environment, [Anderlini and Felli (1994)](https://ideas.repec.org/a/oup/qjecon/v109y1994i4p1085-1124..html) and [Al-Najjar, Anderlini and Felli (2006)](https://ideas.repec.org/a/oup/restud/v73y2006i4p849-868.html) study events of which every finite description leaves exceptions, and [Bolton and Faure-Grimaud (2010)](https://ideas.repec.org/a/oup/restud/v77y2010i3p937-971.html) show that because deliberation takes time, contracts are left incomplete and assign control instead.
[Tirole (2009)](https://doi.org/10.1257/aer.99.1.265) models thinking before contracting as costly, with both an efficiency role and a rent-seeking role, so that contracts can be too complete or too incomplete.
We suppose that a fraction $\kappa$ of an entitlement's value is open to a good-faith challenge: a boundary, an ambiguous lease term, a claim the insurer disputes, a reclassified job duty.
Finding such ambiguities is a search problem, and cheap compute makes search cheap.

Odile has a house worth \$500,000, a pension, and \$400 a year for agent compute.
A neighbouring developer's agent finds a defect in a 1970s easement that puts \$10,000 of her property's value at issue, 2% of it.
Before agents, finding the defect would have taken a lawyer's retainer and months of work, more than the claim was worth, and nobody looked; with agents the search costs little.
Suppose the law favours the holder, so that a dollar spent defending counts three times as much as a dollar spent challenging, and that bringing the challenge costs the developer a fee of \$1,000.

If Odile were funded like Meridian, she would spend about \$1,900 defending and keep 75% of the contested \$10,000.
The challenger would net about \$600 before the fee, so the fee would deter the challenge.
With her \$400 she keeps about a third, roughly \$3,500, and the challenger nets about \$4,300, so the same fee does not deter it.

| Odile's position ($\theta=3$, stake \$10,000) | funded like Meridian | budget \$400 |
|---|---|---|
| she spends | \$1,875 | \$400 |
| she keeps | 75% | 34.6% (\$3,464) |
| challenger nets before the fee | \$625 | \$4,272 |
| deterred by a \$1,000 fee | yes | no |

Formally, a challenger pays a fee $f$, and the two sides then contest the stake $V=\kappa E$, where $E$ is the value of the entitlement.
The defender has a *defender advantage* $\theta\ge1$, meaning a defender's dollar counts $\theta$ times as much as a challenger's, so with $r=1$

$$
\sigma_D=\frac{\theta x_D}{\theta x_D+x_A},
$$

where $x_D$ and $x_A$ are the defender's and challenger's spends.
Here $\theta$ plays a role like that of the merits of the case in Hirshleifer and Osborne's litigation contest: it multiplies the effect of one side's spending.
Like the rest of the results, this contest is non-saturating, since only the ratio of the two sides' weighted spends matters at every scale.
We do not model what would be different if a challenge were a saturating matter.

If both sides are unconstrained, each spends $\theta V/(1+\theta)^2$, the defender keeps $\theta/(1+\theta)$ of the stake and the challenger nets $V/(1+\theta)^2-f$.
Before the fee this is positive for every $\theta$.
A defender advantage shrinks the prize but never makes a challenge unprofitable, and only the fee $f$ can do that.
This depends on the ratio form of the contest: [Hirshleifer (1989)](https://doi.org/10.1007/BF00153394) showed that under the ratio form neither one-sided submission nor two-sided peace can be an equilibrium, and he flagged that property as the form's weakness.
If the defender can spend only $b$, the challenger nets $\bigl(\sqrt V-\sqrt{\theta b}\bigr)^2-f$ and the defender keeps $\sqrt{\theta bV}$.

Nobody challenges a contestable stake of at most

$$
V^\ast(B)=\Bigl(\sqrt{\theta\min(B,\theta f)}+\sqrt f\Bigr)^2,
$$

which we call the *safe stake*; it depends on $\theta$ and $f$ as well as on the holder's budget $B$.
It runs from $f$ for a defender with no budget to $(1+\theta)^2f$ for an unconstrained one, and everything above it is challenged.
Both ends of that range are proportional to the challenge fee $f$.
With $\theta=3$ and $f=\$1{,}000$ the safe stake is \$1,000 with no budget, about \$4,400 with a \$400 budget and \$16,000 for an unconstrained defender.
At $f=\$100$ these become \$100, \$1,600 and \$1,600, and at $f=\$1$ they are \$1, \$16 and \$16.

The challenge fee $f$ is a transaction cost with three parts: finding the ambiguity, preparing the claim, and getting it heard.
The first two are search and drafting, which cheap compute makes cheap.
The third belongs to the state, and Krier's essay proposes to cut it too, through "automated dispute resolution" and enforcement that becomes near-instant computational verification.
So we read his programme as lowering $f$, although the essay does not put it in these terms and a state could choose to hold $f$ up.
As $f\to0$, the safe stake $V^\ast\to0$ for everyone.

When the fee exceeds $B/\theta$ for some holders, a contestable stake that is safe in well-funded hands is open to attack in theirs.
Challengers go where $\theta B_i$ is small relative to $\kappa E_i$, which describes principals who are rich in assets and poor in cash, such as Odile.

Challenges against a constrained defender also reinforce each other.
Each additional challenge splits her budget and makes every other challenge more profitable.
With a stake of \$10,000 per challenge, a defender budget of \$400 and $\theta=3$, one challenger nets about \$4,300, two net about \$5,700 each, four about \$6,800 each and eight about \$7,700 each.
At a fee of \$5,500 a lone challenge loses money and a joint one pays.
There are then two equilibria, one with no challenges and one with many, as in a bank run.

Even between equals, contestable entitlements can make bargaining a net loss.
Take two unconstrained principals with one matter of new surplus $V^+$ between them, each also able to challenge $V^-$ of the other's entitlements, with $f=0$.
Each challenge is individually profitable, so both happen.
The pair's net gain is $V^+/2-4\theta V^-/(1+\theta)^2$.
The pair is worse off than with no bargaining at all when $V^-/V^+>(1+\theta)^2/(8\theta)$, a ratio of one half at $\theta=1$, two thirds at $\theta=3$ and about 1.4 at $\theta=9$.
The stock of existing entitlements is plausibly many times the annual flow of new Coasean surplus, and if so a small $\kappa$ is enough to cross that line.
As back-of-envelope arithmetic only, with both inputs assumed for illustration: if each principal's entitlements are worth six years of its output, and the new surplus the pair gets from Coasean bargaining were a generous 10% of their combined output a year, then at $\theta=3$ the pair loses in any year in which the challenges brought against each of them put more than about 2% of its entitlement value at issue.

[Medema (2020)](https://ideas.repec.org/a/aea/jeclit/v58y2020i4p1045-1128.html) surveys the extortion objection to the Coase theorem, in which a party threatens harm in order to be paid to stop, and the standard reply that it matters only if resources are spent seeking the payment.
Challenges to entitlements are the case where resources are spent.
[ProPublica (2023)](https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims) reported that a US health insurer's review system let its doctors reject over 300,000 claims in two months, at an average of 1.2 seconds each.
The insurer's cost of contesting a claim had fallen almost to zero, and the patient's cost of an appeal had not.

The cost and delay that stop a good bargain from being struck also stop a challenge to Odile from being brought.
Lowering them helps the parties to the bargain and harms her.

We add a conjecture, without a model behind it.
Among principals who deal with each other repeatedly, each can answer a challenge with challenges of its own in later periods, and the threat of that should sustain mutual restraint.
Retaliation costs budget.
So we conjecture that the long-run pattern is peace among the unconstrained and challenges directed at the constrained.

### When the constraint cures itself and when it does not {#dynamics}

Suppose Asha's winnings are paid in cash, she spends all of them on next year's compute, and nothing else drains her budget.
Her \$400 becomes about \$3,200 the next year and about \$8,900 the year after, which is above the \$6,250 she needs to be unconstrained.
Within two years she bargains with Meridian as an equal.
On this path she spends her whole take on compute each year and keeps none of it until her budget passes the threshold, so it is the fastest the constraint can cure itself.

Formally, if stakes are new surplus paid in cash and nothing drains the budget, a constrained principal's budget follows $B_{t+1}=\sqrt{B_tS}$, so $B_t=S^{1-2^{-t}}B_0^{2^{-t}}$ and the gap closes doubly exponentially in $t$.
The constrained earn the highest return on compute, so they catch up.
[Hirshleifer (1991)](https://doi.org/10.1111/j.1468-0343.1991.tb00046.x) called a related effect the paradox of power: in his model poorer contenders rationally fight harder, and the richer side gains relatively only when decisiveness is high enough.
His model differs from ours, so we borrow the mechanism and not his threshold.
It is the best case for Krier, and in it inequality of strength is a short-run problem, as he says.
The society it converges to has every principal unconstrained and $r/2$ of every stake dissipated.

Now suppose the budget is whatever cash is left after living costs, and those costs exceed the principal's other income by $d$ each period.
The budget then follows $B_{t+1}=\sqrt{B_tS}-d$, which has an unstable threshold

$$
B_-=\Bigl(\bigl(\sqrt S-\sqrt{S-4d}\bigr)/2\Bigr)^2\approx d^2/S .
$$

Below $B_-$ the budget falls to zero and stays there.
With $S=\$25{,}000$, a drain of \$1,000 a year puts the threshold at about \$44, and a drain of \$3,000 puts it at about \$486, so Asha at \$400 falls to zero.

Much Coasean surplus is not paid in cash.
Quiet, clean air and a street without cut-through traffic cannot be spent on compute.
When gains come in kind, $B$ stays where it is and shares stay at $\sqrt{B/S}$.
The only way to turn such gains into budget is to sell the entitlement, at the discount described in the [section on liquidity](#liquidity).

Contested entitlements move in the other direction.
A constrained holder like Odile is challenged in each period on whatever contestable holdings exceed her safe stake $V^\ast(B)$, and loses part of them each time.
The process stops only when what she holds is what she can defend.

## Limits compute does not remove

Some limits on Coasean bargaining come from private information and voluntary participation rather than from cost, and no amount of compute removes them.
We cite them rather than re-derive them.

With two parties who each know only their own valuation, no bargaining procedure can at once make honest reporting each party's best policy (incentive compatibility), leave nobody worse off for taking part (individual rationality), run without an outside subsidy (budget balance) and trade whenever trade is worthwhile (efficiency) ([Myerson and Satterthwaite (1983)](https://doi.org/10.1016/0022-0531(83)90048-0)).
With many parties and unanimity required, as for Krier's developer who needs every homeowner's agreement, and with each party's valuation private and drawn independently, the probability of reaching an efficient yes goes to zero as the number of parties $n$ grows, even in an example where every party knows that yes is efficient ([Mailath and Postlewaite (1990)](https://ideas.repec.org/a/oup/restud/v57y1990i3p351-367..html)).
When participation is voluntary, the efficient equilibrium is not robust to even very small transaction costs ([Dixit and Olson (2000)](https://ideas.repec.org/a/eee/pubeco/v76y2000i3p309-335.html)).
With two players contracting is efficient, but with more than two and voluntary participation there are situations in which every equilibrium the authors admit is inefficient ([Ellingsen and Paltseva (2016)](https://research.hhs.se/esploro/outputs/journalArticle/Confining-the-Coase-theorem-Contracting-ownership/991001480655806056)).
Binding offers of side-payments do not always produce efficiency, even with complete information and costless contracting ([Jackson and Wilkie (2005)](https://doi.org/10.1111/j.1467-937X.2005.00342.x)).
[Farrell (1987)](https://doi.org/10.1257/jep.1.2.113) discusses the role of information in the Coase theorem more generally, and [Cooter (1982)](https://doi.org/10.1086/467690) is summarized in secondary sources as arguing that lower communication costs can make agreement harder by easing strategic behaviour.

Krier's bargaining club runs into the Mailath and Postlewaite result.
The club's single offer is computed from the members' reported minimums.
If no member gives up the veto, the common price must be at least the largest reported minimum.
The member with the largest report then sets everyone's price and gains by overstating, trading a better price against a higher risk of killing the deal, so truthful reporting is not that member's best strategy.
If the club clears at a price below the largest report, either the deal fails or some members are overridden and the scheme is no longer voluntary.
If the price is fixed without regard to the reports, honesty costs a member nothing, but the price ignores what members know, and deals worth doing fail whenever it falls below one member's minimum.
The Mailath and Postlewaite result says that this trade-off cannot be designed away and that it worsens as the club grows.

There are also limits from computation itself.
Finding the best partition of $n$ principals into coalitions is NP-complete in $n$ ([Sandholm, Larson, Andersson, Shehory and Tohmé (1999)](https://doi.org/10.1016/S0004-3702(99)00036-3)).
Choosing the winning bids in a combinatorial auction, one in which bidders bid on bundles of items, is NP-complete in the size of the auction, and no polynomial-time algorithm can guarantee a result within a factor $n^{1-\epsilon}$ of the best for any $\epsilon>0$, where $n$ measures that size, unless NP = ZPP, which complexity theorists think very unlikely ([Sandholm (2002)](https://doi.org/10.1016/S0004-3702(01)00159-X)).
The standard procedure for making honest reporting each party's best strategy, the Vickrey–Clarke–Groves mechanism, charges each party the cost its presence imposes on the others and needs the exactly optimal allocation; replacing that allocation with essentially any reasonable approximation destroys the honesty property ([Nisan and Ronen (2007)](https://arxiv.org/abs/1110.0025)).
At scale, then, the mechanism is approximate, and when the honest mechanism cannot be computed in reasonable time the outcome depends on which party can do more of the computation ([Conitzer and Sandholm (2004)](https://dl.acm.org/doi/10.1145/988772.988824)).
The side that can compute more can steer an approximate mechanism.

## Remedies

| Remedy | Effect in the model | Cost |
|---|---|---|
| Compute voucher $\underline B$ (Krier) | raises the floor on shares to about $\sqrt{\underline B/S_i}$ | priced in stakes ($rS_i/4$ for parity), not in compute; raises dissipation, one point for each point of share at $r=1$ |
| Credit or third-party funding | removes the budget limit | maximum dissipation, $r/2$ of every stake; funders take a cut |
| Lower decisiveness $r$: fixed protocols, standard forms, arbitration rules that do not reward cleverness | flattens shares and cuts dissipation together (last row of the population table) | gives up bespoke terms, which are the point of hyper-granular contracting; no voluntary protocol makes honesty the best strategy while also being efficient and needing no subsidy |
| Make matters saturate: fixed-depth protocols, standard forms that bound a contract's complexity, deciders that treat small gaps as ties (Budish, Cramton and Shim's batch auction is the model) | lowers $\phi$; a household gets half of what saturates and a larger share of the rest | gives up bespoke terms; a firm facing a poorly funded household prefers the matter not to saturate, so the protocol has to be imposed and cannot be left to the stronger side |
| Coalitions | cancel the repeat player's $N^{-1/2}$ advantage | only for common stakes; each coalition's internal split is another matter |
| Caps on bargaining compute | would cut dissipation and keep shares even | compute spent in private cannot be observed, so enforcing a cap means inspecting every agent; in an all-pay auction, a different contest in which the highest spender wins outright and everyone pays what they spent, a rigid cap can even raise total spending ([Che and Gale (1998)](https://www.jstor.org/stable/116854)) |
| Take matters off the table (inalienable rights, bright-line rules) | lowers $S_i$ and $\kappa$; for a constrained principal a smaller $S_i$ raises its share of what remains | forgoes surplus on the excluded matters |
| Keep a challenge fee $f$; loser pays | raises the safe stake $V^\ast$ for everyone | it is a transaction cost, kept on purpose |

The inalienability row is the third of the three ways to protect an entitlement in Calabresi and Melamed (1972), "Property Rules, Liability Rules, and Inalienability", *Harvard Law Review* 85(6): 1089–1128: a property rule requires the holder's consent, a liability rule lets others take the entitlement on paying a value set by the state, and an inalienable entitlement may not be sold.
Here inalienability is justified from inside a bargaining model, by its effect on the shares of constrained principals and on the safe stake.
Mateo Petel's critique of Krier, [Price what you can, protect what you must](https://mateopetel.substack.com/p/price-what-you-can-protect-what-you), argues that pricing fails for dignity, privacy and system-wide harms and that the things that must not be negotiated should be fixed in the constitution.
Our section on contestable entitlements and the inalienability row reach a neighbouring conclusion by a different route.
We found no published critique of Krier that models unequal compute as a contest.

Coalitions aside, which Krier proposes himself, the remedies that work in the model are the blunt instruments his essay hopes agents will make unnecessary: standard forms and fixed-depth protocols in place of bespoke terms, bright-line rules in place of prices, and a cost of going to court that is kept on purpose.
[Glaeser and Shleifer (2003)](https://doi.org/10.1257/002205103765762725) argue along similar lines that private litigation can be subverted by the strong, more so as enterprises grow, and that the regulatory state arose in response.

The parties cannot simply agree to stop out-computing each other.
Compute spent in private cannot be observed, so the agreement could not be verified, and negotiating the agreement is itself a matter with a stake.

## Verdict

The first table puts the three worlds side by side, with Asha's figures from the [section on the three worlds](#three-worlds) at $r=1$.

| | saturating world | mixed world | non-saturating world |
|---|---|---|---|
| dollars spent claiming a matter | $\min(rV/2,\;2p\bar q)$, falling with $p$ once the cap binds | as in the non-saturating world for the fraction $\phi$, negligible for the rest | $rV/2$ between unconstrained sides, whatever $p$ |
| what sets Asha's share | the merits and outside options, not compute | $\phi$ and her budget relative to $\phi S$ | her budget relative to $S$ |
| Asha's take | half of everything once the cap is at or below her budget | about \$11,400 with $\phi$ at a fifth, which requires that the firms do not set depth | about \$3,200 |
| where it holds, if the stronger side sets depth at no cost | an equilibrium for households with budgets of at least 8.6% of their largest single stake with a firm ($r=1$) | only where depth is fixed by the matter or by a protocol | an equilibrium for households with budgets below 8.6% of their stakes with firms ($r=1$) |

Between the two budget thresholds in the last row, either world can be the equilibrium, depending on where the household starts.
We do not say which world holds for most real stakes, because that depends on two things nobody has measured: how decisiveness changes with compute in each type of matter, and who sets the depth of a matter.
The second table and the findings after it are derived for non-saturating matters; in the mixed world they apply to the fraction $\phi$ of stakes, with $S_i$ replaced by $\phi S_i$.

The second table sorts the results by the three questions the constitution left open.
Rows are decisiveness and whether gains are liquid; columns are whether entitlements are secure, meaning every contestable stake $\kappa E$ lies below the safe stake $V^\ast$.

| | entitlements secure ($\kappa E\le V^\ast$) | entitlements contestable, fee low |
|---|---|---|
| low decisiveness ($r\lesssim 0.25$) | roughly Krier's world: shares between about a quarter and a half, dissipation at most $r/2$ | not modelled, since the entitlement contest is solved for $r=1$ only; we expect small losses, because at low $r$ a challenger gains little by outspending a holder |
| decisiveness near 1, cash gains, no drain | unequal at first, curing itself within a few periods; converges to equal shares with up to half of every stake dissipated | peace among the strong (conjectured), transfers from the constrained |
| decisiveness near 1, in-kind gains or a drain | a persistent hierarchy of strength; everyone gains something, and the constrained get $\sqrt{B/S}$ of each surplus, falling as matters multiply | holdings shrink towards what each holder can defend; constrained principals can be worse off than with no bargaining |

The right-hand column was derived for a non-saturating contest between challenger and defender; what would be different if a challenge were a saturating matter is not modelled.

Under Krier's own constitution with perfectly secure entitlements, bargaining over new surplus makes nobody worse off in absolute terms.
The suspicion that this world is simply bad is not supported in that column.

In non-saturating matters, Krier's cost claim fails in the part of bargaining that decides distribution.
Spending on negotiation there is set by stakes and decisiveness, not by the price of compute, so neither transaction costs in the claiming part of a bargain nor the cost of a voucher that gives parity tends to zero.
In saturating matters his cost claim holds, and so does his expectation that compute stops deciding the split.

Shares in non-saturating matters are set by budget relative to non-saturating stakes, and the Coasean programme raises the stakes each principal has at issue while nothing in it raises budgets in step, apart from the voucher and, where winnings are cash and can be reinvested, the winnings themselves.
Asha's share falls as $S_i^{-1/2}$ as her non-saturating matters multiply.

Even shares and low dissipation trade off against each other, one for one at $r=1$ against unconstrained counterparties, so a remedy that equalizes shares by funding the weak side raises waste as it does so.

Whether the exercise helps or harms constrained principals depends on whether entitlements stay secure when challenging them becomes cheap.
The essay wants baselines to be contestable and does not ask who can afford the contest.

Three kinds of evidence would change these conclusions.
If $r(q)$, measured matter type by matter type, falls towards zero as both sides' compute $q$ grows over the range agents will use, those types of matter saturate and Krier's cost claim holds for them; how much of the rest of these conclusions survives then depends on $\phi$, the fraction of stakes in the types of matter whose $r(q)$ does not fall.
If entitlements can be defined completely enough that $\kappa$ is close to zero, the right-hand column of the second table empties.
If a technology for verifying compute use made caps enforceable, dissipation could be cut without giving up even shares.

Three measurements would settle much of this.
The first is $r$ itself, estimated from agent-versus-agent negotiations with controlled compute ratios, and its trend $r(q)$ as the compute on both sides grows, for each type of matter; weighted by the stakes in each type, this also gives $\phi$.
The second is the fraction of realized surplus spent on agent compute as agent prices fall.
The third is the rate of challenges to existing entitlements, broken down by the wealth of the holder challenged.

Other work on agent economies raises related concerns without modelling this contest: [Tomašev et al. (2025)](https://arxiv.org/abs/2509.10147), whom Krier cites, flag systemic risk and inequality in virtual agent economies, and [Shahidi, Rusak, Manning, Fradkin and Horton (2025)](https://www.nber.org/papers/w34468) and [Hadfield and Koh (2025)](https://arxiv.org/abs/2509.01063) analyze markets in which AI agents transact.
[Baumol (1990)](https://doi.org/10.1086/261712) and [Murphy, Shleifer and Vishny (1991)](https://academic.oup.com/qje/article-abstract/106/2/503/1905462) showed that talent flows to rent-seeking when the rules reward it; in an agent economy with high decisiveness, compute would be drawn the same way.

## Appendix {#appendix}

### Strength for general decisiveness {#app-strength}

Principal $i$ maximizes $\sum_j\bigl(V_{ij}\sigma_{ij}-x_{ij}\bigr)$ subject to $\sum_jx_{ij}\le B_i$, with $\sigma_{ij}=x_{ij}^r/(x_{ij}^r+x_{ji}^r)$.
For $0<r\le1$, $\sigma_{ij}$ is concave in $x_{ij}$, so each principal's problem is concave and the Karush–Kuhn–Tucker conditions are sufficient.
Write $\mu_i\ge0$ for the multiplier on the budget and $\lambda_i=1+\mu_i\ge1$.
The condition for an interior spend is

$$
V_{ij}\,\frac{\partial\sigma_{ij}}{\partial x_{ij}} = V_{ij}\,\frac{r\,x_{ij}^{r-1}x_{ji}^r}{(x_{ij}^r+x_{ji}^r)^2}=\lambda_i .
$$

Since $\partial\sigma_{ij}/\partial x_{ij}=r\sigma_{ij}\sigma_{ji}/x_{ij}$, this is $rV_{ij}\sigma_{ij}\sigma_{ji}/x_{ij}=\lambda_i$.
The same condition for $j$ in the same matter is $rV_{ij}\sigma_{ij}\sigma_{ji}/x_{ji}=\lambda_j$, because $V_{ji}=V_{ij}$ and the product $\sigma_{ij}\sigma_{ji}$ is shared.
Dividing the two gives $x_{ji}/x_{ij}=\lambda_i/\lambda_j=s_j/s_i$, so $x_{ij}\propto s_i$ within each matter and

$$
\sigma_{ij}=\frac{s_i^r}{s_i^r+s_j^r},\qquad x_{ij}=\frac{rV_{ij}\sigma_{ij}\sigma_{ji}}{\lambda_i}=rV_{ij}\sigma_{ij}\sigma_{ji}s_i .
$$

Complementary slackness gives $\mu_i=0$, so $s_i=1$, when $r\sum_jV_{ij}\sigma_{ij}\sigma_{ji}\le B_i$ evaluated at $s_i=1$; otherwise the budget binds and $s_i<1$ solves $\sum_jx_{ij}=B_i$.
For $r=1$ and $\mu_i>0$ this is Lemma 1 of Díaz-García, Bullo and Marden (2024) with $\lambda_i$ in place of $1/s_i$.

The symmetric single-matter result is the special case $s_i=s_j=1$: $\sigma=1/2$ and $x^\ast=rV/4$.

### A constrained principal against unconstrained counterparties {#app-special}

Set $s_j=1$ for all $j$, and write $s=s_i$.
Then $\sigma_{ij}=\sigma=s^r/(1+s^r)$ in every matter, and $x_{ij}=rV_{ij}\sigma(1-\sigma)s$.
Summing over matters, the budget condition is

$$
rS_i\,s\,\sigma(1-\sigma)=\frac{rS_i\,s^{1+r}}{(1+s^r)^2}=B_i ,
$$

which has a solution $s<1$ when $B_i<rS_i/4$, the value of the left side at $s=1$.
Because $\sigma$ is the same in every matter, $x_{ij}\propto V_{ij}$: the budget is split in proportion to stakes.

For $r=1$, $s=\sigma/(1-\sigma)$, so $s\sigma(1-\sigma)=\sigma^2$ and the budget condition reads $S_i\sigma^2=B_i$, giving $\sigma=\sqrt{B_i/S_i}$.
The principal takes $S_i\sigma=\sqrt{B_iS_i}$.
Each counterparty spends $x_{ji}=V_{ij}\sigma(1-\sigma)$, which sums to $S_i\sigma(1-\sigma)=\sqrt{B_iS_i}-B_i$.
The counterparties' net gain is $S_i(1-\sigma)-S_i\sigma(1-\sigma)=S_i(1-\sigma)^2=\bigl(\sqrt{S_i}-\sqrt{B_i}\bigr)^2$.

The marginal value of budget with counterparties responding is $\mathrm d\sqrt{B_iS_i}/\mathrm dB_i=\tfrac12\sqrt{S_i/B_i}$.
Holding their spending fixed it is $\lambda_i=1/s=(1-\sigma)/\sigma=\sqrt{S_i/B_i}-1$.

With a showing-up cost $c_0$ per matter and equal stakes $V$, attending $k$ matters leaves $B-kc_0$ to contest total stakes $kV$, so the take is $\sqrt{(B-kc_0)kV}$.
This is maximized at $k=B/(2c_0)$, where the take is $(B/2)\sqrt{V/c_0}$.
With heavy-tailed stakes the principal attends the $k$ largest matters, whose total stake is proportional to $k^{1-1/\alpha}$; maximizing $(B-kc_0)k^{1-1/\alpha}$ gives $kc_0/B=(\alpha-1)/(2\alpha-1)$.

### Dissipation identity {#app-dissipation}

From the strength formula, dissipation in a matter is

$$
x_{ij}+x_{ji}=rV\sigma_{ij}\sigma_{ji}(s_i+s_j).
$$

At $r=1$, $\sigma_{ij}\sigma_{ji}=s_is_j/(s_i+s_j)^2$, so dissipation is $Vs_is_j/(s_i+s_j)$.
With $s_j=1$ this is $Vs_i/(1+s_i)=V\sigma_{ij}$.
At $s_i=s_j$ it is $Vs/2$, which is $V/2$ for two unconstrained principals.

### Repeat player {#app-repeat}

A firm faces $N$ households in identical matters of stake $V$, each household spending $b$, and the firm's single spend $X$ counts in every matter.
The firm maximizes $NV\,X/(X+b)-X$.
The first-order condition $NVb/(X+b)^2=1$ gives $X=\sqrt{NVb}-b$, and each household's share is $b/(X+b)=b/\sqrt{NVb}=\sqrt{b/(NV)}$.
If the households pool their budgets into one argument worth $Nb$ that counts in every matter, the same calculation with $Nb$ in place of $b$ gives a share of $\sqrt{Nb/(NV)}=\sqrt{b/V}$.

### Contested entitlements and the safe stake {#app-entitlements}

With $\sigma_D=\theta x_D/(\theta x_D+x_A)$ and both sides unconstrained, the challenger maximizes $V x_A/(\theta x_D+x_A)-x_A$ and the defender maximizes $V\theta x_D/(\theta x_D+x_A)-x_D$.
The first-order conditions are $V\theta x_D/T^2=1$ and $V\theta x_A/T^2=1$ with $T=\theta x_D+x_A$, so $x_D=x_A=x$ and $V\theta x/\bigl((1+\theta)x\bigr)^2=1$, giving $x=\theta V/(1+\theta)^2$.
The defender keeps $\theta/(1+\theta)$, and the challenger nets $V/(1+\theta)-\theta V/(1+\theta)^2=V/(1+\theta)^2$ before the fee.

Against a defender who spends $b$, the challenger's best response is $x_A=\sqrt{\theta bV}-\theta b$ when $V>\theta b$ (and zero otherwise).
Its net is $V-2\sqrt{\theta bV}+\theta b=\bigl(\sqrt V-\sqrt{\theta b}\bigr)^2$ before the fee, and the defender keeps $V\cdot\theta b/\sqrt{\theta bV}=\sqrt{\theta bV}$.

A challenge is unprofitable when $\bigl(\sqrt V-\sqrt{\theta b}\bigr)^2\le f$, that is when $\sqrt V\le\sqrt{\theta b}+\sqrt f$.
An unconstrained defender spends $\theta V/(1+\theta)^2$, which at the boundary $V=(1+\theta)^2f$ equals $\theta f$; a defender with $B<\theta f$ spends all of $B$.
Putting $b=\min(B,\theta f)$ gives the safe stake $V^\ast(B)=\bigl(\sqrt{\theta\min(B,\theta f)}+\sqrt f\bigr)^2$.

With $h$ challengers each contesting a stake $V$ against a defender who splits a budget $B$ evenly, each challenger faces $b=B/h$ and nets $\bigl(\sqrt V-\sqrt{\theta B/h}\bigr)^2-f$, which rises with $h$.

For two unconstrained principals with one matter of new surplus $V^+$ and mutual challenges on $V^-$ each, with $f=0$: the new matter nets $V^+/2$ to the pair, each challenge dissipates $2\theta V^-/(1+\theta)^2$ and otherwise transfers, so the pair's net gain is $V^+/2-4\theta V^-/(1+\theta)^2$, negative when $V^-/V^+>(1+\theta)^2/(8\theta)$.

### Dynamics {#app-dynamics}

With $r=1$, cash winnings and no drain, a constrained principal's next budget is its take, $B_{t+1}=\sqrt{B_tS}$, so $\log B_{t+1}=\tfrac12(\log B_t+\log S)$ and $B_t=S^{1-2^{-t}}B_0^{2^{-t}}$.
The recursion applies while $B_t<S/4$; after that the principal is unconstrained.

With a drain $d$ per period, $B_{t+1}=\sqrt{B_tS}-d$.
Writing $u=\sqrt{B}$, fixed points satisfy $u^2-u\sqrt S+d=0$, so $u=\bigl(\sqrt S\pm\sqrt{S-4d}\bigr)/2$.
The smaller root $B_-=\bigl((\sqrt S-\sqrt{S-4d})/2\bigr)^2$ is unstable: below it $\sqrt{B_tS}-d<B_t$ and the budget falls to zero.
For small $d/S$, $\sqrt{S-4d}\approx\sqrt S-2d/\sqrt S$, so $B_-\approx d^2/S$.

### Saturation and the three worlds {#app-saturation}

*Capped pair.*
In one matter with stake $V$ between two unconstrained sides, depth $\bar q$ caps each side's spend at $c=p\bar q$.
At $x=y=c$ each side's marginal return is $rV/(4c)$, which is at least 1 if and only if $c\le rV/4$.
So when $c\le rV/4$ both sides spend $c$, and otherwise each spends its uncapped $rV/4$; total spend is $\min(rV/2,\;2p\bar q)$.

*Asha against a cap.*
With depth proportional to stake, the firms' total spend against Asha is capped at $c$ and spread in proportion to stakes, as is her budget, so at $r=1$ her share in every matter is her total spend over the sum of the two totals.
Uncapped, the firms spend $\sqrt{BS}-B$ against her, so for $B<c<\sqrt{BS}-B$ the cap binds them, she spends all of $B$, and her share is $B/(B+c)$.
For $c\le B$ both sides spend $c$ and the split is even.

*Mixed world.*
The saturating part, $(1-\phi)S$, is split evenly at negligible cost, and Asha's whole budget goes to the non-saturating part.
The [special case](#app-special) with $\phi S$ in place of $S_i$ gives, for $B<\phi S/4$, a share $\sqrt{B/(\phi S)}$ there and a take of $\sqrt{B\phi S}$, so her overall share is $(1-\phi)/2+\sqrt{\phi B/S}$.
Her spend $B$ and the firms' $\sqrt{B\phi S}-B$ sum to $\sqrt{B\phi S}$, a fraction $\sqrt{\phi B/S}$ of $S$.

*The firm's choice.*
With household strength $s$ and $r=1$ the firm's share is $1/(1+s)$ and its spend $Vs/(1+s)^2$, so it nets $V/(1+s)^2$.
This exceeds $V/2$ if and only if $s<\sqrt2-1$, that is, if the household's share $s/(1+s)$ is below $1-1/\sqrt2$.
Since the household's share is $\sqrt{B/S}$ in its non-saturating stakes $S$, this is $B/S<(1-1/\sqrt2)^2$.

*Bounded tail.*
The best of $q$ uniform draws is about $1-E/q$ with $E$ exponential, so near equal compute the expected gap between the two bests moves by about $1/q$ per unit change in $\ln q_i$.
With a logistic error of scale $\varsigma$, the chance of prevailing moves by $1/(4\varsigma)$ per unit of gap near a tie.
At equal compute the log-odds of prevailing change four times as fast as the chance itself, so $r(q)=4\,\partial P/\partial\ln q_i\approx1/(\varsigma q)$, where $P$ is the chance of prevailing.
The first-order condition for each side's spend, $Vr(q)/(4pq)=1$, then gives spend $pq=\sqrt{Vp/(4\varsigma)}$, which falls as $\sqrt p$.

*Exponential tail.*
The best of $q$ exponential draws is $\ln q$ plus a Gumbel-distributed variable, so the gap between the two bests is $\ln(q_i/q_j)$ plus noise that does not depend on $q$, and $r$ is constant.

*Gaussian tail.*
The best of $q$ Gaussian draws is about $\sqrt{2\ln q}$ plus a Gumbel-distributed variable divided by $\sqrt{2\ln q}$, so $r(q)\approx1/(\varsigma\sqrt{2\ln q})$ for large $q$.

### What the script checks {#app-script}

Every closed form and number above was checked against direct numerical computation in `check_budget_contests.py`, which sits beside this draft.
The script computes the network equilibrium of bilateral contests with budgets on random small networks for $r\in\{0.25,0.5,1\}$.
It checks by constrained optimization that no principal can gain by deviating, and confirms that the iteration reaches the same strengths from 20 random starting points.
It reproduces Asha's table, the share as the number of matters grows, and the population experiment with 3,000 households under each voucher and decisiveness scenario.
It compares the challenger's numerically optimal profit with the closed forms for contested entitlements, and tabulates the safe stake, the profit per challenger as challengers pile on, and the break-even ratio between equals.
It iterates the budget dynamics with and without a drain, finds the best number of matters to attend with a showing-up cost for equal and heavy-tailed stakes, and solves the repeat player's problem numerically.
For all of these the closed forms agree with the numerical equilibria to about $10^{-12}$.
Section H of the script checks the results on saturation and the three worlds.
Its closed forms for spends and shares agree with the computed equilibria to the figures shown in the tables.
The formulas for $r(q)$ in the tail derivations are approximations for large $q$; for $q$ of 100 or more they are within about 2% of the computed values.
It computes the capped pair's total spend against $\min(rV/2,\;2p\bar q)$ (H1) and Asha's spends and share as the cap $c$ falls (H2).
It computes the mixed-world shares for each $\phi$ in the table, and the direct equilibrium with only her lease non-saturating (H3).
It computes $r(q)$ for the four kinds of tail and each side's equilibrium spend as the price of a draw falls (H4).
It finds the firm's thresholds for $r\in\{0.25,0.5,1\}$ and lets firms revise their choices in turn over Asha's matters (H5).
It compares the fraction of total stake in the largest 1% of matters under power-law stakes with a simulation (H6).
To run it:

```bash
uv run --no-project --with numpy --with scipy python _notes/personal_budget/check_budget_contests.py
```
