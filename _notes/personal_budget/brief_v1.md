# Brief: "personal budget" equilibria in Krier's Coasean world

This is the complete technical content for an article. Everything here has been derived and checked numerically (`_tmp/coase_budget/sim.py`; closed forms agree with direct numerical Nash computation to 1e-12). Do not change a formula or a number without saying so. You may reorder, cut and reword freely.

## 0. What the article is

A serious academic article responding to Seb Krier, ["Coasean Bargaining at Scale"](https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale) (Cosmos Institute, September 2025). Question: if every principal (household, firm, state) is represented by a perfectly loyal AI agent, has a bargaining budget that rises with its wealth, and faces selfish counterparties who spend up to their own limits, what equilibrium does each principal end up in, and is that world a good one? The commissioning author suspects it is not, and wants the suspicion *tested*, not confirmed. The honest answer from the models is conditional: there is a regime where Krier is right, and the article must say so plainly.

## 1. Krier's essay: the claims we engage

Paraphrase Krier; quote only short phrases (under 15 words) where the exact wording matters, and few of them.

- Thesis: transaction costs (finding the affected parties, negotiating, enforcing) are why societies fall back on blunt regulation. Personal AI agents cut those costs enough that Coase-style private bargaining over externalities becomes feasible at scale: "hyper-granular contracting". Examples: a delivery truck pays a clean-air fee to a street with an asthmatic child; a developer must find the price at which every homeowner agrees; taxis pay a cut-through fee.
- On cost: he concedes costs shift to compute but says a $10,000 legal bill may become "pennies", and offers the analogy that a billionaire's phone is no better than ours.
- On inequality: a short-run concern, handled by publicly funded baseline agents "similar to public defenders", agent vouchers, or a universal basic compute allocation; he says this is cheap and that the cost tends to zero as agents commoditise.
- On the default allocation of rights: a constitutional choice; start from existing jurisprudence; agents make the baseline "explicit, contestable, and cheap to renegotiate". He notes a poor farmer may sell pollution rights cheaply because he needs cash.
- On stability: constant renegotiation of property rights would destroy investment incentives, but he expects agents to settle on stable arrangements because "constant renegotiation is expensive even for AGI". (Note the tension: the stabiliser he relies on is the cost he says will vanish.)
- On holdouts and many-party bargains: a voluntary "bargaining club" in which each homeowner privately enters a minimum price, the software makes one take-it-or-leave-it offer, and payout is at a common clearing price; he says honesty is then the best strategy. Also Harberger-style fees on people who name absurd prices, and "flash coalitions": 10,000 residents forming a "digital union" instantly against a polluter.
- On the state: it stops being a planner and becomes a "framework guarantor": property rights, contract enforcement, courts, criminal law, bans on catastrophic risks. Three nested layers of agent loyalty: law, provider, user.
- What he does not discuss: bargaining between agents with unequal compute as a contest; the cost of *defending* an existing entitlement; what happens to total negotiation spending when its unit price falls.

## 2. The constitution we fix (Krier's own, made explicit)

- K1 Entitlements. Every entitlement has an owner, as inherited from existing law.
- K2 Voluntary exchange. No entitlement changes hands unless its owner's agent agrees.
- K3 Enforcement. The state enforces contracts and adjudicates disputes. Fraud and violence are excluded.
- K4 Loyal agents. Each agent maximises its own principal's payoff and nothing else. (The commissioning assumption: perfectly aligned agents.)
- K5 Coalitions are legal and cost nothing to form.
- K6 A compute voucher $\underline{B}$ per person may be paid by the state (Krier's public-defender proposal).

Three things the constitution does not settle, which turn out to decide everything:

1. **Decisiveness** $r$: how strongly out-computing the other side moves the split.
2. **How secure entitlements are**: what fraction $\kappa$ of an entitlement's value an ambiguity in its definition leaves open to challenge, and the fee $f$ it costs to bring a challenge.
3. **Liquidity**: whether a principal can pay for compute out of winnings it has not yet collected.

## 3. Notation (keep these symbols and names; one name per concept)

| Symbol | Name | Meaning |
|---|---|---|
| $i, j$ | principals | households, firms, states; each has one loyal agent |
| matter | | one bargain between two principals |
| $V_{ij}$ | stake | dollars of surplus (or of contested entitlement) at issue in the matter between $i$ and $j$ |
| $S_i = \sum_j V_{ij}$ | total stakes | everything $i$ has at issue in a period |
| $m_i$ | number of matters | |
| $p$ | price of compute | dollars per unit |
| $x_{ij}$ | spend | dollars of compute $i$ puts into its matter with $j$ |
| $B_i$ | budget | dollars $i$ can spend on bargaining compute in a period; rises with wealth |
| $r$ | decisiveness | exponent in the contest rule; $0<r\le 1$ in our general results |
| $\sigma_{ij}$ | share | fraction of $V_{ij}$ that $i$ gets |
| $s_i\in(0,1]$ | strength | defined in R2; 1 means the budget does not bind |
| dissipation | | what both sides together spend on compute to divide a stake |
| $c_0$ | showing-up cost | compute needed merely to take part in a matter (parse it, model the counterparty) |
| $\kappa$ | contestable fraction | share of an entitlement's value that a challenge can put at issue |
| $\theta\ge 1$ | defender advantage | how much more a defender's dollar counts than a challenger's |
| $f$ | challenge fee | cost of bringing a challenge, whatever its source: court fee, delay, human attention |
| $V^\ast(B)$ | safe stake | largest contestable stake nobody finds it profitable to challenge |
| $\underline{B}$ | voucher | state-paid floor on budgets |
| $N$ | | number of similar matters a repeat player handles |

## 4. Where compute enters a bargain

Two different uses, which respond oppositely to cheap compute.

- **Showing up** ($c_0$ per matter): finding the counterparty, parsing the matter, stating terms. This is a fixed technological requirement measured in compute units, so its dollar cost $c_0$ falls in proportion to $p$. This is the cost Krier is talking about, and he is right about it.
- **Claiming**: once a surplus exists, how it is split. We model this as a contest. $i$'s share of stake $V$ against $j$ is
$$\sigma_{ij} = \frac{x_{ij}^r}{x_{ij}^r + x_{ji}^r}.$$
This is the Tullock contest success function. Three reasons to adopt it as the reduced form:
  1. A search microfoundation that fits how agents actually work. Suppose each unit of compute buys one independent draw of a candidate argument, contract clause or counter-proposal from a common distribution, and the side holding the single best draw prevails. Then the probability that $i$ holds the best draw is exactly $x_i/(x_i+x_j)$, whatever the distribution. That is $r=1$. (This is best-of-$N$ sampling. Cite the equivalence result per the literature list.)
  2. It is the unique form satisfying a short list of axioms including scale invariance: only the ratio of efforts matters.
  3. It is the standard model of litigation spending.
- What $r$ means: $r\to 0$ is a world where extra compute does not move the split (a solved bargaining problem, or a protocol that ignores cleverness). $r=1$ is the search benchmark. $r>1$ would be increasing returns (a model twice as large draws from a better distribution).
- $r$ is measurable: the slope of $\log(\sigma/(1-\sigma))$ on $\log(x_i/x_j)$ in agent-versus-agent negotiation experiments. Nobody has reported it. Existing evidence shows only that it is positive (see literature, Project Deal).
- The alternative we must state fairly: **saturation**. If every bargaining problem had a finite depth $\bar q$ of compute beyond which more thinking adds nothing, then for cheap enough compute both sides saturate, split evenly, and spend $2p\bar q\to 0$. Then Krier is simply right. Reasons to doubt saturation: the complexity of a contract is chosen by the parties. A contract with $K$ interacting clauses has $K(K-1)/2 = O(K^2)$ pairwise interactions to check, and one conditioned on $S$ binary contingencies has $2^S$ states; the stronger side can add clauses until the weaker side cannot verify them. The literature on deliberate price complexity (Carlin; Gabaix and Laibson) shows this survives competition. So as $p$ falls, complexity rises to absorb it. But this is an argument, not a theorem, and the article should flag saturation as the assumption that would rescue Krier.

## 5. Results

### R1. Cheap compute does not make claiming cheap (one matter, no budget limits)

Each side maximises $V\sigma_{ij} - x_{ij}$. Symmetric equilibrium: each spends $x^\ast = rV/4$ dollars, i.e. buys $q^\ast = rV/(4p)$ units of compute. Dissipation is $rV/2$ dollars, whatever $p$ is. Halve the price of compute and both sides buy twice as much. The cost of negotiating is set by the stake and by $r$, not by the price of compute.

So in the claiming dimension the "transaction cost" of a matter is $rV/2$: proportional to what is at issue. A $10,000 legal fight over a $40,000 stake stays a $10,000 fight ($r=0.5$) when compute becomes cheap; it just contains more computation. The phone analogy fails because a phone is used against nobody; bargaining compute is used against someone who also has it.

Caveat on range: for $0<r\le1$ each side's payoff is concave in its own spend and the equilibrium is in pure strategies. For $r>2$ equilibrium is in mixed strategies and the whole stake is dissipated (Baye, Kovenock and de Vries).

Historical echo: Wallis and North measured the share of US national income spent on transacting (lawyers, finance, trade, clerical work) rising over a century in which the cost of each transaction fell.

### R2. Many matters, one budget: every principal gets one number, its strength

Principal $i$ chooses spends $x_{ij}\ge 0$ on all its matters to maximise $\sum_j (V_{ij}\sigma_{ij} - x_{ij})$ subject to $\sum_j x_{ij}\le B_i$.

Let $\lambda_i\ge 1$ be the value to $i$ of one more dollar of bargaining spend, holding everyone else's spending fixed ($\lambda_i=1$ when the budget is slack, because then the marginal dollar is worth exactly a dollar). Define **strength** $s_i = 1/\lambda_i\in(0,1]$. First-order conditions for both sides of a matter give $x_{ji}/x_{ij}=\lambda_i/\lambda_j$, hence, for $0<r\le1$:

$$\sigma_{ij} = \frac{s_i^r}{s_i^r+s_j^r},\qquad x_{ij} = r\,V_{ij}\,\sigma_{ij}\,\sigma_{ji}\,s_i .$$

$s_i=1$ if $r\sum_j V_{ij}\sigma_{ij}\sigma_{ji}\le B_i$; otherwise $s_i<1$ solves $\sum_j x_{ij}=B_i$. The whole economy's equilibrium is the vector $(s_1,\dots,s_n)$ solving these $n$ equations. For $r=1$ with budgets that must be spent this is Lemma 1 of Díaz-García, Bullo and Marden (2024); see the literature list. We verified numerically on random networks with mixed constrained and unconstrained principals, for $r\in\{0.25,0.5,1\}$, that no principal can gain by deviating (largest relative gain found: $2\times10^{-12}$). We do not claim a uniqueness theorem; the iteration converged to the same point from every start we tried.

Reading: the outcome of every bargain is settled by the two parties' strengths alone, in the same form as a chess rating or a Bradley–Terry paired-comparison model. Strength is not wealth; it is how *unconstrained* you are: budget relative to everything you have at issue.

Special case that carries most of the article: a constrained principal whose counterparties are all unconstrained ($s_j=1$), with $r=1$. If $B_i<S_i/4$:

- share in every matter: $\sigma_i=\sqrt{B_i/S_i}$
- total taken: $\sqrt{B_iS_i}$
- counterparties' total spend against $i$: $\sqrt{B_iS_i}-B_i$; their total net gain: $(\sqrt{S_i}-\sqrt{B_i})^2$
- $i$ splits its budget across matters in proportion to stakes.

If $B_i\ge S_i/4$ the budget does not bind and $i$ gets half of everything, spending $S_i/4$. For general $r$ the threshold is $rS_i/4$ and the share solves $r S_i s^{1+r}/(1+s^r)^2=B_i$, $\sigma=s^r/(1+s^r)$.

Among unequal constrained principals, $i$ spends most where stakes are large *and* the opponent is close to its own strength ($\sigma_{ij}\sigma_{ji}$ peaks at an even match), and rationally concedes most of the surplus to much stronger counterparties.

**Worked case (Asha).** Asha is a nurse who rents. Per year she has $S=\$25{,}000$ at issue: about $12,000 of surplus in her employment contract, $6,000 in her lease, $2,000 with her insurer, $1,000 with platforms, and $4,000 spread over a couple of hundred small matters with neighbours. Her budget for agent compute is $B=\$400$ a year. Her counterparties in the big matters are firms whose budgets do not bind; call the composite **Meridian**.

| | $r=1$ | $r=0.5$ | $r=0.25$ |
|---|---|---|---|
| budget needed for an even split, $rS/4$ | $6,250 | $3,125 | $1,562 |
| Asha's share | 12.6% | 28.4% | 41.7% |
| Asha takes | $3,162 | $7,101 | $10,433 |
| Meridian spends against her | $2,762 | $2,542 | $1,520 |
| Meridian nets | $19,075 | $15,358 | $13,047 |
| dissipated fraction of $S$ | 12.6% | 11.8% | 7.7% |

Asha is better off than with no bargaining (she nets $2,762 at $r=1$), which is Krier's point, and gets about an eighth of the surplus, which is ours.

### R3. More matters stretch the budget thinner

Krier's world multiplies the matters each principal is party to: with $n$ principals there are up to $n-1$ bilateral matters per principal and $n(n-1)/2=O(n^2)$ overall, before counting multi-party ones. Everything with a stake above the showing-up cost becomes live.

- With $B_i$ fixed and $r=1$, share falls as $S_i^{-1/2}$. Twice the stakes at issue ($S=\$50{,}000$): Asha's share falls from 12.6% to 8.9% while her take rises from $3,162 to $4,472. With stakes of $250 per matter and $B=\$400$: 10 matters, share 40%; 100, 12.6%; 1,000, 4%; 10,000, 1.3%.
- New matters crowd out old ones. In the population experiment below, multiplying peer-to-peer matters tenfold cuts the median household's share against firms from 11.5% to 4.0%, so its take on the *unchanged* $20,000 of firm matters falls from about $2,300 to about $800, because the budget moved to the new matters. (It gains more than that on the new matters, as long as those are new surplus. See R7 for when they are not.)
- Showing-up cost and span. If each matter costs $c_0$ to attend and has stake $V$, a constrained principal facing unconstrained counterparties attends $k^\ast=\min(m, B/(2c_0))$ matters: it spends half its budget turning up and half contesting, and takes $(B/2)\sqrt{V/c_0}$ in total. The number of bargains a principal can attend is proportional to its budget. On the rest it takes whatever the default is.
- If stakes are heavy-tailed, with $M(v/v_0)^{-\alpha}$ matters of stake above $v$ and $\alpha>1$ (many small matters), the optimal fraction of budget spent on showing up is $(\alpha-1)/(2\alpha-1)$, and the stakes in play grow without bound as $c_0\to0$. Example with $\alpha=1.5$, $B=\$400$: as $c_0$ falls from $20 to $0.02, matters attended rise from 5 to 5,000, stakes in play from $17,000 to $174,000, share falls from 13% to 4%, take rises from $2,300 to $7,200.

So cheap compute does what Krier says to $c_0$, and the consequence is a larger $S_i$ against the same $B_i$.

### R4. The weaker side's share equals the fraction burned

Dissipation in a matter is $x_{ij}+x_{ji} = rV\sigma_{ij}\sigma_{ji}(s_i+s_j)$. For $r=1$ this is $V s_is_j/(s_i+s_j)$, and against an unconstrained counterparty ($s_j=1$) it equals $V\sigma_{ij}$ exactly: **the fraction of the stake that is dissipated equals the weaker side's share.** What is left after compute is $V(1-\sigma_{\text{weak}})$.

Consequences.

- Dissipation is greatest between equals (half the stake at $r=1$) and vanishes as one side becomes too poor to contest. Asha versus Meridian: 12.6% dissipated, total net surplus $21,837 of $25,000. Asha funded to parity: each side nets $6,250, total $12,500, half the stake gone.
- A planner who maximises total surplus net of costs, which is the criterion Coasean reasoning uses, prefers Asha weak. In this model wealth-maximisation and an even split pull in opposite directions, point for point.
- This prices Krier's voucher. To give a household an even split the voucher must top its budget up to $rS_i/4$: a quarter of its stakes at $r=1$. That is a fraction of stakes, fixed in dollars, and does not fall when compute gets cheaper. And firms answer the voucher by spending more ($x_{ji}$ rises as $s_i$ rises towards 1).

**Population experiment.** 3,000 households; budgets log-normal with median $400 (10th percentile $58, 90th $2,675, 99th $12,906); each has $20,000 a year at issue with unconstrained firms and about 20 matters of $250 with random other households.

| scenario | households constrained | bottom-decile share vs firms | median share vs firms | top-decile share vs firms | dissipated | households keep | firms keep |
|---|---|---|---|---|---|---|---|
| baseline, $r=1$ | 96% | 2.6% | 11.5% | 44% | 14.5% | 20.5% | 65.0% |
| voucher floor $2,000 | 97% | 27.7% | 27.7% | 43% | 28.3% | 27.0% | 44.7% |
| voucher floor $6,250 | 41% | 49.7% | 49.7% | 50% | 49.7% | 27.8% | 22.5% |
| $r=0.25$, no voucher | 82% | 28.1% | 41.7% | 50% | 8.0% | 45.0% | 47.0% |

("keep" = fraction of all surplus retained net of spending.) The $2,000 voucher costs the state 5.8% of total surplus and raises dissipation by 13.8 points; households' net take rises 6.5 points, firms' falls 20 points. The parity voucher costs 23.5% of total surplus; households end up keeping 27.8% and firms 22.5%, with half of everything dissipated. The voucher mostly destroys the firms' surplus; it does not transfer it. Compare the last row: lowering $r$ from 1 to 0.25 with no voucher at all gives households 45% and dissipates 8%.

### R5. A binding budget puts everything else the principal owns on sale

In equilibrium (counterparties anticipating the budget), a constrained principal's take is $\sqrt{B_iS_i}$, so one more dollar of budget is worth $\tfrac12\sqrt{S_i/B_i}$ dollars of surplus. For Asha that is about $3.95. She should therefore sell anything she owns for cash at any price above roughly a quarter of what it is worth to her, and put the cash into her agent. This is Krier's poor farmer, derived: he sells his pollution right cheaply because a dollar of liquidity is worth several dollars in his other bargains. And the more matters the Coasean world opens ($S_i$ up), the higher that premium, and the cheaper constrained principals sell.

(Technical note for the appendix: holding opponents' spending fixed, the marginal dollar is worth $\lambda_i=\sqrt{S_i/B_i}-1 = 6.9$ for Asha; the smaller figure $\tfrac12\sqrt{S_i/B_i}$ lets opponents respond.)

Credit. If principals could borrow freely against expected winnings, nobody would be constrained: every share is one half and dissipation is $rV/2$ on every matter. Third-party funders already do this for lawsuits, taking a share of proceeds. So finance moves the economy from the unequal, low-dissipation corner to the equal, maximum-dissipation corner. Neither corner is the frictionless Coasean outcome.

### R6. Repeat players, and what a coalition actually buys

A firm that has the same matter with $N$ households (one lease form, one employment contract) can reuse an argument across all of them: compute spent once counts in every matter. If each household spends $b$ and the stake per household is $V$, the firm spends $X=\sqrt{NVb}-b$ once, and an isolated household's share is

$$\sigma=\sqrt{\frac{b}{NV}},$$

falling as $N^{-1/2}$. With $b=\$100$, $V=\$6{,}000$: share 12.9% at $N=1$, 1.3% at $N=100$, 0.13% at $N=10{,}000$. If all $N$ households pool their budgets into one shared argument the share returns to $\sqrt{b/V}=12.9\%$.

So Krier's "digital union" is real and matters, and what it does is cancel the repeat player's scale economy. It restores the household to the position in R2; it does not get it past $\sqrt{b/V}$. It works only for stakes that are common across members (the same lease), not for the bespoke matters that hyper-granular contracting is meant to create. (Galanter's "haves" result is the classical statement.)

### R7. Entitlements are only as secure as the friction protecting them

So far every stake was new surplus, and under K2 nobody can end up below where they started. Now drop the assumption that entitlements are perfectly specified. Every legal entitlement is a finite text about an open-ended world (the incomplete-contracts literature); some fraction $\kappa$ of its value is open to a good-faith challenge: a boundary, an ambiguous lease term, a claim the insurer disputes, a reclassified job duty. Finding such ambiguities is a search problem that cheap compute makes cheap.

A challenger pays a fee $f$ and then the two sides contest the stake $V=\kappa E$ with defender advantage $\theta\ge1$ ($r=1$):
$$\sigma_D=\frac{\theta x_D}{\theta x_D+x_A}.$$

- Both unconstrained: each spends $\theta V/(1+\theta)^2$; the defender keeps $\theta/(1+\theta)$; the challenger nets $V/(1+\theta)^2-f$. Before the fee this is positive for every $\theta$: a defender advantage shrinks the prize but never makes challenging unprofitable. Only $f$ does.
- Defender able to spend only $b$: the challenger nets $(\sqrt V-\sqrt{\theta b})^2-f$ and the defender keeps $\sqrt{\theta bV}$.
- **Safe stake.** Nobody challenges a contestable stake of at most
$$V^\ast(B)=\Bigl(\sqrt{\theta\min(B,\theta f)}+\sqrt f\Bigr)^2,$$
which runs from $f$ for a defender with no budget to $(1+\theta)^2f$ for an unconstrained one. Everything above $V^\ast(B)$ is attacked. Security of tenure is measured in units of $f$. With $\theta=3$: at $f=\$1{,}000$, $V^\ast$ is $1,000 with no budget, $4,391 with $B=\$400$, $16,000 unconstrained; at $f=\$100$ it is $100, $1,600, $1,600; at $f=\$1$ it is $1, $16, $16.
- Krier's programme is to drive transaction costs towards zero, and a challenge is a transaction. As $f\to0$, $V^\ast\to0$ for everyone.
- **Selective predation.** At a given fee, the same contestable stake is safe in well-funded hands and prey in poorly funded ones. Challengers go where $\theta B_i$ is small relative to $\kappa E_i$: the asset-rich and cash-poor.
- **Runs.** Challenges against a constrained defender are complements: each additional challenge splits her budget and makes every other challenge more profitable. With stake $10,000 per challenge, defender budget $400, $\theta=3$: one challenger nets $4,272, two net $5,701 each, four $6,836, eight $7,701. At a fee of $5,500 a lone challenge loses money and a joint one pays. There are two equilibria, as with a bank run.
- **Even among equals it is a loss.** Take a pair of unconstrained principals with one matter of new surplus $V^+$ between them, each also able to challenge $V^-$ of the other's entitlements, $f=0$. Each challenge is individually profitable, so both happen. Net gain to the pair: $V^+/2-4\theta V^-/(1+\theta)^2$. The pair is worse off than with no bargaining at all when $V^-/V^+>(1+\theta)^2/(8\theta)$: one half at $\theta=1$, two thirds at $\theta=3$, 1.4 at $\theta=9$. The stock of existing entitlements is many times the annual flow of new Coasean surplus, so a small $\kappa$ is enough. (Illustrative arithmetic, flag as such: if existing entitlements are worth about six years of output and new surplus from Coasean bargaining were a generous 10% of output a year, the break-even at $\theta=3$ is about 1% of entitlement value contestable per year.)

**Worked case (Odile).** Odile is a retired homeowner: a house worth $500,000, a pension, and $400 a year for agent compute. A neighbour's developer finds a defect in a 1970s easement that puts $10,000 of her property's value at issue ($\kappa=2\%$). With $\theta=3$: funded like Meridian she would spend $1,875, keep 75%, and the challenger would net $625 before the fee, so a $1,000 fee deters it. With $400 she keeps 35% ($3,464) and the challenger nets $4,272: the same $1,000 fee does not deter it. Before agents, the fee was a lawyer's retainer and months of delay, far more than $1,000, and nobody looked for the defect.

Real-world anchor: ProPublica reported in 2023 that a US health insurer's review system let its doctors reject over 300,000 claims in two months, at an average of 1.2 seconds each ([ProPublica](https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims)). One side's cost of contesting had fallen to nearly zero; the other side's cost of an appeal had not.

The general lesson: frictions are not only obstacles to good bargains. They are also what protects holders who cannot afford to defend. Lowering them is not neutral between the two.

A conjecture, to be marked as one: among principals who interact repeatedly and can retaliate, mutual restraint is sustainable (the standard repeated-game argument). Retaliation needs budget. So the plausible long-run pattern is peace among the unconstrained and challenges directed at the constrained.

### R8. Dynamics: when the constraint cures itself and when it does not

Winnings can be spent on next period's compute.

- **Self-curing case.** If stakes are new surplus, paid in cash, and nothing drains the budget, a constrained principal's budget follows $B_{t+1}=\sqrt{B_tS}$: Asha goes $400 → $3,162 → $8,891 and is unconstrained within two periods. In general $B_t=S^{1-2^{-t}}B_0^{2^{-t}}$: the gap closes doubly exponentially. The constrained earn the highest return on compute, so they catch up (this is Hirshleifer's "paradox of power"). This is the best case for Krier, and in it inequality of strength is a short-run problem, as he says. The society it converges to has everybody unconstrained and $r/2$ of every stake dissipated.
- **Trap.** If living costs drain $d$ per period from the budget, $B_{t+1}=\sqrt{B_tS}-d$ has an unstable threshold $B_-=\bigl((\sqrt S-\sqrt{S-4d})/2\bigr)^2\approx d^2/S$. Below it the budget goes to zero and stays there. With $S=\$25{,}000$: $d=\$1{,}000$ gives a threshold of $44; $d=\$3{,}000$ gives $486, and Asha at $400 falls to zero.
- **In-kind gains do not cure.** Much Coasean surplus is not cash: quiet, clean air, a car-free street. It cannot be spent on compute. Then $B$ stays put and shares stay at $\sqrt{B/S}$. The only way to turn it into budget is to sell the entitlement, at the discount in R5.
- **Contested entitlements run the other way.** Under R7 a constrained holder loses the part of her contestable holdings above $V^\ast(B)$ each round, and the process stops only when what she holds is what she can defend.

## 6. Limits that no amount of compute removes (short section; cite, do not re-derive)

These are about private information and voluntary participation, not about cost.

- Two parties, private valuations: no mechanism is at once incentive-compatible, individually rational, budget-balanced and efficient (Myerson and Satterthwaite).
- Many parties, unanimity (Krier's developer needing every homeowner): the probability of reaching an efficient yes goes to zero as the number of parties $n$ grows (Mailath and Postlewaite).
- Voluntary participation with more than two players: free-riding by staying out of the contract survives even costless contracting (Dixit and Olson; Ellingsen and Paltseva). Costless binding side-payments do not guarantee efficiency even with complete information (Jackson and Wilkie).
- Krier's bargaining club. If no member surrenders the veto, the common price must be at least the largest reported minimum, so the member with the largest report sets everyone's price and gains by overstating; honesty is not the best strategy, and the incentive is the familiar trade-off between a better price and a higher risk of killing the deal. If instead the club clears below the largest report, some members are overridden and the scheme is no longer voluntary. That is the content of the Mailath–Postlewaite result, not a design detail.
- Computation. Finding the best partition of $n$ principals into coalitions is NP-complete in $n$ (Sandholm et al.); choosing winning bids in a combinatorial auction is NP-complete in the number of bids and hard to approximate; and replacing the exact optimum with a feasible approximation generally destroys the truth-telling property of the standard mechanism (Nisan and Ronen). So at scale the mechanism is approximate, and where it is approximate the side that can compute more can steer it (Conitzer and Sandholm).

## 7. Remedies, evaluated inside the model

| Remedy | Effect in the model | Cost |
|---|---|---|
| Compute voucher $\underline B$ (Krier) | raises the floor on shares to about $\sqrt{\underline B/S_i}$ | priced in stakes ($rS_i/4$ for parity), not in compute; raises dissipation point for point (R4) |
| Credit / third-party funding | removes the constraint | maximum dissipation $r/2$ everywhere; funders take a cut |
| Lower $r$: fixed protocols, standard forms, arbitration rules that do not reward cleverness | flattens shares and cuts dissipation together (last row of the population table) | gives up bespoke terms, which is the point of hyper-granular contracting; and strategy-proof, efficient, budget-balanced protocols do not exist (section 6) |
| Coalitions | cancel the repeat player's $N^{-1/2}$ advantage (R6) | only for common stakes; each coalition's internal split is another matter |
| Caps on bargaining compute | would cut dissipation with even shares | compute spent in private is unobservable; enforcing a cap means inspecting every agent. In a different contest form (all-pay auction) a rigid cap can even raise total spending (Che and Gale 1998). |
| Take matters off the table (inalienable rights, bright-line rules) | lowers $S_i$ and $\kappa$; for a constrained principal a smaller $S_i$ raises its share on what remains | forgoes surplus on the excluded matters. This is the Calabresi–Melamed inalienability rule, justified here from inside a bargaining model |
| Keep a challenge fee $f$; loser pays | raises $V^\ast$ for everyone | it is a transaction cost, kept on purpose |

Observation: the remedies that work are the institutions Krier's essay hopes to slim down: standard forms, unions, bright-line regulation, costly courts.

Also: why do the parties not simply agree to stop out-computing each other? Because the agreement would have to be verified (private compute is not observable) and because negotiating it is itself a matter with a stake.

## 8. Verdict: a regime map

| | entitlements secure ($\kappa E\le V^\ast$) | entitlements contestable, fee low |
|---|---|---|
| **low decisiveness** ($r\lesssim 0.25$) | Krier's world, roughly. Near-even shares, dissipation at most $r/2$. | Small losses; challenges are barely worth bringing. |
| **high decisiveness, cash gains, no drain** | Unequal at first, self-curing within a few periods; converges to equal shares with up to half of every stake dissipated. | Peace among the strong (conjectured), transfers from the constrained. |
| **high decisiveness, in-kind gains or a drain** | Persistent hierarchy of strength. Everyone gains something; the constrained get $\sqrt{B/S}$ of each surplus, falling as matters multiply. | Holdings shrink towards what each holder can defend. Constrained principals are worse off than with no bargaining. |

What the test found, stated plainly:

1. Under Krier's own constitution with perfectly secure entitlements, nobody is made worse off in absolute terms by bargaining over new surplus. The suspicion that the world is simply bad is not supported in that cell.
2. But the essay's cost claim is wrong in the dimension that matters for distribution: negotiation spending is set by stakes and decisiveness, not by the price of compute (R1), so neither transaction costs nor the cost of the voucher tends to zero.
3. Shares are set by budget relative to stakes, and the Coasean programme raises stakes at issue faster than budgets (R2, R3).
4. Even shares and low waste trade off one for one (R4).
5. The sign of the whole exercise for constrained principals depends on whether entitlements stay secure when challenging them becomes cheap (R7), which is a matter the essay treats as settled background.

What would change our mind: evidence that $r$ falls towards zero as agents get more capable (saturation); evidence that entitlement definitions can be made complete enough that $\kappa\approx0$; a compute-verification technology that makes caps enforceable.

Three measurements worth making: $r$ from agent-versus-agent experiments with controlled compute ratios; the fraction of realised surplus spent on agent compute as agent prices fall; the rate of challenges to existing entitlements by counterparty wealth.

## 9. Literature (verified; use these links as hyperlinks on author–year text, no citation keys)

A second list, "Contest literature (verified)", follows at the end. Do not cite anything that is not on one of the two lists.

Bargaining and its limits:
- [Coase (1960)](https://doi.org/10.1086/466560), "The Problem of Social Cost". [Coase (1937)](https://doi.org/10.1111/j.1468-0335.1937.tb00002.x), "The Nature of the Firm".
- Calabresi and Melamed (1972) [no link], "Property Rules, Liability Rules, and Inalienability", Harvard Law Review 85(6): 1089–1128. Three ways to protect an entitlement: property rule (holder's consent needed), liability rule (may be taken on payment of a value set by the state), inalienability (may not be sold).
- [Myerson and Satterthwaite (1983)](https://doi.org/10.1016/0022-0531(83)90048-0), J. Economic Theory 29(2): 265–281.
- [Mailath and Postlewaite (1990)](https://ideas.repec.org/a/oup/restud/v57y1990i3p351-367..html), Review of Economic Studies 57(3): 351–367. With unanimity required and independent private values, probability of an efficient yes goes to zero as the number of agents grows; includes an example where it is common knowledge that yes is efficient. (No rate in $n$ verified: do not state one.)
- [Dixit and Olson (2000)](https://ideas.repec.org/a/eee/pubeco/v76y2000i3p309-335.html), J. Public Economics 76(3): 309–335. Efficient equilibrium not robust to even very small transaction costs once participation is voluntary.
- [Ellingsen and Paltseva (2016)](https://research.hhs.se/esploro/outputs/journalArticle/Confining-the-Coase-theorem-Contracting-ownership/991001480655806056), Review of Economic Studies 83(2): 547–586. Two players: efficient. More than two with voluntary participation: situations where all consistent equilibria are inefficient.
- [Jackson and Wilkie (2005)](https://doi.org/10.1111/j.1467-937X.2005.00342.x), Review of Economic Studies 72(2): 543–566. Binding side-payment offers do not always produce efficiency "despite complete information and costless contracting".
- [Medema (2020)](https://ideas.repec.org/a/aea/jeclit/v58y2020i4p1045-1128.html), "The Coase Theorem at Sixty", J. Economic Literature 58(4): 1045–1128. Survey; includes the extortion objection (a party threatens harm to be paid to stop; Wellisz 1964 quipped that this opens "magnificent business prospects") and the reply that it only matters if resources are spent seeking the rent. Our R7 is that case: resources are spent.
- [Cooter (1982)](https://doi.org/10.1086/467690), "The Cost of Coase", J. Legal Studies 11(1): 1–33. Lower communication costs can make agreement harder by easing strategic behaviour (as summarised in secondary sources; phrase cautiously).
- [Farrell (1987)](https://doi.org/10.1257/jep.1.2.113), "Information and the Coase Theorem", J. Economic Perspectives 1(2): 113–129.

Incomplete contracts and cognition:
- [Tirole (2009)](https://doi.org/10.1257/aer.99.1.265), "Cognition and Incomplete Contracts", AER 99(1): 265–294. Thinking before contracting is costly; it has both an efficiency role and a rent-seeking role, so contracts can be too complete or too incomplete. (State only this much.)
- [Bolton and Faure-Grimaud (2010)](https://ideas.repec.org/a/oup/restud/v77y2010i3p937-971.html), "Satisficing Contracts", REStud 77(3): 937–971. Deliberation takes time, so contracts are left incomplete and assign control instead.
- [Anderlini and Felli (1994)](https://ideas.repec.org/a/oup/qjecon/v109y1994i4p1085-1124..html), QJE 109(4): 1085–1124; [Al-Najjar, Anderlini and Felli (2006)](https://ideas.repec.org/a/oup/restud/v73y2006i4p849-868.html), "Undescribable Events", REStud 73(4): 849–868: events every finite description of which leaves exceptions.
- [Battigalli and Maggi (2002)](https://doi.org/10.1257/00028280260344470), AER 92(4): 798–817. Incompleteness from the cost of describing the environment.
- [Carlin (2009)](https://ideas.repec.org/a/eee/jfinec/v91y2009i3p278-287.html), "Strategic Price Complexity in Retail Financial Markets", JFE 91(3): 278–287. Firms add complexity to keep some consumers uninformed; prices may rise with entry.
- [Gabaix and Laibson (2006)](https://ideas.repec.org/a/oup/qjecon/v121y2006i2p505-540..html), QJE 121(2): 505–540. Shrouded add-on prices persist even in highly competitive markets.
- [Bakos, Marotta-Wurgler and Trossen (2014)](https://doi.org/10.1086/674424), J. Legal Studies 43(1): 1–35. One or two shoppers in a thousand open the licence agreement.

Courts, inequality, repeat players:
- [Galanter (1974)](https://www.cambridge.org/core/journals/law-and-society-review/article/8A16E3B6212A1A61E196841F092CF428), "Why the 'Haves' Come Out Ahead", Law & Society Review 9(1): 95–160. Repeat players versus one-shotters.
- [Glaeser and Shleifer (2003)](https://doi.org/10.1257/002205103765762725), "The Rise of the Regulatory State", J. Economic Literature 41(2): 401–425. Private litigation can be subverted by the strong, more so as enterprises grow; regulation as the response.
- [Glaeser, Scheinkman and Shleifer (2003)](https://ideas.repec.org/a/eee/moneco/v50y2003i1p199-222.html), "The Injustice of Inequality", J. Monetary Economics 50(1): 199–222.
- [Ellingsen and Miettinen (2008)](https://doi.org/10.1257/aer.98.4.1629), "Commitment and Conflict in Bilateral Bargaining", AER 98(4): 1629–1635. Cheap commitment produces either one-sided outcomes or a high probability of conflict. Relevant to Krier's "non-negotiable" coalition price: the polluter's agent can commit too.

Computation:
- [Sandholm, Larson, Andersson, Shehory and Tohmé (1999)](https://doi.org/10.1016/S0004-3702(99)00036-3), Artificial Intelligence 111: 209–238. Optimal coalition structure is NP-complete.
- [Sandholm (2002)](https://doi.org/10.1016/S0004-3702(01)00159-X), Artificial Intelligence 135: 1–54. Winner determination NP-complete; no polynomial algorithm guarantees within $n^{1-\epsilon}$ unless NP = ZPP. (Say "in the size of the auction"; do not specify what $n$ counts.)
- [Nisan and Ronen (2007)](https://arxiv.org/abs/1110.0025), JAIR 29: 19–47. Essentially all reasonable approximations of the optimal allocation make the VCG mechanism non-truthful.
- [Conitzer and Sandholm (2004)](https://dl.acm.org/doi/10.1145/988772.988824), "Computational Criticisms of the Revelation Principle". When the truthful mechanism is intractable, outcomes depend on who can do the hard computation.
- [Larson and Sandholm (2001)](https://www.sciencedirect.com/science/article/pii/S0004370201001321), "Bargaining with Limited Computation: Deliberation Equilibrium", Artificial Intelligence 132(2): 183–217. Computation as part of strategy; equilibria can be Pareto-inefficient.
- [Halpern and Pass (2015)](https://arxiv.org/abs/1412.2993), "Algorithmic Rationality: Game Theory with Costly Computation", JET 156: 246–268.

AI agents:
- [Tomašev et al. (2025)](https://arxiv.org/abs/2509.10147), "Virtual Agent Economies" (cited by Krier; itself flags systemic risk and inequality).
- [Shahidi, Rusak, Manning, Fradkin and Horton (2025)](https://www.nber.org/papers/w34468), "The Coasean Singularity?", NBER WP 34468.
- [Hadfield and Koh (2025)](https://arxiv.org/abs/2509.01063), "An Economy of AI Agents".
- [Anthropic (2026), "Project Deal"](https://www.anthropic.com/features/project-deal): 69 agents, 186 deals. Where the same item sold more than once, a seller represented by the stronger model got $2.68 more and a buyer represented by it paid $2.45 less (median price $12). Sales from a stronger-model seller to a weaker-model buyer averaged $24.18 against $18.63 between two stronger-model agents. People represented by the weaker model rated the fairness of their deals the same (4.06 versus 4.05 on a 7-point scale). Small sample; Anthropic's own caveat. Use: evidence that $r>0$ and that the losing side does not notice.
- [Zhu, Sun, Nian, South, Pentland and Pei (2025)](https://arxiv.org/abs/2506.00073), "The Automated but Risky Game": agent-to-agent deal-making is "an inherently imbalanced game".
- [Davidson et al. (2024)](https://arxiv.org/abs/2401.04536): even the strongest models sometimes lose to weaker ones. Use: $r$ is finite; outcomes are noisy.
- [Imas and Misra (2026), "Agentic Interactions"](https://www.chicagobooth.edu/research/center-for-applied-artificial-intelligence/research/our-faculty-research/2026/agentic-interactions): outcomes track the skill of the human who wrote the prompt, a new source of inequality.
- [Sharp et al. (2025), "Agentic Inequality"](https://arxiv.org/abs/2510.16853): unequal agent quality and quantity as a source of stratification.
- Existing critique of Krier to acknowledge: [Petel, "Price what you can, protect what you must"](https://mateopetel.substack.com/p/price-what-you-can-protect-what-you): pricing fails for dignity, privacy and system-wide harms; non-negotiables must be constitutionalised. Our R7 and the inalienability row of the remedies table reach a neighbouring conclusion by a different route (from inside the bargaining model). We found no published critique that models unequal compute as a contest.
- [ProPublica (2023)](https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims) on batch claim denials.

## 10. Cast (for humanising; keep it small and consistent)

- **Asha**: nurse, renter. Budget $400 a year, $25,000 at issue. The constrained principal.
- **Meridian**: a composite of the firms on the other side of her large matters (employer, landlord, insurer). Unconstrained; a repeat player.
- **Odile**: retired homeowner, asset-rich and cash-poor. The holder of a contestable entitlement.
- Optionally **Bram**, Asha's neighbour with a similar budget, for the even-match case (they split evenly and dissipate a lot relative to the stake).

Include a short table early on mapping each symbol to its story counterpart (Asha's $400 is $B$; her $25,000 is $S$; and so on).

## Contest literature (verified)

- **Prior art for R2, must be credited.** [Díaz-García, Bullo and Marden (2024)](https://arxiv.org/abs/2408.00883), "Strategic coalitions in networked contest games", arXiv:2408.00883. Players with budgets $B_i$ in bilateral lottery contests ($r=1$) on the edges of a graph with values $v_{ij}$. Their Lemma 1 replaces each budget by a multiplier $\lambda_i$ and obtains $x^\ast_{ij}=v_{ij}\lambda_j/(\lambda_i+\lambda_j)^2$, hence share $\lambda_j/(\lambda_i+\lambda_j)$. Our R2 with $r=1$ is their result written in $s_i=1/\lambda_i$. What we add: money has an outside use, so $\lambda_i\ge1$ and a principal can be unconstrained ($s_i=1$); general $0<r\le1$; and the economic reading (R3–R8). Say this plainly; the toy model is extracted from the literature, as the commission asked.
- [Tullock (1980)](https://www.gbv.de/dms/zbw/02063613X.pdf) [link is the volume's table of contents; cite as: "Efficient rent seeking", in Buchanan, Tollison and Tullock (eds), *Toward a Theory of the Rent-Seeking Society*, Texas A&M University Press, 97–112]. The contest form and the symmetric result ($x^\ast=rV/4$ each, $rV/2$ in total) are the textbook derivation from it.
- [Baye, Kovenock and de Vries (1994)](https://doi.org/10.1007/BF01053238), Public Choice 81: 363–380. For $r>2$ the equilibrium is in mixed strategies and, with continuous spending, the whole stake is dissipated; over-dissipation never occurs. (Replace the "pure equilibrium for $r\le2$" caveat in R1 with: in our range $0<r\le1$ each payoff is concave in own spend; for $r>2$ see this paper.)
- [Skaperdas (1996)](https://doi.org/10.1007/BF01213906), "Contest success functions", Economic Theory 7(2): 283–290. Axiomatises the family $f(x_i)/\sum_j f(x_j)$; the power form $x^r$ is the member for which only the ratio of efforts matters (multiplying every effort by the same factor changes nothing). Do not say "unique" and do not cite axiom numbers.
- [Hirshleifer (1989)](https://doi.org/10.1007/BF00153394), Public Choice 63(2): 101–112. Ratio versus difference forms; under the ratio form neither one-sided submission nor two-sided peace can be an equilibrium. (This is exactly why, in R7, a challenge is always worth bringing absent a fee. Worth one sentence: the result depends on the ratio form, and Hirshleifer flagged the property as its weakness.)
- [Jia (2008)](https://doi.org/10.1007/s11127-007-9242-1), Public Choice 135: 125–130. A stochastic derivation of the ratio form from random shocks to performance.
- [Baye and Hoppe (2003)](https://ideas.repec.org/a/eee/gamebe/v44y2003i2p217-226.html), Games and Economic Behavior 44(2): 217–226. A tournament in which each firm buys independent draws of ideas and the best idea wins is strategically equivalent to a Tullock game. For the search microfoundation: state the fact that with independent draws from one continuous distribution the chance of holding the best draw is $x_i/(x_i+x_j)$ as an elementary identity, and cite this paper for the best-draw model, not for the identity.
- [Hirshleifer (1991)](https://doi.org/10.1111/j.1468-0343.1991.tb00046.x), "The paradox of power", Economics & Politics 3(3): 177–200. Poorer contenders rationally fight harder; only when decisiveness is high enough does the richer side gain relatively.
- [Skaperdas (1992)](https://www.jstor.org/stable/2117341), AER 82(4): 720–739.
- [Che and Gale (1997)](https://doi.org/10.1023/A:1017937708549), Public Choice 92: 109–126. Tullock contest with budget-constrained players: a lower exponent can produce more dissipation than a higher one, and rents stay under-dissipated.
- [Che and Gale (1998)](https://www.jstor.org/stable/116854), "Caps on political lobbying", AER 88(3): 643–651. In an all-pay auction (a different contest form from ours) a rigid cap on individual spending can raise total spending, because it levels the field. Use only as a caution in the caps row, with that qualification.
- [Friedman (1958)](https://doi.org/10.1287/opre.6.5.699), Operations Research 6(5): 699–709. Two players with budgets across many contests of the lottery form: allocating in proportion to the value of each contest is an equilibrium. (Echoed by our "splits its budget in proportion to stakes".)
- [Franke and Öztürk (2015)](https://doi.org/10.1016/j.jpubeco.2015.04.002), "Conflict networks", J. Public Economics 126: 104–113: bilateral Tullock contests on a network with a convex cost of total spending (no budget); unique interior equilibrium. [Xu, Zenou and Zhou (2022)](https://cepr.org/system/files/publication-files/DP13647.pdf), J. Economic Theory 206: existence and, under strongly monotone costs, uniqueness for general conflict structures. Neither covers our hard budget with an outside value of money; hence "verified numerically, no uniqueness theorem claimed".
- [Hirshleifer and Osborne (2001)](https://doi.org/10.1023/A:1017520505573), "Truth, effort, and the legal battle", Public Choice 108: 169–195. Litigation as a contest in which success depends on the merits and on each side's effort. Our $\theta$ plays the role of a bias toward the defender.
- [Wallis and North (1986)](https://www.nber.org/system/files/chapters/c9679/c9679.pdf), "Measuring the transaction sector in the American economy, 1870–1970". The transaction sector grew from roughly a quarter of US GNP in 1870 to over a half in 1970 (their Table 3.13: 26% to 55% on the broader definition). Confirmed; use in R1.
- [Baumol (1990)](https://doi.org/10.1086/261712), JPE 98(5): 893–921; [Murphy, Shleifer and Vishny (1991)](https://academic.oup.com/qje/article-abstract/106/2/503/1905462), QJE 106(2): 503–530: talent flows to rent-seeking when the rules reward it. Optional, for the dissipation discussion.

Calabresi and Melamed: no confirmed stable URL; cite without a link.
