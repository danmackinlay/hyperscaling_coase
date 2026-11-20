# An Evolutionary Model of Bargaining

H. Peyton  Young

SFI WORKING PAPER:  1992-02-009

SFI Working Papers contain accounts of scientific work of the author(s) and do not necessarily represent the
views of the Santa Fe Institute.  We accept papers intended for publication in peer-reviewed journals or
proceedings volumes, but not papers that have already appeared in print.  Except for papers by our external
faculty, papers must be based on work done at SFI, inspired by an invited visit to or collaboration at SFI, or
funded by an SFI grant.

©NOTICE: This working paper is included by permission of the contributing author(s) as a means to ensure
timely distribution of the scholarly and technical work on a non-commercial basis. Copyright and all rights
therein are maintained by the author(s). It is understood that all persons copying this information will
adhere to the terms and constraints invoked by each author's copyright. These works  may  be reposted only
with the explicit permission of the copyright holder.

www.santafe.edu

---

# AN EVOLUTIONARY MODEL OF BARGAINING*

H. Peyton Young

School of Public Affairs/Department of Economics
University of Maryland
College Park, MD 20742

November, 1989
Revised September, 1991

* This work was supported by the Santa Fe Institute and by the Office of Naval Research under Contract N00014-89-J-1491. The author is indebted to Brian Arthur, David Canning, Ariel Rubinstein, and two anonymous referees for comments on an earlier draft. Special thanks go to Dean Foster for providing suggestions and criticisms along the way.

---

## Abstract

Classical bargaining theory predicts that when two agents bargain over how to divide a fixed pie, their shares will reflect their alternatives to agreement and aversion to risk. In practice, however, rational bargainers often rely on uniform customs like dividing fifty-fifty. We propose a dynamical model to explain this phenomenon. The essential idea is that bargainers' expectations are shaped by past bargains. This reliance on precedent creates a positive feedback loop that eventually drives expectations toward a fixed division, which then becomes the "customary" solution. When this dynamical process is subjected to small stochastic fluctuations, some divisions are much more likely than others to be observed in the long run. These stable divisions can be computed directly from the agents' utility functions. When the population consists of two disjoint classes of agents, and all agents in the same class have the same utility function, the stable outcome is the Nash solution. When the population consists of two heterogeneous classes of agents, the stable outcome depends on the utility functions represented within each class. If there is some mixing between the two classes, the stable division is fifty-fifty.

---

## 1. Introduction

Classical bargaining theory holds that bargains between rational agents depend solely on the agents' utilities for the outcomes, not the outcomes themselves. As Nash put it: "What the actual courses of action are among which the individuals must choose is not regarded as essential information . . . Only the attitudes (like or dislike) of the two individuals towards the ultimate results are considered." [Nash, 1950]. Not only are classical solutions like Nash, Raiffa, and Kalai-Smorodinsky utilitarian in conception, implementing them generally requires that the utility functions be common knowledge, or at least that they be known to an arbitrator.<sup>1</sup> Yet it is common knowledge that utility functions are often not common knowledge. In practice, bargainers do not rely on detailed calculations involving others' utility functions. Instead, they look for concrete features of the situation that are known to everybody and that can serve as coordination devices. Such "focal points" may be idiosyncratic to a particular case, like a river that runs down the center of a disputed territory [Schelling, 1960]. Or they may reflect social customs that have arisen to deal with similar cases. A well-known example is dividing a homogeneous good fifty-fifty when the parties are similarly situated.

A curious fact about fifty-fifty division is that it is also customary even when the parties are not similarly situated. Consider a tenant who enters into a sharecropping contract with a landlord. The contract specifies the fractional shares of the harvest for each, so it is a pure distributive bargaining problem. Clearly the tenant and the landlord are not in the same position, however. They contribute different inputs to the bargain (labor and land), and doubtless they have different opportunities should they fail to agree. Yet fifty-fifty appears to be the most common sharecropping rule in many societies.<sup>2</sup> Why should this be?

One explanation is that fifty-fifty is the natural focal point for the bargainers, because every other solution is in competition with its mirror image. A second argument is that fifty-fifty is perceived to be fair, and parties to long-run relationships have an interest in treating each other fairly. Yet it is not clear that equal division is all that fair (or even all that focal) in situations like sharecropping where the bargainers are clearly in asymmetric roles. Moreover, fifty-fifty is not the customary division everywhere. In some communities the custom is 2/3 for the landlord, 1/3 for the tenant, in others it is 3/4 for the landlord, 1/4 for the tenant, in still others it is 11/20 for the landlord and 9/20 for the tenant, and so forth. The pattern seems to be that most agricultural communities rely on some

<sup>1</sup> Nash (1950); Raiffa (1953); Kalai and Smorodinsky (1975); Rubinstein (1982).
<sup>2</sup> My sources are Bardhan (1984) and Robertson (1987).

---

custom, that customs vary from one community to another, and the most widespread custom is fifty-fifty [Bardhan, 1984; Robertson, 1987].

In this paper we propose a dynamical model to explain how such customs arise, and why some customs (like fifty-fifty) are inherently more stable than others. The essential idea is that bargainers' expectations are shaped by precedent. Each bargainer has limited information about what other bargainers have demanded in past encounters. Each chooses a best reply assuming that these precedents are a reasonable predictor of what other agents are going to demand now. There is no common knowledge. When agents look at different precedents or the precedents conflict, their responses will very likely be uncoordinated. However, it may happen that a succession of bargainers coordinate by chance on the same rule over a period of time. This establishes (by chance) a set of common precedents and common expectations. People begin to expect that similar bargains will be solved by this rule in the future. Under circumstances that we shall describe below, this positive feedback loop eventually drives society toward a fixed division. It becomes the norm, not because it is inherently "focal," but because early chance events happened to favor it and now everyone expects it.

Of course, a given rule does not remain entrenched forever. Changing economic circumstances may eventually cause the shares to shift in favor of one party or another. Furthermore, there will inevitably be some variability in bargaining outcomes due to differences in agents' behavior and beliefs. When these stochastic influences are included, the long-run behavior of the evolutionary process becomes more complex. In particular, it has no absorbing states. A rule of division will remain in use for a time, after which it will be displaced by another rule. These displacements are irregular and infrequent, but they occur quite rapidly when they do occur. The process then settles down to another period of relative tranquillity in which a fixed rule is in force. We cannot predict which rule will be in use at any given time because of the stochastic nature of the process. Nevertheless we can say that some rules are more likely to be observed than others over the long run. In fact, when the stochastic perturbations are very small, there typically exists one rule that will be observed with probability close to one. This stable rule can be calculated explicitly. It depends on the agents' utility functions, but oddly enough it does not depend (very much) on the details of the stochastic perturbations, so long as they are small.

When each class of agents is homogeneous (e.g., all landlords have the same utility function and all tenants have the same utility function), the long-run stable rule is the Nash solution. When each class is heterogeneous the stable outcome depends on the utility functions represented in each class, but not on their distribution. We therefore obtain a generalization of the Nash bargaining solution that depends on two sets of utility functions, one for each class. If there is some mixing between the classes, then the utility functions represented in each class are the same, and the long-run stable outcome is fifty-fifty.

## 2. The model.

Consider two finite, nonempty classes of individuals A and B. To be concrete we shall think of A as the class of landlords and B as the class of tenants. In each period, one landlord meets one tenant and they bargain over their shares of the crop. The share of the landlord will generically be denoted by $a$, and the share of the tenant by $b$. For technical reasons we are going to assume that all shares are rational fractions with some fixed common denominator $d$, where $d$ is a positive integer. If $d = 100$, for example, then the shares consist of all fractions rounded to the second decimal. $D = \{n/d : 0 \leq n/d \leq 1, n \text{ integer}\}$ is the set of feasible shares, and $\delta = 1/d$ is the precision of the shares.

The bargaining process has the following structure.<sup>3</sup> In each period $t = 1, 2, \ldots$, one landlord $\alpha$ is drawn at random from the class A and one tenant $\beta$ is drawn at random from the class B. They then play the Nash demand game: $\alpha$ demands some fraction $a \in D$, $\beta$ demands some fraction $b \in D$, and they get their demands if $a + b \leq 1$; otherwise they get zero.

Let the demands in period $t$ be denoted by $(a_t, b_t)$. The complete history up to and including period $t$ is the sequence $(a_1, b_1), (a_2, b_2), \ldots, (a_t, b_t)$.

Suppose that agents $\alpha$ and $\beta$ are chosen in period $t + 1$. Assume that neither party has prior knowledge or beliefs about the utility function of the other side, or about the distribution of the utility functions in the general population. To decide what to do they look at recent precedents. Agent $\alpha$ draws a random sample of $k_\alpha$ items from the last $m$ records $s = ((a_{t-m+1}, b_{t-m+1}), \ldots, (a_t, b_t))$. $k_\alpha$ is a measure of $\alpha$'s information, an inherent characteristic of the agent.

Agent $\alpha$ then chooses an optimal reply to the observed frequency distribution of the demands made by tenants in the sample drawn. More precisely, $\alpha$ forms the cumulative probability distribution $F(b)$ of the demands $b_j$ made by tenants in his sample:

<sup>3</sup> This is a specific application of a general model of equilibrium selection in which two populations play a repeated game by random matching [Young (1991).

---

∀b ∈ D F(b) = j/kα iff there are exactly j observations bj in the sample such that bj ≤ b.

F is a random variable that depends on the particular sample that α happened to draw at time t + 1.

Agent α is assumed to have a von Neumann Morgenstern utility function uα(a) for his own share a, where uα(a) is concave and strictly increasing in a. The utility function is normalized so that uα(0) = 0. We shall assume that uα(a) is defined for all a ∈ [0, 1], because later on we shall want to treat the level of precision δ as a variable.

If α demands a and the tenant demands b, then α gets a if b ≤ 1 - a and zero otherwise. Thus α believes his expected payoff (given the observed cumulative distribution F) is

uα(a) F(1 - a) + uα(0) (1 - F(1 - a)) = uα(a) F(1 - a).

We assume that α chooses an amount a_{t+1} in period t + 1 that maximizes his expected payoff:

a_{t+1} = argmax uα(a) F(1 - a). (1)

If there are several values of a that maximize (1), then α chooses each of them with positive probability.

The tenant behaves similarly: β draws kβ items at random from the last m plays, and chooses an optimal response to the observed distribution of demands made by the landlords in her sample. All best replies are chosen with positive probability. The probability distribution over best replies may depend on the sample, but it is stationary over time. The process is therefore a variation of fictitious play in which each agent reacts to a sample of the opponents' recent moves, rather than to all of the opponents' past moves.

To emphasize that convergence in this model is not going to depend on any dynamic learning process at the individual level, we are going to assume that after two individuals play they die and are replaced by agents of the same type as their forebears. Each has the same information-gathering propensity and the same utility function as its parent but not the parent's information. Thus each time an agent plays he starts afresh and must ask around to find out what is going on.

---

The agents' response rules determine a stationary Markov chain. The state space S consists of all sequences of length m whose elements are pairs (a, b) ∈ D x D. Let pα(a | s) be the conditional probability that α demands a given that the state is s, and let pβ(b | s) be the conditional probability that β demands b given that the state is s. We assume that pα(a | s) > 0 if and only if a is a best reply by α to a sample of size kα drawn from s, and pβ(b | s) > 0 if and only if b is a best reply by β to a sample of size kβ drawn from s. This allows for a nonuniform probability of drawing different samples. (For example, recent samples might be more likely to be drawn than older samples.) All that matters is that any appropriate-sized sample could be drawn, any best reply to such a sample could be made, and the probability of these events (conditional on the state) is stationary.

The process begins at time t = m in some arbitrary initial state s0, that is, some arbitrarily chosen sequence of m pairs from D x D. (This is more general than assuming that the process begins at time t = 1 with a randomly chosen pair (a, b).) Assume that every pair (α, β) ∈ A x B is equally likely to be selected to bargain in every period. Given a state s = (a_t-m+1, b_t-m+1), ..., (a_t, b_t) we say that s' is a successor of s if it has the form s' = ((a_t-m+2, b_t-m+2), ..., (a_t, b_t), (a_t+1, b_t+1)). If the process is in state s at time t, then it moves to the successor state s' at time t + 1 with transition probability

$$P_{ss'} = \frac{(1/|A| |B|)}{\alpha \in A \beta \in B}$$

If s' is not a successor of s, then $P_{ss'} = 0$. This process will be called the evolutionary bargaining process with precision δ, memory m, information parameters {kα, kβ} and best reply distributions {pα, pβ}.

3. Asymptotic behavior of the evolutionary bargaining process.

CONVENTION. A state s is a convention if it consists of some fixed division (a, 1 - a) repeated m times in succession, where 0 < a < 1.

By a slight abuse of notation we shall denote this convention by (a, 1 - a). We claim that every convention is an absorbing state of the process P defined by (2). Suppose, indeed, that at time t the process is in the convention (a, 1 - a). Let α and β be an arbitrary landlord and tenant who bargain in period t + 1. In every sample drawn by the landlord, the previous tenants always demanded 1 - a, so the landlord's unique optimal reply is a > 0. Similarly, in every sample drawn by the tenant, the previous landlords always demanded a, so the tenant's unique optimal reply is 1 - a > 0. (Note that the best replies are only unique if 0 < a < 1.) Thus the optimal demands in period t + 1 are (a, 1 - a), so the state in period t + 1 is the same as in period t.

Let k be the larger of minα∈A kα and minβ∈B kβ. k is the critical sample size. We shall show that, if k is not too large relative to memory, then the process P converges with probability one.

THEOREM 1. If k ≤ m/2, then from any initial state the evolutionary bargaining process converges with probability one to a convention.

PROOF. We shall prove that there exists a positive integer N and a positive probability p (both independent of t) such that, from any state s, the probability of converging to a convention within N steps is at least p. Thus the probability of not reaching a convention within rN steps is at most $(1 - p)^r$. This goes to zero as r → ∞, so the process eventually converges to a convention with probability one.

To prove this, consider an arbitrary state s = ((a_t-m+1, b_t-m+1), . . . , (a_t, b_t)) at time t ≥ m. Without loss of generality let k = minα∈A kα and k* = minβ∈B kβ, where k ≥ k*. Fix two agents α and β, where α has sample size k and β has sample size k*. There is a positive probability that two agents like α and β will be selected to play the Nash demand game in every period from t + 1 to t + k inclusive. There is also a positive probability that α will draw the same sample σ = ((a_t-k+1, b_t-k+1), . . . , (a_t, b_t) in each of these periods, and that β will draw the (possibly smaller) sample σ* = ((a_t-k*+1, b_t-k*+1), . . . , (a_t, b_t) in each of these periods. Let a and b be best replies to this sample by α and β respectively. There is a positive probability that α will always demand a, and that β will always demand b from periods t + 1 to t + k inclusive. Hence there is a positive probability of obtaining a run τ = ((a, b), . . . , (a,b)) from periods t + 1 to t + k inclusive.

From periods t + k + 1 to t + 2k there is a positive probability that two agents like α and β will be selected to play every time, and that both of them will always draw from the run τ. (Thus α draws the sample τ itself and β draws a sample of k* items from τ.) Their unique best replies are (1 - a, 1 - b), so we obtain a run τ' = ((1 - b, 1 - a), . . . , (1 - b, 1 - a)) from periods t + k + 1 to t + 2k inclusive.

In period t + 2k + 1, there is a positive probability that a landlord like α will be chosen again and that she draws the sample τ, and also that a tenant like β will be chosen again and that he draws the sample $ \tau^{*} $ consisting of the last k* items in $ \tau^{\prime} $ . Their best replies are then (1-b,b). Note that this requires $ \alpha $ to look back 2k periods, and $ \beta $ to look back k* periods, both of which are possible by hypothesis on m.

$$
t^{*}
$$

$$
\mathbf{k}^{*}
$$

$$
\tau^{\prime}.
$$

$$
\beta
$$

$$
\mathbf{k}^{*}
$$

In period t+2k+2, however, the oldest record in $ \tau $ may have disappeared (if m=2k ). Nevertheless, $ \alpha $ can still draw a sample of size k in which the other side always played b , namely, the most recent k-1 plays in $ \tau $ and the play in the preceding period （t+2k+1）. Meanwhile $ \beta $ can still look at the sample $ \tau^{*} $ because none of these records has disappeared. So there is a positive probability that the best replies in period t+2k+2 will again be (1-b,b).

$$
\beta
$$

$$
t^{*}
$$

Continuing in this manner, we see that there is a positive probability of obtaining a run of (1 - b, b) for m periods in succession, at which point a convention has been reached. It follows that, from a given initial state s, there is a positive probability (possibly depending on the initial state s) of reaching a convention within $ 2 k+m $ periods. Since the number of states is finite, there is a positive probability p (independent of the initial state) of reaching a convention within $ 2 k+m $ periods. This concludes the proof of Theorem 1.

We do not claim that the bound k $ \leq $ m/2 is best possible, but we do claim that incomplete sampling is necessary for this result. Consider the following example. All agents in A have a concave utility function u and all agents in B have a concave utility function v, where u and v have the following values on divisions by 4:

$$
k\leq m/2
$$

| Share x | 0 | 1/4 | 1/2 | 3/4 | 1 |
| --- | --- | --- | --- | --- | --- |
| u(x) | 0 | .3 | .4√2 | .8 | 1 |
| v(x) | 0 | .5 | .5√2 | .9 | 1 |

Suppose that both agents take complete samples, and that the previous demands were either (3/4, 1/2) or (1/2, 1/4). Thus they miscoordinated every time. At time t let $ f_{t} $ be the relative frequency with which the pair (3/4, 1/2) was played in the preceding m periods, and let 1 - $ f_{t} $ be the relative frequency with which (1/2, 1/4) was played in the preceding m periods. The landlord's best reply is 3/4 if and only if

$$
\mathbf{f}_{\mathbf{t}}
$$

$$
1-f_{t}
$$

$$
(1-\mathrm{f}_{\mathrm{t}})\mathrm{u}(3/4)\geq\mathrm{u}(1/2)
$$

Similarly, the tenant's best reply is 1/2 if and only if

---

$$
(1 - f_t)v(1/2) \geq v(1/4),
$$

These hold if and only if $f_t \leq 1 - 1/\sqrt{2}$; moreover the inequality is always strict because $f_t$ is rational. Thus the demands in period $t + 1$ are either $(3/4, 1/2)$ or $(1/2, 1/4)$. It follows that if the agents begin in any state where they have always miscoordinated, then they continue to miscoordinate forever.

## 4. Mistakes and experimentation

The evolutionary bargaining process defined in (2) is based on the assumption that agents always choose best replies given their information. A more realistic assumption is that agents sometimes make mistakes or experiment with other choices. The more general case is to suppose that the agents experiment, which may or may not involve making "mistakes."

Let $\varepsilon\lambda_\alpha$ be the probability that agent $\alpha$ experiments in any given period, and let $q_\alpha(a|s)$ be the conditional probability that $\alpha$ chooses the reply $a$, given that $\alpha$ is experimenting and that the current state is $s$. Similarly define $\varepsilon\lambda_\beta$ and $q_\beta(b|s)$ for every $\beta \in B$. We assume that $q_\alpha(a|s)$ and $q_\beta(b|s)$ have full support, that is, all choices or trembles are possible in any given state. The parameters $\lambda_\alpha > 0$ and $\lambda_\beta > 0$ define the relative probabilities with which particular agents experiment, and the factor $\varepsilon$ determines the absolute probability with which agents in general experiment.<sup>4</sup> This yields a stationary Markov chain on $S$ in which the probability of moving from state $s = ((a_{t-m+1}, b_{t-m+1}), \ldots, (a_t, b_t))$ at time $t \geq m$ to the successor state $s' = ((a_{t-m+2}, b_{t-m+2}), \ldots, (a_{t+1}, b_{t+1})$ at time $t + 1$ is

$$P^\varepsilon_{ss'} = \frac{(1/|A| |B|)}{\sum_{\alpha \in A} \sum_{\beta \in B}} [(1 - \varepsilon\lambda_\alpha)(1 - \varepsilon\lambda_\beta) p_\alpha(a|s) p_\beta(b|s)$$
$$+ \varepsilon\lambda_\alpha(1 - \varepsilon\lambda_\beta) q_\alpha(a|s) p_\beta(b|s) + \varepsilon\lambda_\beta(1 - \varepsilon\lambda_\alpha) p_\alpha(a|s) q_\beta(b|s)$$
$$+ \varepsilon^2\lambda_\alpha\lambda_\beta q_\alpha(a|s) q_\beta(b|s)].$$

$P^\varepsilon_{ss'} = 0$ if $s'$ is not a successor of $s$. For each $\varepsilon > 0$ the process $P^\varepsilon$ will be called the perturbed evolutionary bargaining process. Note that the unperturbed process $P^0$ is the same as the process $P$ defined in (2). We are going to show that the asymptotic behavior of $P^\varepsilon$ is more or less independent of the distributions $p_\alpha, p_\beta, q_\alpha, q_\beta$, so long as $\varepsilon$ is sufficiently small. Moreover (except in case of

<sup>4</sup> This model of independent mistakes generalizes an idea first proposed by Kandori, Mailath and Rob (1991).

---

ties) the process selects exactly one division, which will be observed almost all of the time in the long run. This "stable" division can be computed directly from the utility functions represented in the population.

The model described above differs in several respects from other models of equilibrium selection based on stochastic trembles or noise. In his 1953 paper, for example, Nash suggested that his bargaining solution is the unique (limiting) outcome of the Nash equilibria of a perturbed version of the Nash demand game in which there is a small uncertainty in the payoffs [Nash, 1953]. A more rigorous argument along these lines was provided by Binmore (1987). In a recent paper Carlsson (1991) investigated variations of the Nash demand game in which agents' demands are modified by a small error term. He showed that the Pareto optimal Nash equilibria of this noncooperative game converge to the Nash solution as the error term becomes vanishingly small.

These models of equilibrium stability differ from the present one in that they are static: they presuppose that the outcome of the perturbed game is a Nash equilibrium; they do not describe how the equilibrium is arrived at. To justify this approach, it must be assumed (among other things) that the properties of the game are common knowledge to the agents. In our model, by contrast, there is no common knowledge and no assumption that a Nash equilibrium will be played. Instead, equilibrium (in an asymptotic sense) emerges as a consequence of the long-run dynamics.

## 5. Asymptotic behavior of the perturbed evolutionary bargaining process.

Fix all parameters in the process (2) except for the overall probability of mistakes $\varepsilon$, which will be allowed to vary in the open interval $[0, 1)$. Let this process be denoted by $P^{\varepsilon}$. We are going to characterize the limiting distribution of $P^{\varepsilon}$ as $\varepsilon$ tends to zero.

We begin by showing that the process $P^{\varepsilon}$ is irreducible and aperiodic whenever $\varepsilon > 0$. Suppose that the process is in state $s$ at time $t$. Consider any other state $s' = ((a', b'), (a''', b'') \ldots, (a^*, b^*))$. There is a positive probability that the agents chosen to play in period $t + 1$ will choose the pair $(a', b')$. (This uses the assumption that the experimental distributions $q_{\alpha}, q_{\beta}$ have full support.) Similarly, there is a positive probability that the agents chosen in period $t + 2$ will choose the pair $(a''', b'')$. Continuing in this manner, we see that there is a positive probability that the process will move from any given state $s$ to any other state $s'$ in exactly $m$ periods. Hence the process is irreducible. A similar argument shows that there is a positive probability that it will first arrive at state $s'$ in $m + 1$ periods (assuming that $s' \neq s$). Hence it is aperiodic.

---

It follows that $P^\varepsilon$ has a unique stationary distribution $\mu^\varepsilon$ for every $\varepsilon > 0$, where $\mu^\varepsilon$ satisfies the equation $\mu^\varepsilon P^\varepsilon = \mu^\varepsilon$ [Karlin and Taylor, 1975, Chapter 3]. For every $s \in S$, $\mu^\varepsilon_s$ is (with probability one) the relative frequency with which state $s$ will be observed after $t$ periods as $t \to \infty$. By contrast, the unperturbed process $P^0$ has many stationary distributions. In fact, every distribution whose support consists solely of conventions is a stationary distribution of $P^0$ when $k \leq m/2$.

It can be shown that, as $\varepsilon \to 0$, $\mu^\varepsilon_s$ converges to a distribution $\mu^0_s$ for each state $s$; moreover $\mu^0$ is one of the stationary distributions of $P^0$ [Young, 1991, Theorem 4]. The perturbations therefore select among the stationary distributions of $P^0$. Furthermore, as we shall see below, the selected distribution typically puts all the weight on exactly one convention (or on a small subset of them). In this sense the process selects among the conventions.

STABLE CONVENTION. A convention $s$ is stable if $\lim_{\varepsilon \to 0} \mu^\varepsilon_s > 0$. It is strongly stable if $\lim_{\varepsilon \to 0} \mu^\varepsilon_s = 1.6$

Over the long run, stable conventions will be observed much more frequently than unstable conventions when the probability $\varepsilon$ of the perturbations is small. A strongly stable convention will (if it exists) be observed almost all of the time when $\varepsilon$ is small.

Before showing how to compute the stable conventions in particular cases, let us first consider the qualitative behavior of the evolutionary bargaining process when the noise level $\varepsilon$ is small. If agents never experiment ($\varepsilon = 0$), then Theorem 1 tells us that the process converges to a convention provided that $k \leq m/2$. These are the absorbing states of the unperturbed process. If the agents occasionally experiment, then the process has no absorbing states. It still gravitates towards them, but it does not come to rest because of the random fluctuations caused by experimentation. Nevertheless, the process is at or near an absorbing state (i.e., a convention) most of the time. Occasionally, a large accumulation of mistakes pushes the process away from a given convention and into the basin of attraction of another convention. The likelihood of such an event is small, but if we wait long enough, it is bound to occur. When it does, the process will gravitate towards the new convention,

---

5 A related result is proved by Canning (1991, Theorem 5).
6 This concept was introduced under the name "stochastic stability" for general stochastic dynamical systems by Foster and Young (1990). See also Young and Foster (1991), Young (1991), and Kandori, Mailath and Rob (1991).

---

where it will tend to stay for a long time before another large displacement occurs. The stable conventions are the ones that are hardest to displace. When the probability of experimentation is very small, the stable conventions will be observed almost all of the time because transitions to other conventions are extremely infrequent.

We shall now describe a general technique for computing the stable conventions.

MISTAKE. Let $s = ((a^1, b^1), (a^2, b^2), \ldots, (a^m, b^m))$ be some state and let $s' = ((a^2, b^2), \ldots, (a^m, b^m), (a, b))$ be a successor of $s$. $a$ is a mistake in the transition $s \rightarrow s'$ if, for every landlord $\alpha$, $a$ is not a best reply by $\alpha$ to any sample of size $k_\alpha$ drawn from $s$. Similarly, $b$ is a mistake if, for every tenant $\beta$, $b$ is not a best reply by $\beta$ to any sample of size $k_\beta$ drawn from $s$.

RESISTANCE. If $s'$ is a successor of $s$, the resistance $r(s, s')$ of the one-period transition $s \rightarrow s'$ is the minimum number of mistakes involved in the transition. Clearly $r(s, s') = 0, 1,$ or 2. For every two states $s$ and $s'$, the resistance $r(s, s')$ is the least total number of mistakes in any sequence of one-period transitions that leads from $s$ to $s'$.

To compute $r(s, s')$ one solves a shortest path problem in a directed graph, namely, the graph in which every state is a vertex and there is an edge from $s$ to $s'$ with weight $r(s, s')$ if and only if $s'$ is a successor of $s$.

For notational economy we shall denote the convention $(a, 1 - a)$ by $a$.

$a$-BASIN. For every $0 < a < 1$ the $a$-basin is the set of all states from which the unperturbed process $P^0$ converges to the convention $a$ with positive probability.

If $k \leq m/2$ and $\varepsilon = 0$, then (by Theorem 1) the conventions are the absorbing states of the unperturbed process, so every state is in at least one $a$-basin.

Let $G$ be a complete, directed graph in which each convention is a vertex, and the "weight" or resistance of each directed edge $a \rightarrow a'$ is the resistance of moving from the convention $a$ to the convention $a'$.

$a$-TREE. An $a$-tree is a spanning subtree of $G$ such that, from every convention $a' \neq a$, there exists exactly one directed path from $a'$ to $a$.

---

Let $T_a$ be the set of all $a$-trees.

STOCHASTIC POTENTIAL. The stochastic potential of the convention $a$ is the least resistance among all $a$-trees:

$$\rho(a) = \min \quad \sum r(a', a'')$$

$$T \in T_a \quad (a', a'') \in T$$

The following is a special case of Theorem 4 in Young (1991).

The stochastically stable states of the evolutionary bargaining process are precisely the conventions(s) that minimize $\rho(a)$.

We shall now apply this result to determine the stable conventions under various assumptions about the composition of the bargaining populations.

## 6. Homogeneous populations and the Nash solution

Let's begin with the special case in which every agent in class A has the same utility function $u$, and every agent in class B has the same utility function $v$. Assume further that there is an agent with minimum information in both classes, that is, there exist $\alpha \in A$ and $\beta \in B$ with information $k$, and no other agent has less information. We shall show that, if $k$ is large enough, the stable convention(s) are close to the Nash solution. More precisely, they are the Nash solution(s) on the set of feasible shares $D$.

DISCRETE NASH SOLUTION. Fix the precision $\delta = 1/d$ and let $D = \{n \delta : 0 \leq n \leq d, n \text{ integer}\}$. For every pair of concave, strictly increasing utility functions $u, v$ defined on $D$, the discrete Nash solution is the set of pairs $(a, b)$ that maximize $u(a)v(b)$ subject to $a, b \in D$ and $a + b \leq 1$.

The discrete Nash solution is the same as the ordinary Nash bargaining solution $(a^*, b^*)$ if the latter is in $D \times D$; otherwise, the discrete Nash solution consists of either one or two pairs in $D \times D$. Each discrete Nash solution $(a, b)$ lies within $\delta$ of the ordinary Nash solution in the sense that $|a - a^*| \leq \delta$ and $|b - b^*| \leq \delta$.

---

THEOREM 2. Let all agents in A have the same utility function u, let all agents in B have the same utility function v, and suppose that some agent in each class has minimum information k, where $k \leq m/2$. Then the discrete Nash solution(s) are stable, and for all sufficiently large k (and m) they are the only stable solutions.

The proof of Theorem 2 is accomplished via two lemmas.

For every real number x let $[\bar{x}]$ denote the least integer greater than or equal to x. Let $D^0 = \{a \in D : \delta \leq a \leq 1 - \delta\}$.

LEMMA 1. Under the assumptions of Theorem 2, the minimum resistance to moving out of the basin of attraction of the convention $a$ is $r_k(a) = [\overline{kR(a)}]$, where

$$R(a) = \min \left\{1 - u(a - \delta)/u(a), 1 - v(1 - a - \delta)/v(1 - a)\right\}.$$

$$
a \in D^0
$$

PROOF. Suppose that the process is at the convention $a$, where $0 < a < 1$. Let $\pi$ be a path of least resistance from $a$ to a state that is in some other basin. By definition, $\pi$ contains $r_k(a)$ mistakes. Clearly, $\pi$ must pass through some state $s$ such that some landlord's best reply to a sample from $s$ is different from $a$, and/or some tenant's best reply to a sample from $s$ is different from 1 - $a$. Let $s$ be the first such state. Without loss of generality we can assume that some landlord (say $\alpha$) has a best reply $a' \neq a$ to a sample $\sigma$ of size $k_\alpha$ drawn from $s$. By choice of $s$, every tenant's demand in $s$ that differs from 1 - $a$ must have been generated by an earlier mistake. Let $i \leq k_\alpha$ be the total number of mistakes by tenants in the sample $\sigma$ that the landlord drew.

Now construct another sample $\sigma'$ of size $k_\alpha$ in which there are i instances of 1 - $a'$ and $k_\alpha - i$ instances of 1 - $a$. Landlord $\alpha$'s best reply to this sample is $a'$, because his best reply to $\sigma$ was $a'$, and $\sigma'$ is obtained from $\sigma$ by changing every mistake to 1 - $a'$.

We shall now construct an alternative path $\pi'$ from $a$ to the $a'$-basin in which the total number of mistakes is at most i, from which it follows that $\pi'$ is also a path of least resistance and $i = r_k(a)$.

Beginning at the convention $a$, let a succession of tenants mistakenly demand 1 - $a'$ j times in a row, where $j = \min \{i, k\}$ and $k$ is the minimum among all agents' sample sizes. With positive probability a landlord $\alpha^*$ with minimum information $k$ will be drawn in the next period. (Recall that, by hypothesis, the minimum information $k$ is attained in both classes.) With positive probability $\alpha^*$ will sample the most recent $k$ plays. This sample $\sigma^*$ consists of $j$ instances of 1 - $a'$ and $k - j$ instances of 1 - $a$. In $\sigma^*$ the relative frequency of 1 - $a'$ is at least as great as it was in $\sigma'$ because $j/k \geq i/k_\alpha$. Since $\alpha^*$ and $\alpha$ have the same utility function, and $\alpha$'s best reply to $\sigma'$ was $a',$ it follows that $\alpha^*$'s best reply to $\sigma^*$ is also $a'$.

With positive probability a landlord like $\alpha^*$ will be drawn $k$ times in a row, he will draw the sample $\sigma^*$ each time, and will reply with $a'$ each time. This establishes a run of $a'$ (by the landlords) for $k$ successive periods without introducing more mistakes. After this there is a positive probability that a succession of $k$ tenants will sample this run and demand 1 - $a'$ for $k$ periods in a row`. From here it is clear (as in the proof of Theorem 1) that the process can converge to the convention $a'$ with no further mistakes.

Thus we have constructed an alternative least resistant path from the convention $a$ to the convention $a'$ in which the only mistakes are an initial succession of $i$ mistaken demands 1 - $a'$, where $i = r_k(a)$. To compute $r_k(a)$ it therefore suffices to consider, for every $a' \neq a$, the least number of mistaken demands 1 - $a'$ that would cause a landlord with minimum information $k$ to reply with $a' \neq a$, and the least number of mistaken demands $a'$ that would cause some tenant with minimum information $k$ to reply with 1 - $a'$, and to take the minimum of all these numbers.

Choose an arbitrary convention $a' \neq a$. We shall distinguish two cases: $a' < a$ and $a' > a$.

## Case 1. $a' < a$

Let the process be in the convention $a$. (Note that, since $\delta \leq a' < a$, we implicitly exclude $a = \delta$.) Suppose that the landlords make $i$ successive demands of $a'$ that cause some tenant's best reply to switch to 1 - $a'$ instead of 1 - $a$. We can assume that $i \leq k$ and that the tenant in question has minimum information. When this tenant samples these $i$ mistaken demands $a'$, together with $k - i$ of the previous "conventional" demands $a$, he switches to 1 - $a'$ provided that $(i/k)v(1 - a') \geq v(1 - a)$, that is,

$$i \geq (v(1 - a)/v(1 - a'))k.$$

Over all $a' < a$ the minimum value of $i$ occurs when $a' = \delta$:

---

$$i = \frac{(v(1 - a)/v(1 - \delta))k}{5}$$

The other possibility is that the tenants make the mistakes. Suppose that a succession of $j$ tenants demand 1 - $a'$ by mistake instead of 1 - $a$. (Note that these are only "mistakes" in the sense that they are not optimal replies to the existing set of precedents. The tenants would obviously like to get 1 - $a'$ rather than 1 - $a$ if they thought they could get away with it. They are "optimistic mistakes.") If some landlord with minimum information $k$ samples the $j$ mistaken demands of 1 - $a'$, together with $k - j$ of the previous conventional demands 1 - $a$, then he switches to $a'$ provided that $u(a') \geq (1 - j/k)u(a)$, that is,

$$j \geq (1 - u(a')/u(a))k.$$

Over all $a' \in D^0$, the minimum value of $j$ occurs when $a' = a - \delta$:

$$j = \frac{(1 - u(a - \delta)/u(a))k}{6}$$

**Case 2. $a' > a$.**

An analogous argument shows that, if the landlords make $j$ mistaken demands of $a'$, then some tenant switches provided that

$$i \geq (1 - v(1 - a')/v(1 - a))k.$$

The minimum occurs when $a' = a + \delta$:

$$i = \frac{(1 - v(1 - a - \delta)/v(1 - a))k}{7}$$

If the tenants make $j$ mistaken demands of 1 - $a'$, then some landlord switches provided that

$$j \geq (u(a)/u(a'))k$$

and the minimum occurs when $a' = 1 - \delta$:

$$j = \frac{(u(a)/u(1 - \delta))k}{8}$$

---

It follows that $r_k(a)$ is the least integer greater than or equal to

$$k \min \left\{ v(1 - a)/v(1 - \delta), 1 - u(a - \delta)/u(a), 1 - v(1 - a - \delta)/v(1 - a), u(a)/u(1 - \delta) \right\}.$$ (9)
$$a \in D^0$$

(We remark that the minimum in (9) can in fact be taken over all $a \in D^0$, even though in Case 1 the value $a = \delta$ was excluded and in Case 2 the value $a = 1 - \delta$ was excluded. The reason is that when these values are substituted into the corresponding terms in (9), the result is unity, so they do not affect the minimum.)

We claim that the fourth term of (9) weakly dominates the third term for all $a \in D^0$ and all $u, v \in UxV$:

$$u(a)/u(1 - \delta) \geq 1 - v(1 - a - \delta)/v(1 - a).$$ (10)

Indeed, since $v$ is concave, we have

$$[v(1 - a) - v(1 - a - \delta)]/\delta \leq [v(1 - a) - v(0)]/(1 - a),$$

because the rate of loss of utility in going from 1 - a to 1 - a - $\delta$ is no more than the rate of loss of utility in going from 1 - a to 0. Since $v(0) = 0$ this implies that

$$1 - v(1 - a - \delta)/v(1 - a) \leq \delta/(1 - a)$$ (11)

Similarly, since $u$ is concave, we have

$$[u(1 - \delta) - u(0)]/(1 - \delta) \leq [u(a) - u(0)]/a,$$

from which it follows that

$$u(a)/u(1 - \delta) \geq a/(1 - \delta)$$ (12)

It may be checked that $a/(1 - \delta) \geq \delta/(1 - a)$ whenever $\delta \leq a \leq 1 - \delta$. Combining this with (11) and (12) we therefore have

$$u(a)/u(1 - \delta) \geq a/(1 - \delta) \geq \delta/(1 - a) \geq 1 - v(1 - a - \delta)/v(1 - a),$$ which establishes (10).

A similar argument shows that the first term in (9) weakly dominates the second. It follows that $r_k(a)$ is given by the expression $[kR(a)]$ where

$$R(a) = \min \{ 1 - u(a - \delta)/u(a), 1 - v(1 - a - \delta)/v(1 - a) \}.$$  

(13)

This concludes the proof of Lemma 1.

The preceding proof shows that the minimum resistance to displacing the convention $a$ in favor of the convention $a - \delta$ is essentially $k$ times $1 - u(a - \delta)/u(a)$, which is the relative loss in utility that a landlord would experience from giving up one $\delta$-increment of his share. Similarly, the minimum resistance to displacing the convention $a$ in favor of the convention $a + \delta$ is $k$ times $1 - v(1 - a - \delta)/v(1 - a)$, which is the relative loss in utility that the tenant would experience from giving up one $\delta$-increment of his share.

LEMMA 2. The function $R(a)$ is unimodal and achieves its maximum at precisely the discrete Nash bargaining solution(s). Furthermore, $r_k(a) = [kR(a)]$ achieves its maximum at the discrete Nash bargaining solution(s) for all $k$, and for all sufficiently large $k$ it achieves its maximum only at the discrete Nash bargaining solutions.

PROOF. For every $a \in D^0$ let $f(a) = 1 - u(a - \delta)/u(a)$. Since $u$ is concave, $u(a) - u(a - \delta)$ is non-increasing in $a$. Since $u$ is strictly increasing, $f(a)$ is strictly decreasing in $a$. Similarly let $g(a) = 1 - v(1 - a - \delta)/v(1 - a)$ and conclude that $g(a)$ is strictly increasing in $a$. Therefore $R(a) = \min \{ f(a), g(a) \}$ is first strictly increasing and then strictly decreasing, so it is unimodal.

Let $(a^*, 1 - a^*)$ be a discrete Nash bargaining solution, that is, a division that maximizes $u(a)v(b)$ subject to $a + b \leq 1$ and $a, b \in D$. The maximum is attained at an interior solution $a^* \in D^0$. Then

$$u(a^*)v(1 - a^*) \geq u(a^* - \delta)v(1 - a^* + \delta),$$  

(14)

so

$$u(a^* - \delta)/u(a^*) \leq v(1 - a^*)/v(1 - a^* + \delta),$$

---

$$1 - u(a^* - \delta)/u(a^*) \geq 1 - v(1 - a^*)/v(1 - a^* + \delta),$$

from which it follows that

$$f(a^*) \geq g(a^* + \delta).$$ (15)

Similarly, we have

$$u(a^*)v(1 - a^*) \geq u(a^* + \delta)v(1 - a^* - \delta),$$ (16)

so

$$g(a^*) \geq f(a^* + \delta).$$ (17)

We claim that

$$R(a^*) = \min\{f(a^*), g(a^*)\} \geq \min\{f(a^* + \delta), g(a^* + \delta)\} = R(a^* + \delta).$$ (18)

Indeed, if $f(a^*) \geq g(a^*)$ then (17) follows from (16). If $g(a^*) \geq f(a^*)$ then (17) follows from the fact that $f$ is decreasing. Similarly, conclude from (15) that $R(a^*) \geq R(a^* - \delta)$. Thus $R$ attains a local maximum at $a^*$. Since $R$ is unimodal, $a^*$ is a global maximum. Conversely, if $a^*$ maximizes $R(a)$, then it may be verified that (15) and (17) hold. Hence (14) and (16) hold, which implies that $(a^*, 1 - a^*)$ is a local maximum of $u(a)v(b)$ on DxD. Since $u(a)v(b)$ is concave, $(a^*, 1 - a^*)$ must be a global maximum on DxD as well. We have therefore shown that $(a^*, 1 - a^*)$ is a discrete Nash bargaining solution if and only if $a^*$ maximizes $R(a)$.

Finally, if $a^*$ maximizes $R(a)$, then $a^*$ also maximizes $[kR(a)]$ for all $k$. Conversely, if $a^*$ maximizes $[kR(a)]$ for all sufficiently large $k$, then $a^*$ maximizes $R(a)$. Thus the discrete Nash solutions maximize $[kR(a)]$ for all $k$, and they are the only maximizers of $[kR(a)]$ for all sufficiently large $k$. This completes the proof of Lemma 2.

To establish Theorem 2, it remains to be shown that the discrete Nash bargaining solutions are the conventions with minimum stochastic potential. To this end, let $G$ be the complete, directed graph in which each convention $a$ is a vertex, and the "weight" or resistance of each directed edge $a \rightarrow a'$ is the minimum number of mistakes required in a transition from $a$ to $a'$. By definition, $r_k(a)$ is the minimum weight among all edges exiting from $a$. We are going to show that each discrete Nash solution is the root of a spanning tree of G that has minimum total resistance.

Suppose first that the discrete Nash bargaining solution is unique, and denote it by $(a^*, 1 - a^*)$. Define the following $a^$-tree $T^$:

$$\begin{align*}
a < a^* & \Rightarrow (a, a + \delta) \in T \\
a > a^* & \Rightarrow (a, a - \delta) \in T.
\end{align*}$$

$T^*$ is indicated in Figure 1.

Figure 1. The $a^$-tree defined in (19).

We claim that, for all $k$, the resistance of $T^*$ is no greater than the resistance of any other $a$-tree, and for all sufficiently large $k$, its resistance is strictly less than every other $a$-tree $(a \neq a^*)$. First, note that every vertex $a \neq a^*$ has exactly one outgoing edge in $T^*$, and for all $k$ the resistance of this edge is $r_k(a)$, which is the minimum among all edges exiting from $a$. Now consider any $a'$-tree $T'$ where $a' \neq a^*$. Every $a \neq a', a^*$ has exactly one outgoing edge in $T'$, and for all $k$, the resistance of this edge is at least $r_k(a)$, the resistance of the edge exiting from $a$ in $T^*$. The vertex $a^*$ also has an exiting edge in $T'$, and its resistance is at least $r_k(a^*)$. By Lemma 2 $r_k(a^*) \geq r_k(a')$ and strict inequality holds for all sufficiently large $k$. Hence the unique edge exiting from $a^*$ in $T'$ has a strictly greater resistance than the unique edge exiting from $a'$ in $T^*$ provided that $k$ is large enough. So the total resistance of $T'$ is at least that of $T^*$, and it is strictly greater when $k$ is sufficiently large. Since $T'$ was arbitrary, it follows that $a^*$ has minimum stochastic potential among all conventions, and it is a strict minimum when $k$ is sufficiently large. Thus $a^*$ is stable, and it is the unique stable convention for all sufficiently large $k$.

If there are two discrete Nash bargaining solutions, then for each of them construct a tree $T^*$ as above. A similar argument shows that these are among the $a$-trees of least total resistance for all $k$, and they are the unique trees of least resistance for all sufficiently large k. This establishes Theorem 2.

## 7. Heterogeneous populations and the fifty-fifty solution

Theorem 2 shows that the Nash bargaining solution will eventually be selected by an evolutionary process that does not require any common knowledge on the part of the bargainers. This conclusion is based, however, on the special assumption that all agents in the same class have the same utility function. Moreover, the result is very sensitive to this assumption. If just one agent has a utility function that differs from the norm in his or her class, then the long-run outcome of the process may be completely different from the one described in Theorem 2. The reason is that the long-run behavior of the process is determined by the person who is most risk averse, that is, the one who would suffer the greatest proportional loss in utility from a given reduction in share. If there is just one landlord, for example, who is more risk averse than the others, then his choices will determine the long-run behavior of the process.

Let us therefore consider the more general situation in which the agents in each class have different utility functions. Let U be the (finite) set of utility functions represented among the agents in A, and let V be the (finite) set of utility functions represented among the agents in B. We shall assume further that there is at least one agent with a minimum level of information k in every utility class. That is, for every u ∈ U there exists some agent in A with information k and utility function u, and for every v ∈ V there exists some agent in B with information k and utility function v.7 Theorem 2 says that when two agents bargain with utility functions u and v, then the resistance to moving out of the basin of attraction of the convention $a$ is $[\text{kR}(a)]$. It follows that, over all pairs of agents, the minimum resistance to moving out of the basin of attraction of $a$ is $[\text{kR}^*(a)]$, where

$$\text{R}^*(a) = \min \left\{(1 - u(a - \delta)/u(a)), (1 - v(1 - a - \delta)/v(1 - a)) \right\}.$$
$$(u, v) \in \text{UxV}$$

It is easy to see that $\text{R}^*(a)$ is unimodal. Indeed, it is just the lower envelope of the functions $\text{R}(a)$ over all pairs of utility functions $(u, v) \in \text{UxV}$. A similar argument to the proof of Theorem 2 shows that, for all sufficiently large k, the unique stochastically stable convention(s) are those that maximize $\text{R}^*(a)$. Moreover the maximizers of $\text{R}^*$ are among the stochastically stable conventions for all k. We summarize these observations as follows.

7 The more general case in which the minimum level of information differs among utility classes will be considered in a separate paper.

---

THEOREM 3. Let U be the class of utility functions of agents in A and let V be the class of utility functions of agents in B. Let k be the minimum information among all agents (k ≤ m/2) and suppose that in every utility class there is at least one agent with minimum information. Every value of a that maximizes R*(a) defines a stable convention, and for all sufficiently large k (and m) these are the only stable conventions.

The solutions that maximize R* can be viewed as a generalization of the Nash solution to heterogenous populations of bargainers.

Suppose now that there is some mixing between the classes. Then we would expect that, for every agent in class A, there is at least one agent in class B with the same utility function and the same information, and vice versa. This does not imply that the distribution of agent types is the same in each class, only that the two distributions have the same support. In this case the function R*(a) is symmetric about one-half ($R^*(a) = R^*(1 - a)$), so we obtain the following.

COROLLARY 3.1. Suppose that for every agent in A there is a similar agent in B, and vice versa. If $d = 1/\delta$ is even then $(.5, .5)$ is stable. If $d = 1/\delta$ is odd then $(.5 + \delta, .5 - \delta)$ and $(.5 - \delta, .5 + \delta)$ are stable. Moreover, for all sufficiently large k (and m) these are the only stable conventions.

---

## References

Bardhan, Pranab, (1984): "Land, Labor, and Rural Poverty. Delhi: Oxford University Press.

Binmore, K. G., (1987): "Nash Bargaining Theory II," in The Economics of Bargaining, ed. by K. G. Binmore and P. Dasgupta. Oxford: Basil Blackwell.

Canning, David, (1991): "Average Behavior in Learning Models," Working Paper, Pembroke College, Cambridge.

Carlsson, Hans, (1991): "A Bargaining Model Where Parties Make Errors," Econometrica, 59, 1487-1496.

Freidlin, M. and A. Wentzell, (1984): Random Perturbations of Dynamical Systems. New York: Springer Verlag.

Foster, Dean and H. P. Young, (1990): "Stochastic Evolutionary Game Dynamics," Theoretical Population Biology, 38, 219-232.

Kalai, Ehud and M. Smorodinsky, (1975): "Other Solutions to Nash's Bargaining Problem," Econometrica, 45, 513-518.

Kandori, M., G. Mailath, and R. Rob, (1991): "Learning, Mutation, and Long-Run Equilibria in Games," Working Paper, The University of Pennsylvania.

Nash, J., (1950): "The Bargaining Problem," Econometrica, 18, 155-162.

Nash, J., (1953): "Two-person Cooperative Games," Econometrica, 21, 128-140.

Raiffa, Howard, (1953): "Arbitration Schemes for Generalized Two-Person Games," in Contributions to the Theory of Games, ed. by H. Kuhn and A. W. Tucker. Princeton: Princeton University Press.

Robertson, A. F., (1987): The Dynamics of Productive Relationships, Cambridge: Cambridge University Press.

---

Rubinstein, A., (1982): "Perfect Equilibrium in a Bargaining Model," Econometrica 50: 97-109.

Schelling, T., (1960): The Strategy of Conflict. Cambridge, Mass: Harvard University Press.

Young, H. Peyton, (1991): "The Evolution of Conventions," Working Paper 91-10-043, The Santa Fe Institute.

Young, H. Peyton, and Dean Foster, (1991): "Cooperation in the Short and in the Long Run," Games and Economic Behavior, 3, 145-156.