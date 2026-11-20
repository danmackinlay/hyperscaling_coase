# Cooperative game theorist (Fable). Received second, 2026-10-21. Verbatim.

# Red-team report: cooperative game theory angle

Sources read: `_plans/hyperscaling_coase_commitment_model.md` in full; `notebook/hyperscaling_coase.qmd` lines 102–219 only. Two abstracts fetched to pin citations (Ellingsen–Miettinen 2008 AER, Crawford 1982 Econometrica). Three small computations run (order statistics for the race; core LPs for k=1 with and without a chain; Shapley shares). Nothing written to the repo.

Notation: F = factory; residents 1, 2, 3 with h = (2, 3, 9); v(S) = what coalition S can guarantee (the essay's own convention, which gives v(F∪{i}) = 10 − h_i at k=1, π=10).

---

## 1. Cell C: the residents' internal agreement

**Verdict.** HOLDS WITH NARROWING for "the residents must first settle their split" (true, badly understated). FAILS for "resident 3, who has the most to lose from no deal, breaks first".

**Counter-argument.**
- The internal game over the residents' 6 at k=3 is a 3-player unanimity game (any proper subset of residents delivers nothing to the factory). Its core is the whole simplex; Shapley and nucleolus give 2 each. Harm size is irrelevant to the split because every resident's marginal contribution is identical: each is a veto. A proportional-to-harm split is an institution, not a solution. [sure]
- Under k=3, no deal = clean river = 0 for every resident. Resident 3's 9 never enters a no-deal payoff; it enters only if pollution happens uncompensated, which unanimity makes impossible without resident 3's own signature. Everyone loses exactly their pact share from no deal. If the pact is proportional to harm, resident 3 has the most to lose, which makes resident 3 the most loyal member, not the first defector. [sure]
- "Breaks first" has no referent in cell C: r_f = 0, so the factory cannot credibly refuse, so there is no refusal to break under. And a unilateral break under unanimity delivers nothing to the factory (it still needs the other two); it can only lower the bloc's demand. The sentence imports the k=1 dynamic. At k=1 the first to break is the resident with the largest bilateral surplus with the factory, v(F∪{i}) = 10 − h_i = (8, 7, 1): resident 1, then 2, then 3. Resident 3 is the last to break (the factory can net at most 1 by signing 3) and, with h = 9, the member who most wants the pact — Olson's privileged-group member who would fund it alone if arithmetic allowed. The plan has resident 3's role inverted. [sure, from the essay's own numbers]
- The real instability is the one the plan's own technology creates. If each resident can cheaply and provably commit, each can commit to the whole 6. Sequentially, the first to commit takes the pie from the factory and the other residents alike (resident 3 commits to 15; residents 1 and 2 are left exactly 2 and 3; S = 1, all to one resident). Simultaneously, the residents' side is its own cell D. So cell C needs three conditions, not one: residents can commit, the factory cannot, and an internal allocation rule fixes the split before anyone commits. The third is an institution (a union constitution) the plan silently assumes. [sure]
- Corollary: under unanimity a single committed resident already achieves S = 1. "As one" is unnecessary against the factory; its only work is internal fairness. [sure]

**Narrowing.** "The pact needs an internal allocation rule agreed before any resident can commit; without it, cheap commitment makes the residents' side a holdout race (sequential) or a standoff (simultaneous). Which resident holds out is a matter of who commits first, not of harm." Delete the resident-3 sentence.

**Settle.** Write the 3-resident subgame (6 to split, each may post a demand with large r): sequential → first mover takes 6; simultaneous → Nash-demand continuum plus the E–M selection. Tabulate no-deal payoffs: (0, 0, 0).

---

## 2. Side offers under unanimity

**Verdict.** FAILS as stated: "the factory must be unable to offer resident 3 alone a better deal" does no work in cell C, and the no-side-deals rule is misdescribed.

**Counter-argument.**
- At k=3 a side payment to one resident cannot reduce the factory's bill, because the remaining two each keep a veto and (in cell C) can commit while the factory cannot. Worked: pay resident 3 13 (harm + 4); 7 remain; residents 1 and 2 each commit to harm + 1; factory pays 20 and has overpaid resident 3 by 2. Side offers only reallocate the 20 among residents. [sure]
- A side offer could help the factory only by inducing residents to undershoot (demands summing to < 6), which requires the factory's offer to be credible as a ceiling, i.e. the factory committing. That is cell B, not C. [sure]
- Sequential non-contingent signing (the holdout protocol) exposes early signers to the last signer taking the remainder, but contingent offers ("X if and only if all three sign") are free in this model and remove it. [sure, in-model]
- So the no-side-deals rule does nothing against the factory at k=3. The rule that carries cell C is the internal allocation rule (stopping residents committing against each other, §1). The anti-side-deal rule is k<n medicine, where one signature suffices and a side deal kills the pact. The plan transplanted it. [sure]

**Narrowing.** "Under unanimity the union rule is an internal allocation rule, not an anti-side-deal rule; the anti-side-deal rule belongs to k<n." Move the side-deal sentence to §6.

**Settle.** Enumerate the factory's side-offer strategies at k=3 with r_f = 0 and show payoff ≤ 0 in each; repeat at k=1 and show the pact dies.

---

## 3. The race claim at k=1

**Verdict.** FAILS, on three independent grounds, any one sufficient.

**(a) Form.** The factory needs the *first* of n residents; the pact needs the *last* of n. With per-agent exponential rates μ_f, μ_N: P(pact first) = Σ_{j=0}^{n} C(n,j)(−1)^j · nμ_f/(nμ_f + jμ_N). At equal per-agent rates: n=2 → 0.167; n=3 → 0.050; n=5 → 0.004; n=10 → 0.000. For even odds at n=3 the residents' per-agent speed must be 6.9× the factory's (Monte Carlo agrees: 0.0504). The plan's λ_N/(λ_f+λ_N) hides this by naming one λ per side. "Unchanged by uniform cheapening" survives (the ratio is scale-free) but at the wrong value: the symmetric point is 1/20, not 1/2. Pact assembly is also not memoryless (a max of clocks has a rising hazard), so no single-rate ratio is the right form anyway. [sure, computed]

**(b) Incentive, sharper than Olson.** A resident inside a formed pact gets 0. A resident outside it, with the other two in, faces a bilateral monopoly with the factory over 10 − h_i: up to 8, 7, 1. Residents 1 and 2 strictly prefer to be *outside*. This is not free-riding (benefit without contributing) but active defection (more benefit when the good does not exist). Internal transfers cannot repair it: joining requires τ_i ≥ 10 − h_i, and Σ(10 − h_i) = 16 > 0, the essay's own core deficit. Equivalently, the revocation costs needed to hold the pact are r = (8, 7, 1), summing to 16, the amount by which the core is empty, with the burden on the *low*-harm residents. So the pact cannot form at any speed with rational, informed residents: λ_N is not small, it is zero. The race that exists is between residents 1 and 2 to be the factory's partner — the essay's own undercutting story — not between "the residents" and the factory. [sure, from the essay's numbers; Aivazian–Callen 1981 "The Coase Theorem and the Empty Core" is the essay's own citation for this, sure it exists]

**(c) Olson.** For n=3 with a dominant member, Olson's "privileged group" (Logic of Collective Action, ch. 1) [sure it exists] predicts the big stakeholder provides the good. Here resident 3 would need to pay 8 + 7 = 15 against a harm of 9. Olson's small-group optimism fails for the empty-core reason, not the free-rider reason. His point that it is an incentive problem is fatal: no speed makes resident 1 prefer 0 to 8.

Further: more compute for the residents makes the pact *less* likely, since the defection is a computation (resident 1 working out the 8). The plan's §8 bullet 3 ("if the pact assembles far faster ... the empty core stops mattering") is wrong: the empty core is about stability once formed, which speed cannot repair and only enforcement (r = 16 in total) can. And the only reading that keeps a race — residents' agents instructed at a constitutional stage to join any pact — makes the commitment an institution, so §6 contradicts §4 by letting compute decide what §4 says institutions decide. [sure]

**Narrowing.** "At k=1 the pact is not a coalition the residents would join; it must be imposed (a standing rule with r_i ≥ 10 − h_i). Imposed, there is no race; not imposed, there is no pact. Speed enters only if residents commit before computing their outside options, and more compute removes that case." If a race is kept, use the min-vs-max form.

**Settle.** The formula in (a) at n=3, equal rates; the participation constraint τ_i ≥ 10 − h_i summed. Both one line.

---

## 4. Chain restriction as a commitment device

**Verdict.** HOLDS WITH NARROWING. A chain restriction is an institution and does fix the k=1 core, but it is not a commitment device in the plan's sense, fits none of the four cells, and the core it buys has every non-pivotal resident worse off than under no deal.

**Counter-argument.**
- The result: when feasible coalitions are the connected sets of a line or tree, the restricted game has a nonempty core — Greenberg & Weber 1986 JET (consecutive coalitions) [likely]; Le Breton, Owen & Weber 1992 IJGT "strongly balanced" games [likely]; Demange 1994 JME and 2004 JPE for trees [likely]. Confirmed on the river by LP: chain F–3–2–1 nonempty; chain F–1–2–3 nonempty; unrestricted k=1 empty. [sure]
- Mechanism: the chain makes the factory's neighbour the sole conduit, converting k=1 into a bilateral monopoly between F and the gatekeeper, with the other residents as a side market bribing the gatekeeper to refuse. It changes *who is pivotal*: an entitlement reassignment (Calabresi–Melamed), not a position plus a revocation cost, and imposed rather than chosen. [sure]
- It helps only if it binds the *factory's* access (F∪{1} infeasible). A chain among residents with the factory free to approach anyone leaves every F∪{i} feasible and the core empty. So it restricts the factory's contracting, the opposite of "residents commit". [sure]
- Distribution, in every core point: gate at resident 3 → x_1 + x_2 ≤ −1; gate at resident 1 → x_2 + x_3 ≤ −8 (resident 1 extracts the factory's bilateral surplus 8 from the others). The low-harm gatekeeper is the expensive one. Efficient (clean river), but the non-gatekeepers end below no deal (0), violating the plan's own yardstick. [sure, LP]
- Which cell: none. The cells are defined at k=3 over a pie of 6; at k=1, π=10 there is no pie. If forced: the chain moves the game out of the empty-core regime into a k=n game with n=1 (the gatekeeper), after which A–D apply between F and the gatekeeper with the bribe market on the side. A precondition for the table, not an entry in it. In Schelling's loose sense it commits only the gatekeeper ("nothing passes without me"), and does so by rule, not by revocation cost; it is the other residents being disenfranchised, not the residents committing as one. [sure]

**Narrowing.** "A coalition-feasibility restriction is a third kind of institution the 2×2 cannot express: it changes pivotality, not commitment. It fixes the k=1 core at the price of a bribe from the non-pivotal residents to the pivotal one."

**Settle.** The two LPs above; identify which resident the essay's chain makes the gatekeeper.

---

## 5. Exhaustiveness of the four cells

**Verdict.** FAILS. The cells are corners of a space whose interior has outcomes no corner has, and the "both commit" corner is mislabeled.

- **Deterministic intermediate r.** Backward induction gives a step at r = the side's haggling payoff (3), not the pie: below it commitment is void (A), above it full (B/C/D). Nothing new; "larger than any slice you could gain by backing down" is right in spirit, "the pie" is the wrong threshold. [sure]
- **Crawford 1982, actual content** (abstract): impasse arises "when successful commitment is uncertain and irreversible"; it is probabilistic; and "making commitment more difficult ... need not always lower the probability of impasse". So Crawford gives a lottery over cells with positive-probability impasse and positive expected shares — a mixture no cell has — and a non-monotone cost–impasse relation. The plan's certain standoff and its monotone "cheaper commitment → more standoff" are not Crawford's. [sure, from the abstract]
- **Ellingsen–Miettinen 2008, actual content** (paper text): with c = 0 and q > 1/2 there are efficient compromise equilibria; at q = 1, c = 0 "there is also typically an equilibrium in which they [commit to half]"; with small c > 0 and q < 1 conflict with probability q² is the unique equilibrium; with q = 1 and small c > 0 "efficient compromises remain unattainable, but ... there are also equilibria in which one player gets all the surplus (in addition to the conflicting commitment outcome)". The plan's "this is what happens when committing is free and provable" is wrong in both words: free admits compromise; provable admits winner-take-all alongside standoff. What cheap provable commitment rules out is the *compromise*, not the deal. "Both commit" → {B, C, D}, not D. [sure, quoted]
- **Timing.** E–M's winner-take-all equilibria at q = 1 are the first-mover outcomes. With agents of unequal speed nothing is simultaneous: the first provable commitment takes the pie and the second mover, seeing it, does not commit incompatibly. So "both can commit" is a race to commit first, and one factory agent is structurally faster than three agents who must first agree a split (the min/max asymmetry of §3a). Cheap provable commitment for all tends to B, not D. The plan's §6 "the only place in the model where the ratio of the two sides' compute decides anything" is therefore false: it decides the right-hand column at k=3 too. [sure for the logic; E–M for the equilibrium set]
- **Asymmetric costs.** In Crawford's model the side with the cheaper or more reliable technology gains expected share *and* raises impasse probability: a frontier between S and efficiency, not points. Policy consequence: a union rule alone does not land in C unless the factory is barred from committing; otherwise it moves from B toward D. §4 says this but never names the institution that bars the factory. Labour law does: Boulwarism, take-it-or-leave-it bargaining, held a breach of the duty to bargain in good faith in NLRB v. General Electric (2d Cir. 1969) [sure the case exists; the gloss likely]. That is cell C's missing second rule.
- **Commitment to a procedure** (arbitration, a split rule, a coin) is "both commit, compatible": efficient, S fixed by the procedure. A fifth cell. [sure]
- **Partial commitment within the residents' side** (one commits, two do not) gives S = 1 to one resident under unanimity (§1). The aggregate S hides the within-side distribution the essay's "equitable" question is about. [sure]

**Narrowing.** "Four corners of a continuous space; the right-hand column is 'no compromise', not 'standoff'; with sequential commitment it is a first-mover race in which the coalition side is slower."

**Settle.** Quote the E–M proposition and Crawford's abstract; run the n=3-versus-1 race at k=3.

---

## 6. The yardstick claim, and S in the standoff cell

**Verdict.** HOLDS WITH NARROWING (narrow) for "nobody worse off than under no deal in any cell": true only at the corners r ∈ {0, ∞} with zero cost of committing. FAILS for "cannot distinguish the cells". S is not well defined in D.

- Individual rationality: at k=3 each resident can refuse (0 = no deal) and the factory can decline (0). In A–D as written all payoffs ≥ 0. [sure]
- But commitment *is* a self-imposed penalty: the side that backs down pays r and ends at share − r < 0 whenever r > share, which in Crawford happens with positive probability. And E–M's selection of D needs c > 0, under which both parties in D end at −c < 0: everyone worse off than no deal. At exactly the parameter values the plan's own citations need to *select* D, the no-worse-off yardstick sees D perfectly, as the one cell where everyone is below no deal. The plan uses c > 0 to get D and c = 0 to say the yardstick cannot see it. [sure]
- "Median better off" is not "anyone worse off". Residents' payoffs: A (1, 1, 1), B (ε, ε, ε), C (2, 2, 2), D (0, 0, 0). The median resident is strictly better off in A and C, not in D, and only by the penny in B. So the median yardstick does separate {A, C} from D, and from B up to the penny. The plan conflates the two yardsticks. [sure]
- S in D is 0/0. The plan concedes "no pie to share" and then scores D by efficiency and the others by S: two yardsticks. The honest statement is "no single yardstick works; it takes (efficiency, S); S alone conflates B with D for the residents (0 and 0) and is blind to the within-side split." [sure]
- §6's "the only cell in which a resident can end worse off than under no deal" conflates cell (commitment configuration) with regime (k); and the chain-restricted k=1 core (§4) and D with c > 0 both have parties below no deal. [sure]

**Narrowing.** "Under unanimity with free commitment and nobody backing down, no one is below no deal in A–D. Any positive commitment or revocation cost puts parties below no deal in D and in Crawford's back-downs, so the no-worse-off yardstick does see the standoff; what it cannot see is the B/C split, for which S is needed; S is undefined in D and blind within the residents' side."

**Settle.** Add c > 0 to the table and recompute each cell's payoff vector.

---

## Numbers checked against the river

- h = (2, 3, 9), Σ = 14; π = 20 → pie 6; π = 10 at k=1: all consistent with the essay.
- Core deficit at k=1: 8 + 7 + 1 = 16 from a pot of 0: matches the essay; LP confirms empty core.
- Cell B payments 2, 3, 9 (Σ 14, factory keeps 6): consistent. Cell C demand 20 (factory nets 0): consistent.
- Cell A "3 and 3": not derived. Four symmetric veto players give 1.5 each, S = 3/4. The 3/3 split is the Owen value with the residents as an a priori union (Owen 1977 [sure it exists]), which presupposes the bloc that cell C says needs commitment; merging three veto players lowers their symmetric share from 3/4 to 1/2. [sure, computed]
- Consent rule: "may pollute only if all three sign" at k=3 and "one signature" at k=1: as the essay states.
- §6 "the two who did not sign": at −3 and −9 if resident 1 signs: consistent.
- "Resident 3 has the most to lose from no deal": wrong (no deal = 0 for all at k=3).

## Claims outside my assignment that I believe are wrong

1. **Cell A "efficient, 3 and 3, what experiments show".** (i) Four veto players, not two: see above. (ii) Complete-information multilateral holdout bargaining with non-contingent sequential offers has delay and failure equilibria (Cai 2000 JET "Delay in multilateral bargaining under complete information" [likely]; Menezes & Pitchford 2004 "A model of seller holdout" [likely]), so "Efficient" in A is protocol-dependent. (iii) The equal-split experiments the plan has in mind (Nydegger & Owen 1974; Roth & Malouf 1979 [sure they exist]) are bilateral; multilateral holdout experiments (Cadigan, Schmitt, Shupp & Swope 2009 SEJ [likely]) show frequent delay and failure.
2. **§4 "cheap, provable commitment on both sides turns haggling into standoffs".** Per E–M, provable cheap commitment yields standoff *or* winner-take-all and never compromise; the headline should be "kills the compromise", and with sequential moves the typical outcome is winner-take-all by the faster side.
3. **§5 D "as budgets grow ... the standoff becomes certain" / "play converges to the cell's exact outcome".** E–M's conflict probability q² → 1 as q → 1, but at q = 1 the equilibrium set jumps to include winner-take-all. The limit is discontinuous; D has no unique exact outcome to converge to.
4. **§3 D attribution to E–M as "free and provable"**: wrong pair of words (see 5). Crawford's impasse is probabilistic and needs uncertain commitment success.
5. **§7 "his bargaining club is cell D, and the better the agents, the more reliably it fails to close"**: follows only under simultaneity; with speed asymmetry it is "the faster agent takes the pie".
6. **§5 B "margin about σ/√c_f per resident"**: with three independent acceptances required, holding a fixed joint acceptance probability needs a per-resident margin that grows with n (roughly √(2 ln n)); minor, but the stated rate is per resident, not per deal.

## The single most damaging objection

The model has two sides; the river has four players, and everything the essay has already proved about the river — the empty core at k=1, holdout at k=n — is a proof that the residents are not a side. The right-hand column, "residents can commit as one", is not a commitment choice. It is a coalition already formed with an agreed internal split, which is the hard part, and the model assumes it. At k=3 the union is unnecessary against the factory (a single committed resident takes the whole pie) and, without an internal allocation rule, cheap commitment makes the residents' side its own holdout race or standoff. At k=1 the pact cannot form at any speed, because each low-harm resident is worth more outside it (8, 7) than in it (0) and the enforcement it needs is exactly the core deficit (16), so the "race" of §6 is between residents 1 and 2 to be the factory's partner. Relabel the column honestly, as "an internal institution exists", and claim 2 ("institutions choose the cell") becomes true by construction and empty, while claim 1 ("cheap commitment → standoff") loses its support: the residents never reach the standoff without the institution, and when both sides genuinely can commit, the verified Ellingsen–Miettinen equilibrium set and the min-versus-max speed asymmetry say the faster single agent takes the pie rather than nobody.

Scratch files (gitignored, outside the repo): `/private/tmp/claude-501/-Users-dan-Source-livingthing/4585fff7-db8f-4fce-8214-b5f554c20266/scratchpad/check.py`, `check2.py`.
