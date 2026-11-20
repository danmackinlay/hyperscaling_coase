# Attacker brief template

Fill the slots in angle brackets. One agent per brief, `run_in_background: true`, read-only.

---

You are red-teaming the argument of a blog essay before it is rewritten. You are READ-ONLY: do not edit, create or delete any file, and do not commit. Your output is a report.

Read, in this order, in the repository at <repo path>:
1. `_notes/<slug>/claims.md` in full. The thesis, the objects, the numbered claims, and the known weak points.
2. In `_notes/<slug>/plan.md`, the sections <list the sections: the model, vocabulary, and nothing that records the author's conclusions unless the brief says to treat them as claims under test>.
3. The current draft `<essay path>` is background; consult it where a claim's evidence points there.

Your role: <field, e.g. "an economist whose fields are contest theory, bargaining theory, mechanism design and political economy">. Attack these claims: <list>. Specific questions you must address:
- <one pointed question per claim, phrased so that HOLDS is a possible answer>

Before anything else, read `_notes/<slug>/mission.md` in full; the question it states is the question you are answering, and the claims below are instruments for it. Your report ends with (a) your own answer to that question on the model's numbers, and (b) a proposed delta to the state table in `<state file>`: rows changed, added or retired, each with a status (theorem, computed, argued, empirical, open, refuted) and a source.

For each claim: a verdict, HOLDS, HOLDS WITH NARROWING, or FAILS; the strongest counter-argument you can make, naming papers and results you are confident exist and saying so when you are unsure; the narrowing that would save the claim, if any; and what evidence would settle it. Then any claim outside your list you believe is wrong, briefly. Then the single most damaging objection to the thesis as a whole from your angle. Be adversarial: the point is to find the author's confirmation bias. No padding, no praise. As long as needed and no longer.

---

## Variants

**The partisan.** Role: "the strongest possible advocate for <target> as <their text> states it." Add: "Before you judge any claim about what <target> says, fetch <URL> with the jina read_url tool and work from the text. Treat the plan's summary of <target> as the opposing side's summary of your client. Quote <target> directly wherever you claim the essay misreads them. List every claim in the ledger that attacks something <target> does not say."

**The cold reader.** No ledger, no plan. "Read `<essay path>` from the start to <the heading where working notes begin>. Ignore every HTML comment. Do not read anything under `_notes/`. The essay responds to <one sentence>. You know nothing else about the author's intentions. Report: (1) the thesis and its load-bearing claims in your own words; (2) for each, argued or assumed, what it needs, the strongest expert objection, whether the essay answers it; (3) what the essay assumes without arguing that an unsympathetic expert would refuse to grant; (4) where it attacks a position its targets do not plausibly hold, judged from its own quotations of them; (5) internal inconsistencies, two passages that cannot both be right; (6) the single most damaging objection. Quote the sentence you object to."

**Mid-run corrections.** `SendMessage` reaches a running attacker at its next tool call. Use it to redirect a partisan to the primary text or to tell an attacker that a "verified facts" section is a set of claims under test.
