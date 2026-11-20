# hyperscaling_coase — claims ledger for red-teaming

Written 2026-10-15 from the restructure discussion. The purpose of the essay is now: a productive analysis of *if, when and whom* the Coasean-bargaining-at-scale agenda favours. This file states the thesis as numbered claims, each with its assumptions, evidence, scope and what would refute it, so that the logic can be attacked before any prose is written. The model is the river of `hyperscaling_coase.md` (The model) plus the constitutional stage defined in §2 below. Nothing here is in the essay yet.

## 1. Thesis

Under a uniform fall in the unit price of compute $p$, with institutions held fixed:

- **T-i.** The probability that a party ends worse off than its no-deal position, $X_j$, falls, through cheap verification, wherever the clause menu is capped and the party holds a veto.
- **T-ii.** The share of created surplus a party receives, $S$, does not change, because it is fixed by proposal power and the acceptance rule, neither of which depends on $p$. (Narrowed by W2 below.)
- **T-iii.** The efficiency gap $G$ falls where consents are substitutes or the rulebook holds, and rises where the division or the menu is open.
- **T-iv.** Institutions are not held fixed by the technology, whose comparative advantage is renegotiation, so T-i to T-iii hold only where something outside the market enforces the caps.

Object-level reading: cheated less often; a bigger share no more often; negative wherever cheap cognition can reopen what was settled.

## 2. Objects

Metrics, for regime $R$, budgets $b$, price $p$, draw $\omega$: $X_j=\Pr_\omega[u_j<u_j^0]$; $G=\mathbb E_\omega[W^*-W]$; $S=\mathbb E[\sum_i(u_i-u_i^0)]/\mathbb E[W-W^0]$.

Returns to compute, with $c=m/p$ operations from money $m$. Decision problem: $V(c)=v\,\Phi(\Delta\sqrt c/\sigma)$ for $c<D$, $v$ for $c\ge D$; knee $c^*=\min\{D,(z\sigma/\Delta)^2\}$, fixed by the task. Contest (ratio form): $P_A=c_A/(c_A+c_B)$, marginal value $vc_B/(c_A+c_B)^2>0$ throughout, $P_A=m_A/(m_A+m_B)$ independent of $p$.

Constitutional stage: a regime $R\in\mathcal R$ (entitlement $k$, partition into reaches, clause menu, division rule); proposal power $(\mathcal P,\mathcal W,R_0)$ = who may propose, the winning coalitions of the acceptance rule, the reversion regime. **Collective reading:** an adopted $R$ binds everyone, rejecters included. **Opt-in reading:** $R$ binds signatories only. Draw $\omega$ known to whoever surveyed; others hold the prior $F$ and their own $h_i$. Two sources of ignorance under $F$: of the instance (scope, or ex ante timing) and of the role.

## 3. Claims, by node of the path

**Preamble, the floor (invariant in $p$).**

- **C1.** At $k=1$ the core is empty; at $k=0$ the core is nonempty and the simultaneous-contribution game can land outside it; under private harms no voluntary, budget-balanced, incentive-compatible mechanism is efficient, and at $k=n$ the probability of efficiency falls to zero in $n$. *Evidence:* the cores in the plan; Myerson–Satterthwaite; Mailath–Postlewaite; Aivazian–Callen. *Refuted by:* a protocol reaching welfare 0 at $k=1$ without binding agreements, or a mechanism beating M–S.
- **C2.** Every anti-holdout device lowers $k$, and at $k<n$ the non-pivotal are harmed and unpaid. *Evidence:* the equity passage. *Refuted by:* a device that closes deals at $k=n$ without overriding anyone.

**Node 1. Substitutes?**

- **C3.** Where consents are substitutes, an anonymous posted price clears the market with minimal communication (Jordan), there is no contest, and cheaper compute lowers unit costs for all parties. *Scope:* most consumer and small-coordination markets. *Refuted by:* substitute markets where agent asymmetry extracts; see W3.
- **C4.** Where consents are complements, no anonymous price supports the efficient deal ($9\le c\le 20/3$ is empty); the fallback is personalized nonlinear prices, which is bargaining. *Evidence:* Bikhchandani–Ostroy; the arithmetic. *Solid.*

**Node 2. Menu capped?**

- **C5.** The clause count enters the bill as $n2^m$ in preferences and in bits (Nisan–Segal), and as $2^m$ human elicitation per bargain; no fall in $p$ touches the count. *Refuted by:* compact representations covering real contract preferences; see W4.
- **C6.** Nobody keeps $m$ small voluntarily: a clause one side adds is a contingency the other must price, so the side with the larger evaluation budget gains by adding. *Evidence:* argument only, uncited; see W5.
- **C7.** A fluent agent's comparative advantage is enlarging $m$. *Evidence:* a prediction about the technology; see W6.

**Node 3. Division pinned, or bargain small?**

- **C8.** With an open division and weighted consents, exact pivotality is #P-hard (Deng–Papadimitriou); parties hold sampled estimates with error $\sigma/\sqrt c$ (Castro); the side with tighter estimates picks off residents who underprice themselves. *Solid as stated.*
- **C9.** Contest invariance: with money budgets fixed and a ratio-form success function, a uniform fall in $p$ leaves both the division and the money spent on the contest unchanged. *Evidence:* Tullock. *Assumptions:* ratio form; budgets in money; effort = operations. *Refuted by:* the difference form; see W1.
- **C10.** Exact-play band: the contest collapses once $\min_j c_j\ge 2^{\bar n}$, i.e. once $p\le m_{\min}/2^{\bar n}$; $\bar n^*(p)=\lfloor\log_2(m_{\min}/p)\rfloor$ rises by one per halving. *Follows from C8.* Slow.
- **C11.** Pinning the division by a formula on observables removes the prize at any $n$ (Budish precedent). *Cost:* at $k=n$ a formula that underpays someone fails the deal. *Solid.*

**Node 4. Who set the rules, and when?**

- **C12.** A rule is a distinct layer only when it binds people who did not agree to it. Under an externality, an opt-in mechanism is a deal under the existing entitlement and inherits C1 and C2: one refuser blocks it at $k=n$, non-members are overridden at $k<n$. Krier's club, option fee and veto coalition are opt-in. *Evidence:* Snow's objection (plan, item 10); the river. *Must be spelled out in any version of the essay.*
- **C13.** Under the collective reading, proposal power fixes the share. Take-it-or-leave-it with unanimity: the proposer leaves everyone at reservation and keeps the rest. With majority: the median at reservation, the minority below. Verification pins $X_j=0$ under unanimity and informs without protecting under majority. None of $(\mathcal P,\mathcal W,R_0)$ depends on $p$. *Evidence:* Romer–Rosenthal; Example 1. *Narrowed by W2.*
- **C14.** Design under instance- and role-ignorance is a decision problem over draws with a knee; design by a role-committed party is a contest over roles even when instance-blind. *Evidence:* Example 2; an assertion about legislatures; see W7.
- **C15.** Verification is cheap only under a capped menu (C5) and protective only under a veto (C13).

**Node 5. Can the rules be reopened?**

- **C16.** The regimes under which C3, C10, C11 and C14 deliver are the ones whose terms the technology makes cheap to reopen; "institutions fixed" is not an equilibrium without outside enforcement. Verifiable non-adaptivity is the positive form (Rubinstein; Papadimitriou). *Refuted by:* evidence that agents converge on stable norms on their own; see W8.

**Object level.**

- **C17.** Most economic life sits at leaf A, substitutes. *Empirical assertion; see W9.*
- **C18.** T-i to T-iv follow from C3–C16 where those hold.

## 4. The path

Preamble: the river's three failures, before any compute. Node 1 substitutes? yes → leaf A (prices work; everyone gains; Krier right). Node 2 menu capped? no → leaf B (clause arms race; gains to whoever can afford to read). Node 3 division pinned or bargain small? no → leaf C (pivotality race; uniform halving changes nothing; asymmetric halving extracts). Node 4 rules set ex post by a party? yes → leaf D (agenda control; verification protects under unanimity only). Node 5 rules cheap to reopen? yes → leaf F (erosion; back to node 2 worse off); no → leaf E (cheated less, share by the rules, efficiency gains). Collapses: an open menu unpins the division; renegotiable rules uncap the menu; so six leaves.

## 5. Known weak points, to be attacked first

- **W1 (C9, T-ii).** The invariance uses the ratio form. Hirshleifer 1989 is literally ratio *versus difference* models: under the difference form $P_A$ depends on $c_A-c_B=(m_A-m_B)/p$, which *grows* as $p$ falls, so uniform cheapening sharpens the richer side's advantage. The essay cites the paper and currently assumes the form that favours its thesis. Which form fits pivotality-estimation, where the pick-off depends on the ratio of error bars $\sqrt{c_i/c_f}$, needs stating.
- **W2 (C13, T-ii).** Take-it-or-leave-it is the maximum of agenda control, correct for adhesion contracts and platform terms, wrong for legislatures, where sequential bargaining (Baron–Ferejohn) applies. The invariance in $p$ survives, with one exception: if agents bargain at machine speed, delay becomes cheap, and under unanimity with counter-proposals the standard stationary solution equalizes shares. Under majority the proposer and a minimal coalition still take most of it. So cheap compute *can* move the share, in the weak party's favour, exactly where the weak party holds a veto and may counter-propose. This is a point for Krier and must be in the essay.
- **W3 (C3).** "No contest under substitutes" ignores algorithmic collusion among sellers (Calvano et al.), a contest at leaf A that agents make easier. Uncited.
- **W4 (C5).** Compact preference representations (Ieong–Shoham; the essay concedes "compression is possible exactly when preferences have structure") may cover most real contracts, making $2^m$ a worst case nobody meets.
- **W5 (C6).** Clause complexity as a weapon is asserted, not cited, and may be contradicted by the empirical tendency toward standard forms.
- **W6 (C7).** That agents enlarge $m$ is a prediction; Krier predicts the opposite, convergence to stable equilibria.
- **W7 (C14).** Role-ignorance is rarely met; the realistic rule-maker is captured (Stigler 1971). If so, node 4 almost always resolves to leaf D and the "veil" branch is decorative.
- **W8 (C16).** Agents ossifying rules "wherever the budget ran out" is the essay's reply to Krier's convergence claim, and it is an assertion against an assertion.
- **W9 (C17).** "Most of economic life is substitutes" is doing a lot of work in the if/when/whom verdict and is unsupported.
- **W10 (meta).** Every length estimate this session has undershot by about half (8,500 → 13,566 → 14,264). The path-structure estimate of 7,000 is on the same method. Treat 10,000 as the prior.
- **W11 (the target).** Krier keeps the state as enforcer, claims "massive reduction, not zero", and proposes a democratic mode for community values. A red-team should check whether any claim above attacks a position he does not hold.

## 6. How to red-team this

Three attackers, each read-only, each returning per claim: holds / holds with narrowing / fails, the strongest counter, and what evidence would settle it. (a) The economist: C3, C9, C13, W1–W3, with the contest and bargaining literature. (b) The complexity theorist: C5, C8, C10, W4, whether the bounds apply to instances anyone meets and whether $\bar n^*$ matters at realistic sizes. (c) The Krier partisan: C2, C7, C12, C16, C17, W6–W9, W11, steelmanning the primary text as the plan records it. A fourth, optional: a legal scholar on C12 and the adhesion-contract reading of node 4.
