"""Finite budgets, ex post veto (k=3 consent given on the realised deal), fleet proposes its best mechanism
without an efficiency restriction; flag whether it passes the durability screen."""
import json, sys
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from core2 import *
from screen import screen
NODES = 5
xg, wg = hermegauss(NODES); wg = wg / wg.sum()
REAL = [("F",), (0, 1), (1, 1), (2, 2)]
se = float(sys.argv[1])
acc = np.zeros(4); accd = 0.0; acc_eff = np.zeros(4); exact_true = None
for a in range(NODES):
    for b in range(NODES):
        for c_ in range(NODES):
            w = wg[a] * wg[b] * wg[c_]
            y = [S_TRUE[0] + se * xg[a], S_TRUE[1] + se * xg[b], S_TRUE[2] + se * xg[c_]]
            post = tuple(float(np.clip(1 / (1 + np.exp(-(yi - 1.5) / se**2)), 1e-3, 1 - 1e-3)) for yi in y)
            m = M(post, full_t=True)
            for eff, store in ((False, "any"), (True, "eff")):
                cons = m.cons(sq_res=[{1: 0., 2: 0.}] * 3, sq_f=0.0, ir="expost", sq_res_expost=lambda i, s: 0.0, efficient=eff)
                z = m.lp(m.F(), cons)
                v = np.array([m.F() @ z] + [m.U(i, th, th) @ z for (i, th) in REAL[1:]])
                if store == "any":
                    acc += w * v
                    accd += w * (1.0 if not screen(m, z) else 0.0)
                else:
                    acc_eff += w * v
print(json.dumps(dict(se=se, fleet_best_any_realised=[round(x, 4) for x in acc], share_durable=round(accd, 4),
                      fleet_best_eff_realised=[round(x, 4) for x in acc_eff])), flush=True)
