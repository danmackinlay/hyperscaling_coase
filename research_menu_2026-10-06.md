# A tasting menu for SKAS

*Drafted 2026-10-06 by Claude (Fable 5.1) at Dan's request. Status: proposals, not verdicts. Novelty claims were checked against arXiv/web on the day; "unploughed" means "I could not find it", not "it does not exist".*

## The andragogic thesis

Dan's diagnosis is that his proposals have been leaning on internalised machinery (Kolmogorov probability on dynamical systems, filtrations, causal graphs with interventions, counterfactuals) that cannot be transmitted without a concrete object to demonstrate it on. So the menu is built around **one shared concrete object** that several papers can rotate around, so that SKAS learns the machinery once and reuses it:

> **The killed Markov chain.** A finite state space, a transition matrix, one or more absorbing sets ("basins", "catastrophes", "disempowerment"), an exogenous input channel, and a coarse-graining map φ onto what an observer sees.

Everything SKAS has already written fits on it: his "decision point" is a state near a basin boundary; his "conservation law" is a viability set; his "selective sensitivity" is a ratio of two interventional derivatives; his "coarse-grained view φ(y)" is a σ-algebra; his master-equation/Turing–Ising triad (drift, self-interaction, diffusion) is the generator of the chain. The object is small enough to simulate in an afternoon, yet forces every concept Dan wants taught: harmonic functions, hitting times, spectral theory (Perron–Frobenius), filtrations and stopping times, Pearl interventions (do on the channel versus do on the state), lumpability, and regret bounds. Options A, B, D and E below all live on it; C and F add a causal-graph and a game-theoretic object respectively; G is the thermodynamic dessert.

The most important single fact I found while checking the drafts: **SKAS's "informed choice" is a time-localised version of Kolchinsky & Wolpert's "semantic information"** (information about the environment that is causally necessary for viability, measured by scrambling the environment→agent channel while holding the environment's own dynamics fixed). He should read that paper before writing another line, because it gives him the formalism he is groping for, and because the gap between it and his draft (the *when* of information, rather than the *how much*) is exactly Option A.

---

## Option A. Steerability windows: decision points as committors, and the selective-sensitivity ratio

**1. Research question.** For a stochastic process heading toward one of several absorbing outcomes, when, along a trajectory, does an external input channel have causal power over the outcome, as opposed to the system's own internal state? Define the *steerability* of a state as the ratio of the interventional sensitivity of the outcome to perturbations on the channel versus perturbations on the internal state, and show that it is a property of the committor function. Then measure it on LLM agent trajectories.

**2. Background and precedents.** The committor q(x) = P(hit basin A before basin B | start at x) is the central object of transition path theory (E & Vanden-Eijnden 2006; Metzner, Schütte & Vanden-Eijnden 2009). It is harmonic for the generator, so on a finite chain it is one linear solve. "Decision points" in SKAS's sense are the level set q ≈ ½ with large gradient, i.e. transition states. The LLM literature has independently rediscovered committor estimation by resampling: "forking tokens" (Bigelow et al. 2024), "critical decision points" (Macar, Bogdan et al. 2025, *Thought Branches*), "cliff tokens" (2026), "Forking Fast" (2026). All of these perturb only the model's own sampling, so they measure SKAS's η_x and never his η_y. Nobody has asked where along a trajectory *external* input (a user message, a monitor's intervention, a tool result) is causally decisive, which is the question an oversight regime actually needs answered. Ay & Polani's causal information flow and Dan's own repaired plasticity measure give the interventional (not observational) version of "sensitivity to channel". Kolchinsky & Wolpert's semantic information is the global version; this project localises it in time.

**3. Pros.** It is SKAS's own idea, so motivation is guaranteed, and it rescues it from the Lyapunov-exponent cul-de-sac (chaos is not choice; committors say why). The theory half is textbook Markov-chain mathematics that Dan can teach on a 20-state chain, and every step has a Pearl reading (intervening on the channel versus on the state) so causal graphs get taught on the same object. The empirical half is cheap: resample small open-weight models at each step with and without an injected external message and estimate both sensitivities; this is precisely the Bigelow/Macar protocol plus one extra arm. The safety payoff is legible: a *map of when oversight still works* for a given agent and task. Workshop-sized, with an obvious journal extension.

**4. Cons.** Committor estimation by resampling is expensive at scale and noisy near q ≈ ½, which is exactly where you care. The "ratio of sensitivities" needs a principled normalisation of perturbation sizes on two different spaces (tokens versus environment messages); the honest version is a comparison of two causal information flows, which drags in the estimation curse Dan already distrusts. The forking-token crowd is fast and could publish the "external input" arm any month. Also: a continuous-state version needs diffusion theory SKAS does not have yet; stay discrete.

**5. References.** E & Vanden-Eijnden (2006) *J. Stat. Phys.* 123; Metzner, Schütte & Vanden-Eijnden (2009) *Multiscale Model. Simul.* 7(3); Bigelow, Holtzman, Tanaka & Ullman (2024) arXiv:2412.07961; Macar, Bogdan et al. (2025) arXiv:2510.27484; "Cliff tokens" arXiv:2606.25524; "Forking Fast" arXiv:2608.19611; Ay & Polani (2008) *Adv. Complex Syst.* 11(1); Kolchinsky & Wolpert (2018) *Interface Focus* 8; Dan's `empowerment_plasticity.qmd` (directed-information repair); Baltieri et al. "Mathematical approaches to the study of agents" (OSF preprint, survey of the viability/semantic-information formalisms).

---

## Option B. Early-warning signals for gradual disempowerment: critical slowing down in the human share of control

**1. Research question.** Model gradual disempowerment as a Markov chain on the human share of control with an absorbing state at zero. Characterise its quasi-stationary distribution and the spectral gap, and ask whether the ecological early-warning indicators (rising variance, rising lag-1 autocorrelation, slower recovery from perturbation) appear before absorption becomes likely, and whether they are detectable through a coarse observer map φ.

**2. Background and precedents.** Kulveit et al. (2025) describe gradual disempowerment in prose and list "early warning indicators for concerning feedback loops" as desired future work. EleutherAI's "A Dynamical Model of AI Governability" (2026) builds a two-pool ODE (cooperative versus uncooperative AI labour) and states explicitly that it does not cover the regime where the uncooperative pool becomes a peer, and that an early-warning monitor is the goal. The ecology literature (Scheffer et al. 2009; Dakos et al. 2012) has a mature toolkit for exactly this: critical slowing down near a saddle-node, read off from the leading eigenvalue of the linearised dynamics. Quasi-stationary distributions of absorbing finite chains (Darroch & Seneta 1965; Collet, Martínez & San Martín 2013) are the probabilistic counterpart. A 2026 paper applies the Dakos indicators to collapse of online communities, so the transfer to socio-technical systems has a precedent but no AI-safety instance.

**3. Pros.** This is the richest teaching object on the menu: Perron–Frobenius, spectral gaps, Yaglom limits, the drift–diffusion (Fokker–Planck) picture SKAS already sketched in his Turing–Ising note, and the fluctuation–dissipation relation that makes critical slowing down work, which scratches his thermodynamics itch legitimately. It extends a live, well-received model (EleutherAI) into the regime its authors flagged as open. The deliverable is clear and policy-relevant: a list of statistics a monitoring regime should compute, with a theorem about when they are informative and a simulation showing lead time. The φ-coarse-graining question (can the observer see the slowing down?) connects directly to Option C.

**4. Cons.** Toy-model risk: an audience will ask why a birth–death chain on "share of control" is more than a metaphor, so the model needs at least one mechanism from the gradual-disempowerment story (e.g. substitution of human labour with rate depending on relative capability) rather than a bare random walk. Early-warning signals have known false-positive/false-negative pathologies (they need a slow driver and a saddle-node; other bifurcations give no warning), so the paper must be honest about which disempowerment dynamics have the right bifurcation. Econ-style readers may dismiss it as physics envy.

**5. References.** Kulveit et al. (2025) arXiv:2501.16946; EleutherAI blog, "A Dynamical Model of AI Governability" (2026); Scheffer et al. (2009) *Nature* 461; Dakos et al. (2012) *PLoS ONE* 7(7); Darroch & Seneta (1965) *J. Appl. Prob.* 2; Collet, Martínez & San Martín (2013) *Quasi-Stationary Distributions*, Springer; Méléard & Villemonais (2012) *Probab. Surveys* 9; Sheta (2026) arXiv:2604.13390 (critical-mass collapse in online communities); Dan's `ai_disempowerment.qmd` lock-in models section.

---

## Option C. Agent-relative agency: is being-an-agent monotone under observer coarse-graining?

**1. Research question.** Take the Kenton et al. mechanised-causal-graph definition of an agent (decision nodes whose mechanisms respond to utility mechanisms). Compose it with a causal abstraction map τ from a fine model to a coarse one. When does the abstracted model contain an agent if the fine one does, and vice versa? Is the agency verdict monotone in the refinement order of the observer's σ-algebra? Characterise the pathological directions.

**2. Background and precedents.** Dan's open question "agent-relative agency" asks whether agency can be defined by the extent to which *another* agent gains compression by adopting the intentional stance. Orseau, McGill & Legg (2018) give a relative definition of agency over Turing-machine descriptions. Abel et al. (2025) argue philosophically that agency is frame-dependent but offer no formal preservation result. Jørgensen et al. (2026, CLeaR) do the closest thing: causal games plus causal abstraction to decide when a *group* is a collective agent. What remains open is the single-system, observer-side question: fix one fine system, vary the observer's coarse-graining, and ask how the verdict moves. Dan already has the template result from the coalition work: partition refinement is non-monotone for the private core (Koutsougeras–Yannelis 1993); the same both-directions pathology is likely here, and showing it would be a clean theorem.

**3. Pros.** It is the most direct route to teaching causal graphs, interventions and abstraction (Rubenstein et al. 2017; Beckers & Halpern 2019) with no probability measure theory beyond finite tables. The result would speak to interpretability and oversight: a monitor that coarse-grains an AI system can both manufacture and erase apparent agency, which is a concrete, slightly alarming claim. It also lets SKAS's φ do real work.

**4. Cons.** Jørgensen et al. are close enough that the paper must be positioned carefully as the observer-relativity complement, and they may already have a lemma covering part of it. The Kenton definition is finicky (the mechanism-node machinery needs care), so there is a risk of spending the whole paper on definitions. Some readers regard "agency is relative" as already conceded.

**5. References.** Kenton et al. (2023) *Artificial Intelligence* 322:103963; Jørgensen et al. (2026) arXiv:2605.00248; Abel et al. (2025) arXiv:2502.04403; Orseau, McGill & Legg (2018) arXiv:1805.12387; Rubenstein et al. (2017) UAI; Beckers & Halpern (2019) AAAI; Koutsougeras & Yannelis (1993) *Econ. Theory* 3; Dan's `causality_mechanization_decisions.qmd`.

---

## Option D. Safe no-regret learning in games with absorbing catastrophic joint actions

**1. Research question.** In a repeated game where some *joint* action profiles are absorbing (the game ends badly for everyone), what regret guarantees are achievable by independent learners, and which learning rules (Hedge, UCB, Thompson sampling) reach the catastrophe with what probability? Is there a separation between "no regret conditional on survival" and "no regret including the catastrophe"?

**2. Background and precedents.** This was identified in the August scoping as a confirmed gap, and a recheck confirms it is still open. Plaut, Liévano-Karim, Zhu & Russell (2025/26, JMLR) prove sublinear regret with sublinear mentor queries for a *single* agent under irreversible dynamics; the multi-agent case, where the catastrophe is a joint action and no player can avoid it alone, is untouched. Safe-RL and conservative-bandit literatures treat single-agent constraints. The racing / brinkmanship stories in AI safety (Armstrong, Bostrom & Shulman 2016) are the motivating narrative.

**3. Pros.** It teaches the online-learning toolbox (concentration inequalities, potential-based regret proofs, Thompson sampling) that Dan wants to displace RL with in SKAS's intuitions, and it does so on the killed-chain object. A lower-bound result ("any algorithm with no-regret on survival paths hits the catastrophe with probability bounded below by …") would be a crisp workshop paper. Simulations are trivial. The safety reading is immediate: optimistic exploration in a shared dangerous world is collectively suicidal even when individually rational.

**4. Cons.** Regret proofs are unforgiving for a mathematically unlicked bear-whelp; the first few weeks will be slow. The result risks being a corollary of known safe-exploration bounds plus a union bound, which would make it contextually rather than classically unsolved. Game-theory reviewers may want equilibrium characterisation, not learning dynamics.

**5. References.** Plaut et al. (2025) arXiv:2502.14043; Cesa-Bianchi & Lugosi (2006) *Prediction, Learning, and Games*; Armstrong, Bostrom & Shulman (2016) *AI & Society* 31; conservative bandits (Wu et al. 2016, ICML); Dan's `online_learning.qmd` and the August scoping memory.

---

## Option E. When to pull the plug: shutdown as an inspection game over a drifting hidden capability

**1. Research question.** A principal observes a system's capability through a noisy, lagged channel; the capability drifts upward; the system may sandbag; shutting down is costly and irreversible. Formulate the shutdown decision as a stopping problem coupled to an inspection game, and characterise how detection lag and sandbagging incentive move the optimal stopping boundary. Is there a "window of preventive action" that closes before the evidence arrives?

**2. Background and precedents.** This is the composite model Dan favoured in August (Fearon/Powell commitment problem; cognitive capacity as detection-lag constant; sandbagging endogenous). The classical mathematics is quickest detection (Shiryaev 1963; Poor & Hadjiliadis 2009) and inspection games (Avenhaus, von Stengel & Zamir 2002), both forgotten by the AI-control literature. AI control (Greenblatt et al. 2023), "Auditing games for sandbagging" (2025) and "The Oversight Game" (ICML 2026) are static or one-shot; none have a drifting latent state with a timing decision. The off-switch game (Hadfield-Menell et al. 2017) is the one-period ancestor.

**3. Pros.** Teaches filtrations, stopping times, HMM filtering and sequential testing on the killed chain, which is exactly the "Kolmogorov-axiomatic probability on a dynamical system" Dan says he cannot transmit abstractly. It has a built-in theorem shape (a threshold policy exists; the threshold moves monotonically with lag; sandbagging shifts it the wrong way) and a built-in figure (the closing window). It talks directly to the AI-control crowd in their language.

**4. Cons.** Combining a stopping problem with a strategic opponent gets hard fast; the honest version is a stochastic game and may not admit a clean threshold result. The AI-control community moves quickly and someone may add drift to the auditing game soon. Dan has already circled this model once without landing it, which may mean the entry point was wrong rather than the model.

**5. References.** Powell (2006) *Int. Org.* 60; Fearon (1995) *Int. Org.* 49; Shiryaev (1963); Poor & Hadjiliadis (2009) *Quickest Detection*, CUP; Avenhaus, von Stengel & Zamir (2002) *Handbook of Game Theory* vol. 3 ch. 51; Hadfield-Menell et al. (2017) IJCAI; Greenblatt et al. (2023) arXiv:2312.06942; "Auditing games for sandbagging" arXiv:2512.07810; van der Weij et al. (2024) arXiv:2406.07358.

---

## Option F. Cooperation through uncertainty: does better mind-reading kill cooperation?

**1. Research question.** In a repeated game sustained by reputation under type uncertainty (Kreps–Milgrom–Roberts–Wilson), add a signal of the opponent's type with precision ρ, interpretable as interpretability or capability. Does the cooperative phase shrink monotonically in ρ? Is there a unifying statement with the Hirshleifer effect (information destroys insurance), such that the Cooperative-AI claim "transparency reduces cooperation failure" and the "ignorance is bliss" claim are two regimes of one model?

**2. Background and precedents.** KMRW (1982) and Kreps & Wilson (1982) show a small prior on a cooperative type sustains cooperation in finitely repeated play; Hirshleifer (1971) and Schlee (2001) show public information destroys risk-sharing. Dan's `cooperation_uncertainty.qmd` has the kin-recognition version. Hu et al. (2026, FAccT) argue LLM agents lack the persistent identity reputation needs. The Cooperative AI Foundation lists information asymmetry as a prime cause of cooperation failure. Nobody has put the two claims in one model with capability as the dial.

**3. Pros.** Pure Bayesian updating and extensive-form reasoning, so it teaches filtrations and conditioning without any dynamical-systems overhead; a natural second paper after one of A/B/E. The result is contextually unsolved (a corollary) but the framing is sharp and contrarian for the AI audience. Cheap to simulate; a figure of cooperation length versus ρ would carry it.

**4. Cons.** The economics is thoroughly ploughed and an econ reviewer will say "we knew that". The contribution is the mapping and the regime boundary, which is thin for a theory paper and may be better as a blog post. Least connected to the killed-chain spine.

**5. References.** Kreps, Milgrom, Roberts & Wilson (1982) *J. Econ. Theory* 27; Kreps & Wilson (1982) *J. Econ. Theory* 27; Hirshleifer (1971) *Amer. Econ. Rev.* 61; Schlee (2001) *Amer. Econ. Rev.* 91; Hu et al. (2026) arXiv:2605.30169; Dan's `cooperation_uncertainty.qmd`.

---

## Option G (dessert). The thermodynamic price of staying steerable

**1. Research question.** Still, Sivak, Bell & Crooks (2012) bound the dissipation of a driven system from below by its "nostalgia": information retained about the driving signal that is not predictive of the signal's future. An agent that remains correctable by a low-bandwidth principal must retain information about the principal's possible commands that is non-predictive of the environment. Does this yield a lower bound on the dissipation of corrigibility, and does the bound grow with the agent's capability (i.e. with how much of the environment it already predicts)?

**2. Background and precedents.** Thermodynamics of prediction (Still et al. 2012), Landauer, and England's dissipative adaptation (which SKAS already cites) are the physics; corrigibility (Soares et al. 2015) and the off-switch game are the safety side. Kolchinsky & Wolpert's semantic information is again adjacent. I found nothing joining them.

**3. Pros.** It is the paper SKAS most wants to write, and the physics is bipartite-Markov-chain information theory he can learn on the same finite objects. A clean inequality would be striking and quotable.

**4. Cons.** High risk of a result that is either trivial (nostalgia bound restated) or physically meaningless (the "agent" is not a thermodynamic system with a bath, so dissipation is a metaphor). Dan is least qualified to supervise here, by his own account. Physicists will police the thermodynamics hard. Treat as a side project to be pursued only after a win elsewhere.

**5. References.** Still, Sivak, Bell & Crooks (2012) *Phys. Rev. Lett.* 109, 120604; England (2015) *Nat. Nanotechnol.* 10; Kolchinsky & Wolpert (2018) *Interface Focus* 8; Soares, Fallenstein, Yudkowsky & Armstrong (2015) AAAI workshop; Hadfield-Menell et al. (2017) IJCAI.

---

## The incumbent, re-plated: coalition stability under drifting weight and unequal filtrations

Briefly, since it is already scoped in August. The reason proposals here may have fallen short is the entry point: differential-information cores (Wilson, Vohra, Forges–Mertens–Vohra) are a notoriously fiddly literature to learn *as a first contact with σ-algebras*. If Dan still wants this target, the andragogic fix is to reach it *through* Option E: the drifting-capability-with-lag object is a two-player version of the same model, and once SKAS has filtrations and stopping times from E, the three-player weighted-voting game with unequal filtrations is one more player rather than a new universe. The theorem-backed punchlines from August (incentive constraints, not asymmetry, kill the core; refinement is dual-use; pooling destroys the informational insurance) remain the right destination.

---

## My recommendation

Lead with **A**, because it is SKAS's own idea made rigorous, the mathematics is the gentlest on-ramp to everything Dan wants taught, and the empirical arm is cheap and currently unoccupied. Run **B** in parallel as the "big model" paper, since it uses the same chain with a spectral rather than harmonic lens, and together A and B cover harmonic functions, hitting times, spectra and quasi-stationarity, which is most of a first course in Markov chains. Hold **E** as the third paper, because it inherits the object and teaches filtrations and stopping times, and it is the bridge back to the coalition target. **C** is the right paper if Dan wants causal graphs taught first rather than probability first. **D** is a strong fallback with a known gap but the steepest proof curve. **F** and **G** are side dishes.

## Questions that would sharpen round two

1. Theory-first or empirics-first for the workshop paper? A and B both have simulation arms; A has an LLM arm. Which audience is the target (NeurIPS-workshop-style with a figure from a real model, or a modelling venue)?
2. How much time does SKAS have per week, and for how many months? Options A and B are ~3 months; D and E are longer.
3. Does Dan want to teach probability first (A, B, E) or causal graphs first (C)? The spine changes accordingly.
4. Is the coalition target still live, or may it be retired in favour of E as the "commitment problem" paper?
