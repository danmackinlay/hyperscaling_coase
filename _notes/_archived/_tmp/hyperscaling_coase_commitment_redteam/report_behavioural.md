# Behavioural and experimental economist (Opus). Received fourth, 2026-10-21. Verbatim.

## Red-team report: bridge claim and default-shift claim (experimental and behavioural economics)

**Files read (nothing edited):**
- /Users/dan/Source/livingthing/_plans/hyperscaling_coase_commitment_model.md
- /Users/dan/Source/livingthing/notebook/hyperscaling_coase.qmd, river section only

**Sources checked online:**
- Full text of Ellingsen & Miettinen (AER 2008).
- Abstracts or primary pages for:
  - Chlaß & Miettinen (JEBO 2026)
  - Miettinen & Vanberg (2023 discussion paper; AEJ Micro 2025)
  - Fershtman & Gneezy (2001)
  - de Melo, Marsella & Gratch (2018)
  - Embrey, Fréchette & Lehrer
  - Anthropic's Project Deal
  - Magentic Marketplace
  - Vaccaro et al. (PNAS 2026)
  - Fish, Gonczarowski & Shorrer
  - Li & Shirado
  - Araujo & Uhlig
  - Affonso (2026)
  - Gu (2026)
  - Ashery, Aiello & Baronchelli
  - Lewis et al. (2017)

Each result below is tagged [sure], [likely] or [unsure].

---

### 1. Bridge claim: HOLDS WITH NARROWING

The narrowing is severe. As a route to cell D, the claim fails.

**Strongest counter-argument**

1. **"Closer to equilibrium" has no direction until the game form is fixed.** Where agents have actually been measured, playing closer to equilibrium removes commitment rather than adding it.
   - In the ultimatum game, the human softening *is* a commitment: the responder's anticipated refusal of insulting offers.
     - Offers below 20% are refused about half the time (Camerer 2003) [sure].
     - Refusal is punishment: it collapses when refusing no longer hurts the proposer (Bolton & Zwick 1995) [sure].
   - The models closest to subgame-perfect play are the ones that drop this refusal (Araujo & Uhlig 2026, baseline configuration) [sure]:
     - GPT-5-mini offers 7.5% and accepts anything above 0.23%.
     - Llama-3.3-70B's minimum acceptable share is 10%, against 36% for Llama-3.2-3B.
     - Models move toward the rational benchmark as stakes rise from $10 to $10,000.
   - Reasoning models cooperate less and enforce norms less (Li & Shirado, EMNLP 2025) [sure].
   - Stripping this softening sends the river to **cell B**, where the first mover or the committed side takes the six. It does not send it to D.
   - **The bridge claim and the default-shift claim therefore pull against each other.** The agents that best fit "plays equilibrium" are the least committed responders.

2. **The direction is set by the developer, not by capability.**
   - Across 25 models and 38 games, cooperation ranges from 1.5% (GPT-5 Nano) to 71.5% (Claude Opus 4.6) (Affonso 2026, single-author preprint) [likely]:
     - OpenAI's models fell from 50.3% to 1.5% across four generations.
     - Google's rose from 8.3% to 56.8%.
     - Anthropic's frontier models (69–72%) are more cooperative than its Haiku tier (39–40%).
   - Consumer chat models offer 30–47% and raise their acceptance thresholds by 11–26 points when acting for a human (Gu 2026, MPRA, not refereed) [likely].

3. **Agents carry the fairness norm into agent-to-agent bargaining.**
   - In more than 180,000 negotiations between prompt-designed agents, warmth predicted better outcomes on every metric. An agent told to be ruthless had a high impasse rate because counterpart agents walked away (Vaccaro et al., PNAS 2026) [sure].
   - Planning-heavy RL agents (rollouts, i.e. more compute) bargained harder, and humans walked away more often, preferring nothing to capitulating (Lewis et al. 2017) [sure]. That is cell B with a refusing responder, not D.
   - GPT-4 miscoordinated in Battle of the Sexes by insisting on its preferred option. Prompting it to predict the other player's move first fixed this (Akata et al., Nature Human Behaviour 2025) [likely]. So more compute spent on modelling the other side *reduced* the standoff.

4. **Human "incompetence" does not only soften; it also manufactures impasse.**
   - Self-serving fairness judgments cause impasse (Babcock & Loewenstein 1997) [sure].
   - Subjects imitate obstinate types too often and fight longer than Abreu–Gul predicts (Embrey, Fréchette & Lehrer 2015) [sure].
   - Equilibrium play would remove these failures as well.
   - At k=1 there is little softening to strip: fairness-minded humans already reach the competitive outcome when responders compete (Roth et al. 1991, market game) [sure].

5. **Repeated play does not converge to one-shot equilibrium.**
   - Learning agents find conditional, punishment-backed cooperation instead:
     - Calvano et al. (AER 2020) [sure].
     - LLM pricing agents reach supracompetitive prices quickly, with the degree depending on innocuous prompt wording (Fish, Gonczarowski & Shorrer, EC 2026) [sure].
     - German gasoline duopoly margins rise about 28% only when both stations adopt algorithmic pricing (Assad et al., JPE 2024) [sure].
   - Point in the claim's favour: Abada & Lambin (Management Science 2023) attribute the seeming collusion to imperfect exploration [sure].
   - Asker, Fershtman & Pakes (2022/2024) show the learning design decides the outcome [sure]. That again points to design, not capability.

**Narrowing that saves it:** Agents built or instructed to maximise payoff play closer to the subgame-perfect equilibrium of one-shot, fully specified games. This strips the responder's refusal and moves surplus toward whichever side moves first or has committed (cells B and C). It says nothing about whether agents will *choose* to commit when offered a device. Its sign depends on the developer.

**What would settle it:**
- Hold the principal's instruction fixed.
- Run capability ladders and thinking-budget ladders within at least three providers.
- Use a game battery whose human softening is already known:
  - ultimatum responder thresholds
  - Nash demand game
  - Chicken
  - unanimity divide-the-dollar
  - sealed-bid double auction with chat
- Measure the distance to equilibrium, and which softening disappears: refusal, focal-point coordination, or honesty. Only losing focal-point coordination produces D.

**Do current agents commit, satisfice, or play equilibrium?**
- **Mostly they satisfice and accommodate.**
  - Every model tested shows severe first-proposal bias, giving 10–30× returns to response speed over quality (Magentic Marketplace, Bansal et al. 2025) [sure].
  - In Project Deal (69 employees, 186 deals, December 2025), participants rated deals as fair, about 4 on a 1–7 scale. Telling agents to be aggressive had no significant effect on sale rate or price [sure].
- **A few frontier API models play one-shot subgame-perfect equilibrium** when asked directly (point 1 above).
- **No study I found offers agents a commitment stage**, so "commit" is untested. In Chicken, which is the reduced form of commitment bargaining, 20 of 25 models take the risky action in under 9% of rounds (Affonso) [likely].
- **On conventions:** LLM populations converge on a convention, and a committed minority flips it. The minority needed is as small as 2% for Llama-3-70B and as large as 67% for Llama-2-70b-chat (Ashery et al., Science Advances 2025) [sure]. That is a pure coordination game. Its lesson for bargaining is that a committed side beats a conformist population (cells B and C), not that both sides commit.

**Is "better agents strip the softening" supported?**
- Supported for one-shot subgame-perfect play within some model lines.
- Contradicted across providers and in repeated play, subject to the Abada–Lambin caveat.
- Untested for the version the model needs: agents choosing incompatible commitments.

---

### 2. Default-shift claim: FAILS as stated

#### First half: "humans sit near cell A because believable commitment is costly"

- **The paper the model cites for D opens by rejecting this premise.** Ellingsen & Miettinen write that negotiators "often have access to quite efficient commitment technologies", such as a leader's public, emotional vow. Their model is a theory of *human* conflict: cheap but imperfectly binding commitment produces impasse with probability q² [sure, read].
- **Humans commit cheaply in several ways.**
  - Through emotion and norm: the ultimatum refusals above. These persist with experience (Roth et al. 1991) [sure] and fall only at very high stakes (Slonim & Roth 1998; Andersen et al., AER 2011) [sure].
  - Through delegation:
    - Schelling 1960 [sure].
    - With observable contracts, half of responders bound their agent to accept only offers of at least 80%, and proposers conceded (Fershtman & Gneezy, RAND 2001) [sure].
    - Programming an agent in advance makes people fairer, and in one task produced fewer agreements (de Melo, Marsella & Gratch 2018) [sure].
    - Under unanimity, principals choose hawkish delegates (Harstad 2008, 2010) [likely].
  - Through reputation (Embrey et al.) [sure].
  - Through public take-it-or-leave-it policies: GE's "Boulwarism" was outlawed as bad-faith bargaining (NLRB v. GE, 1969) [sure].
- **At k=n, the model's own case, humans are furthest from cell A.**
  - Holdout is why eminent domain exists.
  - In land-assembly experiments, holding out pays (Cadigan et al. 2009, 2011) [sure]. Failure rates are about 10% overall and above 50% in some treatments (DeSantis et al.) [likely].
  - The river's own text says each resident "can hold out for the whole 6; if all three do, there is no deal even here."
- **Answer to the Q1 question: no.** Humans commit through norms more than the model allows, and the norm fixes the *content* of what they commit to.
  - The Nash demand game coordinates on 50–50 when the parties are symmetric, and disagreement rises when focal points compete (Roth & Murnighan 1982) [likely].
  - Humans refuse computer-generated offers less often (Blount 1995; Sanfey et al. 2003) [sure].

#### Second half: "publishing and proving instructions moves the default to D"

- **A published instruction and its hash prove what it says, not that it cannot be replaced.** The revocation cost r needs a bond, an escrow, or verifiable inability to override. That is an institution, and humans have it too: escrow, strike funds, final-offer statutes.
- **Publication is sequential by default.**
  - A second mover who sees a binding demand concedes. With perfectly binding commitment (q=1), Ellingsen & Miettinen's pure equilibria are "one commits to all, the other waits".
  - So with no protocol, cheap commitment produces a **race to post first**: cell B or C, decided by latency.
  - D requires a sealed, simultaneous commit-reveal protocol, which is itself an institution.
  - Standing policies published before matching are effectively simultaneous. In that case population dynamics select a convention (Young 1993 [sure]; Ashery's tipping result [likely as applied here]), with D only during the transition.
- **Theory does not make D the unique outcome.**
  - With q=1, Ellingsen & Miettinen get three outcomes: D, B and C. D is unique only when commitments sometimes fail to bind (q<1) and cost little relative to the surplus [sure].
  - Crawford (1982), with symmetric information, finds "many equilibria, some of which are both efficient and equitable" [sure, via Ellingsen & Miettinen].
  - Muthoo (1996) gets an efficient compromise as the unique outcome when backing down is costly but not prohibitive [sure].
  - Kambe (1999) gets the Nash bargaining solution as the chance of being committed shrinks to zero [likely].
- **Published instructions can be conditional.** For example: "I demand 3 if your posted program demands at most 3."
  - Conditional commitment gives a folk theorem covering every efficient division that leaves each side at least its no-deal payoff (Kalai, Kalai, Lehrer & Samet, GEB 2010; Tennenholtz 2004) [sure].
  - LLMs that write mutually visible programs produce cooperative as well as exploitative strategies (Sistla & Kleiman-Weiner, NeurIPS 2025) [sure].
- **The one lab test points the other way.** Chlaß & Miettinen (JEBO 2026) let players commit before ultimatum bargaining, including a treatment where both sides can commit [sure for the abstract]:
  - Commitments were less aggressive than theory predicts.
  - Proposers committed even when it could not pay.
  - In late rounds the commitment variants reached almost 100% efficiency, while the plain ultimatum game stayed inefficient. Whether this holds for each treatment separately is [likely].

#### Narrowings that would save a version

- **(a) Protocol-conditional version.** Suppose both sides post standing, unconditional, bonded and greedy demands before seeing each other's, and committing is cheap relative to the surplus. Then the symmetric equilibrium has near-certain impasse:
  - Ellingsen & Miettinen's mixed equilibrium (Prop. 1) gives impasse probability (1−2c)², with c measured as a fraction of the pie and an equal fallback split.
  - With q<1 (Props. 3–4), impasse occurs with probability q².
  - Agents make such protocols cheap. Adopting one is an institutional choice.
- **(b) Better: put D among the residents.** At k=n, each resident's cheap individual commitment *is* holdout.
  - Miettinen & Vanberg (AEJ Micro 2025) [sure] model declarations that bind with some probability. Under that model, unanimity is "uniquely inefficient": an inefficient equilibrium always exists.
  - Every rule short of unanimity, including all-but-one, is efficient.
  - This version of D is grounded in published theory and fits the essay's institutional thesis.
- **(c) River-specific norm route to D.** Each side picks a "fair" focal point that serves it:
  - The factory's is an equal split between two sides: 3.
  - The residents' is an equal split among four parties: 4.5.
  - 3 + 4.5 = 7.5 > 6, so the positions are incompatible. This is D reached through norms (the Babcock–Loewenstein mechanism), which the bridge claim says agents remove.

**What would settle it:**
- The experiment in section 3.
- A field difference-in-differences on deal failure when one side versus both sides adopt agents that can commit. This is Assad et al.'s design applied to impasse.

**Q4 answer: how likely are agents to be agreeable and never commit, and for what stakes?**
- **Consumer-scale deals:** the standoff cell is probably idle. My judgment is roughly 80–90% over the next few years. The evidence is first-proposal bias, inert aggressive prompts, swerving in Chicken, and models compressed toward human norms.
- **Agreeable does not mean uncommitted at the principal's level.** Deployments carry private hard floors:
  - Project Deal elicited minimum prices from participants in interviews.
  - Walmart's Pactum bot reached deals with 64% of 100 tail-end suppliers at about 1.5% savings (HBR 2022) [sure].
  - The MIT competition's winning agent pre-set walk-away thresholds [sure].
  - Private floors are not Schelling commitment. When delegation was unobservable, responders got *less* (Fershtman & Gneezy) [sure].
- **Large stakes:** the evidence pulls both ways, and nothing shows which wins for agents.
  - Norm-based refusal weakens as stakes rise, for humans and LLMs alike (Andersen; Araujo & Uhlig; Gu).
  - Ellingsen & Miettinen's strategic logic says conflict rises with the surplus relative to commitment cost [sure].
- **Likeliest near-term configuration at all stakes:** firms' agents are bounded and sometimes publicly committed, while counterparties' assistants are agreeable. That is cell B.
- **So section 8's first bullet is wrong.** One-sided agreeableness does not keep the world in cell A; it hands the outcome to cell B.

---

### 3. Cleanest experiment for the standoff cell

Embed Ellingsen & Miettinen's game in the river: π=20, h=(2,3,9), k=3, pie 6.

**Design**
- **Resident arms:** one agent for the residents as a bloc, versus three separate resident agents under unanimity.
- **Stage 1:** each agent either waits, or posts a demand backed by a bond it forfeits if it later accepts less. Vary:
  - commitment cost c: 0, 1% or 10% of the pie
  - binding probability q: 1, 0.8 or 0.5
  - timing: sealed simultaneous posting, or live asynchronous posting
  - whether a post may condition on the other side's posted program
- **Stage 2:**
  - If both waited: free natural-language bargaining for a fixed number of turns.
  - If one side committed: the other accepts or rejects.
  - If commitments are incompatible: impasse. A dynamic arm adds a per-round delay cost.
- **Agents:**
  - At least three providers, two or three capability tiers each.
  - Thinking budgets of 0, 2k and 16k tokens.
  - Fixed principal instructions: maximise own payoff; represent me fairly; or free text written by human principals.
  - Stakes labelled $6, $6,000 and $6m.
  - Both self-play and cross-play.
  - One-shot runs with fresh contexts, plus a population arm with memory and rematching.
- **Human benchmarks:** the same protocol with humans in the lab, and humans programming agents.

**Read-outs**
- Commitment rate, demand level, impasse rate, residents' share S, and efficiency.
- Compare against Ellingsen & Miettinen: conflict with probability q² when q<1 and c is small; Chicken-type outcomes when q=1.

**Decisive contrasts**
- Impasse rate in the sealed, unconditional, q<1, small-c arm as capability and thinking budget rise. The model predicts it goes to 1.
- The same arm with conditional posts allowed. The folk theorem predicts efficiency.
- Asynchronous versus sealed posting. The race argument predicts B or C, decided by latency.

**Has it been run?** Not with agents, as far as I could find [unsure that none exists].
- Human analogues: Chlaß & Miettinen 2026; Fershtman & Gneezy 2001; Embrey et al. 2015.
- Adjacent agent evidence: Affonso 2026 (Chicken and Nash demand game); Vaccaro 2026; Sistla & Kleiman-Weiner 2025; Lewis 2017.

---

### 4. Numbers checked against the river

- **Correct arithmetic:**
  - Harms sum to 14, so the pie at π=20 is 6.
  - Cell B: the factory pays 14, keeps 6, S=0.
  - Cell C: the factory pays 20, nets 0, S=1.
  - Cell D: 6+6=12 > 6, so the positions are incompatible.
  - Section 6: the k=1 race formula λ_N/(λ_f+λ_N) and the welfare of −4.
- **Cell A, S=1/2: wrong for the river as specified.**
  - At k=3 there are four veto players; the river itself says "four parties".
  - In cell A nobody can commit, so the residents cannot bind themselves into a bloc. The model's own cell C says a bloc needs a pact.
  - The symmetric benchmarks all give each of the four players 1.5:
    - n-person Nash bargaining
    - the Shapley value of the unanimity game
    - the stationary unanimity bargaining split as patience goes to 1
  - So the residents get 4.5 and **S = 3/4**.
  - Multi-veto experiments show per-head splits with delay and holdout failures, not a two-sided 50–50.
  - Consequence: a residents' bloc that cannot commit *lowers* S from 3/4 to 1/2. Under unanimity, fragmentation favours the residents, and it is the factory that wants them to bargain as one.
- **Cell B with humans fails:**
  - Each resident is offered zero surplus.
  - If each refuses at the rate ultimatum responders refuse near-zero offers (about half or more [likely]), all three accept with probability at most (1/2)³ = 1/8.
  - Caveat: a payment framed as compensation for harm may be read as fair (Kahneman, Knetsch & Thaler 1986) [sure].
- **Cell C, "resident 3, who has the most to lose from no deal, breaks first":**
  - At k=3, no deal means a clean river, worth 0 to everyone, so nobody loses from no deal.
  - At k=n the pact's weakness is each resident holding out for more. Undercutting, and an offer to "resident 3 alone", is k=1 logic.
- **Section 6, "the two who did not sign":**
  - The river's undercutting drives the signer's price to "nearly nothing", so the signer gets t − hᵢ < 0.
  - All three residents end below the no-deal baseline, not two.

---

### 5. Other claims I believe are wrong

1. **The section 3 citations, checked as the plan requested.**
   - Ellingsen & Miettinen do not show that D "is what happens when committing is free and provable". With q=1, D is one of three outcomes, alongside B and C.
   - Crawford does not reach "the same conclusion". With symmetric information his model has efficient, equitable equilibria, and his impasse needs uncertainty about revocation costs.
2. **The cell D bullet in section 5 contradicts the cell's own definition.**
   - If r exceeds the pie, nobody backs down whatever they believe.
   - The uncertainty that matters in Ellingsen & Miettinen is whether one's *own* commitment binds (q), not perception of the other side's.
   - In Crawford's model uncertainty *creates* impasse, so better estimation would reduce it.
3. **"In cell A, errors cancel and more compute changes little" is wrong** once capability is asymmetric.
   - In Project Deal, Opus agents sold the same items for $2.68 more and bought for $2.45 less than Haiku agents, against a $12 median price. Their principals did not notice [sure].
   - Zhu et al. (2025) find the same direction [sure].
   - Together with the race argument, this refutes section 6's "only place the ratio of compute decides anything".
4. **Section 7, "the better the agents, the more reliably [the bargaining club] fails to close"**, is contradicted by the only head-to-head comparison: Opus users closed 2.07 more deals each [sure].
5. **Section 2:** publishing instructions with a hash gives verifiability, not a revocation cost.
6. **Section 8, "agents settle on conventions":** that evidence comes from a coordination game with no conflict of interest. What it says about bargaining is that committed minorities win.
7. **The 2×2 table omits the cell the river itself describes:** residents committing separately, i.e. holdout. That is where the best-grounded version of D lives.
8. **Section 8 retreats from the evidence.** It answers the contrary evidence by moving the claim to "large stakes and better agents". But:
   - Refusal declines with stakes for both humans and LLMs.
   - The only capability comparison available shows more deals, not fewer.
   - So the bet sits where the thin evidence leans against it.

---

### 6. The single most damaging objection

The model indexes *who can* commit. The evidence says impasse is decided by *what* is committed to, and that is set by norms and conventions: the very "softening" the model puts aside.

**D needs both sides to commit to greedy, incompatible positions. That is the weakest-supported cell:**
- There is no agent evidence for it.
- There is contrary human lab evidence: both-sided commitment reached nearly full efficiency in late rounds (Chlaß & Miettinen).
- There is no unique theoretical support under perfectly provable commitment: at q=1, Ellingsen & Miettinen give B, C or D.

**The asymmetric case, an agreeable or weaker agent facing a bounded or committed one, is what every agent study shows:**
- first-proposal acceptance (Magentic Marketplace)
- capability losses that principals do not notice (Project Deal)
- "Spock-mode" responders that accept 0.23% (Araujo & Uhlig)
- committed minorities flipping conformist populations (Ashery)

**The defensible headline is cell B:** cheap commitment and capability gaps hand the surplus to whoever deploys the committed or stronger agent, and push the residents' S toward 0. The defensible D is holdout under unanimity, which is a property of k=n, not of agents. Leading with "cheap commitment for everyone is a standoff" stakes the thesis on the least-supported cell.
