# Cold reader (Opus), model file + river section only, no brief. Received first, 2026-10-21. Verbatim.

Adversarial review of `_plans/hyperscaling_coase_commitment_model.md`, checked against the river section of `notebook/hyperscaling_coase.qmd` (lines 102–218, HTML comments ignored). I read nothing else and changed nothing.

## 1. What the model claims

**Setup.** The river runs under unanimity (k=3) with π=20 and harms h=(2,3,9). A deal leaves 6 of surplus after the residents' harms are fully paid. An outcome is scored two ways: whether that deal happens, and S, the fraction of the 6 that goes to the residents, treated as one bloc.

**What "commit" means.** To commit is to publish a demand together with a forfeit r that you pay if you back down. Agents are said to make this nearly free and checkable by publishing hashed instructions.

**The four cells, by who can commit:**
- Nobody can: the 6 is split 3/3, efficiently, so S=½.
- Only the factory can: it pays exactly the harms, so S=0.
- Only the residents can, as a bloc with the pact enforced: they demand 20, so S=1.
- Both can: each demands all 6, nobody backs down, and there is no deal.

**The claims built on the cells:**
- (i) Cheap agents give both sides commitment, which moves the default from haggling (A) to standoff (D).
- (ii) Only a rule that gives commitment to one side escapes D: a liability rule gives cell B, a union rule gives cell C. So institutions decide the outcome, not agents.
- (iii) Compute only shrinks estimation error, like σ/√c. More compute therefore drives each cell to its exact outcome: S→0 in B, S→1 in C, a certain impasse in D, little change in A. The sign of compute's effect is whatever the cell gives it.
- (iv) At k=1, π=10, the residents' only defence is a no-signing pact formed before the factory signs anyone. The pact wins that race with probability λ_N/(λ_f+λ_N), which does not change when compute gets cheaper for everyone. This is the only place relative compute matters, and the only case where a resident ends up worse off than under no deal.
- (v) Krier's examples map onto the cells. His free bargaining club is D, and it fails more reliably as the agents improve.

## 2. Assumptions an expert would refuse

- **Being checkable is not the same as being irrevocable.** "\"Cheap commitment\" means that setting up such a promise costs almost nothing and the other side can check it, which is what an agent that publishes its instructions and a hash of them provides, …"
  - A hash proves what the instructions said. It forfeits nothing when the principal re-instructs or replaces the agent.
  - By the model's own unit ("The unit of commitment is therefore money: the **revocation cost**…"), a hashed prompt has r≈0. That is cell A.
  - D destroys the 6, so both sides gain by withdrawing their positions together. The model never says why this renegotiation is unavailable. The same goes for the pocket-money promise: the sister can be paid to waive the forfeit.

- **Commitments are assumed simultaneous and unconditional, without saying so.** "So each side, before bargaining, may publish a **position** … and a revocation cost $r$."
  - D needs both positions fixed before either side sees the other's.
  - Published instructions arrive in some order. Under the model's own tie-break ("a penny more makes them accept"), whoever publishes second accepts a committed demand it can already see. That gives B or C, not D.
  - Readable instructions also allow conditional commitments ("demand 3 if your program demands at most 3"). This is the program-equilibrium setting (Tennenholtz 2004), where efficient divisions are equilibria.

- **The residents are treated as one bargainer.** "the residents', bargaining as one, is $d_N$ slices for themselves."
  - This assumes away how three veto-holders split their share, which is the river's own k=n holdout problem.
  - In a world where commitment is cheap "for whoever has an agent", each resident can commit to taking the whole 6 against the other two. That is D inside the union.
  - Residents who "cannot commit" (column 1 of the table) cannot bind themselves to act as one at all.
  - Cell B quietly treats the residents as three people, with separate offers of 2, 3 and 9.

- **Cell A's equal split is imported, not derived.** "The standard answer, which is what happens in experiments too, is that they split it: three and three."
  - At r=0 the model's own rules settle nothing: either side may back down for free, or neither does.
  - The likely sources are the symmetric Nash solution or Rubinstein (1982) with equal patience. Both are two-player results, neither is stated, and Rubinstein's split favours the proposer away from the limit.
  - The experiments are used selectively. Ultimatum experiments (Güth, Schmittberger and Schwarze 1982, and many since) show responders rejecting offers that leave them nothing. That is exactly cell B's offer, yet B assumes acceptance for a penny.

- **Compute is assumed to buy information at the sampling rate.** "…an error that shrinks like $\sigma/\sqrt{c}$, which is what estimating by sampling does."
  - Sampling what? In the transparent river there is nothing to estimate. In the private river, resident i is the only source of h_i and is paid to misreport it.
  - σ/√c is the rate for independent draws from a source that does not care about the result. A counterpart who gains from your error is not such a source.

- **Vanishing noise is assumed to return the noiseless outcome.** "As $c$ grows the errors vanish and play converges to the exact outcome of the cell."
  - A and D have many equilibria without noise, so there is no single "exact outcome" to converge to.
  - The limit of noisy play picks one equilibrium, and the noise determines which. Global games (Carlsson and van Damme 1993) are the standard demonstration.
  - In A, too, noisy demands sometimes clash and compute removes the clashes, so "More compute changes little" is unargued.

- **Cell B's margin and rate are wrong.** "…to avoid a refusal it offers a little more than its estimate, a safety margin proportional to its error."
  - Sampling gives unbounded, roughly Gaussian errors, so no margin avoids refusal. The profit-maximising margin is the error times a factor that grows like √(log c), and refusals still happen with positive probability.
  - So noisy B is inefficient, and compute raises efficiency there. "now with a direction and a rate" is wrong on the rate.

- **Humans are assumed to start in A.** "Humans sit near cell A by default, because for a human a believable commitment is costly to make."
  - Repeat players commit cheaply through reputation. The model's own B example ("what a developer's standard-form offer to every homeowner looks like") is humans in B today.
  - If the baseline is B, the residents already have S=0, and no move to D can lower their payoff. D then costs only the factory.

- **The race in section 6 takes compute as given.** "…are each proportional to that side's compute, … the chance the pact wins is $\lambda_N/(\lambda_f+\lambda_N)$."
  - The formula needs independent, exponentially distributed completion times. With fixed times, the faster side wins for certain.
  - It is Tullock's (1980) lottery contest. When each side chooses its spending, the equilibrium win probability is the ratio of stakes, V_N/(V_N+V_f): about 14 against 10 here, if the residents fund the pact jointly. That is independent of the price of compute.
  - So the invariance survives, but stakes decide the race, along with the residents' free-riding on funding the pact (the river's k=0 problem). The "ratio of the two sides' compute" does not.

- **Institutions are assigned to cells by fiat.** "A liability rule, … is cell B written into law: the factory's position is fixed by the statute and the residents have nothing to commit to."
  - A liability rule abolishes the veto. That is a change of entitlement (Calabresi and Melamed, whom the river cites), and S is whatever the statutory price makes it. It equals cell B only if that price equals each harm.
  - A union rule makes the residents bargain as one. It neither gives them commitment nor denies it to the factory, so it is not cell C.

- **S is asserted to be the right yardstick.** "The share is the right one."
  - S merges residents with harms 2 and 9, and it leaves out the factory, which is also one of the bargainers.
  - The model never says which S is equitable, so its closing phrase about "equitable outcomes" has no criterion behind it.
  - In B and C, compute only moves money between the parties. Only D destroys surplus.

## 3. Contradictions

- **Two parties against the river's four.** The model: "This is ordinary haggling over six slices between two parties who each need the other." The river: "There is a surplus of $6$ to divide among four parties, every resident is pivotal, and each can hold out for the whole $6$; if all three do, there is no deal even here." The river allows a k=3 impasse with no commitment technology at all. The model's table cannot represent that, and it sits badly with "Humans sit near cell A by default".

- **Resident 3.** "…the pact still has to be enforced among the residents, or resident 3, who has the most to lose from no deal, breaks first."
  - This contradicts §1: "a resident who does not sign gets nothing and the river stays clean, which is worth $0$ to everyone." At k=3, resident 3 loses nothing more from no deal than the others do.
  - The direction is also the k=1 one. The river says "at $k=n$ every consent is needed and each of us can hold the deal hostage", so the threat inside a k=3 union is a member holding out for more, not one undercutting.
  - In C the factory is left indifferent and accepts, so there is no impending no-deal for anyone to break under.

- **The signer.** "It is also the only cell in which a resident can end worse off than under no deal, which is the essay's yardstick: the two who did not sign." The river says the factory pays "one of us a token amount and the rest nothing". That token is below the signer's harm, so all three residents end up worse off than under no deal.

- **Backing down in D.** §3: "The positions are incompatible, neither can back down without paying more than the pie is worth, so nobody backs down." §5: "With limited budgets, a side may misjudge whether the other has really committed, and back down, and then there is a deal after all."
  - With r larger than the pie, backing down is worse than no deal whatever the other side has done. No belief about the other's commitment makes it pay.
  - So the only mechanism that gives compute a sign in D is ruled out by D's own definition.
  - §2 also says the other side "can check" a commitment, while §5 turns checking into an estimate.

- **Compute treated as information.** §5: "The factory needs to know each resident's harm to make its exact offer." The river: "…each of us is the only source of our own $h_i$ and is paid to misreport it." Also: "the price of a FLOP does not appear in them anywhere." §3 assumes every number is known (the factory offers exactly 2, 3 and 9). §5 assumes harms are unknown but learnable by computing, which is neither of the river's two information settings.

- **"The only place" relative compute matters.** "This is the only place in the model where the ratio of the two sides' compute decides anything, it is a race to commit first, …" At k=3, publishing commitments is also a race to commit first. And §5's D bullet makes the deal depend on both sides' errors.

- **Small stakes.** "The long tail of his small examples … is cell A with a custom already pinning the split, where none of this bites." This sits against §4's "If both sides have one, the default moves from A to D."
  - Commitment is said to cost "almost nothing" at any stake, so nothing in the model keeps small cases in A.
  - A custom that pins the split in A pins a compatible pair of positions in D just as well, because that pair is an equilibrium there.
  - §8 says agents "settle on conventions". In the demand game, conventions settle near the Nash split (Young 1993), which is the mechanism that dissolves D.

- **A falsifier that cannot fire.** "If the cost of a standoff is large enough that one side always backs down in D…" The model gives a standoff no cost beyond the lost 6, and with r larger than the pie no standoff cost could make backing down pay. A side that does back down had a small r and was never in D.

- **Minor:**
  - S is defined as a count ("of the $6$ slices, how many go to the residents") but used as a fraction ("$S=1$ means the residents got the whole pie").
  - σ is never defined, despite "with every word explained".
  - §6 calls the k=1 case a "cell", a word §3 reserves for A–D.
  - "the world is $6$ better off if the factory pollutes *and pays the residents for their harm*" ties efficiency to payment, which the river's linear welfare explicitly separates.

## 4. Numbers against the river

**Consistent:**
- 2+3+9=14, and 20−14=6, the river's "surplus of 6".
- In B, payments of 2, 3 and 9 leave the factory 6. In C, the demand of 20 leaves it 0. D forgoes 6.
- At π=10, 14>10, so the clean river is efficient.
- §6's "no stable division" matches the river's empty core. I checked it: the four together are worth 0, the factory plus resident i is worth 10−h_i = 8, 7 and 1, and those total 16.

**Inconsistent:**
- **Cell A's S=½.** The river's k=3, π=20 game is a pure four-player unanimity game: every smaller coalition is worth 0 and all four together are worth 6. Its Shapley value, and the symmetric four-player Nash solution, give each player 1.5. The residents then get 4.5, so S=¾. The model's "three and three" gives the factory three times what the average resident gets.
- **"The two who did not sign."** With a token signature, the residents end near −2, −3 and −9 against 0 under no deal. That is three residents worse off, not two.
- **Resident 3.** The numbers give him nothing more to lose from no deal than the other two; each gets 0.
- **Cell B's rate.** "about $\sigma/\sqrt{c_f}$ per resident" is off by a growing factor, as set out in section 2.

## 5. Claims resting on named but unstated results

- **Cell D and everything built on it.** "The result that this is what happens when committing is free and provable is Ellingsen and Miettinen 2008, … Crawford 1982 has the same conclusion with revocation costs." The model itself flags these as second-hand and unverified.
  - **What rests on them:** the first claim; "without them cheap commitment chooses D"; §5's D bullet; and §7's "bargaining club … is cell D" together with its closing "cheap commitment for everyone is a standoff".
  - **What I believe they say (both papers exist; I am unsure of the exact theorems):** in Ellingsen and Miettinen, conflict comes from commitment being costly, however slightly, or only sometimes succeeding. Free, certain commitment keeps the efficient equilibria, which plain demand-game logic gives anyway. In Crawford, impasse comes from revocation costs that are uncertain when the commitments are made.
  - **If so:** neither result gives certain impasse, and the model's own paraphrase ("with positive probability") does not support "nobody backs down. No deal." or "the standoff becomes certain". And if uncertainty is Crawford's engine, shrinking it with compute removes impasse rather than securing it.

- **The definition of commitment.** "This is Crawford's 1982 formulation and it is the standard one." If Crawford's revocation costs are random and learned privately, as I believe, the model's chosen, published r is a different object.

- **Unnamed but load-bearing:**
  - Cell A's ½ rests on "the standard answer" and "experiments".
  - §5's rate rests on "what estimating by sampling does".
  - §6's formula rests on the completion times being exponentially distributed.

- **Krier.** All of §7, and §1's "Krier's own large examples", depend on Krier's text. The model never quotes it, and I could not check it from the two texts I was allowed to read.

## 6. The most damaging objection

Cell D is asserted, not derived, and the model's own machinery selects against it. The load-bearing sentence is "The factory publishes \"I keep all six\" and the residents publish \"we take all six\", each with their hands tied."

- **Nothing selects it.** With free, certain, checkable commitment, D is Nash's demand game. Every pair of positions that sums to 6 is an equilibrium, (3,3) included. (6,6) is an equilibrium only weakly: facing a committed 6, a side gets 0 whatever it demands. Nothing in the model picks (6,6).
- **The model's own additions pick against it.**
  - Published instructions arrive in an order, so the second side to publish accepts, and the game lands in B or C.
  - Readable instructions allow conditional commitment, under which efficient divisions are equilibria.
  - §5's noise in estimating "how big the pie is" is Nash's own 1953 smoothing of the demand game. As the noise vanishes, its equilibria converge to the Nash bargaining split, here the efficient 3/3. In the smoothed game (6,6) is not even an equilibrium, because against a demand of 6 a small positive demand has positive expected value. Nash's uncertainty is shared by both sides; I have not checked the limit with the model's private estimates, but nothing in the model shows it is the impasse.
- **So "More compute makes the impasse more reliable" has no support, and probably the wrong sign.**
- **What falls with D:** the first claim, "without them cheap commitment chooses D", the only negative efficiency effect in §5, and the verdict on Krier.
- **What is left:** whoever alone can commit takes the surplus. That is the ultimatum game, which holds with or without agents. The remaining compute effects, the margins in B and C, are transfers between the parties, and they rest on compute buying information the river says it cannot buy.
