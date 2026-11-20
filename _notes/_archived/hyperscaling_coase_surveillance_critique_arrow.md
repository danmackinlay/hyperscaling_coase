# Red-team of `hyperscaling_coase_surveillance.qmd`, Arrow's brief

Attacker: Kenneth Arrow (information economics, social choice, mechanism design). Written 2026-11-19. Read the claims ledger, the article, Krier's essay as fetched today, and the prior-critiques summary. Arrow (1969) checked against the JEC text (montclair.edu PDF). Greenwald–Stiglitz checked only through a secondary summary (the primary was behind bot walls). Rob (1989) checked against its abstract. Other results are from my recall, marked [sure], [likely] or [unsure].

## Verdict tally

| Item | Verdict |
|---|---|
| Arrow (1969) citation | HOLDS as a quotation. Misplaced in its paragraph, and it leaves out the parts of the paper that matter most |
| C2 Greenwald–Stiglitz | HOLDS WITH NARROWING |
| C3 Holmström, "no interior stopping point" | HOLDS WITH NARROWING |
| C5 attestation | HOLDS WITH NARROWING |
| C6 unravelling | HOLDS |
| C7 preferences | HOLDS WITH NARROWING. The last sentence FAILS as stated |
| C16 data externalities | HOLDS WITH NARROWING |
| C22 "public encoding" | HOLDS WITH NARROWING. "Public" FAILS |
| C30 Coase's inspection cost | HOLDS |
| C32 Hayek's economy of information | HOLDS WITH NARROWING |
| C34 trade-off | FAILS as stated |
| Weak point 8 (differential comparison) | A real gap. It narrows the thesis, which survives in part |
| Weak point 9 (C7 weakest) | The concession is right, but for a different reason than the article gives |
| Weak point 11 (citations) | Coase, Myerson–Satterthwaite, Grossman, Milgrom, Holmström, Arrow: accurate. Rob, Mailath–Postlewaite, Greenwald–Stiglitz: loose. Farrell: accurate |
| Democratic mode (C10, C11, C18) | Social choice supports C10 and C18 by a route the article does not take, and adds one objection it missed |

Count: 3 HOLDS (Arrow citation as a quotation, C6, C30); 8 HOLDS WITH NARROWING (C2, C3, C5, C7, C16, C22, C32, and the democratic mode); 1 FAILS (C34). C7's final sentence and C22's word "public" fail inside claims that otherwise survive.

---

## The Arrow (1969) citation (l.414)

> "Arrow observed in 1969, in "The organization of economic activity", that a market for each externality has one buyer and one seller, so that nothing forces price-taking."

**HOLDS as a quotation.** The text reads: "Each commodity (j,i,k) has precisely one buyer and one seller. Even if a competitive equilibrium could be defined, there would be no force driving the system to it; we are in the realm of imperfectly competitive equilibrium" [sure, checked]. The paraphrase is fair.

**Placement is wrong.** The article uses the sentence to support an *informational* claim: personal prices have as many dimensions as the preference profile. Arrow's thin-market point is about *incentives*. In a market with one buyer and one seller, price-taking cannot be assumed, so each side manipulates. That supports C7, together with Hurwicz (1972), which showed that even the Walrasian mechanism is manipulable in finite economies [sure]. It does not support C22. Move the sentence to the Preferences section, where it is the earliest statement of the problem Myerson–Satterthwaite formalised.

**What else in Arrow (1969) bears on the thesis. Four passages, three for the article and one against it.**

1. *For: exclusion is sensing.* Arrow gives two reasons markets for externalities fail. The second is thinness. The first is Musgrave's exclusion principle: "Pricing demands the possibility of excluding nonbuyers from the use of the product, and this exclusion may be technically impossible or may require the use of considerable resources." His lighthouse example makes exclusion an identification problem: "the lighthouse need only shut off its light when a nonpaying ship is coming into range". This is the article's Remark 1 and its Conduct section, stated in 1969 as a *transaction cost* ("exclusion costs" are the first item on his list). Krier's clean-air fee is an exclusion technology: the street must identify the non-paying truck. The article should cite Arrow here. Here the citation is strongest, and the article does not use it.
2. *For: the same agents in two systems.* Arrow asks "to what extent is the voter, when acting in that capacity, a principal or an agent?". He also says codes of professional ethics "which arise out of the principal-agent relation and afford protection to the principals, can serve also as a cloak for monopoly by the agents." Both apply to agent providers. Neither is used.
3. *Against: agents cut the cost Arrow named.* Arrow writes: "the costs of transmitting and especially of receiving a large number of price signals may be high; thus, there is a tendency not to differentiate prices as much as would be desirable from the efficiency viewpoint; for example, the same price is charged for peak and offpeak usage of transportation or electricity." This is Krier's thesis in Arrow's words, and Krier even uses the peak-electricity example. On Arrow's accounting, agents remove a real transaction cost. The article's Hayek paragraph treats undifferentiated prices as a virtue, while Arrow treated them as a cost-driven departure from efficiency. The article should concede that.
4. *Against: the planner is costly too.* Arrow writes: "Removal of these welfare losses by changing to another system (for example, governmental allocation on benefit-cost criteria) must be weighed against any possible increase in transaction cost (for example, the need for elaborate and perhaps innumerable studies to determine demand functions without the benefit of observing a market)." This is the comparative-institutions test the article never runs (weak point 8, below). Arrow's framing is that transaction costs attach to "any mode of resource allocation". An argument that counts the informational cost of only one mode is, on Arrow's terms, incomplete.

Arrow also gives the norms passage: "It is useful for individuals to have some trust in each other's word... It is difficult to conceive of buying trust in any direct way". See the section on *Limits of Organization* below.

---

## C2. Greenwald–Stiglitz (l.146–151)

> "The externalities in question arise from hidden action and hidden type. A programme to price them by contract is therefore a programme to observe the hidden actions and hidden types that produce them."

**HOLDS WITH NARROWING.**

*Reading.* Greenwald and Stiglitz (1986) show that equilibria with imperfect information or incomplete markets are generically *constrained* Pareto inefficient, and that a government facing the *same* information constraints as private agents can make Pareto improvements with taxes and subsidies [sure]. "Generically inefficient" should be "generically constrained inefficient". The externalities are pecuniary effects that matter because of incentive and selection constraints. They come from moral hazard, adverse selection, signalling, search and incomplete risk markets, not from hidden action and type alone. So "arise from hidden action and hidden type" is **loose**.

*The inference does not follow as stated.* The canonical example (Arnott and Stiglitz; Arnott, Greenwald and Stiglitz 1994) is insurance moral hazard with an observable complement to carelessness, such as cigarettes. The remedy is a tax on cigarettes, which conditions on *observable trades*, not on effort. The authors note that if insurers had complete information on each person's consumption pattern and insurance purchases, *with effort still unobserved*, the market would be efficient [likely, via secondary summary]. Two things follow:

- To fix Greenwald–Stiglitz externalities *by private contract* you need each person's trades with *all other counterparties*, so that exclusivity and nonlinear pricing across markets can be enforced. You do not need the hidden action itself. That is still a surveillance requirement (a full consumption record per person, linked across vendors), and it fits the sugar example exactly. But it is a different requirement from "observe hidden actions and types".
- To fix them *by tax* you need only aggregate sales of the taxed commodity. This is the cleanest available statement of the planner–Krier differential (weak point 8), and it is in the very paper the article cites.

*Narrowing that saves it:* "Pricing these externalities by private contract requires each person's trades to be observable across all counterparties. A commodity tax corrects the same externality using only aggregate sales. The surveillance requirement is the price of doing by contract what the paper's own remedy does by tax."

*What would settle it:* checking Greenwald–Stiglitz §III and Arnott–Stiglitz (1986, "Moral hazard and optimal commodity taxation", JPubE) for the exclusivity condition.

---

## C3. Holmström and "no interior stopping point" (l.153–156)

> "As sensing becomes cheap... the demand for monitoring that emerges from voluntary contracting has no interior stopping point."

**HOLDS WITH NARROWING.**

*Holmström (1979) is stated accurately.* A signal has positive value if and only if the existing signals are not a sufficient statistic for it with respect to the action [sure]. The article's gloss, "any signal that is informative... will be used", is accurate for costless signals.

*Three counter-arguments.*

1. **Holmström's value of information comes from risk sharing.** With a risk-neutral agent and unlimited liability, the first best is reached by charging the realised outcome (selling the firm to the agent), and further monitoring has no value [sure]. For externalities this means charging the polluter for the *harm measured at the victim*, not monitoring the polluter's conduct. Victim-side measurement is still sensing, but its domain is the victim's street, not the actor's life. This is the incomplete-contract theorist's sparse-enforcement point (weak point 5), and Holmström's own model supplies it.
2. **With many polluters and one ambient signal, the relevant result is Holmström (1982, teams) and Segerson (1988).** An ambient-based tax, under which each polluter pays marginal damage on *total* concentration, induces efficient abatement without observing anyone's individual emissions [sure for Segerson; the budget-breaking role is Holmström 1982]. Here is a mechanism that prices a local externality with no individual attribution at all. It needs a budget breaker, and the victims can play that role.
3. **The article's own premise sets the stopping point.** C16 says people "value [privacy] highly". If so, privacy is an argument of the parties' utility, and the efficient contract stops monitoring where the marginal disutility of being sensed equals the marginal contractual value of the signal. That is an interior optimum. Arrow (1963) is the original case: insurers met moral hazard with coinsurance, not monitoring, because monitoring was costly. The article needs the thing that pushes the stopping point outward, and that is C6 and C16 (unravelling and the data externality), not Holmström.

*Narrowing:* "Voluntary contracting stops monitoring only where the parties' own valuation of privacy binds. Unravelling and data externalities (C6, C16) push that point towards full disclosure."

*What would settle it:* a two-line model with a privacy cost in the agent's utility and a cost of signals c → 0. Show whether the optimum converges to full monitoring only when the privacy cost is competed away by unravelling.

---

## C5. Attestation (l.168–177)

> "When a transfer flows towards the party who reports a harm, an unverified report is an invitation to inflate it, and screening by willingness to pay is unavailable."

**HOLDS WITH NARROWING.**

*Counter-argument.* "Screening by willingness to pay is unavailable" is wrong as mechanism design. In Clarke–Groves pivot mechanisms, a household that reports its harm does not receive its own report. It pays the externality its report imposes on others, and truth-telling is dominant [sure]. Under independent private values, Arrow (1979, "The property rights doctrine and demand revelation under incomplete information") and d'Aspremont–Gérard-Varet (1979) give Bayesian incentive-compatible, budget-balanced, efficient mechanisms for this kind of problem without verification [sure]. What these mechanisms give up is individual rationality, or budget balance in the dominant-strategy version. So the trade-off is not attestation against inflation. It is attestation against IR or budget balance, which is C7's territory. The article's either-or ("the claimant can pay... Or the claim can be attested") leaves out the third branch, and Arrow's own 1979 paper is that branch.

Other routes the article omits: ordeals and costly signals (Nichols and Zeckhauser 1982) [sure], and Crémer–McLean (1988) under correlated types, which applies here because neighbours on one street have correlated harms [sure].

*Arrow (1963) supports the article on the emergency case.* Medical facts are where the patient cannot verify, and where society relies on licensed, trusted third parties bound by a code. Seconds-scale verification of labour by route agents would need exactly that apparatus, made machine-readable. The emergency paragraph (l.179–181) **HOLDS**.

*On the Harberger levy* (l.176): the family that values clean air most pays the most, as under any self-assessed tax, and keeps a positive net. That is a distributional objection, not an efficiency one. The article should say which.

*Narrowing:* "Without attestation, truthful reports of circumstances can be elicited only by mechanisms that break budget balance or individual rationality (Arrow 1979; d'Aspremont–Gérard-Varet 1979). Krier's patches choose attestation instead."

---

## C6. Unravelling (l.183–188)

> "Grossman (1981) and Milgrom (1981) showed that when disclosure is verifiable and costless, the only equilibrium is full disclosure, because silence is read as the worst case."

**HOLDS.** The statement is accurate given the standard conditions: the sender is known to be informed, disclosure is costless, and the sender's preferences are monotone [sure]. The known escapes are Dye (1985), where the receiver is unsure the sender is informed, and Jovanovic (1982), where disclosure is costly [sure]. Neither applies here. The insurer knows the customer's agent holds the records, and agent-side disclosure is nearly free. Peppet (2011) is correctly described.

*What the article missed, and what strengthens it:* the Hirshleifer (1971) effect [sure]. Once types are revealed, insurance *against one's type* becomes impossible. Arrow (1963) made the same point about health insurance. Unravelling is therefore not only a loss of privacy. It is a loss of welfare in Arrow's own sense, because it destroys risk-sharing gains that existed behind the veil. This turns C6 from a remark about voluntariness into an efficiency cost that Krier's framework has to count, and the sugar example is exactly that case.

---

## C7. Preferences (l.192–228)

> "They describe the world that ideal agents bring about, in which each party's delegate computes and plays the optimal misreport."
> "The efficiency gain that the proposal promises over the present is available to the degree that the first branch is taken."

**HOLDS WITH NARROWING. The second sentence FAILS.**

*Statements of the results.*

- Myerson–Satterthwaite: accurate, given independent private values with overlapping supports [sure].
- Farrell (1987): accurate. He also argues that a bureaucrat can sometimes beat negotiation under private information, which helps the article and is not used [likely].
- Rob (1989): **loose.** The abstract says the probability of an ex post efficient decision falls below any ε > 0 once the number of residents is large [sure, checked]. So the probability goes to zero in Rob too. The article's "in the second case it tends to zero" understates Rob.
- Mailath–Postlewaite (1990): the result concerns public-good provision with individual rationality for each agent. IR gives each agent an implicit veto, and the probability of provision under any incentive-compatible, IR, budget-balanced mechanism goes to zero as n grows [sure]. "Projects that need the consent of many parties" is **loose but acceptable**.

*"Ideal agents bring about" holds.* The theorems bound *every* mechanism among Bayesian-rational players with a common prior, so delegates who optimise for their principals are exactly the players the theorems describe.

*Counter-arguments.*

1. **Second-best is not zero.** In the bilateral uniform case, the best incentive-compatible, IR, budget-balanced mechanism captures 27/32, about 84%, of first-best surplus (9/64 against 1/6) [sure]. In thick two-sided markets, double-auction inefficiency vanishes at rate O(1/m²) (Rustichini, Satterthwaite and Williams 1994) [sure]. The present baseline is *no* bargaining. So agents with private information and no attestation capture most of the available gain in bilateral and thick-market cases. Only in the Mailath–Postlewaite configuration (many parties, a public good, unanimity through IR) does the gain go to zero without attestation. The developer, the diffuse losers and the large street coalition are in that configuration. The truck and one household are not.
2. **Independence is doing the work, and local externalities are correlated.** Crémer–McLean (1988) and McAfee–Reny (1992) show that with correlated types, efficient and IR mechanisms exist using side bets on others' reports [sure]. The cost is fragility under risk aversion and limited liability (Robert 1991) [likely], plus the designer's need for the joint prior. The joint prior is a population-level statistical model of residents' types, which is an informational requirement the article could use. It is not individual attestation.
3. **The list of exits misses Arrow's own.** "Individual rationality can be dropped, which is coercion and returns the planner." Arrow (1979) and dAGV are exactly the efficient, budget-balanced, non-IR mechanisms. They are a constitutional choice of entitlement (who holds the veto), which links to Cramton–Gibbons–Klemperer and Segal–Whinston. The article cites the latter two but not the source.

*Narrowing that saves it:* "In the many-party, unanimity cases that motivate the essay (the developer, the diffuse losers, large coalitions), the efficiency gain over the present is available only to the degree that preference models are attestable. In bilateral and thick-market cases, second-best mechanisms without attestation capture most of it."

*What would settle it:* computing the Mailath–Postlewaite provision probability for n of the size of a street (10 to 50) and of a neighbourhood (10,000). If it is already small at n = 20, the narrowing costs the article little.

*Weak point 9.* The article calls C7 the weakest link "because shared entitlements and subsidized mechanisms can relax it." The stronger reason is (1): second-best already delivers most bilateral gains. The article is right to make the other five links independent of C7.

---

## C22 and C32. Message spaces and the "public encoding" (l.398–416, l.525–528)

> "A system of personal prices for every externality between every pair of affected parties has as many dimensions as the preference profile it summarizes. At that resolution the price vector is a public encoding of the preferences."

**HOLDS WITH NARROWING on dimension. FAILS on "public" and on "encoding of the preferences".**

*What information economics says.* Hurwicz (1960, 1977), Mount and Reiter (1974), Jordan (1982) and Sato (1981) formalised Hayek. In classical private-goods economies, the competitive mechanism has the minimal message-space dimension among mechanisms that realise Pareto-efficient allocations [sure]. In public-goods economies, the Lindahl mechanism plays that role, with personalised prices whose dimension scales with the number of agents times the number of public goods [likely for Sato]. Segal (2007) shows that any efficient social choice rule must communicate at least a supporting price equilibrium, so personalised supporting prices are the *minimal* thing an efficient mechanism must reveal [likely]. With nonconvexities, finite-dimensional decentralisation can fail altogether (Calsamiglia 1977) [likely]. Arrow (1969) has n²m personalised prices P_jik.

So the dimension claim **HOLDS**. An efficient allocation of pairwise externalities needs a message space growing with the number of affected pairs, and the "one price for many" economy is lost. The article is right on that count, and should cite Hurwicz and Mount–Reiter rather than leave it to the Hayek paragraph.

*Two corrections.*

1. **What the minimal message reveals is not the type.** An equilibrium personalised price reveals each agent's *marginal* willingness to pay *at the equilibrium allocation*: one point and one gradient of an infinite-dimensional preference. "Encoding of the preferences" overstates this. It becomes nearly accurate only when types are low-dimensional and the decision is binary, which is the case in Krier's examples (asthma yes or no, labour yes or no, enter or reroute). There a single threshold price is close to a sufficient statistic for the type. The article's examples happen to be the cases where its claim is strongest, and it should say so.
2. **To whom.** In Lindahl or Arrow-1969 pricing, the actor (the truck) needs only the *sum* of personalised prices on its route. Each household needs only its own component. The full vector is held by whoever clears payments. Hayek's economy at the receiving end, where the truck needs only one number, is *preserved*. What is lost is economy at the clearing node, and what leaks publicly is a k-aggregate that differencing breaks when k is small (the article's own l.401–402 attack, which is correct). Hurwicz called a mechanism "privacy-preserving" when each agent's message depends only on its own characteristics. In that technical sense, Lindahl pricing is privacy-preserving. The article's sense of privacy is different, and the overlap of terms should be flagged, not ignored.

*Narrowing that saves C22:* "The full vector of personalised prices is held by whoever clears payments. Counterparties see aggregates over the k affected parties. Those aggregates leak individual components by differencing when k is small, and in the binary examples a component nearly identifies the type." This keeps the argument and drops "public".

*C32 narrowing:* "Personal prices for every externality lose Hayek's economy at the clearing node, not at the receiver." The article's Hayek charge, "performing the function Hayek said the planner could not perform" (l.527), **HOLDS** for the direct-revelation parts of the proposal: the bargaining club, the quantified diffuse loss, and the Harberger register. It does not hold for a Lindahl-style price layer, which is Hayekian in Hurwicz's formal sense.

*What would settle it:* for the street with k households and a binary decision, compute the mutual information between the posted aggregate fee and one household's binary type as a function of k and of the query pattern. This is the simulation the article's own Discussion (l.563–564) asks for.

---

## C16. Data externalities (l.337–346)

> "show that because one person's data is informative about others, each person's data is nearly worthless at the margin once others have sold theirs... This is a Coasean market that fails for Coasean reasons."

**HOLDS WITH NARROWING.**

*Characterisations.*

- Choi, Jeon and Kim (2019) [likely accurate]: information externalities lead to excessive collection and a low price of privacy.
- Acemoglu, Makhdoumi, Malekian and Ozdaglar (2022) [likely accurate]: data prices are depressed, sharing is excessive, and shutting the market can raise welfare. The price falls as users become more numerous and more correlated [likely].
- Bergemann, Bonatti and Gan (2022) [likely accurate]: an intermediary acquires social data cheaply because of the externality, and prefers aggregated data that supports pricing at the group level.

"Nearly worthless at the margin once others have sold theirs" is a fair gloss across the three.

*"Coasean reasons" is loose.* The failure is that my data's informativeness about you cannot be excluded: Arrow's first source of market failure, exclusion, together with his second, thinness. In the models, the platform contracts *bilaterally* with each user, so the externality between users is a missing market. A zero-transaction-cost Coasean economy would contract over the *joint* disclosure of correlated users, which brings us back to Mailath–Postlewaite with many parties. Say "it fails for Arrovian reasons: non-exclusion and many-party bargaining."

*A point the article misses, and it helps the article.* Acemoglu et al.'s proposed remedy is a mediated data-sharing scheme that de-correlates disclosures [likely]. It needs an intermediary that sees everyone's data. That is precisely the "further layer of monitoring" (l.345–346), and the article could cite it as such.

---

## C30. Coase's inspection cost (l.514–516)

> "Coase (1960) listed among the costs of market transactions the cost of inspection needed to make sure that the terms of a contract are observed."

**HOLDS.** Coase's text: "to undertake the inspection needed to make sure that the terms of the contract are being observed, and so on" [sure]. The inference that zero transaction cost entails zero inspection cost is fair.

Two caveats. First, Coase's inspection covers *the terms of the contract*, not all conduct, so it supports Remark 1 and not totality. Second, Coase's own use of the zero-cost world was to argue for comparing institutions under *positive* costs, including the firm and the government (1960 §VI; 1988). Read in full, Coase demands the comparison the article omits (weak point 8).

---

## C34 and weak point 8. The differential comparison

> "Automatic enforcement with privacy requires coarse, aggregate instruments, which is the congestion charge and the uniform rule."
> (l.450) "A congestion charge for a city can be computed privately."

**C34 FAILS as stated.**

*The congestion charge is a counterexample to the article's own trade-off.* London's congestion charge is enforced by automatic number-plate recognition of every vehicle entering the zone. Images are bound to a registration, a persistent identifier, and kept for penalty processing. Over its domain it meets all four of the article's conditions: sensing, attribution, retention, and linkability to the vehicle register. Computing the *price* privately is easy. Enforcing it is surveillance. So "automatic enforcement with privacy" is not delivered by coarse pricing. Coarse pricing cuts the information needed about *types*. It does not cut the information needed about *conduct*. A uniform ban escapes only because it can be enforced *probabilistically* (Becker 1968: expected penalty = probability × fine), and probabilistic enforcement is available to Krier's contracts too (weak point 5).

*The comparison the article needs, by the layers of Remark 1 (s = σ(a, θ)):*

| Information required | Pigouvian tax authority / regulator | Complete Arrow–Debreu economy (Arrow 1969 construction) | Krier's regime |
|---|---|---|---|
| Conduct aᵢ in the taxed domain | Yes, individually, if enforced deterministically (cameras, meters); sparse if enforced by audit | Yes: exclusion requires identifying each consumer of each externality | Yes, the same |
| Aggregate damage function (distribution of θ) | Yes, statistically ("innumerable studies to determine demand functions", Arrow 1969) | No, revealed by prices | No |
| Individual types θᵢ | No | Revealed only as equilibrium marginal rates, to the clearing node | Yes, for need-conditioned prices, attestation, the club, Harberger registers, diffuse-loss models |
| Verifiable states for contingent claims | No | Yes: contracts are measurable in commonly observed events (Radner 1968) | Yes, the same |

*What survives.* On **conduct**, the surveillance implication does *not* distinguish Krier from the Pigouvian authority or from a complete Arrow–Debreu economy. Remark 1 is Radner's (1968) observation that contingent contracts must be measurable with respect to the information common to the parties [sure], and it binds every enforced allocation mechanism. On **individual types**, it *does* distinguish them. The planner taxing a commodity, or setting a uniform clean-air rule, needs the distribution of θ, not each θᵢ. Krier needs each θᵢ, or its attested proxy, for every need-conditioned price. Greenwald–Stiglitz's own remedy is the sharpest case (C2): aggregate sales for the tax, a full per-person consumption record for the contract.

*Narrowing that saves C34:* restate the three properties. (1) *Individually conditioned* pricing (on θᵢ, not only aᵢ). (2) Automatic enforcement. (3) Privacy *of types*. Then say that conduct sensing is common to every enforced regime, including the planner's, and that what DACN adds is a register of individual types linked to identity. This is a smaller claim, it is true, and it is the one the article's best sections (Circumstances, Preferences, Prices disclose) actually establish.

*What would settle it:* a section that sets the table above against the article's six requirements and marks which ones the regulator shares. My estimate: Conduct, Persons (for any per-capita instrument) and Disputes are shared. Circumstances, Preferences and most of Agents are not.

---

## The democratic mode (C10, C11, C18)

**Social choice supports C10 and C18 by a route the article does not take, and adds one objection it missed.**

1. *Escaping Arrow requires interpersonal information.* Arrow's theorem holds on ordinal, non-comparable information. The escapes (Sen 1970, 1977; d'Aspremont and Gevers 1977) enrich the informational basis with cardinal, interpersonally comparable utilities [sure]. Krier's promise that "the intensity of a person's need is accurately represented and compensated" is an escape of exactly that kind. It needs intensities that can be compared across persons, and therefore needs them measured and certified. That is a social-choice route to C7 and C10, and it is stronger than the article's.
2. *Gibbard–Satterthwaite makes "fidelity" underdetermined (missed).* With three or more options, every non-dictatorial rule is manipulable [sure]. A faithful agent therefore votes *strategically*. A fidelity audit (C10) cannot compare the ballot with the principal's sincere ranking, because the faithful ballot departs from it. It must compare the ballot with the principal's *whole* type plus the agent's beliefs about everyone else. That is a larger disclosure than the article claims, so it strengthens C10. It also undercuts the article's analogy with election audits (l.266–268). The audit problem is not only that the agent constructs the ballot. It is that no sincere benchmark exists to audit against.
3. *Mode choice is itself a social choice.* Which issues go to the willingness-to-pay mode and which to the one-person-one-vote mode is a meta-decision. Arrow's theorem applies to it too, and the willingness-to-pay mode is the Kaldor–Hicks criterion that *Social Choice and Individual Values* rejected (Scitovsky reversals). This bears on C11. In the economic mode, "vote selling" *is* the mechanism, so the boundary between modes is the only thing distinguishing a purchase from a bribe. The article's point that the boundary must be policed **HOLDS**. It would be sharper if it said the boundary has no procedure-independent location to police.
4. *C18 HOLDS.* With no procedure-independent social preference to check outcomes against, legitimacy can only be procedural, and procedural verification is exactly the identity, fidelity and separation checks.

---

## *The Limits of Organization*: support or escape?

**Both. It shows an escape the article dismisses too quickly, and then shows why Krier's design closes it.**

*Escape.* Arrow: "Trust is an important lubricant of a social system. It is extremely efficient" [sure]. His norms are not Ostrom's small groups. They are society-wide internalised codes. Arrow (1963) is the large-scale case: medical ethics and licensure substitute for monitoring physicians across a whole nation, because patients cannot verify. Krier calls the agent a "fiduciary". A professional fiduciary code for agent providers, with licensing, liability and a duty of confidentiality, is a large-scale form of "granular coverage + privacy" that rests on trust. The article's "works in small groups with exit and is Ostrom's case" (l.546) ignores it. So C34's first leg is too narrow.

*Closure, which the article missed and which helps it.* Arrow: "It is difficult to conceive of buying trust in any direct way... there seems to be some inconsistency in the very concept." Krier's programme converts norm-governed externalities (the leaf blower, the smoker, the mask) into priced ones. Each conversion replaces compliance resting on trust with compliance resting on contracts, and contracts need monitoring (Remark 1). Gneezy and Rustichini (2000, "A fine is a price") show the conversion can be one-way [sure]. Arrow's 1972 engagement with Titmuss ("Gifts and Exchanges") took that possibility seriously. So pricing externalities does not merely *use* monitoring. It *uses up* the norms that let a society go without it. This is a better irreversibility argument than C19's fee-income point. *Limits* ch. 2–3 adds that codes and information channels are irreversible investments [likely], which supports the "monitoring layer hardens first" claim (C19).

---

## Weak point 11: citation check

| Citation | Article's characterisation | Verdict |
|---|---|---|
| Coase (1960) | Inspection is among the costs of market transactions | **Accurate** [sure] |
| Arrow (1969) | Market per externality has one buyer and one seller; nothing forces price-taking | **Accurate** [sure, checked]. Misplaced (see above) |
| Greenwald–Stiglitz (1986) | Equilibria generically inefficient with imperfect information and incomplete markets; externalities from hidden action and type | **Loose**: "constrained" inefficient; the externalities are pecuniary, and the paper's remedy conditions on observables [sure on the theorem, likely on the remedy detail] |
| Holmström (1979) | Any informative signal has positive value and will be used | **Accurate** for costless signals and a risk-averse agent [sure] |
| Grossman (1981) | Verifiable costless disclosure: full disclosure is the only equilibrium | **Accurate** (implicit condition: sender known to be informed) [sure] |
| Milgrom (1981) | Same | **Accurate** [sure] |
| Myerson–Satterthwaite (1983) | No IC, IR, BB, efficient bilateral mechanism | **Accurate** (independent private values, overlapping supports) [sure] |
| Farrell (1987) | Drew the consequence for Coase | **Accurate** [likely] |
| Rob (1989) | Probability of efficiency falls with n | **Loose**: it falls below any ε for large n, i.e. tends to zero, as in Mailath–Postlewaite [sure, abstract checked] |
| Mailath–Postlewaite (1990) | Projects needing consent of many; probability → 0 | **Loose but acceptable**: public-good provision with IR (an implicit veto) [sure] |

Also: l.192, "The Coase theorem assumes that the parties know each other's valuations." Coase (1960) states no such assumption. It belongs to the later formalisation. **Loose.**

---

## Claims outside my list that I believe are wrong

- **Remark 1 is Radner (1968)** and its descendants, the measurability of contracts with respect to common information [sure]. "This is immediate" is fair, but the result should be cited, and it binds the planner too (see C34).
- **l.450–452, the congestion charge** "can be computed privately", and the claim that the privacy-preserving version is "close to... the uniform rules". The computation can be private; the enforcement is ANPR surveillance. See C34.
- **l.143, "The sensing must be as wide as the contracting."** This is correct for deterministic settlement only. Under random audit, sensing frequency can fall while expected penalties are preserved (Becker 1968). The sentence should say "the sensing *capability* must be as wide as the contracting." Capability is the version constitutional closure needs anyway.

## Reprise check against the prior critiques

Petel (2025) anticipates the core thesis, and the article cites him nowhere.

- **Core thesis.** Petel: "the more we can enforce, the more we must sense". That is the article's l.143 and its abstract in seven words. The article must cite Petel at l.143 or in the Introduction. The present framing ("Our claim is...", l.27) implies the thesis is new.
- **Persons section (l.237–240).** Petel: without proof of personhood "a neighborhood of one thousand can flower into a swarm of ten thousand sock-puppet agents". He also lists "one human, one principal, one accountable agent" in his governance stack. The Douceur paragraph reprises this and needs a citation.
- **Harberger levy (l.175–176).** Petel: Harberger-style option taxes "presuppose identity, low collusion and honest oracles". The article's attestation and identity points about the levy overlap. Cite Petel.
- **Privacy floor and inalienability (l.321, l.552–554).** Petel's constitutional layer is Calabresi–Melamed inalienability, with "privacy is a right, not a setting" and "price what you can; protect what you must". The article's repair condition is Petel's proposal. Cite him as the existing version of the repair, and say what the article adds: the argument for why the floor must be non-renegotiable.
- **ZK and DP (l.377ff).** Petel proposes "monitoring with differential privacy and zero-knowledge proofs" and "contracts that produce evidence... with retention limits". The article's cryptographic section is in effect a reply to Petel's stack as well as Krier's. Saying so would sharpen it.
- **Scott and legibility (l.530–532).** Petel: "measurement is political (Scott, Goodhart)". Partial overlap. Cite.
- **Ngo's "Schelling fence".** A rule binding against later temptation is the article's non-renegotiable privacy floor. Cite at l.552.
- **Snow.** No substantial overlap found. The article does not use the club opt-in point or the inferred-minimum point.

What the article has that Petel lacks: Remark 2, the differencing and reconstruction argument, the constitutional-closure argument, and the mechanism-design treatment of preference privacy. Those are where its novelty can honestly be claimed.

## Where the article misstates Krier

- **Scope of the privacy promise.** The abstract says Krier "promises its users full privacy". Krier promises users "complete privacy and control over their 'cognitive profile' developed by the agent". His cryptographic remark concerns "ensuring that preferences are communicated and aggregated without revealing sensitive underlying data". He promises nothing about *conduct* going unobserved. He lists "verify, monitor" among the agent's functions and wants "real-time monitoring of regulatory capture". The Conduct requirement therefore does not contradict any promise Krier made. The article's conflict holds only for Circumstances, Preferences and Agents (the profile). That is the same narrowing C34 needs, reached from Krier's text.
- **"The decision still belongs to the individual" (l.187)** is attached to the insurer's dietary records. Krier's nearest sentence, "The choice remains with the individual, but it is now a truly informed choice", comes from the *smoking* paragraph. The insurer passage contains no such sentence. Misattributed.
- **"Which rules stay fixed and which stay open is itself priced and settled by mutual agreement" (l.69).** The paraphrase is fair, but it omits that Krier names the rules to ossify ("basic property rights, contract enforcement"), and that elsewhere the state "continues to define and enforce basic property rights, contract law, criminal justice, and constitutional rights". Weak point 4 is live. This bears on D1, which is the other attackers' brief.
- **The emergency in labour (l.49): "once the emergency is verified".** Krier's labour passage says the neighbour's agent "flags an emergency" and that agents drop the price "because they actually *value* her getting through fast": altruistic valuation, not verification. "Verified emergencies" appears only in the separate low-traffic-neighbourhood paragraph. Minor, but the attestation argument (l.179–181) leans on it.
- **The allergic passenger "is compensated" (l.173).** Krier: "the intensity of a person's need is accurately represented and compensated". He leaves open who pays whom. The article's direction of transfer, towards the claimant, is an inference. It is needed for C5, so state it as one.

## The single most damaging objection

**Remark 1 binds every enforced allocation mechanism, so on conduct the article's surveillance implication does not distinguish Krier from the planner it replaces, or from a complete Arrow–Debreu economy.** Contracts measurable in what the enforcer observes is Radner (1968). Exclusion as a transaction cost is Arrow (1969). The Pigouvian authority's congestion charge already satisfies all four of the article's conditions over its domain. What is specific to Krier is narrower: a register of *individual types* (circumstances, reservation prices, preference models) linked to persistent identity, where the planner needs only their distribution. Greenwald–Stiglitz, the paper the article opens with, shows this most sharply: a commodity tax on aggregate sales corrects the externality, while a private contract needs each person's full consumption record. The thesis survives as "DACN commits a polity to a linked register of individual types". Its title, its trade-off (whose "automatic enforcement with privacy" leg is the congestion charge) and its Conduct section do not survive.
