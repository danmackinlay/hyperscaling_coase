# hyperscaling_coase_surveillance — claims ledger

Written for red-team attackers, 2026-11-19. The article under test is `_plans/hyperscaling_coase_surveillance.qmd` (about 6,800 words), a response to Seb Krier, "Coasean Bargaining at Scale", <https://blog.cosmos-institute.org/p/coasean-bargaining-at-scale>. The article was drafted in one sitting by an AI assistant from Krier's text and the assistant's recall of the literature. Line numbers refer to the `.qmd`.

## Thesis

- **T1.** Six features of Krier's proposal each need an observability capability (sensing of conduct, attestation of circumstances, recorded preference reports, persistent unique identity, inspectable agents, retained linkable records). Together they meet the article's four-condition definition of surveillance (sensing, attribution, retention, linkability), with coverage equal to the contracted domains.
- **T2.** Because the proposal lets the same agents negotiate the rules (which matters are contractible, the baseline entitlements), no domain is exempt by a rule the negotiators cannot change, so the surveillance is *total*; and it is costly to reverse, so it is a *commitment*.
- **T3.** Zero-knowledge proofs and differential privacy do not rescue the proposal's privacy promise: ZK narrows readership but not collection, and differential privacy bounds the personalization of prices (Remark 2).
- **T4.** Granular coverage, automatic enforcement and privacy form a trade-off in which any two can be had and not all three.

The only formal content is Remark 1 (enforceable contracts are measurable with respect to the enforcer's signal, l.127–130) and Remark 2 (under ε-DP the expected price moves by at most a factor e^ε per person's report, l.423–430). Everything else is argued in prose from cited results.

## Claims

Each: statement; rests on; would be refuted by.

### Definitions (l.74–120)

- **D1.** Krier's essay proposes all three properties of "delegated agent constitutional negotiation" (delegation, enforced exchange, constitutional scope). Rests on the article's paraphrase of Krier (l.38–72). Refuted if Krier's text keeps the baseline and constitutional rights outside what agents renegotiate.
- **D2.** Surveillance is properly defined by collection and linkability, not by readership or publication, because access is policy and collection is infrastructure. Refuted if the definition is satisfied by arrangements nobody would call surveillance, or fails for a person's own agent sensing locally.

### Observability requirements (l.122–315)

- **C1.** Sensing coverage must equal contracting coverage, and records must be produced whether or not the actor wants (Remark 1, l.127–143). Refuted by enforcement schemes that sustain the same contracts with sparse, probabilistic, complaint-driven or self-reported evidence.
- **C2.** Greenwald–Stiglitz externalities arise from hidden action and type, so pricing them by contract means observing those (l.145–151).
- **C3.** By Holmström's informativeness principle, voluntary contracting generates a demand for monitoring with "no interior stopping point" once sensing is cheap (l.153–156).
- **C4.** Payment records are themselves a trace of conduct (l.158–160).
- **C5.** Where the transfer flows to the party reporting a harm, screening by willingness to pay is unavailable, so circumstances must be attested; a Harberger levy instead charges declared vulnerability (l.162–179).
- **C6.** Cheap verifiable disclosure unravels (Grossman, Milgrom, Peppet), so "voluntary" disclosure is not voluntary in equilibrium (l.181–188).
- **C7.** Myerson–Satterthwaite, Mailath–Postlewaite, Rob and Farrell describe the world of ideal agents; the proposal's patches (bargaining club, fading vote weight, Harberger levy, quantified loss of diffuse parties) need recorded attributed reports and standing preference models; the promised efficiency gain is available to the degree that agents' preference models are attestable (l.190–228).
- **C8.** Equal votes, instant coalitions and reputation need one persistent, centrally certified identity per person with linked history (Douceur, Friedman–Resnick, Narayanan–Shmatikov) (l.230–248).
- **C9.** Credible conditional commitment needs observability of the agent's policy (Bagwell, Tennenholtz, Critch et al.), and the policy is a compression of the principal, so verifying the agent discloses the person (l.250–260).
- **C10.** Auditing a delegated continuous vote means auditing the agent's model against the person (l.262–268).
- **C11.** Agents that can make verifiable commitments can sell votes; keeping the economic and democratic modes apart requires inspecting inter-agent payments (Benaloh–Tuinstra) (l.270–276).
- **C12.** Competition supervision (Calvano et al.) and the legal boundary on agents (client-side scanning, Abelson et al.) each require examining agent behaviour at scale (l.278–286).
- **C13.** Courts as backstop require retained, attributable records whose privacy is reversible on judicial demand; the "recipe for ruin" duty implies preventive, population-wide monitoring, which is Bostrom's own conclusion from the premise Krier borrows (l.288–300).

### Constitutional closure (l.317–375)

- **C14.** Because the boundary of the contractible is an outcome of the negotiation, sensing infrastructure must be able to reach any domain (l.326–331).
- **C15.** An unobserved domain is a ceded entitlement, so privacy is a baseline allocation like any other and open to renegotiation (l.333–337).
- **C16.** Alienable privacy is sold cheaply: unravelling, wealth effects, data externalities (Choi–Jeon–Kim; Acemoglu et al.; Bergemann–Bonatti–Gan). Repairing the data market by Krier's method needs more monitoring (l.339–349).
- **C17.** Krier's veto-reimbursement rule, applied uniformly, makes a privacy holdout pay those who would profit from disclosure (l.351–355). This is the article's own extension.
- **C18.** Legitimacy of the constitutional settlement requires identity, fidelity and mode-separation checks on the entire population (l.357–360).
- **C19.** Irreversibility: fee income vests; the monitoring layer is the first rule to harden; the sovereign who cannot commit holds final authority over the apparatus (l.362–375).
- **C20.** Krier's state is leaner in rules written and wider in evidentiary reach (l.372–375).

### Cryptographic privacy (l.377–465)

- **C21.** ZK proofs concern commitments, need trusted issuers and tamper-resistant sensors, and leave sensing, attribution and retention unchanged; linkability reduces to key custody, which the court requirement forces on some authority (l.384–394).
- **C22.** Personal, continuously updated prices are accurate statistics of private types; differencing and Dinur–Nissim reconstruction apply; at that resolution "the price vector is a public encoding of the preferences" (l.396–416).
- **C23.** Remark 2 is correct and applies: the asthma and emergency examples are incompatible with any useful ε; joint differential privacy (Kearns et al.) does not help because the large-game condition negates the Coasean premise (l.418–440).
- **C24.** Continuous repricing exhausts the privacy budget or drowns the price in noise (l.442–445).
- **C25.** Krier claims transparency as a benefit, which conflicts with the privacy promise unless an authority decides whose records are open (l.454–465).

### Objections and authorities (l.467–532)

- **C26.** Voluntariness: exit from a provider is not exit from the regime; a subsidized universal agent shows non-enrolment is untenable.
- **C27.** Status quo: present collection is partial and without legal standing; under the proposal the record constitutes rights.
- **C28.** The implication is graded (surveillance coverage ≥ contracting coverage) and weak at small scale.
- **C29.** Symmetric transparency (Brin) is coherent and concedes the argument.
- **C30.** Coase (1960) counts inspection among transaction costs, so zero transaction costs include costless inspection.
- **C31.** Ostrom's design principles include monitoring inside a boundary; the proposal keeps monitoring and removes the boundary.
- **C32.** Hayek praised prices for economy of information; personal prices for every externality lose that economy (also Arrow 1969: one buyer, one seller per externality market).
- **C33.** Scott treated legibility as the precondition of intervention; Krier cites him for a programme of legibility.

### Discussion (l.534–572)

- **C34.** "Any two can be had" among granular coverage, automatic enforcement and privacy, with three named escape conditions.

## Known weak points, least welcome first

1. **The definition may win the argument by itself (D2).** If readership is cryptographically bounded and the sensor is the person's own agent, calling the arrangement "total surveillance" may be a definitional victory. The condition "devices or parties that the person does not control" is doing unexamined work.
2. **The trade-off (T4, C34) is asserted, not proved.** There is no model beyond two one-line remarks, and "implies" in the title is carried by prose.
3. **Remark 2 may be the wrong frame (C22, C23).** A household that posts a price is choosing to disclose a bid, as any seller does; differential privacy protects data subjects from a curator, not a bidder from its own bid. A price need not reveal its reason. Bilateral queries between two agents need no aggregate release.
4. **Constitutional closure may overread Krier (D1, C14, C15).** He retains constitutional rights, contract law and criminal justice as state-enforced bedrock and lets basic rules ossify. Privacy may sit there. "DACN" may be a position he does not hold.
5. **Sparse enforcement (C1).** Random audit with penalties, victim-side sensing, complaint-driven verification and reputation may sustain the contracts without comprehensive recording.
6. **"A term that cannot be verified cannot be enforced" (l.26) is too strong.** Observable-but-unverifiable information can be used through message games and relational contracts; the incomplete-contracts literature the article cites is partly about this.
7. **C3 ignores that monitoring has costs the parties themselves bear**, including their own taste for privacy, multitask distortions and ratchet effects, any of which gives an interior optimum.
8. **No differential comparison.** The regulatory state also needs measurement to tax or inspect. The article never compares the surveillance needed by Krier's regime with that needed by the planner it replaces (C27 only gestures at this).
9. **C7 is conceded in the text as the weakest link.**
10. **C17 and the Bostrom step in C13 are extrapolations** from Krier's text, not things he says.
11. **Citations were characterized from memory.** DOIs were checked to resolve to the intended papers, but the papers were not re-read. Characterizations of Rob (1989), Bagwell (1995), Kearns et al. (2014), Arrow (1969), Mailath–Postlewaite (1990), Friedman–Resnick (2001), Coase's inspection passage and Bostrom (2019) are claims under test.

## Who attacks what

- **Incomplete-contract theorist:** C1, C3, C5, C7, C9, C13, C14, C15, C19, C34; weak points 2, 5, 6, 7, 8.
- **Nozick with a mathematics PhD (partisan for Krier, reads the primary):** D1, D2, C6, C15–C20, C26–C29, C33, the two Remarks as mathematics, the logical form of "implies"; weak points 1, 2, 4, 10.
- **Kenneth Arrow:** C2, C3, C5, C6, C7, C16, C22, C30, C32, C34; the reading of Arrow (1969); weak points 8, 9, 11; reprise check against `_plans/hyperscaling_coase_prior_critiques.md`.
- **Cryptographer in privacy-preserving mechanism design:** D2, C4, C8, C10, C11, C12, C21–C25; weak points 1, 3, 11.
- **Cold reader:** the article alone, no ledger.
