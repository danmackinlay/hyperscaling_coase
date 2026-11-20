import time

import numpy as np
from scipy.optimize import minimize

import model as M

# Anchor 1: worked case full info
s = np.array([[1.0], [1.0], [2.0]])
m = np.array([1.0])
print("full info worked:", M.full_info(s, m, False), M.full_info(s, m, True))

# Anchor 2: rule A sigma=0
rng = np.random.default_rng(1)
N = 2000
s = rng.uniform(0.5, 2.5, (3, N))
m = rng.uniform(0.6, 1.4, N)
for ins in (False, True):
    c, h = M.offer_maker(s, m, ins, -1, s, m, 0.0)
    fi = M.full_info(s, m, ins)
    print("A sigma0 ins", ins, "max|comp-fi|", np.abs(c - fi).max(), "max|hh|", np.abs(h).max())
    # household seat sigma 0 likewise
    for j in range(3):
        c2, h2 = M.offer_maker(s, m, ins, j, s, m, 0.0)
        print("  seat", j, np.abs(h2[j] - fi).max(), np.abs(c2).max(), np.abs(np.delete(h2, j, 0)).max())

# Optimiser check against direct numerical maximisation for random slot problems
def check(sigma, maker, n=200, seed=2):
    rng = np.random.default_rng(seed)
    s = rng.uniform(0.5, 2.5, (3, n))
    m = rng.uniform(0.6, 1.4, n)
    sig = s + sigma * rng.standard_normal((3, n))
    sm = m + 0.4 * sigma * rng.standard_normal(n)
    hb = [M.Belief(sig[i], sigma, 0.5, 2.5) for i in range(3)]
    mb = M.Belief(sm, 0.4 * sigma, 0.6, 1.4)
    worst = 0
    for t in range(4):
        w = M.E[:, t] * np.array([1, 0.5, 1])  # insulate Bob, arbitrary
        others = [i for i in range(3) if w[i] > 0 and i != maker]
        ws = [w[i] for i in others]
        if maker < 0:
            ev, rs, d, off = M.solve_slot(m * M.P[t], ws, [hb[i] for i in others])
        else:
            cj = s[maker] * w[maker]
            ev, rs, d, off = M.solve_slot(None, ws, [hb[i] for i in others], mb, M.P[t], cj)
        for k in range(n):
            def neg(x):
                rr = x[: len(others)]
                lp = sum(hb[i].logF(np.array([rr[q]]))[0] - 0 for q, i in enumerate(others))
                if maker < 0:
                    mg = m[k] * M.P[t] - sum(ws[q] * rr[q] for q in range(len(others)))
                else:
                    dd = x[-1]
                    mg = dd * M.P[t] - sum(ws[q] * rr[q] for q in range(len(others))) - cj[k]
                    lp += mb_k.logS(np.array([dd]))[0]
                return -np.exp(lp) * mg
            hbk = [M.Belief(np.array([sig[i, k]]), sigma, 0.5, 2.5) for i in range(3)]
            mb_k = M.Belief(np.array([sm[k]]), 0.4 * sigma, 0.6, 1.4)
            hb_save = hb
            hb = hbk
            best = 0.0
            # dense multistart + polish
            for start in np.linspace(0.6, 2.4, 7):
                x0 = [start] * len(others) + ([1.0] if maker >= 0 else [])
                bnds = [(0.5, 2.5)] * len(others) + ([(0.6, 1.4)] if maker >= 0 else [])
                res = minimize(neg, x0, method="L-BFGS-B", bounds=bnds)
                res = minimize(neg, res.x, method="Nelder-Mead", bounds=bnds,
                               options=dict(xatol=1e-10, fatol=1e-12, maxiter=4000))
                best = max(best, -res.fun)
            hb = hb_save
            worst = max(worst, best - ev[k])
            if best - ev[k] > 1e-6:
                print("  gap", sigma, maker, t, k, best, ev[k])
    print(f"sigma={sigma} maker={maker}: max(scipy EV - bisection EV) = {worst:.2e}")

t0 = time.time()
for sigma in (np.inf, 0.3, 0.1):
    for maker in (-1, 0, 2):
        check(sigma, maker, n=40)
print("time", time.time() - t0)
