*A literature read by an AI research agent; sources and reading depth are listed at the end.*

# Do rules remove the computational advantage, and at what price?

A rule "removes the computational advantage" if a party's share does not depend on how much computation it or its opponent has. It "keeps the computational benefit" if more computation still enlarges the total. The street is one delivery company and three neighbours choosing which night slots run.

## Answer to A

Yes, under assumptions the street does not obviously meet. It is proved that under a truthful rule (reporting your true valuation is best whatever the others do) a party gains nothing by modelling its opponents, provided valuations are private, known to their holders at no cost, utility is linear in money, nobody colludes, each person has one identity, and the operator is committed to the rule. Drop "known at no cost" and it is proved that even the best-known truthful rule rewards learning about opponents, and that the only rules immune to this are those in which reports do not interact, such as posted prices. Drop private values and, generically, no non-trivial rule of this robust kind exists. It is my conjecture, not a theorem, that the residual modelling of opponents under a truthful rule is aligned with the total. Whether any rule protects a weaker party when the stronger one also chooses the rule is unknown; the one model I found says the rule-chooser takes nearly everything from a naive learner.

## Answer to B

The rules that remove the advantage most completely (posted prices, ascending clocks) keep least of the benefit, and the rule that keeps the benefit best (Vickrey–Clarke–Groves, VCG) cannot balance its payments. It is proved that VCG with private values makes each party's private return to computing its own value equal the social return, that this needs exact welfare maximization, that it is incompatible with balanced payments, and that no efficient auction rule resists false identities. It is also proved that part of the price disappears with randomization or when the parties' interests are substitutes. Unknown: the size of the losses at four parties, and whether language-model agents behave as the theorems assume. I found no experiment that varies capability asymmetry across bargaining and auction rules in one environment.

## 1. Truthful rules and their assumptions

A rule is truthful (also dominant-strategy incentive compatible, or strategy-proof) when honest reporting is optimal against every possible report of the others. VCG picks the outcome that maximizes the sum of reported values and charges each party an amount depending only on the others' reports. Truthfulness is proved for quasi-linear utility (value minus money) and private values (my valuation depends only on my own information). With unrestricted valuations over three or more outcomes, Roberts's theorem says the only truthful rules are weighted variants of VCG (Nisan 2007). Under VCG a party's payoff is the total minus a term it cannot influence, so better estimates of the others buy nothing. Li (2017) lists this as a standard virtue: "spying on other players yields no strategic advantage".

Two results qualify that sentence. Larson and Sandholm (2001) let bidders pay to compute their own valuations; the Vickrey auction then has no dominant strategy, and when the returns to computing are uncertain, bidders may in equilibrium compute on their opponents' valuation problems. Gleyze and Pernoud (2023) let agents buy information about their own and others' preferences. For generic preferences and a broad class of cost functions, agents have no incentive to learn about others if and only if the rule is in effect separable, meaning reports do not interact in determining the outcome. VCG and every standard auction fail; a sequence of posted prices passes. The neighbours do not know what a schedule costs them until they work it out, so this is the street's case. In what I read, the modelling buys better-directed effort on one's own valuation, not a larger slice of a fixed total.

A strategy is obviously dominant if, wherever it first departs from a deviation, its worst outcome is at least as good as the deviation's best (Li 2017). Li proves that such rules are exactly those an operator can run when each agent can check only its own dealings with the operator. For yes/no decisions, including a binary public good, every obviously strategy-proof rule is essentially a generalized ascending clock; the sealed second-price auction is not one. Akbarpour and Li (2020) add that a sealed second-price operator can profit by inventing a higher losing bid, and that among optimal auctions with independent private values no rule is at once sealed, strategy-proof and credible (immune to operator deviations no bidder can detect). On the street, if the company or its platform operates the rule, a sealed truthful rule does not protect the neighbours, and the rules that do are clocks and posted prices. I found no characterization for choices among many schedules.

## 2. What computation still buys under truthful rules

Bergemann and Välimäki (2002) let each agent covertly buy information about its own payoff before the rule runs. With independent private values, every local social optimum of the agents' information choices is an equilibrium under VCG (their Theorem 1). The limits are theirs: "local" means each agent's choice is optimal given the others', so there can be several equilibria; no balanced-budget or participation constraint is imposed; and with interdependent values (my valuation depends on your information) efficient rules in general produce too much or too little acquisition.

Akbarpour et al. (2023) show that the alignment survives only if the rule exactly maximizes welfare over some fixed set of outcomes. An algorithm that is arbitrarily close to optimal can do arbitrarily badly once one party can invest beforehand. Nisan and Ronen (2007) show that replacing the optimum with a heuristic breaks truthfulness for essentially all reasonable heuristics, and that the only motive to misreport is then to help the algorithm. Their second-chance mechanism lets each party submit a program proposing a better input, and takes the best result. That is the nearest published rule to the street's joint search that lifts the total from 6 to 7.5: the company's stronger search enters as a proposal and raises the total. The alignment works because each party is paid as if it owned the whole total, which is why the payments cannot balance.

## 3. The cost for public decisions

Papadimitriou, Schapira and Singer (2008) study choosing k of m resources to maximize the sum of valuations with diminishing returns, which is the form of the night-slot choice. A non-truthful greedy algorithm gets within a constant factor of the optimum; no truthful polynomial-time algorithm does better than a factor of √m, even with two agents. One version bounds communication for general valuations; the other assumes NP is not contained in BPP for compactly described ones. The bound is asymptotic in m. Exact VCG is truthful and costs about 2^m evaluations, trivial for a street's slots, so this barrier is one that cheap computation removes. Dughmi (2011) also gives a randomized rule, truthful for risk-neutral agents, that matches the best non-truthful ratio for a natural class of valuations.

The binding costs are elsewhere. Green and Laffont's theorem, as stated by Nath and Sandholm (2016), is that a truthful and efficient rule cannot have payments summing to zero. Nath and Sandholm prove that a deterministic truthful rule with balanced payments must ignore one agent's valuation entirely; the loss vanishes with many agents, and the street has four. Myerson and Satterthwaite (1983) prove for one buyer and one seller with independent private values and overlapping ranges that no rule is voluntary, balanced, efficient, and truthful on average given beliefs. Hagerty and Rogerson (1987), read second-hand, show that the truthful, balanced, voluntary rules for two parties are posted prices. So the self-financing rule that fully removes the advantage is a posted price per slot, which trades only when the price happens to separate the values and cannot search.

Yokoo, Sakurai and Matsubara (2004) prove that VCG is not robust to one bidder using several identities and that no efficient combinatorial auction is. Ausubel and Milgrom show for auctions that collusion by losers and multiple identities are unprofitable under VCG exactly when every bidder treats the goods as substitutes. Che and Kim (2006) show that collusion by all agents can often be neutralized at no cost, but not subgroup collusion with correlated types. These are private-goods results; I did not find the public-project analogue. Three neighbours are a natural coalition and agents make identities cheap.

Jehiel et al. (2006) prove that with interdependent values and multidimensional information, generically the only deterministic rules implementable ex post (honesty optimal whatever the others' information turns out to be) are constant. If the company's inference tells it more about a neighbour's harm than the neighbour knows, the street is in this case.

## 4. Protection that rests on hardness

Bartholdi, Tovey and Trick (1989) exhibited a voting rule for which finding a profitable misreport is NP-complete. Friedgut, Kalai and Nisan (2008) proved for three alternatives, and Isaksson, Kindler and Mossel (2012) and Mossel and Rácz (2015) for more, that under any rule far from every non-manipulable one a random misreport by a random voter succeeds with probability at least inversely polynomial in the numbers of voters and alternatives. These hold for uniformly random preference profiles. Faliszewski and Procaccia's survey concludes that no rule is known to be usually hard to manipulate, and that structured preferences remain open. So the proposed sentence is fair for worst-case hardness, which fails even against trivial computation, and no rule for the street should count on the company being unable to find a profitable misreport. It is too broad as written: cryptographic commitments rest on average-case hardness by construction, and Canetti, Fiat and Gonczarowski build on them a way for a designer to commit to a rule and prove it truthful without revealing it.

## 5. Designing the rule

Conitzer and Sandholm (2002) prove that choosing the best truthful rule from explicit lists of types and outcomes, without payments, is NP-complete for deterministic rules and solvable by linear programming for randomized ones. The design hardness is therefore a worst case that randomization removes. Cai, Daskalakis and Weinberg (2013) reduce design to the underlying optimization problem when a common prior is known. I found no theorem comparing the difficulty of choosing a rule with that of playing under one. The nearest contrast is that play under a truthful rule is trivial, while computing equilibrium bids in a first-price auction is PPAD-complete (Filos-Ratsikas et al. 2021). Truthful design moves the computation from the players to the rule, and at the street's size neither is hard.

## 6. Learning agents

Braverman et al. (2018) study a seller who chooses the auction each round against a buyer running a no-regret algorithm (one that does as well in hindsight as its best fixed bid). Against the common mean-based algorithms the seller extracts nearly the whole surplus; against a particular algorithm the seller can do no better than a fixed reserve price. Deng, Schneider and Sivan (2019) show for general repeated games that under mild assumptions an optimizer can always secure its Stackelberg value (the payoff from committing first) against any no-regret learner, and no more than that against a learner with no swap regret (a stronger guarantee). A neighbour's agent that merely learns from repeated rounds is exposed unless its algorithm has that stronger property. Here the protection is a property of the weaker party's algorithm, not of the rule, and its floor already hands the stronger party the first-mover payoff. Syrgkanis and Tardos (2013) guarantee a fraction of the optimal total under no-regret play in smooth mechanisms, and say nothing about shares. Kolumbus and Nisan (2022) report that when users delegate to learning agents, the second-price auction stops being truthful for the users.

## 7. Proofs as a rule

Rational proofs (Azar and Micali 2012, read through Guo et al.) have the verifier pay the prover a randomized reward that is maximized by the true answer. They cover counting problems in one round with a very weak verifier. They assume the prover has no stake in the answer beyond the reward, which a bargaining company does. I found no paper applying interactive proofs to bargaining; the zero-knowledge construction in section 4 is the closest.

## 8. Experiments with language-model agents

Zhu et al. (2025) run open bargaining between buyer and seller agents across nine models: more capable models get better prices in both roles. Hoshino et al. (2026) find that centralized matching rules outperform free negotiation among agents, though truthful reporting does not track formal strategy-proofness uniformly. Neither varies capability across rule types.

## What cuts against the thesis

Only separable rules remove the incentive to model opponents once valuations must be computed. Truthful, efficient rules cannot balance payments or resist false identities, and with interdependent values they do not exist. A stronger party facing a learner gets at least the first-mover payoff under any rule, and nearly everything if it chooses the rule. An operator can cheat a sealed truthful rule. Approximate optimization breaks the alignment of investment. In favour of free protection: VCG with private values, randomized truthful rules, collusion-proofing for the whole group, and the substitutes condition.

## Where the red-team notes were wrong or imprecise

The Persico citation does not support "bargaining induces rent-seeking acquisition". On the snippet and a second-hand description, Persico compares first-price and second-price auctions with affiliated values and finds stronger incentives to acquire information in the first-price auction. The Bergemann–Välimäki claim holds only for independent private values, as a local optimum, with no budget or participation constraint.

The notes file the Papadimitriou–Schapira–Singer bound among the strategic costs that a lower price of computation leaves untouched. It is a conflict between truthfulness and polynomial time, and exact VCG escapes it at small m.

"Manipulation is easy on every natural distribution" overstates results proved for uniform profiles.

"Automated mechanism design is NP-hard" holds for deterministic rules without payments in an explicit representation.

Finding 6 (ex ante rule-making escapes Myerson–Satterthwaite) relies on the expected-externality mechanism, which I did not check. From memory it is truthful only on average given beliefs, so beliefs about opponents, and computation on them, matter again.

## Sources and how I read them

- Akbarpour, Kominers, Li, Li, Milgrom (2023), "Algorithmic Mechanism Design with Investment", *Econometrica*. https://web.stanford.edu/~mohamwad/InvestmentIncentives.pdf — read introduction.
- Akbarpour, Li (2020), "Credible Auctions: A Trilemma", *Econometrica*. https://web.stanford.edu/~mohamwad/Credible.pdf — read main theorem.
- Ausubel, Milgrom (2006), "The Lovely but Lonely Vickrey Auction". https://milgrom.people.stanford.edu/wp-content/uploads/2005/12/Lovely-but-Lonely-Vickrey-Auction-072404a.pdf — read main theorem (Theorem 10).
- Azar, Micali (2012), "Rational Proofs", STOC — via Guo, Hubáček, Rosen, Vald, "Rational Arguments". https://www.alonrosen.net/PAPERS/rationalproofs/full.pdf — second-hand; original not opened.
- Bartholdi, Tovey, Trick (1989), "The Computational Difficulty of Manipulating an Election", *Social Choice and Welfare*. https://link.springer.com/article/10.1007/BF00295861 — abstract only.
- Bergemann, Välimäki (2002), "Information Acquisition and Efficient Mechanism Design", *Econometrica*. http://www.dii.uchile.cl/~nicolasf/BergemannValimaki.pdf — read main theorem.
- Braverman, Mao, Schneider, Weinberg (2018), "Selling to a No-Regret Buyer". https://arxiv.org/abs/1711.09176 — read main theorem.
- Buchfuhrer, Schapira, Singer (2010), "Computation and Incentives in Combinatorial Public Projects", EC. https://www.cs.yale.edu/homes/schapira/ec075-buchfuhrer.pdf — read introduction.
- Cai, Daskalakis, Weinberg (2013), "Understanding Incentives: Mechanism Design becomes Algorithm Design". https://arxiv.org/abs/1305.4002 — read introduction.
- Canetti, Fiat, Gonczarowski (2023–26), "Mechanism Design Without Disclosure". https://arxiv.org/abs/2302.05590 — read introduction.
- Che, Kim (2006), "Robustly Collusion-Proof Implementation", *Econometrica*. https://emu-perch-bjgm.squarespace.com/s/RCP.pdf — read introduction.
- Conitzer, Sandholm (2002), "Complexity of Mechanism Design", UAI. https://arxiv.org/abs/cs/0205075 — read main theorem.
- Conitzer, Sandholm (2006), "Nonexistence of Voting Rules That Are Usually Hard to Manipulate", AAAI. http://www.cs.cmu.edu/~sandholm/nonexistence.aaai06.pdf — read introduction; not relied on beyond the survey.
- Deng, Schneider, Sivan (2019), "Strategizing against No-regret Learners", NeurIPS. https://arxiv.org/abs/1909.13861 — read main theorem.
- Dughmi (2011), "A Truthful Randomized Mechanism for Combinatorial Public Projects via Convex Optimization", EC. https://arxiv.org/abs/1103.0041 — read main theorem.
- Faliszewski, Procaccia (2010), "AI's War on Manipulation: Are We Winning?", *AI Magazine*. https://procaccia.info/wp-content/uploads/2020/03/manipulation.pdf — read in full where relevant.
- Filos-Ratsikas, Giannakopoulos, Hollender, Lazos, Poças (2021), "On the Complexity of Equilibrium Computation in First-Price Auctions". https://arxiv.org/abs/2103.03238 — read introduction.
- Friedgut, Kalai, Nisan (2008), "Elections Can be Manipulated Often", FOCS. https://www.rangevoting.org/mani-focs.pdf — read main theorem.
- Gleyze, Pernoud (2023), "Informationally Simple Incentives", *Journal of Political Economy*. http://agathepernoud.com/Gleyze_Pernoud_ISI.pdf — read main theorem.
- Green, Laffont (1977/1979), budget-balance impossibility — via Nath, Sandholm (2016), "Efficiency and Budget Balance", WINE, https://www.cs.cmu.edu/~sandholm/efficiencyAndBudgetBalance.wine16.pdf (read introduction); original not opened.
- Hagerty, Rogerson (1987), "Robust Trading Mechanisms", *Journal of Economic Theory* — via https://arxiv.org/abs/2212.14367; second-hand, original not opened.
- Hoshino, Kitadai, Nishino (2026), "Do Matching Mechanisms Work with LLM Agents?". https://arxiv.org/abs/2606.03030 — read abstract and discussion.
- Isaksson, Kindler, Mossel (2012), "The Geometry of Manipulation", *Combinatorica*. https://arxiv.org/abs/0911.0517 — read main theorem.
- Jehiel, Meyer-ter-Vehn, Moldovanu, Zame (2006), "The Limits of Ex Post Implementation", *Econometrica*. http://www.cs.cmu.edu/~./sandholm/cs15-892F15/limits%20of%20ex%20post%20implementation.pdf — read introduction.
- Kolumbus, Nisan (2022), "How and Why to Manipulate Your Own Agent". https://arxiv.org/abs/2112.07640 — read introduction; the auction result is in a companion paper not opened.
- Larson, Sandholm (2001), "Costly Valuation Computation in Auctions", TARK. https://www.cs.cmu.edu/~sandholm/tark01.pdf — read main theorems (proofs omitted in the source).
- Li (2017), "Obviously Strategy-Proof Mechanisms", *American Economic Review*. https://mpra.ub.uni-muenchen.de/78930/1/MPRA_paper_78930.pdf — read introduction.
- Mossel, Rácz (2015), "A Quantitative Gibbard–Satterthwaite Theorem without Neutrality", *Combinatorica*. https://arxiv.org/abs/1110.5888 — read main theorem.
- Myerson, Satterthwaite (1983), "Efficient Mechanisms for Bilateral Trading", *Journal of Economic Theory* — via lecture notes, https://www.asc.ohio-state.edu/peck.33/gametheory/gameL11.pdf; second-hand.
- Nisan (2007), "Introduction to Mechanism Design (for Computer Scientists)", in *Algorithmic Game Theory*. https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf — read the relevant theorems.
- Nisan, Ronen (2007), "Computationally Feasible VCG Mechanisms", *JAIR*. https://arxiv.org/abs/1110.0025 — read introduction and mechanism definition.
- Papadimitriou, Schapira, Singer (2008), "On the Hardness of Being Truthful", FOCS. https://www.cs.yale.edu/homes/schapira/cppp.pdf — read main theorem.
- Persico (2000), "Information Acquisition in Auctions", *Econometrica*. https://www.jstor.org/stable/2999478 — snippet only, plus the description in Compte and Jehiel (2007), https://philippe-jehiel.enpc.fr/wp-content/uploads/sites/2/2018/03/ascendRand.pdf.
- Syrgkanis, Tardos (2013), "Composable and Efficient Mechanisms", STOC. https://arxiv.org/abs/1211.1325 — read main theorem.
- Yokoo, Sakurai, Matsubara (2004), "The Effect of False-name Bids in Combinatorial Auctions", *Games and Economic Behavior*. https://courses.cs.duke.edu/fall06/cps296.2/yokoo_geb.pdf — read main theorem.
- Zhu et al. (2025), "The Automated but Risky Game". https://arxiv.org/abs/2506.00073 — read introduction and results.
- From memory, not checked: Roberts (1979) in the original; d'Aspremont and Gérard-Varet (1979); the sum-check protocol of Lund, Fortnow, Karloff and Nisan (1990).
