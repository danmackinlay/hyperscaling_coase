# Red-team of the commitment model — handoff configuration

Written 2026-10-21 so that a session with none of this conversation's context can run the attack on the commitment model. Everything an attacker needs to be told is written out below, ready to paste into the Agent tool. The generic method is also packaged as the `argument-redteam` skill (dispatch and collation) and the `anchored-findings` skill (writing the result for Dan); this file is the specific configuration for this target.

## 1. Target

The claim under attack is the rebuilt thesis of `notebook/hyperscaling_coase.qmd`, as stated in `_plans/hyperscaling_coase_summary.md` under "Where we finished", items 4 to 8, and worked out in `_plans/hyperscaling_coase_commitment_model.md`. In one sentence: cheap compute converges bargaining to the full-rationality solution of whatever game the entitlement defines; in adversarial settings that solution is the classical bad one; the settings with good limits are those in which a rule binds one side's commitment; cheap, provable commitment on both sides produces standoffs; Krier's workable devices are such rules and his bargaining devices are not.

Nothing in the essay is to be edited by anyone in this round. The model file has not been attacked before. The previous round's files (`_claims.md`, `_redteam.md`, `_rebuild.md`) attacked the *old* thesis and must be kept away from the attackers, since they contain the author's conclusions.

## 2. The claims, named for the attackers

Attackers need stable labels; these are descriptive rather than numbered, and they do not appear in anything written for Dan.

- **The standoff claim.** With cheap, provable commitment available to both sides, bargaining over the pie of $6$ ends with incompatible commitments and no deal (cell D), citing Ellingsen and Miettinen 2008 and Crawford 1982.
- **The default-shift claim.** Humans sit near the no-commitment cell because believable commitment is costly for them; agents that can publish and prove their instructions move the default to the standoff cell.
- **The institutions-choose claim.** A liability rule is the factory-commits cell written into law; a union or no-side-deals rule is the residents-commit cell written into law; nothing else gets out of the standoff cell.
- **The convergence claim.** An agent with budget $c$ estimates what it needs with error $\sigma/\sqrt{c}$ and plays its cell's equilibrium on the estimates; as $c\to\infty$ play converges to the cell's exact outcome, so the residents' share goes to $0$ in the factory-commits cell, to $1$ in the residents-commit cell, and the standoff becomes certain.
- **The race claim.** At $k=1$ the residents' pact must form before the factory signs one resident; with speeds proportional to compute the pact wins with probability $\lambda_N/(\lambda_f+\lambda_N)$, unchanged by uniform cheapening.
- **The Krier mapping.** His digital union is the residents-commit cell and needs the pact enforced; his developer against every homeowner is the factory-commits cell; his option fee and reimbursing veto are liability rules, the factory-commits cell in law; his free-bargaining club is the standoff cell; his thermostat and parking cases are the no-commitment cell with custom fixing the split.
- **The yardstick claim.** Under unanimity nobody ends worse off than under no deal in any cell, so "median better off" cannot distinguish the cells; the residents' share $S$ can.
- **The bridge claim.** Better agents play closer to equilibrium and so strip the softening that human incompetence and norms have given the theorems; this is the thesis's bet and the model's section 8 lists what would make it wrong.

## 3. Rules for the round

- Six attackers, dispatched in parallel, each read-only, none seeing another's work. Use the Agent tool with `run_in_background: true` for all at once. (Five were configured on 2026-10-21; the sixth, 4g, was added the same day on Dan's objection that the convergence claim presumes a unique equilibrium, which fails in cells A and D even one-shot and in every cell under repetition.)
- Models mixed: two Fable, four Opus, as assigned below, so that no single model family's priors dominate and the assistant's own family stays in the minority.
- Every attacker reads the model file and the river section of the essay, and nothing else from `_plans/` except where a prompt says so. The cold reader reads no brief at all beyond one sentence of purpose.
- The advocate reads Krier's primary text through the Jina reader at `https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale`, never the plan's notes on him.
- Attackers mark confidence on every cited result: [sure], [likely], [unsure]. Carry the marks into the collation.
- Every number an attacker supplies is checked against the river, $h=(2,3,9)$, $\pi=10$ or $20$, before it is repeated anywhere. Round one repeated an attacker's false arithmetic once.
- The model's own section 8, "What would make this wrong", will anchor the briefed attackers. The cold reader is the control for that; weight its findings accordingly.

## 4. The prompts

Each prompt below is complete. Replace nothing.

### 4a. Common preamble, prepended to prompts 4b to 4e and 4g

> You are red-teaming a model written for a blog essay before anything is drafted on it. You are READ-ONLY: do not edit, create or delete any file, and do not commit. Your output is a report.
>
> Read, in the repository at /Users/dan/Source/livingthing: first, `_plans/hyperscaling_coase_commitment_model.md` in full; second, in `notebook/hyperscaling_coase.qmd`, only the section headed "## Someone pollutes our hypothetical river", for the river's model and numbers, ignoring HTML comments. Do not open any other file under `_plans/`; they hold the author's conclusions and an earlier review, and you must reach your own.
>
> For each claim you are assigned, give: a verdict, HOLDS, HOLDS WITH NARROWING, or FAILS; the strongest counter-argument you can make, naming results you are confident exist and marking each [sure], [likely] or [unsure]; the narrowing that would save the claim, if any; and what evidence or calculation would settle it. Check every number against the river's: harms $(2,3,9)$, profit $10$ or $20$, the consent rule as stated. Then list any claim outside your assignment that you believe is wrong, briefly. Then give the single most damaging objection to the model as a whole from your angle. Be adversarial; the point is to find the author's confirmation bias. No padding, no praise. As long as needed and no longer.

### 4b. The economist (model: opus)

> Your role: an economist in bargaining theory, contest theory and the theory of commitment. Attack the standoff claim, the default-shift claim, the convergence claim, and the mapping of the model's cells onto the literature. Specific questions:
> - State exactly what Ellingsen and Miettinen 2008 prove about costless versus costly commitment, which refinement they use, and whether "no deal with certainty when commitment is free" is their result or a paraphrase. Does Crawford 1982 give the same conclusion with revocation costs, and under what information assumptions?
> - In the standoff cell the model assumes both sides' revocation costs exceed the pie. If revocation costs are chosen rather than given, as in Crawford, what is the equilibrium choice, and does the standoff survive?
> - Abreu and Gul 2000: with frequent offers and commitment types, is the limit a war of attrition independent of protocol, and what decides it? Does that support or undercut the model's cell D?
> - The convergence procedure: an agent estimates with error $\sigma/\sqrt{c}$ and "plays its cell's equilibrium on the estimates". Is that a well-defined strategy in each cell? In the factory-commits cell with private harms, is the residents' share a monotone function of the factory's budget, and what is the margin formula?
> - The Coase conjecture: an offerer who cannot commit loses power as offers become frequent. The factory-commits cell assumes the factory can commit. Does the conjecture undercut that cell at machine speed, and what does it do to the model's claim that cheap commitment is symmetric?
> - Is "cheap commitment" a step change, available or not, or continuous in compute? If a step, "as budgets rise" is the wrong variable for the standoff claim; say so if it is.

### 4c. The cooperative game theorist (model: fable)

> Your role: a cooperative game theorist. Attack the residents-commit cell, the race claim, the yardstick claim, and the exhaustiveness of the four cells. Specific questions:
> - In the residents-commit cell the three residents must first agree how to split their six and then commit as one. Is that internal agreement stable? Which resident breaks first if the factory refuses, given harms $(2,3,9)$, and does the model's note that resident 3 "has the most to lose" hold?
> - Under unanimity the factory needs all three signatures. Does it ever gain from a side offer to one resident, and if not, what exactly does the no-side-deals rule do in this cell?
> - The race at $k=1$: is $\lambda_N/(\lambda_f+\lambda_N)$ the right form, what determines the residents' speed $\lambda_N$ for $n$ agents who must each agree, and is Olson's point that it is an incentive problem rather than a speed problem fatal to the race framing?
> - Does restricting who may combine with whom to a chain, which an earlier result showed gives a nonempty core at $k=1$, act as a commitment device in this model's sense, and if so which cell is it?
> - Are the four cells exhaustive? Consider partial commitment, revocation costs between zero and the pie, and asymmetric costs. Does anything qualitatively new appear?
> - Is the yardstick claim right that nobody ends worse off than under no deal in any cell under unanimity, and is the residents' share $S$ well defined in the standoff cell?

### 4d. The behavioural and experimental economist (model: opus)

> Your role: an experimental and behavioural economist, including the empirical study of negotiating software agents. Attack the bridge claim and the default-shift claim. Specific questions:
> - What do ultimatum, Nash demand and bargaining experiments say about human commitment and about rejection of insulting offers? Does "humans sit near the no-commitment cell" describe the evidence, or do humans commit through norms more than the model allows?
> - What do the agent-negotiation studies show: Magentic Marketplace (Bansal et al. 2025), Anthropic's Project Deal, convention formation in language-model populations (Ashery et al. 2025), algorithmic pricing collusion (Calvano et al. 2020; Fish, Gonczarowski and Shorrer; Assad et al. 2024)? Do current agents commit, satisfice, or play equilibrium? Name the studies you are confident of and mark the rest.
> - Is "better agents strip the softening" supported, contradicted, or untested? What would be the cleanest experiment to test the standoff cell with agents, and has anything like it been run?
> - If agents are built to be agreeable and never commit, the model's standoff cell is idle. How likely is that on current evidence, and for what stakes?

### 4e. The Krier advocate (model: fable)

> Your role: the strongest possible advocate for Seb Krier's "Coasean Bargaining at Scale". Before anything else, fetch his essay with the Jina reader tool at https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale and work from his text, quoting him briefly where you claim a misreading. Attack the Krier mapping and the institutions-choose claim. Specific questions:
> - Test the mapping device by device: the digital union, the developer against every homeowner, the option fee, the reimbursing veto, the bargaining club, the thermostat and parking cases. Does his text support each cell assignment?
> - Does he describe how the digital union's commitment is enforced against members who would deal separately? If he does, which cell is it?
> - Does his proposal to price stability against flexibility, by analogy with options markets, address the standoff cell directly? Make the strongest case that it does.
> - Is "Coasean bargaining at scale works at scale exactly to the extent that it stops being bargaining" fair to his text, given that he keeps the courts and calls the initial allocation a constitutional choice?
> - Which of the model's eight claims would he simply accept, and which would he deny, and on what grounds in his own words?

### 4g. The repeated-games theorist (model: opus)

> Your role: a game theorist whose fields are repeated games, equilibrium selection, and learning in games, including the theory of multi-agent learning dynamics. Attack the convergence claim and the model's one-shot framing. Specific questions:
> - The model says each cell has an "exact outcome" that play converges to as the budget $c\to\infty$. In which cells is the one-shot equilibrium actually unique? Treat cell A as a Nash demand game, or state what bargaining protocol would make its outcome unique, and treat cell D in the light of Ellingsen and Miettinen 2008, whose abstract states that when commitment attempts never fail three outcomes survive iterated strict dominance, two of them giving all the surplus to one player. Where the equilibrium set is not a singleton, is "plays its cell's equilibrium on the estimates" a defined strategy at all, and what does more compute converge to?
> - Suppose the river negotiation recurs: the same factory and residents set terms every year, or the same agents meet across many catchments. State what the folk theorem (Fudenberg and Maskin 1986 and its relatives) implies for the set of subgame-perfect equilibrium payoffs at each $k$, on the river's numbers. Do the factory's take-it-or-leave-it outcome, the residents' union outcome, and the standoff each become sustainable as equilibria irrespective of who can commit? If so, what, if anything, does the four-cell table still determine?
> - Does repetition make the residents' pact self-enforcing without any external rule, at $k=1$ and at $k=3$, and at what discount factor on $h=(2,3,9)$ with $\pi=10$ or $20$? If so, the model's statement that the pact "has to be enforced among the residents" by a rule is weakened; say by how much and what remains of it.
> - Equilibrium selection by capable agents. What do the theory of learning in games (Hart and Mas-Colell on uncoupled dynamics; no-regret dynamics and coarse correlated equilibria; Young's adaptive play and stochastic stability in the Nash demand game; Binmore, Samuelson and Young on equilibrium selection in bargaining) and the empirical learning-agent literature (Calvano et al. 2020 and its successors) say about which equilibrium very capable agents converge on, and whether an unbounded budget on all sides settles the selection at all? Give the strongest case that it does, for instance that stochastic stability selects the Nash bargaining solution, and the strongest case that it does not.
> - Complexity-constrained repeated games: Rubinstein 1986, Abreu and Rubinstein 1988, Neyman 1985, Ben-Porath 1993, Gilboa and Samet 1989. Does bounded compute act as a commitment device, so that the model's two budgets, the revocation cost $r$ and the operations budget $c$, are not independent? Can a side with far more compute secure a commitment-like advantage in repeated play, or does the advantage go to the more limited side? Mark confidence on each result.
> - Is the one-shot framing defensible for the cases the model is about, a factory siting decision, a developer buying out every homeowner, so that the repeated-game objection narrows the thesis rather than overturning it? State the narrowing precisely.
> - What is the correct statement of the convergence claim, if any survives? For instance: "as budgets rise, play converges to some equilibrium of the game the entitlement defines, selected by dynamics the entitlement does not control." Say whether a statement of that kind still gives compute any role in the essay's argument, or whether it reduces the essay to equilibrium selection with a preamble about agents.

### 4f. The cold reader (model: opus; this prompt stands alone, no preamble)

> You are reviewing a short model written for a blog essay. You are READ-ONLY: do not edit, create or delete any file; do not commit. Your output is a report.
>
> Read, in the repository at /Users/dan/Source/livingthing: `_plans/hyperscaling_coase_commitment_model.md` in full, and in `notebook/hyperscaling_coase.qmd` only the section headed "## Someone pollutes our hypothetical river", ignoring HTML comments. Open nothing else.
>
> The model is meant to show when cheap bargaining agents help or hurt the people bargaining. You know nothing else about the author's intentions and should not guess at them. Report, in this order: what the model claims, in your own words; what it assumes without arguing, that an expert in economics or game theory would refuse to grant; any place where it contradicts itself or the river section; whether its numbers are consistent with the river's, harms $(2,3,9)$ and profit $10$ or $20$; which of its claims depends on results it names but does not state; and the single most damaging objection to it as a whole. Quote the sentence you object to each time. Name results only when you are confident they exist, and say when you are unsure. Be adversarial; do not pad; do not praise.

## 5. Collation

When all five have returned, write `_plans/hyperscaling_coase_commitment_model_redteam.md` with: a verdict table, claims as rows and attackers as columns; each attacker's report compressed faithfully with its confidence marks kept; and a convergence section that weights a finding by whether two or more attackers reached it independently, or the cold reader reached it alone, and discounts restatements of the model's own section 8. State plainly which claims fail, which narrow, and which hold. Then the decision gates:

- If the standoff claim fails, the thesis loses its headline and reverts to "institutions choose the cell", which Krier does not deny.
- If the convergence claim fails, "compute" does no work in the thesis and the essay is classical bargaining theory with a preamble.
- If the Krier mapping fails on the option fee and reimbursing veto, section 7 of the model goes and the essay's disagreement with him narrows to scale.
- If the bridge claim is contradicted by the agent evidence, the thesis is a bet against current evidence and must say so.

## 6. Writing it for Dan

Do not hand Dan the collation. Write `_plans/hyperscaling_coase_commitment_model_findings.md` under the `anchored-findings` skill: one self-contained paragraph per finding, each quoting the sentence of the model file it is about, stating the point in plain words, running it on the river's numbers, defining every term in the sentence that uses it, naming the attacker by brief, and ending with what the model should do. No claim labels from section 2 above in that document. Then the mechanical quote check against the model file, then a cold anchor test by an agent that has read only the model file and the findings document, looped until nothing structural remains, which took two passes last time. Expect it to come out longer than estimated; last time 3,000 became 8,800.

## 7. Cost

Six attackers at fifteen to twenty-five minutes each in parallel; collation about an hour; the findings document and its two test passes about two hours. Model preferences: Opus for anything written for Dan to read; attackers mixed as above; Sonnet only for mechanical work such as citation ingestion, which is not part of this round.

## 8. Run record (2026-10-21)

Run the same day it was written. Six attackers dispatched in parallel from one session with the prompts above verbatim (4b–4f at once; 4g about forty minutes later, on Dan's objection). Durations and tokens from the harness: cold reader 15.5 min, 177k; cooperative theorist 16.2 min, 155k; Krier advocate 17.6 min, 163k; behavioural economist 23.1 min, 325k; economist 25.7 min, 278k; repeated-games theorist 29.8 min, 290k. All six returned reports in the requested form with confidence marks; none wrote to the repo. Verbatim reports were saved to `_tmp/hyperscaling_coase_commitment_redteam/` (gitignored) together with the collator's notes on the primaries. The collator read Ellingsen and Miettinen 2008 (open LSE copy) and Crawford 1982 (JSTOR PDF supplied by Dan) in full before and during the round, and the abstracts of Miettinen and Vanberg 2025, Abreu and Gul 2000 and Chlaß and Miettinen 2026; the Krier mapping gate was decided on the advocate's reading of his text. Collation: `hyperscaling_coase_commitment_model_redteam.md`, 17,200 words. Findings for Dan: `hyperscaling_coase_commitment_model_findings.md`, thirty anchored paragraphs, about 14,700 words after four anchor-test passes by fresh Opus agents (the handoff estimated two): pass one found five phrases quoted from outside the model, seven undefined terms running through many paragraphs, missing reviewer names and one substantive error, that in cell B the residents' share of each deal falls monotonically and only their expected surplus is hump-shaped; pass two found the proposed thesis contradicting three findings on the residents' remedy and a wrong count of residents below no deal at $k=1$; pass three found the summary sections disagreeing with the findings on what compute does in the standoff cell and dropping the conditions on the standoff's uniqueness; pass four confirmed the arithmetic, the quotations and the reviewer names and left a batch of consistency items across the summary sections, two of them substantive (cell D does have a single outcome under the standoff's five conditions, so "only B and C" needed that qualifier throughout; and a rule can impose a holdout cost larger than the revocation cost, so the reimbursing veto can fire as an exit although the model's own second falsifier cannot), which were applied without a fifth verification pass; a fifth pass is the obvious next check if the document is to be built on. The quote check was clean on every run. Per Dan's instruction the report to him was written by a low-context Opus agent that read only the findings and the model; the first such report, run before the pass-two fixes, listed exactly the passages pass two had flagged, which is independent evidence that the test and the reader see the same things. Two reviewer numbers failed the collator's check and were not repeated: a standoff probability of 98% at a posting cost of 0.06 (the formula gives 96%) and the economist's cell-A S given a deal at the largest error, an artefact of the rule's specification. All four decision gates tripped: standoff, convergence, Krier mapping (on the reimbursing veto, the developer and the club) and bridge.
