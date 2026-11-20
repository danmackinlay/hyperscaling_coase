"""Council role: estimation dial, random proposer by party, one-shot take-it-or-leave-it,
unanimity, base instance (4 slots, 3 residents, pie 6).

Company knows its profits p exactly; estimates each s_i with error sigma_f.
Residents know their own and each other's s_i; estimate each p_t with error sigma_N.
Council's rule 'open books': an audited publication of p with error sigma_a, which the
residents' agents combine with their own estimate.
Council's alternative 'assessed split': council estimates s and p with error sigma_a and
imposes the schedule maximising its estimated pie and t_i = h_i_hat + pie_hat/4.
"""
import itertools, sys
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm

p = np.array([4, 5.5, 4, 5.0])
e = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s_true = np.array([1, 1, 2.0])
X = np.array(list(itertools.product([0, 1], repeat=4)), dtype=float)  # 16 schedules
E = X @ e.T  # (16,3) exposure sums
P = X @ p  # profit
H = E * s_true  # harms (16,3)
PIE = P - H.sum(1)
ORD = -H[np.where((X == [1, 1, 1, 0]).all(1))[0][0]]  # ordinance levels (-1,-2.5,-4)


def post(signal, sig, prior_m, prior_sd):
    if prior_sd is None:
        return signal, sig
    prec = 1 / sig**2 + 1 / prior_sd**2
    return (signal / sig**2 + prior_m / prior_sd**2) / prec, prec**-0.5


def company_proposal(rng, sf, prior_sd=None, grid=None):
    """Return gains (company, r1, r2, r3) realised."""
    if sf == 0:
        b = PIE.argmax()
        return np.array([PIE[b], 0, 0, 0])
    sh = s_true + sf * rng.standard_normal(3)
    mu, om = post(sh, sf, 4 / 3, prior_sd)
    best = (-np.inf, None, None)
    for xi in range(16):
        Ex = E[xi]
        act = Ex > 0
        if not act.any():
            continue
        A = P[xi] - (mu * Ex).sum()
        c = om * Ex

        def negv(k):
            kk = np.zeros(3); kk[act] = k
            return -(A - (c * kk).sum()) * np.prod(norm.cdf(kk[act]))

        r = minimize(negv, np.ones(act.sum()), bounds=[(-5, 8)] * act.sum())
        kk = np.zeros(3); kk[act] = r.x
        t = (mu + kk * om) * Ex
        if grid:
            t = np.ceil(t / grid) * grid * act
            # local search on grid
            def val(t):
                pr = np.prod(norm.cdf((t[act] / Ex[act] - mu[act]) / om))
                return (P[xi] - t.sum()) * pr
            improved = True
            while improved:
                improved = False
                for i in np.where(act)[0]:
                    for dlt in (-grid, grid):
                        t2 = t.copy(); t2[i] += dlt
                        if val(t2) > val(t) + 1e-12:
                            t = t2; improved = True
            v = val(t)
        else:
            v = -r.fun
        if v > best[0]:
            best = (v, xi, t)
    _, xi, t = best
    acc = np.all(t >= H[xi] - 1e-12)
    if not acc:
        return np.zeros(4)
    return np.array([P[xi] - t.sum(), *(t - H[xi])])


DGRID = np.arange(0, 12, 0.005)


def resident_proposal(rng, sN, prior_sd=None, grid=None):
    """Proposer's own gain d, company's gain pie-d; others 0. Returns (company, d)."""
    if sN == 0:
        return PIE.max() - PIE.max(), PIE.max()
    ph = p + sN * rng.standard_normal(4)
    mu, om = post(ph, sN, 4.625, prior_sd)
    dg = DGRID if not grid else np.arange(0, 12, grid)
    best = (-np.inf, None, None)
    for xi in range(1, 16):
        m = X[xi] @ mu - H[xi].sum()
        sd = om * np.sqrt(X[xi].sum())
        ev = dg * norm.sf((dg - m) / sd)
        j = ev.argmax()
        if ev[j] > best[0]:
            best = (ev[j], xi, dg[j])
    _, xi, d = best
    if PIE[xi] >= d:
        return PIE[xi] - d, d
    return 0.0, 0.0


def bargain(sf, sN, n=2000, seed=0, prior_sd=None, grid=None):
    rng = np.random.default_rng(seed)
    g = np.zeros(4); dealrate = 0
    for _ in range(n):
        cp = company_proposal(rng, sf, prior_sd, grid)
        g += cp / 4
        dealrate += (np.any(cp != 0) or sf == 0) / 4
        for i in range(3):
            c, d = resident_proposal(rng, sN, prior_sd, grid)
            g[0] += c / 4; g[1 + i] += d / 4
            dealrate += (d > 0) / 4
    g /= n; dealrate /= n
    return g, dealrate


def assessed(sa, n=20000, seed=1):
    rng = np.random.default_rng(seed)
    G = np.zeros((n, 4))
    for r in range(n):
        sh = s_true + sa * rng.standard_normal(3)
        ph = p + sa * rng.standard_normal(4)
        Hh = E * sh; Ph = X @ ph
        pieh = Ph - Hh.sum(1)
        xi = pieh.argmax()
        t = Hh[xi] + pieh[xi] / 4
        G[r] = [P[xi] - t.sum(), *(t - H[xi])]
    return G


def report(name, g, dr):
    gm = np.prod(np.clip(g, 1e-12, None)) ** 0.25
    print(f"{name:42s} co {g[0]:5.2f} A {g[1]:5.2f} B {g[2]:5.2f} C {g[3]:5.2f} "
          f"| GM/1.5 {gm/1.5:4.2f} floor {g.min():5.2f} deal {dr:4.2f} res.share {g[1:].sum()/max(g.sum(),1e-9):4.2f}")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    print("ordinance levels", ORD, "pie max", PIE.max())
    for sf, sN in [(0, 0), (0.3, 0.3), (1, 1), (0.1, 0.1), (0.1, 0.316), (0.316, 1), (0.1, 1), (0, 0.3), (0, 1), (0.316, 0.1), (1, 0.316)]:
        g, dr = bargain(sf, sN, n)
        report(f"bargain sf={sf} sN={sN}", g, dr)
