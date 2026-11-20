# Sampling brief: capture mechanisms, searched by fan-out rather than grid

Draft, 2026-10-23. Replaces mini-rounds 2 and 3 of `hyperscaling_coase_round5_instance.md`, whose arms become candidate starting points here. No run claims coverage; the write-up says how many runs there were, where each started, and which mechanisms more than one reached.

## The question and the fitness function

The question, verbatim from the mission: under which conditions does more computation for bargaining agents produce better outcomes, and for whom? The capture reading of it, which this round searches: the conditions under which more computation for one side takes value from the other, measured by the mission's criterion and floor, with the status quo reported alongside.

The essay's unit is the entailment: a sentence of the form "for the fair deal to arrive by default, X would have to be true, and nothing in giving everyone an agent makes X true." A mechanism is evidence for an entailment, a model is evidence for a mechanism, and a number is evidence for a model; the run returns them in that order, so that what comes back is what the essay consumes and the model is its footnote.

A run is a local search from a given starting point. It succeeds if it returns **one entailment**, the sharpest within reach of its start, in this form:

1. the entailment in one sentence a non-specialist can read, in the street's terms (the cast of `hyperscaling_coase_humanized.md`: the delivery company, Alice, Bob, Carol, their agents, the platform, the council), for example "Carol would have to have joined a club before the dispute existed";
2. the story: four to six sentences of what the company, the neighbours and their agents do when the entailment is false and one side has more compute, and how it ends, with who pays;
3. the mechanism in one sentence in institutional terms (what the party with more compute does, to whom, through which rule), and the agenda's best reply with what it concedes;
4. the grounding: the smallest model that shows it, every parameter and distribution stated, and a computation on it giving the pie, the split, the floor, who pays, which dial of compute does the work (estimation, speed, commitment, adaptation) and the sign of its effect on the loser, kept to one short paragraph and one table;
5. a replication on the base instance of `hyperscaling_coase_hard_case_instance.md` (four slots, three residents, pie $6$), or the sentence "not expressible on the base instance, because …" with the smallest change that would express it;
6. sources with the marks [sure], [likely], [unsure] and whether the primary was read;
7. a delta block in the mission's form, and a proposed-open-rows field.

Climb, do not survey: a run that returns three weak entailments has failed; a run that returns one entailment with its story, its mechanism and its grounding has succeeded even if the entailment is already on the state's two lists, since convergence is the signal. A run whose model is sound but whose entailment cannot be said in the street's terms has found a sequel, not a finding, and says so.

## The starting-point pool

Each run is dealt one starting point by seed, so the draw is visible. Pool A, a paper: each of Segal 2003; Genicot and Ray 2006; Winter 2004; Halac, Kremer and Winter 2020; Chipty and Snyder 1999; Braverman, Mao, Schneider and Weinberg 2018; Deng, Schneider and Sivan 2019; Ben-Porath 1993; Press and Dyson 2012; Camara, Hartline and Johnsen 2020. The run reads that paper and asks what capture mechanism it implies for a principal against residents with agents. Pool B, a story: each heading of `hyperscaling_coase_humanized.md`, from "When the company always makes the final offer" to "When the street is one of many"; the run reads that section only and pushes the story until compute on one side breaks the fair deal, then builds the model. Pool C, a role: the designer of the principal's agent, told to take the most from resident 3 with a stated compute edge; the designer of the residents' agents, told to stop it at a stated cost; the platform that writes the form and is paid per closed deal; the council that must write the one rule that restores the fair deal. Pool D, a fixed instance: arm 2a of the catalogue (the formation stage, parameters as written) and arm 2c (two neighbourhoods); these runs do not choose their model.

Twelve runs: four from A, four from B, two from C, two from D, drawn by seed $1$ without replacement within a pool; model families alternate so each pool has both. A run reads only the mission (amended 2026-10-23), the base instance and its starting point; it does not read the state file, so that it cannot reproduce the state's findings by memory. It may fetch primaries.

## Collation

The session clusters the twelve returns by entailment, since two mechanisms that expose one entailment are one finding for the essay. An entailment's score is the number of runs that reached it times the number of distinct pools they started from; two runs from one paper count less than one from a paper and one from a story. The top four entailments get one adversarial second reader each, from the other family, briefed to refute the grounding model and its numbers, not the story. Every surviving entailment is replicated on the base instance by the session before it enters the state, as a "sampled finding" row carrying its entailment, its story, its mechanism, its model, its starts, its score and its replication; those not expressible on the base instance go to the critic's list with the change that would express them. The humanised document gets the story of each surviving entailment, and the admission test of mission rule 10 applies: an entailment already on the state's two lists, or one that cannot be told in the street's cast, is recorded and not promoted; what is promoted is a third list, or the finding that the two lists were already complete.

## Stopping rule

This is the last research round before the thesis paragraph and the section plan (the state's next steps 2 and 5, standing since the existence test). Its output is a third list of entailments, the conditions under which more compute for one side takes value from the other, or the finding that there is none beyond the two lists; either way the next document is the thesis paragraph written from the three layers (state, plain summary, humanised document), not another brief. A further round runs only if the thesis paragraph, once drafted, turns out to rest on an entailment nobody has computed.

## What this round does not do

It does not test a null across arms, so it cannot say the null survives; it can only say which mechanisms were found, from where, how often, and whether they replicate. It does not fix parameters in advance beyond the base instance; a run's parameters are its own, stated, and judged by the replication. It does not reach the open system except where a start leads there, which the chain-store paper and the "one of many" story may.

## Budget

Twelve runs, up to four second readers, the session as collator: sixteen agents, about ninety minutes, three million tokens by the hard case's rate. Mini-round 1 and the pilot are unaffected; the pilot's screen becomes a random sample of forty points of its parameter space rather than one parameter at a time, with a sign-change regression on the result.
