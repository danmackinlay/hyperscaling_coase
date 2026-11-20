"""Pact stage: durable (efficient) sets relative to each status quo; the veil; regret."""
import json, sys, itertools as it
import numpy as np
from scipy.optimize import linprog
from core2 import *

P2 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
pr2 = (P2, P2, P2)
KEYS = ["F"] + [f"r{i+1}s{th}" for i in range(3) for th in TYPES]
REAL = ["F", "r1s1", "r2s1", "r3s2"]  # the realised types
log = {}


def sq_liab(sbar):
    xL = (p > sbar * E.sum(0) + 1e-12).astype(float)
    res = [{th: (sbar - th) * (E[i] @ xL) for th in TYPES} for i in range(3)]
    fleet = p @ xL - sbar * (E.sum(0) @ xL)
    return res, fleet, xL


def screen(m, z):
    """durability screen (H-M voting story, passive beliefs on rejection, learning on approval)."""
    found = []
    for A in it.product([(1,), (2,), (1, 2)], repeat=3):
        n = m.n + 1
        pad = lambda r: np.concatenate([r, [0.0]])
        rows, b = [], []
        for i in range(3):
            for th in TYPES:
                Ud = m.U(i, th, th, A=A) @ z
                if th in A[i]:
                    for rep in TYPES:
                        if rep != th:
                            rows.append(pad(m.U(i, rep, th, A=A) - m.U(i, th, th, A=A))); b.append(0.0)
                    r = -pad(m.U(i, th, th, A=A)); r[-1] = 1; rows.append(r); b.append(-Ud)
                else:
                    for rep in TYPES:
                        rows.append(pad(m.U(i, rep, th, A=A))); b.append(Ud)
        r = -pad(m.F(A=A)); r[-1] = 1; rows.append(r); b.append(-(m.F(A=A) @ z))
        Aeq = []
        for s in PROFILES:
            row = np.zeros(n); row[m.k[s] * 16:(m.k[s] + 1) * 16] = 1; Aeq.append(row)
        c = np.zeros(n); c[-1] = -1
        res = linprog(c, A_ub=np.array(rows), b_ub=b, A_eq=np.array(Aeq), b_eq=np.ones(8),
                      bounds=[(0, 1)] * m.nq + [(None, None)] * (m.n - m.nq) + [(None, 1)], method="highs")
        if res.status == 0 and res.x[-1] > 1e-7:
            found.append(["".join(map(str, a)) for a in A] + [round(res.x[-1], 4)])
    return found


def summarise(m, z, base, label, do_screen=True):
    rows = [m.F()] + [m.U(i, th, th) for i in range(3) for th in TYPES]
    v = {k: round(float(r @ z), 4) for k, r in zip(KEYS, rows)}
    real = [v[k] for k in REAL]
    real_base = [base[k] for k in REAL]
    g = [a - b for a, b in zip(real, real_base)]
    ex = [round(float(m.F() @ z), 4)] + [round(float(m.exante(i) @ z), 4) for i in range(3)]
    d = dict(label=label, interim=v, realised_types=real, realised_gains=[round(x, 4) for x in g],
             nash_realised_gains=None if nash(g) is None else round(nash(g), 4), floor_realised=round(min(g), 4),
             nash_realised_abs=None if nash(real) is None else round(nash(real), 4), floor_abs=round(min(real), 4),
             exante=ex, exp_surplus=round(float(m.Wrow() @ z), 4),
             res_share_exante=round(sum(ex[1:]) / sum(ex), 4) if sum(ex) > 1e-9 else None)
    if not m.full_t:
        pay, sched = m.expost(z, S_TRUE)
        d["expost_true"] = [round(x, 3) for x in pay]; d["schedule_true"] = sched
    if do_screen:
        d["replaceable_on"] = screen(m, z)
    print(json.dumps(d, default=float))
    return d


SQ = {"nodeal": ([{1: 0.0, 2: 0.0}] * 3, 0.0)}
for sb in (1.5, 1.0):
    r_, f_, xL = sq_liab(sb)
    SQ[f"liab{sb}"] = (r_, f_)
    print(f"liability statute sbar={sb}: fleet runs {xL}, fleet SQ {f_}, residents' SQ by type {r_}")

for sqname, (sq_res, sq_f) in SQ.items():
    for irmode in (["interim", "expost"] if sqname == "nodeal" else ["interim"]):
        m = M(pr2, full_t=(irmode == "expost"))
        base = {"F": sq_f, **{f"r{i+1}s{th}": sq_res[i][th] for i in range(3) for th in TYPES}}
        kw = dict(sq_res=sq_res, sq_f=sq_f, ir=irmode, sq_res_expost=lambda i, s: 0.0)
        rows = [m.F()] + [m.U(i, th, th) for i in range(3) for th in TYPES]
        b0 = [base[k] for k in KEYS]
        w = [1.0] + [m.pt(i, th) for i in range(3) for th in TYPES]
        tag = f"{sqname}/{irmode}"
        print(f"\n===== {tag}")
        log[tag] = {}
        for eff in (False, True):
            c = m.cons(efficient=eff, **kw)
            name = "eff" if eff else "any"
            zf = m.lp(m.F(), c)
            if zf is None:
                print(name, "infeasible"); log[tag][name] = "infeasible"; continue
            out = {}
            out["fleet_best"] = summarise(m, zf, base, f"{name}:fleet_best")
            out["r3high_best"] = summarise(m, m.lp(m.U(2, 2, 2), c), base, f"{name}:r3high_best")
            zmm, lev = m.maximin(c, rows, b0, m.Wrow())
            out["maximin"] = summarise(m, zmm, base, f"{name}:maximin(level {lev:.4f})")
            zhs, info = logmax_cuts(m, c, rows, b0, w)
            out["hs_nash"] = summarise(m, zhs, base, f"{name}:hs_nash{info}") if zhs is not None else "maximin<=0"
            # range of fleet's take and of r3-high's take over the set
            out["range_F"] = [round(float(m.F() @ m.lp(-m.F(), c)), 4), round(float(m.F() @ zf), 4)]
            out["range_r3high"] = [round(float(m.U(2, 2, 2) @ m.lp(-m.U(2, 2, 2), c)), 4),
                                   round(float(m.U(2, 2, 2) @ m.lp(m.U(2, 2, 2), c)), 4)]
            out["max_exp_surplus"] = round(float(m.Wrow() @ m.lp(m.Wrow(), c)), 4)
            print(name, "range F", out["range_F"], "range r3high", out["range_r3high"], "max E surplus", out["max_exp_surplus"])
            log[tag][name] = out

json.dump(log, open(f"run3_P{P2}.json", "w"), indent=1, default=float)
