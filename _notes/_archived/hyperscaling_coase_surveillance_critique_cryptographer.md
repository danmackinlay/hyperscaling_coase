# Red-team: cryptographer in privacy-preserving mechanism design

Target: `_plans/hyperscaling_coase_surveillance.qmd`, mainly "Cryptographic privacy". Ledger: `_plans/hyperscaling_coase_surveillance_claims.md`. Krier's essay read in full from the Cosmos Institute blog, 2026-11-19.

Confidence marks on named results: [sure] = I know the result and/or checked the text this session; [likely] = known from memory, not re-read; [unsure] = needs checking.

## Verdict tally

| Claim | Verdict |
|---|---|
| C23a (Remark 2 as mathematics) | HOLDS |
| C23b (Remark 2 and joint DP defeat the privacy reply) | FAILS |
| C21 (ZK leaves sensing, attribution, retention unchanged; linkability = authority key custody) | FAILS (oracle half holds) |
| C22 (prices disclose) | HOLDS WITH NARROWING |
| C24 (continuous repricing exhausts the budget) | HOLDS WITH NARROWING |
| C4 (payments are a trace) | FAILS |
| C8 (persistent, centrally certified identity with linked history) | HOLDS WITH NARROWING |
| C10 (auditing the vote = auditing the model against the person) | HOLDS WITH NARROWING |
| C11 (verifiable agents can sell votes; separation needs payment inspection) | HOLDS WITH NARROWING (first half holds and is stronger than stated; second half fails) |
| C12 (legality constraint = client-side scanning) | HOLDS WITH NARROWING |
| C25 (accountability needs an authority choosing whose records open) | HOLDS WITH NARROWING |
| D2 / weak point 1 (definition) | FAILS |

1 HOLDS, 7 HOLDS WITH NARROWING, 4 FAILS.

The one-line summary: cryptography does not rescue personalized prices from disclosing the bid, and it does not rescue the voluntary disclosure regime from unravelling and coercion. It does rescue enforcement from collection and linkage, which is what the article's definition of surveillance actually measures. The article aims its strongest technical argument (Remark 2) at the wrong privacy goal and its weakest (C21) at the part the literature has already solved.

---

## C23a. Remark 2 as mathematics: HOLDS

> "Let $M$ be an $\varepsilon$-differentially private mechanism that maps a profile of reports to a price in $[0, \bar{p}]$ … $e^{-\varepsilon}\, \mathbb{E}[M(\theta')] \le \mathbb{E}[M(\theta)] \le e^{\varepsilon}\, \mathbb{E}[M(\theta')]$."

The proof is right. For each $x$, $\{M > x\}$ is an event, so pure ε-DP gives $\Pr[M(\theta)>x] \le e^\varepsilon \Pr[M(\theta')>x]$; integrate the tail. Hypotheses actually used:

- **Nonnegative output.** Needed for the tail-integral identity. Boundedness is not needed (integrability suffices). Krier lets the emergency price "invert", i.e. go negative. For a range $[-\bar p, \bar p]$ apply the remark to $M+\bar p$: the bound becomes additive, $|\mathbb{E}M(\theta)-\mathbb{E}M(\theta')| \le (e^\varepsilon-1)(\mathbb{E}M(\theta')+\bar p) \approx 2\varepsilon\bar p$. Still bites. The article should state the nonnegativity or the shifted form.
- **Neighbouring relation: one person's report replaced.** For a household of several people treated as several reports, group privacy gives $e^{k\varepsilon}$. If the unit is the household, as the asthma example needs, fine.
- **(ε, δ)-DP.** The same proof gives $\mathbb{E}M(\theta) \le e^\varepsilon \mathbb{E}M(\theta') + \delta\bar p$. With δ ≪ 1/n, as is standard, a move from negligible to prohibitive is still ruled out. Survives.
- **Local DP.** An ε-LDP protocol is ε-DP centrally for the same neighbouring relation, so the bound transfers unchanged [sure].
- **Allocation or menu output.** By post-processing, any $[0,1]$-valued function of the output (the probability the truck is routed through, the expected payment in a menu) satisfies the same multiplicative bound. Survives.

So the remark is correct, general, and close to a tautology: DP with respect to the household means the output is insensitive to the household. That is its definition.

## C23b. Remark 2 and joint DP as an argument against the cryptographic reply: FAILS

> "Neither is compatible with any useful $\varepsilon$."
> "The large-game condition is the negation of the proposal's premise."

**Wrong privacy goal.** Weak point 3 is correct. Differential privacy protects a data subject from inference by the analyst's audience. In the asthma example the household is a seller posting an ask, and the ask is meant to move the price. No privacy engineer would require DP with respect to the seller's own posted price, any more than an auction designer requires the winning bid to be insensitive to the bids. What the household might want hidden is (i) *why* it bid high (the child's asthma) and (ii) *which* household on the street bid high. Both can be protected while the price moves fully:

- (i) is an attribute-inference question, framed by Pufferfish privacy (Kifer and Machanavajjhala, TODS 2014) [likely]. The secret is the medical condition, not the bid. A high ask is weak evidence of asthma, since households ask high for many reasons (a newborn, a home office, plain dislike of trucks, or simple revenue). Nothing in Krier's mechanism requires the reason to be stated. The posted price is the screening device.
- (ii) is solved by posting each household's ask under a per-street pseudonym backed by an anonymous resident credential (below). Within-street anonymity is then k-anonymity over k households. That is weak for a short street, and I concede the point for streets of two or three houses.

Remark 2 therefore shows that DP cannot coexist with *personalization towards the person protected*. That is true and uninteresting. It does not show that personalized prices require surveillance, or that the cryptographic reply fails.

**Joint DP.** The characterization of Kearns, Pai, Roth and Ullman (ITCS 2014) is accurate [sure, checked]. JDP requires that, for every i, the joint distribution of recommendations to all j ≠ i is DP in i's type. Their result computes approximate correlated equilibria in large games, where each player's action has small effect on others' utilities. Two corrections:

1. In KPRU, JDP is mainly an *incentive tool*: privacy of the mediator gives approximate truthfulness of opting in (the McSherry–Talwar route, FOCS 2007 [sure]). It is not offered as a privacy goal for markets with posted prices. Citing it as "the relaxation used in mechanism design" that "does not help" attacks a tool for a different job.
2. The largeness argument is beside the point. Even without largeness, JDP for the household bounds the truck's price as in Remark 2, as the article itself says in the preceding sentence. Largeness matters to KPRU's *equilibrium* result, not to the privacy bound. And "the negation of the proposal's premise" overreaches. Krier's own flagship coalition is "the agents of 10,000 residents" facing a factory, a congestion-type externality that is a large game. The small-number case (one truck, one household) is the non-large case; the many-to-many cases are not.

JDP does help in exactly one example, the emergency, and the article misses it. The labouring woman's own outcome (her toll falls to zero, or a rebate) may depend on her own data under JDP. Only *other* vehicles' outcomes ("yield on this corridor") must be insensitive to her. And the corridor itself is what an ambulance siren already broadcasts: a priority vehicle is on this route now. The article's "announces a medical emergency at its origin" is true of sirens today.

**Narrowing that would save it.** "DP with respect to a party bounds how far prices can track that party's report; so if a price should not reveal *the bid itself*, personalization is bounded." Then drop the conclusion that the cryptographic reply fails. Replace it with the true and narrower claim in C22: a posted personal price discloses the bid, and the bid is correlated with private circumstances.

**What would settle it.** Formalize the secret as the circumstance $c_i$ rather than the report $r_i$. Bound the mutual information between the posted price vector and $c_i$ when households choose asks strategically. That bound is not zero but can be small. This is the open problem the article's last paragraph gestures at, posed in the wrong coordinates.

## C21. "Proofs concern commitments": FAILS (the oracle half holds)

> "Zero-knowledge techniques therefore narrow who reads a record. They leave unchanged what must be sensed, attributed and retained."
> "Linkability becomes a question of who holds the keys that open the commitments, and the essay's own requirement of a court with enforcement power settles that some authority must."

**What holds.** A ZK proof establishes a predicate of committed data, not of the world [sure]. Credentials need issuers, and sensor attestations need sensors: this is the oracle problem. Both sentences in l.386–389 are right.

**What fails.** Anonymous credentials (Chaum 1985; Camenisch–Lysyanskaya, EUROCRYPT 2001 and CL signatures 2002/2004; BBS+) [sure] exist precisely to remove *attribution to a persistent identifier*. Showings are unlinkable to each other and to issuance. Hiding commitments (Pedersen) carry *no* information without the opening. "Retained" records that are perfectly hiding and whose openings sit with the subject are not records of conduct held by others in any useful sense. And the electronic-toll literature shows that enforcement does not need comprehensive sensing:

- **VPriv** (Popa, Balakrishnan and Blumberg, USENIX Security 2009) [likely]. Cars upload anonymized tuples and prove the correct toll by a secure-computation protocol. Enforcement is by random spot checks.
- **PrETP** (Balasch, Rial, Troncoso, Preneel, Verbauwhede and Geuens, USENIX Security 2010) [sure, abstract checked]. The on-board unit computes the fee locally, commits to per-segment fees, and sends the total with a ZK proof of correct computation. Roadside cameras at secret random locations photograph a sample of vehicles. For each sampled (place, time) the driver must open the matching commitment. The provider learns the total and the sampled points, nothing more.
- **Milo** (Meiklejohn, Mowery, Checkoway and Shacham, USENIX Security 2011) [sure, checked]. It closes PrETP's leak that colluding drivers can learn camera locations from spot-check challenges. It uses blind identity-based encryption, so the toll operator learns only the segments it spot-checked.

Note the trust model. None of these needs a tamper-resistant OBU. Cheating is deterred by spot-check probability times penalty (Becker). The article's "there must be tamper-resistant sensors whose attestations cover the street" is wrong: the sensors need to cover a random sample, at locations the driver cannot predict.

**Court access does not force authority key custody.** Openings held by the subject can be compelled the way personal papers are compelled today: by order and contempt, case by case, with notice to the subject. And anonymity can be revoked by *the protocol*, not by an authority, on provable misconduct. Compact e-cash reveals the identity of a double-spender automatically (Camenisch, Hohenberger and Lysyanskaya, EUROCRYPT 2005) [sure]. Blacklistable anonymous credentials allow blocking misbehaving anonymous users without any trusted third party (BLAC, Tsang, Au, Kapadia and Smith, CCS 2007) [likely]. Where a trustee is wanted, threshold group-signature openers distribute it. None of these lets any party "join the records attached to one identifier across contexts" for a compliant person.

### The strongest architecture for the article's examples

**A. Asthma street (vehicle pays a household-specific entry fee).**

1. *Residency.* A land or utility registry issues each resident household a CL/BBS+ credential, "resident of segment s", by blind issuance. The issuer knows who lives where, which it already knows today.
2. *Asks.* Each household posts an ask schedule (vehicle class × hour) to a public bulletin board under a scope-exclusive pseudonym for segment s. A domain-specific pseudonym, or a Semaphore-style nullifier = H(secret, s), proves one ask per resident household and is unlinkable across segments. No medical credential is needed: the ask is the signal. Optionally a ZK range proof shows the ask is under a cap set by the segment's rules.
3. *Street price.* The segment's price is a public function of the asks (sum, or clearing rule). It can be computed openly or in MPC if only the aggregate should be public.
4. *Vehicle side.* A PrETP/Milo OBU logs position locally and commits to per-segment fees. It pays the segment's escrow pot periodically in batched totals via anonymous e-cash or a shielded pool (Zerocash, Ben-Sasson et al., S&P 2014 [sure]). The ZK proof shows the total equals the sum of committed per-segment fees.
5. *Residents' payout.* Each household withdraws its share from the segment pot by proving resident-of-s with a fresh unlinkable showing and a per-period nullifier to prevent double withdrawal.
6. *Enforcement.* Random spot checks by segment-owned or operator cameras at unpredictable points (Milo-style). Victim-side sensing is an alternative: a resident's own roadside air or ANPR sensor challenges a passing plate, which must answer with a commitment opening.
7. *Disputes.* The challenged party opens the one relevant commitment to an arbiter. If it refuses or fails, a deposit is forfeit. Escalation to identity uses an identity escrow encrypted to a k-of-n trustee set, with an opening rule fixed in the credential issuance policy (Camenisch–Lysyanskaya identity escrow, 1998 [likely]).

**B. Emergency corridor.**

1. Triage by the dispatcher or a midwife issues a short-lived, route-bound blind-signed priority token, as dispatch triage authorizes an ambulance today.
2. The token-holder's car presents it per segment and pays zero. Under JDP this is her own outcome.
3. Other vehicles receive a "yield on corridor R until t" broadcast, which reveals what a siren reveals.
4. Abuse is deterred because the issuer, which knows the caller as dispatch does today, can be audited afterwards. The token can also carry an escrowed identity that opens on a complaint.

**C. Sugar and insurer.**

1. The customer's own agent sees the customer's purchases.
2. Retailers sign receipts (the oracle).
3. The agent proves in ZK a predicate over the period, for example "sugared-drink spend < £x", and the insurer learns that bit.
4. *Here the cryptography stops.* A proof over the receipts the user presents proves nothing about the receipts withheld, and a cash purchase or a friend's purchase escapes entirely. Proving a negative needs a complete log the user cannot omit from. So every retailer must record, at checkout, something bound to the user's hidden tag, a per-purchase commitment the user must include, with retailer-side spot checks matching PrETP's cameras. That is sensing of every purchase by parties the person does not control, attributed to a hidden but stable tag.
5. And the insurer's real contingency, diet and health, is not purchase at all. It is unverifiable short of bodily sensing.
6. The alternative is Krier's literal wording, in which the agent commits to "disincentivize high-sugar purchases". Verifying that is TEE remote attestation of a narrow nudge module. It reveals the module and not the profile, but trusts the TEE vendor, and SGX's attack record is long [sure].

### Against the four conditions, and "devices or parties that the person does not control"

| | A. Asthma street | B. Emergency | C. Sugar/insurer |
|---|---|---|---|
| Sensing | Sparse. The OBU is in the driver's car but runs certified firmware, so the driver controls its data but not its code. Spot-check cameras are others' devices but see a random sample. Condition met only if "recorded as they occur" means "some events, sampled". | Dispatch triage (as today). | Met: complete purchase logging by retailers is required for any negative predicate. |
| Attribution | Not met for compliant drivers or residents. Unlinkable showings; persistent identity only at a spot check (the plate photo) or on failure. | Issuer only. | Met with a hidden tag; the insurer sees only predicate bits. |
| Retention | Commitments retained (perfectly hiding); spot-check photos for the audit window. | Token audit trail at the issuer. | Retailer commitments and receipts. |
| Linkability | Not met. No party can join across contexts without the subject's openings, provable misconduct, or a k-of-n trustee quorum acting under a fixed rule. | Not met. | Not met across contexts; within the insurer contract the bit stream is linked by design. |

**What still leaks, and to whom.**

- *Asthma street.* The segment price and each pseudonymous ask go to the public. The fact of residency goes to the registry. Spot-check samples go to the operator, and with Milo the operator learns only its own samples. Total monthly toll goes to the payment issuer. Network metadata leaks if payments are not batched or mixed.
- *Sugar.* The predicate bits go to the insurer, and with them the unravelling pressure of Grossman–Milgrom, which no cryptography touches.
- *Trust assumptions.* Credential issuers do not collude with spot-checkers. TEEs where used. The trustee quorum. The integrity of the random spot-check locations.

The architecture meets the clause "devices or parties the person does not control" only sparsely in A and B. It meets the clause substantively in C, and C is where the article's argument really bites.

**Narrowing that would save C21.** "ZK and anonymous credentials remove attribution and linkage for compliant parties, and spot checks reduce sensing to a random sample. They do not remove (a) the need for trusted issuers and sensors (the oracle), (b) complete third-party logging when a contract conditions on the *absence* of conduct the subject could hide, or (c) disclosure of the contracted predicate itself." Point (b) is the article's best technical point and appears nowhere in it.

## C22. Prices disclose: HOLDS WITH NARROWING

> "An observer who sees the fee before and after one household arrives learns that household's reservation price by subtraction."
> "At that resolution the price vector is a public encoding of the preferences."

**Differencing.** Fair for any *deterministic, exact* aggregate [sure]; it is the textbook motivating attack. It reveals the *ask*, which the household chose to post. Under the pseudonymous-ask design it is posted openly anyway, so differencing adds nothing. What matters is inference from the ask to the circumstance (see C23b).

**Dinur–Nissim.** The appeal is loose [sure]. Dinur and Nissim (PODS 2003) consider an n-bit database and *subset-sum queries over subsets the adversary chooses*. They show that error o(√n) allows reconstruction of almost all bits with polynomially many queries, and error o(n) with exponentially many. Street prices give one linear functional per segment per time slot, over a fixed set of households the querier does not choose. Varying subsets arise only through churn or overlapping segment memberships. And the "query answers" are asks chosen by the subjects, not noisy answers about fixed sensitive bits. A Dinur–Nissim-style linear system can arise if one household's ask enters several overlapping segment prices, but then the household's per-segment asks are posted separately anyway. The citation adds rhetorical weight without fitting the query model.

**"Public encoding of the preferences."** Right if each household posts many fine-grained contingent asks (Krier's "loud music on a Saturday, but not on a Sunday"). The ask schedule then *is* a revealed-preference profile, pseudonymous per segment. That is the true claim: hyper-granular asks disclose hyper-granular preferences to whoever reads the bulletin board, linkable within a segment pseudonym, and Narayanan–Shmatikov-style re-identification of a segment pseudonym from public geography is easy on short streets.

**Narrowing.** "Personal posted prices disclose the posted ask, by design. With per-context pseudonyms they are linkable within a context and not across contexts. Within a context of few households they are effectively identified." Drop Dinur–Nissim, or cite it only for the case of overlapping aggregates.

**What would settle it.** The simulation the article lists as an open question, but measuring re-identification of segment pseudonyms and inference of circumstances from realistic ask distributions, not reconstruction of asks.

## C24. Continual release: HOLDS WITH NARROWING

> "A governance system that reprices every externality within seconds, indefinitely, must either spend an unbounded privacy budget or add noise that grows until the prices no longer track the conditions."

**Composition is charged per access to new private data, not per output.** Repricing from an unchanged report is post-processing and free [sure]. Releasing a stream that changes only when a household's state changes costs budget per *change*. With the sparse vector / AboveThreshold technique, cost scales with the number of threshold crossings, not with queries (Dwork and Roth 2014, ch. 3) [sure].

Continual-release results [sure for DNPR and Chan–Shi–Song; likely for the user-level statement]:

- Dwork, Naor, Pitassi and Rothblum (STOC 2010), and independently Chan, Shi and Song (ICALP 2010 / TISSEC 2011), give counters over T steps with error O(log^{1.5} T / ε) under **event-level** privacy.
- Under **user-level** privacy, where a household contributes at many steps, error grows with the number of contributions per user.
- The article's characterization of DNPR is accurate.

**What this means here.** A truck trip is a fresh event and suits event-level DP for aggregate traffic statistics. A household's preference is a slowly changing state: budget is spent per preference change, which is modest. The claim "reprices within seconds ⇒ unbounded budget" is wrong as stated. The claim "a household whose preferences change often and are released each time accumulates loss linearly (basic) or as √k (advanced) in the number of changes" is right. All of this is moot if, per C23b, DP with respect to the ask is not the goal.

**Narrowing.** Replace "reprices every externality within seconds" with "re-reads fresh private data at every repricing". The budget scales with the information consumed, not the price-update frequency.

## C4. Payments as a trace: FAILS

> "A micro-payment from a vehicle's agent to a resident's agent, timestamped, tells the resident that the vehicle passed and tells the vehicle's payment provider where it went."

- *Payment provider learns the route.* Removed by anonymous e-cash (Chaum, CRYPTO 1982 [sure]), compact e-cash with automatic double-spender identification [sure], shielded pools [sure], or GNU Taler, in which the payer is anonymous and the payee identified for tax [sure]. The provider sees withdrawals, not spends.
- *Resident learns a vehicle passed.* It saw the truck. With per-segment pots and batched payment the resident learns only the pot total.
- *Dispute resolution survives* by selective opening of one transaction to an arbiter, or by escrow released on a ZK proof of a condition.
- *Reputation survives* by within-context pseudonyms or anonymous reputation tokens (below, C8).
- *What remains.* Timing and network metadata unless batched or mixed. And the legal obstacle (AML/KYC, FATF travel rule), which is a policy constraint, not a technical one.
- "A ledger of a million background transfers per person per day is a trace" is true only of a ledger designed to be one.

**Narrowing that would save it.** "Payments are a trace unless the payment layer is anonymous e-cash or a shielded pool, which current AML regimes resist." This is a political-economy claim and should be argued as one.

## C8. One person, one identity: HOLDS WITH NARROWING

> "Each of these requires that one person correspond to one persistent identity. Douceur (2002) showed that without a logically central authority that certifies the correspondence between entities and identities, a participant can always present many identities."

**Douceur** (IPTPS 2002) is characterized accurately [sure]. Without a logically centralized certifying authority, Sybil attacks are always possible except under unrealistic assumptions of resource parity and coordination.

So a certifier, or a decentralized substitute, is needed:

- pseudonym parties (Ford and Strauss, 2008) [likely];
- social-graph schemes (BrightID-type) [likely];
- biometric uniqueness with ZK nullifiers (World ID on Semaphore) [likely].

**"Persistent" and "linked history" do not follow.** One blind issuance suffices. After it, scope-exclusive pseudonyms give one identity per context, unlinkable across contexts. Equal votes, coalition headcounts and per-head vouchers all need only one-per-context uniqueness plus a membership proof.

**Friedman and Resnick undercut the article directly** [sure, checked]. The article cites "The social cost of cheap pseudonyms" for the claim that cheap identities defeat reputation. The same paper proposes "once-in-a-lifetime identifiers": one per person per social arena, issued by an intermediary that guarantees uniqueness. It also shows by blind signatures that "no one, not even the intermediary, can tell that the identifier belongs to A". This is the cryptographic fix, in the article's own source.

**Reputation.** Within-context reputation needs within-context linkage; the article is right that a reputation must join to earlier conduct *in that arena*. Cross-context reputation can be carried by anonymous reputation proofs. Negative reputation, which users would discard, is the hard case. It is handled by blacklistable credentials (BLAC, PEREA [likely]) or by mandatory accumulator state.

**Residency.** "attested against the same identifier that carries the person's reputation" is false under multi-show credentials: residency and reputation can be different unlinkable credentials.

**Narayanan–Shmatikov.** Accurate [sure], but it applies to a linked pseudonymous history. A design with per-context pseudonyms has only short, context-local traces. These remain vulnerable on small contexts (C22) but are not a "full transaction history".

**Narrowing.** "One-person-one-identity requires a uniqueness issuer, or a decentralized proof of personhood, at enrolment, and linkage within each context of reputation. It does not require cross-context linkage." The surveillance condition "attribution to a persistent identifier unique to the person" then fails, unless the definition counts context-scoped pseudonyms. If it does, every forum account is surveillance.

## C10. Auditing a delegated vote: HOLDS WITH NARROWING

> "Auditing the vote then means auditing the model against the person."

True for a *third-party* fidelity audit: comparison needs both sides. But fidelity can be verified by the principal, with no third party seeing both. The verifiable-voting analogue is the Benaloh challenge (cast-as-intended auditing, Benaloh 2006/2007 [sure]): the voter challenges the device at random, and the device cannot tell a challenge from a real cast. A principal can likewise pose random "how would you vote on X?" probes to its own agent. The agent or provider cannot tell probes from live decisions, so systematic infidelity is caught with high probability. Public legitimacy follows statistically if enough principals probe, as it does for Benaloh challenges.

**Narrowing.** "Fidelity can be audited only by the principal or by someone who sees both. System-wide legitimacy then rests on individual verification, which many principals will not do." That is a real weakness, but it is a weakness of turnout in individual verifiability, not of surveillance.

## C11. Vote selling across modes: HOLDS WITH NARROWING

> "An agent that can make verifiable commitments in the economic mode can also prove how it will vote in the democratic mode, and can sell that vote. Keeping the modes apart requires detecting side payments … That detection requires inspecting the payments."

**First half holds, and more strongly than stated.** Benaloh–Tuinstra (STOC 1994) is accurately characterized [sure]. But the sharper literature concerns trusted hardware:

- *Dark DAOs* (Daian, Kell, Miers and Juels, IC3 2018) [sure] show that TEEs let a voter prove, and bind, how a key will be used. This defeats receipt-freeness and enables trustless vote-buying cartels.
- *Complete Knowledge* (Kelkar, Babel, Daian, Austgen, Buterin and Juels, CCS 2024) [sure] formalizes the encumbrance of keys by TEEs and offers proofs of complete knowledge as a countermeasure.
- A remotely attested software agent is the extreme case. It cannot lie to a coercer, whereas coercion resistance (Juels, Catalano and Jakobsson, WPES 2005 [sure]) rests on the voter's ability to give the coercer fake credentials or to revote.

The article should cite these, not only Benaloh–Tuinstra.

**Second half fails.** Payment inspection is not the remedy, and would not work: payment for a vote can move off-system, in cash or in kind. The cryptographic remedies are:

1. *A human-held override credential with revoting and fake credentials (JCJ).* Any agent commitment is then unenforceable, because the buyer cannot verify that the human did not later revote privately. Vote buying fails without inspecting a single payment.
2. *Complete-knowledge proofs* at credential registration, showing the voting key is not encumbered in an enclave.

Both cost something the article could legitimately claim. (1) needs the human, not the agent, to hold final authority over the democratic-mode ballot, plus an untappable registration channel. That caps Krier's "continuous liquid democracy … instantly … constructing preferences". (2) needs trusted hardware assumptions in the other direction.

**Narrowing.** "Fully delegated, attestable agents can sell votes. Preventing this needs either a human-held, unattestable override (limiting delegation) or proofs that voting keys are unencumbered. It does not need payment inspection." This is a genuine incompatibility between full delegation and coercion resistance, and the article undersells it.

## C12. Legality as client-side scanning: HOLDS WITH NARROWING

> "This is client-side scanning in the sense analyzed by Abelson et al. (2024), performed by a system with full context on its subject."

Abelson et al. (J. Cybersecurity 10(1), 2024, tyad020; arXiv 2021) [sure] analyze CSS as on-device matching of content against targets set by a third party, with *reporting* of matches off device. An agent that silently refuses is a content policy (a model refusal), with no information flow off device. Calling it CSS is loose. It becomes CSS when it reports, or when the target list is set and updated by an authority the user cannot inspect. The article's next sentence concedes the configuration choice, so the claim should be stated conditionally. The Abelson et al. warnings about function creep and target-list governance then apply directly, and they are strong.

**Calvano et al.** (AER 2020) [sure]. Supervising algorithmic collusion inspects agents' *pricing behaviour*, which is public output, not principals' data. It does not require surveilling persons.

## C25. Accountability and auditability: HOLDS WITH NARROWING

> "the essay cannot claim both that the record is public enough to deter the powerful and that it is private enough to protect everyone else, without specifying who decides which persons count as powerful. That decision is an access policy, held by an authority."

A disclosure *rule*, not an authority's discretion, can do the work:

- public disclosure for offers above an amount, or by entities of a type, or affecting more than m parties;
- enforced at transaction time in ZK, as in accountable privacy for anonymous payments (Garman, Green and Miers, FC 2016 [likely]), which enforces policy (thresholds, tracing on rule hits) without a trustee choosing;
- auditable private ledgers with ZK-verified aggregate queries (zkLedger, Narula, Vasquez and Virza, NSDI 2018 [likely]).

Krier's billionaire's beach offer is an offer to the public about a public good: it is public by nature, not by authority. "Pattern detection for corruption" over private transactions is harder. MPC or ZK analytics can compute prespecified statistics, but open-ended anomaly detection needs data in the clear. That part of the claim holds.

**Narrowing.** "Rule-triggered disclosure can deliver offer-level accountability without discretionary key custody. Open-ended forensic analytics cannot." The rule is still set constitutionally, which returns to C14/C15, but that is governance of a rule, not custody of keys.

## D2 and weak point 1. The definition: FAILS

> "Sensing: Conduct and circumstances in $D$ are recorded as they occur by devices or parties that the person does not control."
> "We define surveillance by collection because collection is infrastructure and access is policy."

The definition fails its own refutation test from both sides:

- **Read as "some conduct in D is recorded".** Random spot checks satisfy sensing, and existing ANPR, speed cameras, card-payment logs and mobile-network location data already satisfy all four conditions for driving and shopping, for nearly every person. "Total surveillance" then describes the status quo, and the article's differential claim (C27) carries the argument, not the definition.
- **Read as "all conduct in D is recorded".** The PrETP/Milo architecture enforces the street fees without meeting it.
- **Attribution and linkability.** These fail for compliant persons under anonymous credentials and protocol-triggered revocation. The article treats "collection" as one thing, but a perfectly hiding commitment held by a server and opened only by its subject is collection of nothing.
- **"Access is policy."** False of cryptographic access control. Who can read a perfectly hiding commitment is not changeable after the fact by anyone lacking the opening, including a sovereign, absent compulsion of the subject. The Acemoglu non-commitment point applies to *trustee* designs (threshold openers under a court the sovereign controls), which the article correctly flags as an open question in its discussion. It does not apply to subject-held openings or automatic revocation.

**A better definition.** For a domain D, measure surveillance by (a) the information about each person's conduct and circumstances in D available to the *minimal coalition of parties other than the person* that could be lawfully compelled or induced to pool what they hold, and (b) whether the person can avoid that disclosure without forfeiting the entitlements at stake. Call (a) *exposure under collusion* and (b) *compellability*. The first is the standard cryptographic trust-threshold view. The second captures unravelling and coercion.

**Does the conclusion survive under it?** Partly.

- *Exposure under collusion* is low for street pricing and emergencies under the architecture above. The minimal coalition (registry + spot-check operator + trustee quorum) learns little more than today's ANPR network. It is high for contracts that condition on the absence of hideable conduct (sugar), where retailers must log everything against a hidden tag.
- *Compellability* is where the article is right and does not say so. Every fact the regime makes provable by its subject is a fact the subject can be priced into proving (Grossman–Milgrom–Peppet [sure]) or coerced into proving. And no cryptographic design can let a person prove X to a counterparty while preventing them from proving X to a coercer, except by making X unprovable (receipt-freeness), which takes X out of contract.

So the trade-off that survives is between *contractibility* and *coercion resistance*, not between enforcement and collection. The article's own escape condition, a floor of "deliberately unverifiable" facts enforced "as the secret ballot is", is precisely this.

## Weak point 11. Citation characterizations

| Paper | Article's sentence (gist) | Verdict |
|---|---|---|
| Dinur–Nissim 2003 | Sufficiently many accurate statistics allow reconstruction | Accurate as a summary; loose as applied (needs adversarially chosen subset-sum queries, error o(√n)) [sure] |
| Dwork–McSherry–Nissim–Smith 2006 | Output changes by at most e^ε when one input changes | Accurate (they say "ε-indistinguishable"; the name "differential privacy" is Dwork, ICALP 2006) [sure] |
| Dwork–Naor–Pitassi–Rothblum 2010 | Running count, continual release, polylog error | Accurate (event-level) [sure] |
| Kearns–Pai–Roth–Ullman 2014 | Correlated equilibrium under joint DP in large games | Accurate. Omits that JDP is an incentive device there, and that it is (ε, δ) [sure] |
| Dodis–Halevi–Rabin 2000 | Cryptographic mediator replaces trusted one for correlated equilibrium | Accurate; loose on scope: two players, computationally bounded, needs punishment for aborts [sure] |
| Douceur 2002 | Without logically central certifier, many identities possible | Accurate [sure] |
| Friedman–Resnick 2001 | Cheap identities defeat reputation; newcomers distrusted | Accurate but misleading by omission: the paper proposes once-in-a-lifetime pseudonyms via blind signatures, the very fix [sure, checked] |
| Narayanan–Shmatikov 2008 | Sparse traces re-identify with little side information | Accurate (Netflix Prize / IMDb) [sure] |
| Benaloh–Tuinstra 1994 | Receipt-freeness: voter cannot prove the vote; purpose is to defeat vote buying | Accurate [sure] |
| Tennenholtz 2004 | Program equilibrium; programs read each other's source | Accurate [sure] |
| Bagwell 1995 | In pure strategies, value of commitment vanishes under slightly noisy observation | Accurate; van Damme–Hurkens (1997) show mixed equilibria restore it, which the article's "in pure strategies" hedges [likely] |
| Abelson et al. 2024 | Agent legality checking is CSS in their sense | Loose: CSS in their sense involves third-party targets and reporting; refusal alone is not CSS [sure] |

## Claims outside my list that I believe are wrong

- **C5 (circumstances must be attested).** In the asthma case the household *sells* an entitlement at a posted ask. Overstating the ask costs it fee income as trucks reroute, so the ask is screened by the buyer's willingness to pay, with no attestation. The resulting distortion is monopoly pricing (a Myerson–Satterthwaite inefficiency), not a demand for verification. Attestation is needed only where compensation is paid *on a report of harm* (the airline case), not where an entitlement is priced.
- **C1 and Remark 1's gloss.** "The record must be produced whether or not the vehicle's operator wants it produced" is false given random spot checks with penalties. PrETP is a working counterexample. Remark 1 constrains what the contract can condition on, not the density of the evidence. A contract measurable with respect to σ can be enforced by sampling σ.
- **C13 (judicial reversibility needs authority-held keys).** Subject-held openings and compulsion by order give courts what they have today with personal papers.

## Where the article misstates Krier

- **The scope of the privacy promise.** The abstract says the proposal "promises its users full privacy". Krier's promise is narrower. Users "should also have complete privacy and control over their 'cognitive profile' developed by the agent", and the ZK/DP remark concerns "ensuring that preferences are communicated and aggregated without revealing sensitive underlying data". He never promises that conduct is unobserved. His own insurer example has the insurer's agent that "looks at your eating habits". Much of the observability section attacks a promise about conduct that Krier does not make. The defensible target is the cognitive-profile promise (C9, C10, C22's ask schedules).
- **Cryptography as "the essay's own defence".** Krier offers ZK and DP as an example ("For example these systems could be built on technologies like zero-knowledge proofs and differential privacy"), after "There are of course important privacy considerations here, but none of these seem fundamentally intractable". The article's "Privacy concerns are acknowledged and assigned to cryptography" and "it is the essay's own defence" overstate a one-sentence aside into a programme. Attacking it at length is fair; calling it his defence is not quite.
- **Bedrock.** Outside my brief, but checked: Krier writes that the state "continues to define and enforce basic property rights, contract law, criminal justice, and constitutional rights - the bedrock rules", and lets "some rules ossify by mutual agreement (basic property rights, contract enforcement)". This bears on D1 and weak point 4.

## The single most damaging objection from this angle

The article's definition measures collection and linkage, and that is exactly what the deployed privacy-preserving enforcement literature removes. PrETP, VPriv and Milo enforce per-segment road charges with on-board computation, hiding commitments and random spot checks. Anonymous credentials with scope-exclusive pseudonyms give one-person-one-vote and residency without cross-context linkage. Compact e-cash and blacklistable credentials revoke anonymity automatically on provable misconduct, with no authority choosing. Friedman and Resnick, cited by the article for the opposite, propose blind-signed once-in-a-lifetime pseudonyms. Under these designs, attribution and linkability fail for compliant persons, and sensing shrinks to a random sample. So "total surveillance" holds only by stipulation, or by a reading of "sensing" that today's ANPR already satisfies.

The cryptography stops in three places the article does not isolate:

1. **Disclosure of the contracted predicate itself**, including posted asks that encode preferences.
2. **Contracts conditioned on the absence of hideable conduct** (sugar), which need complete third-party logging against a hidden tag.
3. **Compellability.** Any fact provable to a counterparty can be priced out of its subject by unravelling, or extracted by a coercer. Attested agents make this worse (Dark DAOs; complete knowledge). No protocol separates "provable to my insurer" from "provable to my coercer" except by making the fact unprovable.

That trade-off, between contractibility and coercion resistance, is the article's real result. It survives the cryptography, and Remark 2 is not needed to make it.
