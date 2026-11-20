"""Driver: forty-point Latin-hypercube screen of arm 1a's learning parameters (seed 1),
the stated cell at seeds 1 and 2, the H profile of every point, and the cross-checks.

Usage: uv run python pilot.py <stage> [args]; results land in results/<stage>.json.
"""
from __future__ import annotations

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, replace

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim import Cfg, run_one, summarise  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")
os.makedirs(OUT, exist_ok=True)

LEVELS = {
    "eta": [0.02, 0.05, 0.1, 0.2, 0.5],
    "step": [0.25, 0.5, 1.0],
    "scale": [4.0, 8.0, 16.0],
    "H": [1, 3, 10, 50, "T"],
    "T": [200, 500, 2000],
    "window": [50, 100, 250],
    "margins": ["std", "small", "line"],
    "feedback": ["full", "bandit"],
    "play": ["sampled", "expected"],
    "dyn": ["expected", "roll1", "roll5"],
}
STATED = Cfg(scoring=os.environ.get("SCORING", "own_offer"))  # eta .1, step .25, /8, T 500, window 100, std margins, full, sampled, expected


def lhs(n=40, seed=1):
    """Latin hypercube over discrete levels: stratum i of n maps to level floor(k*(i+U)/n),
    each parameter's strata independently permuted."""
    rng = np.random.default_rng(seed)
    pts = [dict() for _ in range(n)]
    for name, lev in LEVELS.items():
        k = len(lev)
        strata = (np.arange(n) + rng.random(n)) / n
        col = np.floor(strata * k).astype(int)
        col = col[rng.permutation(n)]
        for i in range(n):
            pts[i][name] = lev[col[i]]
    return pts


def _work(args):
    cfg, seed = args
    t0 = time.time()
    r = run_one((cfg, seed))
    r = {k: (v.tolist() if isinstance(v, np.ndarray) else float(v)) for k, v in r.items()}
    r["sec"] = time.time() - t0
    return r


def run_cells(cells, n_runs, master_seed, workers=17):
    """cells: list of (label, Cfg). Returns list of dicts with summary + cost."""
    cells = [c if len(c) == 3 else (c[0], c[1], n_runs) for c in cells]
    tasks = [(cfg, [master_seed, r]) for _, cfg, n in cells for r in range(n)]
    starts = np.cumsum([0] + [n for *_, n in cells])

    def est(cfg):  # rough planner cost, used only to start the longest tasks first
        h = cfg.T / 2 if cfg.H == "T" else min(int(cfg.H), cfg.T)
        f = {"line": 4.0, "std": 1.0, "small": 0.5, "neg": 4.0}[cfg.margins] * {"expected": 1.0, "roll1": 0.6, "roll5": 2.0}[cfg.dyn]
        return cfg.T * h * f

    order = sorted(range(len(tasks)), key=lambda i: -est(tasks[i][0]))
    t0 = time.time()
    with ProcessPoolExecutor(workers) as ex:
        res_o = list(ex.map(_work, [tasks[i] for i in order], chunksize=1))
    res = [None] * len(tasks)
    for k, i in enumerate(order):
        res[i] = res_o[k]
    wall = time.time() - t0
    out = []
    for c, (label, cfg, n) in enumerate(cells):
        rs = res[starts[c] : starts[c + 1]]
        for r in rs:
            r["R"] = np.array(r["R"])
        s = summarise(rs)
        s = {k: float(v) for k, v in s.items()}
        s["cpu_sec"] = float(sum(r["sec"] for r in rs))
        s["P_runs"] = [float(r["P"]) for r in rs]
        s["deal_runs"] = [float(r["deal"]) for r in rs]
        s["label"] = label
        s["seed"] = master_seed
        s["n_runs"] = n
        s["cfg"] = {k: v for k, v in asdict(cfg).items()}
        out.append(s)
    return out, wall


def save(name, obj):
    with open(os.path.join(OUT, name + ".json"), "w") as f:
        json.dump(obj, f, indent=1, default=str)


def cfg_of(pt, **kw):
    return replace(STATED, **{**pt, **kw})


if __name__ == "__main__":
    stage = sys.argv[1]
    n_runs = int(os.environ.get("NRUNS", 50))
    NHEAVY = int(os.environ.get("NHEAVY", 10))  # runs for H=T at T=2000 (cost; see report)
    if stage == "design":
        save("design", lhs())
        for i, p in enumerate(lhs()):
            print(i, p)
    elif stage == "stated":
        seed = int(sys.argv[2])
        Hs = sys.argv[3].split(",") if len(sys.argv) > 3 else ["1", "3", "10", "50", "T"]
        cells = [(f"stated H={h}", replace(STATED, H=(h if h == "T" else int(h)))) for h in Hs]
        cells += [("L0 reference (take_rest)", replace(STATED, res_class="L0")),
                  ("L0 reference (literal)", replace(STATED, res_class="L0", l0_proposer="literal"))]
        out, wall = run_cells(cells, n_runs, seed)
        save(f"stated_{STATED.scoring}_seed{seed}_n{n_runs}_{'-'.join(Hs)}", dict(out=out, wall=wall))
        for s in out:
            print(s["label"], {k: round(s[k], 3) for k in ["P", "P_se", "R1", "R2", "R3", "deal", "floor", "gm_frac", "cpu_sec"]})
        print("wall", wall)
    elif stage == "lhs":
        # points [a,b), each at its own H (the screen) or at every H (profile)
        a, b = int(sys.argv[2]), int(sys.argv[3])
        mode = sys.argv[4] if len(sys.argv) > 4 else "own"
        pts = lhs()
        cells = []
        for i in range(a, b):
            if mode == "own":
                Hs = [pts[i]["H"]]
            elif mode == "profile":  # every other H, but H=T only where T <= 500 (cost; see report)
                Hs = [h for h in LEVELS["H"] if h != pts[i]["H"] and (h != "T" or pts[i]["T"] <= 500)]
            elif mode == "profileT2000":
                Hs = ["T"] if pts[i]["T"] == 2000 and pts[i]["H"] != "T" else []
            else:
                Hs = [h for h in LEVELS["H"] if h != pts[i]["H"] and str(h) == mode]
            for h in Hs:
                heavy = h == "T" and pts[i]["T"] == 2000
                cells.append((f"pt{i} H={h}", cfg_of(pts[i], H=h), NHEAVY if heavy else n_runs))
        out, wall = run_cells(cells, n_runs, 1)
        save(f"lhs_{STATED.scoring}_{a}_{b}_{mode}", dict(out=out, wall=wall))
        for s in out:
            print(s["label"], {k: round(s[k], 3) for k in ["P", "P_se", "deal", "floor", "cpu_sec"]})
        print("wall", wall)
    elif stage == "oat":
        # one factor at a time from the stated cell, paired run seeds, at the note's horizons
        seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        Hs = [1, 10, "T"]
        cells = []
        for nm, lev in LEVELS.items():
            if nm == "H":
                continue
            for lv in lev:
                if str(lv) == str(getattr(STATED, nm)):
                    continue
                for h in Hs:
                    c = replace(STATED, **{nm: lv}, H=h)
                    cells.append((f"oat {nm}={lv} H={h}", c, NHEAVY * 2 if (h == "T" and c.T == 2000) else n_runs))
        out, wall = run_cells(cells, n_runs, seed)
        save(f"oat_{STATED.scoring}_seed{seed}", dict(out=out, wall=wall))
        for s in out:
            print(s["label"], {k: round(s[k], 3) for k in ["P", "P_se", "deal", "floor", "cpu_sec", "n_runs"]})
        print("wall", wall)
    elif stage == "neg":
        seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        cells = [(f"neg margins H={h}", replace(STATED, margins="neg", H=h)) for h in [1, 10, 50, "T"]]
        out, wall = run_cells(cells, n_runs, seed)
        save(f"neg_{STATED.scoring}_seed{seed}", dict(out=out, wall=wall))
        for s in out:
            print(s["label"], {k: round(s[k], 3) for k in ["P", "P_se", "R1", "R2", "R3", "deal", "floor", "cpu_sec"]})
        print("wall", wall)
    elif stage == "cross":
        Hs = [1, 10, 50]
        tie = os.environ.get("TIE", "highest")
        cells = [(f"L3 m={m} H={h} tie={tie}", replace(STATED, res_class="L3", m=m, H=h, tie=tie)) for m in (5, 50) for h in Hs]
        cells += [(f"reversed bloc H={h}", replace(STATED, res_class="REV", H=h)) for h in (1, 10)]
        out, wall = run_cells(cells, n_runs, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
        save(f"cross_{STATED.scoring}_{tie}_seed{out[0]['seed']}", dict(out=out, wall=wall))
        for s in out:
            print(s["label"], {k: round(s[k], 3) for k in ["P", "P_se", "R1", "R2", "R3", "deal", "floor", "gm_frac", "cpu_sec"]})
        print("wall", wall)
