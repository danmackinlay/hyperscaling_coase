---
title: "Delegated agent constitutional negotiation favours the incumbents"
date: 2026-11-18
abstract: >
  Seb Krier argues that personal AI agents could make bargaining cheap enough for many externalities to be settled privately instead of by regulation.
  I grant that argument inside given rules and ask what happens when faithful agents negotiate the rules themselves.
  Krier concedes that the initial allocation of rights decides distribution, and reassures us that agents make it cheap to contest and improve the democratic process that amends it.
  I test that reassurance against position-independence: equal stakes and equally capable agents should do equally well whatever positions each side holds when negotiation starts.
  I define four positions (holding an entitlement, being organized, drafting the text, deciding what happens where the text is silent) and argue that the advantage of each does not shrink as cognition gets cheaper.
  In a model of a contested rule, a diffuse group's chance against an organized party of equal stake falls as effort gets cheaper, to one in $n+1$, first where stakes are large and then where they are small.
  Granting Krier's premise that cheap cognition makes rules more detailed, the burden of auditing a drafted rule grows (a conjecture by analogy) and explicit text loses force (an extrapolation).
  The remedies these models point to are non-voluntary.
---

<!-- TODO: citations are DOI/arXiv hyperlinks pending ingestion into Zotero: direnv exec . uv run ref-cite -c <collection> -i _plans/hyperscaling_coase_constitutional_complexity_2.qmd -->

## Summary

Seb Krier's essay [Coasean bargaining at scale](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale) argues that personal AI agents could lower transaction costs far enough that many externalities are settled by private bargaining instead of by regulation.
I grant that argument for outcomes reached inside given rules.
Krier concedes that who starts with which right decides who ends up richer, and argues that agents make that allocation cheap to contest and improve the democratic systems that amend it.
I ask what happens when agents, each serving its own principal, negotiate the rules themselves.
My answer is that a party can hold any of four positions when negotiation starts (holding an entitlement, being already organized, drafting the text, deciding what happens where the text is silent), and that each confers an advantage that cheap cognition does not remove.
By incumbents I mean the holders of these positions, who are not always the defenders of the status quo.
For being organized, a model says the advantage grows as cognition gets cheaper, and reaches rules with smaller stakes.
For drafting and deciding in the gaps, there are reasons to think it grows with the detail of the rules, which cheap cognition makes possible.
The remedies the models point to are non-voluntary.
The argument follows Krier's two routes for changing the rules, and predicts different things on each: on the voluntary route, that the status quo tends to stay; on the democratic route, that rules change the way organized parties and proposers want.
Its parts do different jobs.

On the voluntary route:

1. *The status quo as a floor.* Baseline, conceded by Krier. (Entitlement holder.)
2. *Drafting and auditing.* Carries the claim for the drafter; an analogy.
3. *Incompleteness and residual control.* Carries the claim for the residual controller; an extrapolation.
4. *Costly negotiation.* Carries the claim for the entitlement holder; one model.

On the democratic route:

5. *Contests between buyers of effort.* A lemma: among parties that buy all their effort, the price of effort changes nothing.
6. *Organized parties and diffuse groups.* The main result: a theorem in a model, and the one claim here that an advantage grows as $c$, the cost of cognition, falls.
7. *Proposal power.* Background: classic results that do not depend on $c$.

## Krier's argument

Coase's theorem says that if bargaining were costless, the parties to an externality would reach the efficient arrangement whoever started with the right, though who starts with it decides who pays whom.
Krier's claim is that personal agents remove most of the bargaining costs that have kept the theorem a benchmark and not a description.
A delivery truck's agent sees a fee for entering a street, set by the agents of the residents who would breathe its fumes, and either pays it or takes another route.
Each person's agent knows what its principal will put up with, and on what conditions (loud music on a Saturday but not on a Sunday), so rules and prices could condition on very fine detail.
He also describes agents as a coordination device, letting parties condition their actions on shared signals and reach outcomes that uncoordinated play would miss, and takes his picture of an economy of interacting agents from [Tomašev et al. (2025)](https://arxiv.org/abs/2509.10147).

Krier concedes that efficient bargaining does not settle distribution.
Whoever starts with the right to quiet, or the right to make noise, ends up richer, which is why he calls the initial allocation of rights "a constitutional choice, not a technicality".
His reassurance about that allocation is what this article tests, and it comes in two parts.
On what I call the *voluntary route*, agents leave the baseline in place, with the rights set by centuries of jurisprudence as the starting point, and make it explicit, contestable and cheap to renegotiate.
Some rules would harden by mutual agreement (basic property and contract) while others stay perpetually negotiable (noise, parking), with governance moving from statute to something like a thermostat; he expects agents to settle on stable arrangements for most issues because constant renegotiation costs computation, even for very capable systems.
On what I call the *democratic route*, existing democratic systems amend entitlements.
He regards those systems as slow and captured, and expects agents to improve them through continuous deliberation and liquid delegation, in which a citizen hands their vote on a topic to a trusted party and can take it back at any time.
He separates two modes of decision, bargaining in which willingness to pay decides and decisions in which each person's vote counts equally, and expects agents to move between them by issue.

His cost argument is that legal work costing ten thousand dollars today may cost pennies of compute tomorrow, and that a billionaire's phone is no better than anyone else's.
I read this as the claim that both sides face the same price for reasoning.

Against holdouts he offers one voluntary device and three coercive ones.
In the voluntary *bargaining club*, homeowners who join submit private minimum prices and the club makes one take-it-or-leave-it offer.
A member has no reason to overstate, because if the deal clears it is paid the common clearing price, not its own declared number, and overstating risks killing the deal.
The club disciplines its members; it does nothing about a holder who does not join.
The coercive devices act on holders whether they consent or not.
Chronic over-bidders can have their vote weight fade, or pay a Harberger-style fee, a periodic percentage of the price a holder claims for its right, so that claiming an inflated price is costly.
And a coalition that vetoes a project can be required to reimburse the diffuse public for the loss, which agents quantify.

His counterweight to concentrated wealth is the *flash coalition*: when a factory proposes to increase its emissions, the agents of ten thousand residents form a coalition at once and name a single price.
To stop cost from excluding poorer participants he proposes compute credits in two forms: targeted vouchers for civic uses such as deliberation and legal representation, and a universal allocation people spend as they like, which he offers because a central body choosing which uses deserve support would bring back the planner; he suggests a hybrid of the two.
He compares the cost to the modest public outlay on roads.
He leaves open whether agents should correct their principals' biases or faithfully represent them.

Krier keeps the state as enforcer of contracts and boundary on what agents may do, and says that non-voluntary institutions are needed alongside the agents.
We agree on that; we differ on what agents do to the contest over the rules.

## Setup

### Levels and terms

I take the distinction between two levels of choice from [Buchanan & Tullock (1962)](https://doi.org/10.3998/mpub.7687).
An *operational* outcome is the result of one negotiation: this truck pays this fee for this street today.
A rule is *constitutional* when it fixes the terms of many later negotiations: who owes whom by default, how a bargaining club computes its offer, the formula for a fee, and how any of these may be changed.
In this sense a neighbourhood's fee formula is as much a constitutional rule as anything in a national constitution.
I grant Krier's argument at the *operational level* and ask what happens at the *constitutional level*.

The *status quo constitution* $s_0$ is the set of entitlements, mechanisms and amendment rules in force when negotiation starts.
In existing democracies $s_0$ already contains a majoritarian amendment rule.
A *faithful agent* is one that maximizes its own principal's payoff.
*Granularity* is the number of distinct conditions a rule tests; Krier's Saturday-and-Sunday example is a description of high granularity.
The *unit cost of cognition* $c$ is the price of a unit of effective reasoning: drafting, modelling a counterparty, searching for objections, persuading.
The word *effective* matters because a more capable agent gets more done per unit of compute, so a difference in capability between two sides is a difference in their unit costs.

### Four positions

A party may hold any of four positions under $s_0$.
An *entitlement holder* holds a baseline right, and with it a veto over voluntary change and the benefits of $s_0$ for as long as negotiation lasts.
An *organized party* is already constituted under $s_0$ as a single decision-maker with a single budget: a firm, an agent provider, an agency.
Its defining property, and the one the main result turns on, is that its members are already bound.
A firm is in effect a standing coalition whose members are bound by company law; the residents of a neighbourhood would have to build theirs, and a diffuse group with the same total stake holds many small stakes instead of one.
A *drafter* writes the text of proposed rules, protocols and standard forms.
A *residual controller* decides what happens in contingencies the rules do not cover: owners of assets, providers of agents through their terms of service, and the courts and regulators who apply default law.
A *challenger* is a party seeking a change from $s_0$.

Positions can be held by opposing sides: in Krier's factory example the residents hold the entitlement and the factory is organized.
Each advantage then accrues to whoever holds that position, and which one matters depends on the route.
On the voluntary route the entitlement holder's veto is decisive, and the drafter and the residual controller gain within what the veto allows.
On the democratic route the veto is gone and the entitlement holder has no advantage as such; organization and proposal power decide.
The incumbents of the title are the holders of these positions, who need not be the defenders of $s_0$.

### The benchmark

The benchmark is *position-independence*: two sides with equal total stakes in a rule and equally capable faithful agents do equally well, measured by each side's chance of prevailing or share of what is at stake, whichever positions they hold.

Krier concedes that entitlements decide distribution, so the test needs a reason.
His reassurance is that the allocation can be contested cheaply and amended by an improved democratic process.
That is worth something only if contests over the allocation are not themselves decided by position.
Of the four positions, he concedes the entitlement holder at the operational level and says it is contestable at the constitutional level; flash coalitions and compute credits are his answer to the organized party; the drafter and the residual controller he does not address.

### What is claimed, and how strongly

The main claim is that each of the four positions confers an advantage on at least one of Krier's two routes, that neither route is free of them, and that none of these advantages shrinks towards position-independence as $c$ falls.
I make three stronger claims, and use these names for them throughout.

(i) *Cheap purchased effort.*
In a contested rule, a diffuse group's chance against an organized party of equal stake falls as $c$ falls, down to one in $n+1$ for a group of $n$, and the stake at which that floor is reached falls with $c$.
This is a theorem in a model that isolates the price of purchased effort relative to personal effort.
Outside the model, agents also bring into the contest residents who would otherwise not have known of it or taken part; that helps the diffuse group, and the relative size of the two effects is unmeasured.

(ii) *The audit burden.*
The drafter's advantage grows with granularity.
This is a conjecture by analogy.

(iii) *The weakening of explicit text.*
The residual controller's advantage grows with granularity when renegotiation is cheap.
This is an extrapolation from a two-party model.

Claims (ii) and (iii) are about granularity, not about $c$.
They bear on the main claim through a premise that is Krier's own: cheap cognition is what makes fine-grained rules possible, so granularity rises as $c$ falls.
I call this the *granularity premise* and refer back to it where it is used.
Fine-grained rules are a choice and not a by-product; where the parties refuse them, claims (ii) and (iii) do not arise, and neither do the gains Krier expects from them.

### Scope and related work

The scope is limited in three ways.
I do not claim that the operational gains are illusory, nor that present institutions do better.
I assume the agents are as good as Krier hopes: capable, cheap and faithful.
The results I cite are theorems about models, not evidence about what current language-model agents do, and the few experiments I mention are labelled as such where they appear.

The economics of AI agents already flags distributional and design problems.
[Shahidi et al. (2025)](https://www.nber.org/papers/w34468) argue that agents lower the costs of search, communication and contracting but bring congestion and price obfuscation, leaving the net effect on welfare an empirical question; Tomašev et al. list exacerbated inequality among the challenges of an agent economy; and [Hammond et al. (2025)](https://arxiv.org/abs/2502.14143) survey the risks that arise when many agents interact.
My contribution is narrower: I look only at the constitutional level, and bring to it five bodies of theory, namely bargaining theory, social choice, contest theory and collective action, computational complexity, and incomplete contracts.

## The voluntary route

On this route a rule changes only with the consent of every party whose entitlement it touches.
The first subsection sets the baseline, that each holder's position under $s_0$ is a floor; the second and third argue that the drafter and the residual controller gain on top of it; the fourth shows that a small cost of negotiating can keep $s_0$ in place.

### The status quo as a floor

This subsection is the baseline, conceded by Krier.
[Buchanan & Tullock (1962)](https://doi.org/10.3998/mpub.7687) treated the choice of a decision rule as a trade between decision costs, which rise with the required majority, and the costs imposed on dissenters, which fall with it and vanish at unanimity; as decision costs fall, the best rule moves towards unanimity, which is Krier's voluntary route.
[Rae (1975)](https://doi.org/10.2307/1955287) pointed out that unanimity privileges whatever is already in place, and protects everyone from imposition only if remaining at the status quo counts as imposing no cost.
Agents lower the cost of saying yes, and that does nothing for the party who needs a change that someone else can refuse.

Any change on this route needs each holder's consent, so no holder ends below what $s_0$ gives it.
This follows from consent alone, and it is symmetric, since every party with a veto has the floor; the asymmetry is all in $s_0$, which is Krier's concession.
So this subsection restates the concession, and adds two things.

The first is that the three coercive devices cannot be adopted on this route.
Each takes something from a holder who holds out (voting weight, a fee on its declared price, a reimbursement), so a likely holdout will not consent to any of them.
A reader of Buchanan and Tullock will object that people do unanimously adopt rules requiring less than unanimity, because they choose them behind a veil of uncertainty about which side of future decisions they will be on.
That argument needs parties who do not know their future positions.
Here $s_0$ exists and Krier starts from existing rights, so the likely holdouts know who they are.
The coercive devices therefore need the democratic route, which Krier names as the mechanism for changing entitlements.

The second is that the holder keeps what $s_0$ gives it for as long as negotiation lasts.
The *disagreement point* of a bargaining problem is the pair of payoffs the parties get for as long as they have not agreed ([Nash (1950)](https://doi.org/10.2307/1907266)).
[Binmore, Rubinstein & Wolinsky (1986)](https://doi.org/10.2307/2555382) show that when bargaining takes time, the disagreement payoff that sets bargaining positions is the income each side receives while the dispute lasts.
Under voluntary change that income is what $s_0$ provides, so delay costs the challenger and not the holder, a point the costly-negotiation subsection returns to.

[Aghion & Bolton (2003)](https://doi.org/10.1162/154247603322256765) give a normative result: asked which rule they would choose if they did not know who would gain from future changes, parties prefer some majority rule to unanimity whenever compensating the losers from a change carries deadweight costs, that is, costs borne by someone and received by no one.
So whether the voluntary route suffices depends on whether the costs of reaching and compensating agreement vanish as $c$ falls.
The subsections on drafting and on costly negotiation each describe a cost of reaching agreement that does not.

### Drafting and auditing

This subsection carries the claim for the drafter, and it is an analogy.

At the constitutional level the object of negotiation is often a *mechanism*: a procedure, such as a clearing rule or a fee formula, that takes what the parties report and what happens in the world and returns an outcome.
The parties respond strategically to a mechanism, so what it does to a principal cannot be read off its text.
It is what happens at an equilibrium of the game the text creates, where an *equilibrium* is a profile of strategies, one for each party, from which no party gains by deviating on its own, given what it knows.
To consent on a principal's behalf, a faithful agent must answer one question, which I call the *audit*: is there a contingency in which this rule leaves my principal worse off than $s_0$ would?
A contingency here is a combination of the conditions the rule tests, together with what the parties do in response.

The audit question has two properties.
First, it cannot be answered by solving the mechanism outright: finding an equilibrium is PPAD-complete even in the simplest case, two players with nothing private ([Daskalakis, Goldberg & Papadimitriou (2009)](https://doi.org/10.1137/070699652); [Chen, Deng & Teng (2009)](https://doi.org/10.1145/1516512.1516516)), where PPAD is a class of problems for which a solution is known to exist but no efficient way of finding one is known or expected.
This is a worst-case result, and it binds the drafter as much as the auditor, so it is not the source of any advantage.

Second, the audit is a search problem with a particular shape.
A bad contingency, once pointed out together with the responses claimed for the parties, is quick to check.
Finding one means searching combinations of conditions, and the number of combinations grows exponentially with the number of conditions the rule tests, that is, with granularity.
For the computer scientist, this is the shape of problems in NP, quick to verify and possibly slow to search.
For the economist, checking a claimed arbitrage is quick, and finding one is the hard part.

[Arora, Barak, Brunnermeier & Ge (2011)](https://doi.org/10.1145/1941487.1941511) show how such a search can be made hard on purpose.
They study a seller who pools many assets into many derivatives, each of which pays out according to some subset of the assets.
The textbook view in finance is that structuring of this kind reduces the damage done by the seller's better information.
Pooling many assets and slicing the pooled cash flow lets the seller sell the slices whose value hardly depends on what it privately knows, and keep the rest.
In their model the seller knows which assets are bad and chooses which assets go into which derivative, so it can over-represent the bad assets in a few derivatives.
That shows up only as an unusually dense cluster in the table recording which derivative references which asset, and finding such a planted cluster in an otherwise random table, a relative of the planted-clique problem, is conjectured to be intractable on average, that is, for typical instances as well as contrived ones.
So a buyer with the same computing power as the seller cannot tell a tampered product from a clean one, and complexity makes the seller's information advantage worse where structuring was supposed to make it better.
They give a simpler illustration of the same asymmetry between building an object and examining it: take a contract that pays out if some future number, say a digit of next year's unemployment rate, equals the last digit of a factor of a given huge integer.
Whoever chose the integer by multiplying two primes knows the factors and can value the contract; nobody else can without factoring it.
The result has two ingredients: private information held by the party who constructs the object, and a construction that hides the use of that information from any efficient check.

What follows is an argument by analogy from financial products to rules, not a corollary of the theorem, and I know of no measurement of how often negotiated rules fall in the hard regime.
The table of which derivative references which asset corresponds to the rule's many conditions and clauses.
The hidden dense cluster corresponds to a particular combination of conditions under which the clauses interact to the drafter's benefit.
The seller's knowledge of which assets are bad corresponds to the drafter's private knowledge of which combinations will in fact arise, because they depend on its own plans: a firm knows its expansion plans, and its neighbours' agents do not.
The drafter works in the easy direction: it starts from that combination and writes clauses that produce the outcome it wants there, and it needs not the best possible mechanism but only one that contains its combination.
The auditor works in the hard direction: it must search.
So the advantage does not depend on unequal compute or on any agent being unfaithful; a faithful drafting agent is doing its job.

This is where claim (ii), the audit burden, comes from.
The search space grows exponentially in the number of conditions, while the cost of checking any one combination falls in proportion to $c$.
Under the granularity premise, brute-force audit keeps up only if $c$ falls exponentially in the number of conditions.
Clever search beats brute force on ordinary instances; the planted-structure results say it does not on instances built by an adversary.
Whether drafted rules are such instances is the conjecture.

Any party may draft, including a well-informed challenger, and three things decide who does most of it.
Operators of protocols and providers of agents draft by default, because their protocol and their terms are the text everyone else's agents work within.
Organized parties draft more if drafting is like other effort: the democratic route shows an organized party's effort exceeding a diffuse group's by up to $n$ to one in a contest, and I assume drafting is no different.
And repeat players have more private information worth building in: [Galanter (1974)](https://doi.org/10.2307/3053023) observed that parties who recur in a legal system play for rules as well as outcomes, writing the standard forms and choosing which disputes become precedent, because their stake in a rule is added up over many transactions.

A party that cannot audit can accept complex text, and then the drafter gains, or refuse all complex text, and then $s_0$ stays.
Take Krier's factory and ten thousand residents negotiating, through faithful agents, the mechanism for pricing later disputes, with the residents holding the entitlement to clean air under $s_0$.
If their agents refuse what they cannot audit, the residents are protected, at the cost of a fine-grained mechanism that might have benefited both sides; the beneficiary of the impasse is whoever $s_0$ favours, here the residents, elsewhere the firm.
So on the voluntary route the asymmetry favours the drafter where its text is accepted and the entitlement holder where it is refused, and in neither case do outcomes become position-independent.
On the democratic route a minority cannot refuse, and the asymmetry favours the drafter directly, as the subsection on proposal power argues.

One reply is proofs: a drafter could attach a formal proof that a rule has a stated property.
That has two limits.
The property has to be written down, and *no contingency disadvantages my principal* is exactly what cannot be fully written, as the next subsection argues.
And a demand for proof is a condition on consent, which works only where the drafter would sooner supply the proof than stay at $s_0$.

Another reply is simplicity: insist on simple, standardized rules.
Arora and coauthors recommend this for financial products, and the literature on hidden contract terms points the same way ([Gabaix & Laibson (2006)](https://doi.org/10.1162/qjec.2006.121.2.505)).
I accept this reply, and note its cost: either the rules stay coarse, which is what Krier set out to replace and which leaves $s_0$'s allocation in place, or they favour the drafter.

### Incompleteness and residual control

This subsection carries the claim for the residual controller, and it is an extrapolation.

Any constitution is silent on some contingencies.
Incomplete-contract theory gives three foundations for that silence; two do not weaken as agents improve, and one does.

The first is describability.
If a contract must be a finite text that a procedure can execute, some arrangements that depend on the state of the world in the right way cannot be written ([Anderlini & Felli (1994)](https://doi.org/10.2307/2118357); [Al-Najjar, Anderlini & Felli (2006)](https://doi.org/10.1111/j.1467-937x.2006.00399.x)).
These results concern what can be written, not how fast, so capability does not remove them, and they show only that gaps exist, not who benefits from them.

The second is complexity combined with renegotiation.
It rests on *hold-up*: a party that sinks an investment before the terms of trade are fixed gets only a share of its return in the bargaining that follows, and so under-invests.
In rule-making the sunk investment is reliance: a firm builds where the fee formula makes building worthwhile, a household buys where the noise rule suits it, and a rule that can be reopened afterwards exposes them to renegotiation from a weaker position.
[Segal (1999)](https://doi.org/10.1111/1467-937x.00078) studies a buyer and a seller who can describe $m$ possible trades in advance, only one of which will turn out to be the efficient one.
They may write any long-term contract, including one that depends on messages they send each other later, but they cannot commit not to renegotiate it.
As $m$ grows, the outcome under any such contract, meaning what each party invests beforehand and how the surplus is divided, converges to the outcome with no long-term contract at all, where the parties simply bargain once the efficient trade is known; [Hart & Moore (1999)](https://doi.org/10.1111/1467-937x.00080) obtain the same in a related model.
[Maskin & Tirole (1999)](https://doi.org/10.1111/1467-937x.00079) show the opposing result, that contingencies which cannot be described in advance need not matter if the parties can foresee their payoffs, because a contract can make the outcome depend on reports the parties make later about those payoffs.
Segal and Hart and Moore show that this conclusion fails when renegotiation cannot be prevented and the environment is complex enough.

The third is costly thinking.
[Tirole (2009)](https://doi.org/10.1257/aer.99.1.265) derives incompleteness from the cost of thinking through contingencies.
Unlike the other two, this foundation weakens as $c$ falls.

Segal's condition is that the parties cannot commit not to renegotiate; Krier's feature is that renegotiation is cheap and continuous.
These are different, and they connect through his proposal that some rules harden by mutual agreement while others stay perpetually negotiable.
For the rules he keeps negotiable, the absence of commitment is the design.
For the rules he would harden, something has to enforce the hardening against parties who would later both prefer to reopen, and that enforcer is outside the agents.
So the argument applies to the negotiable class, which is where his fine-grained examples live.
If Segal's result carries over from his two-party model to rule-making among many parties, which is an extrapolation and not a corollary, explicit long-term text in that class loses force as granularity rises.
That is claim (iii), the weakening of explicit text, and through the granularity premise it bears on falling $c$.

When the text is silent, or has lost its force, the outcome is settled by bargaining after the fact, and each side's share depends on what it can do without the other's agreement.
[Grossman & Hart (1986)](https://doi.org/10.1086/261404) and [Hart & Moore (1990)](https://doi.org/10.1086/261729) define ownership of an asset as the right to decide its use in every contingency no contract covers.
They show that this right, called *residual control*, sets the parties' fallback positions in that bargaining, and hence the division.

Krier places the agents inside three nested layers of governance.
The outer layer is the law, a boundary enforced by the state.
Inside it is a market of agent providers, where he relies on competition to drive out agents that serve someone other than their user.
At the core is the individual, whose agent is their advocate within the law and within the provider's terms.
These layers say who holds residual control.
Owners of assets hold it, since he takes existing entitlements as the starting point.
The agent's provider holds it in the market layer, since the agent acts under terms of service the user accepts, and the provider's training and terms settle whatever the user's instructions leave open.^[Whether a user can verify that a supplied agent is faithful is outside this article's scope, which assumes it. [Goldwasser, Kim, Vaikuntanathan & Zamir (2022)](https://arxiv.org/abs/2204.06974) give constructions in which a model's trainer plants a backdoor that no efficient observer can detect; that is a possibility result, not a claim about deployed models.]
Courts and regulators applying default law hold it in the outer layer.
Extending residual control from physical assets to an agent's unspecified behaviour is an analogy from [Hadfield-Menell & Hadfield (2019)](https://doi.org/10.1145/3306618.3314250), who treat an AI system's objective as an incomplete contract whose gaps, like those of human contracts, are filled by outside institutions; for a supplied agent the gap-filler is the provider.

On Krier's cheap renegotiation and fine granularity together, more of what happens is settled by who controls what when the text runs out, and less by the text, which runs against the intuition that finer contracting displaces defaults.

### Costly negotiation

This subsection carries the claim for the entitlement holder, and it rests on one model.

The unit cost $c$ is the price of a unit of cognition, of which each side chooses how much to buy; the democratic route shows when its level matters in a contest and when it does not.
A *participation cost* is a fixed amount each side must spend for a round of bargaining to take place at all; for an agent it is $c$ times the least amount of work needed to read and assess a proposal, and since that amount is positive, a participation cost is positive whenever $c$ is.

[Anderlini & Felli (2006)](https://doi.org/10.1111/j.1468-0297.2006.01054.x) show that when parties must sink costs before a Coasean negotiation, the party that pays recovers only a share in the bargaining that follows, so some mutually beneficial negotiations never start, and negotiating over who bears those costs is a new negotiation with prior costs of its own.
At the constitutional level, some rule changes that would benefit everyone are never negotiated, and $s_0$ stays.

[Lee & Sabourian (2007)](https://doi.org/10.1016/j.jet.2006.03.014) put complexity into the Coase theorem directly.
In their setting two players bargain by alternating offers over a surplus that recurs every period, and in every period without agreement they play an underlying game whose payoffs they receive meanwhile; in our setting, they go on dealing with each other under $s_0$.
Strategies are carried out by finite-state machines, and a strategy's complexity is the number of states its machine needs.
Players care first about payoffs and, between strategies that pay the same, prefer the simpler.
Without transaction costs, this preference eliminates the inefficient equilibria, because the strategies that sustain delay are more complicated than they need to be, and the Coase theorem holds.
With any positive cost of taking part in a round, using the cost structure of [Anderlini & Felli (2001)](https://doi.org/10.1111/1468-0262.00196), in which each side must pay a fixed amount at the start of every round for that round to take place, every equilibrium has perpetual disagreement.
They show the same in the model of [Rubinstein (1982)](https://doi.org/10.2307/1912531), in which two parties alternate offers on how to divide a surplus and delay is costly, once such a cost is added.
My gloss explains why never bargaining can be an equilibrium: against a counterpart who never pays, paying is wasted, and never paying is about the simplest strategy there is.
That no other equilibrium survives is the authors' result.^[I worked from the published abstract and a companion working paper, and have not checked the proof.]

The result is a discontinuity at zero.
The outcome at a tiny positive cost is not near the outcome at zero cost, so the inference from small costs to nearly Coasean outcomes is not safe once complexity is in the model.
Krier expects agents to settle on stable arrangements so as to save computation, and in this model the arrangement that takes least computation to sustain is the one already in force.
That is all I use it for.
It is one two-player model with a specific form of preference for simplicity; it is not evidence about deployed agents, and I do not use it to predict that agent negotiations over rules will deadlock.

While any negotiation lasts, the entitlement holder receives what $s_0$ gives it, so, as the floor subsection showed, delay is paid for by the challenger, and only the side that prefers $s_0$ gains from it.

## The democratic route

On this route a rule can change over a holder's objection, by whatever majoritarian procedure $s_0$ provides.
I make one modelling assumption.
The parties directly affected by a rule are usually a small part of those who decide it, ten thousand residents in a city of a million, so the outcome turns on influence over the unaffected majority, their agents and their delegates: drafting the proposal, making the case, answering the other side, monitoring.
I treat that influence as a contest in which each side's chance of prevailing rises with its share of the total effort.
It is a reduced form, not a model of voting.
The assumption needs defending against Krier's picture of improved deliberation.
The unaffected majority's principals have almost nothing at stake in the rule, so their faithful agents are close to indifferent, and a nearly indifferent decider is one whom the interested sides' submissions can move.
Liquid delegation concentrates those decisions in delegates, who are the natural targets of that effort.
Where the decision is instead taken by equal votes among the directly affected alone, numbers decide whatever the stakes, the diffuse group prevails, and this half of the article does not apply.

### Contests between buyers of effort

This subsection is a lemma: among parties that buy all their effort, the price of effort changes nothing.

Two sides buy all their effort.
Label them $C$, seeking the change, and $I$, defending $s_0$; in this model the label confers no advantage.
Side $i$ values winning at $v_i$, buys $x_i$ units of effort at unit cost $c_i$, and in the contest of [Tullock (1980)](https://doi.org/10.1007/978-1-4757-5055-3_2) prevails with probability equal to its share of the total effort, so $p_C = x_C/(x_C+x_I)$.
Writing $S = x_C + x_I$, the first-order conditions are
$$
\frac{v_C\, x_I}{S^2} = c_C, \qquad \frac{v_I\, x_C}{S^2} = c_I .
$$
With $\theta_i = v_i/c_i$, each side's stake measured in units of effort, dividing the second condition by the first gives $x_C/x_I = \theta_C/\theta_I$, and multiplying each condition by that side's own effort gives $c_i x_i = v_i\, p_C(1-p_C)$.
So
$$
p_C = \frac{\theta_C}{\theta_C + \theta_I}, \qquad c_C x_C + c_I x_I = (v_C + v_I)\, p_C (1 - p_C).
$$
With equal unit costs $c$, the split is $p_C = v_C/(v_C+v_I)$ and total spending is $v_C v_I/(v_C+v_I)$; neither contains $c$, and effort scales as $1/c$.
The invariance holds for any success function that depends only on the ratio of the two efforts, a family characterized by [Skaperdas (1996)](https://doi.org/10.1007/bf01213906); the closed form is specific to this one.

So a common fall in the price of effort changes neither the split nor the money spent: both sides buy more and the bill is unchanged.
Money of the order of the stake is spent whatever $c$ is, a deadweight cost in Aghion and Bolton's sense and not itself an advantage for anyone.
With equal prices the split is symmetric in the stakes; Krier's phone remark is the claim that prices are equal, and I grant it.

Outside the benchmark, which assumes equal capability, there are small experiments on current models.
In Anthropic's Project Deal ([Troy et al. (2026)](https://www.anthropic.com/features/project-deal)), about seventy employees had agents trade items on their behalf, closing a little under two hundred deals averaging about twenty dollars; in runs mixing a stronger and a weaker model, the stronger model's users closed about two more deals each and sold the same item for three to four dollars more, and fairness ratings were the same whichever model had represented the rater.
[Zhu et al. (2025)](https://arxiv.org/abs/2506.00073) simulate consumer negotiations between agents and find that different models obtain significantly different results for their users.
These are trades between individuals and not contests over rules; they show that capability gaps move surplus between users without the losing side perceiving it, so where such gaps exist they add to the positional advantages argued here.

### Organized parties and diffuse groups

This subsection is the main result: a theorem in a model, and the one claim here that is directly about falling $c$.

Take the factory and the residents on the democratic route, and call them the *organized party* and the *diffuse group*; either may be the one seeking the change.
The rule is worth $v$ to the factory and $v$ in total to $n$ residents, $v/n$ each, and it is a public good among the residents: any resident's effort helps all of them.
Effort is measured in units of what it accomplishes.
Either side can buy effort at a price $c$ per unit; before agents this was the price of professional effort (lawyers, lobbyists), and agents lower it.
The price is measured against the cost of personal effort, whose scale the cost function below fixes at one, so a fall in $c$ means purchased effort getting cheaper relative to a person's own attention.
The factory buys $B$.
Each resident can also supply personal effort $a_i$ (attention, turning up, writing) at a private cost $a_i^{1+\alpha}/(1+\alpha)$ with $\alpha > 0$, a cost that rises faster than in proportion, and can buy $b_i$ at price $c$.
A resident's contribution is $e_i = a_i + b_i$, the residents' total is $A = \sum_i e_i$, and they prevail with probability $A/(A+B)$.
Two premises carry the model: personal and purchased effort are interchangeable in the procedure, and the group has no way of binding its members, so each resident chooses its own contribution.

The factory maximizes $vB/(A+B) - cB$, with first-order condition
$$
\frac{vA}{(A+B)^2} = c .
$$
A resident's marginal benefit from another unit of effort is $(v/n)\,B/(A+B)^2$.
Dividing this by the factory's condition shows that it equals $c\,r/n$, where $r = B/A$ is the ratio of the two sides' efforts.

A resident's marginal cost is $e_i^{\alpha}$ while it supplies only personal effort, and $c$ once it buys.
So a resident buys effort only if its marginal benefit reaches $c$, that is, only if $r = n$.
And $r$ cannot exceed $n$, since then every resident would want to buy more, raising $A$.
Hence $r \le n$ always, and the residents' chance of prevailing is
$$
p = \frac{1}{1+r} \;\ge\; \frac{1}{n+1}.
$$

While $r < n$, residents supply personal effort only, with $e^{\alpha} = c\,r/n$, so $A = n\,(c\,r/n)^{1/\alpha}$.
Substituting $A + B = A(1+r)$ into the factory's condition gives $A(1+r)^2 = v/c$, and so
$$
r^{1/\alpha}(1+r)^2 = v\, n^{1/\alpha - 1}\, c^{-(1 + 1/\alpha)}.
$$
The left side increases in $r$, and the right side increases as $c$ falls.
So $r$ rises as $c$ falls, until it reaches $n$ at the price
$$
c^{*} = \left(\frac{v}{n(n+1)^2}\right)^{\alpha/(1+\alpha)},
$$
and stays at $n$ for every lower price.
Below $c^{*}$ each resident supplies personal effort up to the point where its marginal cost reaches $c$, and the group buys the rest; which residents buy is not determined, only the total.

In words: as the price of effort falls, the diffuse group's chance of prevailing falls steadily, reaches $1/(n+1)$ at a positive price, and stays there.
For ten thousand residents the floor is about one chance in ten thousand, against a factory whose stake is no larger than theirs combined.
For illustration, with a stake of 100, twenty residents and $\alpha = 1$, the group's chance is about 0.18 when effort costs 0.85 a unit, about 0.10 at 0.33, and reaches the floor of about 0.05 at a price of about 0.11.

At a high enough price the group is ahead: $r$ is small, and numbers supplying personal effort beat a purse that must buy everything.
Rearranging the expression for $c^{*}$, the floor is reached when the stake exceeds $v^{*} = n(n+1)^2\,c^{(1+\alpha)/\alpha}$, and $v^{*}$ falls with $c$.
So the model does not say that organized parties lose today and will win tomorrow.
It says that at any price the contests with the largest stakes are already at the floor, which fits the observation that organized parties dominate them now, and that as $c$ falls the floor extends to contests with smaller stakes.
Those are the local rules Krier's essay is about, where at present nobody finds it worth hiring a lobbyist.
I cannot say where present prices sit for any particular contest, since the model's units are not calibrated.

A new option cannot by itself make anyone worse off, and it does not here.
Each resident is better off for having the option to buy effort, taking the factory's effort as given.
What lowers the group's chance is that the same fall in price lets the factory buy more, and the factory collects the whole return on what it buys while each resident collects one $n$-th of the return on theirs.
Personal effort, whose cost a resident bears whatever the price of compute, was the group's inframarginal advantage, and cheap purchased effort on the other side swamps it.

With $n = 1$ the floor is one half: one person against a firm with the same stake ends at even odds as $c$ falls.
Krier's phone remark is correct one against one; it fails for a group of $n$ that cannot bind its members.

At the floor the result is that of [Katz, Nitzan & Rosenberg (1990)](https://doi.org/10.1007/bf00139290): when the prize is a public good for a group's members, the group's total effort is set by what one member has at stake (they hold each member's stake fixed as the group grows; here the total is fixed and divided).
Above $c^{*}$, whether a larger group does better or worse at a given price depends on $\alpha$, worse below $\alpha = 1$ and better above it, as the exponent of $n$ in the displayed equation shows; that is the theorem of [Esteban & Ray (2001)](https://doi.org/10.1017/s0003055401003124) for a prize divided among members, on the tendency identified by [Olson (1965)](https://doi.org/10.4159/9780674041660) for larger groups to do worse.

The model takes all $n$ residents to be aware of the contest and taking part at every price.
Before agents many would not have known of it; agents bring them in, which Krier stresses.
That helps the diffuse group and is outside the model, I know of no measurement of its size against the price effect, and it is the qualification on claim (i), cheap purchased effort.

Krier's flash coalition is his answer to numbers.
The model assumes no binding; the flash coalition assumes binding is free.
Three theorems bear on whether a voluntary arrangement can supply the bond, and each says it cannot in its own setting.
[Dixit & Olson (2000)](https://doi.org/10.1016/s0047-2727(99)00089-4) cover the model's own case, where everyone's stake is known: if joining the bargain is voluntary, each party prefers that the others conclude it.
[Mailath & Postlewaite (1990)](https://doi.org/10.2307/2298018) and [Rob (1989)](https://doi.org/10.1016/0022-0531(89)90022-7) cover the case Krier's bargaining club is built for, where each resident's valuation is private and nobody can be forced to take part.
Mailath and Postlewaite show that the chance that any mechanism provides a good whose cost rises with the number served goes to zero as numbers grow; Rob shows that with many residents compensated for a polluting plant, which is Krier's case, the efficient outcome is almost never reached.
Free-riding of this kind is an incentive constraint, not a transaction cost, and these theorems already assume communication is free, so cheaper cognition does not relax them; the bargaining club, as noted earlier, governs members and not joining.
A faithful agent pursues its principal's payoff.
Whether the things that get people to a council meeting, such as anger, loyalty and not wanting to be the one who stayed home, are in that payoff is a design choice Krier leaves open.

I measure compute credits in money.
Fungible credits are income, and if the stake is small beside a resident's income, so that being richer does not change what it will spend on this contest, the price of a unit of effort is still $c$ and the result stands.
Earmarked, non-transferable credits worth $q$ in money per resident buy $A = nq/c$ units, setting aside personal effort, which is small beside what the credits buy once effort is cheap.
The factory's condition gives $A + B = \sqrt{vA/c}$, so
$$
p = \sqrt{\frac{c\,A}{v}} = \sqrt{\frac{nq}{v}} \qquad (nq < v).
$$
Even odds need $nq = v/4$: public money equal to a quarter of the stake, for each contested rule.^[Residents do not buy beyond the quota while $p > 1/(n+1)$, that is, while $nq > v/(n+1)^2$.]
At even odds the factory is also spending a quarter of the stake, since $cB = \sqrt{v\,nq} - nq = v/4$.
That is not the modest fixed outlay Krier compares to funding public roads; it scales with what is at stake in each constitutional question, and someone must decide which contests qualify, which is the central choice Krier wanted to avoid.
The fungible form he prefers for that reason leaves the diffuse group where it was.
Earmarked credits scaled to the stakes are the remedy the model points to, and their price is the point.

[Acemoglu & Robinson (2008)](https://doi.org/10.1257/aer.98.1.267) show that a reform equalizing formal political power can be offset by greater investment in informal power by those who lose from it.
The contest model is one mechanism for that offset: equalize the vouchers, or the votes, and the side whose stake is held in one place spends more to win the contest over how they are used.

### Proposal power

The results here do not depend on $c$; they are background to the claim about drafters.

Krier's equal-vote mode does not equalize the writing of what is voted on, and which issues go to which of his two modes is itself a constitutional choice.
[Romer & Rosenthal (1978)](https://doi.org/10.1007/bf03187594) study an actor with the sole right to put a proposal to a vote against the status quo, where voters can only accept or reject.
The setter proposes its own favourite among the options that beat the status quo, and the worse the status quo is for the voters, the further the setter can pull the result.
[Baron & Ferejohn (1989)](https://doi.org/10.2307/1961664) study majority-rule bargaining over a division, and show that the member recognized to propose obtains a disproportionate share.

Cheap cognition means anyone's agent can now write a proposal, but it does not multiply the right to put one to a vote, nor the attention of those who decide.
The drafter of the voluntary route is the proposer here, and the audit question carries over: a voter's faithful agent deciding how to vote on a drafted rule faces the same hard direction as the residents' agents deciding whether to consent to one.
The difference is that a minority cannot protect itself by refusing, since a majority can adopt the rule whatever a given voter's agent concludes.

Krier's coordination device, described in his section, raises the same issue.
In a *correlated equilibrium* the parties condition their actions on a shared signal.
There are usually many such outcomes, and they differ in who gains.
One can be found efficiently in broad classes of games with many players whose payoffs can be written down compactly, but finding the best one for a given party is NP-hard in most of those classes ([Papadimitriou & Roughgarden (2008)](https://doi.org/10.1145/1379759.1379762)), where NP-hard means at least as hard as a large family of problems, such as scheduling and packing, for which no efficient method has been found.
The advantage here is the proposer's and comes from moving first: whoever proposes the signal chooses among the coordinated outcomes, and the hardness result says only that the others cannot cheaply establish that a better one for them exists.

In a laboratory finding on current models, [Bansal et al. (2025)](https://arxiv.org/abs/2510.25779) built a simulated marketplace in which customer agents choose among offers from business agents.
All the models they tested tended to take the first offer that arrived, and they report that responding first counted for ten to thirty times more than offering better terms.
If this carries over from consumer search to proposals of rules, it favours whoever is placed to propose first: protocol operators and whoever responds fastest, which is a matter of resources.

## Who the incumbents are

The four positions tend to coincide.
A firm is an organized party, usually an entitlement holder over its own assets, and a repeat player with reason to draft.
A large agent provider plainly holds three (it is organized, it writes the protocol and the terms, and its training and terms settle what its agents do where instructions run out), and is an entitlement holder as to its own infrastructure and terms.

Galanter's argument was that the parties with resources and repeat experience come out ahead through structural position, and not through better lawyers alone.
Krier's proposal equalizes the lawyers, and what is left are the four positions.
The entitlement holder keeps its floor, and what $s_0$ gives it while negotiation lasts.
The organized party prevails over a diffuse group of equal stake by up to $n$ to one, in contests whose stakes reach lower as effort gets cheap, in the model.
The drafter may be able to build text others cannot audit, if the analogy holds.
The residual controller decides more as explicit text loses force, if Segal's result carries over.

The models point to remedies for two of the four positions.
For organization, membership can be made binding, so that a diffuse group becomes an organized party, or earmarked credits can be scaled to the stakes.
For drafting, simplicity can be mandated.
It has to be a mandate, because refusing complex text is available to any individual party but leaves $s_0$ in force, so simplicity as a property of the rules actually in force has to be imposed; its cost is the granularity.
The entitlement holder's advantage is answered by the democratic route itself, at the price of the advantages that route confers, and the models offer nothing for the residual controller.
Each remedy needs an authority to impose it, and courts and regulators, the obvious candidates, are themselves residual controllers.

Krier and I agree that non-voluntary institutions are needed; we differ on whether contests over the rules come to be position-independent as cognition gets cheaper, and I have argued that they do not.

## Objections

*Worst-case hardness rarely matters in practice.*
Solvers handle many NP-hard problems routinely, and equilibrium computation in natural games is often easy.
I used the hardness results only to show that the audit cannot be done by solving the mechanism outright, which binds drafter and auditor alike.
The drafting argument rests on the audit's shape as a search and on planted structure, which concerns instances built by an interested party; how often drafters exploit it is an empirical question I cannot answer.

*Agents could be cooperative and make conditional commitments.*
[Tennenholtz (2004)](https://doi.org/10.1016/j.geb.2004.02.002) studies games in which players submit programs that can read one another before play, and [Kalai, Kalai, Lehrer & Samet (2010)](https://doi.org/10.1016/j.geb.2009.09.008) games in which players can verify one another's commitments; agents of this kind can sustain cooperation that faithful agents in an ordinary game cannot.
These are folk theorems, that is, results showing that a very large set of outcomes can each be sustained as an equilibrium.
They make $s_0$ supportable along with everything else; they do not say which outcome is selected, and nothing in them favours a move away from $s_0$.
An agent built to cooperate against its principal's narrow interest is also no longer the fiduciary of Krier's essay, and someone sets the norms it cooperates on.

*Incumbents dominate today as well.*
I agree; in the model the contests with the largest stakes are already at the floor.
The claim is that no advantage shrinks as $c$ falls, and that cheap purchased effort carries the organized party's advantage into smaller contests.

*A large enough coalition becomes an organized party.*
Yes, if membership binds.
A bound coalition with total stake $v$ meets the factory on equal terms in the model.
Binding membership is the non-voluntary element, and someone has to have the authority to bind.

## Tests

Several findings would change my mind.

The test whose failure would count most against the main result is a contest between one buyer of effort and a group whose members each hold a small, costly endowment of personal effort and can also buy effort, with the price of bought effort varied for both sides.
The group's share should fall as the price falls, and level off; a share that holds up would count against (i), cheap purchased effort.

In flash-coalition experiments with privately valued stakes and agents instructed to advocate faithfully for their principals, contribution per member should fall as $n$ grows.
Sustained full contribution at large $n$ without binding rules would count against the free-riding argument.

In audit experiments, we could plant an advantage in a mechanism specification and measure how often an auditor of equal capability detects it, as a function of the number of conditions the specification tests.
Detection that does not fall as that number rises would count against (ii), the audit burden.

In negotiated rules, we could vary the number of conditions a rule tests and the cost of reopening it, and measure how often outcomes are decided by the default allocation of control and not by the negotiated terms.
A rate that rises with neither would count against (iii), the weakening of explicit text.

In repeated agent bargaining over rules, we could vary a small participation cost; agreement rates that approach the zero-cost rate smoothly as the cost shrinks would count against the discontinuity Lee and Sabourian predict.
Proposal power gets no new test, being classical.

The question I most want answered is the one behind (i): how much agents help diffuse groups by bringing their members into contests, against how much they hurt them by letting the other side buy effort cheaply.
Nor do I know how much of the drafting advantage survives an insistence on simple rules once granularity is what people want.
And I do not know who, in Krier's architecture, has the authority to set the non-voluntary rules every remedy here needs, or how that authority would be kept from becoming an incumbent in its turn.
