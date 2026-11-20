# Repeated-games, equilibrium-selection and learning theorist (Opus). Dispatched later on Dan's objection; received sixth, 2026-10-21. Verbatim.

Red-team report: repeated games, equilibrium selection and learning (read-only)

Sources. I read `/Users/dan/Source/livingthing/_plans/hyperscaling_coase_commitment_model.md` and the river section of `/Users/dan/Source/livingthing/notebook/hyperscaling_coase.qmd` (lines 102–219). I opened no other `_plans/` file.
- I checked these abstracts or secondary statements online: Ellingsen–Miettinen 2008 and 2014, Miettinen–Perea 2015, Miettinen–Vanberg 2025, Chatterjee–Sabourian 2000, Gilboa–Samet 1989, Ben-Porath's automata paper, Abreu–Pearce 2007 (through Wolitzky 2011), Wolitzky 2011, Kambe 1999 and Abreu–Gul 2000 (through Levin's notes), Young 1993 and Binmore–Samuelson–Young 2003 (through Naidu–Hwang–Bowles 2010 and Gallo 2011), Fish–Gonczarowski–Shorrer and Akata et al. Everything else is from memory and tagged.
- I ran the arithmetic in the session scratchpad. No repository file was touched.
- Notation: "bloc" means the residents bargain as one. Unless stated otherwise, π=20 and k=3, so the pie is 6.

---

## 1. Convergence claim: FAILS

### 1a. Which cells have a unique one-shot equilibrium?

**Cell A** has no protocol stated.
- As a Nash demand game, every split (d, 6−d) is an equilibrium. So is every profile in which both sides demand at least 6, which ends in disagreement. [sure]
- A becomes unique only under bilateral alternating offers with the residents as a bloc. The proposer then gets 6/(1+δ), which tends to 3–3 as δ→1 (Rubinstein 1982; Binmore–Rubinstein–Wolinsky 1986). [sure]
- The river's actual k=3 structure is three separate vetoes plus the factory. In four-party unanimity bargaining, every individually rational allocation is a subgame-perfect equilibrium for patient players. This is Shaked's result, restated in the Chatterjee–Sabourian 2000 abstract. [sure]
- The stationary equilibrium, the Shapley value of this unanimity game and the four-party Nash solution all give 1.5 to each party. Payments are then (3.5, 4.5, 10.5), the factory keeps 1.5, and S=3/4. [sure]
- So the model's S=½ is a selection, and it also assumes bloc bargaining.

**Cell B** is unique in subgame-perfect equilibrium only if two conditions hold.
- The residents must break their indifference toward accepting.
- They must respond as a bloc or one after another. With three simultaneous votes, "all reject" is an equilibrium of the voting stage, because no single resident is pivotal. So the standoff is a subgame-perfect outcome of B unless weakly dominated strategies are eliminated. [sure]
- In plain Nash equilibrium there is a continuum of outcomes. [sure]

**Cell C** is unique for the bloc's share (S=1) under the same refinements. How the residents divide the 6 among themselves is a three-player demand problem with a continuum of equilibria. [sure]

**Cell D** is not unique.
- Ellingsen–Miettinen 2008 (verified): with commitment attempts that never fail, which is the model's "provable", three outcomes survive iterated strict dominance.
  - In two of them one side takes the whole surplus. These are exactly B's S=0 and C's S=1.
  - The third has a high probability of conflict.
- Uniqueness needs commitment attempts that fail with probability 1−q>0. Conflict then occurs with probability q². With commitment costless (c=0), the analogous results need iterated weak dominance. [sure]
- So D under provable commitment is the union of B, C and a likely standoff, not a fourth outcome.

**Summary.** Only B and C are singletons, and only after refinement. The two cells the thesis rests on, A as the human baseline and D as the agents' default, are exactly the ones without a unique outcome.

### 1b. Is "plays its cell's equilibrium on the estimates" a defined strategy?

**In A and D, no.** It needs a selection rule.
- If each agent selects independently, the demands are incompatible whenever the selections differ.
- "Each side picks its favourite equilibrium" is Ellingsen–Miettinen's third outcome. The standoff then comes from the selection rule, not from compute.

**In B it is the wrong strategy.**
- Literal plug-in play means offering the estimate ĥᵢ. With symmetric continuous errors each resident accepts with probability ½, so all three accept with probability 1/8 at every c. That does not converge.
- The model's B bullet quietly switches to a Bayesian safety margin.
- With Gaussian error σ_c and a pie of 6, the optimal margin is σ_c·z, where z solves φ(z)/Φ(z) = σ_c/6.
  - z = 1.39 at σ_c=1, 2.52 at 0.1, and 3.94 at 0.001.
  - So S falls like σ_c·√(2 ln(6/σ_c)), more slowly than the stated σ/√c. [computed]

**What would the agent be estimating?** The model faces a dilemma between the river's two settings.
- In the transparent setting h and π are common knowledge, so there is nothing to estimate.
- In the private setting the river section itself says each resident "is the only source of our own $h_i$ and is paid to misreport it", and that "the price of a FLOP does not appear" in those theorems. A Monte Carlo rate does not apply to a value someone reports strategically.
- Hart–Mas-Colell 2003: dynamics in which each agent knows only its own payoffs ("uncoupled") cannot guarantee convergence to Nash equilibrium. The obstacle is information, not computation. [sure]
- Stochastic procedures of the regret-testing kind (Foster–Young 2006) do reach an approximate Nash equilibrium, but which one is random. [likely]

**No-regret learning does not help.** No-regret dynamics converge to the set of coarse correlated equilibria. [sure] In the bloc demand game, putting probability 1/3 on each of (6,0), (0,6) and (6,6) is a correlated equilibrium. Each side expects 2, and any deviation to a fixed demand x earns x/3 ≤ 2. So learners can settle into a one-third standoff rate as easily as into an efficient split. [computed]

### 1c. The model's own error device reverses the D bullet

Section 5 lets agents estimate "how big the pie is". Apply that to D, where binding demands are simultaneous and each side has private Gaussian noise of size σ_c on the pie. That is Nash's 1953 smoothed demand game.
- Its interior equilibrium is unique and symmetric. (6,6) is never an equilibrium when σ_c>0.

| σ_c | Demand per side | Probability of agreement |
|---|---|---|
| 1 | 2.62 | 0.78 |
| 0.3 | 2.75 | 0.95 |
| 0.1 | 2.89 | 0.987 |
| 0.01 | 2.985 | 0.999 |

[computed, best responses checked]

- As c→∞, D converges to the 3–3 split with certainty. The standoff does not become certain.
- The general logic is that of global games: vanishing private noise selects an equilibrium, it does not reproduce the full set (Carlsson–van Damme 1993 [sure]; Carlsson 1991 for bargaining [likely]).
- The model's actual D mechanism, misjudging whether the other side has committed, does nothing under its own premise. A provable commitment is checked by a hash at negligible cost.

### 1d. Which equilibrium do very capable agents select?

**Strongest case that budgets settle it.** In the symmetric bloc river, almost every selection theory gives 3–3:
- Nash smoothing (1c above);
- alternating offers as the time between offers shrinks (Binmore–Rubinstein–Wolinsky) [sure];
- Young 1993 adaptive play in the demand game, which picks the Nash split under uniform noise, and also under intentional noise (Naidu–Hwang–Bowles 2010) [sure];
- Binmore–Samuelson–Young 2003, which picks the Nash split in the demand game [sure];
- Kambe 1999 and Abreu–Gul 2000: as the probability of commitment types goes to 0, the war of attrition yields the Nash split weighted by patience [sure];
- Abreu–Pearce 2007: in repeated games with contracts, all perfect Bayesian payoffs converge to Nash bargaining with threats [sure];
- the Kalai–Smorodinsky and egalitarian solutions, which coincide at 3–3 here;
- Harsanyi–Selten 1988, which selects the Nash product in unanimity games [likely], giving S=3/4 with separate vetoes.

On this reading selection is settled, but at cell A's number (or 3/4), not at B, C or D.

**Strongest case that it does not settle.**
- The selected point depends on which perturbation is assumed:
  - commitment that fails with probability 1−q gives conflict with probability q² [sure];
  - noise on the pie gives 3–3;
  - short-lived commitments with alternating offers give immediate agreement at the reversed Rubinstein split (Miettinen–Perea 2015, verified) [sure];
  - durable commitments that lapse give a war of attrition (Ellingsen–Miettinen 2014, verified) [sure];
  - Binmore–Samuelson–Young: Kalai–Smorodinsky in the contract game but Nash in the demand game [sure];
  - Wolitzky 2011: adding one "soft" behavioural type to Abreu–Pearce makes almost every efficient individually rational payoff an equilibrium [sure].
  - Which errors agents make is a design fact, not a budget fact.
- Lock-in. In stochastic-stability models the expected time to leave a non-selected convention grows like ε^(−R) (Kandori–Mailath–Rob 1993; Young 1993; Ellison 1993, 2000) [sure]. Under the model's own mapping, where errors vanish as c→∞, selection takes forever. In the limit every convention is absorbing and history decides.
- Empirical evidence:
  - Calvano et al. 2020: Q-learning agents converge to above-competitive outcomes sustained by punishment, not to the one-shot prediction [sure].
  - The level depends on design: synchronous versus asynchronous updating (Asker–Fershtman–Pakes 2022) [likely], auction format (Banchio–Skrzypacz 2022) [likely], exploration (Abada–Lambin 2023) [likely].
  - LLM pricing agents reach above-competitive prices, and innocuous changes in prompt wording substantially change how far (Fish–Gonczarowski–Shorrer) [sure].
  - LLMs do well in prisoner's-dilemma-type games and poorly at coordination games such as Battle of the Sexes (Akata et al.) [sure].

### 1e. What survives, and what role compute keeps

**Surviving statement:** "If budgets buy precision, then in non-recurring play whose equilibrium is unique after refinement (B, C), Bayesian agents approach it. In A and D the limit is whichever equilibrium the agents' remaining errors and history select: 3–3 under noise about the pie, conflict with probability q² under commitment failure. In recurring play there is no single cell outcome (section 2)."

Compute keeps three roles. None has the essay's sign.
1. **Ratios matter, not levels.** In Young's adaptive play the selected division is an asymmetric Nash split whose weights rise with each side's information (sample size) [likely]. In Gallo 2011's network version, a group's weight is set by its least-informed members [likely]. That reads as: the residents' share is set by their worst agent.
2. **Levels set how strong lock-in is.** Better agents make the first convention stickier, so the rule in force when they arrive matters more.
3. **Verification capacity.** Compute bounds which conditional commitments can be checked (Tennenholtz 2004 [sure]; Critch 2019 [likely]). More compute enlarges the equilibrium set rather than narrowing it.

Apart from these, the essay does reduce to equilibrium selection with a preamble about agents.

**Narrowing that would save a version of the claim:** replace "compute shrinks estimation error" with "technology raises commitment reliability q". Ellingsen–Miettinen then give conflict with probability q²→1, but only along q<1, and that is reliability rather than compute.

**What would settle it:**
- Fix a protocol and an error process for each cell and compute the limit as the error vanishes, as in 1c.
- Simulate learning agents (Q-learning and LLM agents) in the river under each cell's protocol, across compute levels and random seeds.
- The claim survives only if the distribution of S collapses to cell-specific points and the D standoff rate rises with compute.

---

## 2. One-shot framing: HOLDS WITH NARROWING

**What the folk theorem gives on the river's numbers.** Assume terms are set each period and commitments last one period.

- **k=3, π=20.**
  - Every party's minmax is 0. The feasible set is Σu ≤ 6, which is full-dimensional.
  - As δ→1, every u ≥ 0 with Σu ≤ 6 is a subgame-perfect payoff in all four cells (Fudenberg–Maskin 1986). [sure]
  - Explicit thresholds for the bloc [derived]:
    - Repeated B: for δ < ½, S=0 is the unique equilibrium. For δ ≥ ½, every S in [0,1) is one. The residents can afford to reject any lowball because the reward is the whole future pie; the supremum argument gives V̄ ≤ 2δV̄.
    - Repeated C is the mirror image.
    - A and D, read as demand games: every split and the standoff are equilibria at any δ.
    - The standoff appears in B or C only through the simultaneous-vote loophole.
  - So at an annual discount factor of ½ or more (a 100% discount rate), S=0, S=1 and every split between them are equilibria whoever can commit. At δ ≥ ½ the four cells' sets of efficient equilibria coincide.
- **k=3, π=10.** The only individually rational feasible point is (0,0,0,0), so the river stays clean at any δ and repetition changes nothing.
- **k=1.** Minmax is (−2, −3, −9) for the residents and 0 for the factory. The residents' collective outcomes put the factory exactly at its minmax, which is outside the folk theorem's strictly individually rational set. See section 3.

**What the four-cell table still determines:**
- one-shot play;
- finitely repeated play with a known end and no reputational types. B and C have a unique refined one-shot equilibrium, so backward induction gives a unique equilibrium. A and D have several, so Benoit–Krishna 1985 multiplicity applies [sure];
- B and C when δ < ½;
- the threat points.

At k=3 it determines nothing about patient players' equilibrium set.

**How long a commitment lasts matters.**
- The model's revocation cost is per deal. An agent that publishes standing instructions commits to a whole repeated-game strategy.
- One-sided commitment of that kind makes that side the leader of the repeated game, so B or C survives repetition. This is the author's best reply.
- Two-sided commitment of that kind falls under the commitment folk theorem (Kalai–Kalai–Lehrer–Samet 2010; Tennenholtz 2004) [sure]: every individually rational division, the standoff included, is an equilibrium of the one-shot game. Published instructions bring the folk theorem into the one-shot river.

**Repeat players.**
- A developer buys from one-shot homeowners across many projects. Fudenberg–Levine 1989: a patient long-run player facing short-run opponents gets at least its commitment (Stackelberg) payoff if a Stackelberg type has positive prior probability [sure]. So the developer is in B by reputation, with or without agents (Galanter 1974) [sure].
- Between two comparably patient long-run players, reputation selects only weakly or indeterminately (Abreu–Pearce versus Wolitzky).

**Narrowing:** "The table describes one-shot sales of permanent rights (siting, buyouts) between parties who do not deal again and whose commitments are unconditional. For annually renewed consents at k=3 it determines nothing once δ ≥ ½. Where one side is a repeat player, its reputation already assigns the cell, so agents change the margin, not the cell."

---

## 3. The residents' pact (institutions-choose claim): FAILS at k=3, HOLDS WITH NARROWING at k=1

**k=3.**
- A lone resident has nothing to sell, because the factory still needs the other two. Breaking a joint demand gains nothing, so no enforcement is needed at any δ.
- "Resident 3, who has the most to lose from no deal, breaks first" is wrong. At k=3, no deal means a clean river, worth 0 to resident 3 as to everyone.
- What remains: coordinating on the internal split, and credibility toward the factory. Annual repetition supplies the latter at δ ≥ ½.

**k=1, π=10** (the pact is that nobody signs). After any signature, the pact collapses into undercutting, which is a valid equilibrium punishment.
- If the factory can only pay spot bribes of at most π per period:
  - each resident holds out iff δ ≥ (π−hᵢ)/π, which is 0.8, 0.7 and 0.1;
  - so the pact needs δ ≥ 0.8, and the weak link is resident 1, not resident 3;
  - with transfers from resident 3 to residents 1 and 2 the condition is Σ[(1−δ)π − hᵢ] ≤ 0, i.e. δ ≥ 8/15 ≈ 0.53.
- If the factory can pay a lump sum or sign a long-term contract with a defector (the present value of its gain):
  - the pact needs hᵢ + wᵢ ≥ π for every i with Σwᵢ = 0, i.e. 14 ≥ 30;
  - so it fails at every δ. This is the essay's empty-core gap of 8+7+1 = 16 against 0, now per period. [derived]

**k=1, π=20** (the pact sells consent at 20). With equal shares the pact needs δ ≥ 0.8; with the best internal split, δ ≥ 2/3; with long-term offers by the factory, never.

**How much this weakens the model.**
- At k=3 the enforcement claim is gone.
- At k=1 it survives exactly when the factory can contract with a defector over the future, which cheap agent commitment supplies. The rule needed can restrict the factory's side deals rather than the residents. Alternatively, an outside sanction worth 8, 7 and 1 per year of pollution to residents 1, 2 and 3 would do (community enforcement, Kandori 1992; multimarket contact, Bernheim–Whinston 1990 [sure]).

**What would settle it:** whether the essay's consents are permanent rights (the lump-sum case) or renewed each period.

---

## 4. Bounded compute acts as commitment, so r and c are not independent

**Results:**
- Gilboa–Samet 1989 (verified): an unbounded player facing a finite automaton has a dominant strategy (best respond), which the bounded player can exploit to "blackmail" it. In zero-sum games the unbounded player instead drives the automaton down to its security level. [sure]
- Ben-Porath (verified abstract): in zero-sum repeated games, values converge to the one-shot value even when one player's automaton is polynomially larger [sure]. An exponential gap can give an advantage [likely].
- Abreu–Rubinstein 1988: complexity costs shrink the equilibrium set but leave a continuum. [sure]
- Chatterjee–Sabourian 2000 (verified): in unanimity bargaining, complexity costs do not narrow the range of allocations. With noise added, only the stationary allocation survives, which is S=3/4 on the river. [sure]
- Neyman 1985: bounded automata sustain cooperation in the finitely repeated prisoner's dilemma. [sure]
- Press–Dyson 2012: a fixed extortionate strategy extracts surplus from an adaptive opponent. [sure]
- Deng–Schneider–Sivan 2019: an optimizer facing a no-regret learner gets at least its Stackelberg value. [sure]

**Implications:**
- The side that adapts concedes, and the side that is fixed, by limitation or by design, commits.
- Raw compute makes a side a better best-responder, which makes it the follower.
- Compute buys commitment power only when it is spent on shaping the other side's learning or on verifying conditional commitments. That is spending on r, not c.
- On the river: residents' agents that are no-regret learners against a fixed factory offer give S→0, and the reverse gives S→1. The cell is set by who learns and who commits.

---

## 5. Standoff claim: HOLDS WITH NARROWING

**Against it:**
- Ellingsen–Miettinen at q=1 give three outcomes, including B's and C's.
- Short-lived commitments in a sequential protocol give immediate agreement (Miettinen–Perea).
- Durable commitments give delay, not permanent impasse (Ellingsen–Miettinen 2014).
- Conditional commitments give the folk-theorem set.
- Noise about the pie gives 3–3.
- If commitments are observed as they are made, D is a race. The winner takes B or C, efficiently, with probabilities set by the speed ratio.

**For it:** Miettinen–Vanberg 2025 (verified): with minimum-share declarations that bind with some probability, unanimity is uniquely inefficient (delay) among majority rules, while all-but-one is fully efficient. [sure] This is real support at k=3.

**Narrowing:** "With simultaneous, durable, unconditional commitments that fail with probability 1−q, the pie of 6 is lost with probability q². In dynamic play this is delay, and among several parties it is specific to unanimity." The word "provable" has to go. One route by which compute would help the claim: cheaper compute pushes both sides' commitment times to a common latency floor, which makes commitments effectively simultaneous [unsure, my conjecture].

**What would settle it:** the protocol deployed agents actually use (simultaneous or sequential, durable or per round, conditional or not) and the value of q.

---

## 6. Bridge claim: FAILS as a general claim

**Against it:**
- In A, D and all recurring play, the human 50–50 norm is itself an equilibrium, and the robust selection theories pick the same point. Playing closer to equilibrium need not move it.
- In repeated settings, learning agents reach cooperative or collusive outcomes (Calvano; Fish).
- Gale–Binmore–Samuelson 1995: learning in the ultimatum game converges to Nash equilibria in which low offers are rejected, not to the subgame-perfect outcome [sure]. The subgame-perfect outcome is approached only if responders' noise is small relative to proposers' [likely]. So it is the residents' precision, not the factory's estimation, that drives B to S=0.
- LLMs reproduce human fairness behaviour in ultimatum games (Aher–Arriaga–Kalai 2023) [likely].

**Narrowing:** "Where the human outcome rests on a tie-break at indifference in one-shot play (B, C), more precise agents remove it. Elsewhere they converge to some equilibrium, often the norm, and hold it longer."

**What would settle it:** test LLM agents of increasing capability in one-shot ultimatum and demand games and in the repeated river, and see whether the offered share falls in B and the standoff rate rises in D.

---

## Claims outside my assignment that I believe are wrong

1. **A's S=½.** With three separate vetoes the symmetric selections give S=3/4, so forming a bloc lowers the residents' share when nobody can commit.
2. **"Resident 3 breaks first."** Wrong at k=3 (see section 3). At k=1, resident 1 breaks first (thresholds 0.8 versus 0.1).
3. **The Ellingsen–Miettinen paraphrase in section 3 D.** At q=1 there are three outcomes. Their main results assume a positive commitment cost throughout. Conflict is unique only for q<1, with probability q².
4. **"A liability rule is cell B written into law" and "nothing else gets out of D".** A statute can fix any S: harms plus 1.5 each gives S=3/4. D can also be left by:
   - sequencing,
   - arbitration,
   - randomising who commits,
   - safe Pareto improvements (Oesterheld–Conitzer 2022) [sure],
   - conditional commitments,
   - repetition.
5. **Section 6, "the only place the ratio of compute matters".** False: there is the commitment race in D, Young's asymmetric weights, and the leader-versus-learner asymmetry.
6. **The rate in section 5 B.** The margin is σ_c·√(2 ln(6/σ_c)), not σ_c, and literal plug-in play deals with probability 1/8 at every c.
7. **The D mechanism in section 5** contradicts "provable" commitment.
8. **Section 7, "his bargaining club is cell D".** Agents that negotiate freely can condition commitments on each other, and whether a club fails depends on its voting rule (Miettinen–Vanberg).
9. **Section 8, bullet 2.** Durable commitments that can lapse give a war of attrition that ends in agreement, not a collapse into B or C.

---

## Most damaging objection from my angle

The model needs each cell to be a function from "who can commit" to an outcome, so that compute can push play toward it. In the cells that carry the thesis it is a set of outcomes: D under provable commitment contains B's and C's outcomes, by Ellingsen–Miettinen's own abstract.

Both ways the model lets agents improve act on that set against the thesis.
- Sharper private estimates of the pie are Nash's smoothing, under which the standoff disappears. Agreement on 3–3 rises from 0.78 to 0.999 as σ_c falls from 1 to 0.01.
- Published, checkable instructions are conditional commitments. Their equilibrium set is every individually rational division, the same set that annual repetition already produces at δ ≥ ½.

So "more compute makes the cell's outcome more exact" has no referent. What compute plausibly does is lock in whichever convention forms first, and tilt it toward the better-informed side.
