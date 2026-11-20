---
name: argument-redteam
description: |
  Red-team an essay's argument before rebuilding it on reviewer findings — the claims ledger, briefed attackers plus one unprimed cold reader, primaries rather than the author's notes, model diversity, and collation by independent convergence. Use when Dan says "red-team this", "attack the argument", "stress-test the thesis", "find our confirmation bias", or when a thesis has been restated in conversation and a rewrite is about to be built on it. Produces `_notes/<slug>/claims.md` and `_notes/<slug>/redteam.md`; never edits the essay. The readable statement of what it finds is the `anchored-findings` skill.
---

# Argument red-team

**The author's and the assistant's confirmation bias run the same way, so the check comes from readers who share neither context.** Measured on `hyperscaling_coase` (2026-10-15): five read-only attackers, one given the essay alone, converged independently on two findings that reversed a thesis three days of conversation had built. The essay was not touched until the findings had been collated and restated for a human.

## 1. The ledger, written for the attackers

`_notes/<slug>/claims.md`; Dan does not read it. The thesis as three or four numbered statements with their metrics defined once; the model in a paragraph; every claim numbered and grouped by the essay section it lives in, each with statement, assumptions, evidence, scope and *what would refute it*; the author's own **known weak points**, the least welcome first; a paragraph naming which attacker gets which claims. Every piece of evidence must exist in a file: two "worked examples" cited on the first run existed only in chat.

## 2. The attackers

Three to five **briefed by field** so every claim has an attacker whose literature covers it, plus **one cold reader** given the essay body alone, no ledger, no plan, no editing comments, one sentence on the essay's purpose. The cold reader is the control for the ledger's own anchoring. Template and variants in `references/attacker-brief.md`.

Each is read-only, backgrounded, parallel, and returns per claim: **HOLDS / HOLDS WITH NARROWING / FAILS**; the strongest counter, naming results only when confident and saying when unsure; the narrowing that saves the claim; what would settle it. Then claims outside its list it thinks wrong, and the single most damaging objection. Those last two are where unanchored findings surface.

Split the roster across Opus and Fable, the assistant's own family in the minority, and record which ran where. Dan's Opus-for-prose rule does not apply here; diversity does.

Controls, each of which bit once:

- A partisan reads the **primary text**, not the plan's notes on it. The notes on Krier had filed his two central devices as voluntary; they are state-backed. Send the URL; demand quotation.
- A plan's "verified facts" are the author's conclusions. Attackers pointed at them treat each line as a claim under test.
- "Be adversarial" manufactures objections: weight by named results and convergence, and count HOLDS as evidence.
- Hedges ("[likely]", "I believe") survive verbatim into the collation.
- **Mission and state before anything else.** Where the essay has a `_notes/<slug>/mission.md` and a state file, every brief carries the mission question verbatim and names the state rows it targets, and every attacker ends with its own answer to the question on the model's numbers and a proposed delta to the state table, before any verdict on claims. The collation opens with the delta it proposes, and the report to Dan is written from the state by a low-context writer, not from the collation. The commitment-model round (2026-10-21) attacked claims without a mission anchor and produced verdicts on scaffolding; the mission and state pair is the fix (`_notes/hyperscaling_coase_mission.md`, rules of use).
- Published critiques of the target are summarised in `_notes/<slug>/prior_critiques.md` with the overlap against the essay's claims, and that file goes to the partisan and to one attacker briefed to flag every passage that restates a published critique without citing it or claims novelty for a point already in print. Dan's rule (2026-10-21): reprise or quantify only with citation; new critiques are better.
- A thesis that claims a limit, a convergence or an "exact outcome" needs an attacker in equilibrium selection and learning in games. On the commitment model (2026-10-21) that attacker was added mid-round on Dan's objection, and found that the two load-bearing cells had no unique equilibrium to converge to and that repetition dissolved the table.
- The collator reads the primaries the target cites before the reports arrive, and checks every number a report supplies against the model before repeating it. The commitment model's central citation had been adopted from a previous round's paraphrase and was wrong once read; two reviewer numbers failed the check.

Four attackers on a 14,000-word essay: 15 to 35 minutes each in parallel, 200k to 340k tokens each.

## 3. Collation by convergence

`_notes/<slug>/redteam.md`, template in `references/collation-template.md`: a verdict table, each report compressed with its numbers and hedges intact, and a **Convergence** section written only when all are in. A finding counts when **two or more attackers reached it unprompted, or the cold reader alone**. Order: those; then two-attacker findings; single-attacker findings worth keeping; **what survives**; hygiene (dead links, miscitations, wrong notes about the target). A finding that restates one of the ledger's own weak points counts for less.

**Check every attacker number against the model before building on it.** One reader called a division a Pareto improvement that left the firm worse off; the readability pass caught it, the collation had not.

Then stop. The next step is `anchored-findings`. The decision between rebuilding on the findings and narrowing to what survives is Dan's, and its honest form is two short descriptions of two essays.
