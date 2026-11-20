---
title: "Computational and informational costs imply selfish delegated agent constitutional negotiation still need a benevolent leviathan"
date: '2026-11-19'
abstract: |
  Séb Krier argues that AI agents acting for individuals will make bargaining cheap enough for private Coasean deals to replace most regulation of externalities, leaving a lean "framework guarantor".
  I grant a strong premise: agents are perfectly loyal, and the prices of computation $c$ and communication $\kappa$ are positive but arbitrarily small.
  I split the expected shortfall from the best achievable outcome into four causes: friction, which vanishes as $c,\kappa\to 0$, and three that do not.
  The informational loss is independent of $c$ and $\kappa$: when one decision needs the consent of $N$ parties with private values, the probability that voluntary, budget-balanced bargaining reaches an efficient affirmative decision tends to zero as $N$ grows (Mailath and Postlewaite 1990).
  Pricing by each of $N$ independent rights-holders realizes, when values are uniform, a fraction $1/(N+1)$ of efficient trades, and the proposed bargaining club gives up truthfulness, efficiency or voluntariness.
  The computational loss grows exponentially in the worst case in items $m$, parties $N$ and contingencies $k$.
  In a standard contest model with $r\le N/(N-1)$, spending on bargaining advantage is a share $r(N-1)/N$ of the contested surplus for every $c$.
  Each known remedy is a sovereign act, so the scheme needs a benevolent leviathan, able to coerce and maximizing welfare, that, unless it pays an open-ended subsidy, also knows the distribution of preferences.
---

## Introduction

Coase (1960) argued that if bargaining cost nothing, the parties to an externality would strike an efficient deal whatever the initial assignment of legal rights, so the main obstacle to private solutions is the cost of transacting.
Séb Krier, who leads frontier policy development at Google DeepMind and writes in a personal capacity, argues in his essay [Coasean Bargaining at Scale](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale) (Krier 2025) that capable AI agents will bring those costs close to zero.
If each person has a software advocate that knows their preferences and can negotiate with millions of other advocates at almost no cost, then a large share of what governments now do by regulation could be done by private agreement, and the state could retreat to enforcing contracts, criminal law and a few absolute prohibitions.

I think the conclusion does not follow, even when the premise is granted in a strong form.
The losses that keep private bargaining short of efficiency come in two kinds.
One kind scales with the price of computation and communication: search, drafting, messaging, routine monitoring.
Agents will cut these, perhaps by a great deal.
The other kind does not scale with those prices.
It comes from private information, from the number of bits and operations that the allocation problem itself demands, and from spending on bargaining advantage, where the quantity bought rises to offset any fall in its unit price.
For the public decisions that make up most of Krier's examples, the informational loss gets worse as the number of affected parties $N$ grows.
Of the losses that do not scale with price, the informational one carries most of the argument; the computational one shows that cheap computation does not dissolve the residual problem, and that making it tractable is itself a choice of rules.

Every remedy I know of for the losses that do not scale with price is an act of sovereignty: compelling a party who has not consented, taxing to fund a subsidy, assigning entitlements using knowledge of how preferences are distributed, restricting what contracts may say, choosing which of several equilibria is played, and deciding the cases no contract covers.
Agents bargaining for their principals cannot supply these remedies by further bargaining, because choosing a remedy is a decision of the same kind, posed one level up; I argue this in the section on the regress.
The scheme therefore still needs what I will call a benevolent leviathan: an actor that can impose outcomes, including taxes, on parties who do not consent (the leviathan part), and whose objective is aggregate welfare and not its own revenue or power (the benevolent part).
The phrase joins Hobbes's (1651) Leviathan, the sovereign whose power to compel is what makes agreements hold, to the warning of Brennan and Buchanan (1980), who modelled the state as a revenue-maximizing Leviathan because benevolence cannot be assumed.
Every remedy needs the power to coerce, by binding dissenters or by taxing.
Every remedy except an open-ended subsidy also needs something that is not part of this definition, knowledge of how preferences are distributed across the population, and budgeting or policing the subsidy needs it too.
The scheme needs a benevolent leviathan that also has this knowledge, and nothing in the scheme produces one.

The informational argument is old: Farrell (1987) made the case that private information undermines the Coase theorem, and the theorems I rely on date from the 1980s and 1990s.
What I add is to apply them to the mechanisms Krier proposes, and to show that the quantities his proposal scales up, the number of parties and the granularity of contracts, make the residual problem harder.
Several published responses to Krier make related points (Petel 2025; Sharp et al. 2025; Shahidi et al. 2025; Ngo 2026), and I describe each where its argument arises.

A theorem from the literature is cited with the conditions that matter for the application.
A derivation of my own is introduced by the sentence "The derivation is mine." and shown in full.
Claims I believe but cannot prove are marked as arguments.

## What the essay claims and what it concedes

Krier starts from Hayek (1945); in Krier's words, the planner "cannot possess the dispersed, specific knowledge of time and place known only to the individuals on the ground."
He argues that high transaction costs forced societies back on the planner, and that AI agents remove that excuse.
He writes: "What costs $10,000 in legal fees today might cost pennies to compute tomorrow."
An agent that knows its principal can express preferences conditioned on context: loud music tolerated on a Saturday and not on a Sunday, a carpool accepted if it adds less than ten minutes.
In his words, "AGI could enable hyper-granular contracting."
He also casts agents as a coordination device: "instead of each actor guessing everyone else's move (what economists would call a Nash deadlock), they can condition their actions on shared signals and contracts, unlocking deals that were previously out of reach - a correlated equilibrium."
The phrase "Nash deadlock" is Krier's; I define correlated equilibrium in the section on computation.

Four examples carry the essay, and I use them as running cases.
In the first, a delivery truck's agent planning a route "simply sees a higher 'price' for entry onto your street, a signal broadcast by your agent", and decides whether to pay the clean-air fee or go round.
In the same passage, a neighbour in labour can have prices dropped to clear her way, and later "verified emergencies glide through at zero (or negative) price"; Krier hopes the agent system turns enforcement into "a near-instantaneous computational verification."
In the second example, a developer wants to put up a building that the neighbours dislike, and "The developer's agent must discover the price at which every single homeowner would agree."
In the third, Krier anticipates that one homeowner will hold out for an absurd price, and answers with a voluntary bargaining club: "each person privately inputs the minimum they'd accept; the software aggregates that into a single take‑it‑or‑leave‑it offer."
He argues that this makes honesty the best policy: "Overstating just risks killing the deal (you get zero), and if it clears, the payout is at the common clearing price - so padding your number doesn't boost your check. The group speaks with one voice without surrendering property rights".
In the fourth, the agents of 10,000 residents facing a factory's proposal to raise emissions "can form a bargaining coalition in a nanosecond" and declare "Our collective price to accept this pollution is X million dollars, non-negotiable."
He expects adoption to start on a smaller scale, with "agents negotiating the office thermostat, allocating shared resources in an apartment block, or fairly dividing household chores."

Around the examples he places guardrails.
Chronic over-bidders pay an "option fee", which he describes as "a Harberger-style tax in which you periodically pay a percentage of the price you claim"; in the usual form of such a tax, the declared value is also a price at which anyone may buy the asset (Posner and Weyl 2017).
Agents also represent the diffuse public who would gain from a blocked project, and "Any coalition that vetoes must then reimburse that quantified loss", meaning the loss to that public as those agents estimate it.
He distinguishes "economic negotiations where willingness-to-pay determines outcomes" from "democratic negotiations where each person gets equal voting weight regardless of wealth", and says "Agents can seamlessly switch between these modes depending on the issue at stake".
In the democratic mode, agents could "participate in continuous liquid democracy", in which each voter may hand her vote to a delegate who may pass it on.
To the worry that agents will favour the rich he replies "Consider how a billionaire's phone today is no more powerful or effective than yours", and he proposes that governments or philanthropies fund baseline agents for those who cannot afford them, on the model of public defenders and school vouchers.

Krier does not say the state disappears, and he concedes a good deal.
He accepts that outcomes depend on who starts with the rights, because of wealth effects (what a person will pay depends on how rich she is, so who holds a right changes which outcome is efficient) and the endowment effect (people demand more to give up a thing than they would pay to acquire it).
On those starting rights he writes: "The machinery runs either way. What does change is who ends up richer, which is why the initial allocation of these rights is a constitutional choice, not a technicality."
Agents, he says, make that baseline "explicit, contestable, and cheap to renegotiate", and the right starting point is the rights "set up by centuries of jurisprudence", amended through democratic systems that agents can improve.
He acknowledges Acemoglu's (2003) argument that there is no political Coase theorem, summarizing it in his own words as "The sovereign can always renege", and answers it with transparency and with "automated governance": automated auditing, real-time monitoring of regulatory capture, automated dispute resolution.
He grants that "constant renegotiation is expensive even for AGI" and that some rules must be stable.
He keeps the state for contract enforcement, which he calls "a non-negotiable role for the state", for criminal law, and for prohibiting catastrophic risks such as engineered pandemics.
The state, in his summary, "transitions its role from 'central planner' to 'framework guarantor'"; the framework "doesn't do away with the state, and nor should it - it just makes it a lot leaner."
He describes the governance of agents as three nested layers: the law, enforced by the state; "the free market of different services, deployers, products, and providers"; and the individual principal.
Competition in the second layer is what keeps agents loyal: "in a competitive market with switching costs approaching zero, parasitic agents get quickly identified and abandoned."
And of the risk that enhanced coordination produces digital NIMBYism or lets minorities hold majorities hostage, he writes that "these are mechanism design and governance challenges, not fundamental obstacles."

The strongest version of his case runs as follows.
Mechanism design is a mature field with many constructive results.
If the problems left over are problems of mechanism design, then they are engineering problems, and engineering problems yield to effort, which cheap computation supplies in quantity.
The state that remains enforces rules but does not have to know anything about anyone's preferences, because the agents carry that knowledge into the market.
That is the sense in which the residual state is lean and a guarantor, and not a planner.

I disagree with two steps of this case: the claim that the remaining state need not know anyone's preferences, and the inference that what is left is engineering.
Mechanism design contains impossibility theorems as well as constructive results, and the impossibility theorems that bind here have known escape routes.
Each escape route requires an actor that can coerce and that maximizes welfare, and all but an open-ended subsidy also require knowledge of the distribution of preferences.
An actor that sets entitlements, taxes and compensation from statistical knowledge of the population is planning in a sense I make precise in the section on the regress.

## Setup, definitions and notation

There are $N$ principals, indexed by $i$.
Principal $i$ has a private type $\theta_i \in \Theta_i$, which is everything about $i$'s preferences that the others cannot observe.
Types are drawn from a prior distribution $F$ that is common knowledge: known to all, with everyone knowing that everyone knows it, and so on.
An outcome $x$ is chosen from a set $X$ of possible outcomes, and each principal may receive a money transfer $t_i$, negative when $i$ pays.
Principal $i$'s payoff is quasi-linear, meaning money enters additively and is valued the same by everyone:
$$u_i = v_i(x, \theta_i) + t_i .$$
First-best welfare is the largest total value achievable if everyone's type were public:
$$W^\ast(\theta) = \max_{x \in X} \sum_{i=1}^N v_i(x, \theta_i).$$

Each principal is represented by a selfish delegated agent: software that chooses messages and actions to maximize its principal's payoff $u_i$ and nothing else.
"Selfish" here means indifferent to other principals and perfectly loyal to its own.
I assume perfect loyalty throughout, which is the best case for Krier's proposal.
Agency slack, an agent serving its provider or itself at its principal's expense, would add to every loss below.

The price of one unit of computation is $c$ and the price of sending one bit is $\kappa$.
I take both to be positive and as small as anyone likes, $c,\kappa \to 0^+$.
The informational results below hold even at zero; the computational and contest results describe the limit.

A mechanism is a rule that maps the messages the agents send to an outcome and a set of transfers.
A mechanism is incentive compatible, in the Bayesian sense, if no agent expects to gain by misreporting its principal's type, averaging over the others' types and given that the others report truthfully; it is dominant-strategy incentive compatible if truth-telling is best whatever the others report.
It is individually rational, which I will also call voluntary, if every agent, knowing its own type, expects to do at least as well by taking part as by refusing; when the choice to take part is made before types are known, I call it ex-ante voluntary.
It is budget balanced if transfers sum to zero, so that no money enters from outside or leaves.
It is efficient if the outcome maximizes $\sum_i v_i$, that is, attains $W^\ast$.
By the revelation principle, any equilibrium outcome of any bargaining protocol can be reproduced by an incentive-compatible mechanism in which agents simply report their types, so an impossibility for such mechanisms is an impossibility for every protocol; Myerson and Satterthwaite (1983) use it in this way.

I use constitutional negotiation to mean bargaining over the rules themselves: who holds which entitlement, which mechanism aggregates reports, what a contract may say, and who decides cases nobody foresaw.
Buchanan and Tullock (1962) draw the same line between constitutional and post-constitutional choice.

Let $L$ be the expected shortfall of realized welfare from first best, $\mathbb E[W^\ast(\theta)]$ minus expected realized welfare.
I attribute it to four causes, taken in order:

1. $L_{\text{friction}}(c,\kappa)$, the cost of search, drafting and messaging, which scales directly with $c$ and $\kappa$ and tends to zero with them;
2. $L_{\text{info}}(N)$, the loss that would remain with friction removed and computation unlimited, forced by incentive compatibility when types are private;
3. $L_{\text{comp}}(c,\kappa; m, N, k)$, the further loss from being unable to compute or communicate the efficient outcome, where $m$ is the number of distinct items or rights being allocated and $k$ the number of binary contingencies a contract can condition on;
4. $L_{\text{contest}}(N, r, V)$, the value of resources spent on gaining bargaining advantage over a contested surplus $V$, with $r$ defined in the section on contests.

Because each term is the extra loss once the previous causes are accounted for, the four sum to $L$ by construction, but the split depends on the order, and I do not claim the causes are separable in general.
Krier's argument treats $L$ as though it were $L_{\text{friction}}$.

| Symbol | Meaning |
|---|---|
| $N$ | number of parties a decision affects (in the double auction, the number on each side; in the developer case, the number of households, the developer being a further party) |
| $\theta_i$, $\Theta_i$, $\lvert\Theta\rvert$ | private type of principal $i$, its set of possible types, and the number of types when all sets are the same size |
| $F$ | prior distribution of types; for one-dimensional types, its distribution function |
| $\mu$ | mean of a one-dimensional type, $\mathbb E[\theta_i]$ |
| $\theta_{\min}$, $\theta_{\max}$ | lowest and highest possible type |
| $\hat\theta_i$ | type reported by agent $i$ |
| $\langle\theta\rangle_N$ | average type, $\frac1N\sum_i\theta_i$ |
| $x$, $X$ | outcome, and set of possible outcomes |
| $v_i(x,\theta_i)$ | value to principal $i$ of outcome $x$ |
| $t_i$ | money transfer to principal $i$ |
| $u_i$, $\bar u_i$ | payoff of principal $i$, and its payoff from refusing to take part |
| $W^\ast(\theta)$ | first-best welfare |
| $c$, $\kappa$ | price of one unit of computation, and of sending one bit |
| $L$ | expected shortfall from first-best welfare |
| $m$, $m_0$ | number of distinct items or rights, and the number before contingencies are added |
| $k$ | number of binary contingencies a contract can condition on |
| $n$ | number of possible trades in a long-term contract (distinct from $N$) |
| $A$ | set of actions a contract can specify |
| $B$ | budget of bits |
| $V$ | value of the project to the developer; in the contest, the contested surplus |
| $b$ | value to the truck or the factory of permission to proceed |
| $G$, $g$ | distribution function and density of $b$ |
| $s$ | harm to the single resident in the two-party case |
| $d$ | the difference $b - s$ |
| $h_i$, $H$ | harm to resident $i$, and total harm $\sum_i h_i$ |
| $p$ | per-household price posted by the developer |
| $p_i$, $P$ | price posted by resident $i$, and total price $\sum_i p_i$ |
| $\alpha_i$ | partner $i$'s ownership share |
| $\sigma_i$, $\sigma_i'$ | the advocate's signal about $\theta_i$, and a more informative one |
| $r$ | decisiveness of a contest: how steeply share responds to relative spending |
| $e_i$, $Z$ | computation bought by party $i$ in a contest, and $\sum_j e_j^{\,r}$ |
| $w_i$ | party $i$'s budget for a contest |
| $q$ | probability that an attempted commitment succeeds |

## Informational costs

This section concerns $L_{\text{info}}$.
Everything in it holds with $c = \kappa = 0$, so no fall in the price of computation or messaging touches these losses.
As $N$ grows, private information matters less and less for the exchange of private goods, which one person consumes to the exclusion of others, in thick markets, which have many buyers and many sellers.
It matters more and more for single decisions that bind many parties at once.
Externalities are decisions of the second kind.

### The truck and one resident

Start with two parties: Krier's truck and a single resident who holds the right to a clean street.
Call the resident the seller, whose cost $s$ is the harm a trip does her, and the truck the buyer, whose value $b$ is what permission is worth to it.
Each knows only its own number; $s$ and $b$ are independent and their supports overlap.
Myerson and Satterthwaite (1983) prove that no mechanism is at once incentive compatible, individually rational, budget balanced and efficient in this setting.
Some trades worth making will not be made, whatever protocol the agents use and however cheaply they run it.

The size of the loss is easy to compute in the textbook case where $s$ and $b$ are both uniform on $[0,1]$.
The derivation is mine.
First-best gains are $\mathbb E[(b-s)^+]$.
The difference $d = b - s$ has density $1 - d$ on $[0,1]$, so
$$\mathbb E[(b-s)^+] = \int_0^1 d\,(1-d)\,\mathrm d d = \tfrac12 - \tfrac13 = \tfrac16 .$$
The mechanism that maximizes expected gains subject to the other three properties trades only when $b \ge s + 1/4$ (Myerson and Satterthwaite 1983).
It coincides with the linear equilibrium of the double auction studied by Chatterjee and Samuelson (1983), in which each side names a price and trade happens at the midpoint if the buyer's price exceeds the seller's.
It realizes
$$\int_{1/4}^1 d\,(1-d)\,\mathrm d d = \tfrac16 - \left(\tfrac1{32} - \tfrac1{192}\right) = \tfrac{27}{192} = \tfrac{9}{64},$$
a fraction $\tfrac{9/64}{1/6} = \tfrac{27}{32} \approx 0.84$ of first best, so the informational loss is $5/32$ of the available gains, about a sixth.

The loss can be eliminated with money from outside.
The Vickrey–Clarke–Groves mechanism pays each party the total value the others receive at the chosen outcome, less a term its own report cannot affect.
Here it makes the truck pay the reported $s$ and the resident receive the reported $b$, which is efficient, truthful and voluntary, but on every trade it pays out $b - s$ more than it collects.
Its expected deficit is the entire first-best surplus, $1/6$ per pair, and someone outside the bargain has to cover it.

### The developer and the homeowners

Now let one decision require the agreement of many parties.
Mailath and Postlewaite (1990) study a yes-or-no decision, such as whether to provide a public good, in which all must agree, each of $N$ agents has a private value for "yes", positive or negative, and values are independent across agents.
They prove, under further conditions they describe as very mild, that as $N$ increases "the probability of an affirmative efficient decision goes to zero" for any mechanism that is incentive compatible, individually rational and budget balanced.
In their public-good version the cost per person stays fixed as the group grows, so the result is not an artefact of a project that becomes trivially cheap or impossibly dear.
They also give an example in which it is common knowledge that going ahead is efficient and yet the probability of going ahead tends to zero.
Everyone knows the total gain is positive, but nobody knows who should bear how much of the cost, and every voluntary rule for sharing it gives each party a reason to understate its own gain.

These are Krier's developer and his factory.
The mapping is mine.
Take the developer's value $V$ as known and imagine it shared equally among the households as a baseline, so that household $i$'s net value for approval is $V/N - \theta_i$, positive for some households and negative for others, and independent across households.
This is their public-good problem with the sign reversed, a payment to be shared in place of a cost.
The condition that neither answer is obvious is $\theta_{\min} < V/N < \theta_{\max}$, with $V/N$ held fixed as $N$ grows.
When, in addition, $V/N$ exceeds the mean minimum, so that approval is efficient with probability tending to one, the theorem says that voluntary bargaining without outside money fails to approve projects that should go ahead, with probability tending to one.
If $V$ is private as well, the setting is that of Rob (1989), who obtains the same limit for a firm compensating $N$ residents with private damages.

An intuition, offered as intuition: a mechanism can extract from agent $i$ no more than the size of $i$'s stake times the difference $i$'s report makes to the decision.
With $N$ independent agents, the average influence of any one of them on a single decision falls like $N^{-1/2}$, a scaling that Al-Najjar and Smorodinsky (2000) make precise for pivotal players.
With stakes per person bounded, total collectable contributions grow like $N \cdot N^{-1/2} = \sqrt N$, while with fixed cost per person the amount to be covered grows like $N$.
So only a share of order $N^{-1/2}$ of what is needed can be raised; the theorem supplies no constant, but for 10,000 households the order of magnitude is one per cent.

Reversing the entitlement does not help.
If the factory holds the right to pollute, the residents must jointly pay it to abate, and abatement is a public good for them: the same theorem applies, with free-riding in place of holding out.

Under complete information, where everyone's values are known to everyone, voluntary participation causes a similar failure.
Dixit and Olson (2000) show that when joining the bargain is voluntary, the efficient equilibrium does not survive even very small transaction costs, and the remedy they outline is coercive, in effect removing the option of staying out.
Ellingsen and Paltseva (2016) show that with more than two players there are situations in which every equilibrium in the class they study under-provides public goods, because players strategically abstain from contracting.

### Exchange in thick markets is different

In a double auction with $N$ buyers and $N$ sellers of a private good, Rustichini, Satterthwaite and Williams (1994) show that the amount by which traders misreport shrinks like $1/N$ and the efficiency loss like $1/N^2$.
Each trader's report barely moves the market price, so the incentive to shade disappears as the market thickens.
For rival, excludable goods, where one person's use prevents another's and non-payers can be shut out, private information therefore costs less as $N$ grows.
For a single decision that binds $N$ parties, it costs more.

### The bargaining club

The derivation is mine.
Members report minimum acceptable payments $\hat\theta_i$; true minima $\theta_i$ are independent with distribution function $F$ on $[\theta_{\min}, \theta_{\max}]$ and mean $\mu$; the developer values the project at $V$.
The efficient rule is to go ahead if and only if $\sum_i \theta_i \le V$, that is, if and only if the average minimum $\frac1N\sum_i\theta_i$ is at most $V/N$.
The phrase "common clearing price" can be read in three ways, and each reading gives up at least one of the properties Krier claims.

On the first reading, the price does not depend on the reports.
The developer posts a per-household price $p$, and the project goes ahead only if every member accepts.
Truth-telling is then a dominant strategy, as Krier says: a member should accept if and only if $\theta_i \le p$.
But the developer will pay at most $V$, so $p \le V/N$, and the project goes ahead if and only if $\max_i \theta_i \le p$, which happens with probability
$$\Pr\left(\max_i \theta_i \le p\right) = F(p)^N \le F(V/N)^N .$$
Suppose $\mu < V/N < \theta_{\max}$, so that the project is worth doing on average but not every household would accept $V/N$.
Holding $V/N$ fixed as $N$ grows, by the law of large numbers the efficient rule approves with probability tending to one, while $F(V/N) < 1$ and the posted-price rule approves with probability tending to zero, geometrically in $N$.
The rule approves the project when the most reluctant member is satisfied, whereas efficiency asks whether the members are satisfied on average.

On the second reading, the price is computed from the reports so that all members consent, for example $p = \max_i \hat\theta_i$.
Then whoever reports highest sets everyone's payment, and padding does raise that member's check, up to the point where the developer walks away.
Truthfulness is lost, and so is efficiency, since even with truthful reports the project goes ahead only if $N \max_i \hat\theta_i \le V$.
The general fact behind this is that, when preferences can be anything within a broad class, the only efficient mechanisms with dominant-strategy truth-telling are Groves mechanisms, the family to which the Vickrey–Clarke–Groves mechanism belongs, and these do not balance the budget (Green and Laffont 1979; Holmström 1979).

On the third reading, the club binds its dissenters.
Once dissent can be overridden, an efficient rule exists: the expected-externality mechanism described below, which pays members different amounts.
A simpler, approximately efficient one, worked through at the end of the section on the regress, pays every member the mean minimum $\mu$.
Either way, a member whose minimum exceeds her payment is compelled to accept it, which is compulsory purchase (in American usage, eminent domain).
"Without surrendering property rights" is lost.

Joining such a club before knowing one's own type can be ex-ante voluntary, a point I return to below.
Joining after one knows one's type is not, for members with high types.

### Posted prices by many rights-holders

When a buyer needs one permission from each of several sellers, each seller's markup raises the total price the others face, so the sellers together charge more than a single seller would.
This is Cournot's (1838) problem of complementary monopolies.
Here $N$ is the number of independent rights-holders whose permission is each required.
Krier's truck, which can go round, is the case where the result has least force, because competition between routes disciplines the total price.
The result applies in full to a delivery that must reach the street, and to the factory, which needs every resident's permission and cannot be routed round.

The derivation is mine.
Let the buyer's value $b$ for permission be private, with distribution function $G$ and density $g$.
Resident $i$ suffers harm $h_i$ and posts price $p_i$; the total price is $P = \sum_i p_i$ and the total harm $H = \sum_i h_i$.
Assume, generously, that residents know one another's harms, so that only the buyer's value is private.
The buyer proceeds if $b \ge P$, which happens with probability $1 - G(P)$, and the efficient rule is to proceed when $b \ge H$.
Resident $i$ chooses $p_i$ to maximize $(p_i - h_i)(1 - G(P))$.
The first-order condition is
$$1 - G(P) - (p_i - h_i)\, g(P) = 0 \quad\Longrightarrow\quad p_i - h_i = \frac{1 - G(P)}{g(P)} ,$$
and summing over $i$ we get
$$P - H = N\,\frac{1 - G(P)}{g(P)} .$$
The total markup over true harm is $N$ times the inverse hazard rate of the buyer's value.

Measure money in units of the largest possible value of $b$, and let $b$ be uniform on $[0,1]$ with $H < 1$.
The condition becomes $P - H = N(1 - P)$, so
$$P = \frac{H + N}{N + 1}, \qquad 1 - P = \frac{1 - H}{N + 1} .$$
The buyer proceeds with probability $(1-H)/(N+1)$ against the efficient $1 - H$: realized trades are a fraction $1/(N+1)$ of efficient ones.
For the factory and 10,000 residents posting separately, that fraction is $1/10{,}001$.

Krier's flash coalition is a good answer to this.
A coalition that sets one price for all its members is a single seller, so its markup is one inverse hazard rate, and in the uniform case it lets through half the efficient projects.
Two problems remain.
Half the efficient projects are still lost.
And joining the coalition is voluntary, so a resident can do better by staying out and posting her own price.
The derivation is mine.
Suppose the coalition first compensates each member's harm and then shares the markup equally.
In the uniform case, an outsider facing the coalition is one of two complementary sellers, each with markup $(1-H)/3$ and probability of trade $(1-H)/3$, so she earns $(1-H)^2/9$; a member of the full coalition earns an equal share $(1-H)^2/(4N)$ of the coalition's profit, which is less for every $N \ge 3$.
This is the free-riding on participation that Dixit and Olson (2000) and Ellingsen and Paltseva (2016) analyze.
Buchanan and Yoon (2000) call the underlying structure the anticommons: many holders of complementary vetoes underuse a resource in the way that many users of an open-access resource overuse it.

Krier writes that "the externality doesn't vanish, but it does get a price tag. And once a cost is made clear, the marvel of the market can solve it."
Arrow (1969) explains why pricing an externality is not the same as having a competitive market in it.
He observed that a complete set of markets for externalities needs one commodity for each pair of affected person and acting person, for each kind of action, so of order $N^2$ markets per kind of action, and each has one buyer and one seller, so nobody in them takes prices as given.
The factory example has this structure: each resident is the sole seller of a right the factory must buy.

### What restores efficiency

Two classical mechanisms reach efficiency under private information, and each gives up one property.
In the expected-externality mechanism (d'Aspremont and Gérard-Varet 1979; Arrow 1979), each agent receives the expected effect of its report on the others' values, financed by charging the others equal shares, so payments sum to zero.
It is incentive compatible in the Bayesian sense, efficient and budget balanced for any $N$ when types are independent.
It fails individual rationality: some types would rather not take part, and must be bound.
The Vickrey–Clarke–Groves mechanism is truthful, voluntary and efficient, and fails budget balance; in the cases above, the shortfall must come from outside.
It needs no knowledge of $F$, only an authority that can tax to fund the deficit, which in the two-party case is the whole surplus.
The subsidy can be milked by agents who collude, and cheap contracting between agents is the essay's premise.
The derivation is mine.
In the two-party uniform case the truck and the resident can agree to report $b = 1$ and $s = 0$ whatever their true values; the truck then pays $0$, the resident receives $1$, and the pair collect a subsidy of $1$ on every encounter, six times the first-best gain of $1/6$.
That this mechanism is vulnerable to collusion is well known (Ausubel and Milgrom 2006), and budgeting or policing the subsidy needs knowledge of $F$.

So under private information the efficient outcome can be reached only if some actor can do at least one of three things: bind types who would refuse, inject money from outside, which in a polity must be raised by taxation, or redraw the entitlements.

### Entitlements decide feasibility as well as distribution

Krier writes that the machinery "runs either way" and that the initial allocation only decides "who ends up richer".
When types are private, a theorem contradicts this.

Cramton, Gibbons and Klemperer (1987) study $N$ partners who hold shares $\alpha_1, \dots, \alpha_N$ of an asset whose values to them are private and independent with a common distribution.
An efficient, incentive-compatible, voluntary and budget-balanced reallocation exists if and only if the shares are close enough to equal.
With two partners and one owning everything, the problem is the seller and buyer of the truck example, where no such mechanism exists.
Segal and Whinston (2011, 2016) generalize the point: whether efficient voluntary bargaining is possible depends on the status-quo allocation of rights, and the allocations that work are typically shared or probabilistic rights, such as joint ownership in equal shares or a right each party holds with probability one half, and not simple rights in which one party holds the entire entitlement.

So for some assignments of entitlements no efficient voluntary machinery exists, and the initial allocation decides whether the machinery works as well as who gains from it.
Choosing an assignment that does work requires knowing the distribution $F$ of preferences.
My reading of Krier's proposed default, inherited jurisprudence, is that it mostly assigns property rules in the sense of Calabresi and Melamed (1972), entitlements whose holder may refuse to sell at any price, held all-to-one, which is the least favourable case.

### Better-informed advocates make fewer rules acceptable

The expected-externality mechanism is ex-ante voluntary: agents who commit to it before they learn their types expect to gain.
That is Buchanan and Tullock's constitutional stage, and the logic of choosing rules behind a veil of ignorance.
Krier's advocate, though, "could also develop an increasingly sophisticated (though never perfect) model of who you are".

The derivation is mine.
Let agent $i$ hold a signal $\sigma_i$ about $\theta_i$ at the moment it decides whether to join a mechanism, and let $\bar u_i$ be its payoff from staying out.
Assume the mechanism's outcome and the outside option depend on the signal only through the type and the reports, and that the agent's reports do not depend on which signal it held when it joined, for instance because it learns $\theta_i$ before it reports.
Voluntary participation requires
$$\mathbb E[u_i - \bar u_i \mid \sigma_i] \ge 0 \quad \text{for every value of } \sigma_i .$$
Suppose a better advocate holds a more informative signal $\sigma_i'$, in the sense of Blackwell (1953) that $\sigma_i$ is a noisy function of $\sigma_i'$ carrying no information about $\theta_i$ beyond what $\sigma_i'$ does.
Then by the tower property
$$\mathbb E[u_i - \bar u_i \mid \sigma_i] = \mathbb E\big[\,\mathbb E[u_i - \bar u_i \mid \sigma_i']\;\big|\; \sigma_i\big],$$
so each coarse constraint is an average of fine ones.
If every fine constraint holds, every coarse one does; the converse fails.
The set of mechanisms that remain voluntary can only shrink as the signal improves.

The better an advocate knows its principal at the constitutional moment, the fewer constitutions can be agreed voluntarily.
The logic is Hirshleifer's (1971): information that arrives before trading destroys trades that would have insured against it.

### Correlated types

If types are correlated and the designer knows their joint distribution, Crémer and McLean (1988) show that efficiency with voluntary participation is achievable for all but a negligible set of joint distributions, by making each agent's transfers depend on side-bets against the others' reports.
Agents with rich data make correlation plausible, but the construction needs a designer who knows $F$ without error and can impose arbitrarily large penalties, and it fails under small errors in the assumed distribution, which is the motivation for robust mechanism design (Bergemann and Morris 2005).
The exception is consistent with the conclusion of this section: efficiency becomes possible once a powerful and well-informed designer is present.

## Communication and computation

This section concerns $L_{\text{comp}}$.
Its results bind a planner and a market equally, because they are properties of the allocation problem and not of the institution solving it, so they are not an argument for planning.
They show two things.
Cheaper computation does not dissolve them, because a fall in price adds only logarithmically to the size of problem that can be solved, while granularity multiplies the size of the problem posed.
And the only general way to make the problems tractable is to restrict what may be bid for and what contracts may say: requiring substitutes, separable states, a checkable contract language, a menu of permitted coalitions.
Someone has to choose the restriction, and the choice decides whose preferences can be expressed.
Most of the results are worst-case; I take up whether that matters in the section on objections.

### Bits

Take the developer assembling $m$ plots, or any allocation of $m$ indivisible items among agents whose valuations over bundles of items are arbitrary.
Nisan and Segal (2006) show that with two agents, any protocol that finds an efficient allocation must, in the worst case, exchange at least
$$\binom{m}{m/2} \approx 2^m \sqrt{\frac{2}{\pi m}}$$
bits.
With $N$ agents, even improving on a fraction $1/N$ of the best achievable welfare requires a number of bits exponential in $m/N^2$, up to a factor polynomial in $N$.
The bound holds even for a protocol that is handed a candidate answer and only has to check it.
It therefore also bounds the size of any set of prices at which every agent prefers its assigned bundle to any other, which in general needs one price per bundle per agent.

The derivation is mine.
The bit budget $B$ is the amount spent on communication divided by $\kappa$.
The largest fully general two-agent problem that can be solved exactly satisfies $B \approx 2^m\sqrt{2/(\pi m)}$, so
$$m \approx \log_2 B + \tfrac12 \log_2\!\left(\frac{\pi m}{2}\right).$$
A thousandfold fall in $\kappa$ multiplies $B$ by a thousand and so adds $\log_2 1000 \approx 10$ items.
Hyper-granular contracting multiplies $m$ instead: each new binary distinction, weekday against weekend, peak against off-peak, doubles the rights in play, so $k$ distinctions applied to $m_0$ base rights give $m = m_0 2^k$, and the bits needed grow like $2^{m_0 2^k}$.
Once $m_0 > 10$, the ten items bought by a thousandfold fall in $\kappa$ are fewer than one extra binary distinction adds.

Preferences that are separable across states of the world can be handled state by state, and then the bound applies only to the rights that interact within a state.
My judgement is that a Saturday-noise right and a Sunday-noise right are separable for most people, and that the plots in a development are not.

### When simple prices exist

One price per item is guaranteed to support an efficient allocation when valuations are gross substitutes, meaning that raising the price of one item never lowers demand for another (Kelso and Crawford 1982).
Gul and Stacchetti (1999) show that this is essentially the largest class of valuations for which the guarantee holds.
Externality bargains are typically complements: a delivery needs permission for every street on its way, and a development needs every plot and every consent.

### Winner determination

Choosing the welfare-maximizing allocation from bids on bundles of items, the winner determination problem, is NP-hard (Rothkopf, Pekeč and Harstad 1998): no algorithm is known that solves every instance in time polynomial in the number of bids.
Unless P = NP, no polynomial-time algorithm can even guarantee a fraction larger than $m^{-(1/2-\epsilon)}$ of the optimal welfare, for any $\epsilon > 0$ (Sandholm 2002; Lehmann, O'Callaghan and Shoham 2002).
Structured instances are solved routinely, and the developer's problem may be one of them.
What the result excludes is that a fall in $c$ closes the gap in general, since exact methods take time exponential in $m$ on hard instances.
Approximation also costs truthfulness: the Vickrey–Clarke–Groves mechanism is truthful only if its allocation is exactly optimal, and with an approximate optimizer agents can gain by misreporting (Nisan and Ronen 2007).

### Coalitions

Krier's 10,000 residents form their coalition "in a nanosecond", and the coalition he describes includes all of them.
Residents' harms differ, and those whose harms are well above or below the average would do better bargaining as a separate group, so the full coalition has to be stable against every sub-group that could break away.
$N$ agents can form $2^N - 1$ non-empty coalitions, and the number of ways to partition them into coalitions, called the Bell number, grows faster than $a^N$ for every fixed $a$.

The core of a bargaining game is the set of divisions of the payoff that no coalition can improve on for its own members.
Aivazian and Callen (1981) give a three-party externality example in which the core is empty, so that every agreement is undone by some coalition and Coasean bargaining cycles without settling.
For games described by a formula whose size grows polynomially with the number of players, in place of a full table of coalition values, deciding whether the core is empty is NP-complete (Deng and Papadimitriou 1994; Conitzer and Sandholm 2006).
Speed does not help where the core is empty: faster agents find a blocking coalition sooner, and every agreement has one.

### Correlated equilibrium needs a correlator

A correlated equilibrium (Aumann 1974) is defined relative to a source of signals that every player trusts, which privately recommends an action to each player such that no player gains by deviating from its recommendation.
Cryptography can replace the trusted source for the correlation itself (Dodis, Halevi and Rabin 2000).
It cannot replace the selection.
A game generally has many correlated equilibria that divide the payoffs differently, and whoever designs the signal chooses among them, so Krier's "shared signals and contracts" carry a choice of who gains.

### Contracts

A complete contingent contract over $k$ binary verifiable conditions is a function from $\{0,1\}^k$ to a set of actions $A$.
There are $|A|^{2^k}$ such functions, so writing down a typical one takes $2^k \log_2 |A|$ bits.
For two actions, Shannon (1949) showed that almost all such functions need circuits with at least about $2^k/k$ gates.
The contracts people actually want are far more compressible than typical ones.
The compression is where disputes arise, though: a short contract is a rule plus an interpreter, and the interpreter decides the cases the rule does not spell out.

Rice's theorem (Rice 1953) says that no algorithm can decide, for every program, any non-trivial property of what the program does.
A contract language in which compliance can always be checked mechanically must therefore be a restricted language, or disputes need a judge with discretion.
Krier's "near-instantaneous computational verification" is available for contracts written in a language narrow enough to be checked.

Segal (1999) shows that when there are $n$ possible trades, of which one will turn out to be efficient, and renegotiation cannot be prevented, the value of any long-term contract converges to the value of no contract as $n \to \infty$.
Greater granularity means larger $n$.

Incomplete contracts leave residual control rights: someone decides what happens in the cases the contract does not cover (Grossman and Hart 1986; Hart and Moore 1988, 1999).
My reading is that in a constitution the holder of residual control is the sovereign.
Maskin and Tirole (1999) argue in the other direction that contingencies which cannot be described are irrelevant if the parties can foresee their payoffs and can commit not to renegotiate; my reading is that such a commitment needs an enforcer outside the parties.

## Costs that do not fall, and one that rises, as computation gets cheap

This section concerns $L_{\text{contest}}$, and a related loss from impasse that rises as agents improve.

### Bargaining as a contest

The derivation is mine.
It rests on an assumption: a party's share of a contested surplus $V$ increases with the computation it spends relative to its rivals.
There is early evidence that the relative quality of agents moves outcomes.
Zhu et al. (2025) find that when consumers and merchants both delegate to language-model agents, different agents secure significantly different deals for their users.
Vaccaro et al. (2025) report a competition covering about 180,000 automated negotiations, in which how an agent was instructed was strongly associated with how much value it claimed.

In the contest form of Tullock (1980), party $i$ buys $e_i$ units of computation at price $c$ and receives the share $e_i^{\,r} / Z$ of $V$, where $Z = \sum_j e_j^{\,r}$ and $r > 0$ is the contest's decisiveness, how steeply share responds to relative spending.
Party $i$ maximizes $V e_i^{\,r}/Z - c e_i$, with first-order condition
$$\frac{V r e_i^{\,r-1}(Z - e_i^{\,r})}{Z^2} = c .$$
At a symmetric equilibrium $Z = N e^{r}$, which gives $V r (N-1)/(N^2 e) = c$, so
$$e^\ast = \frac{r(N-1)V}{N^2 c}, \qquad c N e^\ast = r\,\frac{N-1}{N}\,V .$$
A necessary condition for this to be an equilibrium, and the standard condition for the symmetric pure-strategy equilibrium, is that each party's expected payoff $V/N - c e^\ast$ be non-negative, which holds when $r \le N/(N-1)$.

Total spending does not contain $c$.
Halving the price of computation doubles the computation each party buys and leaves the share of surplus dissipated unchanged.
With $r = 1$ and two parties, half the surplus is spent fighting over it.
The value of $r$ for agent bargaining is unknown; the claim is the invariance to $c$, not the level.

Krier's "$10,000 in legal fees" sentence is therefore right about one part of legal work and wrong about the other.
The part that is not rival, drafting and search, does fall to pennies.
The part that is rival, out-arguing the other side, stays a fixed share of the stakes, because each side's spending responds to the other's.
If instead every party's budget $w_i$ binds, then $e_i = w_i / c$, and party $i$'s share is
$$\frac{(w_i/c)^{r}}{\sum_j (w_j/c)^{r}} = \frac{w_i^{\,r}}{\sum_j w_j^{\,r}},$$
which does not contain $c$ either: shares follow budgets however cheap computation becomes.
And because equilibrium money spending per party, $r(N-1)V/N^2$, does not depend on $c$, whether a budget binds does not depend on $c$ either.
A billionaire's phone is no better than anyone else's, as Krier says, but the computation his agent can buy is.
Sharp et al. (2025) argue at length that agents will reproduce and widen inequality, and the contest model gives one reason this does not wash out as computation gets cheaper.

### Over-complete contracts

Tirole (2009) models contracting when thinking about contingencies is costly, and calls that thinking cognition.
Part of what it buys is protection against, or advantage over, the counterparty, and contracts can then be too complete from the standpoint of joint surplus, with cognition spent on transferring rents.
Cheaper cognition means more contingencies examined for this purpose.

### Cheap commitment produces impasse

A delegated agent with a fixed mandate is a commitment device in Schelling's (1960) sense: a negotiator who cannot concede gains leverage.
Ellingsen and Miettinen (2008) study bilateral bargaining in which each side can attempt, at a small positive cost, to commit to a demand, and an attempt succeeds with probability $q < 1$.
Each side tries to commit to a demand that leaves the other little, and when both succeed the demands are incompatible.
They show that the unique outcome surviving iterated elimination of strictly dominated strategies involves conflict with probability $q^2$.
As agents make commitment more reliable, $q$ rises and the probability of impasse $q^2$ rises with it.
Krier's own coalition example ends with the word "non-negotiable".
Petel (2025) raises the neighbouring problem of threats and extortion in bargaining between agents.

## The democratic mode

Deciding whether an issue goes to the price mode or the vote mode largely decides its outcome: the same pollution permit may be bought by a factory under willingness to pay and refused under one person one vote.
To "seamlessly switch" between modes is to make a constitutional choice, and someone has to make it.

Within the vote mode, Gibbard (1973) and Satterthwaite (1975) prove that with three or more alternatives, every voting rule that is not dictatorial can be manipulated by some voter misreporting her preferences.
Bartholdi, Tovey and Trick (1989) proposed that computational hardness might protect elections from manipulation.
That protection is a worst-case bound, like the bound on winner determination, and in both cases typical instances may be easy.
Easy typical instances help a manipulator as much as an allocator, so cheap computation weakens the shield in the same way that it helps the solver.
For liquid democracy, Kahng, Mackenzie and Procaccia (2021) model voters who know only the competence of their neighbours, and show that delegation rules using only such local information cannot be guaranteed to improve on direct voting at finding a correct answer, and can do worse.

## The regress and what stops it

The argument of this section is mine and rests on no theorem.
Each remedy identified above is a choice from a menu: the assignment of entitlements, the mechanism, the permitted contract language, the correlating signal, a tax rate, the source of a subsidy, the holder of residual decisions.
Different choices give different parties more.
Any proposed change from the status-quo rules to an alternative is a yes-or-no decision over which every party has a veto, if rules are changed only by unanimous agreement, and a private stake in the outcome.
That is the setting of the Mailath–Postlewaite theorem, applied to each proposed reform in turn, and so far as the stakes are independent and do not shrink per person as the polity grows, the theorem says such reforms will rarely pass when they should.
A negotiation over the rules of that negotiation has the same form.
The sequence stops only at rules that were not chosen by unanimous bargaining among informed parties: rules imposed, inherited, or adopted behind a veil that well-informed agents no longer have.

Hurwicz (2008) poses this as the question of who will guard the guardians.
His answer is that the regress can stop, either through "intervenors", actors who uphold the rules for reasons other than their own payoff, or through arrangements in which self-interest happens to enforce the rules.
He does not claim the regress must fail.
Aghion and Bolton (2003) show that when the social contract is incomplete, the constitution that is optimal before anyone knows their position is not unanimity: it lets a majority bind a minority.
Krier himself stops the regress at centuries of jurisprudence plus improved democratic institutions, which is a state.

### What it must be able to do

The remedies require powers of a specific kind: to bind non-consenting parties, to tax, to assign and reassign entitlements, to forbid renegotiation, to fix the language in which contracts and bids are written, to choose which equilibrium is played, and to decide uncontracted cases.
The guardrails in Krier's essay already use these powers.
A Harberger tax is a compulsory levy on a self-declared value combined with a forced sale at that value (Posner and Weyl 2017), and it cannot be voluntary, since its point is that the owner cannot refuse a buyer who meets the declared price.
"Any coalition that vetoes must then reimburse that quantified loss" is a liability rule in the sense of Calabresi and Melamed (1972): someone other than the holder of the entitlement sets its price and compels the transfer.
Letting "verified emergencies" through at zero price needs a verifier whose verdict binds.
Agent vouchers could come from philanthropy, as Krier allows, but a right to an agent that does not depend on a donor's goodwill needs a tax base.
So the institutions in the essay are not voluntary in the sense its argument requires.

### What it must know

Assigning entitlements that make efficient bargaining feasible, setting a Harberger rate (whose efficient level depends on how often assets turn over and how investment responds to the tax), quantifying the diffuse loss that a vetoing coalition must reimburse, and choosing the mechanism all require the distribution $F$ of preferences; only the open-ended subsidy does not, and it has the weakness just described.
Choosing the mechanism is itself hard: given finite type spaces and a prior, finding the deterministic mechanism that best serves the designer's expected objective under that prior is NP-complete, even with a single agent (Conitzer and Sandholm 2002), and the prior over type profiles has $|\Theta|^N$ entries when each agent has $|\Theta|$ possible types.

Whether knowing $F$ makes the actor a planner needs argument, and there is a gap to concede.
Hayek's knowledge of time and place is knowledge of particulars, and knowing the distribution $F$ is weaker than knowing each $\theta_i$.
I use "planner" for an actor that sets entitlements, tax rates, compensation schedules and permitted contract forms from statistical knowledge of the population, and three things make the job planning in that sense.
First, these are the things planning agencies set.
Second, $F$ is needed separately for each class of decision at the granularity of the mechanism, per neighbourhood and per kind of nuisance, so hyper-granular contracting needs a hyper-granular $F$.
Third, errors in $F$ produce the failures Krier attributes to planners: entitlements that do not permit efficient bargaining, tax rates that deter investment, compensation that over- or under-pays.
Agents may make $F$ cheaper to estimate, which helps whoever holds the job.

### What it must want

The same powers, held by an actor that maximizes its own payoff, are used differently.
Myerson (1981) shows that a revenue-maximizing seller trades only when the buyer's virtual value $b - (1 - G(b))/g(b)$ is non-negative, and so excludes some efficient trades.
In the uniform bilateral example, a profit-maximizing intermediary, the broker of Myerson and Satterthwaite (1983), trades only when the buyer's virtual value $2b - 1$ exceeds the seller's virtual cost, which is the seller's cost plus the ratio of its distribution function to its density, here $2s$.
Trade then requires $b - s \ge 1/2$.
The derivation is mine.
The realized gains are
$$\int_{1/2}^1 d\,(1-d)\,\mathrm d d = \tfrac16 - \left(\tfrac18 - \tfrac1{24}\right) = \tfrac1{12},$$
half of first best, against $27/32$ of first best with a designer maximizing expected gains subject to budget balance and voluntariness, and all of it with a benevolent subsidizer.

The agent providers in Krier's second layer are candidate intermediaries of this kind.
His answer is competition with low switching costs.
That works where providers are substitutes, so that a customer can leave one for another.
A mechanism for a public decision has to include everyone affected by that decision, and the air over a region cannot be divided between competing clearing-houses.
Brennan and Buchanan's Leviathan and Acemoglu's (2003) commitment problem, which Krier cites, are the standing reasons not to assume that the actor holding these powers is benevolent.
Transparency raises the cost of abusing the powers, but the objective of whoever holds them stays what it was.

### The developer and 10,000 homeowners, with a leviathan

The derivation is mine.
Return to the developer, now facing $N = 10{,}000$ households whose minimum acceptable payments $\theta_i$ are independent with mean $\mu$ and variance $\operatorname{Var}(\theta_i)$.
Consider the rule: approve the project if and only if $V \ge N\mu$, and pay every household $\mu$.
No household's report is used, so there is nothing to misreport.
The developer can be offered approval at total price $N\mu$, and accepting is in its interest if and only if $V \ge N\mu$.

The efficient rule approves if and only if $V/N \ge \langle\theta\rangle_N$, where $\langle\theta\rangle_N = \frac1N\sum_i\theta_i$ is the average minimum.
The two rules disagree only when $V/N$ lies between $\mu$ and $\langle\theta\rangle_N$.
If the blunt rule approves wrongly, the loss is $\sum_i\theta_i - V \le N(\langle\theta\rangle_N - \mu)$, since $V \ge N\mu$; if it rejects wrongly, the loss is $V - \sum_i\theta_i \le N(\mu - \langle\theta\rangle_N)$.
In either case the loss is at most $N|\langle\theta\rangle_N - \mu|$, so
$$\mathbb E[\text{loss}] \le N\,\mathbb E|\langle\theta\rangle_N - \mu| \le N\sqrt{\operatorname{Var}(\langle\theta\rangle_N)} = N\sqrt{\operatorname{Var}(\theta_i)/N} = \sqrt{N\operatorname{Var}(\theta_i)},$$
using Jensen's inequality.
Against stakes of order $N$, the relative loss is of order $N^{-1/2}$.
The blunt rule gets better as $N$ grows, while voluntary bargaining, by the theorem of Mailath and Postlewaite, gets worse.

The rule needs three things.
It needs $\mu$, which is a fact about $F$.
It needs the power to bind the households whose $\theta_i > \mu$, who are made worse off: this is compulsory purchase at average harm.
And it needs an authority that does not want the difference for itself, since one that set the payment below $\mu$ and sold approvals would be the broker of the previous subsection.
This is what states already do, and it is the kind of "clumsy, one-size-fits-all" rule Krier wants to replace.
With the same power to bind and with knowledge of all of $F$, not only its mean, the expected-externality mechanism is efficient outright for any $N$; the flat rule is the version that uses no reports and only $\mu$.
What the example shows is that the remedy lies in the powers, and that the rule Krier calls clumsy is their simplest use.

The scheme therefore needs a benevolent leviathan that, unless it relies on an open-ended subsidy, also knows $F$; the arguments of Brennan and Buchanan and of Acemoglu are reasons not to count on one; and agent bargaining does not create one.

## What survives

Frictional costs do fall.
Search, drafting, monitoring and routine verification are mostly non-rival work, and agents will make them cheap.

Thick markets with many buyers and many sellers of rival, excludable, substitutable goods work well and get better with scale: kerb space sold by the minute, electricity by the interval, delivery slots.
The informational loss there is of order $1/N^2$, and simple prices support efficient allocations.
This class of cases is where Krier's argument is strongest.

Disputes among a few parties also survive well.
Krier's expected starting cases, the office thermostat, shared resources in an apartment block, the division of household chores, involve small $N$, and the bilateral informational loss is moderate, $5/32$ of the gains in the uniform example.

The two views make different predictions.
Holding technology fixed, the analysis here predicts that the success of agent bargaining should fall with the number of parties whose consent a single decision needs, and with the degree of complementarity between the rights involved.
It also predicts that resources burned in bargaining should scale with the surplus at stake and should not fall as computation gets cheaper.
Krier's account, in which the remaining costs are frictional, predicts none of these patterns.
The first deployments he expects will show success at small $N$, and that evidence will not distinguish the two accounts until it reaches decisions that bind many parties at once.

Agents may also make the leviathan better informed and more auditable.
High-resolution feedback on policy effects, automated auditing of public spending and monitoring of regulatory capture are Krier's automated-governance proposals, and I think they are a real gain.
They are an argument for better planners, which is a different conclusion from his.

The division I draw differs from Petel's (2025).
Petel divides cases according to whether a good can be priced without being corrupted, whether harms can be verified without surveillance, and how wealth effects distort outcomes.
The division here is mechanism-theoretic and cuts across his: rival against public goods, substitutes against complements, few parties against many.
Ngo (2026) objects from a different direction, that reasoning in terms of efficiency erodes sociopolitical autonomy.
Shahidi et al. (2025) give the most sympathetic economic treatment of AI agents in markets and note that agents bring new frictions of their own, such as congestion and price obfuscation.

## Objections and limits

### The hardness results are worst-case

The communication and computation bounds hold over all instances, real preferences have structure, and language-model agents are good heuristic solvers of structured problems.
I accept this for the results on bits, winner determination and coalition structures.
But the weight of my argument rests on the informational results, which are not worst-case in this sense: Mailath and Postlewaite's limit holds for a broad class of distributions, not for adversarially chosen instances.
And the structure that makes instances easy is often imposed by restricting what can be bid on or contracted for, and imposing it is a constitutional act.

### The informational results assume independent private values and quasi-linear utility

With correlated types, the Crémer–McLean construction restores efficiency, but only with a well-informed designer able to impose large penalties.
With interdependent values, where one party's information bears on another's value, efficient mechanisms are harder to find: Jehiel and Moldovanu (2001) show that when each party's private information has more than one dimension, efficient incentive-compatible mechanisms generically do not exist.
Without quasi-linearity, wealth effects enter, and Krier already concedes that these make outcomes depend on initial rights.
I know of no relaxation of these assumptions that helps his case, though how closely real neighbourhoods fit the models is an empirical matter.

### Repeated interaction and reputation

Agents will interact repeatedly, and reputation can sustain cooperation that one-shot bargaining cannot.
Folk theorems say that in infinitely repeated games with patient players, almost any feasible payoff that gives each player at least what it can guarantee itself can be sustained in equilibrium (Fudenberg and Maskin 1986).
So efficient outcomes are equilibria, among many others, and the theorems do not select them.
Program equilibrium (Tennenholtz 2004) is a new capability: agents that can read each other's code can sustain cooperation even in one-shot games.
But it too enlarges the set of equilibria, so the problem of selecting among them, and the question of who selects, remains.

### Binding side-payments

Agents might make binding promises of side-payments before play, and Coasean bargaining can be read as an exchange of such promises.
Jackson and Wilkie (2005) show that free, binding side-payment promises made before a game is played do not generally yield efficient outcomes.

### Benevolence is a strong requirement

I do not claim that a benevolent leviathan exists, or that anyone should pretend one does.
The claim is about what efficiency requires.
Design for a sovereign that is not benevolent is the problem we actually face, and it is the old problem of constitutional political economy.
My argument is a negative one: agent bargaining does not let us escape that problem.

### The contest model is a modelling choice

The Tullock form is one model of how spending translates into bargaining share, and the invariance of total spending to $c$ is a property of that form and close relatives.
If bargaining share saturates, so that beyond some level more computation buys nothing, then cheap computation would eventually equalize agents, and contest spending would fall.
Whether agent negotiation looks more like a Tullock contest or like a saturating one is an empirical question that the evidence I cite only begins to address.

## Conclusion

Agents will make bargaining cheaper, and Krier's proposal holds up for thick markets in rival goods, for small disputes, and for better-informed and more auditable government.
The disagreement is over the residue.
He holds that what remains after friction falls is a lean state that guarantees a framework, plus engineering.
The theorems and models above say that the informational part of what remains does not depend on the price of computation, that the residue grows with the number of parties and the granularity of contracts, and that it can be removed only by an actor that binds dissenters or taxes, and that, unless it relies on an open-ended subsidy, also assigns entitlements with knowledge of the distribution of preferences, restricts what contracts may say, selects equilibria and decides the cases no contract covers.
An actor with those powers and that knowledge does what planning agencies do.
For it to use them well, it must also want aggregate welfare, which nothing in a system of selfish delegated agents supplies.
For decisions that bind many people, agent bargaining leaves the problem of building a good government in place.

## References

- Acemoglu, D. (2003). [Why not a political Coase theorem? Social conflict, commitment, and politics](https://doi.org/10.1016/j.jce.2003.09.003). *Journal of Comparative Economics* 31(4): 620-652.
- Aghion, P., & Bolton, P. (2003). [Incomplete social contracts](https://doi.org/10.1162/154247603322256765). *Journal of the European Economic Association* 1(1): 38-67.
- Aivazian, V. A., & Callen, J. L. (1981). [The Coase theorem and the empty core](https://doi.org/10.1086/466979). *Journal of Law and Economics* 24(1): 175-181.
- Al-Najjar, N. I., & Smorodinsky, R. (2000). [Pivotal players and the characterization of influence](https://doi.org/10.1006/jeth.2000.2605). *Journal of Economic Theory* 92(2): 318-342.
- Arrow, K. J. (1969). The organization of economic activity: issues pertinent to the choice of market versus nonmarket allocation. In *The Analysis and Evaluation of Public Expenditures: The PPB System*, Joint Economic Committee, US Congress.
- Arrow, K. J. (1979). [The property rights doctrine and demand revelation under incomplete information](https://doi.org/10.1016/b978-0-12-118850-4.50007-2). In Boskin, M. J. (ed.), *Economics and Human Welfare*. Academic Press: 23-39.
- Aumann, R. J. (1974). [Subjectivity and correlation in randomized strategies](https://doi.org/10.1016/0304-4068%2874%2990037-8). *Journal of Mathematical Economics* 1(1): 67-96.
- Ausubel, L. M., & Milgrom, P. (2006). The lovely but lonely Vickrey auction. In Cramton, P., Shoham, Y., & Steinberg, R. (eds.), *Combinatorial Auctions*. MIT Press.
- Bartholdi, J. J., Tovey, C. A., & Trick, M. A. (1989). [The computational difficulty of manipulating an election](https://doi.org/10.1007/bf00295861). *Social Choice and Welfare* 6(3): 227-241.
- Bergemann, D., & Morris, S. (2005). [Robust mechanism design](https://doi.org/10.1111/j.1468-0262.2005.00638.x). *Econometrica* 73(6): 1771-1813.
- Blackwell, D. (1953). [Equivalent comparisons of experiments](https://doi.org/10.1214/aoms/1177729032). *The Annals of Mathematical Statistics* 24(2): 265-272.
- Brennan, G., & Buchanan, J. M. (1980). The Power to Tax: Analytical Foundations of a Fiscal Constitution. Cambridge University Press.
- Buchanan, J. M., & Tullock, G. (1962). [The Calculus of Consent](https://doi.org/10.3998/mpub.7687). University of Michigan Press.
- Buchanan, J. M., & Yoon, Y. J. (2000). [Symmetric tragedies: commons and anticommons](https://doi.org/10.1086/467445). *Journal of Law and Economics* 43(1): 1-14.
- Calabresi, G., & Melamed, A. D. (1972). [Property rules, liability rules, and inalienability: one view of the cathedral](https://doi.org/10.2307/1340059). *Harvard Law Review* 85(6): 1089.
- Chatterjee, K., & Samuelson, W. (1983). [Bargaining under incomplete information](https://doi.org/10.1287/opre.31.5.835). *Operations Research* 31(5): 835-851.
- Coase, R. H. (1960). [The problem of social cost](https://doi.org/10.1086/466560). *Journal of Law and Economics* 3: 1-44.
- Conitzer, V., & Sandholm, T. (2002). [Complexity of mechanism design](https://arxiv.org/abs/cs/0205075). *Proceedings of UAI 2002*.
- Conitzer, V., & Sandholm, T. (2006). [Complexity of constructing solutions in the core based on synergies among coalitions](https://doi.org/10.1016/j.artint.2006.01.005). *Artificial Intelligence* 170(6-7): 607-619.
- Cournot, A. A. (1838). Recherches sur les principes mathématiques de la théorie des richesses. Hachette.
- Cramton, P., Gibbons, R., & Klemperer, P. (1987). [Dissolving a partnership efficiently](https://doi.org/10.2307/1913602). *Econometrica* 55(3): 615.
- Crémer, J., & McLean, R. P. (1988). [Full extraction of the surplus in Bayesian and dominant strategy auctions](https://doi.org/10.2307/1913096). *Econometrica* 56(6): 1247.
- d'Aspremont, C., & Gérard-Varet, L.-A. (1979). [Incentives and incomplete information](https://doi.org/10.1016/0047-2727%2879%2990043-4). *Journal of Public Economics* 11(1): 25-45.
- Deng, X., & Papadimitriou, C. H. (1994). [On the complexity of cooperative solution concepts](https://doi.org/10.1287/moor.19.2.257). *Mathematics of Operations Research* 19(2): 257-266.
- Dixit, A., & Olson, M. (2000). [Does voluntary participation undermine the Coase theorem?](https://doi.org/10.1016/s0047-2727%2899%2900089-4). *Journal of Public Economics* 76(3): 309-335.
- Dodis, Y., Halevi, S., & Rabin, T. (2000). [A cryptographic solution to a game theoretic problem](https://doi.org/10.1007/3-540-44598-6_7). *Proceedings of CRYPTO 2000* (Lecture Notes in Computer Science): 112-130.
- Ellingsen, T., & Miettinen, T. (2008). [Commitment and conflict in bilateral bargaining](https://doi.org/10.1257/aer.98.4.1629). *American Economic Review* 98(4): 1629-1635.
- Ellingsen, T., & Paltseva, E. (2016). [Confining the Coase theorem: contracting, ownership, and free-riding](https://doi.org/10.1093/restud/rdw001). *Review of Economic Studies* 83(2): 547-586.
- Farrell, J. (1987). [Information and the Coase theorem](https://doi.org/10.1257/jep.1.2.113). *Journal of Economic Perspectives* 1(2): 113-129.
- Fudenberg, D., & Maskin, E. (1986). [The folk theorem in repeated games with discounting or with incomplete information](https://doi.org/10.2307/1911307). *Econometrica* 54(3): 533.
- Gibbard, A. (1973). [Manipulation of voting schemes: a general result](https://doi.org/10.2307/1914083). *Econometrica* 41(4): 587.
- Green, J. R., & Laffont, J.-J. (1979). Incentives in Public Decision-Making. North-Holland.
- Grossman, S. J., & Hart, O. D. (1986). [The costs and benefits of ownership: a theory of vertical and lateral integration](https://doi.org/10.1086/261404). *Journal of Political Economy* 94(4): 691-719.
- Gul, F., & Stacchetti, E. (1999). [Walrasian equilibrium with gross substitutes](https://doi.org/10.1006/jeth.1999.2531). *Journal of Economic Theory* 87(1): 95-124.
- Hart, O., & Moore, J. (1988). [Incomplete contracts and renegotiation](https://doi.org/10.2307/1912698). *Econometrica* 56(4): 755.
- Hart, O., & Moore, J. (1999). [Foundations of incomplete contracts](https://doi.org/10.1111/1467-937x.00080). *Review of Economic Studies* 66(1): 115-138.
- Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review* 35(4).
- Hirshleifer, J. (1971). The private and social value of information and the reward to inventive activity. *American Economic Review* 61(4).
- Hobbes, T. (1651). Leviathan. Andrew Crooke.
- Holmström, B. (1979). [Groves' scheme on restricted domains](https://doi.org/10.2307/1911954). *Econometrica* 47(5): 1137.
- Hurwicz, L. (2008). [But who will guard the guardians?](https://doi.org/10.1257/aer.98.3.577). *American Economic Review* 98(3): 577-585.
- Jackson, M. O., & Wilkie, S. (2005). [Endogenous games and mechanisms: side payments among players](https://doi.org/10.1111/j.1467-937x.2005.00342.x). *Review of Economic Studies* 72(2): 543-566.
- Jehiel, P., & Moldovanu, B. (2001). [Efficient design with interdependent valuations](https://doi.org/10.1111/1468-0262.00240). *Econometrica* 69(5): 1237-1259.
- Kahng, A., Mackenzie, S., & Procaccia, A. D. (2021). [Liquid democracy: an algorithmic perspective](https://doi.org/10.1613/jair.1.12261). *Journal of Artificial Intelligence Research* 70: 1223-1252.
- Kelso, A. S., & Crawford, V. P. (1982). [Job matching, coalition formation, and gross substitutes](https://doi.org/10.2307/1913392). *Econometrica* 50(6): 1483.
- Krier, S. (2025). [Coasean bargaining at scale: decentralization, coordination, and co-existence with AGI](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale). Cosmos Institute.
- Lehmann, D., O'Callaghan, L. I., & Shoham, Y. (2002). [Truth revelation in approximately efficient combinatorial auctions](https://doi.org/10.1145/585265.585266). *Journal of the ACM* 49(5): 577-602.
- Mailath, G. J., & Postlewaite, A. (1990). [Asymmetric information bargaining problems with many agents](https://doi.org/10.2307/2298018). *Review of Economic Studies* 57(3): 351.
- Maskin, E., & Tirole, J. (1999). [Unforeseen contingencies and incomplete contracts](https://doi.org/10.1111/1467-937x.00079). *Review of Economic Studies* 66(1): 83-114.
- Myerson, R. B. (1981). [Optimal auction design](https://doi.org/10.1287/moor.6.1.58). *Mathematics of Operations Research* 6(1): 58-73.
- Myerson, R. B., & Satterthwaite, M. A. (1983). [Efficient mechanisms for bilateral trading](https://doi.org/10.1016/0022-0531%2883%2990048-0). *Journal of Economic Theory* 29(2): 265-281.
- Ngo, R. (2026). [Economic efficiency often undermines sociopolitical autonomy](https://www.mindthefuture.info/p/economic-efficiency-often-undermines). Mind the Future.
- Nisan, N., & Ronen, A. (2007). [Computationally feasible VCG mechanisms](https://doi.org/10.1613/jair.2046). *Journal of Artificial Intelligence Research* 29: 19-47.
- Nisan, N., & Segal, I. (2006). [The communication requirements of efficient allocations and supporting prices](https://doi.org/10.1016/j.jet.2004.10.007). *Journal of Economic Theory* 129(1): 192-224.
- Petel, M. H. (2025). [Price what you can, protect what you must](https://mateopetel.substack.com/p/price-what-you-can-protect-what-you). Critical Systems.
- Posner, E. A., & Weyl, E. G. (2017). [Property is only another name for monopoly](https://doi.org/10.1093/jla/lax001). *Journal of Legal Analysis* 9(1): 51-123.
- Rice, H. G. (1953). [Classes of recursively enumerable sets and their decision problems](https://doi.org/10.1090/s0002-9947-1953-0053041-6). *Transactions of the American Mathematical Society* 74(2): 358-366.
- Rob, R. (1989). [Pollution claim settlements under private information](https://doi.org/10.1016/0022-0531%2889%2990022-7). *Journal of Economic Theory* 47(2): 307-333.
- Rothkopf, M. H., Pekeč, A., & Harstad, R. M. (1998). [Computationally manageable combinational auctions](https://doi.org/10.1287/mnsc.44.8.1131). *Management Science* 44(8): 1131-1147.
- Rustichini, A., Satterthwaite, M. A., & Williams, S. R. (1994). [Convergence to efficiency in a simple market with incomplete information](https://doi.org/10.2307/2951506). *Econometrica* 62(5): 1041.
- Sandholm, T. (2002). [Algorithm for optimal winner determination in combinatorial auctions](https://doi.org/10.1016/s0004-3702%2801%2900159-x). *Artificial Intelligence* 135(1-2): 1-54.
- Satterthwaite, M. A. (1975). [Strategy-proofness and Arrow's conditions: existence and correspondence theorems for voting procedures and social welfare functions](https://doi.org/10.1016/0022-0531%2875%2990050-2). *Journal of Economic Theory* 10(2): 187-217.
- Schelling, T. C. (1960). The Strategy of Conflict. Harvard University Press.
- Segal, I. (1999). [Complexity and renegotiation: a foundation for incomplete contracts](https://doi.org/10.1111/1467-937x.00078). *Review of Economic Studies* 66(1): 57-82.
- Segal, I., & Whinston, M. D. (2011). [A simple status quo that ensures participation (with application to efficient bargaining)](https://doi.org/10.3982/te591). *Theoretical Economics* 6(1): 109-125.
- Segal, I., & Whinston, M. D. (2016). [Property rights and the efficiency of bargaining](https://doi.org/10.1111/jeea.12185). *Journal of the European Economic Association* 14(6): 1287-1328.
- Shahidi, P., Rusak, G., Manning, B., Fradkin, A., & Horton, J. (2025). [The Coasean singularity? Demand, supply, and market design with AI agents](https://www.nber.org/papers/w34468). NBER Working Paper 34468.
- Shannon, C. E. (1949). [The synthesis of two-terminal switching circuits](https://doi.org/10.1002/j.1538-7305.1949.tb03624.x). *Bell System Technical Journal* 28(1): 59-98.
- Sharp, M., Bilgin, O., Gabriel, I., et al. (2025). [Agentic inequality](https://arxiv.org/abs/2510.16853). arXiv:2510.16853.
- Tennenholtz, M. (2004). [Program equilibrium](https://doi.org/10.1016/j.geb.2004.02.002). *Games and Economic Behavior* 49(2): 363-373.
- Tirole, J. (2009). [Cognition and incomplete contracts](https://doi.org/10.1257/aer.99.1.265). *American Economic Review* 99(1): 265-294.
- Tullock, G. (1980). Efficient rent seeking. In Buchanan, J. M., Tollison, R. D., & Tullock, G. (eds.), *Toward a Theory of the Rent-Seeking Society*. Texas A&M University Press.
- Vaccaro, M., Caosun, M., Ju, H., et al. (2025). [Advancing AI negotiations: a large-scale autonomous negotiation competition](https://arxiv.org/abs/2503.06416). arXiv:2503.06416.
- Zhu, S., Sun, J., Nian, Y., et al. (2025). [The automated but risky game: modeling and benchmarking agent-to-agent negotiations and transactions in consumer markets](https://arxiv.org/abs/2506.00073). arXiv:2506.00073.
