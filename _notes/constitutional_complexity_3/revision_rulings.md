# Revision: rulings on the cold read

The cold reader's full report is in `_tmp/coase3/cold_read_1.md`. Its line numbers refer to the file as it stands now. Address every item in it. For most the suggested fix is right and you should apply it in your own words. Where an item needs a decision about substance, the ruling is below and overrides the reader's suggestion.

## Things that changed in the file since you wrote it

- House spelling is Oxford **-ize** (maximize, realize, generalize, analyze). My earlier instruction to use -ise was wrong. The file has been converted; keep it that way. "Behaviour", "labour", "kerb" stay British.
- The References section now holds verified entries with DOI links, in the form `- Authors (Year). [Title](link). *Venue* vol(issue): pages.` Do not rewrite existing entries. Delete entries for works you no longer cite. Add these if you cite them, exactly as given:
  - `- Blackwell, D. (1953). [Equivalent comparisons of experiments](https://doi.org/10.1214/aoms/1177729032). *The Annals of Mathematical Statistics* 24(2): 265-272.`
  - `- Fudenberg, D., & Maskin, E. (1986). [The folk theorem in repeated games with discounting or with incomplete information](https://doi.org/10.2307/1911307). *Econometrica* 54(3): 533.`
  - `- Hobbes, T. (1651). Leviathan. Andrew Crooke.`
- Three sentences were edited for accuracy (gross substitutes; Zhu et al. and Vaccaro et al.; the Mailath–Postlewaite per-person cost). Keep their substance.

## Rulings

1. **Title.** Fixed by the author. Leave it exactly as it is, grammar included.

2. **The premise.** The prices of computation and messaging are positive and may be as small as anyone likes: $c,\kappa\to 0^+$. The informational results hold even at exactly zero. The computational and contest results are statements about that limit. Say this once in the abstract and once in the setup, and make every later sentence consistent with it. Dixit–Olson's "very small transaction costs" then needs no apology.

3. **The term "benevolent leviathan".** Keep the two-part definition: *leviathan* = can impose outcomes, including taxes, on parties who do not consent; *benevolent* = its objective is aggregate welfare. Knowledge of the distribution $F$ is a third thing the job requires, not part of the definition. Wherever the three appear together (abstract, end of the "claims and concedes" section, conclusion) say "a benevolent leviathan that also knows $F$" or equivalent, so the reader never sees two definitions.

4. **The decomposition.** Present it as an ordered attribution, not an identity: first the loss that would remain with truthful agents and unlimited computation removed, and so on. Give the terms their arguments: $L_{\text{info}}(N)$, $L_{\text{comp}}(c,\kappa;m,N,k)$, $L_{\text{contest}}(N,r,V)$. Or replace the equation with a four-item list. Your choice; it must not assert additivity and then deny it.

5. **Mailath–Postlewaite.** State the conditions we actually know from the paper's abstract: a yes/no decision, all must agree, each agent's value private, types independent, "very mild" further conditions. Soften the opening promise from "cited with its conditions" to "cited with the conditions that matter for the application". Spell out the mapping to the developer: for the theorem to apply as the neighbourhood grows, the project must scale with it, so that the developer's value per household $V/N$ stays in the range where some households' minima exceed it. Add the one-sentence resolution of the "common knowledge that it is efficient" puzzle (everyone knows the total gain is positive; nobody knows who should bear how much, and every voluntary rule for sharing invites understatement). In the intuition, multiply influence by the size of the stake and state the implied rate: only a share of order $N^{-1/2}$ of what is needed can be raised.

6. **Bargaining club.** Add the missing constraint and the comparison, as a derivation of ours. The developer pays at most $V$, so the per-household price satisfies $p\le V/N$. Let $\mu=\mathbb E[\theta_i]$. If $V/N>\mu$, the efficient rule (go ahead iff $\frac1N\sum_i\theta_i\le V/N$) approves with probability tending to one by the law of large numbers, while the posted-price-with-veto rule approves with probability $F(p)^N\le F(V/N)^N\to 0$ whenever $V/N<\bar\theta$. Reading 2 loses truthfulness and is also inefficient (it approves only if $N\max_i\hat\theta_i\le V$). Reading 3: once dissent can be overridden an efficient rule exists, but it pays members different amounts (the expected-externality mechanism) or, more simply, pays the mean (see ruling 13); either way members with high minima are compelled.

7. **Posted prices by many rights-holders (the Cournot derivation).** $N$ is the number of independent rights-holders whose permission is each required. Say plainly at the start that the truck with a way round is the case where the result has least force, and that it applies in full to a delivery that must reach that street and to the factory, which needs every resident's permission and cannot be routed round. Run the uniform example on the factory and the 10,000 residents as well: without a coalition, a fraction $1/10{,}001$ of efficient projects proceed. Give Krier credit: his flash coalition is the merged price-setter, which lifts this to one half. Then the two residual problems: one half is not one, and joining the coalition is voluntary, so a resident does better staying out and posting her own price (the Dixit–Olson and Ellingsen–Paltseva point). Fix the abstract: "pricing by each of $N$ independent rights-holders". Attach the "sole seller" sentence to Arrow, not Starrett. Explain Starrett in two plain sentences or cut him.

8. **"Inherited jurisprudence mostly assigns all-to-one rights."** Mark as my reading, and tie it to Calabresi and Melamed's property rules (an entitlement its holder may refuse to sell at any price).

9. **Crémer–McLean.** "Is consistent with", not "strengthens".

10. **Communication and computation section.** Restructure as the reader suggests. Open with the section's role: these bounds bind a planner and a market equally, so they are not an argument for planning; they show two things. First, cheaper computation does not dissolve them, because problem size enters exponentially and price only linearly. Second, the only way to make the problems tractable is to restrict what may be bid for and what contracts may say, and someone has to choose the restriction. Then keep, each worked on a running example:
    - bits (Nisan–Segal) with the punchline made explicit: with $m=m_0 2^k$ the bits needed grow like $2^{m_0 2^k}$; a thousandfold fall in $\kappa$ buys about ten more items, which is less than one extra binary distinction once $m_0\ge 10$. State $B=\text{spending}/\kappa$.
    - when simple prices exist (substitutes against complements), on the route and the development;
    - winner determination, one short paragraph, without the Håstad–Zuckerman parenthetical;
    - coalitions, with the missing step: Krier's coalition is all 10,000 residents, and it has to be stable against sub-groups whose harms differ from the average and who would do better bargaining separately, which is where the count of coalitions and the empty core come in;
    - correlated equilibrium needs a correlator, and the selection point. Drop PPAD.
    - contracts: the $2^k$ count (note Shannon's bound is for two actions), the checkable-language point tied to the quoted "near-instantaneous computational verification", Segal, residual control, Maskin–Tirole. Mark "the holder of residual control is the sovereign" and "that commitment needs an outside enforcer" as my reading.
    Cut the "incentives and computation compound" subsection to one sentence (Nisan and Ronen only). Move "designing the mechanism is itself hard" to one sentence in the regress section where the designer's task is discussed, stating the objective (expected welfare or revenue under the prior). Remove from the references anything no longer cited (Håstad, Zuckerman, Dobzinski, Dobzinski–Vondrák, Vondrák, Daskalakis et al., Chen et al., and whatever else falls out).

11. **Costs section.** Retitle to say what it shows: costs that do not fall, and in one case rise, as computation gets cheap. Use "computation" throughout the article for what agents spend; "cognition" only when reporting Tirole. Budgets: either cut the sentence or add this one-line derivation: if every party's budget $w_i$ binds, then $e_i=w_i/c$ and party $i$'s share is $w_i^{\,r}/\sum_j w_j^{\,r}$, which does not contain $c$. "More of it" in the Tirole paragraph means more in quantity. Ellingsen–Miettinen: state their conditions (small positive commitment cost; attempts succeed with probability $q<1$), say why both sides attempt it (each tries to commit to a demand that leaves the other little, and when both succeed the demands are incompatible), and say that as agents make commitment more reliable $q$ rises and with it $q^2$, without taking the limit. Do not introduce $\gamma$.

12. **Voting.** Acknowledge the symmetry: both the winner-determination bound and the manipulation shield are worst-case. The asymmetry is in who benefits from typical cases being easy: an allocator and a manipulator both do.

13. **A running example carried through to its remedy.** The reader's most important complaint is that no example is followed to the point where the leviathan acts. Add a short subsection near the end of the regress section doing this for the developer and the 10,000 homeowners. It is a derivation of ours:
    - Rule: approve the project iff $V\ge N\mu$, where $\mu=\mathbb E[\theta_i]$ is the mean minimum acceptable payment, and pay every household $\mu$. No reports are used, so there is nothing to misreport.
    - Accuracy: the efficient rule approves iff $V/N\ge\bar\theta_N$, the sample mean. The two rules disagree only when $V/N$ falls between $\mu$ and $\bar\theta_N$, and the loss from a wrong decision is then $|V-\sum_i\theta_i|\le N|\bar\theta_N-\mu|$. With variance $\sigma^2$ of $\theta_i$, the expected loss is at most $N\cdot\sigma/\sqrt N=\sigma\sqrt N$, against stakes of order $N$: a relative loss of order $N^{-1/2}$. The blunt rule gets better as $N$ grows; voluntary bargaining gets worse.
    - What it takes: knowing $\mu$, which is a fact about $F$; binding the households whose $\theta_i>\mu$, who are made worse off, which is compulsory purchase (eminent domain) at average harm; and not wanting the difference for oneself, since an authority that set the payment below $\mu$ and sold approvals would be the broker of the earlier example.
    - This is what states already do, and it is the kind of "clumsy, one-size-fits-all" rule Krier wants to replace. The theorems say that for large $N$ it is close to the best available, and that what agents can improve is the estimate of $\mu$.
    Check the bound yourself before writing it.

14. **Why this is a planner's job.** Do not assert it; argue it, and concede the gap. Hayek's knowledge is of particulars, and knowing $F$ is weaker than knowing each $\theta_i$. But (i) what the actor does with $F$ is set entitlements, tax rates, compensation schedules and permitted contract forms, which is what planning agencies do; (ii) $F$ is needed separately for each class of decision at the granularity of the mechanism, per neighbourhood and per kind of nuisance, and hyper-granular contracting means hyper-granular $F$; (iii) errors in $F$ produce the failures Krier attributes to planners. Use "planner" in this sense and say so. Soften "is doing a planner's job" to something the argument supports.

15. **The regress and Mailath–Postlewaite.** Argue the mapping, as argument: any proposed change from the status-quo rules to an alternative is a yes/no decision over which every party has a veto and a private stake, which is the setting of the theorem, for each proposed reform in turn.

16. **Vouchers.** Krier says governments or philanthropies. A right to an agent that does not depend on a donor's goodwill needs a tax base.

17. **Contradiction at the end.** Agent bargaining leaves the problem of good government in place. Say that both times; drop "moves the problem to a different place".

18. **Predictions.** Keep the first two gradients (number of parties whose consent one decision needs; complementarity). Replace the third: resources burned in bargaining should scale with the surplus at stake and should not fall as computation gets cheaper.

19. **Qualifications.** Abstract: the contest result is "in a standard contest model". Conclusion: "the theorems and models above", and do not attribute the contest or computational claims to theorems.

20. **Status labels.** One fixed light form for our own derivations, used every time (for example a sentence beginning "The derivation is mine"). Drop the promise of "two or three lines". Drop the tautological sentence about arguments.

21. **Krier's material used later but never introduced.** Add to the summary section, briefly and in his words where short: enforcement becoming "a near-instantaneous computational verification"; the billionaire's phone; liquid democracy; verified emergencies passing at zero price; the three layers (law, a competitive market of agent providers, the individual); his starting cases (office thermostat, apartment block, chores); automated governance. Say who Krier is in a clause at first mention (he leads frontier policy development at Google DeepMind and writes in a personal capacity). Make every quotation's speaker unambiguous; the "dispersed, specific knowledge" phrase and "The sovereign can always renege" are Krier's words.

22. **Notation.** One symbol, one meaning, and every symbol in the table. Reports $\hat\theta_i$; ownership shares $\alpha_i$; the advocate's signal $\sigma_i$; contest decisiveness $r$; the truck's or factory's value for permission $b$ throughout, with distribution function $G$ and density $g$; resident's harm $s$ in the two-party case and $h_i$ with many; write "the Bell number" in words; drop $K$ (say "for each kind of action"); a different letter for the contest sum; table entries for $p$, $\mu$, $\sigma$, $\bar\theta$, $\underline\theta$, $\bar u_i$, $m_0$, $A$, $n$, $B$. Define virtual cost where it is used.

23. **Prose.** Apply the reader's section 5 in full: cut the announcing sentences and the flourishes, keep at most one "does A; does not B" antithesis in the whole article, describe the prior responses (Petel, Ngo, Shahidi et al., Sharp et al.) once, not twice, replace the heading about "thinning" the veil with a literal one, and end on a plain statement. Gloss each term of art at first use as the reader lists; where a gloss would be longer than the point is worth, cut the point.

24. **Length.** Do not let it grow past about 9,500 words. The cuts in ruling 10 pay for the additions.

Keep one sentence per line. Do not open any repository file other than the article, `_tmp/coase3/cold_read_1.md`, this file, and the files you were given before.
