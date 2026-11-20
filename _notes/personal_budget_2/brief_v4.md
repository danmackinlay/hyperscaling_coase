A cold reader went through your revision of `_plans/hyperscaling_coase_personal_budget_2.qmd`; here are my rulings, to apply in place under the same rules as before (no maths or numbers changed, sentence per line, -ize, one term per concept, no git, no other files). Line numbers are the reader's and may be off by a few. Aim for no net growth: these are replacements, not additions.

A. Two routes to sufficiency (most important). The article says "the sufficiency world is $r=0$" (about L202, L208, L736, L751), but in Result 9 compute stops mattering with $r>0$ because effective compute is capped at $G(n)$. Those are different mechanisms. Fix:
- The sufficiency world stays defined by its production function and four properties.
- Say once, where $r$ is introduced as the free parameter (about L202–210): within the contest success function, sufficiency arises on a matter in two ways. Either $r=0$, so compute never shifts shares; or $r>0$ but both sides can afford the compute that solves the matter outright, so compute shifts shares only below that level. The second is a property of a matter, not of the whole economy.
- L202: "Compute stops mattering, $r=0$, in a game both sides can solve outright" must not equate the two; say compute stops mattering in a game both sides can solve outright, which has the same effect on that matter as $r=0$.
- Result 9: add that $G(n)$ here plays the part of the satiation level $\bar c$ (this also answers the reader's point that "satiation" was defined at $\bar c$ and then used at $G(n)$).
- L736 ("Results 1 to 9 collapse to the sufficiency world at $r=0$, and what makes $r=0$ is …"): restate as: Results 1 to 8 reduce to the sufficiency world at $r=0$, and, by Result 9, on any matter both sides can solve.
- The line about threats (about L675) may keep "at $r=0$".

B. Cruxes section. Restructure into two short groups with one lead sentence each.
 Group 1, "which world a matter is in":
 - Decisiveness $r$, measured on matters neither side can solve outright (otherwise the measurement returns zero for the wrong reason). $r=0$ gives sufficiency everywhere. $0<r\le1$ gives the results here. $r>1$, where Jones's fitted 1.3 lies, is outside the methods used here, and Hirshleifer's result suggests wealth then buys advantage. Measurement: the Project Deal design with compute varied on a fixed model.
 - The fraction of matters, weighted by surplus, that both sides can solve with the compute they have, and how much of each matter's detail is set by circumstances ($n_0$) and how much by the contract. Say plainly that sufficiency is decided matter by matter, so the answer may be "some matters in each".
 Group 2, "which results apply within the contest world":
 - Verifiable compute use (restraint). Give a measurement: whether an agent can prove an upper bound on the compute it used, which today's proofs of work done do not provide.
 - Pledgeable bargaining gains. Do not state it as a result; say what decides it (whether a lender can verify stakes and collect from gains) and that the nearest present-day evidence is which legal claims litigation funders will and will not finance. Keep "not modelled here, open question" and "decides who gets what, not waste".
 - Reusability $\phi$. The current measurement ("how many matters … one analysis serves") measures $M$, not $\phi$. Replace: $\phi$ is the elasticity of effective compute per matter with respect to the number of similar matters handled, so it can be measured by how a representative's results per dollar improve with its caseload. At $\phi=0$ scale gives nothing; for any $\phi>0$ the advantage grows with $M$ as in Result 8.

C. Attributions to Krier. Wherever the text says his words "treat" or "frame" something, or state his expectation more broadly than the quotation does, mark it as my reading or narrow it to what he says:
- L159 "Krier's billionaire's phone treats bargaining like using a phone: a task with a ceiling" → the remark, read as a claim about bargaining, describes a task with a ceiling.
- L220 "That answer treats the compute spent…" → "Read as a claim about all the compute spent on a bargain, that answer…".
- L504 "He frames the gap to be closed as one of access to a cheap good." and L115 "the subsidy which puts everyone on an equal footing": his words are "prevent cost barriers"; do not attribute "equal footing". Say what he proposes and then what the contest world implies.
- L559 "Krier does not expect concentration among agent providers" → he expects weak network effects and easy switching among providers; then L595 should say reuse of bargaining work is a separate source of scale, without "not a network effect but".
- L603 "The phrase treats the detail of a contract as something both sides benefit from and can equally handle." → drop the attribution; say that whether both sides can handle the detail is what decides whether compute matters. Also avoid "the detail of a contract" before detail is defined at L608.
- L684 remove the scare-quoted "computational verification"; say it requires a court to judge purpose, which is more than verifying that a term was met.
- L704 many-parties table row: replace the quotation "a coalition 'in a nanosecond'" in the sufficiency column with plain words (coalitions form at negligible cost).
- L59 and L743 about the state: say the remedies are rules about how bargaining is conducted, which go beyond enforcing contracts and entitlements; do not say what Krier's state does or does not include.
- L543–545: keep both facts, but not as concession-then-reversal. One sentence: the allocation removes the trap and restores the Gini coefficient; next sentence: mean wealth and waste, plainly.

D. Small repairs.
- L458 "the trap of the kind described in the next section" → "in the section on wealth over time".
- L703 table row "detail of a matter", contest column: the detail of a matter is set by circumstances and the drafter; what is bounded by $\log_\gamma(C/G_0)$ is the detail a principal can solve. Sufficiency column: every matter is one both sides can solve (not "unlimited").
- L623–627 drafter paragraph: add that the drafter's choice matters only when the circumstances alone are within what the other side can solve, $n_0\le n_i$; if $n_0>n_i$ the matter is already beyond it whatever the contract says. Do not write as if the contract alone sets $n$.
- L76 "the agent-bargaining world" → "bargaining between agents" (it is a third name for a world).
- L47 "Items 2 and 3" → "Items 2 and 3 of this summary". L463 "(1, 2 and 5)" → "Results 1, 2 and 5".
- L364: at the first use of "in end-of-period terms", add "that is, dollars spent multiplied by $R$".
- L368 "wealth above the parity threshold below buys no strength" → "wealth above a level defined next, the parity threshold, buys no strength" or similar, so the term is not used before its definition.
- L43 "a quarter at $r=1$ when the stakes are evenly divided at equal compute" → simpler: "a quarter at $r=1$ and merit shares of one half" is not available because merit share is undefined there; use "a quarter at $r=1$, when equal compute would split each bargain evenly".
- L57 "keep half of its net gain": make "its" explicit (the net gain from bargaining that the sufficiency world gives).
- L540 "the parity threshold is $Rw\ge E/4\approx2$" → "the parity threshold is $Rw=E/4\approx2$".
- L542: state the 0.2% directly (only 0.2% of principals end between the two thresholds).
- L210–211 "That makes it a conservative choice: the case $r>1$ is untested, and probably worse." → say the case $r>1$ is not solved here and that Hirshleifer's result, discussed in the section on wealth over time, suggests it favours the richer side.
- L323 delete "I checked these on random networks of 60 principals at $r=0.5$ and $r=0.9$." (the Summary already says how results were checked). Keep the Summary's script path and the literal TODO line.
- L181 uses "strength" for Elo playing strength while *strength* is later a defined term ($a_i$); say "playing ability" or "rating" there.

Not accepted: merging "bargain"/"transaction"/"matter" (bargain is the informal word before the definition; leave), and removing the script path.

Reply with a short list of anything you did differently from these rulings and why, plus the net word change.