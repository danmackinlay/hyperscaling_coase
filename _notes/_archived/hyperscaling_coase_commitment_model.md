# The commitment model, written down simply

> **Attacked 2026-10-21, later the same day, by six independent reviewers.** The text below is left exactly as it stood, so that the quotations in the findings resolve. The findings, in plain words, are in `hyperscaling_coase_commitment_model_findings.md`; the one-page report is `hyperscaling_coase_commitment_model_brief.md`; the reviewers' collation is `hyperscaling_coase_commitment_model_redteam.md`. In short: cells B and C stand; cell A's split is wrong on the river (four veto players give the residents three quarters, not half); cell D is asserted, not derived, and the cited papers make the standoff one of three outcomes under reliable commitment and unique only under slightly unreliable, simultaneous, unconditional, once-off commitment, with probability $q^2$; the compute claims fail in D and narrow in B; the race at $k=1$ fails; the yardstick sentence is wrong both ways; the Krier mapping fails on the developer, the club and the reimbursing veto. A replacement thesis is proposed in the findings, for Dan's decision.

Written 2026-10-21. This is the calculation the rebuilt essay needs and nobody has done: the river with commitment added, in four cells, and a stated meaning for "as the agents' computing budgets rise". It is written for a reader who knows the river and nothing else, with every word explained. Symbols are collected at the end. It has not been attacked yet.

## 1. The river, in one paragraph

A factory upstream wants to pollute. Three residents live downstream. If the factory pollutes it earns a profit of $\pi$; resident $i$ suffers a harm of $h_i$. The harms are $h=(2,3,9)$, so they add up to $14$. Take $\pi=20$: polluting earns $20$ and costs $14$ of harm, so the world is $6$ better off if the factory pollutes *and pays the residents for their harm*. That $6$ is the pie. Who gets the slices is the whole question. The rule we use is unanimity, $k=n=3$: the factory may pollute only if all three residents sign. That is the rule in Krier's own large examples, a developer who needs every homeowner, a beach closure that needs everyone who loses access. A resident who signs gets a payment; a resident who does not sign gets nothing and the river stays clean, which is worth $0$ to everyone.

Two ways of scoring an outcome. The first is *efficiency*: does the deal that creates the $6$ happen at all? The second is *the residents' share*, which I will write $S$: of the $6$ slices, how many go to the residents after they have been paid their harm? $S=1$ means the residents got the whole pie, $S=0$ means the factory kept it, $S=\tfrac12$ means they split it. (The essay's own yardstick, "is anyone worse off than under no deal", turns out not to tell the cells apart, because unanimity protects everyone's no-deal position in all of them. That yardstick is too weak for the question. The share is the right one.)

## 2. What "commit" means, and its unit

To *commit* is to tie your own hands so that you cannot accept less than some position, and to prove it to the other side. A twelve-year-old does it like this: "I promise to give my pocket money to my sister if I ever accept fewer than four slices", written down and shown to the other side. The pocket money is the point. Backing down now costs you something, so your threat to walk away is believable.

The unit of commitment is therefore money: the **revocation cost**, written $r$, the amount you lose if you back down from your published position. $r=0$ means you have not committed at all; you can say anything and change your mind for free. A large $r$, larger than any slice of pie you could gain by backing down, means your position is as good as fixed. This is Crawford's 1982 formulation and it is the standard one. "Cheap commitment" means that setting up such a promise costs almost nothing and the other side can check it, which is what an agent that publishes its instructions and a hash of them provides, and what humans have always found hard, since for humans a believable promise to walk away has meant burning a bridge or staking a reputation.

So each side, before bargaining, may publish a **position** (the share of the pie it insists on) and a revocation cost $r$. The factory's position is $d_f$ slices for itself; the residents', bargaining as one, is $d_N$ slices for themselves. If $d_f+d_N\le 6$ the positions are compatible and each side gets what it asked for. If $d_f+d_N>6$ they are incompatible, and somebody has to back down and pay their $r$, or nobody does and there is no deal.

## 3. The four cells

Each cell is a different answer to "who can commit?" In each I say what the two sides do, what happens, and the score.

**Cell A: neither side can commit** ($r_f=r_N=0$). Both sides can talk, threaten and change their minds for free. This is ordinary haggling over six slices between two parties who each need the other. The standard answer, which is what happens in experiments too, is that they split it: three and three. Each resident gets their harm back plus a bit of the three. *Efficient; $S=\tfrac12$.* This is roughly where humans start, because human commitment is expensive.

**Cell B: only the factory can commit** ($r_f$ large, $r_N=0$). The factory publishes: "I pay each of you exactly your harm, $2$, $3$ and $9$, and not a cent more, and I have tied my hands." The residents can accept, and be exactly as well off as with a clean river, or refuse, and have a clean river. They are indifferent, so a penny more makes them accept. The factory keeps all six slices. *Efficient; $S=0$.* This is a take-it-or-leave-it offer, and it is what a developer's standard-form offer to every homeowner looks like.

**Cell C: only the residents can commit** ($r_N$ large, $r_f=0$). The residents publish: "We sign only if we are paid $20$ between us, and we have tied our hands." The factory can accept, and earn $20-20=0$, exactly as if it had not polluted, or refuse. It is indifferent, so a penny makes it accept. The residents keep all six slices. *Efficient; $S=1$.* This is a union with a rule against side deals, and it is Krier's "digital union" of residents' agents naming one price. Notice what it needs: the three residents must commit *as one*, which means they first settle among themselves how to split their six, and the factory must be unable to offer resident 3 alone a better deal. Under unanimity the factory needs all three anyway, but the pact still has to be enforced among the residents, or resident 3, who has the most to lose from no deal, breaks first.

**Cell D: both sides can commit** ($r_f$ and $r_N$ both large). The factory publishes "I keep all six" and the residents publish "we take all six", each with their hands tied. The positions are incompatible, neither can back down without paying more than the pie is worth, so nobody backs down. No deal. The river stays clean, which at $\pi=20$ is the wrong outcome: six slices of pie that could have existed do not. *Inefficient; there is no pie to share.* This is impasse. The result that this is what happens when committing is free and provable is Ellingsen and Miettinen 2008, and with a small cost of committing the standoff still happens with positive probability; Crawford 1982 has the same conclusion with revocation costs. (Both as reported by the economist in the red-team; verify before citing.)

| | Residents cannot commit | Residents can commit as one |
|---|---|---|
| **Factory cannot commit** | A. Haggling. Split 3 and 3. Efficient, $S=\tfrac12$. | C. Union. Residents take the pie. Efficient, $S=1$. |
| **Factory can commit** | B. Take it or leave it. Factory takes the pie. Efficient, $S=0$. | D. Standoff. No deal. Inefficient, no pie. |

## 4. What cheap agents do to the table

Humans sit near cell A by default, because for a human a believable commitment is costly to make. An agent that can publish its instructions and prove it has done so makes commitment cheap for whoever has an agent. If both sides have one, the default moves from A to D. That is the first claim: **cheap, provable commitment on both sides turns haggling into standoffs**, and it is the opposite of the agenda's promise, which is that agents turn haggling into deals.

The way out of D is a rule that lets one side commit and forbids the other from matching it, which lands the game in B or C. A liability rule, "the factory may pollute but must pay each resident a set amount", is cell B written into law: the factory's position is fixed by the statute and the residents have nothing to commit to. A union rule, "the residents bargain as one and no resident may deal separately", is cell C written into law. Both are institutions. Both are things the Coasean agenda describes as friction. That is the second claim: **the institutions are what choose the cell, and without them cheap commitment chooses D.**

## 5. What "as budgets rise" means, cell by cell

Now add the thing the essay was supposed to be about. A real agent does not know every number exactly. It estimates the ones it needs: how big the pie is, what the other side will settle for, whether the other side has really tied its hands. Give each agent a budget $c$, counted in operations, and let its estimate of any number it needs have an error that shrinks like $\sigma/\sqrt{c}$, which is what estimating by sampling does. (This is the only place "compute" enters, and its unit is operations.) The agent then plays its cell's strategy using its estimates. As $c$ grows the errors vanish and play converges to the exact outcome of the cell. A twelve-year-old's version: when two children first play a board game they make mistakes, and the game sometimes ends nicely by accident; when they are both experts, the game ends exactly the way the rules make it end. If the rules are mean, getting better at the game makes it meaner.

Run that through the four cells.

- **A.** Errors on both sides roughly cancel. The split stays near three and three. More compute changes little.
- **B.** The factory needs to know each resident's harm to make its exact offer. With a limited budget it does not know it exactly, so to avoid a refusal it offers a little more than its estimate, a safety margin proportional to its error. As its budget grows, the margin shrinks and the residents' share goes from a little above zero to zero. **More compute for the factory moves $S$ toward 0.** This is the essay's own "from a price toward a quote", now with a direction and a rate: the margin is about $\sigma/\sqrt{c_f}$ per resident.
- **C.** The mirror image. The residents need to know the factory's profit to set their price at exactly $20$; with error they ask a little less to be safe; as their budget grows the share goes to one. **More compute for the residents moves $S$ toward 1.**
- **D.** With limited budgets, a side may misjudge whether the other has really committed, and back down, and then there is a deal after all. As budgets grow, both sides see the other's commitment exactly, nobody backs down, and the standoff becomes certain. **More compute makes the impasse more reliable.**

So the sign of "more compute" on the residents' share and on efficiency is not fixed. It is the sign the cell gives it, and cheap compute does not choose the cell. That is the formal content of "ubiquitous cheap bargaining agents, as their budget for computation increases, do not necessarily lead to equitable outcomes": in cell B more compute drives the residents' share to zero, in cell D it drives the pie out of existence, and the agenda's own program, cheap commitment for everyone and no rule assigning it, puts us in D, while the agenda's standard-form offers put us in B.

## 6. The one place the ratio of compute matters: the race at $k=1$

Change the rule to $k=1$, the factory needs one signature, and $\pi=10$, so the clean river is the right outcome. Now the residents' commitment, the pact "none of us signs unless all three agree", has to be in place *before* the factory signs one of them, because once one has signed the other two are harmed and unpaid. If the speed at which the factory finds and signs a resident, and the speed at which the three residents assemble their pact, are each proportional to that side's compute, call them $\lambda_f$ and $\lambda_N$, the chance the pact wins is $\lambda_N/(\lambda_f+\lambda_N)$. Halve the price of compute for everyone and both speeds double and the chance is unchanged. This is the only place in the model where the ratio of the two sides' compute decides anything, it is a race to commit first, and it lives in the one cell where the essay already showed no stable division exists. It is also the only cell in which a resident can end worse off than under no deal, which is the essay's yardstick: the two who did not sign.

## 7. What this says about Krier, in his own terms

His digital union of residents' agents is cell C, and it works exactly if the pact among the residents is enforced against side deals, which is a rule, not an agent. His developer who offers every homeowner a price is cell B, and the better the developer's agent knows each homeowner's floor, the less it pays. His option fee and his reimbursing veto are liability rules, cell B written into law with the payment fixed by a formula rather than by the factory's estimate, which is why they work and why they are regulation. His bargaining club, in which agents negotiate freely and all can commit, is cell D, and the better the agents, the more reliably it fails to close. The long tail of his small examples, the thermostat and the parking, is cell A with a custom already pinning the split, where none of this bites. The essay's disagreement with him is therefore not about whether agents cut costs. It is that in the large cases his program is sold on, what the agents cut costs *of* is commitment, and cheap commitment for everyone is a standoff.

## 8. What would make this wrong

- If agents in practice do not commit, because they are built to be agreeable, then the world stays in cell A and the claim about D is idle. The current evidence, that agents take the first acceptable offer and settle on conventions, points this way for small stakes. The claim is about large stakes and better agents, and it is a bet.
- If the cost of a standoff is large enough that one side always backs down in D, then D collapses into B or C according to who backs down, and the question becomes who has the larger revocation cost, which returns to institutions.
- If at $k=1$ the residents' pact assembles far faster than the factory's single offer, which is Krier's "flash coalition in a nanosecond", the race in section 6 goes to the residents whatever the ratio of compute, and the one-shot empty core stops mattering.

## 9. The symbols, collected

- $\pi$: the factory's profit from polluting. $h_i$: resident $i$'s harm. $h=(2,3,9)$; the pie at $\pi=20$ is $\pi-\sum h_i=6$.
- $k$: the number of consents the factory needs; $k=3$ in sections 3 to 5, $k=1$ in section 6.
- $d_f$, $d_N$: the positions, the number of slices each side insists on. Compatible iff $d_f+d_N\le 6$.
- $r_f$, $r_N$: revocation costs, the money a side loses by backing down from its position; the unit of commitment.
- $S$: the residents' share of the pie, between $0$ and $1$.
- $c$: an agent's budget in operations; its estimation error is $\sigma/\sqrt{c}$; "as budgets rise" means $c\to\infty$ and play converges to the cell's exact outcome.
- $\lambda_f$, $\lambda_N$: the speeds of signing one resident and of assembling the pact at $k=1$; the pact wins with probability $\lambda_N/(\lambda_f+\lambda_N)$.
