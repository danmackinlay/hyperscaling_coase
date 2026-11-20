"""Finite budgets: fleet TIOLI, bundled vs slot-by-slot. Fleet estimates each s_i with N(0, sigma) error.
Fleet maximises expected profit given its estimate (flat prior). Per schedule the problem is
  max_z (c - sigma * sum_i z_i E_i) * prod_i Phi(z_i),  c = profit - sum_i shat_i E_i,
so the optimum depends on the draw only through c; tabulate z*(c) per schedule.
"""
import itertools
import numpy as np
from scipy.stats import norm

SLOTS = "MDEN"
p = np.array([4.0, 5.5, 4.0, 5.0])
e = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1.0, 1.0, 2.0])
SCHEDULES = [np.array(x) for x in itertools.product([0, 1], repeat=4) if sum(x) > 0]
ZGRID = np.linspace(-1.5, 4.0, 56)
Z3 = np.array(list(itertools.product(ZGRID, ZGRID, ZGRID)))  # 56^3 ~ 175k
PHI = norm.cdf(Z3)


def name(x):
    return "".join(c for c, b in zip(SLOTS, x) if b)


def pie(x):
    return p @ x - (s * (e @ x)).sum()


def table(E, sig, cgrid):
    """For exposure vector E, return best value and z* for each c in cgrid."""
    mask = E > 0
    Z = Z3.copy(); Z[:, ~mask] = 0.0
    PH = np.where(mask, PHI, 1.0).prod(1)
    cost = sig * (Z * E).sum(1)
    # dedupe rows where masked coords vary
    vals = (cgrid[:, None] - cost[None, :]) * PH[None, :]
    idx = vals.argmax(1)
    return vals[np.arange(len(cgrid)), idx], Z[idx]


rng = np.random.default_rng(1)
NSIM = 20000
cgrid = np.arange(-6, 20.0001, 0.02)

for sig in (1.0, 0.3, 0.1):
    eps = rng.normal(0, sig, size=(NSIM, 3))
    shat = s + eps
    # per-schedule tables
    tabs = {}
    for x in SCHEDULES:
        E = e @ x
        tabs[name(x)] = (E, p @ x) + table(E, sig, cgrid)
    # ---- bundle: pick best schedule per draw
    gains_b = np.zeros((NSIM, 4)); pie_b = np.zeros(NSIM); deal_b = np.zeros(NSIM); nrun_b = np.zeros(NSIM)
    bestval = np.full(NSIM, -np.inf); bestname = np.empty(NSIM, dtype=object)
    bestt = np.zeros((NSIM, 3))
    for nm, (E, prof, vals, Zs) in tabs.items():
        c = prof - shat @ E
        ci = np.clip(np.round((c - cgrid[0]) / 0.02).astype(int), 0, len(cgrid) - 1)
        v = vals[ci]
        better = v > bestval
        bestval[better] = v[better]
        bestname[better] = nm
        t = shat * E + Zs[ci] * sig * E
        bestt[better] = t[better]
    for n in range(NSIM):
        nm = bestname[n]
        if bestval[n] <= 0:
            continue
        E, prof = tabs[nm][0], tabs[nm][1]
        t = bestt[n]
        if (t >= s * E - 1e-9).all():
            x = np.array([1 if ch in nm else 0 for ch in SLOTS])
            gains_b[n, 0] = prof - t.sum(); gains_b[n, 1:] = t - s * E
            pie_b[n] = pie(x); deal_b[n] = 1; nrun_b[n] = 1 if "N" in nm else 0
    # ---- slot by slot
    gains_s = np.zeros((NSIM, 4)); pie_s = np.zeros(NSIM); nrun_s = np.zeros(NSIM); nslots = np.zeros(NSIM)
    for tslot in range(4):
        x = np.zeros(4, int); x[tslot] = 1
        E, prof, vals, Zs = tabs[name(x)]
        c = prof - shat @ E
        ci = np.clip(np.round((c - cgrid[0]) / 0.02).astype(int), 0, len(cgrid) - 1)
        v = vals[ci]
        t = shat * E + Zs[ci] * sig * E
        offer = v > 0
        acc = offer & (t >= s * E - 1e-9).all(1)
        gains_s[acc, 0] += prof - t[acc].sum(1)
        gains_s[acc, 1:] += t[acc] - s * E
        pie_s[acc] += pie(x); nslots[acc] += 1
        if tslot == 3:
            nrun_s[acc] = 1
    gb = gains_b.mean(0); gs = gains_s.mean(0)
    from collections import Counter
    print(f"\n-- sigma={sig}")
    print(f"  bundle schedules proposed: {Counter(bestname).most_common(4)}")
    print(f"  bundled : deal rate {deal_b.mean():.3f}  P(N runs) {nrun_b.mean():.3f}  E[pie] {pie_b.mean():.3f}  "
          f"E[gains] {gb.round(3)}  product {np.prod(gb):.4f}  floor {gb.min():.3f}  "
          f"ex-post floor {gains_b.min(1).mean():.3f}  residents' share {gb[1:].sum()/pie_b.mean():.3f}")
    print(f"  slotwise: slots/run {nslots.mean():.2f}  P(N runs) {nrun_s.mean():.3f}  E[pie] {pie_s.mean():.3f}  "
          f"E[gains] {gs.round(3)}  product {np.prod(gs):.4f}  floor {gs.min():.3f}  "
          f"ex-post floor {gains_s.min(1).mean():.3f}  residents' share {gs[1:].sum()/pie_s.mean():.3f}")
print("\n  Limit sigma->0: both (6; 0,0,0), product 0, floor 0, residents' share 0.")
