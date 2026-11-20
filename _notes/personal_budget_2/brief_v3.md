You are revising one academic article in place: `/Users/dan/Source/livingthing/_plans/hyperscaling_coase_personal_budget_2.qmd` (about 820 lines). Read all of it first. It responds to Séb Krier's essay "Coasean bargaining at scale". The author (Dan) has read the draft and asked for four changes. Your job is a clear, human presentation: plain literal prose, no ornament, no rhetorical flourishes, no mixed metaphors. Change only what the four items need. Do not alter any mathematics, number, result, table value, citation or quotation except where an item below says so. Net growth should stay under about 350 words; cut where a reframed passage makes an old sentence redundant.

Hard rules for this repo:
- One sentence per line in prose (the file already follows this; keep it).
- Oxford spelling with -ize endings (summarize, realize), British otherwise.
- No colons in headings. First person singular "I" for the author's own judgements.
- Define every coined term at first use and then use exactly one term per concept.
- Do NOT read any other file whose name starts with `_plans/hyperscaling_coase_` (the author wants this article written without reference to his earlier essays). Do not run any git command. Do not create other files. Do not touch `<!-- -->` comments.

## Change 1. Name the benchmark world; stop attributing it to Krier

At present the article assembles a production function from two of Krier's sentences and calls it "the Krier benchmark" (also "the benchmark", "the benchmark I attribute to Krier", $Y_i^K$, $w^{**}_K$). Dan's instruction, verbatim in substance: we should sound as if we are inspired by Krier and want to see what his method assumes about the world; we are not attempting to be adversarial but to have a productive engagement; so do not call the benchmark what Krier said, but make up a name for this world so that we can find our cruxes about it.

Use this name: the *sufficiency world*. Define it at first use, roughly: a world in which a fixed amount of compute per matter is sufficient, so that more of a principal's own compute adds nothing and what the other side spends does not matter. Say plainly that Krier's essay does not state a production function, that two of his sentences suggest one, and that I name the world in which it holds so that we can ask which of its properties his conclusions need and which of them hold. He may not accept every property; that is the point of naming it.

Name its counterpart too, once, where the contest success function is introduced or where the two are first contrasted: the *contest world*, a world in which a principal's share of a matter depends on its compute relative to its opponent's. Use it wherever the article now says things like "in the models here" as the opposite pole, where that reads naturally (table column headers, the simulation table rows already say "contest").

Then replace every "Krier benchmark" / "the benchmark" / "benchmark's" with the one term (e.g. "the sufficiency world", "the sufficiency world's Gini coefficient", "under sufficiency" where a short form is unambiguous, but prefer the full term). Section heading "The Krier benchmark" becomes something like "The sufficiency world". Rename the symbols: $Y_i^{K}$ → $Y_i^{\mathrm{suf}}$ and $w^{**}_K$ → $w^{**}_{\mathrm{suf}}$, everywhere including tables and the notation appendix (add a row for $Y_i^{\mathrm{suf}}$ if helpful). Keep "satiation level" ($\bar c$) and the four property names (satiation, no rivalry, compute only creates surplus, cheap floor) as they are. The simulation-table row "Krier benchmark ($r=0$)" becomes "sufficiency world ($r=0$)". Phrases such as "Krier's billionaire's phone" where they refer to his actual remark stay, since that is his.

## Change 2. Tone: productive engagement, organized around cruxes

The facts and results stay exactly as they are, including the ones unfavourable to the sufficiency world. What changes is the stance.
- Front matter `description:` and the opening paragraphs: replace the "test of / I doubt that the resulting world is the good one Krier describes" stance with: Krier's essay is the starting point; I take the proposal seriously, ask what world it presumes, name that world, and then build toy models to find which measurable quantities decide whether we are in it. Keep it short. Keep the definition of principal and the set-up sentences (compute budget, many bargains, selfish opponents with perfectly aligned agents computing to their own limits, gains spent on compute or ordinary uses), since those were Dan's brief.
- "What we concede to Krier" → a heading and wording that reads as taking his institutional premises as given (e.g. "The institutions we take as given"), not as concessions in a dispute. "The models concede Krier …" in the Summary likewise.
- Wherever the text scores a point ("is right for some … and wrong for the rest", "property (iv) fails", "does not cover", "which flatters it", "a planner's job of a kind his essay sets out to avoid"), keep the finding but state it as what holds in which world, without the scoring. Example: "This is the cost Krier says will 'approach zero asymptotically', and in this model it does not: property (iv) fails." could become a statement that in the sufficiency world this cost vanishes with $p$ and in the contest world it is a fixed fraction of stakes. Do not weaken or hedge any result; just drop the adversarial register.
- Add a short section titled "Cruxes" (place it just before or just after "Verdict", or fold the current "Some measurements and extensions would change the conclusion" list into it; your judgement, but there must be exactly one such list, not two). It lists the quantities whose values decide between the sufficiency world and the contest world, each in one or two plain sentences saying what value would put us in which world and how it could be measured. Draw them only from what the article already contains:
  1. Decisiveness $r$ for bargaining agents at a fixed model (the Project Deal design with compute varied).
  2. Whether the matters people actually face can be solved outright with the compute both sides have, and who sets their complexity (see Change 3).
  3. Whether agents can verify one another's compute use, which decides whether restraint can be sustained.
  4. Whether bargaining gains can be pledged to a lender; this decides the results on who gets what, not the results on waste. Keep the article's existing statement that this market is unmodelled and an open question.
  5. How much bargaining work is reusable across matters ($\phi$).
  Keep the remaining extension items (solve $r>1$; the risk item in Change 4) in the Limitations list.
- "Other responses to Krier": "objected" → neutral ("responded"). Keep the content.
- The "Verdict" section may be renamed if a calmer heading fits (e.g. "Where this leaves the proposal"); keep its three comparisons and all its content.

## Change 3. What must be simple is the matter, not the contract alone

The draft says compute stops mattering "when a contract is simple enough for both sides to work out the best outcome completely". Dan's correction: it is a combination of contract and circumstances; we may collapse the two into one number but must say so. Fix every place this appears: Summary item 7; the paragraph beginning "Compute stops mattering, $r=0$, in a game both sides can solve outright"; the whole "Contract detail" section including Result 9; the standard-form remedy; the tally-table row "contract detail"; the sentence in the Verdict "what makes $r=0$ is a contract of detail small enough for both sides to solve".

The content to state, plainly:
- What a party's agent has to solve is the bargaining game on a matter. How hard that game is depends on the terms of the contract and on the circumstances: what each side wants and knows, what each could do instead, and the states of the world the agreement has to cover.
- The model collapses both into the single number $n$. Say that this is a simplification. Write $n_0$ for the part set by circumstances, so that $n\ge n_0$; the drafter chooses only how much detail the contract adds beyond $n_0$.
- Consequences to state in one sentence each: Result 9's satiation holds for a matter of fixed $n$, not for a contract considered apart from its circumstances; and the standard-form right can cap what the contract adds but not $n_0$, so it restores satiation only on matters whose circumstances alone are solvable within the basic compute allocation, $G(n_0)$ within it.
Keep the section heading "Contract detail" or change it to something like "How complex a matter is" if that reads better; keep the term *detail* for $n$ but make its definition cover both sources.

## Change 4. Record one deferred question about risk

In "Limitations and tests", the sentence "Principals are risk-neutral, …" and the bullet "Add risk aversion." Expand, in about three sentences total: the models treat the share as a division of the surplus, which is the same as a probability of winning the whole surplus only for a risk-neutral principal or one with many small independent matters. If the contest decides who wins, a liquidity-constrained principal that puts all its savings into compute on one large matter is making an all-or-nothing bet, and a principal that cares about the long-run growth of its wealth, as under the Kelly criterion, would spend less. That would move the constrained principal's optimum and the parity threshold; it is not modelled here.

## When done

Reply with a short plain list: what you changed under each of the four items, the line numbers of the new definitions (sufficiency world, contest world, $n_0$) and of the Cruxes section, the approximate net word change, and anything you chose not to do and why. Do not summarize the article.