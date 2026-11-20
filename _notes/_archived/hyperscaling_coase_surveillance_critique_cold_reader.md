# Cold-reader critique: "Delegated agent constitutional negotiation implies a commitment to total surveillance"

Reader: control reader who saw only `_plans/hyperscaling_coase_surveillance.qmd`. Line numbers refer to that file as read on 2026-11-19.

## 1. Thesis and load-bearing claims

Thesis. A regime in which personal agents (a) bind their principals, (b) trade externality entitlements under automatically verified contracts, and (c) also negotiate the rules themselves, logically requires, and then entrenches, an apparatus that senses, attributes, retains and links people's conduct and circumstances. Because the rules are themselves negotiable, nothing outside the negotiation limits which domains that apparatus covers. Cryptography only controls who reads the records, not what gets collected, and differential privacy, if used, removes the personalised pricing the proposal is built for.

Load-bearing claims:

- **C1 (measurability).** You can enforce only contracts measurable with respect to what the enforcer observes (Remark 1). So sensing has to be at least as wide as contracting.
- **C2 (six requirements).** Six features of the proposal each require one kind of observability: sensing of conduct, attestation of circumstances, preference reports, persistent unique identity, inspectable agents, and retention with linkage on demand. Together they meet all four conditions of the surveillance definition (line 315).
- **C3 (constitutional closure).** Under constitutional scope, no domain is exempt by a rule the negotiators cannot change, and the negotiation tends to open domains rather than close them (unravelling, wealth effects, data externalities, the veto-reimbursement rule).
- **C4 (irreversibility).** Once built, the monitoring is hard to withdraw: it creates income streams, hardened rules depend on it, and the sovereign cannot commit.
- **C5 (crypto fails).** ZK proofs do not reduce sensing. Prices leak types. DP bounds how far one person can move a price (Remark 2), and composition makes continuous repricing expensive.
- **C6 (trilemma).** Of granular coverage, automatic enforcement and privacy, any two can be had but not all three.

## 2. Claim by claim

### C1. Measurability, and "sensing must be as wide as contracting"

- **Argued or assumed.** Remark 1 is argued, and it is correct as stated: it is true by definition. The step from Remark 1 to the surveillance definition is assumed.
- **What it needs.** The enforcer's signal $\sigma$ has to be produced by continuous recording of nearly every person. Remark 1 says nothing about how $\sigma$ is produced. The prose then claims: "The record must be produced whether or not the vehicle's operator wants it produced, since otherwise the operator's agent would decline to produce it when a fee is due" (l.140), and "The sensing must be as wide as the contracting" (l.143).
- **Strongest expert objection.** Enforcement can be probabilistic. Several standard tools enforce a contract without recording every instance of the conduct:
  - Becker-style random audits with large penalties;
  - costly state verification (Townsend), where the state is checked only on some outcomes;
  - self-reporting under a perjury or penalty rule;
  - claimant-initiated evidence, where the household's own sensor is used only when it sues.

  Each makes the transfer measurable with respect to a signal that includes the audit outcome. None needs "Conduct and circumstances in $D$ … recorded as they occur … for nearly every person" (l.91–94).

  A second objection: in the incomplete-contracts literature the article cites, a state observable by the parties can be implemented through message games even when a court cannot verify it (Moore–Repullo, Maskin–Moore). Under those mechanisms the court does not need the record. The parties still observe each other, so this does not escape the article's sensing condition, but it does weaken the retention and linkage steps.
- **Answered?** No. The trust option appears only for small groups (l.546). Spot checks, audits and liability rules are never discussed, although they are the standard way to enforce at scale without full monitoring.

Holmström's informativeness principle (l.153–156) is stated correctly for a costless signal. The conclusion, "the demand for monitoring that emerges from voluntary contracting has no interior stopping point", ignores the obvious objection: if principals dislike being observed, observation enters their utility, and the optimum is interior again. The article's reply is C3's claim that privacy is underpriced, which answers the objection in part.

### C2. The six requirements

- **Circumstances (l.164–188).** Mostly holds. The incentive argument is sound: when the transfer flows to whoever reports the harm, the report needs attestation, or a Harberger levy ends up charging the vulnerable. The unravelling argument is standard and correctly applied. One strong line: "That is true of the choice set and false of the equilibrium."
- **Preferences (l.192–228).**
  - The impossibility results are cited correctly, and so is the point that ideal agents misreport optimally.
  - Two steps fail.
  - First: "The efficiency gain that the proposal promises over the present is available to the degree that the first branch is taken" (l.225). Myerson–Satterthwaite applies just as much today. The proposal's claimed gain comes from cutting search, negotiation and settlement costs, not from overcoming private information. Gains over the present are therefore available without verifiable preferences.
  - Second, the revelation-principle step is misused. "By the revelation principle, any mechanism of this kind is equivalent to one in which each agent reports its principal's type to a mediator" (l.218). That is an equivalence of outcomes, not of information flows, and it does not show that type reports exist anywhere.
  - The article itself concedes that this link is optional (l.227).
- **Persons (l.232–248).**
  - Unique identity for equal votes and Sybil resistance: argued, and it holds.
  - Cross-context linkability: not derived. "Reputation requires linkage across interactions by construction" (l.246) is true within one reputation context. Anonymous credentials with scope-exclusive pseudonyms (Camenisch–Lysyanskaya and successors) give one identity per person and in-context reputation, without any party being able to join records across contexts. The definition's linkability condition is specifically "across contexts" (l.103).
  - The Narayanan–Shmatikov point (re-identification from sparse traces) is a real residual risk. It is a risk, not an entailment.
- **Agents (l.252–286).**
  - The vote-buying argument holds and is the most original point in the paper. Receipt-freeness is incompatible with agents that can make verifiable commitments, so keeping the modes apart requires inspecting payments.
  - Weaker: "What is verified about the agent is thereby disclosed about the person" (l.260). Verifying a commitment ("I will pay $x$ if $y$") discloses that commitment, not the policy. TEE or ZK attestation of policy properties is the obvious reply, and it is not addressed.
  - The legality check: "Whether such an agent refuses silently or reports is a configuration choice" (l.286). A silently refusing agent creates no retained third-party record. So this is a possibility the proposal opens, not one it entails.
  - Calvano et al.: fine as motivation for supervision, which is not the same as personal surveillance.
- **Disputes and prohibitions (l.290–300).**
  - Retention: the parties can keep their own signed transcripts and produce them in court, as they do today. Ordinary contract law already satisfies the definition's retention and linkability conditions for the contracted domain. The novelty therefore lies only in coverage, which the article concedes at l.483–488.
  - Bostrom: see §4.
- **The conclusion at l.315.** "The six requirements together satisfy the four conditions of our definition of surveillance, with coverage equal to the set of domains in which contracts are enforced." Overstated on two counts. Linkability across contexts is not established, as above. And "equal to" conflicts with "at least as wide as" (l.319).

### C3. Constitutional closure

- **Argued, but with a selective premise.** The key sentence is "A domain is opened whenever the reported harms in it exceed the cost of monitoring it" (l.328). That describes the economic mode only. The article's own summary says the system also has "a democratic mode with equal weight per person" (l.68). A majority that values privacy could use it to close domains. This route to a privacy floor is never discussed.
- **The proposal's own entrenchment mechanism is used in one direction only.** "Which rules stay fixed and which stay open is itself priced and settled by mutual agreement" (l.69), and some rules "harden by mutual agreement so that investment can rely on them" (l.366). The article uses hardening only to argue that monitoring becomes fixed (l.367–368). The same mechanism could harden a privacy floor. The article instead says a floor "contradicts the essay's aim that baselines be cheap to revisit" (l.554).
- **"An unobserved domain is a ceded entitlement" (l.331–335).** Correct under Remark 1 if enforcement must be ex ante and automatic. Under ex-post liability with claimant-supplied evidence, it does not hold.
- **The data-externality results (l.342–344).** Correctly invoked, and the strongest support for the claim that privacy sells cheaply.
- **The veto-reimbursement extension (l.348–352).** The article flags it as an extension, which is honest. It is still the article's rule, not the essay's.

### C4. Irreversibility

The vested-interest point (l.362–364) is plausible and novel. The other two are weaker:

- "The monitoring layer is therefore the first thing to become fixed" (l.368) assumes that every hardened rule is automatically enforced.
- The sovereign argument restates the definition's rationale; it does not add to it.

These are plausibility arguments, not entailments, and "commitment … irreversibility" (l.119) is claimed as if argued to the same standard as entailment.

### C5. Cryptography

- **Proofs concern commitments.** Correct: this is the standard oracle problem. It answers the essay's privacy reply as far as sensing goes.
- **Prices disclose.** The differencing example (l.401–402) works only for the article's own construction, a fee that is "the sum of the households' reservation prices". The Dinur–Nissim invocation (l.408) is loose. Their reconstruction needs many accurate answers to different subset queries chosen by the attacker. A routing agent re-querying one street's fee over time does not get different subsets of households. The article half-concedes this at l.563.
- **Remark 2.** The mathematics is correct, and it shows what the prose says: under ε-DP with a small ε, one household cannot move the expected price from negligible to prohibitive, or to zero. The objection is that DP may be the wrong privacy target. The household wants its report to move the price; that is the contract. What it plausibly wants hidden is the reason (asthma), which a ZK credential can hide while the valuation is revealed. The article treats revealing a valuation as a privacy failure without arguing that the essay's promise covers valuations. "Complete privacy and control over their cognitive profile" (l.23) arguably does cover them, so this is answerable, but the article does not answer it.
- **The JDP point (l.437–442).** Correct and well made.
- **Composition (l.444–447).** Overstated. If the inputs have not changed, repeated queries can be served from a cached noisy release at no extra privacy cost (post-processing). Releases need to track only changes in the reports, and continual-observation methods give polylogarithmic error. "must either spend an unbounded privacy budget or add noise that grows until the prices no longer track" holds only if the underlying reports change continually.
- **The final sentence (l.452).** Fair as a conclusion.

### C6. The trilemma

Given the definitions, "granular coverage" ("any externality … is contractible", l.541) plus automatic enforcement rules out privacy almost by Remark 1. The trilemma is therefore close to definitional. The substantive question is whether the essay is committed to "any externality". "Any two can be had" (l.545) is asserted with examples, not shown, and it ignores mixed regimes such as probabilistic audit.

## 3. Unargued assumptions an unsympathetic expert would refuse

1. That enforcement must be ex ante, exhaustive and automatic, rather than probabilistic or ex post on claimant evidence.
2. That the negotiation runs in the economic mode wherever privacy is at stake (l.328).
3. That cross-context linkage follows from reputation and identity. Anonymous credentials are not mentioned.
4. That information revealed to a counterparty or carried in a price counts as "surveillance". The definition counts any counterparty-controlled device (l.94). Under that standard an ordinary market transaction recorded by the seller already qualifies.
5. That a state duty to prevent catastrophe will in fact be exercised through agents (l.300: "has an evident place to look").
6. That the essay aims at zero unpriced externalities (l.144). See §4.

## 4. Attacks on positions the target does not plausibly hold (judged from the article's own summary)

- "the essay's aim is that no such gaps remain, since each gap is an unpriced externality" (l.144). The article's own account says the essay "concedes … that some risks cannot be priced at all" (l.22), and its examples are local and selective. Nothing in §"The proposal" attributes a no-gaps aim to the essay. The article supplies the aim, and the "total" conclusion leans on it.
- Bostrom (l.297–300). The essay borrowed a case from Bostrom; it is not shown to accept his conclusion. Preventive policing is also a duty of any state that prohibits catastrophic acts, not something specific to DACN. The paragraph insinuates rather than argues.
- The privacy floor (l.552–554). The article says a floor contradicts the essay's aim. On the article's own account, the essay provides for rules that "harden by mutual agreement" (l.366). A hardened privacy floor is therefore within the proposal, not contrary to it.
- The veto rule applied to privacy holdouts (l.348–352). The article admits this extends the rule beyond its stated use.

## 5. Internal inconsistencies

1. Total versus graded.
   - Title: "implies a commitment to total surveillance."
   - l.495: "Our implication is graded: surveillance coverage is at least contracting coverage."
   - Both can hold only under the dispositional reading of "total" discussed in §6, which is not the reading the title invites.
2. Equal versus at least.
   - l.315: "with coverage equal to the set of domains in which contracts are enforced."
   - l.319: "surveillance coverage must be at least as wide as contracting coverage."
3. No gaps versus unpriceable risks.
   - l.144: "the essay's aim is that no such gaps remain."
   - l.22: the essay "concedes … that some risks cannot be priced at all."
4. Independence from predation versus reliance on non-commitment.
   - l.28: "The argument does not depend on … the state being predatory."
   - l.113–115: surveillance is defined by collection because access "can be changed after the record exists, by parties other than its subject", citing the sovereign's inability to commit. Irreversibility (l.370–375) and the open question at l.566 depend on the same point.
   - "Predatory" and "unable to commit" are not the same thing. Still, the reason the definition ignores access controls is the prospect of misuse, so the article does depend on a non-benign sovereign.
5. Hardening used in one direction only.
   - l.366–368: hardened rules make monitoring "the first thing to become fixed."
   - l.554: a hardened privacy floor "contradicts the essay's aim that baselines be cheap to revisit."
6. Preferences optional versus decisive.
   - l.227–228: "Preference privacy is the weakest of our six links … The other five do not depend on it."
   - l.225: "The efficiency gain that the proposal promises over the present is available to the degree that the first branch is taken."
   - The first passage says the proposal can work without verifiable preferences. The second says its gains depend on them. Calling them "links" also suggests a chain, in which the weakest link would break the rest; the article means six independent requirements.

## 6. Is "implies" earned, and does "total surveillance" mean what readers will take it to mean?

- **The definition.** "Surveillance is *total* when no domain of conduct that affects other people is excluded from $D$ by a rule that the surveilling parties are unable to change" (l.105). Read literally, this is a modal property of the exemptions, not a size for $D$. A regime with a small $D$, all of whose exclusions can be amended, is "total". So is any constitutional democracy with an amendable privacy clause, once it has any surveillance with coverage $D$.
- **What readers will hear.** Comprehensive actual collection over (nearly) everything. The article delivers that only conditionally: coverage at least equal to contracting coverage, plus a tendency, argued in C3, for contracting coverage to grow.
- **Further problems with the definition.**
  - It requires that the *surveilling parties* be unable to change the rule. In DACN the negotiators are everyone, while the surveilling parties are counterparties, providers and courts. The article treats these as one group.
  - The definition rules out access controls by design (l.113). That is defensible, but it means a regime with strong, enforced access law and a recorded but unread ledger still counts as "total surveillance". Many readers would dispute that label.
- **"Implies."**
  - Earned for: "coverage ⊇ contracting coverage, for the sensing condition", given automatic ex-ante enforcement.
  - Earned for: "no exogenous exemption", which follows from the definition of constitutional scope.
  - Not earned for: the tendency toward large coverage, the cross-context linkability condition, or irreversibility. These are plausibility arguments.
  - The abstract is more accurate than the title: "a three-way trade-off". A title such as "…cannot also promise privacy" would match what is shown.

## 7. Hard to follow, used before defined, or formal statement versus prose

- **Remark 1** does not say what the surrounding prose says. It bounds contracts by the enforcer's signal. The prose concludes recording "by devices or parties that the person does not control", "for nearly every person". Nothing in the formal set-up models who generates $\sigma$, what it costs, or whether it can be random.
- **"A refinement of $\sigma$ under another name" (l.133).** A neat line, but no ordering of signals is defined.
- **The revelation-principle sentence (l.218–219)** slides from outcome equivalence to "the reports are inputs to it".
- **"Political Coase problem."** Used at l.507 ("again") and alluded to at l.115. Acemoglu (2003) is cited at l.371, but the problem is never stated.
- **"Harberger-style tax."** Not explained. Most economists will know it; law readers may not.
- **"Bargaining club"** is introduced in the summary, but the mechanism (who aggregates the reservation prices, and what is posted) is never specified. The differencing attack at l.401 assumes a posted sum the essay is not shown to use.
- **Remark 2.** The statement and proof are correct, and the prose reads them correctly. The phrase "anything one household reports" (l.432) is right for neighbouring profiles.
- **Dinur–Nissim (l.408).** The theorem's query model does not fit the prose's setting (§2, C5).
- **"Commitment."** Defined (l.117–119) as entailment plus irreversibility, but the title uses "a commitment to", which reads as an intention.

## 8. Single most damaging objection

The title's conclusion is reached by equivocating on "total". As defined at l.105, surveillance is total whenever no exemption is beyond amendment. That is satisfied by any amendable constitution and says nothing about how much is collected. The substantive claim the article actually supports is graded: "surveillance coverage is at least contracting coverage" (l.495). Two things block that claim from becoming coverage of everything:

- The step from Remark 1 to universal continuous recording of nearly every person ignores probabilistic and ex-post enforcement (audits, costly state verification, claimant-supplied evidence).
- The step from the open constitution to expanding coverage rests on the economic mode alone. It ignores the proposal's own democratic mode and its mechanism for hardening rules, either of which could entrench a privacy floor. The article uses hardening only to fix monitoring in place.

What survives is a strong, narrower result: automatic, ex-ante enforcement of personalised externality contracts cannot coexist with the essay's privacy promise, and DP or ZK do not close the gap. The title claims more than that.
