# Revision instructions after the cold read

A reader with no context (Krier's essay read a while ago, undergraduate economics, nothing else) read the draft and reported where they got lost.
Their findings are below, each with my ruling on what to do.
Line numbers refer to the draft as you left it.
Your earlier corrections to my brief (repeat-player waste is $2rs(1-s)$; the condition for wealth to grow out of the constrained region; Alice's two benchmark figures) were right and stay.

One correction of my own first: **spelling is Oxford *-ize*** (summarize, maximize, minimize, amortize, recognize, formalize), as `_voices/dan_voice.md` says. My brief was wrong. Krier's quoted words keep his spelling. Otherwise British (neighbour, labour, towards).

## A. Substantive rulings (these change what the article claims)

**A1. Comparators.** The cold reader is right that "better than a world without bargaining" is empty, because the model's wage is itself a bargain, and that "better than the one we have" (L680) compares against a world the models do not contain.
Replace both with what the models do say:
- *Per matter*: a principal can refuse any matter and keep its entitlement, so no single matter leaves it worse off than if that matter had never been raised. This is a guarantee about each matter, not a comparison of worlds. Manufactured threats are the exception.
- *Against the benchmark*: as now.
- *Against the present*: not modelled, and say so in one short paragraph in the verdict. What the models suggest (label as conjecture): today the same contest is run with lawyers' hours and human attention as the input, and most small matters are never contested because the fixed cost of engaging is too high; cheap compute then (a) improves discovery, by Result 2, and (b) extends the contest to matters now settled by default rules, with the same fraction $r/2$ burnt on each. Whether that nets out well depends on $r$.
Delete "recognisably better than the one we have for the comfortable". The verdict sentence should be about the benchmark: every principal gets less than the benchmark gives; how much less, and for whom, as below. Use Dan's word "recognizably" at most once.

**A2. The credit market must be promoted, and the inequality claim narrowed.** Under the constitution as conceded (perfect enforcement, aligned agents) I see no reason a funder could not advance compute against a share of the bargaining gain, as litigation funders do. So be straightforward about it:
- With such funding nobody is liquidity-constrained, every matter is contested at parity, shares are at merit, there is no trap, and waste is at its maximum, $r/2$ of every surplus (Result 5).
- The inequality results (the square-root law, the trap) therefore hold only where bargaining gains cannot be pledged: where the gain is not money (quiet, light, a view), where the funder cannot verify the stakes or the merit, or where the funder is itself a repeat player with the scale advantage of the later section. Offer those three as reasons such a market might be incomplete; do not claim it would fail.
- The robust results are the waste results (1, 2, 5) and the scale and contract-size results; the distributional results are conditional. Both a subsidy and credit fix distribution by raising waste.
Put this in the opening summary, at the point where the square-root law is derived (before it, explain why a constrained principal spends everything on compute: a marginal dollar is worth more than $R$ there), and in the verdict.

**A3. Why $r=1$ is the headline (L196).** The stated reason is wrong. Correct reason: $r=1$ is Jones's own round summary and the low end of the measured range (the fitted slope gives about 1.3), and it is the largest value for which the many-matter model here is solved. It is therefore a conservative choice; say that $r>1$ is untested and probably worse.

**A4. "At $r=0$ every result collapses to the benchmark" (L674) and "all have one source" (L659) are false as written.** Results 1 to 9 collapse to the benchmark at $r=0$. The many-party limit does not depend on $r$ or on compute at all. Manufactured threats do not depend on $r$ either, and see A5: they pay *better* at $r=0$.

**A5. Result 10's condition must include the cost of the contest.** With equal shadow prices each side spends $r\,s_is_j(h+\kappa)$ on the matter. So $j$'s net gain from making the threat is
$$s_jh-s_i\kappa-r\,s_is_j(h+\kappa),$$
and at equal strength this is positive iff $h/\kappa>(2+r)/(2-r)$: $h>3\kappa$ at $r=1$, $h>\kappa$ at $r=0$. (Check with the conifers: $500-100-300=100$.) State the gross transfer $s_jh-s_i\kappa$ and the net condition separately. Note the consequence: the contest's waste deters marginal threats, so the benchmark world ($r=0$) is the one where threats pay most easily.
Also soften "So $i$'s stakes rise with other principals' compute" (L606): the link from compute to the number of such acts found is not modelled; say "if more search finds more such acts, then …" and call it a conjecture. And do not use "stakes" there (stakes is $E_i$, surplus available); say "the surplus $i$ is forced to bargain over".

**A6. "Roughly half of what Krier's picture promises to the comfortable" (L44).** Say what is halved: the net gain from bargaining, $E_i/4$ against $E_i/2$ at $r=1$. End-of-period resources are 67% to 98% of the benchmark in the table.

**A7. "The remedies that work" (L45, L675).** None is tested. Say "the remedies the models point to". Drop "fixed bargaining protocols" (it appears nowhere else). The standard-form remedy reduces waste and inequality *by construction* in the contract-size model (both sides can solve the game, so the split is at merit and extra compute is worth nothing); say that, not that it is shown to work.

**A8. The benchmark formula versus its properties (L124–140).** As written $Y^K$ has no compute in it, so properties (i) and (iii) do not follow from it. Make the dependence explicit: the surplus of a matter is realized only if at least $\bar c$ is spent on it; above that, nothing changes. Restate (iii) as "compute only creates surplus; it never moves it between the parties". For (iv), give the context of Krier's sentence: "these costs approach zero asymptotically" comes directly after his proposal that governments or philanthropies provide baseline agent services to low-income users, so it is a statement about the cost of that subsidy. Quote enough to show that. This also answers the cold reader's worry at L433: the identification is correct, but the article has to show the context.
Call $\bar c$ "the benchmark's satiation level", not "Krier's $\bar c$".

**A9. Contract size (Result 9) rests on an assumed cost function.** Do not call it a theorem. Say: assume the compute needed to solve a matter outright grows exponentially in the detail $n$, $G(n)=G_0\gamma^n$; give the two reference points for $\gamma$ as reference points and say plainly that mapping Hex board size onto contract contingencies is an analogy, not a measurement. The consequences then follow from the assumption.
Say what limits the drafter: the other side accepts any contract that leaves it at least its entitlement, so the drafter raises $n$ until either $S(n)$ stops growing or its own compute cost outweighs the gain; a right to a standard form changes the other side's fallback from its entitlement to its merit share of $S(\bar n)$. Say $\theta=\tfrac12$ here. Use $C_i<C_j$ for budgets, not $c_i<c_j$.

**A10. Two models of how wealth becomes strength.** Say explicitly that the fixed-budget model applies when compute cannot be bought at the margin within the period (rationed, or sold in tiers), and that the wealth-funded model supersedes it when compute can be bought. Say explicitly that Result 3 reverses "richer principals are stronger" above the parity threshold. Make the $\eta,\mu$ claim conditional ("if budgets rise at least in proportion to wealth and stakes less than in proportion") and drop "compute is a discretionary purchase".

**A11. Assemble the production function once.** The cold reader is right that the promised single function never appears. At $r=1$, for a principal that is small relative to its opponents, with compute $C_i$, stakes $E_i$, and opponents of strength $\bar a$:
$$\text{bargaining income}=\sqrt{E_iC_i/\bar a}\quad\text{for } C_i\le \bar aE_i ,$$
(share $\sqrt{C_i/(\bar aE_i)}$ on every matter; parity at $C_i=\bar aE_i/4$; the whole surplus at $C_i=\bar aE_i$). This one formula shows own compute (square root), opponents' compute (through $\bar a$, inversely), and stakes. When compute is bought at price $p$ and the alternative is capital at $R$, opponents who hold capital have $\bar a=1/(pR)$ and a principal buys compute only up to parity, which gives the two-branch $Y_i(w_i,E_i)$ already in the draft. Present it in that order in the wealth-funded section or the tally, and let the tally table say, for each row, which model and which value of $r$ it comes from.
(I have checked the square-root form numerically up to parity; beyond parity it follows from the same budget equation $x^2/(1+x)^2=C_i/(\bar aE_i)$, $s=x/(1+x)$.)

**A12. Smaller corrections.**
- L83: only the contract-size section relaxes C6. Use the word "constitution" consistently for C1–C6 whenever they are referred to (Dan asked for a constitution to be fixed), or not at all.
- L165: the share is a logistic function of $r\log(c_{im}/c_{jm})$ shifted by $\log(\theta_m/(1-\theta_m))$.
- L182–185: the $2.68 and $2.45 figures are for the same item; the $24.18 against $18.63 comparison is an average over deals and is not item-matched. Say so.
- L433: see A8.
- L449: mark the click-through comparison as my reading, not a result.
- L493: support "few end up in between" with the numbers: at the end 12.7% of principals are liquidity-constrained and 12.5% are at zero wealth.
- L495: it restores the benchmark's Gini, not its distribution (mean wealth stays at half).
- Reconcile the simulation with the closed form: at mean stakes the closed-form unconstrained steady state is $w^{**}\approx13$, while mean wealth in the contest rows is 21. The reason is that survivors face some opponents at zero wealth, from whom they take nearly the whole surplus at little cost (Result 5). The 0.2% at zero wealth in the benchmark row are principals whose drawn stakes give $E/2<\underline y$.
- L605: say what the incomplete-contracts literature says (contracts cannot specify every contingency, and what matters is who holds residual control when an unspecified one arises) and then that legal entitlements are incomplete in the same way.
- L544: "a further argument", not "a third".
- L439: say that $\lambda_ic_{im}=rS_ms(1-s)$ comes from the first-order condition.
- L246: one sentence on why discovery is under-provided: each side pays the whole cost of its own discovery and receives half of what it creates.
- L385–399 (general $r$): either show the two substitutions or cut to the small-$\rho$ result with a sentence saying what the exponent means (at lower decisiveness, wealth matters less for the share).
- Summary items must carry their conditions ($r=1$; opponents unconstrained; $\theta=\tfrac12$; $r\le2$ for Result 1).
- Verdict: "worse than the benchmark I have attributed to Krier", since the benchmark is a reading.

## B. Structure

**B1. Give the argument a spine.** After the benchmark's four properties, say that each section tests one of them, and keep to it:
one matter → is compute only productive, and does its cost vanish (iii);
many matters with fixed budgets → rivalry (ii);
buying compute from wealth → satiation and the cheap floor (i), (iv), and the single production function (A11);
wealth over time → the role of the initial endowment;
repeat players → scale, which the benchmark has no place for;
contract size → when satiation does hold;
manufactured threats → the one case of harm.
Open each section with the question it answers, in a plain declarative sentence. Keep the Krier quotations, but **do not** follow each with "The sentence presumes that…": eight uses of one template is the most machine-like feature of the draft. Say what the quotation commits Krier to in whatever words fit that place, and not always.

**B2. Rewrite the opening summary** in plain words that need none of the article's defined terms, or gloss each term in a clause. Include A2 and the conditions.

**B3. Notation table.** Move it to the end as a reference appendix; point to it once from the introduction. In the text, define each symbol in a sentence where it is first used. Add to the table a note that $R$ (capital letter, return on capital) and $r$ (decisiveness) are different things. Use $M_i$ for the count of a principal's matters and $M$ only for the repeat player's count of similar matters, and say they are the same thing for the landlord.

**B4. Many-party matters** go to a short appendix; keep the tally row but mark it "not part of the model; see appendix".

**B5. The landlord.** Where Alice's tenancy first appears (Result 3), say that the landlord's scale is being ignored until the repeat-player section, and that it makes things worse for Alice.

**B6. Cast.** Do not announce a protocol (L53). Use the cast where it helps.

**B7. Say once how results were checked**, in one short paragraph near the start: the closed forms are theorems of the toy models and each was checked against a direct numerical solution; the wealth table is simulation output; statements about market structure are conjecture; the script is `_plans/hyperscaling_coase_personal_budget_2_sim.py`. Then remove the scattered apparatus: "(theorem of the toy model)" ×10, "(checked numerically)", "to within $10^{-8}$", "less than $10^{-15}$", "confirmed by best-response iteration", "Numerically, for $r\in\{…\}$…", "a checked number", and the footnote. Keep a plain label only where a result is *not* a theorem (Result 9's assumption, the simulation, conjectures).

## C. Vocabulary: one term per concept

- Three thresholds, three names: the benchmark's *satiation level* $\bar c$; the *parity threshold* $Rw_i\ge rE_i/4$; the *trap threshold* $w_-$. Never a bare "threshold".
- Compute spent on dividing a surplus: call it *waste* throughout, defined once (the dollars both sides spend on claiming compute), noting once that the literature's name is rent dissipation. Not also "burnt", "dissipated", "spent contesting", "forgone".
- $Y_i$ is *end-of-period resources*; *bargaining income* is $\sum_mS_ms_{im}$. Fix L368 against L383: the two "$800 against …" comparisons use different comparators without saying so.
- *Strength* means $a_i$ only. Opus is "the more capable model". A party with more compute has "the larger budget". The party that writes the contract is "the drafter" throughout.
- *Unconstrained* / *liquidity-constrained* defined once, before Result 1 uses them; in Result 1 say "two principals whose spending is not limited by their wealth". Avoid "comfortable" and "those without spare cash" as informal synonyms, or introduce them once as glosses.
- *Merit share* for $\theta$; drop "fair shares", "the one a neutral arbiter would give" may appear once as the gloss of merit.
- *Matter* throughout for a bilateral bargain; "deal" only for the agreement reached.
- *Detail* $n$ throughout; not also complexity, size of the game, granularity (except in Krier's quotation).
- "The Krier benchmark" throughout; not also Krier's picture, Krier's world, Krier's good outcome.
- "computation" → "compute" throughout.

Terms to gloss in a clause at first use: Tullock contest; Skaperdas's axioms (say what kind: e.g. that each side's share rises in its own effort and falls in the other's, and that the ranking of two sides does not depend on a third); AlphaZero; Elo; social planner; Kuhn–Tucker conditions and multiplier (or write the Lagrangian in one line); mixed strategies; all-pay auction; conflict network; disagreement point; Harberger tax; units of compute (abstract units in the model; in Jones's data a unit of processing time).

## D. Prose

Cut: rhetorical questions used as paragraph openers (L167, L189, and the heading at L265 can become a statement); aphorisms that restate the previous sentence (L192, L564); "Four things stand out" / "Six consequences follow"; "comes out right in mechanism"; "with the confidence the toy models allow"; "What this article adds is…" (say what it does, once, plainly).
Keep the literal `TODO:` line; Dan wants open threads marked that way.

## E. Hand-back

Edit the file in place. Touch no other file. No git.
Reply with: anything in these rulings you disagree with or could not carry out, any new number you introduced (so I can check it), and the word count.
