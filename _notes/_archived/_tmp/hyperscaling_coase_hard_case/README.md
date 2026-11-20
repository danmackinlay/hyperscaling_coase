# hyperscaling_coase hard-case round, 2026-10-21

Expensive to regenerate (22 agents, 61 minutes, 3.45M subagent tokens): keep until the essay is drafted.

- `results.json`: the workflow's returned object, verbatim (`{date, rows[9]{first, second, agree}, optimists[2], critic, cold}`).
- `workflow_output_full.json`: the same with the harness wrapper (logs, progress, token counts).
- `results_readable.md`: the JSON rendered per row for reading; `# ROW …`, `# OPTIMIST …`, `# MODEL CRITIC`, `# COLD READ`.
- `agent_scratch/`: every subagent's scripts and saved outputs, copied from the shared scratchpad (`bits/`, `lang/`, `pact/`, `enforcer/`, `fb/` (the cut-off budgets reader), `mp/`, `wealth/`, `incumbent/`, `bundling/`, `consistency/` (the cold reader), top-level `*.py` from the Fable readers and optimists).
- `primaries.md`: what the collating session verified against primaries (Krier read; Petel and Snow via the prior-critiques file) and how the two families' numbers compare.
- `collator_rerun.py`, `collator_rerun_out.txt`: the session's re-run of every number carried into the state.
- `apply_state_delta.py`: the exact-match edit script that applied the round's deltas to `_plans/hyperscaling_coase_summary.md`; `summary_before_hard_case.md` is the state as it stood before.

Resume the workflow from cache with `Workflow({scriptPath: '_plans/hyperscaling_coase_hard_case_workflow.js', resumeFromRunId: 'wf_0091ef74-8c2', args: {date: '2026-10-21'}})`; the journal is under the session's `subagents/workflows/wf_0091ef74-8c2/`.
