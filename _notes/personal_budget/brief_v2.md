# Brief: carry three worlds through the article

Article: `_plans/hyperscaling_coase_personal_budget.qmd` (edit this file in place; touch no other file).
Check script, already extended, read-only for you: `_plans/hyperscaling_coase_personal_budget_sim.py`, section H.
Every number below comes from that section and has been checked.

## Why this revision

The article treats saturation in one short subsection ("### Saturation", in "The model") as a yes-or-no question and then sets it aside.
Dan (the author) wants all the cases kept in play.
There are three, and the article should carry all three from the model through the results, remedies and verdict:

1. **Saturating world.** Every matter has a fixed finite depth.
2. **Non-saturating world.** Only the ratio of the two sides' compute matters, at every scale. This is the article's current main case; everything now in "Results" is derived for it.
3. **Mixed world.** A fraction of each principal's stakes is in matters that never saturate and the rest is in matters that do.

Nothing now in the article is to be cut or shortened.
This is an essay still being worked out: there is no length target, and existing material stays unless a sentence becomes false, in which case correct it.

## Vocabulary (use these and coin nothing else)

- *depth* $\bar q$ of a matter: units of compute beyond which more adds nothing (already in the article).
- *saturating matter*: one with a fixed finite depth. *Non-saturating matter*: one where only the compute ratio matters at every scale, so no depth is ever reached.
- *saturating world*, *non-saturating world*, *mixed world*: as above.
- $\phi$: the fraction of a principal's total stakes $S_i$ that is in non-saturating matters. (The symbol is free; the article uses $f$ for the challenge fee and $c_0$ for the showing-up cost.)
- $r(q)$: decisiveness measured when both sides use $q$ units of compute, i.e. the slope of the log-odds of prevailing on the log compute ratio at equal compute $q$. The article already defines decisiveness as that slope; this only lets it depend on the level.

Add $\bar q$ and $\phi$ to the symbols table.

## The content, in the order the argument needs it

### A. Diminishing returns is not saturation

For any $r\le1$ the contest already has diminishing returns to a side's own spend, and dissipation is still $rV/2$ whatever compute costs.
What makes dissipation independent of the price $p$ is that only the ratio of the two spends matters.
Saturation is a different property: an absolute level of compute beyond which nothing changes.
So the question for a matter is whether it has an absolute scale or only a relative one.

### B. A test for which matters saturate (extends the search story already in "Two uses of compute")

Keep the search story: each unit of compute buys one independent draw of a candidate (argument, clause, counter-proposal) and a side uses its best draw.
The article already notes that if whoever holds the single best draw prevails, the chance is $q_i/(q_i+q_j)$ whatever the distribution. That is $r=1$ at every scale, with no saturation, even if quality is bounded.

Now suppose instead that whoever decides (a court, an arbitration protocol, the other side's own assessment) compares the two best draws with some error of fixed size, so that a small enough gap is as good as a tie.
Then the upper tail of the distribution of candidate quality decides what happens as both sides' compute $q$ grows.
Script H4 computes $r(q)$ with the decider's error logistic and of scale equal to one standard deviation of a single draw:

| Upper tail of candidate quality | $r(10)$ | $r(100)$ | $r(1{,}000)$ | $r(10{,}000)$ | $r(10^6)$ | Reason |
|---|---|---|---|---|---|---|
| bounded (uniform): a best answer exists | 0.27 | 0.034 | 0.0035 | 0.0003 | 0.0000 | the gap between the two bests shrinks like $1/q$; $r(q)\approx 1/(\text{error scale}\times q)$ |
| exponential | 0.65 | 0.66 | 0.67 | 0.67 | 0.67 | the gap depends only on $\log(q_i/q_j)$, so $r$ is constant: the article's contest with $r=2/3$ |
| Gaussian | 0.44 | 0.33 | 0.27 | 0.24 | 0.19 | the gap shrinks like $1/\sqrt{2\ln q}$, so $r$ falls, but a millionfold rise in compute only halves it |
| power law (index 3) | 0.62 | 0.83 | 0.94 | 0.99 | 1.00 | the gap grows with $q$, the decider's error stops mattering, $r\to1$ |

Equilibrium spend per side on a \$10,000 stake as the price of a draw falls from 1 to 0.01 to 0.0001 dollars (same script):
bounded \$92, \$9.30, \$0.93 (closed form $\sqrt{Vp/(4\varsigma)}$ with $\varsigma$ the error scale, so spend falls as $\sqrt p$);
exponential \$1,667 at every price;
Gaussian \$698, \$542, \$457 (a ten-thousandfold fall in price cuts spend by about a third).

Conclusion to state: saturation needs two things together, a best answer that exists and a decider that ignores small gaps.
Bounded quality alone is not enough.
High-frequency trading is the example: the speed gaps are tiny and bounded below by physics, but the trade goes to whoever is ahead by any margin, and [Budish, Cramton and Shim (2015)](https://ideas.repec.org/a/oup/qjecon/v130y2015i4p1547-1621.html) find that competition did not change the size or frequency of the arbitrage opportunities and only raised how fast a trader must be to capture them; their remedy, frequent batch auctions, works by making time discrete so that tiny speed advantages stop mattering.
(Verified at abstract level only: say no more about the paper than this.)
The three limit types of the best of many draws are standard extreme value theory (the Fisher–Tippett–Gnedenko theorem); name it in plain words and cite no link.
Jia (2008), already cited in the article, is the nearest published derivation of the ratio form from noise in performance; do not claim more for it than the article already does.

This table is ours, derived for this article and checked numerically; say so plainly and do not present it as a published result.
The Gaussian row matters for Dan's question: returns that diminish on average can still fail to saturate over any range of compute that will be observed.

### C. What each world looks like for Asha (all $r=1$; S = \$25,000, B = \$400)

**Saturating world.** Two unconstrained sides on a matter of depth $\bar q$ together spend $\min(rV/2,\;2p\bar q)$ (script H1).
Take depth proportional to stake, so that each side's spend against Asha is capped at a total of $c$ dollars over all her matters, and let $c$ fall with the price of compute (script H2):

| cap $c$ on each side's spend | Asha spends | firms spend | Asha's share | dissipated fraction of $S$ |
|---|---|---|---|---|
| \$2,762 or more (the cap does not bind) | \$400 | \$2,762 | 12.6% | 12.6% |
| \$1,600 | \$400 | \$1,600 | 20% | 8.0% |
| \$800 | \$400 | \$800 | 33% | 4.8% |
| \$400 | \$400 | \$400 | 50% | 3.2% |
| \$100 | \$100 | \$100 | 50% | 0.8% |
| \$10 | \$10 | \$10 | 50% | 0.1% |

Closed form: while $B<c<\sqrt{BS}-B$ her share is $B/(B+c)$; once $c\le B$ both sides are at the cap and split evenly.
The cap binds the stronger side first, so falling compute prices first raise Asha's share and only then cut her own bill.
In this world Krier is right about cost and also about distribution: the split stops depending on compute.
"Split evenly" is the article's existing assumption for a saturated matter; more exactly, the split is whatever the merits and outside options give, and compute no longer moves it.

**Non-saturating world.** The rest of the Results section as it stands.

**Mixed world.** A fraction $\phi$ of her stakes is non-saturating; the rest saturates at negligible cost and splits evenly.
She then concentrates her whole budget on the non-saturating part, so every formula in Results holds there with $S$ replaced by $\phi S$.
For $r=1$ and $B<\phi S/4$: her share in non-saturating matters is $\sqrt{B/(\phi S)}$, her overall share of $S$ is $(1-\phi)/2+\sqrt{\phi B/S}$, and the dissipated fraction of $S$ is $\sqrt{\phi B/S}$.
If $\phi\le 4B/S$ (6.4% for Asha) her budget covers an even fight over all of it and she gets half of everything.
Script H3:

| $\phi$ | share in non-saturating matters | Asha takes | overall share | dissipated fraction of $S$ |
|---|---|---|---|---|
| 100% (non-saturating world) | 12.6% | \$3,162 | 12.6% | 12.6% |
| 50% | 17.9% | \$8,486 | 33.9% | 8.9% |
| 20% | 28.3% | \$11,414 | 45.7% | 5.7% |
| 6.4% | 50% | \$12,500 | 50% | 3.2% |
| 2% | 50% | \$12,500 | 50% | 1.0% |

A direct check with her actual matters: if only the lease (\$6,000) is non-saturating and every other matter saturates at \$5 a side, the computed equilibrium gives her 25.2% of the lease surplus and \$11,010 in all, matching the closed form $\sqrt{380/6000}$.

Two things to say about this table.
The mixed world is much kinder to Asha in total than the non-saturating world, because she gets half of everything that saturates.
Within the non-saturating part nothing in the Results changes in kind: her share there still falls as non-saturating stakes multiply, the voucher that buys parity there costs $r\phi S/4$, and the trade-off between even shares and waste holds there.
So in the mixed world what matters for every result is the stake-weighted fraction $\phi$, not the number of matters that saturate.

Stakes are plausibly heavy-tailed, and then a few matters carry much of $\phi$: with power-law stakes of index $\alpha$ the largest 1% of matters hold $0.01^{1-1/\alpha}$ of total stake, about 10% at $\alpha=2$ and about 21% at $\alpha=1.5$ (script H6; the simulation agrees).
A consequence of the $\min(rV/2,2p\bar q)$ formula worth one or two sentences: with a common depth, the large-stake matters saturate first as $p$ falls, and a matter stays non-saturating as $p$ falls only if its depth grows at least as fast as $1/p$. A non-saturating matter is therefore one whose depth is unbounded, or one whose depth some party chooses.

### D. Who chooses the world

The article's existing argument (the stronger side can add clauses; Carlin; Gabaix and Laibson; Bakos et al.; Larson and Sandholm; Halpern and Pass) stays. Sharpen it with this result (script H5).

Suppose a firm can choose whether its matter with a household saturates (even split, negligible spend, firm nets $V/2$) or does not.
At $r=1$, against a household of strength $s$ the firm nets $V/(1+s)^2$ on a non-saturating matter.
So it prefers the non-saturating matter exactly when the household's share there would be below $1-1/\sqrt2\approx29\%$, which is when the household's budget is below $(1-1/\sqrt2)^2\approx8.6\%$ of its non-saturating stakes.
For $r=0.5$ the thresholds are a share of 38% and a budget of 4.5% of those stakes; for $r=0.25$, 44% and 2.3%.
Against an unconstrained opponent the firm nets $V/4<V/2$ and prefers saturation.
So complexity is chosen against counterparties who cannot afford the contest, and not against equals.

The choice is self-reinforcing across firms, because every additional non-saturating matter thins the household's budget and lowers its share in all of them.
With Asha's firm matters (\$12,000 job, \$6,000 lease, \$2,000 insurer, \$1,000 platforms; \$21,000 in all), letting firms revise in turn:

| household budget | starting with every matter saturating | starting with none saturating |
|---|---|---|
| \$400 (Asha) | all four end non-saturating | all four stay non-saturating |
| \$1,500 | all four stay saturating | all four stay non-saturating |
| \$3,000 | all four stay saturating | all four end saturating |

Rule: every matter saturating is an equilibrium when the budget is at least 8.6% of the household's largest single stake (\$1,030 here); none saturating is an equilibrium when the budget is below 8.6% of all its stakes with firms (\$1,800 here); between the two, both are.
Asha's \$400 is below 8.6% of her job stake alone, so her employer makes that matter non-saturating whatever the others do, and the rest follow.

What this says about the three worlds, to be stated carefully as conditional on the assumption that depth is the stronger side's choice and costs nothing to raise:
within one household's dealings with firms the mixed world is not a resting point; it tips to all or nothing.
Across the population the outcome is mixed in a different sense: well-funded households live in the saturating world and poorly funded ones in the non-saturating world.
A household's own mixed world survives where depth is fixed by the nature of the matter or by a protocol the firm cannot alter.
This is the answer to "which of the two is the more reasonable assumption": neither holds for everyone, and which one holds for a given principal depends on its budget and on who sets the depth.

### E. Remedies and verdict

Remedy to add (as a new row or by extending the "lower decisiveness" row, your choice): make matters saturate, by fixed-depth protocols, standard forms that bound a contract's complexity, and deciders that treat small gaps as ties (Budish, Cramton and Shim's batch auction is the model).
Effect in the model: lowers $\phi$; a household gets half of what saturates and a larger share of the rest.
Cost: forgoes bespoke terms; and by D, a firm facing a poorly funded household prefers the matter not to saturate, so the protocol has to be imposed, not left to the stronger side.

Verdict: the regime map currently has decisiveness and liquidity as rows and security of entitlements as columns.
Add the three worlds without dropping any existing cell; a short table or paragraph placed before or after the map is fine.
The sentence "If $r$ falls towards zero as agents become more capable, bargaining saturates and Krier's cost claim holds" should become a statement about measuring $r(q)$ as $q$ grows, matter type by matter type, and about measuring $\phi$.
The contested-entitlements results were derived for a non-saturating contest; say so, and say what would be different if a challenge were a saturating matter is not modelled.

### F. Summary and framing

"What we found" should name the three worlds in plain words, say which results belong to which, and give the Asha figure for the mixed world (about \$11,400 if a fifth of her stakes never saturate, against about \$3,200 if none do).
Its last paragraph ("Krier's picture survives more generally if ... the returns to compute in bargaining run out. Neither has been measured ...") should be revised to match.
At the start of "Results", say that the sections which follow are derived for non-saturating matters and tell the reader where the other two worlds are treated.

### G. Appendix

Add short derivations: the capped contest ($\min(rV/2,2p\bar q)$; share $B/(B+c)$); the mixed-world share; the firm's threshold $V/(1+s)^2$ against $V/2$; the $1/(\varsigma q)$ approximation for the bounded tail and the $\sqrt p$ spend. Each is two or three lines:

- Capped pair: at $x=y=c$ each side's marginal return is $rV/(4c)$, which is at least 1 iff $c\le rV/4$.
- Bounded tail: best of $q$ uniform draws is about $1-E/q$ with $E$ exponential; a 1% rise in $q_i$ moves the gap by about $1/q$ in expectation; with a logistic error of scale $\varsigma$ the chance of prevailing moves by $1/(4\varsigma)$ per unit of gap near a tie, so $r(q)=4\,\partial P/\partial\ln q_i\approx1/(\varsigma q)$; the first-order condition $V r(q)/(4pq)=1$ gives spend $pq=\sqrt{Vp/(4\varsigma)}$.
- Exponential tail: best of $q$ draws is $\ln q$ plus a Gumbel variable, so the gap is $\ln(q_i/q_j)$ plus noise that does not depend on $q$.
- Gaussian tail: best of $q$ draws is about $\sqrt{2\ln q}$ plus a Gumbel variable divided by $\sqrt{2\ln q}$, so $r(q)\approx1/(\varsigma\sqrt{2\ln q})$ for large $q$.
- Firm's choice: with household strength $s$ and $r=1$ the firm's share is $1/(1+s)$ and its spend $Vs/(1+s)^2$, net $V/(1+s)^2$; this exceeds $V/2$ iff $s<\sqrt2-1$, i.e. household share $s/(1+s)<1-1/\sqrt2$, i.e. $B/S<(1-1/\sqrt2)^2$ using $\sigma=\sqrt{B/S}$.

In "What the script checks", add what section H checks (H1 to H6 above).

## Where things go

- "The model" keeps a subsection on saturation, rewritten to hold A and B and to define the three worlds.
- A new Results section holds C and D. Put it where the argument needs it; after "More matters stretch the budget thinner" works, since it uses only the strength results. Give it an anchor like `{#three-worlds}`.
- Headings in this article are plain claims or noun phrases. No colons in headings.
- Add a sentence where a later section's claim depends on the world: "More matters stretch the budget thinner" (only non-saturating matters count towards $S$), the voucher and dissipation section (parity costs $r\phi S/4$), and the entitlements section (derived for a non-saturating contest).

## House rules

- Read `_voices/dan_voice.md` and `_voices/slop_patterns.md` first and write to them. Clear, plain, human presentation; the article says "we" throughout, keep that.
- One sentence per line in prose. Tables and display maths as the article already does them.
- Plain literal phrasing: no metaphors, no rhetorical beats, no slogans. Define every term at first use; one term per concept; no new coinages beyond the vocabulary above.
- Round numbers in prose; exact figures only in tables.
- State conditions with symbols, as the article does (say what a quantity is a function of, what a threshold is a threshold in).
- Citations are hyperlinks on author–year text. Add no citation beyond Budish, Cramton and Shim (2015) with the link given above. No `[@key]` citations; do not touch any bibliography file.
- Never write `<!-- sem -->` markers or any HTML comment.
- Do not read any other `_plans/hyperscaling_coase*` file. Do not run git commands that change anything. Do not edit the script.
- Running-cast convention: Asha (nurse, \$400, \$25,000), Meridian (the firms), Bram (neighbour), Odile (homeowner). Use them; add no new characters.

## What to hand back

A short list: each section you changed or added, with one line on what changed, and any place where you found the brief's claim did not fit what the article already says (do not paper over a mismatch; report it).
