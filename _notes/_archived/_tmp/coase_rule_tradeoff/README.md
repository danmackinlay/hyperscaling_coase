# coase_rule_tradeoff

Scratch for `_plans/hyperscaling_coase_rule_tradeoff.md` (2026-11-18). Keep while that note is live; it cites these files.

- `rules.py` — the simulation. `uv run python rules.py 4000 uniform` (about 4 minutes) writes `results_uniform.json`; `lognormal` is the second population.
- `tables.py` — prints the tables the note quotes: `uv run python tables.py uniform`.
- `spec.md` — the specification handed to the independent re-implementation.
- `check/` — that re-implementation, written without sight of `rules.py`.
- `repeat.py` — the first rule played for two rounds (no memory, naive households, strategic households). `uv run python repeat.py anchor` is the textbook check; `uv run python repeat.py population 0.3 320 uniform 1.0 16` is one row of the note's table (about 3 minutes on 16 cores) and writes `repeat_population_uniform_sigma0.3_delta1.0.json`. Kinds: `population`, `instance` (Alice, Bob and Carol), `solo` (Carol alone with the night slot).
- `repeat_tables.py` — prints those tables: `uv run python repeat_tables.py population [prior] [delta]`.
- `check_repeat/` — the independent re-implementation of the two-round figures and its specification; `repeat_claims_mine.json` holds this program's figures for the same cases.
