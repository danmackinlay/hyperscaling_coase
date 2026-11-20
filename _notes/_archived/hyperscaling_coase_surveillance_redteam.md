# hyperscaling_coase_surveillance — red-team findings

Collated from five read-only attackers dispatched 2026-11-19 against `hyperscaling_coase_surveillance_claims.md`. All five ran on Opus, at Dan's instruction; there is no model diversity in this round. Roster: an incomplete-contract theorist (IC), Nozick with a mathematics PhD as partisan for Krier (Noz), Kenneth Arrow (Arrow), a cryptographer in privacy-preserving mechanism design (Crypto), and a cold reader given the article alone (Cold). Noz and Arrow were also given `hyperscaling_coase_prior_critiques.md` for the reprise check. Verdicts are the attackers'; the convergence section is the collation. Confidence marks are the attackers' own: [sure], [likely], [unsure]. Full reports are in `hyperscaling_coase_surveillance_critique_{incomplete_contracts,nozick,arrow,cryptographer,cold_reader}.md`. Line numbers refer to the article `.qmd`.

Collator's checks: every quotation of Krier used below was checked against his text as fetched 2026-11-18. The Petel quotation was checked against the prior-critiques file, which records it as verbatim. Arithmetic checked: 27/32 = 0.84; e^0.1 = 1.105; ln 10^4 = 9.2. Not checked by the collator: the attackers' characterizations of papers the article does not cite (PrETP, VPriv, Milo, Kaplow–Shavell, Jackson–Sonnenschein, Segerson, Radner and others). They carry the attackers' marks.

## Verdict table

H = holds, N = holds with narrowing, F = fails, blank = not assessed. Cold gave no formal verdicts; entries are the collator's reading of its prose.

| Claim | IC | Noz | Arrow | Crypto | Cold |
|---|---|---|---|---|---|
| Remark 1 as mathematics | H | H | H (is Radner 1968) | | H |
| Remark 2 as mathematics | | H | | H | H |
| D1 Krier holds the position attacked | misstated | N | misstated | noted | misstated |
| D2 definition of surveillance and of "total" | | N | F for "total" (planner meets it) | F | F for "total" |
| C1 sensing as wide as contracting | N | F at l.143 | F at l.143 | F | F |
| C2 Greenwald–Stiglitz | | | N | | |
| C3 no interior stopping point | F | F | N | | F |
| C4 payments are a trace | | N | | F | |
| C5 pay or attest | F | F | N | F | H |
| C6 unravelling | N | F as voluntariness, H as price | H | H | H |
| C7 preferences | N | | N, last sentence F | | N, l.225 F |
| C8 identity with linked history | | | | N | N |
| C9 commitment needs inspectable policy | F | | | | N |
| C10 fidelity audit | | | H, strengthened | N | |
| C11 vote selling | | | H | N: first half H, remedy F | H |
| C12 collusion, client-side scanning | | | | N | N |
| C13 courts, Bostrom | N | N | | F on key custody | N |
| C14 endogenous boundary | N | N | | | N |
| C15 unobserved domain is ceded | F in general | F in general | | | N |
| C16 privacy sold cheaply | | N | N | | H |
| C17 veto rule on privacy holdouts | F | F | | | flagged |
| C18 legitimacy checks | | N | H | | |
| C19 irreversibility | N | N | N | | N |
| C20 leaner but wider reach | | N | | | |
| C21 ZK leaves collection unchanged | | | | F, oracle half H | H on oracle |
| C22 prices disclose | | N | N, "public" F | N | N |
| C23 Remark 2 defeats the privacy reply | | N | | F | N |
| C24 composition | | | | N | N |
| C25 auditability conflict | | | | N | |
| C26–C29 objections | | N, N, H, H | | | |
| C30 Coase inspection | | | H | | |
| C32 Hayek | | | N | | |
| C33 Scott | | N | | | |
| C34 three-way trade-off | F | F | F | | F |

## Reports, compressed

**IC (Opus).** 1 H, 6 N, 6 F. Remark 1's model takes transfers as t(s) with deterministic s and no messages, so it leaves out messages from informed parties (Moore–Repullo 1988, Maskin–Tirole 1999 [sure]; fragile per Aghion et al. 2012 [sure]), probabilistic verification with sanctions (Becker 1968, Townsend 1979, Mookherjee–Png 1989, Kaplow–Shavell 1994 on self-reporting [sure]), victim-side detection, and relational enforcement (Levin 2003, Baker–Gibbons–Murphy 2002 [sure]). Required sensing then scales with fee/F and dispute frequency, not with contracting coverage. C34 is a tautology under the article's definitions and has a counterexample (self-report plus random audit) otherwise; the real trade-off is privacy against sanction severity, with detection probability at least fee/F_max. Proportionality norms for cent-scale fees might bound F and restore the article's version approximately. C3 fails: informativeness has strict value only under risk aversion; privacy disutility is inside the surplus; Crémer 1995, ratchet effects, Prat 2005 give interior optima [sure]. C5 fails: types are types; VCG, Varian 1994, Crémer–McLean 1988, Ben-Porath–Dekel–Lipman 2014 elicit without attestation [sure]. C7: dichotomy false; Jackson–Sonnenschein 2007 linking gives near-efficiency from attributed report histories without attested models [sure]. C9 conflates correlated equilibrium (no commitment), Bagwell (noisy observation of actions; fails in mixed strategies, van Damme–Hurkens 1997 [sure]) and delegation. C14's strongest form is renegotiation-proofness: a privacy floor survives only if it protects absent parties or makes facts unverifiable. C15 holds only for harms not detectable at the victim, which are pooled-risk externalities created by contracts themselves. C19's best argument is missing: the retained stock of records cannot be uncollected. Krier's bargaining-club incentive claim is false in general and the article lets it pass. Rob (1989) asymptotics [unsure], not re-read.

**Noz (Opus).** 2 H, 10 N, 3 F. Reconstructs the title as premises: only "automatic enforcement of granular contracts needs mass record-keeping over the contracted domains" is a valid implication, and it rests on a premise (records the obligor cannot suppress) that audit, posted tolls and victim-side sensing weaken. "Total" (l.105) holds on the literal definition whenever no rule is entrenched, including when coverage is empty; it cannot tell Krier from any amendable democracy. Bentham's inspection house, cited as the model at l.111, fails the definition's retention condition. Krier keeps "constitutional rights" as state-enforced "bedrock", puts "complete privacy and control" in the innermost layer, and gives baseline revision to "our democratic political systems"; nine ledger claims attack something he does not say. C6 fails as a voluntariness claim on Nozick's account (others acted within their rights) and holds as a price claim; Dye 1985 caveat omitted [sure]. C15 conflates entitlement with enforceability; boundary-crossing harms are evidenced on the victim's side. C17 contradicts C6 (worst-case pricing leaves no pooled cost to raise), overrides Krier's privacy commitment, and has the structure of blackmail. Remark 2 correct; needs nonnegative prices, and Krier's emergency price goes negative. Reprise: Petel (2025) wrote "the more we can enforce, the more we must sense" and his "price what you can, protect what you must" is the article's own repair; uncited.

**Arrow (Opus).** 3 H, 8 N, 1 F. Remark 1 is Radner (1968) and binds every enforced allocation mechanism [sure]; Arrow (1969) already lists exclusion cost as a transaction cost [sure, checked]. London's congestion charge, enforced by number-plate recognition, meets all four surveillance conditions, so "automatic enforcement with privacy" is not delivered by coarse pricing and C34 fails. On conduct the implication does not distinguish Krier from the Pigouvian planner or a complete Arrow–Debreu economy. On individual types it does: the planner needs the distribution, Krier needs each person's. Greenwald–Stiglitz's own remedy is a commodity tax on aggregate sales, where the private contract needs each person's consumption record across vendors [sure on theorem, likely on remedy detail]. C7's l.225 fails: the best bilateral mechanism captures 27/32 of first-best surplus in the uniform case [sure]; thick markets converge (Rustichini–Satterthwaite–Williams 1994 [sure]); only many-party unanimity goes to zero. C22: the full personal price vector is held by whoever clears payments; counterparties see sums, which leak by differencing when few households share the price; "public encoding" should go. The Arrow (1969) thin-market sentence is accurate and misplaced (it is an incentive point). Arrow (1969) also says undifferentiated prices are a cost-driven departure from efficiency, which is Krier's thesis. Additions that strengthen the article: Hirshleifer (1971) effect makes unravelling a welfare loss, not only a privacy loss; Gibbard–Satterthwaite means a faithful agent votes strategically, so a fidelity audit has no sincere benchmark; pricing a norm-governed externality uses up the norm (Gneezy–Rustichini 2000 [sure]), a better irreversibility argument. A fiduciary professional code for agent providers is a large-scale trust-based escape the article ignores. Citations: 7 accurate; Rob, Mailath–Postlewaite, Greenwald–Stiglitz loose; none wrong. Same Petel finding as Noz.

**Crypto (Opus).** 1 H, 7 N, 4 F. PrETP (Balasch et al. 2010 [sure, abstract checked]), VPriv (Popa et al. 2009 [likely]) and Milo (Meiklejohn et al. 2011 [sure, checked]) enforce per-segment road charges with on-vehicle computation, hiding commitments and random spot checks; no tamper-resistant sensors, no full coverage. Anonymous credentials with per-context pseudonyms give one-per-person without cross-context linkage; compact e-cash and blacklistable credentials revoke anonymity on provable misconduct with no authority choosing [sure/likely]. Friedman–Resnick, cited for persistent identity, proposes blind-signed once-in-a-lifetime pseudonyms [sure, checked]. Worked architecture for three examples: asthma street and emergency corridor fail attribution and linkability for compliant parties and meet sensing only as a random sample; the sugar/insurer example meets the conditions substantively, because a contract conditioned on the absence of hideable conduct needs complete third-party logging. Remark 2 correct and general, but DP with respect to a seller's own posted price is the wrong goal; the secrets are the reason for the ask and which household posted it. Joint DP lets the emergency rebate depend on her own data; the corridor broadcast reveals what a siren reveals. "Large-game condition negates the premise" overreaches: Krier's 10,000-resident coalition is a large game. Dinur–Nissim does not fit the query model [sure]. Composition is charged per access to new private data, not per price update [sure]. Vote selling: first half holds and is understated; cite Dark DAOs (Daian et al. 2018 [sure]) and Kelkar et al. 2024 [sure]; the remedy is a human-held override credential with revoting (Juels–Catalano–Jakobsson 2005 [sure]), not payment inspection, and it caps full delegation. Cryptography stops at three places: the contracted predicate is disclosed; contracts on absent hideable conduct need full logging; anything provable to a counterparty is provable to a coercer and priced out by unravelling. Krier's privacy promise covers the "cognitive profile", not conduct.

**Cold reader (Opus), article only.** The title equivocates on "total": the definition is a modal property of exemptions, satisfied by any amendable constitution, and the supported claim is the graded one at l.495. Remark 1 to universal recording ignores audits, costly state verification and claimant evidence. Closure runs on the economic mode alone (l.328) and uses hardening in one direction only (l.366 against l.554). Cross-context linkability is never derived; anonymous credentials are not considered. Remark 2 correct, but "DP may be the wrong privacy target": the household wants its report to move the price, and what it wants hidden is the reason. Six internal inconsistencies quoted, including l.315 "equal to" against l.319 "at least", l.144 against l.22, l.225 against l.227, and l.28 against l.113. Holds: the vote-buying argument ("the most original point in the paper"), unravelling, the oracle point, the joint-DP paragraph, data externalities. Suggests the title "…cannot also promise privacy".

## Convergence

Weighted by independence: a finding counts when two or more attackers reached it without being pointed at it, or when the cold reader reached it alone. Findings that restate one of the ledger's own weak points are marked (WP) and count for less from the briefed attackers; the cold reader had no ledger.

**Finding all five reached.**

1. **Enforcement does not need comprehensive recording (WP5; Cold unprompted).** Random audit with penalties, self-reporting, victim-side detection and messages from informed parties sustain the same contracts with sparse sensing. IC and Crypto each supplied a concrete regime (self-report plus audit; PrETP/Milo). What follows from Remark 1 is that verification *capacity* must reach every contracted domain, not that conduct is recorded as it occurs. *Verdict:* C1 narrows to capacity; l.140 and l.143 fail as written.

**Findings four reached.**

2. **"Total surveillance", as defined, does not carry the title (WP1; Cold unprompted).** Cold, Noz, Arrow, Crypto; IC did not assess the definition and says only that it survives in the weak form "sensable on demand". Cold and Noz: "total" is a property of the rule set and holds for any amendable constitution. Arrow and Crypto: existing number-plate enforcement already meets the four conditions. Noz: the cited panopticon fails them. *Verdict:* D2 fails for "total"; T2 fails as an implication.

3. **The three-way trade-off is definitional or false (WP2).** IC, Noz, Arrow, Cold. IC and Arrow each gave a counterexample to a leg (random audit; the congestion charge). *Verdict:* C34 fails as stated.

4. **"No interior stopping point" does not follow from Holmström (WP7; Cold unprompted).** IC, Noz, Arrow, Cold. All four say the force that pushes the stopping point outward is unravelling and data externalities, not informativeness. *Verdict:* C3 fails as stated; hand its work to C6 and C16.

5. **The article's argument is strongest for insurance and pooled-risk externalities (unprompted).** IC (harms not detectable at the victim), Noz (spillovers that cross no boundary), Crypto (contracts on the absence of hideable conduct), Arrow (the contract needs each person's consumption record across vendors). The sugar example is where every attacker says the surveillance requirement is real. *Verdict:* C15 narrows to this class.

6. **Closure overreads Krier (WP4; Cold unprompted from the article's own summary).** Noz, IC, Arrow, Cold; Crypto noted it. Krier's bedrock, his hardening rules and his democratic mode can each supply a privacy floor. IC supplies the repair: under renegotiation-proofness a floor survives only if it protects parties absent from the negotiation or makes facts unverifiable. *Verdict:* D1 narrows; C14 holds in IC's form only.

7. **"Pay or attest" is a false dichotomy.** IC, Arrow, Crypto, Noz against; Cold for. Truthful mechanisms exist without attestation at the cost of budget balance or individual rationality; a posted ask is screened by the buyer. The emergency case survives (Arrow, IC). *Verdict:* C5 fails as stated; merge into C7.

**Findings three reached.**

8. **Remark 2 is correct and aimed at the wrong secret (WP3; Cold unprompted).** Cold, Crypto, Noz. The household's price is its own disclosure; the secrets are the reason and the identity of the bidder. Disagreement to record: Cold calls the joint-DP paragraph "correct and well made"; Crypto says the large-game point overreaches. *Verdict:* C23 narrows to "a personal price discloses the bid".

9. **l.225 fails: efficiency gains do not depend on attestable preferences outside consent problems.** Arrow, IC, Cold. *Verdict:* C7 holds for the developer and diffuse-loser cases only.

10. **The veto-rule extension fails.** Noz, IC; Cold flagged it. It contradicts C6 and assumes the entitlement in dispute. *Verdict:* C17 fails.

11. **Irreversibility is argued to a lower standard than entailment.** Cold, Noz, IC. Better arguments offered: the retained stock of records (IC); pricing uses up norms (Arrow). *Verdict:* C19 narrows.

**Findings two reached independently.**

12. **Krier's privacy promise covers the cognitive profile, not conduct (unprompted).** Crypto and Arrow, each from Krier's text. The Conduct section contradicts no promise he made.

13. **What is specific to Krier is a linked register of individual types (unprompted).** Arrow and IC. The planner needs conduct sensing too, and needs only the distribution of types. This is the differential comparison the article lacks (WP8), and both say it favours a narrower version of the article.

14. **Cross-context linkability is not derived (Cold unprompted).** Cold and Crypto. Per-context pseudonyms suffice for votes, residency and reputation.

15. **The core thesis is in print.** Noz and Arrow, both from the prior-critiques file (pointed at it by design). Petel (2025): "the more we can enforce, the more we must sense", plus proof of personhood, the Harberger preconditions, and an inalienable privacy floor.

**Single-attacker findings worth keeping.**

- Crypto: the surviving result is a trade-off between contractibility and coercion resistance. Anything provable to a counterparty is provable to a coercer; the only separation is to make the fact unprovable.
- IC: privacy trades against sanction severity; detection probability must be at least fee/F_max.
- IC: Jackson–Sonnenschein linking needs attributed report histories, which moves C7's weight onto identity and linkage.
- Arrow: Gibbard–Satterthwaite leaves a fidelity audit with no sincere benchmark.
- Arrow: Hirshleifer effect, unravelling destroys insurance against one's type.
- Arrow: a licensed fiduciary code for agent providers is a large-scale trust-based escape.
- IC: Krier's bargaining-club incentive claim is false in general.
- Disagreement on C6: Arrow says the known escapes from unravelling (Dye, Jovanovic) do not apply here; IC and Noz say the article should state them.

**What survives.**

Both Remarks as mathematics. The oracle point about zero-knowledge proofs. Unravelling as a claim about prices. The data-externality results. Mailath–Postlewaite applied to the developer. Uniqueness of identity at enrolment. The vote-selling incompatibility between attestable agents and receipt-freeness, which Cold, Crypto and Arrow all say holds (Cold calls it "the most original point in the paper"; Crypto says it is understated). Reachability by courts of any record that exists. The surveillance requirement for insurance-type contracts. Novelty relative to Petel: Remark 2, the differencing argument, the closure argument, and the mechanism-design treatment of preferences.

**What this does to the thesis.**

T1 narrows from recording to verification capacity, plus real requirements on identity and on individual types. T2 fails as an implication; closure survives only in the renegotiation-proofness form. T3 half holds: the oracle point and bid disclosure stand, but cryptography does remove attribution and linkage for compliant parties, and Remark 2 does not defeat the cryptographic reply. T4 fails as stated.

The attackers converge on a narrower and different article, in three compatible parts: (a) what Krier's regime adds over the planner is a linked register of individual circumstances and valuations (Arrow, IC); (b) the cases that need sensing inside a person's own domain are insurance-type contracts on pooled risk (IC, Noz, Crypto, Arrow); (c) making a fact provable to a counterparty makes it extractable by unravelling or coercion, and attestable agents make this worse (Crypto, with Cold and Arrow on vote selling).

**Hygiene, to fix regardless.**

- Krier misattributed: l.187 "the decision still belongs to the individual" paraphrases his smoking paragraph, not the insurer case; l.49 "once the emergency is verified" belongs to his low-traffic-neighbourhood paragraph, and the labour passage says "flags"; l.173 the direction of compensation is the article's inference; l.56 drops his "Ideally"; abstract "full privacy" overstates "complete privacy and control over their 'cognitive profile'"; "the essay's own defence" overstates a one-sentence example; l.144 "no such gaps remain" is the article's attribution; l.69 drops his examples of which rules harden; l.290 his court example is non-payment, not conduct.
- Internal: l.315 "equal to" against l.319 "at least"; l.225 against l.227; l.144 against l.22; l.28 "does not depend on the state being predatory" against l.113.
- Citations: Hart–Moore (1988) and Holmström (1979) do not state the l.26 slogan; Remark 1 should cite Radner (1968) and Arrow (1969) on exclusion; Greenwald–Stiglitz is "constrained" inefficient; Rob's probability also tends to zero; "the Coase theorem assumes" is a later formalization; Dinur–Nissim does not fit; composition overstated; Abelson et al. concerns reporting, not refusal; Friedman–Resnick proposes the fix; Arrow's thin-market sentence belongs in Preferences; Bagwell needs van Damme–Hurkens; Bentham fails the definition.
- Remark 2 needs nonnegative prices stated; Krier's price inverts.
- Uncited: Petel, Ngo, the privacy-preserving tolling literature, Dark DAOs and Kelkar et al.
- Never explained: the political Coase problem, Harberger tax.
- Ledger: line references drifted by two or three lines; no evidence cited in it exists outside the article.
