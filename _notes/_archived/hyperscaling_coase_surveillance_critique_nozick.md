# Red-team report: Nozick (with a mathematics PhD) on `hyperscaling_coase_surveillance.qmd`

Written 2026-11-19. Sources read: Krier's essay (fetched from cosmos-institute.org 2026-11-19), the claims ledger, the article, the prior-critiques summary. Confidence marks on external texts: [sure], [likely], [unsure]. Line numbers refer to the `.qmd`.

## Position in one paragraph

I defend the voluntary-exchange core: persons hold rights that are side constraints; holdings are just if they come from just acquisition and transfer; a person may sell anything they own, privacy included; the state is minimal. Four of Krier's devices are incompatible with that position and I give them up: the Harberger-style "option fee" (a tax on holdings that also works as a forced sale), the requirement that "any coalition that vetoes must then reimburse that quantified loss" (a liability charged for declining to sell what one owns), "periodic voting on baseline entitlements" with equal weight (this is demoktesis, the end point of ASU ch. 9's "Tale of the Slave" [sure]), and pricing spillovers that cross no boundary, such as "neighborhood character" and the non-smoker's narrowed social world. What remains is Krier's core layer ("complete privacy and control over their 'cognitive profile'") plus voluntary contracting over boundary crossings, with state courts. Against *that* proposal most of the article's constitutional argument does not apply. Against Krier as written, a good part of it does. The article never separates the two, and it should.

---

## D1. Is DACN Krier's position?

**Verdict: HOLDS WITH NARROWING.** Krier supports two of the three clauses of "constitutional scope". He does not support the clause that does the work, which is that the bargaining agents revise the baseline, including constitutional rights and privacy.

Where Krier supports the article:
- "Agents don't magic it away; they only make it explicit, contestable, and cheap to renegotiate." ("it" is the baseline of who holds which entitlement.)
- "Beyond periodic voting on baseline entitlements, agents could fundamentally transform how citizens deliberate … continuous liquid democracy."
- "an agent-mediated system could explicitly price the value of stability versus flexibility, letting some rules ossify by mutual agreement (basic property rights, contract enforcement) while others remain perpetually negotiable (noise ordinances, parking rules)." This supports the third clause, that the boundary between fixed and open rules is settled by agreement.

Where Krier contradicts the article:
- "My view here is that we already have many of these rights set up by centuries of jurisprudence, and this is the right starting point. To the extent that these need to change or adapt, our democratic political systems are the right mechanism to do so." Baselines are revised by the democratic process, which agents improve. They are not revised by bilateral bargaining.
- "The (gradually automated) state continues to define and enforce basic property rights, contract law, criminal justice, and constitutional rights - the bedrock rules without which agent negotiations would be meaningless."
- "the state's role is not just to enforce the contracts that agents make, but to define the absolute boundaries of what they are permitted to do".
- Privacy sits in the innermost doll as a "should", alongside the person's control over their own profile. Krier never lists privacy among the things that are negotiable.
- "the constant renegotiation of property rights would destroy investment incentives."

So Krier's position is: agent-assisted bargaining inside a bedrock the state enforces, where the bedrock is amendable by a democratic process that agents improve. That is not "the same agents negotiate … the baseline assignment of entitlements" (l.85). It is closer to the case the article says "could stop there" (l.320).

The overread becomes decisive because of a formal point. Under the article's definition (l.105), every constitutional democracy with an amendment procedure already has no domain "excluded … by a rule that the surveilling parties are unable to change." Krier's bedrock is amendable, and so is the US Bill of Rights. If amendability is enough, the closure argument applies equally to the status quo. If it is not enough, the article needs a measure of how costly a change is, and the definition has none. "Cheap to renegotiate" is the only textual hook, and Krier attaches it to trading *from* the baseline more than to rewriting the baseline.

Ledger claims that attack something Krier does not say:
- Abstract, l.6: "The proposal extends the bargaining to the baseline entitlements themselves". Krier gives baseline revision to democratic systems, not to bargaining.
- C14, l.326: "the essay proposes that the settlement be cheap to revisit". Half true. He also says agents "would likely converge on stable equilibria" and that constant renegotiation is destructive.
- C15, l.335: privacy is "open to renegotiation on the same terms". Krier never says so and places privacy in the core.
- C17: the article admits this is an extension, and it runs against Krier's explicit privacy commitment (see below).
- C5, l.176: Krier aims the Harberger levy at "chronic hyper-bidders" blocking development. Applying it to declared medical circumstances is the article's move.
- l.187: "The essay says of such cases that the decision still belongs to the individual." Krier's sentence ("The choice remains with the individual, but it is now a truly informed choice") is about smoking policy, not insurer disclosure. In the insurer case his offer is explicitly conditional: "if you empower your agent".
- C13, l.297: "The essay borrows the case" from Bostrom. Krier cites no source for "easy nukes" and proposes prohibition, not prevention. Calling it a borrowing is fair as provenance. "Follows the premise to a conclusion that the essay does not report" implies an omission, but Krier does not adopt Bostrom's framework.
- C26, l.476: Krier's "right to an agent" is offered as an equity measure analogous to public defenders. It is not a judgment that non-enrolment is untenable.
- l.554: "the essay's aim that baselines be cheap to revisit". Partial, as for C14.

**Narrowing that saves it.** Define DACN as Krier writes it: agents bargain inside a bedrock; agents also take part in a continuous democratic process that can amend the bedrock; and agents agree among themselves which ordinary rules ossify. Then argue that cheap, continuous, agent-mediated amendment differs in kind from today's costly amendment. That requires a cost parameter in the definition of "total".

**What would settle it.** Ask Krier whether privacy of the cognitive profile is part of the bedrock or a default open to democratic revision. His text points to bedrock.

## D2. The four-condition definition

**Verdict: HOLDS WITH NARROWING.** As a parameterized notion ("surveillance with coverage D") it is defensible, and it correctly separates collection from access. It wins by stipulation in two places: the name "surveillance" carries a normative charge that the conditions do not, and "total" is defined modally in a way that comes apart from coverage.

Arrangements that satisfy it and that few would call surveillance:
- A land title registry (D = real-property holdings). It is kept by a registrar the owner does not control, bound to a legal identity, retained indefinitely, and joinable by courts and tax authorities on terms the owner does not set.
- Hospital records under a national health identifier (D = clinical circumstances).
- Notarized contracts and court dockets.
- Credit-bureau histories. Some would call these surveillance, which shows the boundary is contested, not settled by the definition.

Arrangements that are plainly surveillance and escape it:
- Bentham's inspection house, which l.111 cites as the model. The inspector watches and keeps no record, so it fails Retention, and arguably Attribution. The cited paradigm fails the definition.
- Live CCTV monitoring without recording, and an informant who reports orally.
- Targeted wiretaps of a few suspects. They fail "nearly every person", so the definition is of *mass* surveillance and should be labelled that way.
- A mandated self-tracking app on the person's own phone, with upload on demand. On a literal reading the person controls the device, so Sensing fails, yet this is plainly surveillance.

The "does not control" clause. When the sensor is the person's own agent, and the agent records locally and discloses only under contracts the person entered, Sensing fails and Linkability is contestable. The person agreed to the dispute forum, so did they "set" the conditions? The definition is silent. The article's conclusion therefore needs a further premise: enforcement requires records the obligor cannot suppress (l.140). That premise lives in the derivation, not in Remark 1, and it is contested (tamper-evident sensors on the obligor's own equipment, such as tachographs, are controlled by the obligor and cannot be suppressed by them).

The cleanest case is the vehicle on the asthmatic child's street. The sensor is the *resident's* device, recording a crossing into the resident's air. Relative to the driver it satisfies Sensing. From a rights standpoint it is the victim's own evidence of a boundary crossing, of the same kind as a doorbell camera or a stretch of fence. The definition calls it surveillance. A rights theory distinguishes it from sensing inside the driver's cab. The morally relevant variable for me is consent together with the place where the sensing happens, not collection, and the definition is constructed so as not to see that variable.

The formal defect in "total" (l.105): "no domain … is excluded from D by a rule that the surveilling parties are unable to change." Read literally, this holds whenever no unchangeable rule exists, *whatever D is*, including D = ∅. "Total" as defined is a property of the rule set, not of coverage. The title's "total surveillance" therefore follows from two things: (surveillance with some coverage D) and (no entrenched rules). It does not follow from D expanding. The intended reading, that D will expand to every domain affecting others, is a dynamic claim (C14), and the definition does not encode it.

**Narrowing.** Rename the definition "mass record-keeping with coverage D" or keep the term and add a "sensing location" condition. Redefine "total" as: D contains every domain affecting others in which the cost of monitoring is below the reported harm. That is what C14 actually argues.

**What would settle it.** Test the definition against a panel of clear cases (registry, medical record, CCTV, panopticon) and report where it disagrees with ordinary judgment.

## The logical form of the title

Reconstruction:

- P1 (Krier). Agents form contracts over externalities at the granularity of persons and moments. The contracts settle automatically, and courts are the backstop.
- P2 (article, Remark 1). An enforceable transfer is a function of the enforcer's signal σ.
- P3 (article). For automatic settlement, σ must be produced without the obligor's cooperation, retained, bound to a unique persistent identity, and joinable on judicial demand.
- P3′ (article, implicit). Nearly every person contracts in each contracted domain.
- ⊢ L1. There is surveillance (D2) with coverage ⊇ the contracted domains. *Valid from P1, P2, P3, P3′.*
- P4 (Krier, partly). Which domains are contracted is set by agreement among agents and by agent-mediated democratic revision.
- P5 (article, empirical). A domain is opened whenever reported harm exceeds monitoring cost, and monitoring cost tends to zero.
- P6 (article; depends on the D1 reading). No exclusion is entrenched beyond the negotiators' reach.
- ⊢ L2. Surveillance is "total". *Valid from L1 and P6 alone on the literal definition, and trivially so (see D2). On the intended reading it needs P5 and is "made likely by", not implied.*
- P7–P9 (article). Vested fee income; hardened rules presuppose sensing; the sovereign controls the apparatus.
- ⊢ L3. "Commitment". Entailment is the tautology "adopting DACN adopts its preconditions", already contained in L1. Irreversibility is "made likely by" P7–P9, which are political-economy conjectures.

Of these premises, P1 alone is Krier's. P4 is half his. P2, P3, P3′, P5, P6 and P7–P9 are the article's. The inference is a valid implication only as far as L1, and only given P3, which sparse-audit and victim-side enforcement contest (see the Remark 1 note below). The title asserts "implies … total … commitment". At most "implies mass record-keeping over the contracted domains" is warranted. The rest is "makes likely", conditional on a reading of Krier (P6) that D1 shows he does not hold.

## Remark 1 as mathematics

**Verdict: HOLDS as stated, but it is a definition and not a result; the prose draws more from it than it contains.**

Given t = t(s) and s = σ(a, θ), the first sentence is immediate. The second is the Doob–Dynkin lemma: f(a, θ) is σ(σ)-measurable iff f = t∘σ for measurable t, which needs standard Borel spaces. That hypothesis goes unstated but is harmless.

Three overreaches:
1. **Messages are excluded by assumption.** Once transfers can depend on parties' reports, t(s, m), mechanisms of the Moore–Repullo kind can implement outcomes that depend on information the parties observe and the enforcer does not [likely]. The remark restricts the contract space; it does not discover a limit on it. This is weak point 6.
2. **Coverage of sensing ≠ coverage of contracting.** If σ is random, sensing each instance with probability q and penalizing at 1/q of the scale, contracts stay measurable with respect to the realized σ and incentives are preserved in expectation (the Becker logic). l.143, "The sensing must be as wide as the contracting", does not follow. What follows is that sensing *capability* must reach every contracted domain. Records of nearly every person's conduct do not follow. Under random audit, P3′ fails for Attribution and Retention.
3. **"Hyper-granular contracting is a refinement of σ under another name" (l.133).** This holds only for contracts that condition on conduct. Contracts that condition on a party's *own* announced price (a posted toll, an ask) need σ to reveal only that the toll was paid. The asthma street's toll is of that kind: the truck pays or reroutes, and the payment is its own evidence (C4).

## Remark 2 as mathematics

**Verdict: the statement and proof are correct under unstated hypotheses. It does not say what the surrounding prose says.**

Check: for M ∈ [0, p̄], E[M] = ∫₀^p̄ Pr[M > x] dx. ε-DP applied to S = (x, p̄] gives Pr[M(θ) > x] ≤ e^ε Pr[M(θ′) > x]. Integrating gives the upper inequality, and swapping θ and θ′ gives the lower one. Both directions are right.

Hypotheses needed:
- (i) Prices are nonnegative. The labour example has the price "invert", that is, go negative. Once negative prices are allowed, the multiplicative bound fails and only an additive bound of order (e^ε − 1)·range survives.
- (ii) Pure ε-DP. Under (ε, δ)-DP the bound becomes E[M(θ)] ≤ e^ε E[M(θ′)] + δp̄.
- (iii) Neighbouring profiles differ in one report. A household of several members, or one household reporting in several roles, gets e^{kε}.
- p̄ is used only for integrability.

The numerical claims are right: ε = 0.1 gives about ±10%; a move from "negligible to prohibitive" by a factor of 10⁴ needs ε ≥ 9.2; and a positive expectation cannot reach zero.

Mismatch with the prose. Remark 2 bounds a price that is DP *with respect to the household's report*. Krier's privacy promise is that "preferences are communicated and aggregated without revealing sensitive underlying data". The underlying data is the asthma. The price is a bid the household chooses to post. A seller who posts an ask has disclosed the ask by choice; DP protects data subjects from a curator, not a bidder from his own bid (weak point 3). Krier needs the price to be uninformative about the *reason*, and many reasons map to one bid. The claim "differential privacy bounds the personalization of prices" (abstract, l.10) is true only if privacy is defined to include the bid itself. Krier does not define it that way, and in the rights framework the bid is the household's own information to sell. Where Krier does invoke aggregation (coalition prices from many members), Remark 2's regime, many contributors each mattering little, is exactly where DP works, and the remark does not hurt him. The differencing attack (l.401–402) is real but narrower: it reveals one household's share of a street total to an observer who sees both the before and after totals. Residents can split a street toll among themselves by MPC and publish only the total.

**Narrowing.** "If the bid itself is to be protected from observers, DP bounds how much one household's bid can move the posted price." Keep the remark. Drop "bounds the personalization of prices" as a general statement.

## C6. Unravelling makes "voluntary" disclosure involuntary

**Verdict: FAILS as a claim about voluntariness. HOLDS as a claim about prices.**

The sentence: "That is true of the choice set and false of the equilibrium." (l.188). In equilibrium every agent *chooses* to disclose; "false of the equilibrium" is a category error. On my account [sure, ASU ch. 8, "Voluntary Exchange"]: "Other people's actions place limits on one's available opportunities. Whether this makes one's resulting action non-voluntary depends upon whether these others had the right to act as they did." The low-risk customers who disclose, and the insurer who prices non-disclosure, act within their rights. The high-risk customer's disclosure, or the higher premium they pay, is a voluntary response to a narrowed but rightful choice set.

Apply the offer/threat distinction. The insurer's discount for disclosure improves on the baseline, so it is an offer. The rise in the non-discloser's premium is not a threat by anyone. It is a market price formed by others' rightful disclosures. No one proposes to cross the customer's boundary.

What does hold: under Grossman–Milgrom assumptions [sure], the price of silence converges to the worst-type price, and "privacy at the old pooled price" leaves the menu. The assumptions are verifiable, costless disclosure and a receiver who knows the sender holds the information. Dye (1985) shows partial disclosure when the receiver is unsure whether the sender is informed [sure], and the article omits that caveat. Krier's ZK proposals make verification cheap, so they push towards full unravelling. That is a fair point against him.

**Narrowing.** "Cheap verification makes privacy costly in equilibrium; the cost falls on bad types, and no rights violation is needed to produce it." This is a claim about distribution and welfare, not voluntariness.

**What would settle it.** State which theory of voluntariness the article uses. If it is a moralized baseline, mine gives the opposite verdict. If it is a predictive baseline, say so and drop "not voluntary".

## C15. "An unobserved domain is a ceded entitlement"

**Verdict: FAILS in general. HOLDS for the narrow class of non-boundary "externalities".**

The sentence: "A right to be unobserved in the home is, mechanically, a right to impose unpriced externalities from the home." (l.334). This runs together *entitlement* and *enforceability*. On a boundary-crossing account, a right is a constraint on what others may do to you. My right that you not install sensors in my home does not give me permission to send fumes or noise across your boundary. That remains a wrong, compensable on whatever evidence exists. And the evidence for a boundary crossing is available *at the boundary*, on the victim's side, from sensors the victim controls: fumes in the child's bedroom, decibels at the neighbour's wall. I discuss pollution in exactly these terms, as a crossing compensable by the principle of compensation (ASU ch. 4, with a note citing Coase 1960 and Michelman, "Pollution as a Tort" [sure]). Remark 1 bounds what can be *collected*. It does not change who is *entitled*. "Mechanically" holds only in a de facto sense.

Where it holds: Krier's spillovers that cross no boundary. The sugar drinker's cost to a shared insurance pool, "neighborhood character", the non-smoker's narrowed options. Measuring these does require sensing inside the actor's domain. In my framework they are not rights violations and no compensation is owed, so nothing is ceded by leaving them unobserved. Against Krier as written, who prices "negative-sum" effects generally, the claim has force. Against a rights-bounded Krier it has none.

**Narrowing.** "For externalities that can be detected only inside the actor's domain, exempting that domain from sensing leaves them unpriced." Then acknowledge that boundary-crossing harms can be priced by sensing on the victim's side.

## C16. Alienable privacy is sold cheaply

**Verdict: HOLDS against Krier as written. FAILS as a rights objection.**

The data-externality results are correctly characterized [likely for all three; Acemoglu et al. on welfare gains from shutting the market, likely]. But that someone sells cheaply what they own is not an injustice. My disclosure about myself that is informative about you takes nothing that is yours; ASU recognizes no property in information about oneself held by others [likely]. The welfare loss (Acemoglu) is real. It is not a rights argument. "To repair it by the essay's method … would require tracing what each disclosure reveals about third parties" (l.345) holds only if Krier prices *all* spillovers. Krier's text does seem to ("negative-sum" generally), so against him the regress point stands.

**Narrowing.** Present it as an efficiency argument against pricing all spillovers, not as an argument about privacy rights.

## C17. The veto-reimbursement extension

**Verdict: FAILS as a reading of Krier. HOLDS as a conditional about a rule applied without exception.**

Krier: "Any coalition that vetoes must then reimburse that quantified loss … Stonewalling remains possible, but it now carries a real, rising cost." The article: "Nothing in the mechanism distinguishes a homeowner who blocks a building from a resident who declines sensors" (l.350), and "the extension follows from applying it uniformly" (l.351).

Three objections:
1. **Something does distinguish the cases: Krier's own text.** The resident's privacy over their cognitive profile is in the core doll ("complete privacy and control"). Applying the veto rule "uniformly" means overriding an explicit contrary commitment. A rights-based reading treats privacy as a property-rule entitlement, and the veto rule then does not reach it.
2. **On the merits, the rule is itself unjust, and the extension inherits the injustice.** Making a person pay others for gains forgone because he would not sell what he owns is a charge for withholding a benefit nobody was owed. My test for an unproductive exchange is: "if they were impossible or forceably prohibited … one of the parties to the potential exchange would be no worse off" [sure, ASU ch. 4, "Productive Exchange"]. The neighbours' "loss" from my declining sensors is measured against a baseline in which I had already surrendered my domain. They lose nothing that is theirs. I give up the veto-reimbursement rule entirely; it is a liability rule on property, and Petel already observes that agent markets reach for liability rules (see the reprise check below). My treatment of blackmail runs the other way and is instructive: someone holding information may charge "only for what he forgoes by silence" [sure]. The article's extension makes the *subject* pay others for *their* forgone revelation. That is the blackmail structure, not a principle of compensation.
3. **The two examples contradict each other internally.** The neighbours can sense fumes on their own property, so their fee income is not blocked by my declining sensors in mine. And if non-discloser customers are priced as the worst case (C6), they impose *no* extra cost on the insurer's pool. C17 needs pooling, and C6 says pooling unravels. They cannot both hold.

**Narrowing.** "If Krier's veto rule were applied to every refusal to contract, privacy holdouts would pay; Krier should therefore confine the rule, and a rights theory says how."

## C18. Legitimacy needs population-wide identity, fidelity and separation checks

**Verdict: HOLDS WITH NARROWING.**

Krier does have an equal-weight democratic mode, so against him the claim has a target. But it divides into three parts.
- **Identity.** Population-wide identity checks are what voter rolls already are. They are not new and are rarely called surveillance.
- **Fidelity.** Auditing a delegated agent's model against the person (l.268) *is* new and is the strong part.
- **Legitimacy premise.** On my view a settlement is legitimate because individuals consent and rights are respected, not because a vote counted everyone once. In a framework of voluntary communities with exit (ASU ch. 10 [sure]), a community that votes by agents needs fidelity checks only on its own members, who joined on those terms.

**Narrowing.** Restrict the claim to continuous delegated democratic voting, and to its fidelity audit.

## C19. Irreversibility

**Verdict: HOLDS WITH NARROWING. It is political-economy conjecture, not entailment.**

1. "Monitoring becomes a vested interest of the monitored" (l.364). If the sensors and the income are the residents', this is their rightful interest. Each person can still stop contracting. Aggregate lock-in is a forecast, not a commitment in the sense of entailment.
2. "Every hardened rule that is enforced automatically presupposes the sensing that enforces it. The monitoring layer is therefore the first thing to become fixed" (l.367–368). The rules Krier names as ossifying, "basic property rights, contract enforcement", are enforced by courts after the fact on evidence brought in disputes, not automatically. The premise "enforced automatically" does not hold of Krier's examples, so the conclusion does not follow.
3. "The apparatus built to watch officials is the same apparatus that records citizens" (l.372). This is asserted. Krier's anti-corruption tools ("automated public spending monitoring", "real-time monitoring of regulatory capture") watch public transactions. Identity of the two apparatuses needs an argument.

**Narrowing.** Restate C19 as "the regime creates constituencies for monitoring, and a sovereign that cannot commit will control what exists", as a forecast that makes irreversibility likely.

**Does my dominant protective association already concede monitoring of this kind?** No [likely]. The association may prohibit independents' enforcement procedures that it deems unreliable or unfair, and it must compensate those it prohibits (ASU ch. 5 [sure]). Procedural rights against being punished by unreliable procedures (ASU ch. 5 [likely]) cut both ways. They demand reliable evidence, which favours records, but they concern the procedure applied once a dispute arises. The knowledge the association needs is knowledge of who is enforcing, by what procedure, against its clients, and it learns this from clients' complaints. Nothing in it requires monitoring conduct across the population before any dispute. The principle of compensation applies to prohibited *risky* acts (ch. 4 [sure]). It licenses prohibiting, say, private manufacture of bioweapons with compensation to those disadvantaged, not a dragnet over the innocent. So the minimal state concedes the C13 *problem* (prohibition of catastrophic risk). It does not concede Bostrom's *solution*.

## C20. "Leaner in rules, wider in evidentiary reach"

**Verdict: HOLDS WITH NARROWING.** Krier does write "it just makes it a lot leaner". The quotation is accurate. The rejoinder that the state's evidentiary reach "extends to every contracted act of every person" (l.375) holds only if the state holds the records. In a distributed scheme the courts reach records *on demand in a dispute*, which is today's position for any private record that can be subpoenaed. **Narrowing.** "Wider in what it could reach on judicial demand", and compare with present subpoena reach (weak point 8).

## C26. Participation is voluntary

**Verdict: HOLDS WITH NARROWING.** "Exit from a provider is not exit from the regime" (l.473) is true. But Krier claims exit only from providers ("A user who finds these policies too restrictive … can … take their business to a competitor") and voluntariness only for the bargaining clubs ("these institutions can be voluntary"). The reply is a fair anticipation of the objection, not a refutation of something he says.

The subsidy inference fails. "An institution that requires subsidy to ensure universal enrolment is one in which non-enrolment has been judged untenable" (l.477) is a non sequitur. Public defenders do not make *not being prosecuted* untenable.

The rights analysis is the same as for C6. Non-enrolment that becomes costly because of others' rightful choices is not coercion. If instead the *state* forbids contracting or enforcing disputes except through agents, my ch. 5 argument requires it to compensate those it disadvantages [sure]. That would be the principled ground for Krier's vouchers. It is evidence that the state is prohibiting an alternative, not evidence that people are being forced to enrol.

**Narrowing.** "There is no exit from the regime short of emigration, as with any state; non-participation is penalized by market prices and, wherever the state channels disputes through agents, by law."

## C27. Surveillance already exists

**Verdict: HOLDS WITH NARROWING.** The distinction it draws, partial and probabilistic collection today against complete and legally consequential collection under the proposal, is the right one. "Constitutive of legal rights" (l.486) is wrong. Records *evidence* rights and contracts *constitute* them. Land registries, bank ledgers and medical records already have legal standing, so "being absent from the record has a cost that no one bears today" (l.487) is false for anyone without a title deed or a credit file. The missing comparison is with the regulatory state's own measurement for taxing and inspecting (weak point 8).

## C28. The system can stay small

**Verdict: HOLDS** on the reading of Krier ("The same mechanisms used to settle a parking dispute can be adapted and scaled up …"). It is a real concession and, logically, it costs the title: "A bounded club with voluntary membership, mutual visibility and free exit has monitoring that its members control" (l.496) is my framework for utopia. If the large-scale regime is a federation of such communities with exit, the article's argument loses weight there too. Then the operative variables are scale and exit, not DACN.

## C29. Symmetric transparency

**Verdict: HOLDS.** Fair to Brin (1998) [sure on the book and thesis].

## C33. Scott

**Verdict: HOLDS WITH NARROWING.** Krier is quoted fairly ("agent networks can provide governments with high-resolution, real-time feedback about … citizen preferences"). But "The cure the essay offers for the state's poor eyesight is the condition Scott identified as dangerous" (l.532) overstates. Scott's disasters needed four elements together: administrative legibility, high-modernist ideology, an authoritarian state willing to coerce, and a prostrate civil society [sure]. Legibility alone is the *capacity*; Scott acknowledges that legibility also underwrote benign state functions [likely]. Krier's whole programme opposes high-modernist planning. **Narrowing.** "Supplies one of Scott's four conditions; the political Coase problem the essay concedes supplies a second." Petel already cites Scott (and Goodhart) on measurement as political (see the reprise check).

## Weak points 1, 2, 4, 10

- **WP1 (definitional victory).** Confirmed and sharpened. "Total" is satisfied by D = ∅ under the literal definition, the cited panopticon fails the definition, and the "does not control" clause turns on an unstated premise about suppressibility. See D2.
- **WP2 ("implies" carried by prose).** Confirmed. Implication holds only as far as L1 (mass record-keeping over contracted domains), conditional on P3. T4/C34 ("any two can be had") is not a theorem. Its three cases are illustrations, and the third property, "Privacy", is defined so as to be the negation of the article's definition of surveillance, so "coverage + enforcement ⇒ ¬privacy" is L1 restated, not an independent trade-off.
- **WP4 (overreads Krier).** Confirmed. See D1. Privacy sits in Krier's core layer, constitutional rights in his state-enforced bedrock, and baseline revision in democratic systems.
- **WP10 (C17 and Bostrom are extrapolations).** Confirmed. C17 contradicts Krier's privacy commitment and is internally inconsistent with C6. The Bostrom step attributes an unreported conclusion to a source Krier does not cite.

---

## Claims outside my list I believe are wrong (brief)

- **C5 (l.176).** The levy on declared vulnerability attacks a use Krier does not propose (see D1). Applied to circumstances, a self-assessed levy also has the wrong comparative statics: it deters *overstatement*, and the honest asthma family declares truthfully and pays for a right they actually value. That is the levy working as designed, not a reductio.
- **C3 (l.156), "no interior stopping point".** The parties' own disutility from being observed is a cost of monitoring, so a voluntary contract stops where the marginal informativeness of a signal equals the observed party's taste for privacy. Holmström's principle says informative signals have *positive gross* value, not that net value is positive (weak point 7).
- **C13, prevention.** See C19. My minimal state prohibits catastrophic risks with compensation. Prevention by dragnet is a separate step, and the article's "evident place to look" (l.300) is a suggestion, not an implication.
- **C4.** Payment records leak location only if payments are linkable. Unlinkable payment tokens (Chaum) exist. The point needs C8's identity requirement to go through and should say so.

## Reprise check (against `_plans/hyperscaling_coase_prior_critiques.md`)

The article cites none of Ngo, Snow or Petel.

- **Petel 2025 anticipates the core thesis.** The summary quotes him: "the more we can enforce, the more we must sense". That is C1/T1 in one line. The article's introduction presents the enforcement–privacy conflict as its own claim. It must cite Petel and state its addition: the derivation, Remark 1, the closure argument, and Remark 2.
- **Petel on Calabresi–Melamed inalienability, and "privacy is a right, not a setting".** These are adjacent to l.321 and to the first escape condition (l.552–554: a privacy floor placed beyond renegotiation). Petel's slogan "price what you can, protect what you must" *is* the article's repaired proposal. The article should engage him as the existing statement of its own remedy. C15 ("privacy is a baseline allocation like any other") states the opposing view without naming Petel, who holds it.
- **Petel on proof of personhood** ("a neighborhood of one thousand can flower into … sock-puppet agents"), and on Harberger taxes that presuppose identity and honest oracles. This overlaps C8 and part of C7.
- **Petel on contracts that produce evidence, with retention limits.** This overlaps C13 (courts need retained records).
- **Petel and Krier on the political Coase problem.** Petel calls it "the hard stop: agents can't bind the sovereign". This overlaps C19(iii) and l.115. Krier concedes it himself, so the article cannot present it as an objection without noting both.
- **Petel citing Scott and Goodhart on measurement as political.** This overlaps C33.
- **Ngo's "Schelling fence".** A rule binding against later temptation; he applies it to property rights and the Harberger/land-value-tax line. Adjacent to the privacy-floor escape condition and to C19. Cite if the article says an entrenched rule is the remedy.
- **Snow.** On delegated judgment and the agent constructing the citizen's position, adjacent to l.267 ("the agent constructs the ballot"). The article's angle, auditing, is different, so a citation is enough.
- **Implied novelty.** The final open question, small-game joint DP (l.570, "as far as we can find, uncharacterized"), is not in the prior critiques. Nothing else is claimed as novel in so many words, but the introduction's framing ("This article examines that assignment") presents a thesis Petel stated in a sentence.

## The single most damaging objection

The title's force comes from constitutional closure, and closure depends on a reading of Krier he does not hold. Krier keeps "constitutional rights" as bedrock the state enforces, places "complete privacy and control" over the cognitive profile in the innermost layer, and gives baseline revision to "our democratic political systems". The article's first escape condition, a privacy floor beyond the agents' reach, is therefore already in Krier's text. The article half-concedes this at l.554 and calls it a contradiction with an "aim" Krier states only weakly. And once the floor is in, the definition of "total" cannot tell Krier's regime from any amendable democracy: on the literal definition (l.105), "total" holds whenever no rule is entrenched, whatever the coverage. What survives is L1: automatic enforcement of granular contracts needs mass record-keeping over the contracted domains. Even that holds only under premise P3, which random audit, posted tolls that are their own evidence, and victim-side sensing at boundaries all weaken. That narrower thesis is defensible, it is close to Petel's published line, and it should be the title.

## Tally

HOLDS: 2 (C28, C29). HOLDS WITH NARROWING: 10 (D1, D2, C16 against Krier as written, C18, C19, C20, C26, C27, C33, Remark 1). FAILS: 3 (C6 as a voluntariness claim, C15 in general, C17 as a reading of Krier). Remark 2: the mathematics is correct; the interpretation needs narrowing (counted separately). The title's "implies" is valid only for the weakened L1.
