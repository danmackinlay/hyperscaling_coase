import json, sys
import numpy as np
from scipy.optimize import minimize
from core import *

P2 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5

# --- instance check by enumeration
print("schedule profit harms(1,1,2) surplus")
for j, x in enumerate(X):
    h = [S_TRUE[i] * E[i] @ x for i in range(3)]
    print(f"{NAMES[j]:5s} {p@x:5.1f} {h} {surplus(x, S_TRUE):5.2f}")
print("first best at true:", first_best(S_TRUE))
prof = profiles(P2)
Wstar = 0
for s, pr in prof:
    m, arg = first_best(s)
    Wstar += pr * m
    print("profile", s, "pr", pr, "FB", m, arg)
print("expected first-best surplus W* =", Wstar)


def sq_liab(sbar):
    xL = (p > sbar * E.sum(0) + 1e-12).astype(float)
    res = [{th: (sbar - th) * (E[i] @ xL) for th in TYPES} for i in range(3)]
    fleet = p @ xL - sbar * (E.sum(0) @ xL)
    true = [fleet] + [res[i][S_TRUE[i]] for i in range(3)]
    sq_surplus = sum(pr * surplus(xL, s) for s, pr in prof)
    return xL, res, fleet, true, sq_surplus


SQS = {"nodeal": ([{1: 0, 2: 0}] * 3, 0.0, [0, 0, 0, 0], 0.0)}
for sbar in (1.5, 1.0):
    xL, res, fleet, true, sqs = sq_liab(sbar)
    print(f"liability sbar={sbar}: schedule {xL}, fleet {fleet}, res interim {res}, at true {true}, E surplus {sqs}")
    SQS[f"liab{sbar}"] = (res, fleet, true, sqs)

lp = LP(P2)
results = {}
for name, (sq_res, sq_f, sq_true, sq_surp) in SQS.items():
    cons = lp.base_constraints(sq_res, sq_f)
    rows = [lp.fleet_row()] + [lp.exante_row(i) for i in range(3)]
    sqv = [sq_f] + [sum((P2 if th == 2 else 1 - P2) * sq_res[i][th] for th in TYPES) for i in range(3)]
    mechs = {}
    # fleet-optimal
    mechs["fleet_opt"] = lp.solve(lp.fleet_row(), cons)
    # residents-optimal (equal-weight sum)
    mechs["res_opt"] = lp.solve(sum(rows[1:]), cons)
    # surplus-max then (tie-break nothing)
    tot = sum(rows)
    mechs["surplus_max"] = lp.solve(tot, cons)
    # maximin of ex ante gains: add eps variable via augmenting: emulate with bisection
    lo, hi = 0.0, 10.0
    best = None
    for _ in range(40):
        mid = (lo + hi) / 2
        try:
            z = lp.solve(tot, cons, extra_ub=[(-rows[j], -(sqv[j] + mid)) for j in range(4)])
            lo, best = mid, z
        except AssertionError:
            hi = mid
    mechs["maximin_exante"] = best
    # Nash max of ex ante gains, SLSQP from maximin point
    A_ub, b_ub, A_eq, b_eq, bounds = cons
    R = np.array(rows); c0 = np.array(sqv)
    f = lambda z: -np.sum(np.log(np.maximum(R @ z - c0, 1e-12)))
    g = lambda z: -(R.T @ (1 / np.maximum(R @ z - c0, 1e-12)))
    r = minimize(f, best, jac=g, method="SLSQP", bounds=bounds,
                 constraints=[{"type": "ineq", "fun": lambda z: b_ub - A_ub @ z, "jac": lambda z: -A_ub},
                              {"type": "eq", "fun": lambda z: A_eq @ z - b_eq, "jac": lambda z: A_eq}],
                 options={"maxiter": 2000, "ftol": 1e-12})
    mechs["nash_exante"] = r.x
    print(f"\n==== status quo {name}: SQ at true {sq_true}, SQ E-surplus {sq_surp}; SLSQP {r.message}")
    results[name] = {}
    for mn, z in mechs.items():
        rep = lp.report(z, sq_res, sq_f, sq_true=sq_true, label=mn)
        rep["abs_true_nash_vs_clean_river"] = (round(float(np.prod(rep["at_true_payoffs"])), 4)
                                               if min(rep["at_true_payoffs"]) >= -1e-9 else None)
        rep["abs_true_floor_vs_clean_river"] = round(min(rep["at_true_payoffs"]), 3)
        results[name][mn] = rep
        print(json.dumps(rep, default=float))
        np.save(f"mech_{name}_{mn}_P{P2}.npy", z)
json.dump(results, open(f"run1_P{P2}.json", "w"), indent=1, default=float)
