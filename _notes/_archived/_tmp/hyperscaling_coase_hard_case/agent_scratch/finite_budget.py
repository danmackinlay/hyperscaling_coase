"""Finite budgets beside the limit, outside-option arm.

Switches on: outside option (reroute at 3/slot), finite budgets (fleet's estimate of each s_i has
error sigma/sqrt(c_f) in {1, 0.3, 0.1}; residents know p); k=3; transparent otherwise; linear money.
Protocol: the fleet, holding the outside option, makes a take-it-or-leave-it offer (schedule x,
transfers t_i) maximising its expected payoff given its posterior s_i ~ N(shat_i, sig^2); each
resident accepts iff t_i >= s_i e_i.x; if any refuses the fleet reroutes everything (6.5).
Failed deals count as zero gains for everyone (the fleet keeps its reroute value).
Also: symmetric Nash split with the fleet's pie estimate noisy, for contrast.
"""
import itertools, sys
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm

rng = np.random.default_rng(0)
p = np.array([4.0, 5.5, 4.0, 5.0]); e = np.array([[0.5, 0, 0.5, 1.0], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]]); s = np.array([1.0, 1.0, 2.0])
rr = np.maximum(p - 3, 0); d_F = rr.sum()
schedules = [np.array([1,1,0,0.]), np.array([1,1,1,0.]), np.array([0,1,0,0.]), np.array([0,1,1,0.]), np.array([1,0,0,0.])]  # the five with positive gain over reroute
label = lambda x: "".join(c for c, b in zip("MDEN", x) if b)


def best_offer(shat, sig, x):
    ex = e @ x  # exposure per resident
    mu = shat * ex; sd = np.maximum(sig * ex, 1e-9)
    # fleet payoff: rr.(1-x) + P(all accept)(p.x - sum t) + (1-P) rr.x ; choose t to maximise
    def obj(t):
        pa = np.prod(norm.cdf((t - mu) / sd))
        return -(pa * (p @ x - t.sum()) + (1 - pa) * (rr @ x))
    best = None
    for z in (0.3, 1.2):
        r = minimize(obj, mu + z * sd, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-9, "maxiter": 4000})
        if best is None or r.fun < best.fun: best = r
    return best.x, -best.fun + rr @ (1 - x)


def simulate(sig, draws=4000):
    gains = np.zeros((draws, 4)); deal = np.zeros(draws); eff = np.zeros(draws); scheds = {}
    for k in range(draws):
        shat = s + rng.normal(0, sig, 3)
        cand = [(best_offer(shat, sig, x), x) for x in schedules]
        (t, val), x = max(cand, key=lambda c: c[0][1])
        h = s * (e @ x)
        if np.all(t >= h - 1e-12):
            deal[k] = 1
            gains[k, 0] = p @ x + rr @ (1 - x) - t.sum() - d_F
            gains[k, 1:] = t - h
            eff[k] = label(x) in ("MD", "MDE")
            scheds[label(x)] = scheds.get(label(x), 0) + 1
        # else: fleet reroutes all, gains 0
    g = gains.mean(0)
    print(f"sigma={sig}: deal rate {deal.mean():.3f}; offered schedule (deals) {dict(sorted(scheds.items(), key=lambda kv: -kv[1])[:4])}; "
          f"expected gains counting failures as 0 (F; r1,r2,r3) {np.round(g,3)}; floor {g.min():.3f}; product {np.prod(np.maximum(g,0)):.2e}; "
          f"residents' share of realised gains {g[1:].sum()/max(g.sum(),1e-12):.3f}; expected pie {g.sum():.3f} of 1.5")


for sig in (1.0, 0.3, 0.1, 0.0):
    simulate(sig if sig > 0 else 1e-6, draws=600 if sig > 0 else 50)
print("limit (sigma -> 0): fleet offers each resident exactly its harm, runs MD or MDE, keeps all 1.5: gains (1.5; 0,0,0), product 0, floor 0")
