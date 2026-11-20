# The red-team of the commitment model, reported for Dan

Written 2026-10-21 by a low-context Opus agent that read only `hyperscaling_coase_commitment_model.md` and `hyperscaling_coase_commitment_model_findings.md`, at Dan's request that the report come from someone with no inside knowledge. Reproduced verbatim. The four passages it says it had to guess at were clarified in the findings document immediately afterwards; the substance is unchanged.

**What was tested and how.**

The model asks how a factory, needing all three residents' signatures, divides the pie: the 6 left from a profit of 20 after paying harms of 2, 3 and 9. It sorts outcomes into four cells by who can commit, meaning publish a demand and lose money by retreating, and claims that cheap commitment on both sides, which software agents supply, yields standoffs, incompatible demands and no deal, and that the cell sets what more computing budget does. Six reviewers attacked it: an economist, a cooperative game theorist, a behavioural economist, an advocate for Krier, whose proposals the model criticises, a cold reader briefed in one sentence, and a repeated-games theorist. None saw another's work or the essay beyond its river section; the session that ran them, and wrote the findings, read the cited papers and re-checked their numbers.

**What failed.**

First, Ellingsen and Miettinen 2008, cited for the standoff, do not prove it. With perfectly reliable commitments either side may take all 6, or both gamble and usually end in standoff; the standoff is the sole outcome only when commitments are simultaneous, unable to respond to each other, cheap relative to the pie, made once and slightly unreliable, and then has probability q², q being the chance a commitment holds. All six found this.

Second, the model's own premises favour the factory: nothing makes the sides publish at once, the first to publish takes the 6 because the other accepts a penny over nothing, and one factory outpaces three residents, who either publish clashing demands or stop to agree. Instructions that can respond to each other would also make the standoff avoidable; all six found both.

Third, the model counts an agent's published instructions and hash, which proves only which instructions ran, as commitment, but the owner can reissue them free. A real cost of backing down needs a bond, escrow or court, all institutions, so the claim that without institutions cheap commitment yields a standoff defeats itself. Four reviewers found this.

Fourth, the model says more compute brings play to each cell's outcome and makes the standoff surer, but only cells where one side alone commits have a single outcome, and in the standoff cell backing down costs more than 6, so no belief makes it pay. Compute also chooses the cell, which the model denies, by deciding who commits first and cheapest. Six, six and two reviewers found these.

Fifth, the human baseline, a split of 3 and 3 when nobody commits, is wrong twice: humans in large cases face take-it-or-leave-it offers or zoning law, and uncommitted residents cannot bargain as one, so four parties can each block any deal and any method treating them alike gives each 1.5, three quarters of the pie to the residents. Five reviewers found each.

Sixth, the residents' cell assumes they act as one. If resident 3 alone commits to 15, the factory pays 15, 2 and 3 and resident 3 takes all 6; the hard problem is the residents' own split, where Miettinen and Vanberg 2025, read only in abstract, find that requiring everyone's consent makes binding minimum demands inefficient. All six found this.

**What survived.**

When one side alone can commit it takes the pie, provided the other accepts a penny over nothing, as agents do and people often do not, and residents answer one at a time. A rule giving one side the power to commit does fix the division, but Krier says the same. More compute for the factory does shrink the residents' share of each deal, more slowly than stated and to a floor.

**What is proposed instead.**

Cheap commitment for everyone does not by itself produce a standoff. If agents' instructions can respond to each other, the only question is which split; otherwise whoever commits first and most cheaply wins, on the river the factory, which pays 2, 3 and 9 and keeps the rest. Residents who can commit need two rules: one fixing their own split before any commits, one barring the factory from committing. Compute settles outcomes only where one side alone commits; elsewhere it decides who commits first or cheapest. The quarrel with Krier becomes scale and price: his club's single price must cover resident 3's 9, so 27 against a profit of 20. The document calls this proposed, not adopted, and says nothing in it is new.

**What Dan has to decide, and what in the findings document I could not follow.**

The document leaves you one decision: whether to adopt the thesis above in place of the model's closing claim that cheap commitment for everyone is a standoff.

These passages I had to guess at. "Observable but imperfectly binding" sits in the paragraph that says "nothing was committed": is a hashed instruction no commitment, or the slightly unreliable kind that yields the standoff? "Which on the river is the harms, 14" prices Krier's club at 14; a later finding says 27. "Loses power as offers become frequent" I could not turn into a split of the 6. The standoff arithmetic rests on "3 and 3 when both wait", a split rejected elsewhere; does it survive 1.5 each? "A threshold on that discount factor of one half", the weight on next year's payoff, comes without working; claims about the essay's unseen river section I took on trust.
