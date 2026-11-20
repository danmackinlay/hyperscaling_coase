# Revision brief (v3): third draft

You are producing the third draft of `_plans/hyperscaling_coase_constitutional_complexity_2.qmd` by rewriting the second draft in place.

Read, in order: the second draft (that file); Seb Krier's essay <https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale>; `_voices/dan_voice.md`; the "Hard constraints" section of `_tmp/coase_constitutional_2/brief.md`; and, for the explanations it specifies of each cited result, `_tmp/coase_constitutional_2/brief_v2.md`.
All hard constraints still apply (no other `hyperscaling_coase` file, no other essay in the repo, no new facts or citations beyond the briefs and the drafts, one verbatim Krier quotation, one sentence per line, Oxford `-ize`, "I"/"we" never indefinite "you", no colons in headings, no banned words, no mode labels, same citation URLs, frontmatter keys and TODO comment intact, edit only this file, no git).
Where this brief and v2 conflict, this brief wins. Where this brief is silent, keep the second draft.

## Why a third draft

A second cold reader could follow the explanations but found faults in the argument and the structure. In order of weight:

1. The benchmark was stated three ways that do not agree, and attributed to Krier although the article had just reported that he concedes entitlements decide distribution.
2. The thesis is about the cost of cognition $c$, but two of the three "widening" claims are about granularity, and nothing connected the two.
3. The organized-versus-diffuse result compared two separate models (linear cost, quadratic cost). Giving residents the option of buying compute cannot make them worse off by itself, so the comparison did not show what the text said. **The result has been re-derived in a single model in which $c$ is a parameter; the new derivation is below and replaces the old one.**
4. "Incumbent" was unclear when the positions are split between opposing sides, as they are in the article's own running example.
5. The drafting analogy never said what in a rule corresponds to the planted structure, or why auditing is search and not verification; and its example ended with the non-drafter protected.
6. The Aghion & Bolton step was asked to carry more than it can.
7. The Summary section was introduction, definitions, roadmap and literature review at once (116 lines), and the roadmap gave equal billing to results that carry the thesis and results that are background.
8. Too long for its argument.

## New structure

```
## Summary                      (short: what is claimed, in about fifteen lines, then the grouped list)
## Krier's argument             (everything the reader needs to know about the essay, in one place)
## Setup                        (two levels; terms; four positions; the benchmark; strength of each claim; scope; related work)
## The voluntary route
### The status quo as a floor   (baseline; short)
### Drafting and auditing
### Incompleteness and residual control
### Costly negotiation
## The democratic route
### Contests between buyers of effort   (a lemma)
### Organized parties and diffuse groups (the theorem about c)
### Proposal power                       (background; short)
## Who the incumbents are
## Objections
## Tests
```

Target 7,000 to 8,000 words. Cuts to make: the provider-backdoor paragraph (reduced to one footnote, see below); the remark on Krier's "constant renegotiation is expensive" in the contest subsection; the emotions conjecture (reduced to two sentences); the repeated statement of the disagreement with Krier at the end (one sentence there, pointing back); the restatement of the operational/constitutional distinction in the first voluntary-route subsection; the zero-knowledge definition; the Conitzer & Sandholm citation; the "title should be read that way" remark; the sentence about a faithful agent thinning the veil.

## Summary section

About fifteen lines of prose, no definitions beyond what a sentence can carry, then the list.
Content: what Krier claims (one or two sentences); what is granted; the question (what happens when agents negotiate the rules); the answer in plain words (four positions a party can hold when negotiation starts, each of which confers an advantage that cheap cognition does not remove; for one of them a model says the advantage grows as cognition gets cheaper; for two it grows with the detail of the rules); that the remedies the models point to are non-voluntary.
Then the list, grouped under the two routes, each item tagged with its role:

Voluntary route
1. The status quo as a floor. *Baseline, conceded by Krier.* (entitlement holder)
2. Drafting and auditing. *Carries the claim for the drafter; an analogy.*
3. Incompleteness and residual control. *Carries the claim for the residual controller; an extrapolation.*
4. Costly negotiation. *Carries the claim for the entitlement holder; one model.*

Democratic route
5. Contests between buyers of effort. *A lemma: among parties that buy all their effort, the price of effort changes nothing.*
6. Organized parties and diffuse groups. *The main result: a theorem in a model, and the one claim here that is directly about falling $c$.*
7. Proposal power. *Background: classic results that do not depend on $c$.*

## Krier's argument (new section; gather everything here)

All of: Coase's theorem stated in one sentence for the reader who does not know it (if bargaining were costless, the parties to an externality would reach the efficient arrangement whoever started with the right, though who starts with it decides who pays whom); Krier's claim that agents remove the bargaining costs; one or two of his examples; his concession (the permitted quotation); **his reassurance, which is what the article tests**: agents make the allocation explicit, contestable and cheap to renegotiate (voluntary route), and improve the democratic systems that amend it (democratic route, with the gloss of liquid delegation); his two modes (bargaining by willingness to pay, and decisions in which each person's vote counts equally, with agents moving between them by issue); his cost argument, with the billionaire's-phone remark introduced as "I read this as the claim that both sides face the same price for reasoning"; the bargaining club (with why members do not overstate: a member is paid the common clearing price, not its own declared number, and overstating risks killing the deal); the three coercive devices (Harberger-style fee as Krier describes it; reimbursement with the loss quantified by agents); flash coalitions (the agents of ten thousand residents forming a coalition at once and naming a single price, which he presents as a counterweight to concentrated wealth); compute credits in two forms (targeted vouchers for civic uses; a universal allocation people spend as they like, which he prefers to avoid a planner choosing categories), which he compares to the modest cost of public roads; and his statement that the state stays as enforcer and that non-voluntary institutions are needed.
Do NOT introduce his three nested layers here; introduce them in the residual-control subsection, where they are used.
Nothing about Krier should appear for the first time later in the article, except those three layers.

## Setup section

**Levels, terms.** As in the second draft (operational/constitutional with the criterion; $s_0$; faithful agent; granularity, defined as the number of distinct conditions a rule tests; unit cost of cognition $c$, effective units).

**Positions.** The four, as in the second draft. Flag the organized party's defining property as the one the main result turns on: its members are already bound. Add: positions can be held by opposing sides (in Krier's factory example the residents hold the entitlement and the factory is organized). Then each advantage accrues to whoever holds that position. The article does not offer a rule for which position prevails in general; it shows that on the voluntary route the entitlement holder's veto is decisive, and on the democratic route organization and proposal power are. "The incumbents" of the title are the holders of these positions.

**The benchmark, once.** *Position-independence*: two sides with equal total stakes in a rule and equally capable faithful agents do equally well, measured by each side's chance of prevailing or share of what is at stake, whichever positions they hold. State why this is the right test of Krier, since he concedes that entitlements decide distribution: his reassurance is that the allocation can be contested cheaply and amended by an improved democratic process. That reassurance is worth something only if contests over the allocation are not themselves decided by position. Then which positions he addresses: the entitlement holder (conceded at the operational level, said to be contestable at the constitutional level); the organized party (flash coalitions and compute credits are his answer); the drafter and the residual controller (not addressed). Delete the second draft's two route-specific benchmark sentences ("every rule change that benefits all affected parties gets made" is a statement about efficiency and is compatible with any degree of dependence on position).

**What is claimed, and how strongly.** One paragraph, then three short items.
Main claim: for each of the four positions, the advantage does not shrink towards position-independence as $c$ falls.
Stronger claims, each with its strength and its premise:
- (i) *Linear effort prices.* The organized party's advantage over a diffuse group grows as $c$ falls, and reaches its maximum at a positive $c$. A theorem in a model that isolates the price of effort. Outside the model, agents also bring into the contest residents who would otherwise not have known of it or taken part; that helps the diffuse group, and the relative size of the two effects is unmeasured.
- (ii) *The audit burden.* The drafter's advantage grows with granularity. A conjecture by analogy.
- (iii) *The weakening of explicit text.* The residual controller's advantage grows with granularity when renegotiation is cheap. An extrapolation from a two-party model.
- (ii) and (iii) are about granularity, not $c$. They bear on the main claim through a premise, which is Krier's own: cheap cognition is what makes fine-grained rules possible, so granularity rises as $c$ falls. State this premise here, explicitly, and refer back to it in both subsections.
Do not write "the models say it widens" of (ii) or (iii).

**Scope.** Three limits (not "four"): operational gains granted and no claim that present institutions do better; agents assumed capable, cheap and faithful; results are theorems about models, and the few experiments are labelled as such where they appear (not "reported separately").

**Related work.** The three papers, then the bodies of theory used, now five: bargaining theory, social choice, contest theory and collective action, computational complexity, incomplete contracts.

## The voluntary route

Opening paragraph: on this route a rule changes only with the consent of every party whose entitlement it touches. Say what each subsection contributes (floor; drafter; residual controller; cost of negotiating) without claiming that all four are about $c$.

### The status quo as a floor (at most about 25 lines)
- Buchanan & Tullock and Rae, as in the second draft, briefly.
- The floor: any change needs each holder's consent, so no holder ends below what $s_0$ gives it. This follows from consent alone. It is symmetric (every party with a veto has the floor); the asymmetry is all in $s_0$, which is Krier's concession. Say that this subsection restates the concession and adds two things.
- Addition one: the three coercive devices cannot be adopted on this route. Give the reason for each in a clause (each takes something from a holder who holds out: voting weight, a fee on its declared price, a reimbursement), then the Buchanan & Tullock objection and the answer (their unanimous adoption of non-unanimous rules needs parties who do not know which side they will be on; here $s_0$ exists and Krier starts from existing rights, so the likely holdouts know who they are). So those devices need the democratic route; Krier names democratic systems as the mechanism for changing entitlements (do not write "for exactly this purpose").
- Addition two: the holder keeps what $s_0$ gives it for as long as negotiation lasts, and [Binmore, Rubinstein & Wolinsky (1986)] show that this income during the dispute is what sets bargaining positions when bargaining takes time ([Nash (1950)] for the notion of a disagreement point, glossed). So delay costs the challenger and not the holder. The costly-negotiation subsection returns to this.
- Aghion & Bolton, reduced to two or three sentences and to what it can bear: a normative result (which rule would parties choose if they did not know who would gain from future changes) that some majority rule is preferred to unanimity whenever compensating the losers from a change carries deadweight costs, glossed. So whether the voluntary route suffices depends on whether such costs vanish with $c$; the subsections on drafting and on costly negotiation each describe a cost that does not. Do not say the result "sends us" anywhere, and delete the callback to it at the end of the voluntary route.

### Drafting and auditing
Rewrite in this order.

1. **Mechanism and the audit question.** A mechanism as before. The audit, restated as a question: *is there a contingency in which this rule leaves my principal worse off than $s_0$ would?* A contingency here is a combination of the conditions the rule tests together with what the parties do in response. (Equilibrium: gloss as before, adding "of the kind suited to parties with private information" so the economist does not object.)
2. **Two properties of that question.**
   - It cannot be answered by solving the mechanism outright: finding an equilibrium is PPAD-complete even with two players [Daskalakis, Goldberg & Papadimitriou (2009); Chen, Deng & Teng (2009)]; gloss PPAD as problems where a solution is known to exist but no efficient way of finding one is known or expected. This is a worst-case result, and it binds the drafter as much as the auditor, so it is not the source of any advantage.
   - It is a search problem with a particular shape. A bad contingency, once pointed out, is quick to check. Finding one means searching combinations of conditions, and the number of combinations grows exponentially with the number of conditions the rule tests, that is, with granularity. For the computer scientist: this is the shape of problems in NP, quick to verify and possibly slow to search. For the economist: checking a claimed arbitrage is quick; finding one is the hard part.
   - Move the correlated-equilibrium material out of this subsection entirely (to "Proposal power").
3. **The planted-structure result.** As in the second draft, with two expansions: one more sentence on the textbook view (pooling many assets and slicing the pooled cash flow lets the seller sell the slices whose value hardly depends on what it privately knows, and keep the rest); and the factoring illustration made concrete (a contract that pays out if some future number, say a digit of next year's unemployment rate, equals the last digit of a factor of a given huge integer: whoever chose the integer by multiplying two primes knows the factors and can value the contract; nobody else can without factoring it). Keep the two-ingredients sentence.
4. **The analogy, with its parts named.** State the label first (an argument by analogy from financial products to rules, not a corollary; no measurement of how often negotiated rules fall in the hard regime). Then the correspondence: the table of which derivative references which asset corresponds to the rule's many conditions and clauses; the hidden dense cluster corresponds to a particular combination of conditions under which the clauses interact to the drafter's benefit; the seller's knowledge of which assets are bad corresponds to the drafter's private knowledge of which combinations will in fact arise, because they depend on its own plans (a firm knows its expansion plans; its neighbours' agents do not). The drafter works in the easy direction: it starts from that combination and writes clauses that produce the outcome it wants there. It does not need the best possible mechanism, only one that contains its combination. The auditor works in the hard direction: it must search. So the advantage does not depend on unequal compute or on any agent being unfaithful; a faithful drafting agent is doing its job.
5. **Granularity and $c$** (this is (ii)). The search space grows exponentially in the number of conditions; the cost of checking any one combination falls in proportion to $c$. Under the premise from the Setup that granularity rises as $c$ falls, brute-force audit keeps up only if $c$ falls exponentially faster than granularity rises. Clever search beats brute force on ordinary instances; the planted-structure results say it does not on instances built by an adversary. Whether drafted rules are such instances is the conjecture.
6. **Who drafts.** The advantage attaches to the act of drafting with private information, and any party may do it, including a well-informed challenger. Three things decide who does most of it: protocol operators and agent providers by default; organized parties, because drafting is effort and an organized party's effort exceeds a diffuse group's by up to $n$ to one (forward reference to the main result; do not say "by a wide margin"); repeat players, who have more private information worth building in [Galanter (1974)], as in the second draft.
7. **What the asymmetry does on this route** (replaces the second draft's example paragraph; this fixes the example that undercut itself). As in the financial case, a party that cannot audit cannot tell a clean proposal from a tampered one. It has two responses. It can accept complex text, and then the drafter gains. Or it can refuse all complex text, and then $s_0$ stays. Take Krier's factory and ten thousand residents negotiating, through faithful agents, the mechanism for pricing later disputes, and suppose the residents hold the entitlement to clean air under $s_0$. If their agents refuse what they cannot audit, the residents are protected, and the cost is the fine-grained mechanism that might have benefited both sides, which is never adopted. The beneficiary of the impasse is whoever $s_0$ favours, here the residents, elsewhere the firm. So on the voluntary route the asymmetry favours the drafter where its text is accepted and the entitlement holder where it is refused; in neither case do outcomes come to track stakes. On the democratic route a minority cannot refuse, and the asymmetry favours the drafter directly (forward reference to "Proposal power").
8. **Replies.** Proofs: a drafter could attach a formal proof that a rule has a stated property (no zero-knowledge). Two limits: the property has to be written down, and "no contingency disadvantages my principal" is exactly what cannot be fully written (next subsection); and a demand for proof is a condition on consent, which works only where the drafter would sooner supply the proof than stay at $s_0$. Simplicity: accept it, as in the second draft, and state the trade-off corrected: the rules stay coarse, which is what Krier set out to replace and which leaves $s_0$'s allocation in place, or they favour the drafter.

### Incompleteness and residual control
Keep the second draft's version with these changes.
- Describability: keep to two sentences; make the first concrete (if a contract must be a finite text that a procedure can execute, some arrangements that depend on the state of the world in the right way cannot be written); keep "these show only that gaps exist".
- Segal: before the result, say what the sunk investment is in rule-making, since hold-up needs one: parties act in reliance on a rule (a firm builds where the fee formula makes it worthwhile; a household buys where the noise rule suits it), and a rule that can be reopened after they have done so exposes them to renegotiation from a weaker position. Maskin & Tirole: add the reason in a clause (a contract can make the outcome depend on reports the parties make later about their payoffs).
- Krier and Segal's conditions, corrected. Segal's condition is that the parties cannot commit not to renegotiate; Krier's feature is that renegotiation is cheap and continuous. Say that these differ and how they connect: Krier proposes that some rules harden by mutual agreement while others stay perpetually negotiable. For the rules he keeps negotiable, the absence of commitment is the design. For the rules he would harden, something has to enforce the hardening against parties who would later both prefer to reopen, and that enforcer is outside the agents. So the argument applies to the negotiable class, which is where his fine-grained examples live.
- Then (iii), with the label and with the premise from the Setup connecting granularity to $c$.
- Grossman & Hart / Hart & Moore step as in the second draft.
- Residual controllers, in order and uninterrupted. Introduce Krier's three nested layers HERE (the law as outer boundary; a market of agent providers, where he relies on competition to drive out agents that serve someone other than their user; the individual, whose agent is their advocate within the law and the provider's terms). Then: owners of assets; the provider (with the analogy and Hadfield-Menell & Hadfield, after the list item, not in the middle of the list); courts and regulators. Attach ONE footnote to the provider item, replacing the deleted backdoor paragraph: whether a user can verify that a supplied agent is faithful is outside this article's scope, which assumes it; [Goldwasser, Kim, Vaikuntanathan & Zamir (2022)] give constructions in which a model's trainer plants a backdoor that no efficient observer can detect, a possibility result and not a claim about deployed models.
- Closing: as in the second draft.

### Costly negotiation
Keep the second draft's version with these changes.
- "A participation cost is positive whenever $c$ is": give the reason (it is $c$ times the least amount of work needed to read and assess a proposal, and that amount is positive).
- Describe the Anderlini & Felli (2001) cost structure in a clause (each side must pay a fixed amount at the start of every round for that round to take place). Describe Rubinstein's model in a clause (two parties alternate offers on how to divide a surplus, and delay is costly). Attribute the Rubinstein extension to Lee & Sabourian ("they show the same in...").
- The gloss, corrected for what it does and does not show: it explains why never bargaining can be an equilibrium (against a counterpart who never pays, paying is wasted, and never paying is about the simplest strategy there is); that no other equilibrium survives is the authors' result. Put the note on sources in a footnote: I worked from the published abstract and a companion working paper, and have not checked the proof.
- Order: the Krier sentence (the arrangement that takes least computation to sustain is the one in force) comes BEFORE "That is all I use it for", not after.
- Close with the delay point (referring back to the floor subsection). Delete "or simpler text" and the Aghion & Bolton callback.

## The democratic route

Opening: a rule can change over a holder's objection by whatever majoritarian procedure $s_0$ provides. Then the modelling assumption, stated as one: the parties directly affected by a rule are usually a small part of those who decide it (ten thousand residents in a city of a million), so the outcome turns on influence over the unaffected majority, their agents and their delegates: drafting the proposal, making the case, answering the other side, monitoring. I treat that influence as a contest in which each side's chance of prevailing rises with its share of the total effort. It is a reduced form, not a model of voting.

### Contests between buyers of effort (a lemma; compress)
- Two sides who buy all their effort. Label them $C$ (seeking the change) and $I$ (defending $s_0$), and say the label confers no advantage in this model. Tullock success function glossed; first-order conditions; $\theta_i = v_i/c_i$; results $p_C = \theta_C/(\theta_C+\theta_I)$ and total spending $(v_C+v_I)p_C(1-p_C)$. Keep the derivation but shorter than the second draft: state the two first-order conditions, the ratio, the two results, and the equal-cost case; drop the lines on effort in physical units except the one fact that effort scales as $1/c$.
- Generalization in one sentence: the invariance holds for any success function that depends only on the ratio of the two efforts, a family characterized by [Skaperdas (1996)]; the closed form is specific to this one.
- What it is for: among parties that buy all their effort, a common fall in the price of effort changes neither the split nor the money spent; both sides buy more and the bill is unchanged. Money of the order of the stake is spent whatever $c$ is; this is a deadweight cost in Aghion & Bolton's sense and not itself an advantage for anyone. With equal prices the split is symmetric. Krier's phone remark is the claim that prices are equal; granted.
- Capability evidence, three sentences, marked as outside the benchmark (which assumes equal capability): Project Deal with the base numbers; Zhu et al.; so where capability is unequal the gap is larger than in the benchmark case, and the Project Deal participants did not perceive it.

### Organized parties and diffuse groups (the main result; replace the second draft's derivation with this)

**Setting.** The factory and the residents on the democratic route. Call them the *organized party* and the *diffuse group*; either may be the one seeking the change. The rule is worth $v$ to the factory and $v$ in total to $n$ residents, $v/n$ each, and it is a public good among the residents (any resident's effort helps all). Effort is measured in units of what it accomplishes. Either side can buy effort at a price $c$ per unit: before agents this was the price of professional effort (lawyers, lobbyists), and agents lower it. The factory buys $B$. Each resident can also supply personal effort $a_i$ (attention, turning up, writing) at a private cost $a_i^{1+\alpha}/(1+\alpha)$ with $\alpha > 0$, which rises faster than in proportion, and can buy $b_i$ at price $c$. A resident's contribution is $e_i = a_i + b_i$, and $A = \sum_i e_i$. The residents prevail with probability $A/(A+B)$.
Two premises, stated as premises: personal and purchased effort are interchangeable in the procedure; and the group has no way of binding its members, so each resident chooses its own contribution.

**Derivation** (show these steps).
- The factory maximizes $vB/(A+B) - cB$: first-order condition $vA/(A+B)^2 = c$.
- A resident's marginal benefit from another unit of effort is $(v/n)\,B/(A+B)^2$. Dividing by the factory's condition, this equals $c\,r/n$, where $r = B/A$ is the ratio of the two sides' efforts.
- A resident's marginal cost is $e^{\alpha}$ while it supplies only personal effort, and $c$ once it buys. So a resident buys effort only if its marginal benefit reaches $c$, that is only if $r = n$; and $r$ cannot exceed $n$, since then every resident would want to buy more, raising $A$. Hence $r \le n$ always, and the residents' chance of prevailing is
$$p = \frac{1}{1+r} \;\ge\; \frac{1}{n+1}.$$
- While $r < n$ residents supply personal effort only, with $e^{\alpha} = c\,r/n$, so $A = n\,(c\,r/n)^{1/\alpha}$. Substituting $A + B = A(1+r)$ into the factory's condition gives $A(1+r)^2 = v/c$, and so
$$r^{1/\alpha}(1+r)^2 = v\, n^{1/\alpha - 1}\, c^{-(1 + 1/\alpha)}.$$
- The left side increases in $r$; the right side increases as $c$ falls. So $r$ rises as $c$ falls, until it reaches $n$ at the price
$$c^{*} = \left(\frac{v}{n(n+1)^2}\right)^{\alpha/(1+\alpha)},$$
and stays at $n$ for every lower price.

**Result, in words.** As the price of effort falls, the diffuse group's chance of prevailing falls steadily, reaches $1/(n+1)$ at a positive price, and stays there. For ten thousand residents the floor is about one chance in ten thousand, against a factory whose stake is no larger than theirs combined. A numerical illustration (I computed these; keep them rounded): with a stake of 100, twenty residents and $\alpha = 1$, the group's chance is about 0.18 when effort costs 0.85 a unit, about 0.10 at 0.32, and reaches the floor of about 0.05 at a price of about 0.11.

**Why, in words** (this answers the objection that a new option cannot hurt). Each resident is better off for having the option to buy effort, taking the factory's effort as given. What lowers the group's chance is that the same fall in price lets the factory buy more, and the factory collects the whole return on what it buys while each resident collects one $n$-th of the return on theirs. Personal effort, whose cost a resident bears whatever the price of compute, was the group's inframarginal advantage, and cheap purchased effort on the other side swamps it.

**The case $n = 1$.** The floor is one half: one person against a firm with the same stake ends at even odds as $c$ falls. Krier's billionaire's-phone point is correct one against one. It fails for a group of $n$ that cannot bind its members.

**Relation to the literature** (short). At the floor the result is that of [Katz, Nitzan & Rosenberg (1990)]: when the prize is a public good for a group's members, the group's total effort is set by what one member has at stake (they hold each member's stake fixed as the group grows; here the total is fixed and divided). Above $c^{*}$, whether a larger group does better or worse at a given price depends on $\alpha$, with the threshold at $\alpha = 1$; that is the theorem of [Esteban & Ray (2001)] for a prize divided among members, on the tendency identified by [Olson (1965)] for larger groups to do worse. Two sentences; no separate linear, quadratic and general cases.

**What the model leaves out.** It takes all $n$ residents to be aware of the contest and taking part at every price. Before agents many would not have known of it; agents bring them in, which Krier stresses. That helps the diffuse group and is outside the model, and I know of no measurement of its size against the price effect. This is (i).

**Flash coalitions.** As in the second draft, with the mapping stated: the model assumes no binding; Krier's flash coalition assumes binding is free. [Dixit & Olson (2000)] is the theorem for the model's own case, where everyone's stake is known: if joining is voluntary, each party prefers that the others conclude the bargain. [Mailath & Postlewaite (1990)] and [Rob (1989)] cover the case Krier's bargaining club is built for, where each resident's valuation is private: glosses as in v2. Do not repeat that the club does nothing about non-joiners if the Krier section already said it; refer back. Then two sentences only on motive: a faithful agent pursues its principal's payoff, and whether the things that get people to a council meeting are in that payoff is a design choice Krier leaves open.

**Compute credits**, in money. Fungible credits are income; assuming the stake is small beside a resident's income, so that being richer does not change what it will spend on this contest, the price of a unit is still $c$ and the result stands. Earmarked, non-transferable credits worth $q$ in money per resident buy $A = nq/c$ units. The factory's condition gives $A + B = \sqrt{vA/c}$, so
$$p = \sqrt{\frac{c\,A}{v}} = \sqrt{\frac{nq}{v}} \qquad (nq < v).$$
Even odds need $nq = v/4$: public money equal to a quarter of the stake, for each contested rule, and at even odds the factory is also spending a quarter of the stake. Footnote: residents do not buy beyond the quota while $p > 1/(n+1)$, that is while $nq > v/(n+1)^2$. Then the two points about Krier as in the second draft (not a modest fixed outlay; someone decides which contests qualify; the fungible form leaves the group where it was), and say plainly whether this is offered as a remedy: it is the remedy the model points to, and its price is the point.
End with Acemoglu & Robinson as in the second draft.

### Proposal power (background; short)
- Say at the top that the results here do not depend on $c$ and are background to the claim about drafters.
- Krier's two modes were introduced in the Krier section; refer back. Equal votes do not equalize the writing of what is voted on.
- Romer & Rosenthal; Baron & Ferejohn; glossed as in the second draft.
- What cheap cognition does and does not open up: anyone's agent can now write a proposal; the right to put one to a vote, and the attention of those who decide, are not multiplied by it.
- The drafter is the proposer, and the audit question carries over; a minority cannot protect itself by refusing.
- Correlated equilibrium, introduced here with its role in Krier (he describes agents as a coordination device that lets parties condition on shared signals and reach outcomes that uncoordinated play would miss): one such outcome can be found efficiently in broad classes of games with many players whose payoffs can be written down compactly, but finding the best one for a given party is NP-hard in most of those classes [Papadimitriou & Roughgarden (2008)], NP-hard glossed (at least as hard as a large family of problems, such as scheduling and packing, for which no efficient method has been found). So whoever proposes the signal chooses among the coordinated outcomes unless others can produce and check an alternative.
- Bansal et al., as in the second draft, ending with who is placed to propose first: protocol operators and whoever responds fastest, which is a matter of resources.
- Fold in, as a clause and not a paragraph: which issues go to which of Krier's two modes is itself a constitutional choice.

## Who the incumbents are
- Positions coincide, as in the second draft; for the provider say it holds three plainly (organized, drafter, residual controller) and is an entitlement holder as to its own infrastructure and terms.
- Galanter, then what is left after the lawyers are equalized, one line per position, each at the strength the body gives it: the entitlement holder keeps its floor and what $s_0$ gives it while negotiation lasts; the organized party's advantage over a diffuse group grows to $n$ to one as effort gets cheap, in the model; the drafter may be able to build text others cannot audit, if the analogy holds; the residual controller decides more as explicit text loses force, if Segal's result carries over.
- Remedies: the models point to remedies for two of the four positions. For organization: binding membership, or earmarked credits scaled to the stakes. For drafting: mandated simplicity (with the reason a mandate is needed, as in the second draft, and its cost: it gives up the granularity). None for the entitlement holder beyond the democratic route itself, and none for the residual controller. REMOVE "non-unanimous amendment" from the list of remedies. Each remedy needs an authority to impose it, and courts and regulators are themselves residual controllers; say so here.
- One sentence on the disagreement with Krier, pointing back to the Setup; not the four-sentence repeat.

## Objections
As in the second draft, with: the hardness objection answered by reference to the search-and-planted-structure argument; the folk-theorem reply ending "they do not say which outcome is selected, and nothing in them favours a move away from $s_0$" (delete "I expect $s_0$ to be the likely selection"); a gloss for the economist on what Tennenholtz studies (players submit programs that can read one another before play); "incumbents dominate today" answered with the claim as now stated (the advantage does not shrink as $c$ falls, and for the organized party the model says it grows).

## Tests
- First, and marked as the one whose failure would count against the main result: a contest between one buyer and a group whose members each hold a small costly-effort endowment and can also buy effort, with the price of bought effort varied for both sides; the group's share should fall as the price falls and level off. A share that holds up as the price falls would count against (i).
- Flash coalitions (free-riding) as in the second draft; audit detection, now against the number of conditions the specification tests and not its length; the incompleteness test; the participation-cost test.
- Say that proposal power gets no new test, being classical.
- Open questions as in the second draft.

## Abstract
Rewrite to match: Krier's reassurance and the benchmark of position-independence in one clause each; four positions; the main result stated as what it is (in a model, the organized party's advantage over a diffuse group of equal stake grows as effort gets cheaper, to $n$ to one); (ii) and (iii) with their labels and the granularity premise; remedies non-voluntary. About 170 words.

## Final note to return
Word count; departures and why; any instruction you think makes the argument worse; whether every step of the new derivation checked when you re-derived it; any `TODO:` inserted.
