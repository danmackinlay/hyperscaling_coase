---
name: anchored-findings
description: |
  Turn a multi-agent analysis (reviewer reports, a red-team collation, a long thread of coined vocabulary) into a findings document a human can read in one sitting — one self-contained paragraph per finding, each quoting the source sentence it is about, run on the source's own worked example, every term defined where used, provenance in comments — then a mechanical quote check and an anchor test by a cold agent, looped until nothing structural remains. Use when Dan says "I've lost the chain of referents", "I can't parse this", "make this human-digestible", or before any rewrite is built on reviewer findings. Judges readability, not truth; the `argument-redteam` skill judges truth.
---

# Anchored findings

**A collation written for the agents that produced it is unreadable by the person it was for.** On `hyperscaling_coase` (2026-10-15) the red-team collation ran on four layers of vocabulary, the essay's, the assistant's, the ledger's and each reviewer's; Dan picked a sentence at random and could not say which argument it belonged to, and "floor" in it meant something different from "floor" in the ledger it summarized. The fix was a different unit and a test, not a shorter summary.

## The delta first

Where the essay has a mission and state pair (`_notes/<slug>/mission.md`, and a state file holding the table of conditions), the findings document opens with a delta block, `Delta to state, <date>: rows changed …; rows added …; rows retired …; mission touched: no | yes, because …`, and its findings are ordered by the rows they move, not by how badly they damage the artefact under review. The commitment-model round (2026-10-21) ordered thirty findings by damage to a scaffolding model and lost the one that answered Dan's question; a reader with no context then summarised the damage and not the answer.

## The unit

One paragraph per finding, 200 to 350 words, readable by someone who has read the source and nothing else. Each paragraph:

1. **Quotes the source sentence it is about**, verbatim, under its real heading. An informal name may follow a real heading, never replace it.
2. **Says what is wrong in plain words.**
3. **Runs the point on the source's own example and numbers**, on the page: "frontages $(1,1,3)$ and a quota of $4$", not "the frontage game"; derive any number the reader cannot check ("$\pi-h_1=8$").
4. **Defines every technical term in the sentence that uses it, every time.**
5. **Ends with the consequence as an action**, keep, narrow, rewrite or delete, and the replacement claim.

Across paragraphs: no references forward or back, redundancy over indirection; no coined terms, the scaffolding vocabulary retired by name at the top; symbols only where the source introduces them or where introduced and defined on the spot; third parties quoted via the reviewer who read them, never paraphrased from a paraphrase; reviewers named by brief in the preamble, with counts that match; provenance in HTML comments; the source's order, with any proposed new order last and mapped by real headings; a proposed thesis above the findings, marked proposed. Findings sharing an anchor merge. Expect two to three times the estimated length: 3,000 estimated, 8,800 delivered.

## Who writes, with what in context

**The writer holds the most context; the tester holds the least.** On the first run the writer was the main session, holding every reviewer report in full, the source, the model, and Dan's complaint with the sentence he had picked; the same session had written the unreadable collation the day before, so the model was not the variable. Never write from a collation, which is the thing being replaced. If the writing is delegated to a fresh session, hand it the full reports, the source, the example, the complaint and the rules, and expect its first draft to fail the test. Dan's Opus-for-prose rule applies to the essay afterwards; here the test is the quality control.

## The quote check

Every phrase quoted from the source must be in the source. Regex pairing of double quotes fails, so check an explicit list:

```bash
f=<source path>; miss=0
while IFS= read -r q; do grep -qiF -- "$q" "$f" || { echo "MISSING  $q"; miss=1; }; done <<'LIST'
<one quoted phrase per line>
LIST
[ $miss -eq 0 ] && echo "all quotations found"
```

It caught four misquotes from memory and one sentence Dan had rewritten mid-session.

## The anchor test

A **new** agent each pass, read-only, given exactly two files, the source without its comments or working notes, and the document without its comments, and no knowledge of the discussion. Per finding: the anchor quoted or ANCHOR MISSING; a two-sentence restatement; every guessed term; every sentence it could not tie down; arithmetic against the source's numbers. Then the thesis and proposed order for guessed terms and unsupported claims; a contradiction checklist from the previous pass; the three hardest paragraphs. Prompt in `references/anchor-test-prompt.md`. Fix, re-run the quote check, re-run the test.

Measured: pass one found a missing anchor, two wrong numbers (one copied from a reviewer), labels that existed only in editing comments, reviewers the preamble never named, and seven contradictions, two of which changed the thesis paragraph; pass two found none of those. Two passes; 15 to 20 minutes and about 230k tokens each.

## Pitfalls, each of which happened

One word meaning three things across layers. Section labels from the editing process. "The previous finding" pointing at the wrong one after a reorder. Forward references in the opening paragraph. Reviewer arithmetic copied unchecked. Thesis claims no finding carries. Working files named as if the reader could see them. "Four readers" followed by three names.

## What it is not

Not a judgement of truth, and it must not reopen the argument; that is `argument-redteam`, upstream. A plan artefact in `_notes/`, not essay prose; the essay that follows is written under `dan-voice`, with one Opus agent per passage given one placeholder, the relevant plan sections and the whole essay, and de-slopped under `slop-hunter`.
