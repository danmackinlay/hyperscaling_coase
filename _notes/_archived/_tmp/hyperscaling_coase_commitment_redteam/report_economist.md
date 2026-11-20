# Economist in bargaining, contest and commitment theory (Opus). Received fifth, 2026-10-21. Verbatim.

## Red-team report: the commitment model (bargaining, contest and commitment theory)

**What I read.** All of `/Users/dan/Source/livingthing/_plans/hyperscaling_coase_commitment_model.md`, and lines 102–219 of `/Users/dan/Source/livingthing/notebook/hyperscaling_coase.qmd` (the river section). I opened no other `_plans/` file and wrote nothing to the repo. I ran the numbers in a throwaway `uv run --no-project` session.

**Sources checked.**
- Ellingsen & Miettinen 2008: full text.
- Crawford 1982: the abstract, plus E–M's account of it. The full text is paywalled.
- Ellingsen & Miettinen 2014, and Miettinen & Vanberg 2025: abstracts.
- Abreu & Gul 2000: excerpts (the PDF's font is garbled, so I decoded them), checked against Jonathan Levin's teaching notes on the paper.

Notation: E–M is Ellingsen & Miettinen, AG is Abreu & Gul, and IWD is iterated elimination of weakly dominated strategies.

---

## 0. What the cited papers actually prove (Q1)

**Ellingsen & Miettinen 2008, AER 98(4) [sure; read in full].**

The setup:
- The game is one-shot, the moves are simultaneous, and commitments are observable.
- Each side either commits to a demand s at cost c ≥ 0, or waits.
- Two waiters split the pie (b_1, b_2).
- A waiter facing a commitment gets the residual.
- Incompatible commitments pay −c to each side.
- A commitment sticks with probability q.

The results, by case:
- **q = 1, c > 0** (Lemma 1, Prop. 1). Only two strategies survive iterated strict dominance: "demand everything" and "wait". The game that remains is Chicken.
  - Its pure equilibria are one side demanding everything while the other waits. Those are the model's cells B and C.
  - In the mixed equilibrium each side waits with probability c/b_i, so conflict happens with probability (1 − c/b_1)(1 − c/b_2).
- **q = 1, c = 0** (Lemma 2, Prop. 2). Under plain Nash equilibrium, Crawford's many efficient compromises are all equilibria. Two rounds of IWD leave three outcomes: both demand everything (conflict), B, and C.
- **q < 1 and 0 < c < q(1−q)(1−b_i)** (Prop. 3(i)). Only "demand everything" survives iterated strict dominance. There is a unique equilibrium, with conflict probability q².
  - This holds "even as q is arbitrarily close to 1".
  - Above that cost band the game is Chicken again (Prop. 3(ii)).
- **q < 1, c = 0** (Prop. 4). The same unique conflict outcome, with probability q², reached by IWD.

So "no deal with certainty when commitment is free" is a paraphrase, not their result.
- In the free, certain case they report three outcomes, and two of them are efficient.
- Certainty does follow if you delete weakly dominated strategies a third time, for both players at once, because "demand everything" weakly dominates "wait" in the 2×2 game that remains. But that step depends on the order of deletion: delete one player's "wait" first and (greedy, wait) survives. They do not claim it.
- Their headline cuts against the model's paraphrase. What makes conflict unique is a small *positive* cost combined with commitment that *fails sometimes*. Perfectly binding commitment brings B and C back as equilibria.

**Crawford 1982 [sure on the abstract and on E–M's summary].** Impasse arises "when successful commitment is uncertain and irreversible".
- Whether a commitment sticks is settled only after the demands are made, and in his general case each side knows privately what backing down would cost it.
- His leading special case is a Prisoner's Dilemma. There, impasse has *positive* probability: q² ≤ 1/4 in the binary case with q < 1/2.
- With symmetric information and *strong* commitment, there are efficient and equitable equilibria, for example both sides committing to half.
- The abstract adds that making commitment harder "need not always lower the probability of impasse".

Crawford does not reach the same conclusion. His impasse comes from weak or uncertain commitment; the model's comes from strong commitment.

**Dynamic versions.**
- **E–M 2014, GEB 87 [sure, abstract].** Commitments are durable but decay at random, and sides can re-commit. The unique Markov perfect equilibrium is a war of attrition: both first commit to incompatible offers, and they agree once one commitment decays. In expectation the more patient and more committed side gets more. **The pie is lost to delay, not lost outright.**
- **Miettinen & Vanberg 2025, AEJ: Micro 17(1) [sure, abstract].** In multilateral bargaining where precommitments bind with some probability, unanimity is uniquely inefficient (it causes delay). Every other voting rule, including all-but-one, is fully efficient.
  - This is the strongest support the model has. But it puts the fault in the rule k = n, not in commitment.
  - I am [unsure] how cleanly their divide-the-dollar game maps onto the river, where the harms make it more than a split.

---

## 1. Standoff claim

**Verdict: HOLDS WITH NARROWING, and the narrowing is heavy.** As worded — certain no-deal, from cheap *provable* commitment, citing E–M and Crawford — it fails.

**Counter-arguments.**

- **On the model's own premise, cell D is not an equilibrium.** The premise is that r exceeds the pie and the commitment is provable, which is E–M's q = 1.
  - With any positive cost of committing, the profile in D is not an equilibrium. Against a side committed to 6, posting nothing saves the cost and still yields 0. The game is Chicken [E–M, sure].
  - In river units (pie 6, uncommitted split b = 3), the pure equilibria are exactly B and C.
  - The mixed equilibrium has a standoff with probability (1 − c/3)², and each side's expected gain is exactly c. For example, c = 0.06 gives a 98% standoff.
  - So D is the symmetric mixed equilibrium of a game whose pure equilibria are the model's other two cells.

- **If revocation costs are chosen rather than given (Q2).**
  - First, a correction: in Crawford they are *not* chosen. They are random draws. Players choose only whether to attempt commitment and what to demand.
  - Suppose instead each side picks a bond r together with its demand d, at a posting cost κ:
    - κ = 0: this is E–M's q = 1, c = 0 case. Nash gives the many-compromise set; two rounds of IWD give standoff, B or C.
    - κ > 0: Chicken, as above.
    - If postings are sequential, the second poster sets r = 0 and accepts, and the first takes all six.
    - If revocation costs rise with the amount conceded and are never prohibitive (Muthoo 1996, per E–M's summary) [sure], the unique outcome is an efficient compromise.
  - The standoff survives only three ways: as the mixed equilibrium, as a weak equilibrium when κ = 0, or with q < 1.

- **Conditional commitment.** Published instructions can be programs that condition on the other side's published program.
  - Three results apply: program equilibrium (Tennenholtz 2004, GEB) [sure]; the commitment folk theorem (Kalai, Kalai, Lehrer & Samet 2010, GEB) [sure]; and observable delegation contracts (Fershtman, Judd & Kalai 1991, IER) [sure the paper exists; likely on the folk-theorem form].
  - Under them, every individually rational split, 3/3 included, is an equilibrium.
  - Example: "demand 3 if your program demands ≤ 3 against me, else demand 6", played against itself, is an equilibrium. E–M's dominance argument does not delete it, because against itself it beats "always 6".
  - The model's restriction to unconditional demands is doing the work.

- **Abreu & Gul (Q3) [sure on the main result].**
  - **Is the limit a war of attrition independent of protocol?** Yes. With commitment types on both sides, take any sequence of protocols in which both sides can make an offer within every interval ε. As ε → 0, play converges to the unique equilibrium of a continuous-time war of attrition, independent of protocol. They prove this for one commitment type per side [sure]; the general case is [likely].
  - **What decides it.** The weakness index T_i = −ln(z_i)/λ_i, where:
    - z_i is the prior probability that side i is genuinely committed;
    - λ_i = r_j(1 − α_i)/(α_i + α_j − 1) is i's equilibrium concession rate;
    - r_i is i's discount rate (impatience) and α_i its demand.
    - The weaker side concedes at time 0 with positive probability. A side is weaker when its prior credibility is lower or it is less patient.
  - Perpetual disagreement has probability only z_1·z_2. The rest of the loss is delay.
  - In the symmetric case with one posture per side, the expected loss is at least 2α − 1 of the pie [sure].
  - With a rich set of postures, as z → 0 the outcome converges to the patience-weighted (Rubinstein/Nash) split, with no delay (Kambe 1999; AG) [likely].
  - AG explicitly link this to the Coase conjecture: at frequent offers, revealing that you are flexible means conceding.
  - **Net effect on cell D: it mostly undercuts it.**
    - There is no certain no-deal.
    - The winner is set by *ratios* of credibility and patience, so one side wins, as in B or C with delay.
    - Speed and protocol wash out.
    - It supports only "symmetric greedy postures burn most of the pie in delay".
    - With verifiable code, z is known to be 0 or 1, AG has no bite, and we are back in E–M's static Chicken.
  - Contest theory agrees: the complete-information war of attrition has efficient equilibria where one side concedes at once, plus a dissipative symmetric one (Hendricks, Weiss & Wilson 1988) [likely].

- **Step or continuous (Q6).** In the model "can commit" is binary, and compute enters only as σ/√c, which never appears in D's outcome. **So "as budgets rise" is the wrong variable for the standoff claim.**
  - The right variables are the cost of committing relative to the pie (c/6) and how reliably a commitment sticks (q).
  - E–M make the outcome a threshold in those: for q < 1 there is a unique standoff iff c < 3q(1−q) slices.
  - At q = 1 there is no threshold: the standoff appears only in the mixed equilibrium, with probability rising smoothly as c falls.
  - One perverse case: at fixed c, pushing q toward 1 eventually leaves the unique-standoff region.

**Narrowing that saves it.** "One-shot; both sides can make observable, nearly free commitments that stick with probability q < 1; and c < 3q(1−q) of the six slices. Then the unique equilibrium has both demanding all six, and the standoff has probability q²."
- Examples: q = 0.9 needs c < 0.27 and gives an 81% standoff; q = 0.99 needs c < 0.03 and gives 98%.
- If commitment binds perfectly, the outcome is B or C, or a standoff with probability (1 − c/3)² in the symmetric mixed equilibrium.
- If sides can re-commit, the outcome is delay, and the more patient, more credible side wins.
- E–M's remark that, at a fixed commitment cost, bigger pies invite conflict genuinely supports the model's "large stakes" framing in §8 [sure].

**What would settle it.**
- Specify the agents' commitment technology: cost per commitment, probability it sticks, decay rate, and whether instructions may condition on the other side's instructions.
- Solve E–M 2014 at the river's numbers to get the expected loss from delay.
- Measure q empirically: how often principals override or redeploy an agent after publishing its instructions.

---

## 2. Default-shift claim

**Verdict: FAILS.**

**Counter-arguments.**

- **The empirical premise.** In large cases humans are not near cell A, and the model says so itself: cell B is "what a developer's standard-form offer looks like".
  - Repeat players commit routinely: posted prices, most-favoured-customer clauses, delegating to negotiators with limited authority, strike votes.
  - Holdouts look like D, which is why eminent domain exists.
  - The rationalist literature on impasse (Fearon 1995) [sure] already names commitment problems and private information as its human causes.

- **The mechanism.** A published hash proves *which* instructions run, not that the principal cannot redeploy the agent. That is observability, not irrevocability.
  - Katz 1991 (RAND) [sure]: delegation contracts that are unobservable or renegotiable carry no commitment value.
  - Irrevocability needs a bond, an escrow or a court, which is an institution. So "without institutions cheap commitment chooses D" refutes itself: without an institution there is no r.
  - The author's best defence comes from this very gap: commitments that are observable but imperfectly binding are E–M's q < 1 case, where the unique standoff lives. But that delivers a probability of q², and the driver is imperfect binding, not proof.

- **Equilibrium selection with roles.** Factory and residents are distinct roles.
  - In games where players know their roles, only strict (pure) equilibria are evolutionarily stable (Selten 1980) [sure], so a convention picks B or C, not the mixed standoff.
  - Risk dominance (Harsanyi & Selten) [sure] in the river's Chicken: (factory commits, residents wait) risk-dominates iff (3 − c_f)·c_N > c_f·(3 − c_N), which holds iff c_N > c_f. Only the comparison of costs matters, not their level.
  - The residents must first agree among three people, while the factory is one principal. So c_N > c_f, and the selection is **B: efficient, S = 0.**
  - Long-run learning dynamics pick the risk-dominant convention (Young 1993; Kandori, Mailath & Rob 1993) [likely for this two-population game].

- **The Coase conjecture (Q5).** An uninformed offerer who cannot commit loses its power as offers become frequent (Gul, Sonnenschein & Wilson 1986) [sure].
  - With private harms at machine speed, cell A is not 3/3. The factory's offers climb to the top of the range of possible harms, and the residents keep the rents from their private information.
  - **Does it undercut cell B?** Not if the factory's commitment is truly irrevocable, which is the cell's premise. Yes if the "commitment" is a published hash, because that can be revoked at machine speed. B then needs an irrevocable bond worth at least the remaining surplus (about 6).
  - That bond is tested on the equilibrium path: under the convergence procedure in §3, residents refuse 2% of the time at s = 0.1 and 8% at s = 0.3.
  - **What it does to "symmetric".** Cheap commitment is symmetric in availability, not in value. It is worth everything to the uninformed side that makes offers, and is a loss to the informed side. In the private-harm river, giving both sides agents shifts surplus toward the factory.

**Narrowing.** "If agents condition on their role, cheap observable commitment hands the pie to whichever side commits more cheaply or sooner. If agents play without regard to role (one population), and commitment binds imperfectly, the standoff probability rises toward q²." That is a different claim, and a distributional one.

**What would settle it.**
- Compare how often impasse occurs in large human bargains against small ones.
- Check whether deployed negotiating agents condition on their role.
- Measure how often principals redeploy an agent after publishing it.
- Run an experiment with two agent populations given cheap, escrowed commitment, with and without role labels.

---

## 3. Convergence claim

**Verdict: FAILS as stated.** B and C survive with narrowing, but only in an information regime the river does not have.

**Counter-arguments.**

- **No information regime fits.**
  - In the transparent river there is nothing to estimate.
  - In the private river each harm h_i is known only to resident i, who is paid to misreport it. That is the essay's own sentence, and sampling does not shrink such uncertainty.
  - σ/√c needs a third regime: harms are objective facts, measured with noise.

- **The rule the author uses is not the rule stated.** "Play the cell's equilibrium on the estimates" means certainty equivalence in B: offer exactly the estimated harm ĥ_i.
  - Each resident refuses that half the time, so under unanimity the deal closes 1/8 of the time.
  - The author's margin is instead a Bayesian best response. In D, "equilibrium" is not unique (B, C or mixed), so the rule is not defined there at all.

- **The margin formula (Q4).**
  - Notation: s = σ/√c_f is the factory's error (standard deviation) per harm; P̂ is its estimated pie; n = 3 under unanimity; Φ and φ are the standard normal distribution and density.
  - Offer: t_i = ĥ_i + s·x*, where x* solves P̂/s − n·x* = Φ(x*)/φ(x*).
  - For small s with P̂ = 6, x* ≈ √(2 ln(2.4/s)). So the margin is about (σ/√c)·√(2 ln(2.4√c/σ)), **not σ/√c**.
  - The multiplier is 2.5 at s = 0.1, 3.3 at s = 0.01, and 3.9 at s = 0.001.

- **Monotonicity: no.** A Monte Carlo run (harms (2,3,9), π = 20, flat prior, 400k draws) gives:

  | s | Deal closes | Residents' expected surplus (slices) | S given a deal | Total expected surplus |
  |---|---|---|---|---|
  | 5 | 0.6% | 0.01 | 0.35 | ~0.03 |
  | 1.5 | 34% | 1.07 | 0.53 | 2.0 |
  | 0.7 | 74% | 2.08 | 0.47 | 4.5 |
  | 0.3 | 92% | 1.61 | 0.29 | 5.5 |
  | 0.1 | 98% | 0.73 | 0.12 | 5.9 |
  | 0.01 | 99.85% | 0.10 | 0.017 | 6.0 |

  - The residents' surplus is **hump-shaped** in the factory's budget, while efficiency rises monotonically.
  - In B, factory compute raises efficiency, and only past the peak does it cut the residents' share. The essay reports only the second half.
  - At finite budgets B is not "efficient", and S is ambiguous whenever the deal fails.

- **Private harms put a floor under S.**
  - If each harm is a predictable part plus a private part with standard deviation τ, the factory's error is √(τ² + σ²/c), which falls to τ, not 0. S falls to a floor set by τ, not to 0. For τ = 0.3 slices: S given a deal ≈ 0.29, and the deal closes 92% of the time.
  - If harms are purely private, the same formula holds with s = τ, and S is flat in the factory's budget.

- **C is not B's mirror image.** Under unanimity C needs one estimate (of π) while B needs three acceptances. At s = 0.1, the factory's share in C is 0.042, against the residents' 0.124 in B.

- **D has no compute content.**
  - With r_i above 6, holding firm is optimal whatever a side believes about the other, so "misjudge and back down" cannot happen.
  - If compute lets a side see a commitment the other has already made (sequential moves), that side yields and the outcome is B or C. Compute *removes* standoffs.
  - If moves are simultaneous there is nothing to see. Modelling the error as noisy best response (logit quantal response, McKelvey & Palfrey 1995) [likely]: as the noise goes to 0 in symmetric Chicken, play converges to the mixed equilibrium. The standoff probability tends to (1 − c/3)², which is certain only if c = 0 exactly.

- **Cell A.** With private information at machine speed, A is governed by Coase and AG dynamics, not by errors "roughly cancelling" around 3/3.

**Narrowing.** "If harms are objective but costly to measure, then in the factory-commits cell, once the factory's error per harm is below about 0.7 of a slice, more factory compute raises the chance of a deal and pushes the residents' share toward zero, at rate (σ/√c)·√(2 ln c). An irreducible private component of harm stops it at a floor. Compute does nothing in the standoff cell."

**What would settle it.** The calculation above. The essay should state the information regime and the hump.

---

## 4. Claims outside my assignment that I believe are wrong

- **Cell A's S = 1/2.** Under k = n = 3, with residents not acting as one (as the table's column says), there are four veto players. The symmetric Nash bargaining solution and the Shapley value give 1.5 each [sure], as does the unanimity Baron–Ferejohn limit [likely]. That makes **S = 3/4**; the 3/3 split is a two-party result.
- **Cell C: "resident 3, who has the most to lose from no deal, breaks first".** At k = 3 no resident loses anything from no deal: the river stays clean, and any deal repays the harm. Each resident gains only its slice of the 6. This is k = 1 reasoning.
- **Cell C's internal split.** C also needs the residents to divide the 6 among three veto players. With cheap individual commitment, that is the unanimity case Miettinen & Vanberg find inefficient. A no-side-deals rule does not fix it; the rule must also fix the shares.
- **§4: "a union rule is cell C".** It makes the residents one player but does not stop the factory committing, so with the factory's agent the result is D or a race. The liability rule removes the veto altogether, which changes the entitlement; it is not a commitment assignment within the same game.
- **§6: "the only place the ratio of compute decides anything".** False wherever compute buys speed or cheapness of commitment:
  - Observable commitment makes D a race at k = 3 too.
  - Risk dominance compares c_N with c_f.
  - AG's weakness index is a ratio.
  - λ_N/(λ_f + λ_N) is Tullock's ratio contest [sure]. If speed is bought, with prizes 10 (factory) and 14 (residents), equilibrium spending totals V_f·V_N/(V_f + V_N) ≈ 5.8. That exceeds the 4 the clean river saves. Cheap compute changes the form of the waste, not its size. The formula is standard; applying it here is my own mapping.
- **§2: "Crawford's 1982 formulation".** Crawford's revocation costs are random, realised after commitment, and often private. A chosen, published bond is Schelling's third-party contract.
- **§5: "cheap compute does not choose the cell".** False if compute lowers a side's own commitment cost (risk dominance) or speeds its commitment (the race).

---

## 5. The single most damaging objection

The 2×2 table assigns outcomes to *capabilities*, but the game in which both sides can commit is not cell D: it contains B and C.
- In E–M's certain-commitment game, which is the model's own premise, any positive cost of committing makes the game Chicken. Its pure equilibria are "factory demands six, residents wait" (B) and the reverse (C).
- The standoff is only the symmetric mixed equilibrium, in which each side expects to gain exactly what committing costs it.
- E–M's unique-standoff theorem needs commitments that fail with probability 1 − q, and even then the standoff happens with probability q².

So who *can* commit does not choose the cell. Who commits *first*, or *more cheaply*, does.
- Risk dominance in the river selects the cheaper committer, and only the comparison c_N > c_f matters.
- One factory commits more cheaply than three residents who must first agree among themselves.
- So the model's own ingredients predict B: the deal closes, efficiently, on the factory's terms, with S = 0.

That turns the essay's efficiency claim ("agents produce standoffs; Krier's club fails to close") into a distributional one ("agents hand the pie to the cheapest committer"). The σ/√c compute channel plays no part in either.

The author's confirmation bias shows in three places:
- The prior red-team's paraphrase of E–M was adopted without checking it.
- The D-cell "misjudge and back down" story contradicts the cell's own r > pie premise.
- B's low-budget, fairer and less efficient region was left out.
