# Brief: "The compute budget of a Coasean principal"

You are writing a serious academic article, as a Quarto `.qmd` file, for Dan MacKinlay (statistician and ML researcher, writes at danmackinlay.name).
The article responds to Séb Krier, "Coasean Bargaining at Scale" (Cosmos Institute, 26 Sep 2025), <https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale>.
Read Krier's essay in full before writing (fetch it; do not work from this brief's quotations alone).

Write the file to `/Users/dan/Source/livingthing/_plans/hyperscaling_coase_personal_budget_2.qmd`.

**Do not read any other file whose name starts with `_plans/hyperscaling_coase_`, nor any of Dan's notebook posts on this topic.** This round is meant to be independent of his earlier work. You may read `_plans/hyperscaling_coase_personal_budget_2_sim.py` (the numerical checks for this article) and the two voice guides named below.

## The assignment, in Dan's words

> write a serious academic article that explores the equilibria in which individual principals will find themselves in an actually-existing Coasean-bargaining world. Suppose I (and all other principals on the planet …) have a computational budget, correlated with my current endowments. Consider how many matters I might need to contract, and the optimal allocation of my compute budget over all the bargains I am presumably involved in. Assume other principals are selfish, adversarial and represented by perfectly aligned agents who may compute up to *their* limits, which are different. Profitable outcomes accrued by one principal may be spent on compute, or on object level costs. I am suspicious that the world this leads to is recognisably a good one, but this needs testing.
>
> I would like to try to push the Krier piece to its limits to uncover any downsides of the implied model. … set up some toy mathematical models … You should use symbols when making claims (e.g. "computational complexity $\mathcal{O}(N^3)$ in number of clauses"), don't just talk about things being NP hard without claiming what they are hard in, or convex without saying what they are convex in.
>
> Your special angle: given what we know about compute and game theory, what can we say about the principal's production function with respect to compute and initial endowments? How does that tally with the production function implied by good outcomes in Krier's ideal state?

"Suspicious that" here means he doubts it. The job is a test, not a hit piece: report what survives as plainly as what fails.

## What I need from you

The models, derivations, numbers and references below are done and checked. Your job is the exposition: a clear, human presentation that a reader who has read Krier's essay, and has undergraduate economics and some game theory, can follow without having sat through the derivation.

- **Reader.** Has read Krier. Knows what a Nash equilibrium and a first-order condition are. Has not seen contest theory, does not know what a "contest success function" or "shadow price" is until you say. Has never seen this brief.
- **Every symbol and every term is defined where it first appears**, in a full sentence. Keep a notation table near the start.
- **Controlled vocabulary.** Use the literature's name for a thing when it has one (contest success function, rent dissipation, liquidity constraint, repeat player, standard-form contract, shadow price). Do not coin new terms. The few working labels in this brief (*matter*, *stakes*, *strength*, *decisiveness*, *the Krier benchmark*) must each be defined once and used consistently; if you can do without one, drop it. One term per concept, no synonyms.
- **Running example with a fixed cast.** Carry one small cast through the whole article and state each result first as what happens to them, then in symbols, then (where there is one) the checked number. Suggested cast: Alice, a tenant and employee with a little liquid savings; Bob, her neighbour, of similar means; and a landlord company with $M$ tenants. Worked numbers for them are given below. Do not let the toy numbers carry the exposition; one line of numbers after the story.
- **Anchor each section to a sentence of Krier's**, quoted exactly, and say what that sentence presumes. Verbatim quotations are supplied below; check them against the essay.
- **Claims carry their scope.** "Convex in $c_{im}$", "exponential in the number $n$ of contingencies", "independent of the price $p$". Never a bare "NP-hard" or "convex".
- **State which results are theorems of the toy model, which are simulation output, and which are conjecture.** State plainly where Krier comes out right.
- **Voice.** Read `/Users/dan/Source/livingthing/_voices/dan_voice.md` and `/Users/dan/Source/livingthing/_voices/slop_patterns.md` and follow them. Mechanical rules: British spelling with *-ise*; "we" for author-and-reader, "I" for Dan's own judgements, never an indefinite "you"; no colon in headings; no rhetorical set-up-then-reveal; no praise of the argument's own interest; plain literal phrasing, no mixed or decorative metaphor; round numbers in prose; literal `TODO:` for open threads. Link text names the concept, never a page or section title ("the [paradox of power](…)", not "see Hirshleifer's paper").
- **Format.** One sentence per line in prose paragraphs (the repo's pre-commit hook requires it). Maths in `$…$` and `$$…$$`. Pipe tables. No executable code cells. Frontmatter: `title`, `date: '2026-11-19'`, `description` (one plain sentence), `categories` (a few from: economics, cooperation, game theory, AI, institutions). Cite by hyperlinking author–year text to the URL given in the reference list below; do not invent citation keys and do not cite anything not in that list. End with an HTML comment: `<!-- TODO: uv run ref-cite -c <collection> -i _plans/hyperscaling_coase_personal_budget_2.qmd to move these links into Zotero -->`.
- **Length.** Whatever the argument needs; I expect 6,000 to 8,000 words. Prefer cutting a secondary section to compressing a primary one into shorthand.
- **Check my algebra as you go.** If a derivation does not go through, or a claim seems stronger than the model supports, do not paper over it: write it the way you can defend and list the discrepancy in your final message to me.

Your final message to me should list: anything you could not verify, any place you departed from this brief and why, and the word count.

---

## 1. Krier's sentences to anchor on (verbatim; verify)

- K-a: "What costs $10,000 in legal fees today might cost pennies to compute tomorrow. Consider how a billionaire’s phone today is no more powerful or effective than yours."
- K-b: "Skeptics might say agents don't eliminate costs entirely; they just shift them to compute overhead, data privacy setups, agent configurations etc. This is true! But it also underestimates the scale of reduction."
- K-c: "This is unlikely to be a huge growing cost over time, as agent tech commoditizes, these costs approach zero asymptotically."
- K-d: "A hybrid might work best: a universal basic compute allocation for personal use, plus additional targeted support for specific democratic and legal functions where equal participation is constitutionally guaranteed."
- K-e: "The agents themselves would likely converge on stable equilibria for most issues simply to reduce computational overhead - constant renegotiation is expensive even for AGI."
- K-f: "But what if the agents of 10,000 residents, seeing a factory’s proposal to increase emissions, can form a bargaining coalition in a nanosecond?"
- K-g: "The developer’s agent must discover the price at which every single homeowner would agree."
- K-h: "Ideally the agent system transforms enforcement from a costly legal battle into a near-instantaneous computational verification."
- K-i: "The (gradually automated) state continues to define and enforce basic property rights, contract law, criminal justice, and constitutional rights - the bedrock rules without which agent negotiations would be meaningless."
- K-j: "Unlike social media, network effects are also far weaker. And in a competitive market with switching costs approaching zero, parasitic agents get quickly identified and abandoned."
- K-k: "In other words, AGI could enable hyper-granular contracting."

## 2. The thesis, in one paragraph

Krier's good outcome presumes a particular production function for each principal: income from bargaining that is flat in the principal's own compute above a small threshold, unaffected by anyone else's compute, with a threshold whose cost falls to nothing as compute gets cheap (K-a, K-c).
What we know about compute in adversarial games gives a different function: a principal's share of each bargain depends on the *ratio* of its compute to its opponent's.
Under that function, and conceding Krier perfect agent alignment, perfect enforcement and a common compute price, four things follow in the toy models.
(1) Spending on bargaining does not fall as compute gets cheaper: at equal strength a fraction $r/2$ of every surplus is spent contesting its division, whatever the price $p$ of compute.
(2) Wealth as such buys no advantage above a threshold, which is Krier's billionaire's-phone claim and it survives; but the threshold is a fixed fraction of a principal's stakes in dollars, not a cheap fixed quantity of compute, and below it a principal's share falls as the square root of its wealth-to-stakes ratio.
(3) Making a contest fair makes it expensive: the compute burnt on a matter equals the weaker side's share of it, so subsidies that restore fair shares raise waste.
(4) The parameter that separates the two worlds, the decisiveness $r$ of compute, is zero only in games small enough for both sides to solve, and the size of the game is chosen by the stronger side.
The world is better than a world with no bargaining for nearly everyone in these models (one exception: manufactured threats), and it delivers roughly half of what Krier promises to the comfortable and much less to the liquidity-constrained.
The remedies that work are rules that bound the bargaining game itself, which is a planner's job that Krier's "framework guarantor" state (K-i) was not given.

## 3. Constitution (fix this early, and say that it concedes Krier everything it can)

- C1 Entitlements. Every principal holds well-defined rights. If a bargain fails each side keeps its entitlement. Courts enforce every contract, perfectly and free.
- C2 Voluntariness. Nobody is bound without consent; silence is refusal.
- C3 Alignment. Every agent serves its principal perfectly.
- C4 Open compute market. Anyone may buy compute at the same price $p$ per unit.
- C5 Criminal law. No violence, theft or fraud.
- C6 Freedom of bargaining technique. No limit on how much compute a party brings to a bargain or on how complicated a contract it proposes. (Sections 9–10 relax this one.)

Principals are selfish; each agent computes up to its principal's limit. "Principal" covers people, firms, any contracting party.

## 4. Notation

| symbol | meaning |
|---|---|
| $N$ | number of principals |
| $w_i$ | liquid wealth of principal $i$ at the start of a period, in dollars |
| matter $m$ | one bilateral bargain, between $i$ and an opponent $j=j(m)$ |
| $S_m$ | surplus of matter $m$: the dollars a deal creates over both sides keeping their entitlements |
| $E_i=\sum_{m\ni i}S_m$ | $i$'s *stakes*: total surplus across all of $i$'s matters |
| $c_{im}$ | compute $i$ spends on matter $m$ |
| $p$ | price of one unit of compute, dollars |
| $R$ | gross return on a dollar put to object-level use (capital, tools, training) instead of compute |
| $s_{im}$ | $i$'s share of $S_m$ |
| $\theta_m$ | the share $i$ would get at equal compute ("merit"; $\tfrac12$ unless stated) |
| $r$ | decisiveness of compute |
| $\lambda_i$ | shadow price of compute to $i$: the income $i$ would gain from one more unit |
| $a_i=1/\lambda_i$ | $i$'s bargaining *strength* |
| $\rho_i=Rw_i/E_i$ | wealth-to-stakes ratio |

## 5. The Krier benchmark production function (my reading of K-a to K-d; label it as a reading)

$$Y_i^{K} \;=\; R\,w_i \;+\; \theta E_i \;-\; p\,\bar c\,M_i \qquad\text{whenever } c_{im}\ge \bar c \text{ on each of } i\text{'s } M_i \text{ matters,}$$

with $\bar c$ a fixed, technologically given amount of compute needed to find and close a deal, so that $p\bar c\to0$.
Four properties:
(i) *satiation*: $\partial Y_i/\partial c_{im}=0$ above $\bar c$;
(ii) *no rivalry*: $\partial Y_i/\partial c_{jm}=0$;
(iii) *compute is productive*: more compute in total means more surplus in total;
(iv) *cheap floor*: the subsidy that lifts everyone to $\bar c$ costs $p\bar c$ per matter and vanishes as $p\to0$.
Krier does not write this down; it is what "a billionaire's phone … no more powerful or effective than yours" and "these costs approach zero asymptotically" amount to. He does grant that outcomes depend on who holds the entitlement and on wealth effects on willingness to pay; that is a different channel and not what we test.

## 6. What we know about compute in adversarial games

The contest success function (define: the map from two sides' efforts to their shares or win probabilities):

$$s_{im}=\frac{\theta_m c_{im}^{\,r}}{\theta_m c_{im}^{\,r}+(1-\theta_m)\,c_{jm}^{\,r}} .$$

- This is the Tullock ratio form. [Skaperdas (1996)] shows the ratio form is the one contest success function, among those satisfying his axioms, in which only the ratio of efforts matters (homogeneity of degree zero). [Hirshleifer and Osborne (2001)] use exactly this form for litigation, with $\theta$ the true degree of fault: at equal effort the court gets it right, and effort bends the result.
- Useful identity: $\partial s_{im}/\partial c_{im}=r\,s_{im}(1-s_{im})/c_{im}$. The share is a logistic function of $r\log(c_{im}/c_{jm})$.
- Evidence that compute behaves this way. [Jones (2021)] trained AlphaZero agents on the board game Hex across six orders of magnitude of compute. Elo rating rises linearly in log compute, about 500 Elo per tenfold increase (fitted coefficient 510). Elo is by definition a logistic in rating difference with scale 400, so a linear-in-log-compute Elo *is* the ratio form with $r=(\text{Elo per tenfold})/400\approx1.3$. Jones's own summary: an agent with twice its opponent's compute wins about 2/3 of the time, which is $r=1$ exactly. He notes this matches a toy in which each player draws random numbers in proportion to its compute and the highest draw wins; that toy is the $r=1$ lottery contest, the same structure as the research tournament of [Fullerton and McAfee (1999)].
- The same paper shows the limit of this: the curve flattens at perfect play. The compute needed to reach perfect play multiplies by about 7 for each unit increase in board size ($10^{430/510}$ from the fitted coefficients; perfect play needs about $10^{11}$ units at size 3 and $10^{16}$ at size 9). So: ratio form while neither side can solve the game; no return to compute once both can.
- Bargaining agents specifically. [Anthropic's Project Deal (2026)]: 69 employees, 186 deals, about $4,000 traded by Claude agents. Agents on the stronger model (Opus) sold for $2.68 more and bought for $2.45 less than agents on the weaker (Haiku) for the same item, on items with a median price of $12; an Opus seller facing a Haiku buyer averaged $24.18 against $18.63 for Opus facing Opus; and the people represented by the weaker model rated their deals as just as fair (4.06 vs 4.05 on a 7-point scale). [Zhu et al. (2025)] find the same imbalance across LLM agents in simulated consumer negotiations. These vary model quality, not compute at fixed model, so they show $r>0$ for bargaining without measuring it.
- Where $r=0$. A game both sides can solve outright. The alternating-offers bargaining game with complete information ([Rubinstein 1982]) has a closed-form solution; more compute buys nothing. This is the world of K-a.
- Honest status: nobody has measured $r$ for agent bargaining as a function of compute ratio. $r$ is the paper's free parameter. $r=0$ is the Krier benchmark; $r=1$ is the headline case because it is the measured value for the one game studied carefully.

## 7. One matter

**Result 1 (spending on a bargain does not depend on the price of compute).** Two unconstrained risk-neutral principals, one matter. Each maximises $s_{im}S_m-p\,c_{im}$. The first-order conditions are $r s(1-s)S_m/c_{im}=p$ for both, so $c_{im}=c_{jm}$, the share is $\theta_m$, and

$$p\,c^{*}=r\,\theta_m(1-\theta_m)\,S_m \quad\text{each;}\qquad \text{fraction of } S_m \text{ spent} = 2r\theta_m(1-\theta_m)=\tfrac r2 \text{ at } \theta_m=\tfrac12 .$$

A pure-strategy equilibrium of this form needs each side's net payoff non-negative: $r\le2$ at $\theta=\tfrac12$. ([Baye, Kovenock and de Vries (1994)]: for $r>2$ equilibrium is in mixed strategies and the whole surplus is dissipated in expectation.)
The price $p$ does not appear in the dollars spent. Cheaper compute means more compute bought, $c^*\propto1/p$.
This is rent dissipation ([Tullock 1980]; [Posner 1975]); what is specific to our setting is reading $p$ as the price of compute and noticing the result does not depend on it.
Merit is preserved at equal strength ($s=\theta$): the split is the one a neutral arbiter would give; the cost is the waste.
Checked numerically for $r\in\{0.5,1,1.5\}$, $p\in\{1,10^{-3},10^{-6}\}$: spending is $r/4$ of $S$ each in every case.
Cast: Alice and Bob bargain over his leaf blower; a deal is worth $100 a year between them. At $r=1$ each spends $25 on compute and nets $25. Make compute a million times cheaper and each still spends $25.

Against K-e ("agents … converge on stable equilibria … to reduce computational overhead"): in a single matter mutual restraint is not an equilibrium, since either side gains by deviating. Between the same two parties over many periods restraint could be sustained by the threat of reverting to the contest, but only if each can observe the other's compute, and compute is private: one can prove that work was done, not that it was not. Mark this as the main untested escape route (a verifiable limit on compute per matter). Do not claim it is impossible.

**Result 2 (which transaction costs vanish).** Split compute into *discovery* $A=A_i+A_j$, which creates surplus $S(A)$, increasing and concave, and *claiming* $b_i$, which divides it (creating versus claiming value: [Lax and Sebenius 1986]). Payoff $s(b_i,b_j)S(A)-p(A_i+b_i)$.
Symmetric equilibrium: $S'(A^*)=2p$ (each side gets half the benefit of discovery, so too little is done; a planner sets $S'(A^\circ)=p$) and $p\,b^*=rS(A^*)/4$ each.
With $S(A)=\bar S(1-e^{-A/k})$: $A^*=k\ln(\bar S/2pk)$, discovery spending $pA^*\to0$ as $p\to0$, $S(A^*)\to\bar S$, claiming spending $\to r\bar S/2$.

$$\lim_{p\to0}\frac{\text{total spending on the transaction}}{S}=\frac r2 .$$

| $p$ | discovery spending / $S$ | claiming spending / $S$ | planner's cost / $S$ |
|---|---|---|---|
| $10^{-1}$ | 0.20 | 0.50 | 0.26 |
| $10^{-2}$ | 0.04 | 0.50 | 0.05 |
| $10^{-3}$ | 0.006 | 0.50 | 0.007 |
| $10^{-6}$ | 0.000 | 0.50 | 0.000 |

($r=1$, $\bar S=k=1$.) Krier is right about the first column (K-a, K-b): the cost of finding the deal and writing it down goes to nothing. The second column is the part his sentence does not cover.

## 8. Many matters and a budget

### 8a. How many matters

With $N$ principals there are up to $N-1$ bilateral matters per principal and $N(N-1)/2$ in all (about $5\times10^{19}$ for $N=10^{10}$), and $2^{N-1}$ coalitions containing any one principal. Finding which pairs have a deal worth making is the discovery problem, where cheap compute helps and Krier is right. Krier's own picture is "a million micro-transactions in the background" per person. What matters below is not the count $M_i$ but total stakes $E_i$, except for a per-matter fixed cost (8d).

### 8b. Hard budgets (the base case Dan asked for)

Each principal has a compute budget $C_i$, use it or lose it, and chooses $c_{im}\ge0$ with $\sum_m c_{im}=C_i$ to maximise $\sum_m S_m s_{im}$. For $r\le1$ the objective is concave in $i$'s own allocation $(c_{im})_m$, so the Kuhn–Tucker conditions characterise the best response. For $r<1$ every matter gets some compute and, with $\lambda_i$ the multiplier on the budget and $a_i=1/\lambda_i$ (take $\theta=\tfrac12$):

$$s_{im}=\frac{a_i^{\,r}}{a_i^{\,r}+a_j^{\,r}},\qquad c_{im}=r\,a_i\,S_m\,s_{im}(1-s_{im}),\qquad \sum_m c_{im}=C_i \text{ pins down } a_i .$$

(Derivation: $i$'s condition on matter $m$ is $rS_ms(1-s)/c_{im}=\lambda_i$ and $j$'s is the same with $c_{jm},\lambda_j$; divide to get $c_{im}/c_{jm}=a_i/a_j$.)

Consequences, all checked numerically on random networks of 60 principals ($r=0.5$ and $0.9$; a best-response search from an uninformed start recovers the allocation to $10^{-8}$):

1. *One number per principal.* Every bilateral split in the economy is determined by the two parties' strengths, as in a rating system.
2. *Allocation rule.* Compute goes in proportion to $S_m\,s_{im}(1-s_{im})$: to large matters and to evenly matched ones. Little is spent on matters that are nearly won or nearly lost.
3. *Only relative budgets matter.* Multiply every $C_i$ by the same factor and no share changes (numerically: to $10^{-16}$). A general fall in the price of compute, or a general rise in budgets, changes nothing about who gets what. This is the opposite of property (ii) of the benchmark.
4. *Two principals.* If $i$ and $j$ face only each other, across any number of matters, $s=C_i^{\,r}/(C_i^{\,r}+C_j^{\,r})$ on every matter and each allocates in proportion to $S_m$: the proportional rule of [Friedman (1958)]. (Check: budgets 3:1 give 0.75 at $r=1$.)
5. *Strength is compute per dollar at stake.* In a population of similar principals $a=4C/(rE)$. If budgets scale with wealth as $C_i\propto w_i^{\eta}$ and stakes as $E_i\propto w_i^{\mu}$, strength scales roughly as $w_i^{\eta-\mu}$ (exact only near equal strength; say so). Stakes in a job, a home, a neighbourhood grow less than in proportion to wealth ($\mu<1$) while compute is a discretionary purchase ($\eta\ge1$), so richer principals are stronger on every matter. If instead $\eta=\mu$ everyone is equally strong and all splits are at merit.
6. *Abandonment at $r=1$.* At $r=1$ the best response is $c_{im}=\max\{0,\sqrt{a_iS_mc_{jm}}-c_{jm}\}$: principal $i$ puts nothing on a matter where the opponent's compute exceeds $a_iS_m$. Example checked numerically: $j$ has budget 1 and two matters each with $S=1$, one against $k$ (budget 1, no other matters) and one against $i$ (budget $C_i$, no other matters). $j$ abandons the matter against $i$ entirely once $C_i>4$.

These are close relatives of the conflict-network models of [Franke and Öztürk (2015)] and [Xu, Zenou and Zhou (2022)], which use convex effort costs where we use a budget.

### 8c. Buying compute out of wealth (Dan's "profits may be spent on compute or on object-level costs")

Now $i$ splits wealth $w_i=k_i+p\sum_mc_{im}$ between object-level capital $k_i$, returning $R$ per dollar, and compute. End-of-period resources are $Rk_i+\sum_mS_ms_{im}$.
A principal with $k_i>0$ is *unconstrained*: its shadow price of compute is $\lambda_i=pR$, the same for all such principals, so $a_i=\bar a=1/(pR)$.
A principal who would want to spend more than $w_i$ on compute is *liquidity-constrained*: $k_i=0$, $\lambda_i>pR$, $a_i<\bar a$.

**Result 3 (above a threshold, wealth buys no advantage).** Any two unconstrained principals split every matter between them at merit, each forgoing $rS_m/4$ of end-of-period income on it. A billionaire does no better against a merely comfortable opponent than the comfortable do against each other. This is K-a, and it survives. It is the "[paradox of power](Hirshleifer 1991)": the richer side has no reason to spend more on the contest than the stake warrants, and the poorer side fights as hard. But note what the threshold is. $i$ is unconstrained iff

$$R\,w_i\;\ge\;\frac r4\,E_i ,$$

a fixed fraction of $i$'s stakes in dollars, independent of $p$. In units of compute the threshold is $rE_i/(4pR)$, which grows without bound as compute gets cheaper. Krier's $\bar c$ is a technological constant; this threshold is set by the equilibrium.

**Result 4 (below the threshold: the square-root law).** Take $r=1$ and a constrained principal $i$ whose opponents are unconstrained. Writing $x=a_i/\bar a$, the share is $s=x/(1+x)$ and the budget equation is $x^2/(1+x)^2=\rho_i$, so

$$s_{im}=\sqrt{\rho_i}=\sqrt{Rw_i/E_i}\ \text{ on every matter},\qquad Y_i=\sqrt{R\,w_i\,E_i}\quad(\rho_i\le\tfrac14),$$

and $i$ puts all its wealth into compute and none into object-level capital. Together with Result 3, at $r=1$:

$$Y_i(w_i,E_i)=\begin{cases}\sqrt{R\,w_i\,E_i}, & Rw_i<E_i/4\\[2pt] R\,w_i+E_i/4, & Rw_i\ge E_i/4\end{cases}\qquad\text{against}\qquad Y_i^{K}=R\,w_i+E_i/2 .$$

(Continuous at the threshold: both branches give $E_i/2$.) For general $r\le 1$ the constrained share solves $r\,s^{(1+r)/r}(1-s)^{(r-1)/r}=\rho_i$; for small $\rho_i$, $s\approx(\rho_i/r)^{r/(1+r)}$ and $Y_i\approx E_i^{1/(1+r)}(Rw_i/r)^{r/(1+r)}$: a Cobb–Douglas function of stakes and wealth with exponent $r/(1+r)$ on wealth. The elasticity of bargaining income with respect to compute, for a principal facing unconstrained opponents, is $r(1-s)/(1+r(1-2s))$, which is exactly $\tfrac12$ at $r=1$ for every $s<\tfrac12$.
The marginal return on a dollar for a constrained principal is $\tfrac12\sqrt{RE_i/w_i}>R$: such principals would borrow to buy compute if they could. With a perfect credit market (lending against expected bargaining gains, as litigation funders do) nobody is constrained and only the waste of Result 1 remains. Say this: the liquidity constraint, not the contest, is what makes shares unequal.

| $\rho_i=Rw_i/E_i$ | share of each surplus | $Y_i/Y_i^K$ |
|---|---|---|
| 0.01 | 0.10 | 0.20 |
| 0.05 | 0.22 | 0.41 |
| 0.10 | 0.32 | 0.53 |
| 0.25 (threshold) | 0.50 | 0.67 |
| 1 | 0.50 | 0.83 |
| 10 | 0.50 | 0.98 |

Cast: Alice's tenancy is worth $4,000 a year of surplus between her and the landlord; she has $160 in liquid savings; take $R\approx1$. $\rho=0.04$, her share is 20%, $800, obtained by spending all $160 on compute. The benchmark gives her $2,000. (Illustrative numbers, not estimates; say so.)

**Result 5 (a fair contest is an expensive one).** On a matter between a constrained $i$ and an unconstrained $j$ at $r=1$, the end-of-period income both sides forgo by buying compute is exactly

$$R\,p\,(c_{im}+c_{jm})=s_{im}\,S_m .$$

(From $Rp\,c_{jm}=S_ms(1-s)$, $Rp\,c_{im}=xS_ms(1-s)$, $s=x/(1+x)$.) The waste on a matter equals the weaker side's share of it. A lopsided match is cheap because the weak side concedes and the strong side need not exert itself; at equal strength half the surplus is burnt. So any policy that raises the weak side's share (K-d's basic compute allocation) raises waste one for one, as long as $r$ stays put.

**Result 6 (what a compute subsidy costs).** To bring $i$ to the threshold takes a top-up of $(rE_i/4R-w_i)^+$ dollars per period: proportional to stakes, independent of the price of compute. Against K-c ("these costs approach zero asymptotically") and property (iv).

### 8d. A fixed cost per matter

If merely reading and evaluating a proposal costs $f$ units of compute ([Anderlini and Felli (2006)] show that even small costs paid before bargaining can stop Coasean agreement), a matter is worth engaging only if its value at the optimum covers that: $S_m\,s_{im}\,(1-r(1-s_{im}))\ge\lambda_if$. (Value of a matter net of the shadow cost of the compute spent on it: $S_ms-\lambda_ic_{im}=S_ms(1-r(1-s))$.) For a weak principal, with $s$ small and $\lambda_i$ large, most matters fail the test: it engages on a few large ones and lets the rest go by default. A principal with budget $C_i$ can read at most $C_i/f$ proposals, and an adversary can send more than that. C2 (silence is refusal) protects the principal's entitlements but then the surplus on those matters is lost; the alternative, a bond of at least $pf$ posted with each proposal and paid to the recipient, makes reading self-financing. [Shahidi et al. (2025)] flag congestion of this kind. Keep this short. Note that click-through terms of service are this equilibrium today, with human attention as the budget.

### 8e. Dynamics and initial endowments

Each period a principal needs subsistence consumption $\underline c$ and saves a fraction $\beta$ of what is left: $w_i'=\beta\,(Rk_i+Y_i-\underline c)^+$. Bargaining income includes the wage bargain; there is no other income in the model.

Against unconstrained opponents at $r=1$, in the constrained region $w'=\beta(\sqrt{REw}-\underline c)^+$. If $\beta RE>4\underline c$ this map has an unstable fixed point

$$w_-=\Big(\tfrac{\beta\sqrt{RE}-\sqrt{\beta^2RE-4\beta\underline c}}{2}\Big)^{2}$$

below which wealth, and with it the principal's share of every bargain, falls to zero. Above it wealth grows until the principal is unconstrained and settles at $w^{**}=\beta(E/4-\underline c)/(1-\beta R)$ (needs $E/4>\underline c$, $\beta R<1$). Under the benchmark there is no such threshold: income is $E/2$ whatever the wealth, and $w^{**}_K=\beta(E/2-\underline c)/(1-\beta R)$.
So initial endowments matter in one specific way: through which side of $w_-$ a principal starts. Above it, the concavity of the production function ($r\le1$) erases initial differences.

Simulation (600 principals, about 8 matters each on a random network, stakes lognormal with mean 1, initial wealth lognormal with median 1 and log-s.d. 1.5, $\beta=0.9$, $R=1.05$, $\underline c=1.2$, 300 periods, $r=1$; `_plans/hyperscaling_coase_personal_budget_2_sim.py`):

| scenario | Gini of wealth | share of principals at zero wealth | compute spending / total surplus | mean wealth |
|---|---|---|---|---|
| Krier benchmark ($r=0$) | 0.27 | 0.2% | 0 | 46 |
| contest, $p=10^{-3}$ | 0.45 | 12.5% | 0.39 | 21 |
| contest, $p=10^{-6}$ | 0.45 | 12.5% | 0.39 | 21 |
| contest + basic compute worth $0.05 a period (0.6% of mean stakes) | 0.42 | 9.7% | 0.44 | 18 |
| contest + basic compute worth $0.50 a period (6% of mean stakes) | 0.28 | 0.7% | 0.48 | 22 |

The closed-form threshold at mean stakes ($E\approx8$) is $w_-\approx0.27$; the parity threshold is $Rw\ge E/4\approx2$.
Reading: (a) the two contest rows are identical, a million-fold fall in the price of compute changes nothing; (b) a basic compute allocation that is large enough *in dollars relative to stakes* does remove the trap and restore the benchmark's distribution, so K-d works as a distributional remedy; (c) it does so while raising waste from 39% to 48% of surplus and leaving mean wealth at half the benchmark; and the subsidy is unfunded in the simulation (it arrives free), so this flatters it.
This is simulation output for one parameter set, not a theorem. The case $r>1$ is not simulated: the allocation problem is then not concave in $c_{im}$. [Hirshleifer (1991)] finds that when decisiveness is high the paradox of power fails and the richer side gains; treat $r>1$ (which is where Jones's fitted 1.3 sits) as likely worse than what is shown, and flag it as untested.

## 9. Repeat players

Much bargaining work is reusable across matters of the same type (a landlord's analysis of its lease, a model tuned on its past negotiations). Let effective compute on a matter be $z_{im}=g_i^{\phi}\,\ell_{im}^{1-\phi}$, with $g_i$ a general investment paid for once and usable on all of $i$'s matters of this type, $\ell_{im}$ matter-specific work, and $\phi\in[0,1)$ the reusable fraction. Shares use $z$ in place of $c$.
For a principal with $M$ identical matters the optimum has $g/\ell=\phi M/(1-\phi)$, total spending per matter $rSs(1-s)/\lambda$ exactly as before, and effective compute per matter larger by the factor $M^{\phi}$ than a one-matter principal spending the same. Against $M$ one-matter counterparties with the same shadow price:

$$s_{\text{repeat}}=\frac{M^{\phi r}}{1+M^{\phi r}} .$$

| $\phi$ | $M=10$ | $M=10^3$ | $M=10^6$ |
|---|---|---|---|
| 0.2 | 0.61 | 0.80 | 0.94 |
| 0.5 | 0.76 | 0.97 | 0.999 |

($r=1$; checked by best-response iteration.) By Result 5 almost nothing is burnt on such matters: this equilibrium is cheap and lopsided. It is [Galanter's (1974)] repeat players and one-shotters, and it needs no wealth advantage: the tenants could each be richer than the landlord.
Cast: with $M=10{,}000$ tenants and $\phi=0.2$ the landlord's share is 86% even against an unconstrained Alice.
The counter is pooling (K-f, the 10,000 residents): tenants represented by one provider amortise over $M'$ and the ratio becomes $(M/M')^{\phi r}$. So parity requires providers of comparable scale on both sides of each type of matter. Against K-j: the economy of scale here is not a network effect; it is the reuse of bargaining work, and it pushes representation toward a few large providers. A principal's strength then depends on her provider's scale in that type of matter, a third argument of the production function that is neither her compute nor her endowment. (Conjecture about market structure; the share formula is the theorem.)

## 10. The size of the game is a choice

Section 6 gave two regimes. Formalise: a matter is contracted at detail $n$ (number of contingencies the contract distinguishes; K-k's "hyper-granular"). Solving it outright takes compute $G(n)=G_0\gamma^{n}$: $\gamma\approx7$ per unit of board size in Jones's Hex data; $\gamma=2$ for exhaustively checking $n$ binary contingencies ($2^n$ states). Effective compute is $\min\{c,G(n)\}$. Surplus $S(n)$ rises with detail, say $S(n)=\bar S(1-\delta^{n})$, $0<\delta<1$.

- If both sides can afford $G(n)$ the split is at merit and extra compute is worthless. Krier's satiation is real for a game of fixed size.
- Affordable detail grows only logarithmically: the largest solvable $n$ is $\log_\gamma(C/G_0)$. A million-fold fall in the price of compute adds at most $\log_7 10^6\approx7$ units at Hex's rate, or $\log_2 10^6\approx20$ binary contingencies. Hyper-granularity is bounded by the logarithm of the budget.
- With unequal budgets $c_i<c_j$ and $j$ proposing, $j$ gains twice from choosing $n$ beyond what $i$ can solve ($n>n_i=\log_\gamma(c_i/G_0)$): a larger $S(n)$, and a share above merit, $s_j=e_j^{\,r}/(e_j^{\,r}+c_i^{\,r})$ with $e_j=\min\{c_j,G(n)\}$. The game played is sized to the stronger party; the weaker one never reaches the flat part of the curve.
- The literature has the same mechanism without the compute: [Gabaix and Laibson (2006)] on shrouded terms and [Carlin (2009)] on strategic complexity in retail finance; [Tirole (2009)] models thinking about contingencies before signing as costly and partly rent-seeking, so that contracts can be more complete than is socially worthwhile; and [Arora, Barak, Brunnermeier and Ge (2011)] show a drafter of financial derivatives can plant unfavourable terms whose detection is computationally intractable for the buyer (as hard as finding a planted dense subgraph), so drafter and reviewer face different costs at the same $n$. [Larson and Sandholm (2001)] and [Halpern and Pass (2015)] are the formal treatments of bargaining and games when computation is costly.
- Remedy: a right to a standard form. Any party may insist on a contract of detail at most $\bar n$, with $G(\bar n)$ inside the basic compute allocation. On those matters both sides can solve the game, $r$ is effectively 0, there is no contest and no waste. The cost is the surplus given up, $S(n)-S(\bar n)=\bar S(\delta^{\bar n}-\delta^{n})$ per matter. This is the one remedy here that reduces waste and inequality together. It is a restriction on freedom of contract (it repeals C6), i.e. a planner regulating the complexity of bargains instead of their outcomes.

## 11. Stakes are not fixed: threats

Everything so far treated $E_i$ as given. Suppose $j$ can take a lawful act that costs $j$ $\kappa>0$, harms $i$ by $h>0$ and has no other use. Without a way to commit, $j$ never takes it. With cheap commitment (the escrows and automatic enforcement of K-h) $j$ can bind itself to act unless paid. That creates a matter with surplus $h+\kappa$. Relative to a world where the threat was never made, $i$ loses and $j$ gains $s_jh-s_i\kappa$ (positive iff $s_j/s_i>\kappa/h$), and the contest over the split burns compute on a matter of size $h+\kappa$ that created nothing.
Finding such acts is a search over what the law permits. Property rights are an incomplete contract ([Grossman and Hart 1986]; [Hart and Moore 1990]): they cannot list every act, and whoever can afford the search finds the gaps. So $i$'s stakes rise with other principals' compute.
C2 does not help: refusing means the act is carried out.
This is the one mechanism in the article that leaves a principal worse off than in a world with no bargaining at all. [Daly and Giertz (1975)] is the classic statement of extortion in Coasean bargaining; [Ngo (2026)] objects to Krier on related grounds (credible threats as a blind spot of efficiency reasoning).
Remedy: a rule against acts taken in order to be bought off, which requires a court to judge purpose.

## 12. Matters with many parties (brief; not the special angle, say so)

K-f and K-g. Two separate limits.
Computational: for a general $N$-party bargain the number of ways to partition the parties into coalitions lies between $N^{N/2}$ and $N^{N}$, and [Sandholm et al. (1999)] show that any guarantee on the quality of the partition found requires examining at least $2^{N-1}$ of them; [Deng and Papadimitriou (1994)] give hardness results in $N$ for the standard cooperative solution concepts; [Conitzer and Sandholm (2002)] for designing the mechanism itself. These are worst cases; real disputes have structure. A $k$-fold increase in compute adds $\log_2k$ parties to what is solvable in the worst case.
Informational: [Mailath and Postlewaite (1990)] show that with private valuations, voluntary participation and no outside subsidy, the probability that an efficient $N$-party agreement is reached goes to zero as $N$ grows, for any mechanism at all ([Myerson and Satterthwaite 1983] is the two-party case). Compute does not appear in the theorem. Krier's own remedies at this point (Harberger-style fees on stated valuations, compulsory reimbursement by vetoing coalitions) are compulsory, which is the theorem's way out. For our purposes: this component of the production function is flat in compute. [Dixit and Olson (2000)] is the related participation result.

## 13. The tally (this table is the answer to Dan's special-angle question; give it room)

| | implied by Krier's good outcome | in the models here |
|---|---|---|
| own compute | no effect above a small fixed $\bar c$ | raises income with elasticity $r(1-s)/(1+r(1-2s))$ ($\tfrac12$ at $r=1$) until $Rw_i\ge rE_i/4$; none above that |
| the threshold | fixed in compute units, so its cost $p\bar c\to0$ | fixed in dollars as a fraction of stakes; in compute units grows as $1/p$ |
| others' compute | no effect | lowers income; scaling all budgets together changes nothing |
| total compute | adds to total surplus | discovery compute adds, and its cost vanishes as $p\to0$; claiming compute subtracts $r/2$ of surplus at equal strength, at any $p$ |
| initial endowment | sets entitlements only | also sets the share, $\sqrt{Rw_i/E_i}$ below the threshold; with subsistence needs, a trap below $w_-$ |
| scale | none | repeat player's share $M^{\phi r}/(1+M^{\phi r})$ |
| cost of a subsidy for fair shares | vanishes with $p$ | $(rE_i/4R-w_i)^+$ per head per period at any $p$, and raises waste |
| contract detail | unlimited ("hyper-granular") | at most $\log_\gamma$ of the budget; chosen by the stronger party |
| many parties | coalition "in a nanosecond" | efficient agreement fails for large $N$ at any compute |

## 14. Is it a good world? (Dan's question; answer it directly and with calibrated confidence)

- Compared with no bargaining: better, for everyone, in sections 7–10, because a principal can always refuse and keep the entitlement. Section 11 is the exception.
- Compared with the benchmark, at $r=1$: the comfortable get the benchmark's shares at the cost of half the surplus; the liquidity-constrained get square-root shares; some fall below a threshold and stay there; representation concentrates; the stronger side sets the complexity.
- All of it turns on $r$. At $r=0$ every result collapses to the benchmark. What makes $r=0$ is a game small enough for both sides to solve.
- So the remedies that work bound the game: standard forms (section 10), fixed bargaining protocols, a verifiable cap on compute per matter if one can be built, a rule against manufactured threats (section 11), proposal bonds (8d). Each is a rule about bargaining technique made and enforced by someone who is not a party: a planner's rule. Krier's state enforces contracts and entitlements (K-i); this one must also regulate how bargaining is done.
- A caution on caps: [Che and Gale (1998)] show that capping contest spending can *raise* total spending when contestants value the prize differently (in the all-pay-auction case). A compute cap is not obviously safe.
- What would change the conclusion, stated as tests: measure the share as a function of compute ratio for bargaining agents at fixed model, i.e. estimate $r$ (the Project Deal design with compute varied instead of model); find out whether agents can verify one another's compute use; solve the $r>1$ case; add risk aversion; add a credit market for compute.
- Limitations to state: the contest success function is imported from board games, not measured in bargaining; risk neutrality; linear returns $R$; $\theta=\tfrac12$ throughout the multi-matter results; the constrained principal is assumed small relative to its opponents (so their shadow prices do not move); no repeated-game cooperation; one simulation parameter set; the subsidy in the simulation is unfunded.

## 15. Other responses to Krier (one short paragraph, placed where it fits, so nothing is reprised without credit)

[Petel (2025)] argues for constitutional non-negotiables, hardened identity and verification, and limits on platform power. [Sharp et al. (2025)] name "agentic inequality" and classify it by availability, quality and quantity of agents, without an equilibrium model. [Ngo (2026)] argues that efficiency framings neglect autonomy and credible threats. [Shahidi et al. (2025)] survey market design with agents and flag congestion and obfuscation. What this article adds is an equilibrium account of how much is spent and who gets what, and the comparison of production functions.

## 16. References (the only ones you may cite; link text → URL)

- Krier (2025), Coasean Bargaining at Scale — https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale
- Coase (1960), The Problem of Social Cost — https://doi.org/10.1086/466560
- Jones (2021), Scaling Scaling Laws with Board Games — https://arxiv.org/abs/2104.03113
- Anthropic (2026), Project Deal — https://www.anthropic.com/features/project-deal
- Zhu et al. (2025), The Automated but Risky Game — https://arxiv.org/abs/2506.00073
- Skaperdas (1996), Contest success functions — https://doi.org/10.1007/BF01213906
- Hirshleifer and Osborne (2001), Truth, Effort, and the Legal Battle — https://doi.org/10.1023/A:1017520505573
- Fullerton and McAfee (1999), Auctioning Entry into Tournaments — https://doi.org/10.1086/250072
- Rubinstein (1982), Perfect Equilibrium in a Bargaining Model — https://doi.org/10.2307/1912531
- Tullock (1980), Efficient Rent Seeking — https://doi.org/10.1007/978-1-4757-5055-3_2 (2001 reprint of the 1980 chapter)
- Posner (1975), The Social Costs of Monopoly and Regulation — https://doi.org/10.1086/260357
- Baye, Kovenock and de Vries (1994), The solution to the Tullock rent-seeking game when R>2 — https://doi.org/10.1007/BF01053238
- Lax and Sebenius (1986), The Manager as Negotiator (book, Free Press; no link)
- Friedman (1958), Game-Theory Models in the Allocation of Advertising Expenditures — https://doi.org/10.1287/opre.6.5.699
- Franke and Öztürk (2015), Conflict networks — https://doi.org/10.1016/j.jpubeco.2015.04.002
- Xu, Zenou and Zhou (2022), Equilibrium characterization and shock propagation in conflict networks — https://doi.org/10.1016/j.jet.2022.105571
- Hirshleifer (1991), The Paradox of Power — https://doi.org/10.1111/j.1468-0343.1991.tb00046.x
- Anderlini and Felli (2006), Transaction Costs and the Robustness of the Coase Theorem — https://doi.org/10.1111/j.1468-0297.2006.01054.x
- Shahidi, Rusak, Manning, Fradkin and Horton (2025), The Coasean Singularity? — https://doi.org/10.3386/w34468
- Galanter (1974), Why the "Haves" Come Out Ahead — https://doi.org/10.2307/3053023
- Gabaix and Laibson (2006), Shrouded Attributes — https://doi.org/10.1162/qjec.2006.121.2.505
- Carlin (2009), Strategic price complexity in retail financial markets — https://doi.org/10.1016/j.jfineco.2008.05.002
- Tirole (2009), Cognition and Incomplete Contracts — https://doi.org/10.1257/aer.99.1.265
- Arora, Barak, Brunnermeier and Ge (2011), Computational complexity and information asymmetry in financial products — https://doi.org/10.1145/1941487.1941511
- Larson and Sandholm (2001), Bargaining with limited computation — https://doi.org/10.1016/S0004-3702(01)00132-1
- Halpern and Pass (2015), Algorithmic rationality — https://doi.org/10.1016/j.jet.2014.04.007
- Grossman and Hart (1986), The Costs and Benefits of Ownership — https://doi.org/10.1086/261404
- Hart and Moore (1990), Property Rights and the Nature of the Firm — https://doi.org/10.1086/261729
- Daly and Giertz (1975), Externalities, Extortion, and Efficiency — https://www.jstor.org/stable/1806636
- Ngo (2026), Economic efficiency often undermines sociopolitical autonomy — https://www.mindthefuture.info/p/economic-efficiency-often-undermines
- Sandholm, Larson, Andersson, Shehory and Tohmé (1999), Coalition structure generation with worst case guarantees — https://doi.org/10.1016/S0004-3702(99)00036-3
- Deng and Papadimitriou (1994), On the Complexity of Cooperative Solution Concepts — https://doi.org/10.1287/moor.19.2.257
- Conitzer and Sandholm (2002), Complexity of Mechanism Design — https://arxiv.org/abs/cs/0205075
- Mailath and Postlewaite (1990), Asymmetric Information Bargaining Problems with Many Agents — https://doi.org/10.2307/2298018
- Myerson and Satterthwaite (1983), Efficient mechanisms for bilateral trading — https://doi.org/10.1016/0022-0531(83)90048-0
- Dixit and Olson (2000), Does voluntary participation undermine the Coase Theorem? — https://doi.org/10.1016/S0047-2727(99)00089-4
- Che and Gale (1998), Caps on Political Lobbying — https://www.jstor.org/stable/116854
- Petel (2025), Price What You Can, Protect What You Must — https://mateopetel.substack.com/p/price-what-you-can-protect-what-you
- Sharp et al. (2025), Agentic Inequality — https://arxiv.org/abs/2510.16853
- Tomašev et al. (2025), Virtual Agent Economies — https://arxiv.org/abs/2509.10147
