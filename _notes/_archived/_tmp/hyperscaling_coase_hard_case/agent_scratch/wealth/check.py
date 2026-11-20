"""Independent check of the NBS by direct numeric maximisation (Nelder-Mead over transfers), plus common-origin comparison."""
import math, numpy as np
from scipy.optimize import minimize
from wealth import p, E, s, W0, SCHED, NAME, NONE, ALL, util, origin_utils, harms
def lognp(t, x, U0, cal):
    w = np.r_[W0[0] + p @ x - t.sum(), W0[1:] + t]
    G = [util(j, w[j], x, cal) - U0[j] for j in range(4)]
    return -sum(math.log(g) for g in G) if min(G) > 0 else 1e9
for cal in ["marg", "wta", "money"]:
    U0 = origin_utils(NONE, cal); res = []
    for x in SCHED:
        best = None
        for start in [harms(x) + 1.5, harms(x) * 2 + 0.5, harms(x) + 3]:
            r = minimize(lognp, start, args=(x, U0, cal), method="Nelder-Mead", options=dict(xatol=1e-9, fatol=1e-12, maxiter=40000))
            if best is None or r.fun < best.fun: best = r
        if best.fun < 1e8: res.append((NAME(x), -best.fun, best.x))
    res.sort(key=lambda r: -r[1])
    print(cal, [(n, round(math.exp(v), 10), np.round(t, 3)) for n, v, t in res[:3]])
# common origin (clean river, residents at endowment): fleet's-right no-deal outcome MDEN
for cal in ["marg", "wta"]:
    U0 = origin_utils(NONE, cal)
    w = W0.copy(); w[0] += p @ ALL
    G = np.array([util(j, w[j], ALL, cal) - U0[j] for j in range(4)])
    print(cal, "fleet's right MDEN vs clean origin: utility", np.round(G, 4), "EV money", np.round(np.r_[100, W0[1:]] * (np.exp(G) - 1), 3))
# WTP for dropping N from MDEN
for cal, f in [("marg", lambda d, w: w * (1 - math.exp(-d / w))), ]:
    print("WTP drop N (marg):", [round(f(d, w), 4) for d, w in zip(s * E[:, 3], W0[1:])])
from wealth import v
print("WTP drop N (wta):", [round(w * (1 - math.exp(-(v(hA, w, 'wta') - v(hB, w, 'wta')))), 4)
      for hA, hB, w in zip(harms(ALL), harms(np.array([1,1,1,0])), W0[1:])])
print("WTA r3 under MDE (marg):", 2 * (math.exp(4 / 2) - 1), " WTA r3 under MD:", 2 * (math.exp(2 / 2) - 1))
