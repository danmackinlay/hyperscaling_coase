"""Pact stage relative to three status quos; HS-Nash, extremes, durability screen."""
import json, sys, itertools as it
import numpy as np
from scipy.optimize import minimize, linprog
from core import *

P2 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
prof = profiles(P2)
pt = lambda th: P2 if th == 2 else 1 - P2
lp = LP(P2)


def sq_liab(sbar):
    xL = (p > sbar * E.sum(0) + 1e-12).astype(float)
    res = [{th: (sbar - th) * (E[i] @ xL) for th in TYPES} for i in range(3)]
    fleet = p @ xL - sbar * (E.sum(0) @ xL)
    true = [fleet] + [res[i][S_TRUE[i]] for i in range(3)]
    return res, fleet, true, xL


SQS = {"nodeal": ([{1: 0.0, 2: 0.0}] * 3, 0.0, [0.0] * 4, None)}
for sbar in (1.5, 1.0):
    SQS[f"liab{sbar}"] = sq_liab(sbar)


def party_rows():
    """fleet then (i,theta) interim rows, with HS weights."""
    rows, w, keys = [lp.fleet_row()], [1.0], ["F"]
    for i in range(3):
        for th in TYPES:
            rows.append(lp.interim_row(i, th, th)); w.append(pt(th)); keys.append(f"r{i+1}s{th}")
    return np.array(rows), np.array(w), keys


def concave_max(cons, R, c0, w, z0):
    A_ub, b_ub, A_eq, b_eq, bounds = cons
    f = lambda z: -np.sum(w * np.log(np.maximum(R @ z - c0, 1e-12)))
    g = lambda z: -(R.T @ (w / np.maximum(R @ z - c0, 1e-12)))
    r = minimize(f, z0, jac=g, method="SLSQP", bounds=bounds,
                 constraints=[{"type": "ineq", "fun": lambda z: b_ub - A_ub @ z, "jac": lambda z: -A_ub},
                              {"type": "eq", "fun": lambda z: A_eq @ z - b_eq, "jac": lambda z: A_eq}],
                 options={"maxiter": 3000, "ftol": 1e-13})
    return r.x, r.message


def maximin(cons, R, c0, obj):
    lo, hi, best = 0.0, 20.0, None
    for _ in range(45):
        mid = (lo + hi) / 2
        try:
            z = lp.solve(obj, cons, extra_ub=[(-R[j], -(c0[j] + mid)) for j in range(len(c0))])
            lo, best = mid, z
        except AssertionError:
            hi = mid
    return best, lo


def durability(z):
    """Search product events A for an alternative gamma, IC given A, that every approving type and the
    fleet strictly prefer (given A) and every non-approving type weakly disprefers. Returns best eps per A."""
    found = []
    opts = [(1,), (2,), (1, 2)]
    for A in it.product(opts, repeat=3):
        n = lp.n + 1  # last var eps
        rows_ub, b = [], []
        pad = lambda r: np.concatenate([r, [0.0]])
        for i in range(3):
            for th in TYPES:
                Ug = lambda rep: lp.interim_row(i, rep, th, A=A)
                Ud = lp.interim_row(i, th, th, A=A) @ z
                if th in A[i]:
                    for rep in TYPES:
                        if rep != th:
                            rows_ub.append(pad(Ug(rep) - Ug(th))); b.append(0.0)
                    r = -pad(Ug(th)); r[-1] = 1.0
                    rows_ub.append(r); b.append(-Ud)
                else:
                    for rep in TYPES:
                        rows_ub.append(pad(Ug(rep))); b.append(Ud)
        fr = -pad(lp.fleet_row(A=A)); fr[-1] = 1.0
        rows_ub.append(fr); b.append(-(lp.fleet_row(A=A) @ z))
        A_eq, b_eq = [], []
        for k in range(lp.K):
            row = np.zeros(n); row[k * 16:(k + 1) * 16] = 1; A_eq.append(row); b_eq.append(1.0)
        bounds = [(0, 1)] * lp.nq + [(None, None)] * 6 + [(None, 1.0)]
        c = np.zeros(n); c[-1] = -1
        res = linprog(c, A_ub=np.array(rows_ub), b_ub=np.array(b), A_eq=np.array(A_eq), b_eq=b_eq,
                      bounds=bounds, method="highs")
        if res.status == 0 and res.x[-1] > 1e-7:
            found.append((A, round(res.x[-1], 4)))
    return found


def at_true(z, sq_true):
    k0 = lp.kidx[S_TRUE]
    qs = {NAMES[j]: round(z[lp.qi(k0, j)], 3) for j in range(16) if z[lp.qi(k0, j)] > 1e-6}
    pay = [sum(z[lp.qi(k0, j)] * p @ X[j] for j in range(16)) - sum(z[lp.tau(i, S_TRUE[i])] for i in range(3))]
    pay += [z[lp.tau(i, S_TRUE[i])] - S_TRUE[i] * sum(z[lp.qi(k0, j)] * E[i] @ X[j] for j in range(16)) for i in range(3)]
    gains = [pay[j] - sq_true[j] for j in range(4)]
    pie = sum(gains)
    nash = float(np.prod(gains)) if min(gains) >= -1e-9 else None
    nash_abs = float(np.prod(pay)) if min(pay) >= -1e-9 else None
    return dict(schedule=qs, payoffs=[round(v, 3) for v in pay], gains_over_sq=[round(v, 3) for v in gains],
                nash_gains=None if nash is None else round(nash, 4), floor_gain=round(min(gains), 3),
                pie_over_sq=round(pie, 3), pie_abs=round(sum(pay), 3),
                res_share_abs=round(sum(pay[1:]) / sum(pay), 3) if sum(pay) > 1e-9 else None,
                nash_abs_vs_clean=None if nash_abs is None else round(nash_abs, 4), floor_abs=round(min(pay), 3))


R, w, keys = party_rows()
out = {}
for name, (sq_res, sq_f, sq_true, xL) in SQS.items():
    cons = lp.base_constraints(sq_res, sq_f)
    c0 = np.array([sq_f] + [sq_res[i][th] for i in range(3) for th in TYPES])
    exante = [lp.fleet_row()] + [lp.exante_row(i) for i in range(3)]
    tot = sum(exante)
    mechs = {}
    mechs["fleet_opt"] = lp.solve(lp.fleet_row(), cons)
    mechs["res_bloc_opt"] = lp.solve(sum(exante[1:]), cons)
    zmm, lev = maximin(cons, R, c0, tot)
    mechs["maximin_interim"] = zmm
    zhs, msg = concave_max(cons, R, c0, w, zmm)
    mechs["hs_nash"] = zhs
    Wmax = tot @ lp.solve(tot, cons)
    out[name] = {"sq_true": [float(v) for v in sq_true], "sq_interim": {k: float(v) for k, v in zip(keys, c0)},
                 "max_exp_surplus": round(float(Wmax), 4), "maximin_level": round(lev, 4), "hs_msg": msg}
    print(f"\n==== {name}: SQ at true {sq_true}; max expected surplus {Wmax:.4f}; maximin interim gain {lev:.4f}")
    for mn, z in mechs.items():
        ex = [round(float(r @ z), 4) for r in exante]
        exg = [round(ex[0] - sq_f, 4)] + [round(ex[i + 1] - sum(pt(th) * sq_res[i][th] for th in TYPES), 4) for i in range(3)]
        interim = {k: round(float(r @ z), 3) for k, r in zip(keys, R)}
        d = dict(exante_payoffs=ex, exante_gains=exg,
                 exante_nash=round(float(np.prod(exg)), 4) if min(exg) >= -1e-9 else None,
                 exp_surplus=round(float(tot @ z), 4), interim=interim, at_true=at_true(z, sq_true))
        d["replaceable_on"] = durability(z)
        out[name][mn] = d
        print(mn, json.dumps(d, default=float))
        np.save(f"z_{name}_{mn}_P{P2}.npy", z)
json.dump(out, open(f"run2_P{P2}.json", "w"), indent=1, default=float)
