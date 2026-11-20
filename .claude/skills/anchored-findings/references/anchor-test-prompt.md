# Anchor test prompt

One fresh agent per pass (a new `Agent` call, never a resumed one), `run_in_background: true`. Fill the angle brackets. Add the contradiction checklist from the previous pass's report, or from your own reading, under "Then check specifically".

---

You are testing whether a document is readable by someone who has read one essay and nothing else. You are READ-ONLY: do not edit, create or delete any file; do not commit. Your output is a report.

Read exactly two files in the repository at <repo path>, and nothing else, in this order:
1. `<source path>`, from the start to the heading "<first working-notes heading>". Stop there. Ignore every HTML comment (`<!-- ... -->`).
2. `<findings path>`, all of it, ignoring its HTML comments, which are provenance notes not meant for the reader.

Do not open anything else under `_notes/`. You have no knowledge of the discussion that produced these files, and that is the point.

The document claims that every paragraph under "<findings heading>" stands alone: it quotes the essay sentence it is about, states its point in plain words, runs it on the essay's own numbers, defines every technical term in the sentence that uses it, and ends with what the essay should do. Test that mechanically, paragraph by paragraph, for all <N> findings:

- **Anchor.** Quote the essay passage the paragraph is about, with the section heading it sits under. If you cannot find it, say ANCHOR MISSING and quote the phrase you searched for. Where the document names a section of the essay, check the name is a real heading.
- **Restatement.** Restate the paragraph's claim in two sentences of your own.
- **Guessed terms.** List every term, name or symbol whose meaning you had to guess because neither the paragraph nor the essay defines it. The document names its reviewers by their briefs in its preamble; those count as defined.
- **Unanchored sentences.** Quote any sentence that refers to something you could not locate in the essay or in the paragraph itself, or that depends on another finding without restating what it needs.
- **Numbers.** Where the paragraph does arithmetic on the essay's example, check it against the essay's numbers, <list them>, and say whether it is consistent. Do not check claims about the literature.

Then test, more briefly, the sections "<thesis heading>" and "<proposed-order heading>" for guessed terms and for any claim no finding supports.

Then check specifically whether the document contradicts itself on any of these points, quoting both sides if so:
<(a) ... (g) ...>

Finally: the three paragraphs hardest to follow, one sentence each on why. Be literal. Do not judge whether the findings are correct, only whether they can be read. No praise, no padding.
