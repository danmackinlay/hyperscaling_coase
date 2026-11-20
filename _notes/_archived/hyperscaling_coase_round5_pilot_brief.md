# Pilot brief: screening the learning arm before it is fixed

Draft, 2026-10-23, for one agent. Purpose: before any learning arm of `hyperscaling_coase_round5_instance.md` is written into a round, find out which of its parameters move the *sign* of the finding and which only move its size, so that the round fixes the ones that do not matter and sweeps the ones that do. The pilot produces no finding for the state; it produces a parameter verdict.

## Read, in this order, and nothing else

1. `_plans/hyperscaling_coase_mission.md` in full (the amendment of 2026-10-23 is merged).
2. `_plans/hyperscaling_coase_hard_case_instance.md`, the base instance.
3. `_plans/hyperscaling_coase_round5_instance.md`, the sections "Common to every arm" and "Arm 1a". Open no other file under `_plans/`; do not open the state file.

You are READ-ONLY in the repository: write nothing under `_plans/`, `notebook/` or anywhere tracked; your scripts and outputs go in your scratchpad directory, and you copy the final script and its output table into `_tmp/hyperscaling_coase_round5/pilot/` at the end. Do not commit.

## The question

Arm 1a asks whether a principal that plans over the residents' learning rule takes more than its seat share, $1.5$ of $6$, under a proposer drawn by lot among the four parties. Implement arm 1a as the note states it, with the principal's planner in the stated policy class and the residents in class L1 (mean-based, multiplicative weights over the demand grid), plus the reference cell with every party in L0. Then screen.

## The screen

Sample forty points of the parameter space below at random (a Latin hypercube over the listed values, seed $1$), rather than varying one parameter at a time, so that interactions show; at each point run $50$ runs (not the note's $200$; this is a screen) and record the principal's long-run take, each resident's, the deal rate and the floor. Then regress the sign of (principal's take $-\ 1.5$) and its size on the parameters to see which predict a change:

| Parameter | Stated | Screen over |
|---|---|---|
| learning rate $\eta$ | $0.1$ | $0.02,\ 0.05,\ 0.1,\ 0.2,\ 0.5$ |
| demand grid step | $0.25$ | $0.25,\ 0.5,\ 1$ |
| payoff rescaling for multiplicative weights | divide by $8$ | divide by $4$, by $8$, by $16$ |
| principal's horizon $H$ | $1,10,T$ | $1,\ 3,\ 10,\ 50$, and $T$ if feasible (report its cost if not) |
| length of play $T$ | $500$ | $200,\ 500,\ 2000$ |
| window for the reported average | last $100$ | last $50$, last $100$, last $250$ |
| margin set | $\{0,0.25,0.5,1,2\}$ | that set; $\{0,0.5,1\}$; a continuous margin chosen by line search |
| feedback | full information | full information; bandit (she scores only the demand she played) |
| sampled against expected play | sampled | sampled; expected (she plays the mean demand) |
| principal's planning dynamics | expected learner dynamics | expected; one sampled rollout; five averaged rollouts |

Then two cross-checks: residents in L3 with memory $5$ and $50$ at the stated values, and the reversed cell (residents plan as a bloc at $H=10$, principal in L1).

## What to return

The forty-point table, and one row per parameter: whether it predicts a change in the **sign** of (principal's take $-\ 1.5$), whether it predicts the **ordering** of takes across $H$, the largest change in the principal's take associated with it, and the wall-clock cost per point. Then, in under 400 words: which parameters the round may fix at the stated value because nothing moves; which it must sweep because a sign or an ordering moves, with the range to sweep; whether $H=T$ is feasible at $200$ runs and, if not, the largest feasible $H$; any place where the note's description of the planner or the learner could be implemented two ways, with the way you chose; and anything the arm needs that the note does not say. Mark every number with its seed, and run the stated cell twice with seeds $1$ and $2$ to report the seed noise, which is the yardstick for "moves".

Do not interpret the result for the essay and do not assess the null; the round does that. If a sign flips under a parameter that has no economic meaning (the rescaling, the window, the dynamics approximation), say so plainly: that is the pilot's most useful possible result, since by Dan's rule a finding that depends on such a parameter is too weak to carry.

## Model and budget

One Opus agent; a few hours of its own time; nothing else runs on this arm until it returns.
