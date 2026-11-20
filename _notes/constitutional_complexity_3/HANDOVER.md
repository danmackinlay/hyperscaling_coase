# Handover: response to Krier, "Coasean Bargaining at Scale"

Written 2026-11-20 by the session that produced the article, for an agent continuing the work in this repository.
You have none of that session's history, memory or repository instructions.
Where this note and the article disagree, the article is right.
Dan is in the research phase and has decided nothing about structure yet.
Do not start drafting until he says so.

## Files

Everything was moved (not copied) on 2026-11-20 from `~/Source/livingthing` into this folder, `_notes/constitutional_complexity_3/`.
The folder convention is in the repository README.
None of it was ever committed in livingthing, so there is no history to consult there.

| File here | What it is | Path in livingthing before the move |
|---|---|---|
| `draft.md` | The article, about 10,000 words, 750 lines. Never rendered through Quarto. | `_plans/hyperscaling_coase_constitutional_complexity_3.qmd` |
| `HANDOVER.md` | This note. | `_plans/hyperscaling_coase_constitutional_complexity_3_handover.md` |
| `brief_v1.md` | The technical brief the drafter worked from: thesis, definitions, every result and derivation with its status. | `_tmp/coase3/brief.md` |
| `refs_verified.md` | The reference list checked against Crossref and arXiv, with DOIs and a discrepancies section. Slow to regenerate. | `_tmp/coase3/refs_verified.md` |
| `refs_from_memory.md` | The same list as first written from memory. Superseded by `refs_verified.md`. | `_tmp/coase3/refs_todo.md` |
| `cold_read_1.md` | First cold-read report. Its line numbers refer to the draft before revision. | `_tmp/coase3/cold_read_1.md` |
| `revision_rulings.md` | The 24 rulings sent to the drafter after the first cold read. | `_tmp/coase3/revision_decisions.md` |

`brief_v1.md`, `cold_read_1.md` and `revision_rulings.md` are records and still name the old paths.
The second cold-read report was not saved to a file; its findings are summarised below.

## The other line of work in this repository

`_notes/constitutional_complexity_2/` is another agent's folder, holding a different response to the same essay.
Dan told this session not to read his other drafts on the topic, so that the argument here would be independent.
This session has seen only the title and file table of that folder's handover, and nothing of its argument.
Dan also has further drafts matching `_plans/hyperscaling_coase*` in livingthing that this session never opened.
Ask Dan before reading any of them; the independence may still matter to him.

## The source being answered

Séb Krier, "Coasean Bargaining at Scale", Cosmos Institute, 2025: <https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale>.
Krier argues that AI agents acting for individuals make bargaining cheap enough for private deals to replace most regulation of externalities, leaving the state as a lean "framework guarantor".
His running examples: a delivery truck priced onto a street; a developer needing every homeowner's agreement; a voluntary "bargaining club" with a common clearing price; 10,000 residents forming a coalition against a factory.

## What the article argues

Cheap bargaining removes only the costs that scale with the price of bargaining.
Krier's examples fail for reasons that do not, so the framework guarantor is where the whole difficulty has gone.

1. Grant perfectly loyal agents and prices of computation $c$ and communication $\kappa$ that are positive but arbitrarily small.
   Search, drafting and messaging costs vanish.
   Three losses remain: private information ($L_{\text{info}}$), the communication and calculation the allocation problem itself requires ($L_{\text{comp}}$), and spending on bargaining advantage ($L_{\text{contest}}$).
2. Private information decides Krier's cases.
   When one decision needs the consent of $N$ parties with private values, the probability that voluntary, budget-balanced bargaining approves a worthwhile project goes to zero as $N$ grows (Mailath and Postlewaite 1990).
   Exchange of private goods among many traders is different: loss of order $1/N^2$ (Rustichini, Satterthwaite and Williams 1994).
3. Every known remedy is an act of authority: overriding a dissenter, taxing to fund a subsidy, assigning rights using the distribution $F$ of preferences.
   Choosing a remedy is the same kind of decision one level up, so agents cannot bargain their way to it.
   Hence a "benevolent leviathan": able to coerce, maximising welfare, and knowing $F$ unless it pays an open-ended subsidy.

The article is a condition ("efficiency needs this"), not a case for planning, and it says nothing in Krier's scheme supplies such an actor.

Derivations that are the article's own, each introduced in the text by "The derivation is mine.":

- Prices posted separately by $N$ rights-holders let through a fraction $1/(N+1)$ of efficient trades when values are uniform.
- A coalition lifts that to $1/2$, but an outsider earns $(1-H)^2/9$ against a member's $(1-H)^2/(4N)$, so staying out pays for $N \ge 3$.
- The bargaining club must give up truthfulness, efficiency or voluntariness.
- Efficient allocation of $m$ items needs about $2^m/\sqrt{m}$ bits in the worst case (Nisan and Segal 2006); a thousandfold fall in $\kappa$ buys about ten more items.
- In a Tullock contest with $r \le N/(N-1)$, total spend is $r(N-1)V/N$ for every $c$.
- The flat rule "approve if $V \ge N\mu$, pay each resident the mean $\mu$" has expected loss at most $\sqrt{N\,\mathrm{Var}(\theta_i)}$, so relative loss of order $N^{-1/2}$.

## How it was produced

Dan's instructions for the article, which still stand unless he changes them:

- Use symbols when making claims, and say what a quantity is hard in or convex in.
- Have an Opus 5.5 agent write the prose, briefed for clear human presentation, to avoid the house style of the working model.
- Have a second, contextless Opus 5.5 agent do a cold read for undefined terms and references, and fix what it finds before showing Dan.

What happened: literature search and derivations by the working session, a brief, an Opus 5.5 draft, a Sonnet agent verifying references against Crossref, a cold read, 24 rulings, a revision, a second cold read, a final pass.
Both cold readers reproduced every displayed derivation.
The second found one real overclaim, now fixed: a tax-funded subsidy needs no knowledge of $F$, so "every remedy needs $F$" was false.

## What is not verified

- Theorem statements checked against abstracts or source text: Mailath–Postlewaite, Ellingsen–Miettinen, Ellingsen–Paltseva, Dixit–Olson, Segal, Nisan–Segal, Hurwicz.
  The rest are stated from memory of the literature.
  Check first: the Al-Najjar–Smorodinsky $N^{-1/2}$ scaling, the form of Dixit and Olson's coercive remedy, and the mapping of the developer example onto Mailath–Postlewaite, which the text marks as the author's.
- Four references have no DOI: Arrow 1969, Hayek 1945, Hirshleifer 1971, Hurwicz 1960.
- Prior critics cited (Petel, Sharp et al., Ngo, Shahidi et al.) were found independently.
  Dan's notes mention a response by Snow, which was not found.
- References are author–year with DOI links, not Zotero keys.
- The contest model's invariance to $c$ is a modelling choice and is flagged as one.

## Discussion with Dan after the article

None of this is in the article yet.
Citations in this section are from memory and were not looked up.

**Where the leviathan's unselfishness is needed.**
Running a fixed rule needs only a disinterested party that can commit (Holmström 1982, the budget breaker).
Choosing the rule needs unselfishness, because the same powers aimed at revenue give Myerson's (1981) optimal auction or Brennan and Buchanan's (1980) revenue-maximising state.

**When a leviathan should use exchange and not direct assignment.**
By the revelation principle, direct assignment from reports can reproduce any equilibrium of any exchange rule.
So exchange wins only through communication cost, computation cost, or not knowing $F$.

| World | Use | Why |
|---|---|---|
| Leviathan knows every $\theta_i$ | Assignment | Nothing to elicit. |
| Private goods, many traders, substitutes | Exchange | Double auction loses $O(1/N^2)$ without using $F$; prices are the smallest message supporting an efficient allocation (Hurwicz; Mount and Reiter 1974; Jordan 1982). |
| One decision needing $N$ consents | Coerced flat rule | Voluntary approval probability goes to 0; flat rule loses $O(N^{-1/2})$. |
| Few parties, complements | Rights assigned so that exchange then works | Cramton, Gibbons and Klemperer 1987; Segal and Whinston 2011. |
| $F$ unknown or wrong | Exchange, where the thick-market result applies | Its guarantee does not depend on $F$. |

Weitzman (1974): prices beat quantities when marginal cost is steeper than marginal benefit, $C'' > |B''|$.

**Mechanisms that provably beat the leviathan's own attempt $a_0$ without it computing their outcome.**
Three kinds: a fallback rule (anyone may propose an alternative to $a_0$, adopted by consent; Nisan and Ronen 2007's second-chance mechanism); invariants (each voluntary trade without third-party effects is a Pareto improvement); verified delegation (Azar and Micali 2012, rational proofs).
Also Conitzer and Sandholm (2004), computational criticisms of the revelation principle.

Limits established in discussion:

- These repair a shortage of computation in the leviathan, not private information.
  If $a_0$ is already the best incentive-compatible rule given $F$, nothing is unanimously preferred (Holmström and Myerson 1983).
- Pooled computation buys little: $N$ agents in parallel extend exhaustive search over $2^k$ constitutions by $\log_2 N$ clauses, about 13 for $N = 10{,}000$.
  Checking costs $N$ evaluations per proposal, and assumes each agent can cheaply evaluate a proposal for its principal.
- The proposers' real advantage is knowing their own values, which gives local search: good under substitutes, liable to stall under complements.
- $a_0$ must not depend on the current parties' reports, or they misstate to improve their guaranteed minimum before the improvement stage.
  The flat rule qualifies.
- In Krier's many-consent cases, improving on $a_0$ is itself an $N$-party bargain, so it almost never happens as $N$ grows.
- Rational proofs hold only against an agent maximising the stated payment.
  Dan's three objections are each correct: a spiteful agent, an agent with outside stakes larger than the payment, and a proposer of a constitution that later reaches a state it prefers (a long-run property of a program, undecidable in general).
  Relevant: Eliaz 2002; Abraham, Dolev, Gonen and Halpern 2006.

One consequence for the thesis: computation is the one requirement the leviathan can hand to the selfish agents, by checking and not searching.
Coercion and unselfishness cannot be handed over.

## Open decisions, all Dan's

1. **Title.** Dan has said the title must change. Both cold readers flagged "still need" as ungrammatical, and the argument rests on information more than computation.
   Headings may not contain colons, so candidates are single clauses. None chosen.
   For a plain-language main piece: "What the framework guarantor has to do" (the session's pick); "Which bargains can agents strike without a sovereign?"; "Where agent bargaining works and where it needs a state"; "What Coasean agents cannot bargain over".
   For the technical piece: "Private information, not transaction cost, limits Coasean bargaining among AI agents" (the session's pick); "Informational and computational costs imply that constitutional negotiation among selfish delegated agents still needs a benevolent leviathan" (the original with its grammar fixed and information first); "Agent bargaining over shared decisions needs a benevolent rule-setter".
   The draft still carries the original title verbatim, as Dan first specified it.
2. **Structure.** Options discussed:
   (a) put the constructive material into this article and trim the informational detail;
   (b) write a short plain-language main piece and make this article its technical companion.
   The session recommended (b): the article is organised by kind of loss with separately citable subsections, which suits a reference, and the informational detail holds its strongest original results.
   The main piece would be organised by kind of decision, following the table above, with the developer example carried through.
   Dan answered "Not yet".
3. **Sequel.** A weak trusted checker over strong untrusted agents, with the three objections above as its substance. Not started.
4. **Whether an existing draft is already the main piece.** Unknown; see "The other line of work in this repository".

## Conventions the article follows

These come from livingthing, where the draft was written. Its formatter and linter are not in this repository.

- One sentence per line in prose (livingthing: `uv run format-sentences <file>`).
- Oxford spelling, -ize (livingthing's Vale rules; the remaining warnings were inside Krier quotations and one cited title).
- No colons in headings; "I" for the author; no indefinite "you".
- `references.bib` is generated from Zotero and never edited by hand. The draft's citations are author–year with DOI links, not `[@Key]`, and need ingesting before it becomes a top-level `.qmd`.
- The draft keeps its Quarto frontmatter (`title`, `date`, `abstract`); it lacks the `categories` and `author` keys this site's posts carry.
- Dan's shell is fish; commands handed to him must be valid fish.
