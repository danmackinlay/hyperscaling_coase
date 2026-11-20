Cold read of /Users/dan/Source/livingthing/_plans/hyperscaling_coase_constitutional_complexity_3.qmd (721 lines). I read the whole file twice and no other file. I made no edits.

# 1. Nerdview

- **L2.** "selfish delegated agent constitutional negotiation still need a benevolent leviathan". The title is ungrammatical: the subject is singular and the verb is "need". It also stacks five nouns that the reader cannot parse until L101 and L113. Fix: "Why bargaining by self-interested AI agents over the rules still needs a benevolent leviathan", or "Information and computation costs mean AI agents bargaining for their principals still need a benevolent sovereign".
- **L5.** "Séb Krier", "Coasean bargaining", "framework guarantor". Nobody here is introduced. Coase is explained only at L17, and "framework guarantor" is Krier's phrase, glossed only at L76. Fix: "Séb Krier (Cosmos Institute) argues that AI agents will make bargaining cheap enough that private deals, in the manner of Coase's theorem, replace most regulation…"
- **L7.** "expected loss relative to first-best welfare". "First best" is jargon and is defined only at L98. Fix: "relative to the best outcome achievable if everyone's preferences were public".
- **L18.** Krier is never described: who he is, or why his essay matters. Add one clause.
- **L32.** "Hobbes's sovereign" assumes the reader knows Leviathan (1651). There is no citation and no gloss. Fix: "Hobbes's Leviathan, the sovereign whose power to compel is what makes agreements hold".
- **L47.** It is unclear whose words "cannot possess the dispersed, specific knowledge of time and place" are, Hayek's or Krier's paraphrase. See §2.
- **L54.** "Nash deadlock" is presented as "what economists would call" it. Economists do not use the term, and a newcomer will take it as standard. "Correlated equilibrium" is not defined until L395, with no forward pointer. Fix: add "(Krier's phrase; correlated equilibrium is defined below)".
- **L64.** "a Harberger-style tax" is not explained until L513. Gloss it at first use: "a tax on the value you declare for an asset, with an obligation to sell to anyone who offers that value".
- **L70.** "wealth effects and the endowment effect" are not glossed. A statistician will not know either. Fix: "wealth effects (how much you will pay depends on how rich you are, so who holds a right changes the efficient outcome) and the endowment effect (people demand more to give up a thing than they would pay to get it)".
- **L94.** "common knowledge" is not glossed. Fix: "known to all, with everyone knowing that everyone knows it".
- **L108.** The definition of incentive compatibility omits "in expectation over the others' types". L280 later says the expected-externality mechanism is "incentive compatible in expectation", which reads as a weaker property than the one defined. Fix: "no agent expects to gain, averaging over the others' types, by misreporting…", and name the two notions Bayesian and dominant-strategy.
- **L118, L122.** "$L_{\text{comp}}(c,\kappa; m, N, k)$" and "depends on $c$ and $\kappa$ only through how fast the problem's size grows against them". The phrase is opaque. Fix: "for a fixed budget, the largest problem that can be solved grows only logarithmically as $c$ and $\kappa$ fall, while the problem posed grows exponentially in $k$".
- **L147.** "$r$ | returns to relative effort". "Returns" is jargon. Fix: "decisiveness: how steeply share responds to relative spending". The symbol also clashes with other uses; see §2.
- **L155.** "private goods in thick markets" is jargon. "Thick" is glossed only implicitly at L207, and "private good" never. Fix: "goods one person consumes to the exclusion of others, in markets with many buyers and sellers".
- **L171.** "the linear equilibrium of the double auction studied by Chatterjee and Samuelson". "Double auction" is not glossed. Fix: "(each side names a price and trade happens at the midpoint if the bid exceeds the ask)", or cut the parenthetical.
- **L177.** "The Vickrey–Clarke–Groves mechanism". It is named by its bilateral instance only, and the general rule is never stated, although L282 and L375 generalise from it. Fix: "in which each party is paid the total value its participation adds for the others (here: the truck pays the reported $s$…)".
- **L184.** "under conditions they describe as very mild". L41 promises that every theorem is cited with its conditions, and the conditions here are never stated. Fix: state them (independent private values, quasi-linear utility, per-capita cost bounded away from the support's extremes, and so on), or drop the L41 promise.
- **L199.** "under complete information" is not glossed. Fix: "(everyone's values known to everyone)".
- **L200.** "a form of coercion restores efficiency" is vague. Fix: name it, e.g. "making participation compulsory".
- **L201.** "every consistent equilibrium" uses a technical refinement without explanation. Fix: gloss it or drop "consistent".
- **L210.** "rival, excludable goods". Fix: "goods where one person's use prevents another's and non-payers can be shut out".
- **L234.** "on sufficiently rich preference domains" and "Groves mechanisms". Neither is defined, and the relation to VCG is never stated. Fix: "Groves mechanisms (the family VCG belongs to: each agent is paid the others' reported values at the chosen outcome, plus a term its own report cannot affect)". Gloss "rich domain" as "when preferences can be anything within a broad class".
- **L238.** "compulsory purchase" is a British legal term. Fix: add "(eminent domain)".
- **L247.** "Cournot's (1838) problem of complementary monopolies" is a label standing in for an explanation. Fix: "Cournot's problem of complementary monopolies: when a buyer needs one input from each of several sellers, each seller's markup raises the price the others face, so the total markup exceeds what a single seller would charge".
- **L268.** "an airshed" is jargon. Fix: "the air over a region".
- **L274.** "the victim's production set is non-convex in (output, rights held), because the victim can always shut down and so bounds its own loss". A non-economist cannot follow why shutting down implies non-convexity, nor why non-convexity kills competitive equilibrium. Fix: one sentence each. As pollution rises, the victim's loss stops rising once it shuts down, so its demand for clean air is not smooth. Market-clearing prices exist only when such sets are convex.
- **L280.** "The expected-externality mechanism" is named and described in a single compressed clause. Fix: "each agent receives the expected effect of its report on the others' values, financed by charging the others equal shares, so payments sum to zero".
- **L283.** "a team needs an outside budget-breaker". Holmström (1982) is about hidden effort, not private types, and the analogy is not explained. Fix: explain it, or cut.
- **L294.** "which is the Myerson–Satterthwaite case" is a label for an argument. Fix: "with two partners and one owning everything, this is the seller–buyer problem of the truck example, where no such mechanism exists".
- **L295.** "shared or probabilistic rights" is not explained. Fix: give an example, such as a right that each party holds with probability ½, or joint ownership with a buy-sell clause.
- **L312.** "in Blackwell's sense", "garbling". The concept is not cited, and "garbling" is jargon. Fix: "$s_i$ is a noisy function of $s_i'$".
- **L325.** "generically achievable" is jargon. Fix: "achievable for all but a negligible set of joint distributions".
- **L343.** "The bound is on nondeterministic communication". Fix: "the bound holds even for a protocol that is handed the answer and only has to check it". "The size of any price system that supports it" uses "supports" undefined. Fix: "prices at which every agent prefers its assigned bundle to any other".
- **L368.** "combinatorial bids" is not glossed. Fix: "bids on bundles of items". "NP-hard in the number of bids" is odd phrasing.
- **L369.** "Håstad 1999, derandomized by Zuckerman 2007" is pure insider material. It also never explains why Håstad's $n^{1-\epsilon}$ (as in the reference title) becomes $m^{1/2-\epsilon}$. Fix: cut the parenthetical.
- **L376.** "an algorithm that may trust the reports" and "cannot do better than a factor $m^{1/2-\epsilon}$". The direction of "factor" is unclear. Fix: "cannot guarantee more than a fraction $m^{-(1/2-\epsilon)}$ of optimal welfare".
- **L389, L396.** "compactly represented games" and "large games with compact descriptions" are not glossed. Fix: "games described by a formula whose size grows polynomially with the players, not by a full payoff table".
- **L397.** "PPAD-complete" is not glossed, and the sentence adds nothing to the argument. Fix: cut it, or "belongs to a class of problems believed to have no efficient algorithm".
- **L405.** "the optimal deterministic mechanism": optimal for what objective? The two-sentence subsection never says why it matters to the argument. Fix: state the objective and add "so the designer the earlier remedies need faces a hard problem too", or cut.
- **L433, L440, L468.** "cognition", "computation", "inference budget" (L461) are used interchangeably. Fix: pick "computation" and use it throughout.
- **L489.** "continuous liquid democracy" and "delegation rules using only local information" are not glossed. Fix: "liquid democracy, in which each voter may hand her vote to a delegate who may pass it on". "Local information" means a voter knows only her neighbours' competence.
- **L535.** "The agent platforms in Krier's second layer of governance" introduces a layer and platforms the summary never mentions. Fix: describe them in the L45–78 summary.
- **L553.** "Thick two-sided markets". "Two-sided market" is a term of art for platform markets. Fix: "thick markets with many buyers and many sellers".
- **L591.** "with multidimensional signals" is not glossed. Fix: "when each party's private information has more than one dimension".
- **L598.** "Folk theorems" are neither glossed nor cited. Fix: "Folk theorems (results that almost any feasible payoff can be sustained in infinitely repeated games with patient players)", plus a citation.

# 2. Undefined or dangling references, citations, notation

## Citations, checked mechanically

- Every author–year cited in the text is in the reference list.
- Every reference-list entry is cited somewhere in the text.
- Names used without any reference: Hobbes (L32), Blackwell (L312), Harberger (L64; only Posner and Weyl are cited, at L513), and folk theorems (L598, unattributed).

## Quotations with unclear source

- **L47.** "cannot possess the dispersed, specific knowledge of time and place". The sentence opens "Krier's starting point is Hayek (1945)", so the quote could be Hayek or Krier. Fix: "In Krier's words, a planner…", or give Hayek's page.
- **L49.** "What costs $10,000 in legal fees today…" has no attribution in the sentence. Fix: "He writes, …"
- **L73.** "The sovereign can always renege" could be Krier's words or Acemoglu's. Fix: say which.
- **L418, L461, L489, L515, L535, L558, L567.** These sentences rely on parts of Krier that the summary at L45–78 never presents:
  - "a near-instantaneous computational verification" (L418)
  - "a billionaire's phone is no better" (L461)
  - "the continuous liquid democracy Krier proposes" (L489)
  - "verified emergencies" at zero price (L515)
  - the "second layer of governance" (L535)
  - "Krier's own starting cases, the office thermostat, shared resources in an apartment block, the division of household chores" (L558; L56 had said four examples "carry the essay")
  - "automated governance" (L567)

  Fix: add each to the summary section, or attribute it at the point of use ("Krier also proposes…").

## Pointers

- **L30.** "bargaining over them is the same problem posed one level up". This is a forward claim with no pointer; it is argued only at L495–500. Fix: add "(see 'The regress and what stops it')".
- **L65.** "Any coalition that vetoes must then reimburse that quantified loss". "That" has no antecedent, and the following clause, "with agents representing the diffuse public who would gain", is hard to parse. Fix: "Any coalition that blocks a project must reimburse the loss to those who would have gained, a loss quantified by agents representing that diffuse public."
- **L86.** "My disagreement is confined to that last step." The previous paragraph has several steps, and it is unclear whether "last" means "the residual state need not know preferences" (L83) or "the leftover problems are engineering problems" (L82). L87–89 attacks both. Fix: name the step.
- **L237.** "the expected-externality mechanism described below" resolves to L280. That mechanism does not pay "every member the same $p$", which is the rule just described. See §3.
- **L241 and L391** ("I return to this below") resolve correctly, to L304 and L472.

## Notation

- **$r$ has three meanings.** It is members' reports $r_i$ (L218), partners' shares $r_1,\dots,r_N$ (L292), and contest decisiveness $r$ (L445). The table lists only the last. Fix: reports $\hat\theta_i$, shares $\alpha_i$.
- **$s$ has two meanings.** It is the seller's cost (L161) and the advocate's signal $s_i$ (L309). Neither $s$ nor $b$ is in the table. Fix: signal $\sigma_i$, and add $b$ and $s$.
- **$S$ has two meanings.** It is the contest sum $\sum_j e_j^r$ (L446) and a bundle (L376). Neither is in the table.
- **$B$ has two meanings.** It is a bit budget (L347) and the Bell number $B_N$ (L383). Neither is in the table.
- **$v$ has two meanings.** It is the truck's value (L249) and the valuation function $v_i(x,\theta_i)$, also $v(S)$ at L376. The table mentions the truck's $v$ only inside the $G, g$ row.
- **$K$ versus $k$.** $K$ is kinds of action (L273) and $k$ is contingencies. They are easy to confuse, and $K$ is not in the table.
- **Symbols missing from the table:**
  - $p$, the per-household posted price (L223); the table has only $p_i$ and $P$
  - $n$, possible trades (L420), which sits beside $N$ and $m$ without comment
  - $\gamma$ (L473), defined and never used: cut it
  - $\bar u_i$ (L309), $m_0$ (L351), $A$ (L410)
  - $F_b, f_b$ (L529), which clash with the prior $F$
  - $\underline\theta, \bar\theta$ (L218)
  - $|\Theta|$ (L406), whereas the table defines $\Theta_i$ per agent
- **Table row $N$** reads "parties whose interests a decision affects". At L206 the market has $N$ buyers and $N$ sellers, so $2N$ parties.
- **The decomposition at L118** gives $N$ as an argument of $L_{\text{comp}}$ only. $L_{\text{info}}$ also depends on $N$ (that is the whole of §Informational costs), and $L_{\text{contest}}$ depends on $N$, $r$ and $V$. Fix: write $L_{\text{info}}(N)$ and $L_{\text{contest}}(N, r, V)$.

# 3. Logical gaps

- **L6 against L153, L347–349 and L445–449: the premise contradicts the arguments.** The abstract grants that "computation and messaging cost nothing". At $c=\kappa=0$, though:
  - the bit budget $B$ (L347) is infinite, so the computational frontier is unbounded;
  - the Tullock equilibrium $e^\ast = r(N-1)V/(N^2c)$ is undefined.

  The computational and contest arguments need $c,\kappa>0$, falling. Fix: "however low, but positive, the prices of computation and messaging".
- **L153 against L200.** The informational section says it "holds with $c=\kappa=0$", but cites Dixit–Olson on "very small transaction costs". Fix: move Dixit–Olson elsewhere, or note the exception.
- **L9 against L262–264: abstract and body disagree.** The abstract says "per-street pricing realizes a fraction $1/(N+1)$". In the body, $N$ is the number of residents each posting a price, and a single per-street price is the merged monopolist that realizes ½. The mapping is also inconsistent within the body:
  - L263 speaks of "a street of ten households";
  - L355 and L361 speak of "a route's segments", which suggests $N$ streets on a route.

  Fix: "pricing by each of $N$ independent rights-holders", and choose one reading of $N$.
- **L57, L267–268.** Krier's truck can "go round", and the caveat concedes that substitute routes defeat the result. So the running example is the case where the result has least force. Fix: say so, and move the derivation's illustration to a case with no route around it (the factory, the airshed).
- **L31 against L12 and L88: the central term changes definition.** At L31 the benevolent leviathan has two parts (coercion, welfare objective). At L12 and L88 it has three, adding knowledge of $F$. Fix: define it with all three at L31.
- **L124 against L118.** The equation is an exact equality, but the text says "I do not claim they are additive". The reader cannot tell what the equation asserts. Fix: present the terms as an ordered attribution (friction first, then information given zero friction, and so on), or replace the equation with a list.
- **L189–190: the mapping to Mailath–Postlewaite is not spelled out.** The theorem's condition is fixed per-capita cost (L185). That corresponds to $V/N$, or the developer's required compensation per household, staying fixed as the neighbourhood grows; the text does not say so. Also, "probability of an affirmative efficient decision → 0" means "fails to approve projects that should go ahead, with probability tending to one" only if the probability that going ahead is efficient stays bounded away from zero. Fix: state both conditions.
- **L186.** "common knowledge that going ahead is efficient and yet the probability of going ahead tends to zero". A newcomer asks why the parties do not simply go ahead. Fix: one sentence: everyone knows the total benefit exceeds the cost, but nobody knows who should pay how much, and any voluntary rule for assigning shares invites understatement.
- **L192–194, the intuition.** "No more than the difference $i$'s report makes to the decision": this needs to be multiplied by the size of $i$'s stake, and "amount that has to be covered grows like $N$" needs a pointer back to fixed per-capita cost. The implied rate is also never stated: only a fraction of order $N^{-1/2}$ of the needed money can be raised. A newcomer is left with no sense of how bad it is at $N=10$ or at $N=10{,}000$. Fix: state the rate.
- **L220: "each reading gives up one of the properties" is understated.**
  - Reading 1 is truthful but inefficient. Its constraint that the developer pays at most $V$, so $p \le V/N$, is never stated, and that constraint is what makes $F(p)^N$ fall while efficient approval (mean $\theta \le V/N$) tends to 1 by the law of large numbers. Spell this out.
  - Reading 2, $p=\max r_i$, gives up truthfulness and is also inefficient: it approves only if $N\max r_i\le V$.
- **L236–237.** The third reading pays "every member the same $p$", and the text then says such a rule exists: "the expected-externality mechanism". That mechanism pays type-dependent transfers. A rule with equal pay and an aggregate test invites high types to overstate so as to block. Fix: "once dissent can be overridden, an efficient rule exists, though it pays members different amounts (the expected-externality mechanism, below)".
- **L275.** "The truck example has this structure: each resident is the sole seller…". This illustrates Arrow's thin-market point, not Starrett's non-convexity, which is the sentence just before. Fix: attach it to Arrow.
- **L300.** "inherited jurisprudence mostly assigns rights all-to-one". This empirical claim is unsupported and not marked as argument, despite L40–43. Fix: cite it or flag it.
- **L328.** "The exception therefore strengthens the conclusion". It is consistent with the conclusion; it does not strengthen it. Fix: "The exception is consistent with the conclusion".
- **L334.** The computational results "bind decentralized agents and a planner equally". A newcomer then asks why they support the need for a leviathan. The link, that restrictions are constitutional choices, comes only at L430–431. Fix: say at L334 what role this section plays in the argument.
- **L383–384.** Krier's coalition is the grand coalition of all 10,000. The text does not say why finding the best partition into coalitions is the relevant problem. Fix: explain, e.g. that rival sub-coalitions form when residents' harms differ, and the grand coalition must be stable against them.
- **L436 against L452–453.** The section claims "losses that can rise as $c$ falls", but its main model shows spending "does not contain $c$". Only the commitment subsection, which works through $q$ and not $c$, shows a rise. Fix: "losses that do not fall, and in one case rise, as $c$ falls".
- **L460.** "With binding budgets, shares follow budgets." The model has no budgets. Fix: derive the claim or cut it.
- **L468.** "Cheaper cognition means more of it spent this way". This is more in quantity, but by the Tullock logic not necessarily more in value. Fix: say which is meant.
- **L475.** Ellingsen–Miettinen assume a positive commitment cost $\gamma$ and $q<1$. Pushing toward the free, certain limit leaves the theorem's conditions. The reader is also not told why both sides attempt commitment: each tries to commit to demanding the whole surplus. Fix: state the conditions and the mechanism.
- **L487–488 against L371 and L580–585.** Worst-case hardness is used against Krier for winner determination ("a fall in $c$" does not close it). Here, worst-case hardness as protection against manipulation is dismissed as "the kind that cheap computation removes". A newcomer will notice the asymmetry. Fix: say that both are worst-case, and that the manipulation point concerns typical instances, which are easy for manipulators as well as for solvers.
- **L497–498.** "The Mailath–Postlewaite theorem applies to it directly." Choosing a constitution from a menu is a decision among many alternatives, not a yes/no decision. The independence and fixed-cost conditions are not checked either. Fix: "applies in spirit", or argue the mapping.
- **L516.** "Agent vouchers need a tax base." L67 said governments "or philanthropies" fund them, and philanthropy is voluntary. Fix: address the philanthropy option.
- **L522.** "The framework guarantor needs what Hayek said the planner lacks, in distributional form." Hayek's point concerned particular circumstances. Knowing $F$, a statistical aggregate, is a much weaker requirement than knowing each $\theta_i$. The thesis that the guarantor "is doing a planner's job" rests on equating the two, and that equation is asserted, not argued. Fix: argue it explicitly, e.g. that setting entitlements, Harberger rates and compensation is what planners do, whatever their data.
- **L533.** "27/32 of first best with no intermediary". The second-best mechanism still needs a designer. Fix: "with a designer maximizing expected gains subject to budget balance".
- **L543 against L630.** One sentence says agent bargaining "moves the problem … to a different place". The other says it "leaves the problem … where it was". These contradict. Fix: pick one.
- **L562.** The prediction "success should fall with the surplus at stake relative to the cost of computation, since contest spending scales with surplus" is not supported by the model. The dissipated share $r(N-1)/N$ is independent of both $V$ and $c$. Fix: drop "relative to the cost of computation". If the claim concerns absolute spending, say why it lowers success.
- **L584 against the title and abstract.** The author says "the weight of my argument rests on the informational results", yet the title leads with "Computational". Fix: reorder the title.
- **L617–619 against L11.** The body concedes that a saturating contest would make contest spending fall, but the abstract states "whatever $c$ is" unqualified. **L627** says "The theorems above say…", though the contest term is the author's model and the computational term depends on $c$. Fix: qualify both.
- **L40–43 against the body.** Many claims are left unmarked although the opening promises every claim will be labelled: L300, L424 ("the holder of residual control is the sovereign"), L354, and L425's "that commitment needs an enforcer outside the parties", which is the author's addition attached to Maskin–Tirole. Also, the derivations are longer than the promised "two or three lines".

# 4. Mathematics

Re-derived and confirmed:

- **L169–170.** The density of $d=b-s$ on $[0,1]$ is $1-d$, and $\int_0^1 d(1-d)\,\mathrm dd = 1/6$. Correct.
- **L172–173.** $\int_0^{1/4}(d-d^2)\,\mathrm dd = 1/32-1/192 = 5/192$, so $32/192 - 5/192 = 27/192 = 9/64$. The ratio is $27/32 = 0.84375$. Correct. "About a sixth" (L175) is exactly $5/32 = 15.6\%$; "16 per cent" at L558 is consistent. Suggest giving $5/32$ once.
- **L178.** The VCG deficit is $E[(b-s)^+]=1/6$. Correct.
- **L226.** $F(p)^N$ follows from independence. Correct.
- **L255–262.**
  - The first-order condition of $(p_i-h_i)(1-G(P))$ is correct.
  - Summing gives $P-H=N(1-G)/g$.
  - In the uniform case, $P(N+1)=H+N$, so $1-P=(1-H)/(N+1)$.
  - At $N=10$ the fraction is $1/11$.
  - In the monopoly case ($N=1$) it is ½.

  All correct.
- **L273.** $N\cdot N\cdot K$ markets. Correct.
- **L314–317.** The tower-property argument is correct. It needs $s_i$ independent of everything else given $s_i'$, which garbling supplies, and the mechanism's outcome must not depend on $s_i$ beyond $s_i'$. That assumption is worth stating.
- **L340.** By Stirling, $\binom{m}{m/2}\approx 2^m\sqrt{2/(\pi m)}$. Correct.
- **L348–349.** $\log_2 B = m - \tfrac12\log_2(\pi m/2)$, and $\log_2 1000\approx 9.97$. Correct.
  - The relation $B$ = spending$/\kappa$ is implicit. State it.
  - Make the punchline explicit: with $m=m_0 2^k$, the bits needed grow like $2^{m_0 2^k}$. A thousandfold fall in $\kappa$ buys about 10 items, which is less than one extra binary distinction once $m_0\ge 10$.
- **L383.** $2^N-1$ is correct. The Bell number is superexponential. Correct.
- **L411.** $|A|^{2^k}$ functions and $2^k\log_2|A|$ bits are correct. Shannon's $2^k/k$ bound is for Boolean outputs ($|A|=2$). Say so.
- **L447–450.**
  - $\partial/\partial e_i$ of $Ve_i^r/S$ is $Vre_i^{r-1}(S-e_i^r)/S^2$. Correct.
  - At symmetry, $Vr(N-1)/(N^2e)=c$, so $e^\ast=r(N-1)V/(N^2c)$.
  - Total spending is $r(N-1)V/N$.
  - The payoff is non-negative iff $r\le N/(N-1)$. This is necessary, and it is the standard condition for a pure symmetric equilibrium, but "exists when … which is the condition that payoff is non-negative" understates the second-order requirements.
  - At $r=1$, $N=2$, spending is $V/2$.

  All correct.
- **L529–533.**
  - The uniform virtual value is $2b-1$ and the virtual cost is $2s$, so trade happens iff $b-s\ge 1/2$.
  - $\int_0^{1/2}(d-d^2)\,\mathrm dd = 1/8-1/24 = 1/12$, so the gain is $1/6-1/12 = 1/12$, which is half.

  Correct. "Virtual cost" is used without definition (only virtual value is defined). Add: "the seller's virtual cost, $s+F_s(s)/f_s(s)$".

Formulas with undefined symbols:

- **L376.** $S, T$ are glossed as bundles, but $S$ clashes with L446.
- **L406.** $|\Theta|$.
- **L473.** $\gamma$ is defined and never used.

I found no arithmetic errors.

# 5. Machine-written or mannered prose

- **L40–43.** "An argument, which is a claim I believe but cannot prove, is called an argument." This is tautological. Fix: "Claims I believe but cannot prove are marked as arguments."
- **Five labels for one status.** "short derivation of mine using known results" (L167), "a short analysis of my own" (L217), "a short derivation of mine" (L247), "a short observation of mine" (L307), "a short calculation of mine" (L346, L531), "a small model of my own" (L440). Fix: one fixed tag, e.g. "(my derivation)".
- **Sentences that announce:**
  - L125 "Its use is to make one point visible."
  - L155 "The organizing observation is an asymmetry"
  - L209 "The contrast is the main structural fact of this section."
  - L216–217 "its rules can be analyzed exactly. What follows is…"
  - L266 "There is a caveat."
  - L297 "Two consequences follow."
  - L324 "There is an honest exception."
  - L481 "which I treat briefly"
  - L493 "This section is argument, not theorem."

  Cut or fold each into the claim that follows.
- **Flourishes:**
  - L290 "With private types that is false, by a theorem."
  - L344 "This is Hayek's problem of dispersed knowledge stated as a theorem"
  - L382 "The speed of forming a coalition is not the constraint."
  - L390 "makes the cycle turn faster without ending it"
  - L401 "their author picks the winners"
  - L457 "This divides Krier's … sentence in two."
  - L589 "They do."
- **Repeated "X does A; it does not B" antithesis:** L264, L418, L524 ("That helps the leviathan do its job; it does not remove the job"), L540 ("Transparency raises the cost …; it does not change the objective"), L543, L568, L630. Keep one.
- **L507.** The tricolon "what it must be able to do, what it must know, and what it must want" is repeated as three headings. It is acceptable as structure, but the sentence itself is a set piece.
- **L302.** The heading "why a better advocate thins it" uses a vague figure. Fix: "Better-informed advocates make fewer rules acceptable".
- **L630.** The closer "leaves the problem of building a good government where it was" is a set-piece ending, and it contradicts L543.
- **Hedging:** L353 "In fairness", L593 "I do not know of a relaxation … but the theorems are stated for particular models and real economies are not those models", L605 "which seems to be what Coasean bargaining needs".
- **Repetition.** L38 and L570–574 describe Petel, Ngo and Shahidi twice in near-identical words ("sympathetic economic treatment … new frictions of its own"). Cut one. "Krier is right" recurs at L24, L555 and L623–624.

# Three questions

**Thesis in two sentences.** Suppose AI agents made bargaining effectively free and perfectly loyal. The losses from private information, from the sheer size of the allocation problem, and from spending on bargaining advantage would remain. The informational loss gets worse as more parties must consent to one decision. Every known remedy needs an actor that can coerce, knows the distribution of preferences, and aims at total welfare, so Krier's "lean framework guarantor" is a planner and agent bargaining does not produce one. I could state this, but only after reconciling the three-part leviathan of L12 with the two-part one of L31, and after discounting a title that foregrounds computation when L584 says the weight lies on information.

**Hardest section.** "Communication and computation" (L330–431) was the hardest. It is a run of about twenty citations in a row, with unglossed terms of art (nondeterministic communication, compact representations, PPAD, value-query model, derandomization, winner determination). Most results are never run on the truck, developer or factory. The section's role in the argument is unclear, because it concedes at L334 that the results bind a planner equally, and the link to the thesis (restrictions are constitutional choices) appears only in its last two sentences. Three changes would fix it:

- Open with that link.
- Keep three results, each worked on a running example: the Nisan–Segal bit count with the $m=m_0 2^k$ comparison made explicit; substitutes versus complements; and incomplete contracts with residual control.
- Move or cut the rest: correlated-equilibrium complexity, mechanism-design hardness and Rice.

**Single most important thing still not understood.** The reader would still not know what the benevolent leviathan actually does in one of the running examples. Take the developer and 10,000 homeowners: which mechanism does it run, who is taxed and how much, and what it must know. The reader also would not know why acting on knowledge of the distribution $F$ alone counts as "doing a planner's job" in Hayek's sense. No example is carried through to its remedy. The planner equivalence is asserted at L89, L522 and L628 and never argued, and without that argument the thesis does not follow.