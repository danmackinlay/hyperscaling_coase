> Historical: this is the 2026-10-13 cut-and-move map for the three-bin draft. The structure it describes was superseded on 2026-10-15 by the proposed order at the end of `hyperscaling_coase_rebuild.md` and on 2026-10-21 by `hyperscaling_coase_summary.md`. Kept as the record of phases one and two.

# hyperscaling_coase section skeleton

Proposed restructure for the minimum viable essay (2026-10-13). Frame: three bins, floor / complexity / contest, defined in `hyperscaling_coase.md` under Vocabulary. The essay is organised by parameter rather than by bin: the clause section carries complexity and contest both, the division section carries contest, the river carries the floor, and the frame is stated once, in the decomposition section.

**Source and workflow.** The working file is a stub (commit `replan`). The full text is `notebook/_hyperscaling_coase.backup.qmd`, committed in `replan`, hidden from Quarto and the qmd walkers by its `_` prefix, and byte-identical to `git show 9fd53c5a5c:notebook/hyperscaling_coase.qmd`. Paragraph numbers ¶ index the backup's body as blank-line-separated blocks, 146 of them, headings and displays included, with the backup's line range. **Phase one** copies paragraphs from the backup into the stub in the order below, verbatim, no rewording; it is deterministic and could be a script. **Phase two** ran 2026-10-13: four Opus agents, one per section group, resolved all nine NEW passages and every `<!-- edit: -->` mark; each new passage is marked `<!-- new: NEW-n -->`. Essay body 14,264 words after it. Residue in the plan, open question 12; the `<!-- phase two: trim -->` notes remain for the de-slop pass.

**Honest arithmetic.** Phase one ran 2026-10-13 (`_tmp/hyperscaling_mve/assemble.py`, re-runnable against the committed stub): 13,566 words of essay body, comments and Incoming excluded, from 17,800. The phase-two trims listed inline take it near 11,500. Reaching 8,500 means dropping whole arguments; candidates at the end.

## (Intro, untitled)

Already in the stub, in Dan's edited form: ¶1 image, ¶2–5.
- ¶8 (L68–73) "Here I want to examine the claim in terms of computational scaling." Keep.
- ¶10–12 (L82–93) two HTML comments. Carry over; Dan prunes.
- NEW-1 replaces ¶9 (L75–80) "All else being equal".

Cut: ¶6–7, the "Whose theorem?" callout; ¶9.

## Someone pollutes our hypothetical river — ~2100 after phase one

Model, then floor. Absorbs "Who gets paid in Utopia?" and the private-harms floor from "Cheap is not free".
- ¶15 (L99–103) "You and I, as regular schlubs" — opening.
- ¶16 (L105–109) "We operationalize these notions"
- ¶17 (L111) "Let us see how that looks in practice"
- ¶18 heading, title kept.
- ¶19–31 (L115–163) the model, in order.
- ¶32 (L165–173) "First, consider $k=n$."
- ¶33 (L175–179) "Suppose the catchment has three residents"
- ¶34 (L181–187) "At $k=1$", then NEW-2.
- ¶35 (L189–196) "At $k=0$", then NEW-3.
- ¶36 (L198–200) "Now bump $\pi$ to $20$"
- ¶37 (L202–204) "Now make the harms private."
- ¶62a, the two sentences L369–370 from "First the strategic floor" to "does not appear in them anywhere". Edit: drop "the $L$ of the decomposition", not yet defined here.
- ¶38 (L206–211) "That is one failure per regime"
- ¶39 (L213–216) "One question we passed over: who chose $k$?"

Cut: ¶13 heading; ¶14 "The attraction of tireless personal negotiators".

## What makes up transaction costs — ~1500

- ¶40 heading.
- ¶41 (L220–222) "The Coasean optimist argument goes as follows"
- ¶42 (L224–229) Resource costs. Edit: the forward reference names "Cheap is not free".
- ¶43 (L231–242) Strategic costs. Edit: section-name reference. Footnote: the direction-of-misreport sentence rescued from ¶137 (L859–864), "At $k=0$ I understate… at $k=n$ I overstate".
- ¶44 (L244–253) Computational costs. Edit: drop the Sandholm coalition-search count; the division count becomes "settling a division fairly by computation is hard in the technical sense".
- ¶45–47 (L255–270) the decomposition and its reading. Edit ¶47: "The next two sections size $D_a$".
- ¶48 (L272–276) "The activities are Dahlman's". Phase two: cut candidate, scholarly positioning.
- ¶49 (L278–288) "Unit prices will fall" — seeds Coase's menu.
- NEW-4 after ¶49.

## How big is a contract? — ~1950 *(placeholder title; was "How big is the bargaining problem?" plus the clause half of "Cheap is not free")*

The $m$-story, complexity and contest both.
- ¶50 heading, retitle.
- ¶51 (L292–305) "Suppose every agent is truthful". Phase two: trim; 401 words.
- ¶52 (L307–311) *The preference object.*
- ¶54 (L323–329) *The division.* Edit the opening "Given the blocs, the spoils", which referred to ¶53. The one party-count item here: exact pivotality is #P, stated as the precondition the division section needs.
- ¶55 (L331–334) *The bits.*
- ¶56 (L336–343) "Now we consider how rapidly the cost grows" — Dan's draft. Edit: keep the $m$ sentences; drop the two $e^n$ sentences and the $C=\frac{b}{a}e^m e^n$ formula.
- ¶58 (L347–348) "The question we set at the top was how cheap"
- ¶60 (L356–360) "The $m$-race reads differently" — the standard form calls the race off; the contest half of the clause story.
- ¶61 (L362–366) "It is worth asking what the proposed technology does" — the fluent negotiator as $m$-enlarger.
- ¶62b, L368 then L371–382, with the `<!-- Dan: placeholder -->` comment: the elicitation bottleneck. Edit: "two components" becomes one, drop "Second,".
- ¶63 (L384–389) "So the answer to 'how cheap' splits three ways", with NEW-5 replacing the $n/\ln n$ sentence; drop the last sentence ("worst-case bookkeeping… deferred").

Cut: ¶53 *The search*, Bell numbers and Sandholm; ¶57 heading; ¶59 the race against $2^n$ and $B_n$.

## Can prices save us? — ~1550, ~1250 after trims

- ¶74 heading.
- ¶75 (L444–449) "The obvious rejoinder"
- ¶76–78 (L451–467) convexity, gross substitutes, the valuation display, the substitutes/complements arithmetic.
- ¶79 (L469–479) "To say a price mechanism functions smoothly" — the no-uniform-price arithmetic.
- ¶80 (L481–496) "It is worth being explicit about what we quietly assume a price to be". Phase two: trim the additive-representation arithmetic, which repeats ¶79.
- ¶81 (L498–504) "Perhaps that is too strong a test" — tâtonnement. Phase two: to a footnote on ¶82.
- ¶82 (L506–508) "Which leaves Krier's actual mechanism."

Move out: ¶83 to the division section.

## The contest over the division — ~1000 *(placeholder title; was "The computational core")*

- ¶64 heading, retitle.
- ¶65 (L393–397) "Return to the bargaining club"
- ¶66 (L399–403) "The toy shows how pivotality detaches from harm." Edit: "of two sections ago".
- ¶67 (L405–410) "What the members will hold instead are estimates". Phase two: Larson–Sandholm to a footnote.
- ¶69–70 (L415–421) the core display and "one constraint per coalition": certifying a division costs $2^n$ in general.
- ¶73 (L432–440) "We should be careful about what this does and does not say." Edit: it makes the inference point twice; keep one.
- ¶83 (L510–515) "And here too the technology has a direction of its own." — the drift from price to quote.

Cut: ¶68 "This asymmetry deserves a stability concept of its own"; ¶71–72 the $\mathrm{Core}(b)$ display and definition.

## The rulebook — ~1700, ~1500 after trims *(now 2199)*

- ¶84 heading, retitle.
- DECIDE ¶85–89 (L519–544): the capacity function, the Demand display with $B_n$, the message-count paragraph. Recommendation: cut ¶85–88; keep ¶89 with the $B_n$/$2^n$ and ten-thousand-doublings sentences removed, for its message-frugality point and "which rules delete which terms, in that order".
- ¶90 (L546–552) *First, bound the bargain.* NEW-6 replaces its $B_n$ arithmetic; the treewidth sentences can stay.
- ¶91 (L554–568) *Second, cap the language.* Extraction and dissipation are defined here; the division section precedes this and does not use the words.
- ¶92 (L570–588) *Third, pin the division.* Phase two: trim; 578 words.
- ¶95 (L596–606) "linear in $n$". Edit: drop the first three sentences through "$h(\log R)$"; start at "Set the caps low enough".
- ¶96 (L608–614) "So: does cheaper compute, by itself, get us anywhere?" Edit: drop the three curve sentences; keep the first sentence, "What lets compute compound…", and the last sentence with its footnote.

Cut: ¶93–94 the capped Demand display.

## Institutions as contest-enders — ~1000 *(placeholder title; was "cached computation" + "compute armour")*

- ¶103 heading, retitle.
- NEW-7 replaces ¶104 (L653–658) "The $B_n$ term is charged for settling who bargains with whom". Keep ¶104's Coase 1937 citation and its "two cost curves" sentence if they fit.
- ¶105 (L660–666) "Which inverts the prediction". Edit: "The outside curve has $B_n$ and $2^n$ in it, charged on the number of parties whose agreement is needed" becomes "the outside curve is a contest, charged on the number of parties whose agreement is needed and on what each can spend".
- ¶106 (L668–671) Krier's ossification, with NEW-8 replacing the sentence "Converging on a partition *is* the coalition-structure search…".
- ¶107 (L673–677) "Two boundaries on the inversion." Edit: "cache" wording.
- ¶109 (L681–688) "The cache spends computation once" — compute armour. Edit the opening clause.
- ¶110 (L690–693) "Which is what the boring institutions were all along."

Cut: ¶108 heading; ¶97–102, the Shalizi section entire with its vale wrappers. ¶100's planner's-epsilon point already survives in ¶129.

## What survives — ~1950, ~1600 after trims

- ¶111 heading.
- ¶112 (L697) "Everything above deserves its discount"
- ¶113–114 (L699–709) worst case. Phase two: trim; with $B_n$ gone what is left is the clause bound and the contest point about who picks the instance.
- ¶115 (L711–714) the substitutes concession.
- ¶116 (L716–723) hierarchy, with NEW-9 replacing "It is the freeze, not the tree, that deletes the $B_n$ term, because the Bell numbers count exactly the re-litigations foregone".
- ¶117–121 (L725–762) equity: Krier's three claims and the democratic-mode concession, with their HTML comments.
- ¶122 (L764–777) decision problem against contest. Phase two: trim once NEW-4 states the frame.

## Point the agents at the rulebook — ~1100

- ¶123 (L779–781) "Where does that leave the disagreement?"
- ¶124 (L783–788) "Which suggests where to look"
- ¶125 (L790–792) the trap.
- ¶126 (L794–796) failing upward.
- ¶127 (L798–799) the one line.
- ¶128 (L801–808) design is NP-hard. Phase two: cake-cutting to a footnote.
- ¶129 (L810–815) three reasons. Edit: "the Shalizi asymmetry" gets a footnote citing `@Shalizi2012Soviet` with a one-sentence gloss, since the section is gone.
- ¶130 (L817–824) the political Coase theorem; the close.

## Held outside the essay

- ¶140–144 (L872–895) Incoming: carry over verbatim after the close, before References, until Dan decides where it lives.
- ¶145–146 References: in the stub.

## Cut entirely

¶6–7; ¶9 (replaced); ¶13–14; ¶53; ¶57; ¶59; ¶68; ¶71–72; ¶85–88 (recommended); ¶93–94; ¶97–102; ¶104 (replaced); ¶108; ¶131–139, the appendix, except the ¶137 sentence footnoted in the decomposition section.

## New prose (phase two, each marked `<!-- new -->`)

| id | where | spec | words |
|---|---|---|---|
| NEW-1 | intro, replacing ¶9 | the three-way answer: a count compute does not touch, a contest compute makes worse, a floor nothing touches | ~80 |
| NEW-2 | river, after ¶34 | $k=1$ is an empty core: the factory with any one resident out-threatens the grand coalition; "refuse together, not apart" as a theorem; cite `@Aivazian1981Coase`. Source: plan, The model | ~80 |
| NEW-3 | river, after ¶35 | $k=0$: the core is fine and the contribution game misses it; Olson | ~40 |
| NEW-4 | decomposition, after ¶49 | the three bins named; in a decision problem compute has a knee, in a contest a prize | ~120 |
| NEW-5 | clause section, inside ¶63 | the $n$ sentence of the three-way answer: what grows in $n$ is a contest | ~40 |
| NEW-6 | rulebook, inside ¶90 | why bound the bargain without $B_n$: exact play becomes affordable inside it, and the other two rules get a membership list | ~80 |
| NEW-7 | institutions, replacing ¶104 | the firm fixes membership and pins the division by wage; Coase's margin is a local rule; the org chart is a settled contest, not a cached search | ~120 |
| NEW-8 | institutions, inside ¶106 | agents that stop renegotiating have settled a division wherever the contest stood when the budget ran out, which favours the bigger budget | ~60 |
| NEW-9 | what survives, inside ¶116 | the frozen membership ends the contest: nobody re-litigates who belongs to which reach, and there is no prize in doing so | ~40 |

Inline edits, listed above: section-name references (¶42, ¶43, ¶47, ¶66); openings that referred to cut paragraphs (¶54, ¶62b, ¶109); $B_n$ clauses (¶44, ¶56, ¶95, ¶96, ¶105, ¶107); the ¶73 duplicate; the ¶129 footnote; the ¶137 footnote.

Rules for the new prose: dispatch to a modern Opus agent (`model: "opus"`), not Fable, Dan's standing preference for drafting; existing citation keys only; a claim wanting a key not in the sidecar gets a `<!-- cite: -->` comment; never emit a `<!-- sem -->` marker; sentence per line; Oxford -ize; no colon headings.

## Decide

(Decisions in `*`

- ¶85–89, above, specifically “(L519–544): the capacity function, the Demand display with $B_n$, the message-count paragraph. Recommendation: cut ¶85–88; keep ¶89 with the $B_n$/$2^n$ and ten-thousand-doublings sentences removed, for its message-frugality point and "which rules delete which terms, in that order".”

  *  Recommendation approved.

- Prices: its own section, as mapped, or folded into the clause section, which would make that section about 3,500 words.

  * Let's draft the prices section as its own thing and see if it works

- Incoming: stays in the file, moves to the plan, or is dropped.

  * keep in the file for now.

- Whether phase one runs in the stub on master, with Dan not editing meanwhile, or in a worktree.

  * in the stub on master. I'll go make dinner

- Whether process rule 1 (sign-off before body paragraphs) is waived for phase one, which writes no new prose.

  * Yes, suspend this rule for the duration of the current edit

## Candidates if 8,500 is the target

Each is a whole argument, not a trim: ¶48 (lineage); ¶81 (tâtonnement, even as a footnote); ¶113–114 (the worst-case objection and its answer); ¶124–126 (the small cases, the trap, failing upward, which could compress to one paragraph); ¶128 (design is NP-hard, keeping one sentence); ¶129 (the three reasons, keeping the approximation point).
