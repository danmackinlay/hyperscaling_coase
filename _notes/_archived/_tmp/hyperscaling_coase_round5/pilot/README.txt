Arm 1a pilot (2026-10-23). About 3 h on 17 cores to regenerate. Run from this folder with uv run --project ../../.. python:
pilot.py stated <seed> | lhs 0 40 own | lhs 0 40 profile | oat 1 | cross 1 | neg 1   (env SCORING=own_offer|counterfactual, TIE=highest|zero, NRUNS, NHEAVY)
Seeds: design (Latin hypercube) seed 1; run r of a cell uses default_rng([seed, r]). Raw cells are in results/*.json.
Outputs: out_table40.md (the forty points), out_verdict_*.txt (H profile, regressions, one-factor runs), out_stated_cell_seeds.txt, out_crosschecks.txt.
