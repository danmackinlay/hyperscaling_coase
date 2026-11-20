# Red-team: incomplete contracts and enforcement

Critique of `_plans/hyperscaling_coase_surveillance.qmd` against ledger claims C1, C3, C5, C7, C9, C13, C14, C15, C19 and C34, and weak points 2, 5, 6, 7 and 8. Written 2026-11-19 from the article, the ledger and Krier's essay (fetched the same day).
Citation marks: [sure] means I am confident of the result as stated; [likely] means I am confident of its substance but not of every detail; [unsure] means check it before relying on it.
Rob (1989) could not be re-read because the publisher served a captcha.

## Verdict tally

| Item | Verdict |
|---|---|
| Remark 1, as mathematics | HOLDS |
| l.29 "a term that cannot be verified cannot be enforced" (WP6) | FAILS as stated |
| C1 (and WP5) | HOLDS WITH NARROWING |
| C3 (and WP7) | FAILS as stated; holds for insurance-type contracts |
| C5 | FAILS |
| C7 | HOLDS WITH NARROWING |
| C9 | FAILS as stated (the load-bearing step) |
| C13 | HOLDS WITH NARROWING |
| C14 | HOLDS WITH NARROWING |
| C15 | FAILS as a general claim; holds for statistical externalities |
| C19 | HOLDS WITH NARROWING |
| C34 (and WP2) | FAILS as a non-trivial claim |
| WP8 | HOLDS as a weakness; a differential that favours the article is available |

Totals: 1 HOLDS, 6 HOLDS WITH NARROWING, 6 FAILS.

---

## C1, Remark 1, and the l.29 slogan (WP5, WP6)

> "a term that cannot be verified cannot be enforced" (l.29)

> "If two profiles $(a, \theta)$ and $(a', \theta')$ produce the same signal, every enforceable contract pays the same in both. The set of enforceable contracts is the set of transfer rules measurable with respect to $\sigma$." (l.128–129)

> "The record must be produced whether or not the vehicle's operator wants it produced, since otherwise the operator's agent would decline to produce it when a fee is due." (l.140)

> "The sensing must be as wide as the contracting." (l.143)

**Verdict.** Remark 1 HOLDS inside its own model. That model takes transfers to be $t(s)$ with $s = \sigma(a,\theta)$ deterministic and admits no messages, so measurability is true by construction. The l.29 slogan FAILS as stated. C1 HOLDS WITH NARROWING: the narrowing replaces "comprehensive, continuous, involuntary recording" with "a verification capacity that can be deployed on demand or at random over the contracted domain".

**Strongest counter-argument.** Remark 1 leaves out the three standard devices by which contracts economize on verification. Each breaks the step from "contracting coverage" to "recording coverage".

1. *Messages from parties who know more than the court.* With transfers $t(s, m)$, where $m$ are messages from parties who commonly observe $(a,\theta)$, the implementable set is bounded by what the parties know, not by $\sigma$. Moore and Repullo (1988, Econometrica) show that in subgame-perfect implementation almost any social choice function can be implemented when the state is observable to the parties but unverifiable [sure]. Maskin (1999) is the Nash-implementation counterpart [sure]. Maskin and Tirole (1999, REStud) use this to argue that unverifiability alone need not make contracts incomplete [sure]. The counter-literature limits but does not reverse this. Renegotiation and complexity can make message mechanisms worthless (Hart–Moore 1999; Segal 1999, both REStud) [sure], and Aghion, Fudenberg, Holden, Kunimoto and Tercieux (2012, QJE) show that Moore–Repullo mechanisms are not robust to small amounts of private information [sure]. So the article is entitled to say that message games are fragile. It is not entitled to Remark 1's conclusion that the enforceable set equals the $\sigma$-measurable set.
   The truck case fits Moore–Repullo exactly. The resident's own agent observes the truck entering, and the truck knows it entered. The court only has to be able to verify when one side challenges the other.
2. *Probabilistic verification with sanctions.* Becker (1968) [sure]: deterrence requires that the detection probability times the sanction, $pF$, be at least the gain from evasion. For a fee of a few cents, $p$ can be tiny. Townsend (1979) [sure] and Mookherjee and Png (1989, QJE) [sure] show that optimal contracts verify only in some states, and randomly. Kaplow and Shavell (1994, JPE) [sure] show that self-reporting with a reduced sanction, backed by audits, saves enforcement cost. This answers l.140 directly. The operator's agent self-reports the entry and pays, because non-reporting is audited with probability $q$ and penalised. On the equilibrium path the record is produced voluntarily. Involuntary sensing is needed for a fraction $q$ of person-moments, not for all of them. The real constraints are limited liability, proportionality norms, the loss of deterrence from Type I errors (Png 1986; Polinsky and Shavell 2000, JEL survey) [likely], and marginal deterrence. Those constraints bound how small $q$ can be. They do not force $q = 1$.
3. *Victim-side detection.* Physical externalities (fumes, noise, smoke, a cut-through taxi) show up where the victim is, so they can be sensed by the victim's own devices. The injurer is recorded only where its conduct crosses into someone else's domain, which is how witnesses have always worked.
4. *Relational enforcement.* Levin (2003, AER) and Baker, Gibbons and Murphy (2002, QJE) [sure] show self-enforcing contracts on performance that is observable but not verifiable, sustained by the value of future dealings. Delivery fleets and taxi firms are repeat players on a street. The cost is identity for the firm, not for persons.

The citation at l.29 is also off. Hart and Moore (1988) [likely] is a paper about how far observable-but-unverifiable information *can* be used through messages and renegotiation, and where that stops. It does not state the slogan. Holmström (1979) is about informativeness, not verifiability.

**Narrowing that saves C1.** "A contract over conduct in domain $d$ is automatically enforceable only if some verification technology covers $d$ with positive probability, backed by a sanction large enough that $pF$ is at least the gain from evading. Enforcement also needs attribution of sanctions to a legal person." That still requires sensing *capacity* everywhere contracting reaches, which is a real point. Because capacity is infrastructure, part of the article's "collection is infrastructure" argument survives. What goes is "recorded as they occur" and "retained" for every act. The four-condition definition then holds only in the weak form "sensable on demand".

**What would settle it.** A model in which enforcement can use (i) messages, (ii) random audit with a sanction bounded by wealth, and (iii) victim-side signals. Then compute the minimum expected sensing per person-moment needed to sustain a fee schedule of a given granularity. If it scales with granularity, the article wins. If it scales with $1/F$ and with the frequency of disputes, the article loses this step.

## C3: informativeness and "no interior stopping point" (WP7)

> "As sensing becomes cheap, and each person's own agent is already a sensor of that person, the demand for monitoring that emerges from voluntary contracting has no interior stopping point." (l.156)

**Verdict.** FAILS as stated. It holds, narrowed, for insurance-type contracts in which the monitored party is risk averse over large stakes.

**Strongest counter-argument.**

- *Where the strictness comes from.* Holmström's principle [sure] says that an informative signal has strictly positive value because of the trade-off between insurance and incentives under risk aversion. With a risk-neutral injurer and enough liability, the first best is reached without monitoring the action, either through outcome-based liability or through Becker enforcement with arbitrarily small $p$. Once $pF$ exceeds the fee, further monitoring is worth zero, and that is an interior stopping point. Krier's micro-fees are small independent lotteries, over which agents are close to risk neutral (Arrow–Pratt), so the strict-value premise fails exactly where the article applies it most (trucks, taxis, noise).
- *Privacy is inside the surplus.* In a Coasean bargain the monitored party's dislike of being monitored is a cost the bargain internalizes. Monitoring stops where its marginal informational value equals sensing cost plus the monitored party's privacy disutility. Cheap sensing removes only the first of those two terms. To get "no stopping point" the article needs that privacy disutility is not priced or is bid down to zero. That is C6 and C16 (unravelling, data externalities), not informativeness. C3 should hand over to those claims.
- *Commitment not to learn.* Crémer (1995, QJE, "Arm's length relationships") [sure]: a principal can do better with a worse monitoring technology, because knowing less lets it commit to punishments it would otherwise renegotiate away. Ratchet effects (Freixas, Guesnerie and Tirole 1985; Laffont and Tirole 1988) [sure]: when information gathered now is used to tighten terms later, effort and revelation fall, so the parties gain by committing not to observe. Aghion and Tirole (1997, JPE) [sure]: a principal who knows less leaves the agent real authority and gets more initiative. Prat (2005, AER, "The wrong kind of transparency") [sure]: observing actions rather than consequences can lower welfare. Each of these produces an interior optimum, or a corner at low monitoring, even when sensing costs nothing.
- *Multitask cuts both ways.* Holmström and Milgrom (1991) [sure]: when some tasks cannot be measured, the optimal response can be low-powered incentives on all tasks, which is an interior stopping point. It can also be to measure the remaining tasks, which supports the article. The article should not use multitask on either side without a model.

**Narrowing that saves C3.** "In insurance-type relationships, where the monitored party is risk averse over large stakes and the outcome signal is noisy (diet and health premiums), voluntary contracting creates demand for every cheap informative signal, and the remaining stopping point is the monitored party's privacy disutility. Unravelling and data externalities drive that disutility's price down (C6, C16)." The sugar example is the article's strongest case and should carry this claim alone.

**What would settle it.** Show that, in Krier's examples, the monitored parties are risk averse over the relevant stakes, or that commitment-not-to-learn arrangements cannot survive the regime's renegotiability. The second may well be true (see C14), and would be a better argument than informativeness.

## C5: circumstances must be attested when the transfer flows to the reporter

> "When a transfer flows towards the party who reports a harm, an unverified report is an invitation to inflate it, and screening by willingness to pay is unavailable." (l.174)

> "Applied to circumstances, that answer charges people in proportion to their declared vulnerability, so that the family of the asthmatic child pays the largest levy on the street." (l.176)

**Verdict.** FAILS.

**Strongest counter-argument.**

- *Types are types.* In mechanism design, asthma severity is part of $\theta_i$, just as a homeowner's valuation is. The article's split between "circumstances" (which it says need attestation) and "preferences" (for which it grants the escape routes at l.204–208) has no basis in the theory. The ways out it grants for preferences (shared entitlements, subsidised mechanisms) apply equally here.
- *Transfers to the reporter are compatible with truthful reporting.* In VCG and pivot mechanisms the household is paid according to its effect on others, and truthful reporting of harm is a dominant strategy with no verification. The cost is a budget deficit (Green and Laffont 1977/1979) [sure], which is Myerson–Satterthwaite in another form, not attestation. Varian (1994, AER, "A solution to the problem of externalities when agents are well-informed") [sure] uses a two-stage mechanism in which each party names the price the other pays, and so elicits truthful compensation when the parties know each other's types. Crémer and McLean (1988) [sure]: when types are correlated, as asthma-relevant harm on one street plausibly is through shared traffic exposure, lotteries can elicit types at no cost with no verification. Pesendorfer (1998, JET, "Pollution claim settlements under correlated information") [likely] makes this point in Rob's own setting.
- *Ex-post audit, bonding and signalling.* Ben-Porath, Dekel and Lipman (2014, AER) [sure] study optimal allocation when verification is costly and used only sometimes. A claimant who posts a bond forfeited on a failed random audit makes the claim credible, and needs a doctor's examination with probability $q$, not a standing medical registry. The article's own emergency case already concedes ex-post audit (l.181). That is verification when audited, not ex-ante attestation.
- *The Harberger point leaves out the net.* A self-assessed levy that is paired with compensation equal to the claim when harmed is truthful when the levy rate matches the probability of being harmed, as in the logic of Posner and Weyl's self-assessed tax [likely]. The family of the asthmatic child pays the largest levy *and* receives the largest compensation. "Pays the largest levy" without the net transfer is misleading.
- *Inflation produces inefficiency, not breakdown.* If the household's ask is just an ask, inflating it is ordinary bilateral-monopoly markup: some trucks reroute that should not. The demand for attestation comes only from Krier's promise that intensity be "accurately represented and compensated". Truthful mechanisms meet that promise at the cost of a deficit.

**Narrowing that saves C5.** "Making reported circumstances truthful under budget balance, voluntary participation and efficiency requires either verification (ex ante, or ex post with positive probability) or giving up one of those properties." That is C7 applied to circumstances, and it should be merged into C7. The emergency case survives better. In it, speed means the cheap mechanisms (deficit-financed VCG, correlation lotteries) are probably infeasible within seconds, and a false claim is costly, so some fast ex-post verification is genuinely needed. Even so, the requirement is verification on audit, not a registry.

**What would settle it.** Write the asthma street as a mechanism-design problem. Compute the deficit of the efficient dominant-strategy mechanism and compare it with the cost of auditing at rate $q$. If both are small, C5's dichotomy (pay or attest) is false in its own example.

## C7: impossibility results and the "attestable model or strategic agent" dichotomy

> "Both found that the probability of reaching the efficient outcome falls as the number of parties grows, and in the second case it tends to zero." (l.196)

> "If the model can be attested to counterparties, private information is removed and the impossibility theorems lose their force ... If it cannot be attested, the agent is a strategic bargainer with private information and the theorems apply in full." (l.223–224)

**Verdict.** HOLDS WITH NARROWING. The citations are broadly right. The dichotomy is false, but its best replacement still needs records.

**Characterizations.**
- Myerson and Satterthwaite (1983) [sure]: stated correctly. With overlapping supports, no mechanism is Bayesian incentive compatible, interim individually rational, budget balanced and ex-post efficient at once.
- Mailath and Postlewaite (1990, REStud) [sure]: stated correctly. With a unanimity or consent requirement, the probability of provision tends to zero as $n$ grows. The application to the developer who needs every homeowner's consent is exactly right, and is the article's best use of the literature.
- Rob (1989, JET) [likely on the setting, unsure on the asymptotics]: a single plant and many residents with private damages, with an inefficiency from private information. I could not re-read it to confirm that the probability of the efficient outcome falls with $n$. Check this before relying on "Both found".
- Neeman (1999, REStud) [sure on the abstract] shows that whether voluntary bargaining succeeds depends on the structure of property rights, and identifies property-rights structures that are efficient. The article cites Cramton–Gibbons–Klemperer and Segal–Whinston for this point and should add Neeman, which is about public-good externalities rather than partnerships.

**Strongest counter-argument against generalizing beyond consent problems.** The near-impossibility for large $n$ applies to unanimity and public-good problems. Most of Krier's contracts are not that shape. A truck choosing among many streets is in a thick market, and in thick private-good markets the losses from incentive compatibility vanish as $n$ grows (Gresik and Satterthwaite 1989; Rustichini, Satterthwaite and Williams 1994: double-auction inefficiency of order $1/n^2$) [sure]. Competition among streets for traffic disciplines inflated asks without attestation.

**Against the dichotomy.** There are at least three intermediate cases.
- *Partial or hard evidence.* Green and Laffont (1986) [sure], Bull and Watson (2004, 2007) [likely], and Hart, Kremer and Perry (2017, AER, "Evidence games") [sure]: agents can disclose selected verifiable facts without the model as a whole being attestable.
- *Correlated types.* Crémer and McLean (1988) [sure]: correlation lets the mechanism extract truth with no verification. It needs risk neutrality, unbounded transfers and a common prior, and it fails robustness (Bergemann and Morris 2005) [sure].
- *Linking decisions.* Jackson and Sonnenschein (2007, Econometrica, "Overcoming incentive constraints by linking decisions") [sure]: when many independent decisions are linked, each agent's reports are budgeted to match the prior's distribution, and efficiency is approached as the number of decisions grows. Krier's regime of millions of micro-negotiations is the ideal setting for this.

The linking route has a sting for Krier, and the article should take it rather than the dichotomy. Linking needs a history of each agent's reports, attributed across negotiations. That is the "fading vote weight" requirement in general form. It does not need the model to be attestable, and a record of reports discloses much less than an attested model.

**Narrowing that saves C7.** "For consent problems (developers, single plants), efficiency without subsidy or coercion needs verification of types. For thick-market externalities, incentive losses shrink with market size. Across repeated micro-negotiations, near-efficiency needs attributed, linked histories of each agent's reports, not attested preference models." That moves C7's weight onto C8 (identity and linkage), which is a stronger link.

**What would settle it.** Classify Krier's examples by structure (consent, public good, thick-market bilateral, repeated) and assign each the relevant result. My guess: the developer and diffuse-loser cases go to Mailath–Postlewaite and the article; routing and noise go to thick-market results and against it.

## C9: commitment needs inspectable policies

> "Conditional commitments of this kind are valuable only when they can be observed." (l.253)

> "To make the agent's commitments credible to strangers, something about that policy must be verifiable by them or by an attesting third party. What is verified about the agent is thereby disclosed about the person." (l.259–260)

**Verdict.** FAILS as stated. A narrowed version is true but does not support "discloses the person".

**Strongest counter-argument.**
- *Correlated equilibrium needs no commitment.* The passage opens with Krier's correlated-equilibrium framing (l.252). A correlated equilibrium (Aumann 1974, 1987) [sure] is self-enforcing. Each player obeys a private recommendation because obeying is a best response. No commitment is involved, so the observability of commitments is irrelevant to it. The article joins two different mechanisms with "of this kind".
- *Bagwell (1995).* Bagwell [sure] shows that in a Stackelberg game where the follower sees the leader's *action* with noise, the pure-strategy equilibria lose the first-mover advantage. The result is about observing an action, not a contract or an escrow. Even on its own terms it is fragile. van Damme and Hurkens (1997, GEB) [sure] find a mixed-strategy equilibrium that approaches the Stackelberg outcome as the noise vanishes. Maggi (1999, GEB) [likely] shows that commitment value is restored when the leader has private information. The article reports the pure-strategy result as general.
- *The right literature, and what it actually requires.* Delegation as commitment is the relevant body of work. Katz (1991, RAND) [likely]: unobservable delegation contracts generally have no commitment value. Fershtman, Judd and Kalai (1991, IER) [sure]: observable delegation contracts can sustain cooperative outcomes. What must be observed in these models is *the commitment*, meaning the relevant contract term or conditional rule, not the delegate's whole decision function.
- *Bonding and escrow.* A conditional promise ("I pay $x$ if you reroute") is a contract. With escrow, the counterparty needs to verify the escrow terms and the performance (the rerouting), not the agent's policy. That reduces C9 to C1.
- *Repeated play.* Folk theorems with public monitoring (Fudenberg, Levine and Maskin 1994) [sure] sustain cooperation by observing actions, not programs.
- *Program equilibrium.* Tennenholtz (2004) and Critch et al. need source inspection for one-shot games *without* enforceable contracts. In a regime with courts and escrow, that case is residual.

**Narrowing.** "Commitments outside enforceable contract and repeated play, such as one-shot conditional cooperation between strangers, require that the conditional rule be verifiable. Verifying one rule discloses that rule, not the principal's profile." Disclosure of the person then depends on how many such commitments are made, and the article gives no estimate of that.

**What would settle it.** Show that a substantial part of Krier's value comes from one-shot conditional commitments between strangers that cannot be written as escrowed contracts. Without that, C9 should be dropped or folded into C10 and C11. C10 and C11 are stronger, because there the object audited genuinely is the agent's model or its payments.

## C13: courts need retained, attributable records that can be de-anonymized on demand

> "Whatever privacy the protocol gave at the time of the transaction must be reversible on judicial demand, or the court cannot do the job the essay assigns it." (l.293)

**Verdict.** HOLDS WITH NARROWING.

**Strongest counter-argument.** Courts do not need records of everything. They need the evidence that interested parties bring, and burdens of proof decide who must keep what. Dewatripont and Tirole (1999, JPE, "Advocates") [sure] and Shin (1998, RAND) [likely] show that adversarial procedure gets information from interested parties efficiently. Bull and Watson (2004, JET) [likely] model verifiability as the disclosure of hard evidence held by the parties. Hay and Spier (1997, JLS) [likely] show that assigning the burden of proof economizes on evidence costs.

Krier's own court example is "If the delivery truck's agent agrees to the 'clean air fee' but the company refuses to pay". That is a dispute about an agreement and non-payment. It needs a signed acceptance held by the creditor and proof of non-payment. It needs neither sensing of conduct nor linkage across contexts. Disputes about conduct ("did the truck enter?") need evidence of that event, which the claimant keeps because the claimant bears the burden. That is evidence the party chose to retain, produced by discovery, not privacy built into the protocol that can be reversed.

**Narrowing.** "Courts need attributable evidence of agreements and contested events, kept by the parties who bear the burden of proof, and compelled through discovery. Any record that exists can be reached by a court." That last point is the article's real insight and survives intact: the record is reachable because it exists. The narrowed claim drops "the protocol must have a judicial trapdoor".

On the Bostrom step (outside contract theory): the article can do better than extrapolate. Krier writes that "the underlying cognitive infrastructure it creates is part of what a modern state may need to manage them". That is close to an endorsement of using the agent layer for preventive purposes. The article should quote it rather than say only that the essay "does not report" Bostrom's conclusion (l.297).

**What would settle it.** Analyse, for each class of dispute in the regime, who bears the burden and what they must retain. Retention by interested parties, scaled by how often disputes arise, is the real requirement.

## C14 and C15: endogenous contractibility, and "an unobserved domain is a ceded entitlement"

> "By Remark 1, a contract over conduct that the enforcer cannot observe is void in effect. To exempt a domain from sensing is therefore to assign every entitlement in that domain to whoever acts there." (l.332–333)

> "A right to be unobserved in the home is, mechanically, a right to impose unpriced externalities from the home." (l.334)

> "The sensing infrastructure must therefore be able to extend to any domain that the negotiation may open." (l.327)

**Verdict.** C15 FAILS as a general claim, and holds for statistical externalities. C14 HOLDS WITH NARROWING.

**Against C15.**
- *Residual control is not cession.* In Grossman–Hart–Moore [sure], ownership is valuable *because* some contingencies cannot be verified. The owner holds residual control, and others bargain with the owner ex post over what both can observe (Hart–Moore renegotiation). Allocating residual control is the efficient design choice when the owner's non-contractible investment matters most. A privacy domain is an allocation of residual control, which the theory treats as possibly efficient, not as a void to be filled. The article is right that, for conduct nobody but the actor can observe, the actor holds the de facto entitlement. Whether that is a defect depends on whose investment matters, which GHM makes the central question.
- *"Mechanically" is false for physical externalities.* Noise, smoke and fumes cross the boundary and can be detected where they land (see C1, point 3). The home stays unobserved while the harm from it is priced on arrival. The claim holds only for externalities whose harm cannot be detected by the victim. These are statistical or actuarial ones: diet raising pooled insurance cost, behaviour changing risk in a pool. Those are largely fiscal externalities created by pooling, that is, by contracts themselves. The narrowed claim is still interesting: it says the pressure for surveillance comes from risk pools, not from neighbours.

**Against C14's "no stopping point".** Even with zero sensing cost, contract theory gives reasons to leave verifiable matters out of contracts.
- Bernheim and Whinston (1998, AER, "Incomplete contracts and strategic ambiguity") [sure]: when some aspects of a relationship cannot be verified, it can be optimal to leave verifiable aspects unspecified too.
- Spier (1992, RAND) [sure]: proposing a contingent clause signals the proposer's type, so in equilibrium contracts stay incomplete. Proposing to open a domain is such a signal.
- Crémer (1995) and the ratchet literature (see C3) give commitment value to not learning.
- Tirole (1999, Econometrica, "Incomplete contracts: where do we stand?") [sure] reviews the foundations and stresses that incompleteness needs an explicit friction. The frictions just listed survive falling sensing costs.

The article's real argument for no stopping point is unravelling and data externalities (C6, C16), which work against all of these. C14 should rest on them explicitly.

**Where C14 is strong.** The article's point that no rule is beyond change by the negotiators has an exact contract-theory counterpart. Any rule the current parties all prefer to change will be renegotiated (Hart–Moore 1988; Maskin–Moore 1999, REStud, "Implementation and renegotiation") [sure]. A privacy floor can hold only if it protects parties who are absent from the negotiation, or if it makes the facts technically unverifiable. The article's secret-ballot remedy (l.553) is correct: it is the standard way to commit against renegotiation by destroying the information. This is the strongest version of the closure argument and should be stated in these terms.

**Narrowing.** C15: "For externalities whose harm cannot be detected at the victim (actuarial and pooled-risk externalities), an unobserved domain leaves the entitlement with the actor." C14: "Under renegotiation-proofness, no privacy floor survives except one enforced by making facts unverifiable. Whether the endogenous boundary sits at total coverage depends on whether unravelling and data externalities outweigh strategic ambiguity, signalling and commitment-not-to-learn."

**What would settle it.** For C15, sort Krier's examples into externalities detectable at the victim and ones that are not. For C14, a model of endogenous contractibility in which unravelling (C6) and data externalities (C16) are set against Spier and Bernheim–Whinston forces.

## C19: irreversibility

> "Monitoring becomes a vested interest of the monitored." (l.364)

> "The monitoring layer is therefore the first thing to become fixed and the last that could be reopened." (l.368)

**Verdict.** HOLDS WITH NARROWING.

**Strongest counter-argument.** Fee income is a transfer. Removing sensors hurts the recipients and helps the payers by the same amount. Under efficient renegotiation, monitoring is removed whenever that raises joint surplus, so vesting by itself creates no irreversibility. Persistence needs a political-economy friction. Candidates: Coate and Morris (1999, AER, "Policy persistence"), where policies induce specific investments that create constituencies [sure]; Fernández and Rodrik (1991, AER), status-quo bias from uncertainty about who gains [sure]; and the Olson asymmetry between concentrated and diffuse interests. Hold-up on sunk sensor investment is a weaker version. "First thing to become fixed" is an entailment (hardened, automatically enforced rules presuppose their sensing) and holds as complementarity. It does not show that sensing hardens *before* the rules.

The article misses the strongest irreversibility argument. The *stock* of retained records cannot be uncollected. Withdrawing the sensors ends the flow but not the archive, and the archive's option value to a sovereign who cannot commit (Acemoglu 2003, correctly cited) [sure] stays.

**Narrowing.** Rest irreversibility on (i) the persistence of the retained stock, (ii) Coate–Morris-style specific investment by recipients, and (iii) the sovereign's lack of commitment. Drop the suggestion that vesting alone does it.

**What would settle it.** Identify the asymmetry between the political power of recipients and payers in Krier's examples. Households on a street against national logistics firms is not obviously concentrated against diffuse in the direction the article needs.

## C34: the trilemma (WP2)

> "Any two can be had." (l.545)

> "Automatic enforcement with privacy requires coarse, aggregate instruments, which is the congestion charge and the uniform rule." (l.547)

**Verdict.** FAILS as a non-trivial claim. Under the article's definitions it is a tautology. Under definitions that allow probabilistic and message-based enforcement, a regime with all three properties exists.

**Formal statement under the article's definitions.** Let domains be $d \in \mathcal D$. *Automatic enforcement*: transfers are measurable with respect to $\sigma$. *Privacy*: there is a $d_0$ on which $\sigma$ does not vary with $(a_{d_0}, \theta_{d_0})$. *Granular coverage*: every $d$, including $d_0$, admits a transfer rule that varies with $(a_d, \theta_d)$. By Remark 1 the three are inconsistent. That is Remark 1 restated, and it holds only because "automatic" has been defined as "$\sigma$-measurable with deterministic $\sigma$" and "privacy" as "$\sigma$ constant on a domain".

**Counterexample regime.** Self-reporting with random audit (Kaplow and Shavell 1994) [sure], together with victim-side detection.
- *Granular*: any externality can be the subject of a fee.
- *Automatic*: settlement follows from the self-report, and audits follow a fixed random rule without discretion.
- *Privacy*: each person-moment is sensed with probability $q$, which can be close to 0 when the sanction is large (Becker) [sure]. Home interiors are never sensed for externalities that land elsewhere.

The binary definition of privacy (domains "not sensed") excludes this regime only because every domain is audited with positive probability. Once privacy is measured as the probability of being sensed, the trilemma becomes a trade-off between privacy and **sanction severity, limited liability and error costs**. That fourth variable is absent from the article. "Automatic enforcement with privacy requires coarse, aggregate instruments" is false: random audit is both automatic and granular.

**Narrowing that saves C34.** "With sanctions bounded by limited liability or proportionality, and for externalities not detectable at the victim, granular automatic enforcement requires a detection probability at least fee/$F_{\max}$ in every contracted domain. Privacy, measured as the probability of not being sensed, is then bounded by $1 - \text{fee}/F_{\max}$ domain by domain." That is a non-trivial and checkable statement. The article's three-way version is its limit when $F_{\max}$ is close to the fee, for example under strong proportionality norms for micro-fees. Proportionality may well hold for a regime of cent-scale fees, and arguing that it does would rescue much of C34.

**What would settle it.** Whether a polity running Krier's regime would accept $F/\text{fee}$ ratios of $10^3$ to $10^6$. If not, $q$ cannot be small and the article's trilemma returns in approximate form.

## WP8: no differential comparison

**Verdict.** HOLDS as a weakness, and the comparison can be made in the article's favour. A Pigouvian planner needs measurement of the injurer's activity, often through coarse proxies such as input taxes and two-part instruments (Fullerton and Wolverton) [likely], and *population-level* estimates of harm. It needs no individual victim types. Krier's regime needs injurer-side sensing at a finer grain *plus* individual victim types (circumstances, preferences) and their identity bindings. The differential is therefore concentrated on the victim side (C5, C7, C8) and on grain. That is a sharper thesis than "total surveillance" and should be stated.

---

## Claims outside my list that I believe are wrong

- **C6 (unravelling).** The Grossman–Milgrom result requires that disclosure be costless and that the sender be known to hold the information. With uncertainty about whether the sender is informed (Dye 1985; Jung and Kwon 1988) [sure], or with disclosure costs (Verrecchia 1983) [sure], unravelling is partial. "Silence is priced as the worst case" (l.475) is too strong. The correct version is "silence is priced below average".
- **C17 (veto reimbursement against privacy holdouts).** Krier's reimbursement compensates diffuse losers from a blocked *project*, relative to a baseline in which the project could proceed. Extending it to a privacy holdout assumes that neighbours hold an entitlement to the fee income from sensing. That entitlement is the conclusion under dispute. Under a baseline in which privacy is the default, nobody loses anything, so there is nothing to reimburse. The extension assumes what it was meant to show.
- **Krier's bargaining club, which the article accepts without comment (l.60).** Krier claims that "padding your number doesn't boost your check" because "the payout is at the common clearing price". If the common price must clear every member's minimum, the member with the highest minimum sets the price and gains by padding up to the point where the deal dies. That is the pivotal-agent incentive behind Mailath–Postlewaite. Krier's incentive-compatibility claim is false in general [sure, by Myerson–Satterthwaite and Mailath–Postlewaite]. The article's C7 would be stronger if it said so, since it shows that Krier's own patch fails without the verifiable reports the article says are needed.

## Places the article misstates Krier

- **Constitutional scope (D1, l.85–89).** The article says "The same agents negotiate the rules of the exchange: the baseline assignment of entitlements". Krier says baselines start from "centuries of jurisprudence" and that "To the extent that these need to change or adapt, our democratic political systems are the right mechanism to do so". He says agents "only make it explicit, contestable, and cheap to renegotiate", and that the state "continues to define and enforce basic property rights, contract law, criminal justice, and constitutional rights - the bedrock rules". Agents improve the democratic process; they are not the negotiators of the constitution. This is weak point 4, and it matters for C14: Krier places the exempting rule outside agent bargaining, though not outside democratic change.
- **Which rules harden (l.69).** The article says "Which rules stay fixed and which stay open is itself priced and settled by mutual agreement". Krier names the hardened rules: "letting some rules ossify by mutual agreement (basic property rights, contract enforcement) while others remain perpetually negotiable (noise ordinances, parking rules)". The paraphrase is fair but drops the examples, which put the core rules on the fixed side.
- **Enforcement (l.56).** Krier hedges: "*Ideally* the agent system transforms enforcement from a costly legal battle into a near-instantaneous computational verification." This is minor, but the "ideally" matters for C1.
- **Courts (l.290–293).** Krier's only example of what courts do is the case where the truck's agent "agrees to the 'clean air fee' but the company refuses to pay". That is a dispute over agreement and payment, not over conduct (see C13). The article generalizes it to evidence of everything sensed.
- **In the article's favour on Bostrom (l.297).** Krier writes that "the underlying cognitive infrastructure it creates is part of what a modern state may need to manage them". The article understates how close Krier comes to the preventive use.

## Single most damaging objection

The first half of the article rests on Remark 1, and Remark 1's model of enforcement leaves out the three devices by which contract and enforcement theory economize on information. The first is messages from parties who observe more than the enforcer (Moore–Repullo; Maskin–Tirole). The second is probabilistic verification with sanctions (Becker; Townsend; Mookherjee–Png; Kaplow–Shavell self-reporting). The third is detection at the victim. With these included, the required expected sensing scales with $\text{fee}/F$ and with how often disputes occur, not with how far contracting reaches. "Recorded as they occur ... whether or not the operator wants" (l.140) and "the sensing must be as wide as the contracting" (l.143) do not follow. The trilemma (C34) turns out to be a restatement of the article's own definitions, and the real trade-off is between privacy and sanction severity.

What survives is substantial but different:
1. sensing *capacity* on demand over every contracted domain;
2. attributable identity for anyone who can be sanctioned, and linked histories of reports (Jackson–Sonnenschein);
3. actuarial and pooled-risk externalities that cannot be detected at the victim, where risk aversion makes informativeness bite;
4. victim types under Krier's "accurately represented" promise, for consent problems (Mailath–Postlewaite).

A revised article built on these four would be harder to answer than the present one.
