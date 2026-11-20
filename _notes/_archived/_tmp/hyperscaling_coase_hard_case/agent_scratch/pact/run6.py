"""Finite budgets: the fleet observes y_i = s_i + N(0, se^2) for each resident (public signal), prior P(s_i=2)=1/2.
The pact is designed on the posterior. Report, averaged over signals given the realised s=(1,1,2), the interim
payoffs of the realised types for the fleet-best durable (efficient) mechanism and the maximin durable one."""
import json, sys
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from core2 import *

NODES = 5
xg, wg = hermegauss(NODES); wg = wg / wg.sum()
KEYS = ["F"] + [f"r{i+1}s{th}" for i in range(3) for th in TYPES]
REAL = [0, 1, 3, 6]  # F, r1s1, r2s1, r3s2 in KEYS order


def sq_liab(sbar):
    xL = (p > sbar * E.sum(0) + 1e-12).astype(float)
    res = [{th: (sbar - th) * (E[i] @ xL) for th in TYPES} for i in range(3)]
    return res, p @ xL - sbar * (E.sum(0) @ xL)


SQ = {"nodeal": ([{1: 0.0, 2: 0.0}] * 3, 0.0), "liab1.5": sq_liab(1.5)}
out = {}
for se in [float(a) for a in sys.argv[1:]] or [1.0, 0.3, 0.1]:
    for sqname, (sq_res, sq_f) in SQ.items():
        base = np.array([sq_f] + [sq_res[i][th] for i in range(3) for th in TYPES])
        acc = {"fleet_best": np.zeros(4), "maximin": np.zeros(4)}
        accW = {"fleet_best": 0.0, "maximin": 0.0}
        nps = {"fleet_best": 0.0, "maximin": 0.0}
        for a in range(NODES):
            for b in range(NODES):
                for c_ in range(NODES):
                    w = wg[a] * wg[b] * wg[c_]
                    y = [S_TRUE[0] + se * xg[a], S_TRUE[1] + se * xg[b], S_TRUE[2] + se * xg[c_]]
                    post = [float(np.clip(1 / (1 + np.exp(-(yi - 1.5) / se**2)), 1e-3, 1 - 1e-3)) for yi in y]
                    m = M(tuple(post), full_t=False)
                    cons = m.cons(sq_res=sq_res, sq_f=sq_f, ir="interim", efficient=True)
                    rows = [m.F()] + [m.U(i, th, th) for i in range(3) for th in TYPES]
                    zs = {"fleet_best": m.lp(m.F(), cons)}
                    zs["maximin"], _ = m.maximin(cons, rows, list(base), m.Wrow())
                    for k, z in zs.items():
                        v = np.array([rows[j] @ z for j in REAL]) - base[REAL]
                        acc[k] += w * v
                        accW[k] += w * float(m.Wrow() @ z)
                        nps[k] += w * (float(np.prod(v)) if v.min() >= -1e-9 else 0.0)
        out[f"{sqname}_se{se}"] = {k: dict(mean_realised_gains=[round(x, 4) for x in acc[k]],
                                         nash_of_means=round(float(np.prod(acc[k])), 4) if acc[k].min() >= -1e-9 else None,
                                         mean_of_nash=round(nps[k], 4), exp_surplus=round(accW[k], 4)) for k in acc}
        print(sqname, se, json.dumps(out[f"{sqname}_se{se}"]), flush=True)
json.dump(out, open(f"run6_{'_'.join(sys.argv[1:]) or 'all'}.json", "w"), indent=1)
