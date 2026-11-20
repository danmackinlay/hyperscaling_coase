---
title: The compute budget of a Coasean principal
date: '2026-11-19'
description: Starting from Séb Krier's proposal that AI agents make Coasean bargaining cheap, I name the world the proposal presumes and use toy models to find which measurable quantities decide whether we live in it.
categories:
- economics
- game theory
- AI
- institutions
---

[Séb Krier (2025)](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale) proposes that personal AI agents could make private bargaining cheap enough to replace much of what regulation now does.
The starting point is [Coase (1960)](https://doi.org/10.1086/466560): if bargaining cost nothing, a polluter and a neighbour would trade the right to pollute until no further trade could make both better off, whoever held the right at the start.
What stops this in practice is transaction costs: finding the other party, agreeing terms, enforcing the agreement.
Krier argues that agents acting for each of us drive those costs towards zero, and he summarizes the consequence in one line:

> "In other words, AGI could enable hyper-granular contracting."

This article asks what life looks like for one principal in that world.
By *principal* I mean any party that holds entitlements and contracts over them: a person, a firm, a household.
Each principal has a budget for compute, which it can enlarge by spending its wealth.
It is party to many bargains at once and must decide how to divide its compute among them.
Every other principal is selfish and is represented by an agent that serves it perfectly and computes up to its own principal's limit, which differs from ours.
Gains from one round of bargaining can be spent on compute for the next round, or on ordinary productive uses.

The question I care most about is the shape of the principal's *production function*, by which I mean the map from what a principal brings to a period (its wealth, its compute, the bargains it is party to) to the resources it ends the period with.
Krier's essay does not state such a function, but two of his sentences suggest one.
I call the world in which it holds the *sufficiency world*: a fixed amount of compute per bargain is sufficient, so that more of a principal's own compute adds nothing and what the other side spends does not matter.
What we know about compute in games against an opponent suggests a different world, which I call the *contest world*: a principal's share of what a bargain creates depends on its compute relative to its opponent's.
Krier may not accept every property of the sufficiency world; I name it so that we can ask which of its properties his conclusions need and which of them hold.
I take the proposal seriously, and build toy models to find which measurable quantities decide which world we are in; the section "Cruxes" lists them.

## Summary

The models take as given Krier's institutional premises: perfectly loyal agents, perfect and free enforcement of contracts, and a single market price for compute.
Under those premises they give the following.

1. Finding deals becomes almost free as compute gets cheaper, as Krier says.
   Dividing the gain from a deal does not get cheaper.
   When two agents are evenly matched, they spend a fixed fraction of every gain arguing over its division, and that fraction does not fall as compute gets cheaper; they simply buy more compute with the same dollars.
   In the model the fraction is $r/2$, where $r$ measures how far an advantage in compute shifts the outcome and is assumed no larger than 2; at $r=1$ it is half the gain.
2. Among principals who can afford to match their opponents' spending, extra wealth buys no advantage, as Krier's remark about the billionaire's phone says.
   What it takes to afford that is not a small and shrinking amount of compute but a fixed fraction of what the principal has at stake, in dollars: a quarter at $r=1$, when equal compute would split each bargain evenly.
3. A principal that cannot afford to match spends all its savings on compute, because each extra dollar of compute is worth more to it than a dollar invested elsewhere.
   At $r=1$, against opponents who can afford to match, it gets a share of every bargain equal to the square root of its savings relative to its stakes.
   Once subsistence needs are added, principals who start with too little lose their savings altogether and stay there.
4. Items 2 and 3 of this summary are about unequal shares, and they hold only where principals cannot borrow against what they stand to gain.
   Under the premises above, nothing obvious stops a funder advancing compute against a share of a principal's gain, as litigation funders do today.
   With such funding every bargain is fought at parity, every principal gets the share it would get at equal compute, and the compute wasted reaches its maximum.
   The results on waste are robust; the results on who gets what are conditional on there being no such funding.
5. On a bargain between a principal that cannot afford to match and one that can, the compute wasted equals the weaker side's share.
   So any remedy for unequal shares, a subsidy or a loan, works by raising waste.
6. A large party that reuses its bargaining work across many similar bargains, as a landlord does across its leases, wins most of each one without any advantage in wealth.
7. Compute stops mattering when a bargain, meaning the contract terms together with the circumstances they cover, is simple enough for both sides to work out the best outcome completely.
   The party that drafts the contract chooses how much detail the contract adds; the circumstances set a floor it cannot lower.

Measured against the sufficiency world, principals in the contest world who can match their opponents keep half the net gain from bargaining that the sufficiency world gives, those who cannot keep less, and the economy as a whole loses the waste.
No principal is made worse off by any single bargain it takes part in, because it can always refuse and keep what it had; the exception is a threat manufactured in order to be bought off.
The remedies the models point to are rules about how bargaining is conducted, which go beyond enforcing contracts and entitlements.

The closed-form results below are theorems of the toy models, and each was checked against a direct numerical solution in the script `_notes/personal_budget_2/check_closed_forms.py`.
The table of wealth over time is simulation output for one set of parameters.
Statements about the market structure of agent provision, and about the present day, are conjecture, and are labelled as such where they appear.
A table of notation is at the end of the article.

## A small cast

Three principals appear throughout.
*Alice* is a tenant and an employee with a little liquid savings, $160 in the worked examples.
*Bob* is her neighbour, of similar means.
*The landlord* is a company that rents homes to many tenants, Alice among them.
Their dollar figures are chosen to make the arithmetic easy to follow and are not estimates of anything.

## The institutions we take as given

The models give bargaining between agents every institutional support I could formalize, so that whatever they find is attributable to bargaining itself and not to some failure of enforcement or alignment.
I call the rules the *constitution*.

C1 (entitlements)
: Every principal holds well-defined rights.
    If a bargain fails, each side keeps its entitlement.
    Courts enforce every contract, perfectly and at no cost.

C2 (voluntariness)
: Nobody is bound without consent.
    Silence counts as refusal.

C3 (alignment)
: Every agent serves its principal perfectly.

C4 (open compute market)
: Anyone may buy compute at the same price $p$ per unit.

C5 (criminal law)
: No violence, theft or fraud.

C6 (freedom of bargaining technique)
: There is no limit on how much compute a party brings to a bargain or on how detailed a contract it proposes.

Most of the constitution is Krier's own, or near enough: he asks the state to "define and enforce basic property rights, contract law, criminal justice, and constitutional rights", and he hopes for agents loyal to their principals.
C3 assumes more than he claims, since he writes that alignment is never fully solved.
C6 is not something he states, but nothing in his essay restricts it; only the section on how complex a matter is relaxes it.
Principals are selfish and risk-neutral.

## The sufficiency world

Two sentences in Krier's essay suggest how a principal's income might respond to compute:

> "What costs $10,000 in legal fees today might cost pennies to compute tomorrow. Consider how a billionaire's phone today is no more powerful or effective than yours."

> "This is unlikely to be a huge growing cost over time, as agent tech commoditizes, these costs approach zero asymptotically."

The second sentence needs its context.
It comes directly after Krier's proposal that "To prevent cost barriers for low-income users, governments or philanthropies could provide baseline agent services (similar to public defenders) and guarantees."
So "these costs" are the costs of that subsidy, and his claim is that a subsidy which removes cost barriers gets cheaper over time.

The production function below is my reading of the two sentences, not something Krier writes, and it defines the sufficiency world.
Call one bilateral bargain, between principal $i$ and an opponent $j$, a *matter* $m$.
Its *surplus* $S_m$ is the value, in dollars, that an agreement creates over both sides keeping their entitlements, and principal $i$'s *stakes* $E_i=\sum_{m\ni i}S_m$ are the total surplus over all the matters it is party to, $M_i$ of them.
Let $c_{im}$ be the units of compute $i$ spends on matter $m$, bought at price $p$ per unit, and let $R$ be the gross return on a dollar put to ordinary productive use (capital, tools, training) instead.
Units of compute are abstract here; in the empirical work cited below a unit is a fixed amount of processing.
In the sufficiency world, the surplus of a matter is realized only if each side spends at least a fixed amount $\bar c$ of compute on it, which I call the *satiation level*; above that, more compute changes nothing.
Each side then receives its *merit share* $\theta_m$ of the surplus, the share a neutral arbiter would give it, which is $\tfrac12$ unless stated.
A principal ends the period with resources

$$Y_i^{\mathrm{suf}} \;=\; R\Big(w_i-p\sum_m c_{im}\Big) \;+\; \sum_m \theta_m S_m\,\mathbf 1\big[c_{im}\ge\bar c\big],$$

where $w_i$ is its liquid wealth at the start of the period and $\mathbf 1[\cdot]$ is one if the condition holds and zero otherwise.
At the optimum it spends $\bar c$ on each matter and ends with $Rw_i+\theta E_i-Rp\bar cM_i$, and since $\bar c$ is set by technology, the last term goes to zero as compute gets cheap.
The sufficiency world has four properties.

(i) Satiation
: Above $\bar c$, more of $i$'s own compute adds nothing to its income.

(ii) No rivalry
: An opponent's compute $c_{jm}$ does not enter $i$'s income.

(iii) Compute only creates surplus
: Compute brings surplus into being; it never moves surplus from one party to the other.

(iv) Cheap floor
: The subsidy that lifts everyone to the satiation level costs $p\bar c$ per matter and vanishes as $p\to0$.

Krier does grant that outcomes depend on who holds an entitlement at the start, and that wealth affects willingness to pay ("A poor farmer might sell pollution rights cheaply to a rich factory not because it's efficient, but because they need cash now").
That is a different channel from the one studied here.
Throughout, entitlements and valuations are held fixed, and the question is only how the surplus of each matter is divided and what the division costs.

Each of the following sections asks whether one property holds in the contest world.
The section on a single matter asks whether compute only creates surplus, and whether its cost vanishes (iii).
The section on fixed budgets asks whether an opponent's compute matters (ii).
The section on buying compute out of wealth asks whether income stops responding to compute above some level, and whether the floor is cheap (i, iv), and assembles the production function the models imply.
The section on wealth over time asks what part the initial endowment plays.
The section on repeat players concerns scale, which plays no part in the sufficiency world.
The section on how complex a matter is asks when satiation does hold.
The section on manufactured threats describes the one case where bargaining leaves a principal worse off.

## Compute in games against an opponent

Krier's billionaire's phone, read as a claim about bargaining, describes a task with a ceiling, where past some point extra capacity sits idle.
Games against an opponent who is also computing behave differently, and there is a standard model for how.

A *contest success function* is a rule that maps the efforts of two competing sides to their shares of a prize, or their probabilities of winning it.
The one used here is

$$s_{im}=\frac{\theta_m c_{im}^{\,r}}{\theta_m c_{im}^{\,r}+(1-\theta_m)\,c_{jm}^{\,r}} ,$$

which gives $i$ its merit share $\theta_m$ when both sides spend the same and tilts its share $s_{im}$ towards whoever spends more.
The exponent $r\ge0$ is the *decisiveness* of compute: at $r=0$ compute makes no difference, and the larger $r$, the more a given ratio of compute shifts the outcome.
This is the ratio form of the Tullock contest, a standard model of competition for a prize in which each side's share rises with its fraction of the total effort.
[Skaperdas (1996)](https://doi.org/10.1007/BF01213906) lists a small set of axioms a contest success function might satisfy, among them that each side's share rises in its own effort and falls in the other's, and that the comparison between two contestants does not depend on a third.
He shows that the ratio form is the only one satisfying them in which the outcome depends only on the ratio of efforts, so that doubling both sides' effort changes nothing.
[Hirshleifer and Osborne (2001)](https://doi.org/10.1023/A:1017520505573) use this form for litigation, with $\theta$ standing for the true degree of fault: at equal effort the court gets it right, and unequal effort bends the result.
Both papers take effort as given, in whatever unit it is measured, and neither says that compute is that unit.
Skaperdas also shows that if the outcome depends on the difference of efforts and not on their ratio, the function is logistic in that difference, and a given gap in spending would then buy a larger advantage as compute gets cheaper.
That the ratio form holds with compute as the measure of effort is an assumption of this article, and the evidence for it is Jones's measurement, described in the next paragraph.
One identity does most of the algebra below,

$$\frac{\partial s_{im}}{\partial c_{im}}=\frac{r\,s_{im}(1-s_{im})}{c_{im}},$$

and the share is a logistic function of $r\log(c_{im}/c_{jm})+\log\big(\theta_m/(1-\theta_m)\big)$.

The best measurement I know of how compute behaves in such a game is [Jones (2021)](https://arxiv.org/abs/2104.03113).
He trained AlphaZero agents, programs that learn a board game by playing against themselves, to play Hex across about six orders of magnitude of training compute.
He measured playing ability as an Elo rating, the chess rating system in which the difference between two players' ratings determines the probability that one beats the other.
The rating rises linearly in the logarithm of compute, about 500 Elo per tenfold increase.
Elo ratings are defined so that the probability of winning is a logistic function of the rating difference with scale 400.
A rating linear in log compute is therefore the ratio form above, with $r$ equal to the Elo gained per tenfold increase divided by 400, about $1.3$.
Jones's own round summary is that an agent with twice its opponent's compute wins about two-thirds of the time, which is $r=1$; the fitted slope gives a little over 70%.
He notes that this matches a toy model in which each player draws random numbers in proportion to its compute and the highest draw wins.
That toy is the $r=1$ contest, the same structure as the research tournament of [Fullerton and McAfee (1999)](https://doi.org/10.1086/250072).

The same paper shows where this stops.
The curve flattens at perfect play, and the compute needed to reach perfect play multiplies by about 7 for each unit increase in the side length of the board, from about $10^{11}$ units at size 3 to about $10^{16}$ at size 9.
So there are two regimes.
While neither side can solve the game, the ratio form holds; once both can, extra compute returns nothing.
Jones measures compute spent in training, not in play, though he also finds that the two trade off against each other at a stable rate.

For bargaining agents specifically, [Anthropic's Project Deal (2026)](https://www.anthropic.com/features/project-deal) ran a marketplace in which Claude agents represented 69 employees and struck 186 deals worth about $4,000 in total.
For the same item, agents running the more capable model (Opus) sold for $2.68 more and bought for $2.45 less than agents running the less capable one (Haiku), where the median item price was $12.
Averaged over deals, not matched by item, an Opus seller facing a Haiku buyer got $24.18 against $18.63 when Opus faced Opus.
The people represented by the less capable model rated their deals as just as fair as everyone else did, 4.06 against 4.05 on a seven-point scale where 4 means fair to both.
[Zhu et al. (2025)](https://arxiv.org/abs/2506.00073) find the same imbalance across LLM agents in simulated consumer negotiations.
These studies vary the model, not the compute given to a fixed model, so they show that $r>0$ for agent bargaining without measuring it.

Compute stops mattering in a game both sides can solve outright, which has the same effect on that matter as $r=0$.
The alternating-offers bargaining game with complete information has a closed-form solution ([Rubinstein 1982](https://doi.org/10.2307/1912531)), and an agent that can compute it gains nothing from more compute.
That is the world of the billionaire's phone.

Nobody has measured $r$ for agent bargaining as a function of the compute ratio, so it is the free parameter of this article.
Within the contest success function, sufficiency arises on a matter in two ways.
Either $r=0$, so compute never shifts shares; or $r>0$ but both sides can afford the compute that solves the matter outright, so compute shifts shares only below that level.
The second is a property of a matter, not of the whole economy.
The headline case below is $r=1$.
It is Jones's own round summary and the low end of the measured range, and it is the largest value for which the many-matter model here can be solved by the methods used.
The case $r>1$ is not solved here; Hirshleifer's result, discussed in the section on wealth over time, suggests it favours the richer side.

## One matter

This section asks whether compute only creates surplus, and whether what is spent on a bargain falls as compute gets cheaper.
Krier anticipates the objection and answers it with a claim about scale:

> "Skeptics might say agents don't eliminate costs entirely; they just shift them to compute overhead, data privacy setups, agent configurations etc. This is true! But it also underestimates the scale of reduction."

Read as a claim about all the compute spent on a bargain, that answer treats it as a fee for doing the bargain, which falls as the input gets cheaper.
In the contest world this holds for one part of the compute and not for the other.

### Spending does not fall with the price

Alice and Bob bargain over Bob's leaf blower: an agreement over hours and compensation is worth $100 a year to the two of them together, over and above Bob blowing leaves when he likes.
At $r=1$, each of their agents spends $25 on compute arguing over the split, and each gets $50 of the surplus, or $25 net.
Make compute a million times cheaper and each still spends $25; they just buy a million times as much of it.

**Result 1.**
Take two principals whose spending is not limited by their wealth, bargaining over one matter.
Each chooses compute to maximize its share of the surplus less the cost of compute, $s_{im}S_m-p\,c_{im}$.
Using the identity above, the first-order conditions are

$$\frac{r\,s_{im}(1-s_{im})\,S_m}{c_{im}}=p \qquad\text{and}\qquad \frac{r\,s_{im}(1-s_{im})\,S_m}{c_{jm}}=p,$$

since $j$'s share is $1-s_{im}$ and so $s(1-s)$ is the same for both.
Together they give $c_{im}=c_{jm}$, so each side gets its merit share $\theta_m$, and each spends

$$p\,c^{*}=r\,\theta_m(1-\theta_m)\,S_m .$$

I call the dollars both sides spend on dividing a surplus, as opposed to creating it, *waste*; the literature's name for it is *rent dissipation* ([Tullock 1980](https://doi.org/10.1007/978-1-4757-5055-3_2); [Posner 1975](https://doi.org/10.1086/260357)).
Here waste is the fraction $2r\theta_m(1-\theta_m)$ of the surplus, which is $r/2$ at $\theta_m=\tfrac12$.
For this to be an equilibrium each side's net payoff must be non-negative, $\theta_m\ge r\theta_m(1-\theta_m)$, which at $\theta_m=\tfrac12$ means $r\le2$.
For $r>2$ the equilibrium is in mixed strategies, in which each side randomizes its spending, and the whole surplus is wasted in expectation ([Baye, Kovenock and de Vries 1994](https://doi.org/10.1007/BF01053238)).

The price $p$ does not appear in the dollars spent; it only sets how many units those dollars buy, $c^*\propto 1/p$.
The result is Tullock's and Posner's; what is particular to the agent setting is reading $p$ as the price of compute and noticing that waste does not depend on it.
Both sides end at their merit shares, so the division is not distorted; the cost is the waste of reaching it.

### Which transaction costs vanish

Compute does two jobs in a bargain.
Some of it finds the agreement: works out what each side wants, which terms create value, how to write them down.
The rest decides who gets what.
Negotiation scholars call these creating and claiming value (Lax and Sebenius 1986, *The Manager as Negotiator*, Free Press).
Krier's examples are mostly about the first job.

**Result 2.**
Let total discovery compute $A=A_i+A_j$ create surplus $S(A)$, increasing and concave in $A$, and let claiming compute $b_i$, $b_j$ divide it through the contest success function.
Principal $i$'s payoff is $s(b_i,b_j)\,S(A)-p\,(A_i+b_i)$.
Each side pays the whole cost of its own discovery and receives half of what it creates, so in the symmetric equilibrium discovery stops where $S'(A^*)=2p$.
A social planner, a hypothetical decision-maker choosing spending to maximize the two sides' combined payoff, would continue to $S'(A^\circ)=p$.
Claiming spending is $p\,b^*=r\,S(A^*)/4$ each, as in Result 1.
With $S(A)=\bar S(1-e^{-A/A_0})$, where $\bar S$ is the most the agreement could ever be worth and $A_0$ sets how fast discovery approaches it, $A^*=A_0\ln(\bar S/2pA_0)$.
Discovery spending $pA^*$ goes to zero as $p\to0$ and $S(A^*)\to\bar S$, while waste goes to $r\bar S/2$, so

$$\lim_{p\to0}\frac{\text{total spending on the transaction}}{S}=\frac r2 .$$

| $p$ | discovery spending / $S$ | waste / $S$ | planner's discovery spending / $S$ |
|---|---|---|---|
| $10^{-1}$ | 0.20 | 0.50 | 0.26 |
| $10^{-2}$ | 0.04 | 0.50 | 0.05 |
| $10^{-3}$ | 0.006 | 0.50 | 0.007 |
| $10^{-6}$ | 0.000 | 0.50 | 0.000 |

: Spending on one transaction as compute gets cheaper ($r=1$, $\bar S=A_0=1$). {#tbl-discovery}

The first column behaves as Krier expects.
The cost of finding an agreement and writing it down goes to nothing, and with it the gap between what the parties discover and what a planner would have them discover.
The second column is constant in $p$: in the contest world compute also moves surplus between the parties, so property (iii) does not hold there.

### Restraint between agents

Krier expects agents to settle down:

> "The agents themselves would likely converge on stable equilibria for most issues simply to reduce computational overhead - constant renegotiation is expensive even for AGI."

For that to remove waste, agents would have to agree to spend less on claiming.
In a single matter, mutual restraint is not an equilibrium: if Bob's agent holds back, Alice's agent gains by not holding back.
Between the same two parties over many periods, restraint could be sustained by the threat of reverting to the contest if either side cheats, which is the ordinary logic of repeated games.
That requires each side to observe the other's compute.
Compute use is private: an agent can prove it did some work, but not that it did no more.
A verifiable limit on compute per matter is the main way out of Result 1 that I have not tested; I do not know how to build one.

## Many matters under a fixed budget

This section asks whether an opponent's compute affects a principal's income.
Krier's agent manages, in his words, "a million micro-transactions in the background".
With $N$ principals there are up to $N-1$ matters per principal and $N(N-1)/2$ in all, about $5\times10^{19}$ for $N=10^{10}$, and $2^{N-1}$ coalitions containing any one principal.
Finding which pairs have an agreement worth making is the discovery problem of Result 2, where cheap compute helps.
Once matters are found, each principal has to spread its compute over them.
What counts below is not the number of matters $M_i$ but the stakes $E_i$, except where reading each matter has a fixed cost.

The model of this section applies when compute cannot be bought at the margin within the period: when it is rationed, or sold in fixed tiers.
Each principal has a compute budget $C_i$ for the period, which it cannot save, and chooses $c_{im}\ge0$ with $\sum_m c_{im}=C_i$ to maximize its *bargaining income* $\sum_m S_m s_{im}$.
The next section, where compute is bought out of wealth, supersedes this one whenever compute can be bought.

For $r\le1$ the share is concave in $c_{im}$, so $i$'s objective is concave in its own allocation and the first-order conditions of the Lagrangian

$$\mathcal L_i=\sum_m S_m s_{im}-\lambda_i\Big(\sum_m c_{im}-C_i\Big)$$

identify the best response; these are the Kuhn–Tucker conditions, which add that a matter given no compute must have a marginal return no higher than $\lambda_i$.
The multiplier $\lambda_i$ is $i$'s *shadow price* of compute: the bargaining income one more unit would bring, when compute is allocated as well as it can be.
For $r<1$ the marginal share is unbounded as $c_{im}\to0$, so every matter receives some compute.
Define $i$'s *strength* as $a_i=1/\lambda_i$: a principal is strong when one more unit of compute is worth little to it, because it already has plenty.
Take $\theta_m=\tfrac12$.
Principal $i$'s condition on matter $m$ is $rS_m s_{im}(1-s_{im})/c_{im}=\lambda_i$, and $j$'s is the same with $c_{jm}$ and $\lambda_j$.
Dividing one by the other gives $c_{im}/c_{jm}=a_i/a_j$, and so

$$s_{im}=\frac{a_i^{\,r}}{a_i^{\,r}+a_j^{\,r}},\qquad c_{im}=r\,a_i\,S_m\,s_{im}(1-s_{im}),\qquad \sum_m c_{im}=C_i ,$$

where the last equation pins down each $a_i$.

Every matter in the economy is divided according to the two parties' strengths alone, as in a rating system.
Alice's share against the landlord depends on her strength and the landlord's, and on nothing else about either of them.

Compute is allocated in proportion to $S_m\,s_{im}(1-s_{im})$: towards large matters and towards evenly matched ones.
Little goes to matters that are nearly won or nearly lost.

Only relative budgets matter.
Multiply every $C_i$ by the same factor and no share changes, because shares depend only on ratios of strengths.
A general fall in the price of compute, or a general rise in budgets, changes nothing about who gets what.
This is the opposite of property (ii): here an opponent's compute is the only thing a principal's own compute is measured against.

If Alice and Bob face only each other, across any number of matters, each allocates in proportion to the surplus $S_m$ and the share on every matter is $s=C_A^{\,r}/(C_A^{\,r}+C_B^{\,r})$.
This is the proportional rule of [Friedman (1958)](https://doi.org/10.1287/opre.6.5.699) for advertising budgets.
If Bob's budget is three times Alice's, at $r=1$ he takes 75% of every matter between them.

In a population of similar principals every share is $\tfrac12$, each matter takes $raS_m/4$ units, and the budget gives $a=4C/(rE)$: strength is compute per dollar at stake.
Suppose budgets scale with wealth as $C_i\propto w_i^{\eta}$ and stakes as $E_i\propto w_i^{\mu}$.
Then strength scales roughly as $w_i^{\eta-\mu}$, a relation exact only near equal strength.
If budgets rise at least in proportion to wealth ($\eta\ge1$) and stakes less than in proportion ($\mu<1$), richer principals are stronger on every matter.
If instead $\eta=\mu$, everyone is equally strong and every matter is divided at merit.

At $r=1$, $i$'s best response on matter $m$ is $c_{im}=\max\{0,\sqrt{a_iS_mc_{jm}}-c_{jm}\}$, so $i$ puts nothing at all on a matter where its opponent's compute exceeds $a_iS_m$.
Suppose Bob has a budget of 1 unit and two matters, each with surplus 1: one against Alice, who has a budget of 1 and no other matters, and one against the landlord, who has a budget $C_L$ and no other matters.
Once $C_L>4$, Bob puts all his compute on his matter with Alice and abandons the one with the landlord.

These results are close relatives of the conflict-network models of [Franke and Öztürk (2015)](https://doi.org/10.1016/j.jpubeco.2015.04.002) and [Xu, Zenou and Zhou (2022)](https://doi.org/10.1016/j.jet.2022.105571), in which each player fights several neighbours in a network and divides its effort among the fights; they use convex costs of effort where we use a budget.

## Buying compute out of wealth

This section asks whether income stops responding to compute above some level, as satiation says, and whether the floor is cheap.
When compute can be bought, a principal splits its wealth as $w_i=k_i+p\sum_m c_{im}$, between ordinary capital $k_i$, which returns $R$ per dollar, and compute.
Its *end-of-period resources* are $Y_i=Rk_i+\sum_m S_m s_{im}$, capital returns plus bargaining income.
(The capital letter $R$, the return on capital, is unrelated to the decisiveness $r$.)

A principal that keeps some capital, $k_i>0$, is *unconstrained*: at the margin it is indifferent between a dollar of compute and a dollar of capital, so a unit of compute must be worth $pR$ to it.
Its shadow price of compute is $\lambda_i=pR$, the same for every unconstrained principal, and so is its strength, $a_i=\bar a=1/(pR)$.
A principal for which a dollar of compute is worth more than a dollar of capital, even with all its wealth in compute, is *liquidity-constrained*: it holds no capital, $k_i=0$, its shadow price is above $pR$, and its strength is below $\bar a$.

**Result 3.**
Any two unconstrained principals have the same strength, so they divide every matter between them at merit, and each spends $rS_m/4$ on it in end-of-period terms, that is, dollars spent multiplied by $R$.
A billionaire does no better against an unconstrained opponent of modest means than two such opponents do against each other.
This is Krier's billionaire's phone, and it holds in the contest world too.
It is the [paradox of power](https://doi.org/10.1111/j.1468-0343.1991.tb00046.x) of Hirshleifer: the richer side has no reason to spend more on a contest than the prize warrants, and the poorer side fights as hard.
It also reverses the conclusion of the fixed-budget model that richer principals are stronger: once compute can be bought, wealth above a level defined next, the parity threshold, buys no strength.

The level at which this starts differs from the satiation level of the sufficiency world.
With every opponent unconstrained, all of $i$'s shares are $\tfrac12$ and its desired spending is $p\cdot r\bar aE_i/4=rE_i/(4R)$ dollars, so $i$ is unconstrained if and only if

$$R\,w_i\;\ge\;\frac r4\,E_i ,$$

which I call the *parity threshold*.
It is a fixed fraction of $i$'s stakes, in dollars, and does not depend on $p$.
In units of compute it is $rE_i/(4pR)$, which grows without bound as compute gets cheaper.
The satiation level is a technological constant; the parity threshold is set by opponents' spending in equilibrium.

Alice's tenancy is worth $4,000 a year in surplus between her and the landlord, and in this example it is her only matter.
For now I ignore the landlord's scale; the section on repeat players adds it, and it makes things worse for Alice.
At $r=1$ and $R\approx1$ her parity threshold is $1,000 of savings.
If she had $1,000 she would spend all of it on compute, take half the surplus, $2,000, and end the year with $2,000 in resources, against $3,000 in the sufficiency world.

### The production function at $r=1$

Before turning to Alice's actual $160, it helps to write the production function once, in terms of compute.
Take $r=1$ and a principal $i$ that is small relative to its opponents, all of whom have strength $\bar a$, and suppose $i$ has $C_i$ units of compute.
Write $x=a_i/\bar a$ for its strength relative to theirs, so that its share on every matter is $s=x/(1+x)$.
Its spending is $\sum_m c_{im}=a_iE_is(1-s)=\bar aE_i\,x\,s(1-s)$, and setting that equal to $C_i$ gives $x^2/(1+x)^2=C_i/(\bar aE_i)$, that is, $s^2=C_i/(\bar aE_i)$.
So

$$\text{bargaining income}=\sum_m S_m s_{im}=\sqrt{\frac{E_i\,C_i}{\bar a}}\qquad\text{for } C_i\le\bar aE_i ,$$

with share $\sqrt{C_i/(\bar aE_i)}$ on every matter, parity at $C_i=\bar aE_i/4$, and the whole surplus at $C_i=\bar aE_i$.
This one formula shows how income depends on the principal's own compute (as its square root), on its opponents' compute (inversely, through their strength $\bar a$) and on its stakes.
Compare the sufficiency world, where income is flat in own compute above $\bar c$ and does not depend on opponents at all.

When compute is bought at price $p$ and the alternative is capital at $R$, opponents who hold capital have $\bar a=1/(pR)$.
A principal below parity has a marginal dollar of compute worth more than $R$, so it puts all its wealth into compute, $C_i=w_i/p$.
A principal at parity would get less than $R$ from further compute, so it buys compute only up to parity and keeps the rest as capital.

**Result 4.**
Substituting $C_i=w_i/p$ and $\bar a=1/(pR)$ into the formula, a liquidity-constrained principal facing unconstrained opponents has

$$s_{im}=\sqrt{\rho_i}=\sqrt{R\,w_i/E_i}\ \text{ on every matter},\qquad Y_i=\sqrt{R\,w_i\,E_i}\qquad(\rho_i\le\tfrac14),$$

where $\rho_i=Rw_i/E_i$ is its wealth-to-stakes ratio.
It holds no capital, so its end-of-period resources are its bargaining income alone.
Putting Results 3 and 4 together, at $r=1$:

$$Y_i(w_i,E_i)=\begin{cases}\sqrt{R\,w_i\,E_i}, & Rw_i<E_i/4\\[2pt] R\,w_i+E_i/4, & Rw_i\ge E_i/4\end{cases}\qquad\text{against}\qquad Y_i^{\mathrm{suf}}=R\,w_i+E_i/2 .$$

The two branches meet at the parity threshold, where both give $E_i/2$.
Above it, the net gain from bargaining is $E_i/4$ against the sufficiency world's $E_i/2$: half.

Alice has $160, so $\rho=160/4000=0.04$.
Her agent spends all $160 on compute, and her share of the tenancy surplus is $\sqrt{0.04}=20\%$, so her bargaining income is $800 against the sufficiency world's $2,000.
Her end-of-period resources are also $800, since she has nothing left in capital, against the sufficiency world's $2,160, which adds her untouched savings.

| $\rho_i=Rw_i/E_i$ | share of each surplus | $Y_i/Y_i^{\mathrm{suf}}$ |
|---|---|---|
| 0.01 | 0.10 | 0.20 |
| 0.05 | 0.22 | 0.41 |
| 0.10 | 0.32 | 0.53 |
| 0.25 (parity threshold) | 0.50 | 0.67 |
| 1 | 0.50 | 0.83 |
| 10 | 0.50 | 0.98 |

: End-of-period resources in the contest world relative to the sufficiency world, at $r=1$, against unconstrained opponents. {#tbl-sqrt}

Above the parity threshold, end-of-period resources are between 67% and 98% of the sufficiency world's, depending on how much wealth a principal holds beside its stakes.

**Result 5.**
On Alice's tenancy the landlord's agent spends $640 and Alice's spends $160, so waste is $800, which is Alice's share.
If someone gave Alice enough to bargain at parity, her share would rise to $2,000 and waste would rise to $2,000 as well.

In symbols, on a matter between a liquidity-constrained $i$ and an unconstrained $j$ at $r=1$, waste in end-of-period terms is

$$R\,p\,(c_{im}+c_{jm})=s_{im}\,S_m ,$$

which follows from $Rp\,c_{jm}=S_ms(1-s)$ (because $Rp\bar a=1$), $Rp\,c_{im}=x\,S_ms(1-s)$ and $s=x/(1+x)$.
Waste on a matter equals the weaker side's share of it.
A lopsided matter is cheap because the weak side concedes and the strong side need not spend much; at equal strength, half the surplus is wasted.
Any policy that raises the weak side's share raises waste one for one, as long as $r$ does not change.

**Result 6.**
Bringing Alice to the parity threshold takes $840 a year, whatever compute costs.
In general it takes a top-up of $(rE_i/4R-w_i)^+$ dollars per period, proportional to stakes and independent of the price of compute.
Krier expects this cost to "approach zero asymptotically", as property (iv) says; in the sufficiency world it is $p\bar c$ per matter and vanishes with $p$, and in the contest world it is a fixed fraction of stakes at any $p$.

### Borrowing against bargaining gains

A dollar of extra wealth is worth $\tfrac12\sqrt{RE_i/w_i}$ to a liquidity-constrained principal, more than $R$ whenever $\rho_i<\tfrac14$.
Such a principal would borrow to buy compute if anyone would lend.
Under the constitution, with perfect enforcement and loyal agents, I see no reason a funder could not advance compute against a share of the bargaining gain, as litigation funders do with lawsuits.
With such funding nobody is liquidity-constrained.
Every matter is contested at parity, every share is at merit, there is no trap of the kind described in the section on wealth over time, and waste is at its maximum, $r/2$ of every surplus.
Alice would borrow compute worth $1,000, take $2,000, repay $1,000 and keep her $160 in capital, ending with $1,160 instead of $800; waste on her tenancy would rise from $800 to $2,000.

So the square-root law and the trap hold only where bargaining gains cannot be pledged.
Three reasons such a market might be incomplete come to mind: the gain may not be money (quiet, light, a view); the funder may be unable to verify the stakes or the merit share; or the funder may itself be a repeat player with the scale advantage described below.
I do not claim the market would fail.
The waste results (Results 1, 2 and 5) and the results on scale and on how complex a matter is do not depend on it; the results on who gets what do.
Either remedy, a subsidy or credit, fixes distribution by raising waste.

### Decisiveness other than one

For general $r\le1$ the same steps go through.
The share is $s=x^r/(1+x^r)$, so $x=\big(s/(1-s)\big)^{1/r}$, and the budget condition becomes $x\,r\,s(1-s)=\rho_i$.
Substituting the first into the second,

$$r\,s^{(1+r)/r}(1-s)^{(r-1)/r}=\rho_i ,$$

which reduces to $s=\sqrt{\rho_i}$ at $r=1$ and gives $s=\tfrac12$ at the parity threshold $\rho_i=r/4$.
For small $\rho_i$, $s\approx(\rho_i/r)^{r/(1+r)}$, so bargaining income is approximately $E_i^{1/(1+r)}(Rw_i/r)^{r/(1+r)}$, a Cobb–Douglas function of stakes and wealth.
The exponent on wealth, $r/(1+r)$, falls with $r$: at lower decisiveness, wealth matters less for the share.
The elasticity of bargaining income with respect to a liquidity-constrained principal's own compute, against unconstrained opponents, is $r(1-s)/(1+r(1-2s))$, which is $\tfrac12$ at $r=1$ for every $s<\tfrac12$.
If Alice doubled her compute, her bargaining income would rise by about 40%.

### A fixed cost of reading

Suppose that merely reading and evaluating a proposal costs a fixed $f$ units of compute.
[Anderlini and Felli (2006)](https://doi.org/10.1111/j.1468-0297.2006.01054.x) show that even small costs paid before bargaining begins can prevent Coasean agreement.
From the first-order condition, the compute $i$ spends on a matter is worth $\lambda_ic_{im}=rS_ms_{im}(1-s_{im})$ at its shadow price.
So the value of a matter to $i$, net of that, is $S_ms_{im}\big(1-r(1-s_{im})\big)$, and a matter is worth engaging only if

$$S_m\,s_{im}\,\big(1-r(1-s_{im})\big)\ \ge\ \lambda_i f .$$

For a weak principal, with small shares and a high shadow price, most matters fail this test.
Alice engages on a few large matters, her tenancy and her job, and lets the rest go by default.
A principal with $C_i$ units can read at most $C_i/f$ proposals, and the landlord, an insurer and a hundred vendors can between them send more than that.
C2 protects Alice's entitlements, since silence is refusal, but the surplus on the unread matters is lost.
A bond of at least $pf$ posted with each proposal and paid to the recipient would make reading self-financing.
[Shahidi et al. (2025)](https://doi.org/10.3386/w34468) flag congestion of this kind among agents.
I read click-through terms of service as this equilibrium today, with human attention as the budget.

## Wealth over time

This section asks what part a principal's initial endowment plays.
Krier offers a remedy for unequal access:

> "A hybrid might work best: a universal basic compute allocation for personal use, plus additional targeted support for specific democratic and legal functions where equal participation is constitutionally guaranteed."

He proposes an allocation of compute.
In the contest world the results above imply that the gap to be closed is one of dollars relative to stakes, and that closing it raises waste.
To see what happens over many periods, let wealth evolve, with no credit market.

Each period a principal must consume a subsistence amount $\underline y$ and saves a fraction $\beta$ of what remains, so next period's wealth is $w_i'=\beta\,(Y_i-\underline y)^+$, where $(\cdot)^+$ means the larger of the quantity and zero.
Bargaining income includes the wage bargain, and there is no other income in the model.

**Result 7.**
For a liquidity-constrained principal facing unconstrained opponents at $r=1$, wealth evolves as $w'=\beta(\sqrt{REw}-\underline y)^+$.
Substituting $u=\sqrt w$, its fixed points solve $u^2-\beta\sqrt{RE}\,u+\beta\underline y=0$.
If $\beta RE>4\underline y$ there are two, and the lower one,

$$w_-=\Big(\tfrac{\beta\sqrt{RE}-\sqrt{\beta^2RE-4\beta\underline y}}{2}\Big)^{2},$$

is unstable.
I call it the *trap threshold*: below it, wealth falls to zero and with it the principal's share of every matter.
Above it, wealth grows.
If it grows past the parity threshold, the principal becomes unconstrained and wealth settles at $w^{**}=\beta(E/4-\underline y)/(1-\beta R)$, which requires $E/4>\underline y$ and $\beta R<1$.
(If $w^{**}$ would lie below the parity threshold, wealth instead settles at the upper constrained fixed point; with the parameters below it does not.)
In the sufficiency world there is no trap: bargaining income is $E/2$ whatever the wealth, and wealth settles at $w^{**}_{\mathrm{suf}}=\beta(E/2-\underline y)/(1-\beta R)$.
So initial endowments matter in one specific way, through which side of the trap threshold a principal starts on.
Above it, the concavity of the production function in wealth erases initial differences among principals with the same stakes.

To see the whole economy, I simulated 600 principals, each party to about 8 matters on a random network, with surplus per matter drawn from a lognormal distribution with mean 1, initial wealth lognormal with median 1 and log-standard deviation 1.5, $\beta=0.9$, $R=1.05$, $\underline y=1.2$ and $r=1$, for 300 periods.
These are simulation results for one set of parameters, not theorems.

| scenario | Gini of wealth | share of principals at zero wealth | waste / total surplus | mean wealth |
|---|---|---|---|---|
| sufficiency world ($r=0$) | 0.27 | 0.2% | 0 | 46 |
| contest, $p=10^{-3}$ | 0.45 | 12.5% | 0.39 | 21 |
| contest, $p=10^{-6}$ | 0.45 | 12.5% | 0.39 | 21 |
| contest + basic compute worth 0.05 a period (0.6% of mean stakes) | 0.42 | 9.7% | 0.44 | 18 |
| contest + basic compute worth 0.5 a period (6% of mean stakes) | 0.28 | 0.7% | 0.48 | 22 |

: Wealth after 300 periods (simulation, one parameter set, no credit market). {#tbl-sim}

At mean stakes, about 8, the trap threshold is $w_-\approx0.27$ and the parity threshold is $Rw=E/4\approx2$.
The two contest rows are identical: a million-fold fall in the price of compute changes nothing.
In the contest rows, at the end, 12.7% of principals are liquidity-constrained and 12.5% are at zero wealth, so only 0.2% end between the two thresholds.
A basic compute allocation large enough in dollars relative to stakes removes the trap and restores the sufficiency world's Gini coefficient.
Mean wealth stays at half the sufficiency world's, and waste rises from 39% to 48% of surplus, as Result 5 predicts.
The allocation also arrives free in the simulation, with nobody taxed to pay for it; a funded allocation is not simulated.

Two numbers need reconciling with the closed forms.
At mean stakes the closed-form unconstrained steady state is $w^{**}\approx13$, yet mean wealth in the contest rows is 21.
The difference is that survivors face some opponents at zero wealth, from whom they take nearly the whole surplus at little cost, as Result 5 says a lopsided matter allows.
The 0.2% of principals at zero wealth in the sufficiency-world row are those whose drawn stakes give $E/2<\underline y$.

The case $r>1$ is not simulated, because the allocation problem is then not concave in $c_{im}$ and the first-order conditions no longer identify the best response.
[Hirshleifer (1991)](https://doi.org/10.1111/j.1468-0343.1991.tb00046.x) finds that when decisiveness is high the paradox of power fails and the richer side gains.
Jones's fitted $r\approx1.3$ lies in that region, so I expect $r>1$ to be less favourable to poorer principals than what is shown here, but that is untested.

## Repeat players

This section is about scale, which plays no part in the sufficiency world.
Krier expects weak network effects and easy switching among agent providers:

> "Unlike social media, network effects are also far weaker. And in a competitive market with switching costs approaching zero, parasitic agents get quickly identified and abandoned."

Network effects are one force towards concentration, and bargaining has another.
Much bargaining work can be reused across matters of the same type: the landlord's analysis of its standard lease, or a model tuned on its past negotiations with tenants, serves all its tenancies.
Alice's work on her one tenancy serves only that.

**Result 8.**
Let the effective compute on a matter be $z_{im}=g_i^{\phi}\,\ell_{im}^{1-\phi}$, where $g_i$ is a general investment paid for once and usable on all of $i$'s matters of this type, $\ell_{im}$ is work specific to the matter, and $\phi\in[0,1)$ measures how much of the work is reusable.
Shares are given by the contest success function with $z$ in place of $c$.
A principal with $M$ similar matters (for the landlord, $M$ is its number of tenancies, which here is all of $M_i$) minimizes the cost $g+M\ell$ of reaching a given $z$ by setting $g/\ell=\phi M/(1-\phi)$.
Its effective compute per matter is then $M^{\phi}$ times that of a one-matter principal spending the same per matter, and its total spending per matter is $rSs(1-s)/\lambda$, as before.
Against $M$ one-matter opponents with the same shadow price, its share is

$$s_{\text{repeat}}=\frac{M^{\phi r}}{1+M^{\phi r}} .$$

| $\phi$ | $M=10$ | $M=10^3$ | $M=10^6$ |
|---|---|---|---|
| 0.2 | 0.61 | 0.80 | 0.94 |
| 0.5 | 0.76 | 0.97 | 0.999 |

: The repeat player's share at $r=1$. {#tbl-repeat}

With $M=10{,}000$ tenancies and $\phi=0.2$, the landlord's share of each is 86%, even if Alice had the savings to be unconstrained.
Both sides then spend $rSs(1-s)$ in end-of-period terms, about $470 each on the $4,000 tenancy, so Alice's bargaining income is about $550, and under $80 after paying for her compute.
Waste on such a matter is $2rs(1-s)$ of the surplus, about a quarter here, falling towards zero as the match becomes more lopsided.
This is the "haves" against the "have-nots" of [Galanter (1974)](https://doi.org/10.2307/3053023): the repeat player against the one-shotter.
It needs no wealth advantage; each tenant could be richer than the landlord.

The counter is pooling, which is the mechanism Krier names:

> "But what if the agents of 10,000 residents, seeing a factory's proposal to increase emissions, can form a bargaining coalition in a nanosecond?"

If Alice and her fellow tenants are represented by one provider that amortizes its work over $M'$ tenancies, the ratio of effective compute becomes $(M/M')^{\phi}$ and the landlord's share falls to $(M/M')^{\phi r}/(1+(M/M')^{\phi r})$.
Parity requires representatives of comparable scale on both sides of each type of matter.
Reuse of bargaining work is a separate source of economies of scale, and it pushes representation towards a few large providers.
A principal's strength then depends on her provider's scale in each type of matter, a further argument of the production function that is neither her compute nor her endowment.
The share formula is a theorem of the model; what it implies for the market structure of agent provision is my conjecture.

## How complex a matter is

This section asks when satiation does hold.
Krier's phrase for what agents enable is "hyper-granular contracting", and his illustrations are conditional preferences: loud music on Saturday but not Sunday, carpooling only if it adds less than ten minutes.
Jones's two regimes say that whether both sides can handle such conditions is what decides whether compute matters at all.

What a party's agent has to solve is the bargaining game on a matter.
How hard that game is depends on the terms of the contract and on the circumstances: what each side wants and knows, what each could do instead, and the states of the world the agreement has to cover.
As a simplification, the model collapses both into one number, the *detail* $n$ of the matter, the number of contingencies the game distinguishes.
Write $n_0$ for the part set by the circumstances, so that $n\ge n_0$; the party that writes the contract chooses only how much detail it adds beyond $n_0$.
The rest of this section rests on an assumption, not a theorem: that the compute needed to solve a matter outright grows exponentially in its detail, $G(n)=G_0\gamma^{n}$ with $G_0$ a constant and $\gamma>1$.
Two reference points for $\gamma$ are about 7 per unit of board size in Jones's Hex data, and 2 for checking $n$ binary contingencies exhaustively, since there are $2^n$ combinations.
Mapping Hex board size onto contract contingencies is an analogy, not a measurement.
A principal's effective compute is $\min\{C,G(n)\}$: compute beyond what solves the game is useless.
Surplus rises with detail, $S(n)=\bar S(1-\delta^{n})$ with $0<\delta<1$, and $\theta=\tfrac12$.

**Result 9 (follows from the assumption).**
If both sides can afford $G(n)$, the division is at merit and extra compute is worth nothing; $G(n)$ here plays the part of the satiation level $\bar c$.
The satiation property of the sufficiency world holds for a matter of fixed detail $n$, not for a contract considered apart from its circumstances.

The detail a principal can afford grows only logarithmically in its budget: the largest $n$ it can solve is $\log_\gamma(C/G_0)$.
A million-fold fall in the price of compute adds about $\log_7 10^6\approx7$ units at Hex's rate, or $\log_2 10^6\approx20$ binary contingencies.

With unequal budgets $C_i<C_j$ and $j$ as the *drafter*, the party that writes the contract, $j$ gains twice by adding detail that takes $n$ beyond what $i$ can solve, $n>n_i=\log_\gamma(C_i/G_0)$.
It gains a larger surplus $S(n)$, and it gains a share above merit, $s_j=e_j^{\,r}/(e_j^{\,r}+C_i^{\,r})$ with $e_j=\min\{C_j,G(n)\}$.
The choice matters only when the circumstances alone are within what $i$ can solve, $n_0\le n_i$; if $n_0>n_i$ the matter is beyond $i$ whatever the contract says.
What limits the drafter is that the other side accepts any contract that leaves it at least its entitlement, by C2.
So the drafter raises $n$ until either $S(n)$ stops growing appreciably or its own compute cost outweighs the gain.
The landlord drafts the lease at a detail beyond what Alice's agent can solve, and Alice never reaches the flat part of the curve.

The literature has the same mechanism without the compute.
[Gabaix and Laibson (2006)](https://doi.org/10.1162/qjec.2006.121.2.505) show how firms shroud add-on prices, and [Carlin (2009)](https://doi.org/10.1016/j.jfineco.2008.05.002) how retail financial firms make prices complex on purpose.
[Tirole (2009)](https://doi.org/10.1257/aer.99.1.265) models thinking about contingencies before signing as costly and partly a matter of rent-seeking, so that contracts can be more complete than is socially worthwhile.
[Arora, Barak, Brunnermeier and Ge (2011)](https://doi.org/10.1145/1941487.1941511) show that a seller of financial derivatives can plant unfavourable terms whose detection by the buyer is as hard as finding a planted dense subgraph in a random graph, a problem believed intractable, so drafter and reviewer face different costs at the same $n$.
[Larson and Sandholm (2001)](https://doi.org/10.1016/S0004-3702(01)00132-1) and [Halpern and Pass (2015)](https://doi.org/10.1016/j.jet.2014.04.007) are formal treatments of bargaining and of games when compute is costly.

The model points to a remedy: a right to a *standard-form contract*.
Anyone may insist on a contract that brings the matter's detail to at most $\bar n\ge n_0$, with $G(\bar n)$ within the basic compute allocation.
That changes the other side's fallback from its entitlement to its merit share of $S(\bar n)$, so a drafter who proposes more detail must offer at least that.
On matters contracted at $\bar n$ both sides can solve the game, so by construction the division is at merit, extra compute is worth nothing, and there is no waste.
The right can cap what the contract adds but not $n_0$, so it restores satiation only on matters whose circumstances alone are solvable within the basic compute allocation, $G(n_0)$ within it.
The cost is the surplus given up, $S(n)-S(\bar n)=\bar S(\delta^{\bar n}-\delta^{n})$ per matter.
In this model it reduces waste and inequality together, which no other remedy considered here does, though that is a consequence of the assumption and not a tested result.
It is also a restriction on freedom of contract, a repeal of C6: a rule about how detailed contracts may be, made by someone who is not a party to them.

## Manufactured threats

This section describes the one case in which bargaining leaves a principal worse off than if the matter had never arisen.
Krier expects agents to make enforcement nearly free:

> "Ideally the agent system transforms enforcement from a costly legal battle into a near-instantaneous computational verification."

Cheap enforcement also makes commitments cheap, including commitments to do harm.

Suppose Bob could lawfully plant a row of fast-growing conifers along the boundary, at a cost to him of $200, which would cut Alice's light and cost her $1,000 a year in value.
Bob has no use for the trees.
Without a way to commit, he would never plant them, since that only costs him money.
With escrows and automatic enforcement he can bind himself to plant them unless Alice pays.
That creates a matter with surplus $1,200, the harm avoided plus Bob's cost saved.
At equal strength and $r=1$, each side spends $300 on compute over it; Bob ends $100 better off than if he had never made the threat, and Alice $700 worse off.

**Result 10.**
Let $j$ have a lawful act that costs it $\kappa>0$, harms $i$ by $h>0$ and has no other use.
If $j$ can commit, the act creates a matter with surplus $h+\kappa$.
The *disagreement point*, what each side gets if no agreement is reached, is $-h$ for $i$ and $-\kappa$ for $j$, and the agreement gives each its share of $h+\kappa$ on top of that.
Relative to a world where the threat was never made, the gross transfer from $i$ to $j$ is

$$s_jh-s_i\kappa .$$

With equal shadow prices each side also spends $r\,s_is_j(h+\kappa)$ on the matter, so $j$'s net gain from making the threat is

$$s_jh-s_i\kappa-r\,s_is_j(h+\kappa),$$

and $i$ loses the transfer plus its own spending.
At equal strength the net gain is positive if and only if $h/\kappa>(2+r)/(2-r)$: $h>3\kappa$ at $r=1$, and $h>\kappa$ at $r=0$.
For the conifers, $500-100-300=100$.
Waste therefore deters marginal threats, and the sufficiency world, $r=0$, is the one in which threats pay most easily.

The theory of incomplete contracts ([Grossman and Hart 1986](https://doi.org/10.1086/261404); [Hart and Moore 1990](https://doi.org/10.1086/261729)) starts from the observation that contracts cannot specify every contingency, so what matters is who holds residual control when an unspecified one arises.
Legal entitlements are incomplete in the same way: they cannot list every lawful act a neighbour might take.
Finding acts like Bob's is a search over what the law permits.
If more search finds more such acts, then the surplus $i$ is forced to bargain over rises with other principals' compute; that is a conjecture, not something the model shows.
C2 does not help, because refusing means the act is carried out.

[Daly and Giertz (1975)](https://www.jstor.org/stable/1806636) is the classic statement of extortion within Coasean bargaining, and [Ngo (2026)](https://www.mindthefuture.info/p/economic-efficiency-often-undermines) responds to Krier on related grounds, that efficiency reasoning tends to overlook credible threats.
The remedy the model points to is a rule against acts taken in order to be bought off, which requires a court to judge purpose, which is more than verifying that a term was met.

## The two production functions compared

Krier describes the state's role as that of a "framework guarantor":

> "The (gradually automated) state continues to define and enforce basic property rights, contract law, criminal justice, and constitutional rights - the bedrock rules without which agent negotiations would be meaningless."

Given those rules, the table sets the sufficiency world against the contest world as the models give it, and says which model and which value of $r$ each row comes from.

| | sufficiency world | contest world | source |
|---|---|---|---|
| own compute | no effect above the satiation level $\bar c$ | bargaining income $\sqrt{E_iC_i/\bar a}$; elasticity $r(1-s)/(1+r(1-2s))$, which is $\tfrac12$ at $r=1$; bought only up to the parity threshold | wealth-funded model; formula at $r=1$, elasticity for $r\le1$ |
| where income stops responding | at $\bar c$, fixed in compute units, so its cost $p\bar c\to0$ | at the parity threshold $Rw_i\ge rE_i/4$, fixed in dollars; in compute units it grows as $1/p$ | wealth-funded model, $r\le1$ |
| others' compute | no effect | lowers income, through $\bar a$; scaling all budgets together changes nothing | fixed-budget model, $r\le1$ |
| total compute | creates surplus | discovery compute creates surplus and its cost vanishes as $p\to0$; waste is $r/2$ of surplus at equal strength, at any $p$ | one matter, $r\le2$ |
| initial endowment | sets entitlements only | also sets the share, $\sqrt{Rw_i/E_i}$ below the parity threshold; with subsistence needs, a trap below $w_-$; both removed by a credit market | wealth-funded model and simulation, $r=1$, no credit |
| scale | no effect | a repeat player's share is $M^{\phi r}/(1+M^{\phi r})$ | repeat-player model, $r\le1$ |
| cost of a subsidy for parity | vanishes with $p$ | $(rE_i/4R-w_i)^+$ per head per period at any $p$, and raises waste | wealth-funded model, $r\le1$ |
| detail of a matter | every matter is one both sides can solve | set by circumstances ($n_0$) and the drafter; a principal can solve detail up to $\log_\gamma(C/G_0)$ | matter-complexity model, under an assumed cost function |
| many parties | coalitions form at negligible cost | efficient agreement fails for large $N$ at any compute | not part of the model; see the appendix |

: Two production functions for a principal. {#tbl-tally}

Several rows agree in part.
Discovery gets cheap; above the parity threshold, wealth buys no advantage; a matter of detail both sides can solve has the satiation of the sufficiency world.
The disagreements in the first seven rows come from one feature: bargaining income depends on the ratio of a principal's compute to its opponent's, so compute is an input to a contest, and spending on it does not fall with its price.
The many-party limit has a different source and does not depend on compute at all.

## Where this leaves the proposal

The models support three comparisons, of different strength.

The first is per matter.
A principal can refuse any matter and keep its entitlement, so no single matter leaves it worse off than if that matter had never been raised.
This is a guarantee about each matter, not a comparison of worlds.
Manufactured threats are the exception.

The second is between the contest world at $r=1$ and the sufficiency world.
Principals above the parity threshold get the sufficiency world's shares but keep half its net gain from bargaining, since the other half is waste.
Below the parity threshold, and without a credit market, shares scale with the square root of wealth relative to stakes, and some principals fall below the trap threshold and stay there.
With a credit market the inequality goes and the waste rises to its maximum.
Representation concentrates in providers that can reuse bargaining work, and the drafter sets the detail of the contract.
Repeat players, and principals facing much weaker opponents, can get more than the sufficiency world gives them; the economy as a whole gets less, by the amount wasted.
For most principals the contest world is worse than the sufficiency world, and how much worse depends on $r$, a number nobody has measured.

The third comparison, against the present, is not modelled.
What the models suggest, as conjecture, is this.
Today the same contest is run with lawyers' hours and human attention as the input, and most small matters are never contested, because the fixed cost of engaging is too high and default rules settle them.
Cheap compute then improves discovery, by Result 2, and extends the contest to matters now settled by default rules, with waste of $r/2$ of the surplus on each.
Whether that nets out well depends on $r$.

Results 1 to 8 reduce to the sufficiency world at $r=0$, and, by Result 9, on any matter both sides can solve.
Manufactured threats do not depend on $r$ in that way; they pay more easily at $r=0$.
The many-party limit in the appendix does not depend on $r$ or on compute.

The remedies the models point to are rules that bound the game: standard-form contracts, a verifiable cap on compute per matter if one can be built, a rule against manufactured threats, and bonds posted with proposals.
None of them is tested here.
Each is a rule about how bargaining is conducted, made and enforced by someone who is not a party, which goes beyond enforcing contracts and entitlements.
Caps need care: [Che and Gale (1998)](https://www.jstor.org/stable/116854) show, for an all-pay auction (a contest in which every side pays what it spends and the highest spender wins), that capping spending can raise total spending when contestants value the prize differently.

## Cruxes

Two quantities decide which world a matter is in.

- *Decisiveness $r$ for bargaining agents, measured on matters neither side can solve outright*, since on solvable matters the measurement returns zero for a different reason.
  At $r=0$ every matter is in the sufficiency world; $0<r\le1$ gives the results here; $r>1$, where Jones's fitted 1.3 lies, is outside the methods used here, and Hirshleifer's result suggests that wealth then buys advantage.
  It can be measured with the Project Deal design, varying the compute given to a fixed model instead of the model.
- *The fraction of matters, weighted by surplus, that both sides can solve with the compute they have*, and how much of each matter's detail is set by circumstances ($n_0$) and how much by the contract.
  Sufficiency is decided matter by matter, so the answer may be that some matters are in each world.

Three more decide which results apply within the contest world.

- *Whether agents can verify one another's compute use.*
  If they can, restraint can be sustained between parties who meet repeatedly.
  The test is whether an agent can prove an upper bound on the compute it used, which today's proofs of work done do not provide.
- *Whether bargaining gains can be pledged to a lender.*
  That depends on whether a lender can verify the stakes and collect from the gains; the nearest present-day evidence is which legal claims litigation funders will and will not finance.
  It decides the results on who gets what, not the results on waste.
  The market for such lending is not modelled here, and whether it would be complete is an open question.
- *Reusability $\phi$*, the elasticity of effective compute per matter with respect to the number of similar matters handled.
  At $\phi=0$ scale gives nothing; for any $\phi>0$ the advantage grows with $M$ as in Result 8.
  It can be measured by how a representative's results per dollar improve with its caseload.

## Other responses to Krier

Others have responded to Krier's essay on different grounds.
[Petel (2025)](https://mateopetel.substack.com/p/price-what-you-can-protect-what-you) argues for constitutional non-negotiables, hardened identity and verification, and limits on platform power.
[Sharp et al. (2025)](https://arxiv.org/abs/2510.16853) name "agentic inequality" and classify it by the availability, quality and quantity of agents, without an equilibrium model.
[Ngo (2026)](https://www.mindthefuture.info/p/economic-efficiency-often-undermines) argues that efficiency framings neglect autonomy and credible threats.
[Shahidi et al. (2025)](https://doi.org/10.3386/w34468) survey market design with agents and flag congestion and obfuscation.
Krier himself builds on the "virtual agent economy" of [Tomašev et al. (2025)](https://arxiv.org/abs/2509.10147).
This article differs from these in computing, for a given decisiveness, how much is wasted on bargaining and who gets what.

## Limitations and tests

The contest success function is imported from board games, not measured in bargaining.
Principals are risk-neutral, returns on capital are linear at rate $R$, and the merit share is $\tfrac12$ throughout the results on many matters.
The square-root law assumes the liquidity-constrained principal is small relative to its opponents, so that their shadow prices do not move.
There is no cooperation sustained by repeated play.
The simulation uses one parameter set, has no credit market, and its subsidy is unfunded.

Besides the cruxes and the case $r>1$, risk aversion could change the conclusion.
A share of the surplus is the same as a probability of winning all of it only for a risk-neutral principal or one with many small independent matters.
If the contest decides who wins, a liquidity-constrained principal that puts all its savings into compute on one large matter makes an all-or-nothing bet, and a principal that cares about the long-run growth of its wealth, as under the Kelly criterion, would spend less, which would move its optimum and the parity threshold.

TODO: decide whether the standard-form remedy deserves its own model, with $\bar n$ chosen by a planner trading surplus lost against waste avoided.

## Appendix A. Matters with many parties

This appendix is not part of the production-function argument, but two of Krier's examples involve many parties at once:

> "The developer's agent must discover the price at which every single homeowner would agree."

There are two separate limits on finding such a price.

The first is computational.
For a general bargain among $N$ parties, the number of ways to partition them into coalitions lies between $N^{N/2}$ and $N^{N}$.
[Sandholm et al. (1999)](https://doi.org/10.1016/S0004-3702(99)00036-3) show that any guarantee on the quality of the partition found requires examining at least $2^{N-1}$ of them.
[Deng and Papadimitriou (1994)](https://doi.org/10.1287/moor.19.2.257) give hardness results in $N$ for the standard cooperative solution concepts, and [Conitzer and Sandholm (2002)](https://arxiv.org/abs/cs/0205075) for designing the mechanism itself.
These are worst cases, and disputes that arise in practice have structure; but in the worst case a $k$-fold increase in compute adds only $\log_2k$ parties to what can be handled.

The second is informational, and compute does not touch it.
[Mailath and Postlewaite (1990)](https://doi.org/10.2307/2298018) show that when each party's valuation is private, participation is voluntary and nobody subsidizes the agreement from outside, the probability of reaching an efficient agreement goes to zero as $N$ grows, for any mechanism at all.
[Myerson and Satterthwaite (1983)](https://doi.org/10.1016/0022-0531(83)90048-0) is the two-party case, and [Dixit and Olson (2000)](https://doi.org/10.1016/S0047-2727(99)00089-4) a related result on voluntary participation.
Krier's own remedies at this point are an option fee on stated valuations, in the manner of a Harberger tax (a periodic tax on the value an owner declares, at which anyone may then buy), and compulsory reimbursement by coalitions that veto.
Both are compulsory, which is the theorem's way out.
For our purposes this component of the production function is flat in compute.

## Appendix B. Notation

Symbols used in only one section are defined there.
The capital letter $R$ (the return on capital) and the lower-case $r$ (decisiveness) are different quantities.

| symbol | meaning |
|---|---|
| $N$ | number of principals |
| $w_i$ | liquid wealth of principal $i$ at the start of a period, in dollars |
| $m$ | a matter: one bilateral bargain, between $i$ and an opponent $j$ |
| $S_m$ | surplus of matter $m$: the dollars an agreement creates over both sides keeping their entitlements |
| $E_i=\sum_{m\ni i}S_m$ | $i$'s stakes: total surplus over the matters $i$ is party to |
| $M_i$ | number of matters $i$ is party to |
| $M$ | a repeat player's number of similar matters (for the landlord, equal to $M_i$) |
| $c_{im}$ | compute $i$ spends on matter $m$, in units |
| $p$ | price of one unit of compute, in dollars |
| $R$ | gross return on a dollar put to ordinary productive use instead of compute |
| $k_i$ | $i$'s ordinary capital |
| $Y_i$ | end-of-period resources, $Rk_i+\sum_mS_ms_{im}$ |
| $s_{im}$ | $i$'s share of $S_m$ |
| $\theta_m$ | merit share: $i$'s share if both sides spend the same ($\tfrac12$ unless stated) |
| $r$ | decisiveness: how strongly a compute advantage shifts the share |
| $Y_i^{\mathrm{suf}}$ | end-of-period resources in the sufficiency world |
| $\bar c$ | the satiation level of the sufficiency world |
| $n$, $n_0$ | detail of a matter, and the part of it set by the circumstances |
| $C_i$ | $i$'s compute budget, where it is fixed |
| $\lambda_i$ | $i$'s shadow price of compute: the bargaining income one more unit would bring |
| $a_i=1/\lambda_i$ | $i$'s strength |
| $\bar a=1/(pR)$ | strength of every unconstrained principal |
| $\rho_i=Rw_i/E_i$ | $i$'s wealth-to-stakes ratio |
| $w_-$ | the trap threshold |

<!-- TODO: move these hyperlink citations into Zotero and cite them as [@Key] (dan-lit-search skill) -->
