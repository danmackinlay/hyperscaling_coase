"""Compute dials on the wealth-effects row: fleet take-it-or-leave-it under the residents' right,
estimating each s_i with error sigma; limit (sigma->0) and finite budgets; linear vs log ('marg' and 'wta').
Also the residents' bloc take-it-or-leave-it limit (fleet held to no-deal utility) and the fleet's-right TIOLI limit."""
import math, itertools
import numpy as np
from scipy.stats import norm
from wealth import p, E, s, W0, SCHED, NAME, NONE, ALL, v

rng = np.random.default_rng(20261021)


def wta(i, x, si, cal):  # money resident i needs at endowment to accept schedule x, given sensitivity si
    h = max(si, 0) * (E[i] @ x)
    if cal == "lin":
        return h
    return W0[i + 1] * (math.exp(v(h, W0[i + 1], cal)) - 1)


def fleet_gain_u(m, cal):
    if cal == "lin":
        return m
    return math.log((100 + m) / 100) if m > -100 else -1e9


def res_gain_u(i, x, t, cal):
    h = s[i] * (E[i] @ x)
    if cal == "lin":
        return t - h
    return math.log((W0[i + 1] + t) / W0[i + 1]) - v(h, W0[i + 1], cal)


ZS = np.linspace(-1, 3.5, 91)


def fleet_offer(shat, sig, cal):
    """best (x, t) for a fleet with posterior s_i ~ N(shat_i, sig^2), per-resident markup z_i"""
    best = (None, None, 0.0)  # x, t, expected utility gain
    for x in SCHED:
        if not x.any():
            continue
        tz, pz = [], []
        for i in range(3):
            if E[i] @ x == 0:
                tz.append(np.zeros(1)); pz.append(np.ones(1)); continue
            if sig == 0:
                tz.append(np.array([wta(i, x, shat[i], cal)])); pz.append(np.ones(1)); continue
            tz.append(np.array([wta(i, x, shat[i] + z * sig, cal) for z in ZS])); pz.append(norm.cdf(ZS))
        # coordinate ascent over z_i
        idx = [0 if len(a) == 1 else len(ZS) // 2 for a in tz]
        for _ in range(6):
            for i in range(3):
                if len(tz[i]) == 1:
                    continue
                others_p = np.prod([pz[j][idx[j]] for j in range(3) if j != i])
                others_t = sum(tz[j][idx[j]] for j in range(3) if j != i)
                m = p @ x - others_t - tz[i]
                val = others_p * pz[i] * np.array([fleet_gain_u(mm, cal) if mm > -100 else -9 for mm in m])
                idx[i] = int(np.argmax(val))
        t = np.array([tz[i][idx[i]] for i in range(3)])
        pr = np.prod([pz[i][idx[i]] for i in range(3)])
        ev = pr * fleet_gain_u(p @ x - t.sum(), cal)
        if ev > best[2]:
            best = (x, t, ev)
    return best


def simulate(sig, cal, n=400):
    G = np.zeros((n, 4)); deal = np.zeros(n); sched = {}
    for k in range(n):
        shat = s + rng.normal(0, sig, 3) if sig > 0 else s.copy()
        x, t, _ = fleet_offer(shat, sig, cal)
        if x is None:
            continue
        need = np.array([wta(i, x, s[i], cal) for i in range(3)])
        if np.all(t >= need - 1e-12):
            deal[k] = 1
            G[k] = [fleet_gain_u(p @ x - t.sum(), cal)] + [res_gain_u(i, x, t[i], cal) for i in range(3)]
            sched[NAME(x)] = sched.get(NAME(x), 0) + 1
    eg = G.mean(0)
    meq = eg.copy() if cal == "lin" else np.r_[100 * (math.exp(eg[0]) - 1), W0[1:] * (np.exp(eg[1:]) - 1)]
    return deal.mean(), eg, meq, {k: v_ / n for k, v_ in sorted(sched.items(), key=lambda kv: -kv[1])}


def bloc_limit(cal):
    """residents' bloc TIOLI, perfect info: fleet held to zero gain (pays P(x)); bloc picks x and the
    internal split by the three residents' Nash product (one internal rule among several)."""
    from wealth import nbs, origin_utils, util
    best = None
    for x in SCHED:
        tot = p @ x
        # split tot among residents maximizing sum log gains; grid over shares
        bestx = None
        for a in np.linspace(0, tot, 121):
            for b in np.linspace(0, tot - a, 121):
                t = np.array([a, b, tot - a - b])
                g = [res_gain_u(i, x, t[i], cal) for i in range(3)]
                if min(g) <= 0:
                    continue
                val = sum(math.log(gg) for gg in g)
                if bestx is None or val > bestx[0]:
                    bestx = (val, t, g)
        if bestx:
            from scipy.optimize import minimize
            def f(ab):
                t = np.array([ab[0], ab[1], tot - ab[0] - ab[1]])
                g = [res_gain_u(i, x, t[i], cal) if W0[i+1] + t[i] > 0 else -1 for i in range(3)]
                return 1e9 if min(g) <= 0 else -sum(math.log(gg) for gg in g)
            r = minimize(f, bestx[1][:2], method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-12, maxiter=20000))
            t = np.array([r.x[0], r.x[1], tot - r.x[0] - r.x[1]])
            bestx = (-r.fun, t, [res_gain_u(i, x, t[i], cal) for i in range(3)])
        if bestx and (best is None or bestx[0] > best[1][0]):
            best = (x, bestx)
    x, (val, t, g) = best
    print(f"   bloc TIOLI limit ({cal}): schedule {NAME(x)}, transfers {np.round(t,2)}, resident gains {np.round(g,4)},"
          f" EV {np.round(W0[1:]*(np.exp(g)-1),3) if cal!='lin' else np.round(g,3)}; fleet gain 0")


if __name__ == "__main__":
    for cal in ["lin", "marg", "wta"]:
        print(f"\n=== fleet TIOLI, residents' right, {cal} ===")
        for sig in [1.0, 0.3, 0.1, 0.0]:
            d, eg, meq, sch = simulate(sig, cal, n=2000 if sig > 0 else 1)
            prod = np.prod(eg) if np.all(eg > 0) else 0.0
            print(f" sigma {sig}: deal {d:.3f}; E gains (u) {np.round(eg,4)}; product {prod:.3e};"
                  f" money-equiv {np.round(meq,3)} prod {np.prod(meq) if np.all(meq>0) else 0:.3g}; schedules {sch}")
        bloc_limit(cal)
