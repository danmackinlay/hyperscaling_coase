"""Collator re-runs for the hard-case round (2026-10-21).

Every number the session carries into the state table is recomputed here,
from the instance file alone. Sections are labelled by the row they serve.
"""
from itertools import product, permutations
from math import log, prod, sqrt, log2
import numpy as np

rng = np.random.default_rng(20261021)
SLOTS = "MDEN"
P = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
S = np.array([1, 1, 2.0])
W0 = {"f": 100.0, 0: 10.0, 1: 10.0, 2: 2.0}
X = [np.array(b) for b in product((0, 1), repeat=4)]


def harms(x, arb=False, s=S):
    h = s * (E @ x)
    if arb and x[0] and x[2]:
        h = h.copy(); h[2] += 1.5
    return h


def pie(x, arb=False, s=S):
    return P @ x - harms(x, arb, s).sum()


def lab(x):
    return "".join(c for c, b in zip(SLOTS, x) if b) or "none"


def best(xs, arb=False):
    return max(xs, key=lambda x: pie(x, arb))


def nash_product(g):
    g = list(g)
    if any(v < 0 for v in g):
        return float("nan")
    return prod(g)


print("=== BASELINE (all rows) ===")
for arb in (False, True):
    b = best(X, arb)
    print(f"{'arbitrary' if arb else 'parametric'}: best {lab(b)} pie {pie(b, arb):.2f}; "
          f"equal split {pie(b, arb)/4:.3f} each, product {(pie(b, arb)/4)**4:.4f}")
print("MDEN parametric pie", pie(np.ones(4, int)), "; arbitrary MDE pie", pie(np.array([1, 1, 1, 0]), True))

print("\n=== LANGUAGE: clause menus (rows language, enforcer, bundling) ===")
menus = {
    "four slots": X,
    "two A: {M,D}|{E,N}": [np.array([a, a, b, b]) for a in (0, 1) for b in (0, 1)],
    "two B: {M,D,E}|{N}": [np.array([a, a, a, b]) for a in (0, 1) for b in (0, 1)],
    "one: all or nothing": [np.zeros(4, int), np.ones(4, int)],
}
for nm, ms in menus.items():
    for arb in (False, True):
        b = best(ms, arb); v = pie(b, arb)
        print(f"  {nm:22s} {'arb' if arb else 'par'}: {lab(b):5s} pie {v:.2f} product {(v/4)**4:.3f}")

print("\n=== LANGUAGE: uniform per-head price (Krier club), parametric ===")
def club(x, arb=False):
    h = harms(x, arb); prof = P @ x
    bestp = None
    for t in np.linspace(h.max(), prof / 3, 20001):
        g = [prof - 3 * t] + list(t - h)
        npv = nash_product(g)
        if bestp is None or (npv == npv and npv > bestp[0]):
            bestp = (npv, t, g)
    return bestp
for sched in ([1, 1, 1, 0], [1, 1, 0, 0]):
    r = club(np.array(sched))
    print(f"  {lab(np.array(sched))}: best uniform t {r[1]:.3f}, gains {np.round(r[2],3)}, product {r[0]:.3f}; "
          f"bare clearing price {harms(np.array(sched)).max()} -> total {3*harms(np.array(sched)).max()} vs profit {P@np.array(sched)}")
print("  MDEN: 3*8 =", 3 * 8, "vs profit 18.5 -> no deal")

print("\n=== WEALTH: Nash product in log utility on pie 6 (MDE), rows wealth/incumbent/language ===")
def util_gain(party, money):
    return log(W0[party] + money) - log(W0[party])
# maximise sum log(util gains) over money gains summing to 6 (Lagrange via scipy-free bisection on FOC u'/u equal)
from scipy.optimize import minimize
def neg_logprod(g3):
    g = list(g3) + [6 - sum(g3)]
    if min(g) <= 0: return 1e9
    ug = [util_gain(0, g[0]), util_gain(1, g[1]), util_gain(2, g[2]), util_gain("f", g[3])]
    return -sum(log(u) for u in ug)
res = minimize(neg_logprod, [1.5, 1.5, 1.3], method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 20000})
g = list(res.x) + [6 - sum(res.x)]
ug = [util_gain(0, g[0]), util_gain(1, g[1]), util_gain(2, g[2]), util_gain("f", g[3])]
print(f"  money gains (f; r1,r2,r3) = ({g[3]:.3f}; {g[0]:.3f}, {g[1]:.3f}, {g[2]:.3f}); utility gains {np.round(ug,4)}; product {prod(ug):.3e}")
ug_eq = [util_gain(0, 1.5), util_gain(1, 1.5), util_gain(2, 1.5), util_gain("f", 1.5)]
print(f"  equal money split: utility gains {np.round(ug_eq,4)}, product {prod(ug_eq):.3e}; floor in utility = fleet {ug_eq[3]:.4f}")
# money-harm reading: ordering of schedules by utility Nash product equals ordering by pie?
print("  fleet-holds-right origin under money harm: resident 3 wealth at MDEN =", W0[2] - harms(np.ones(4, int))[2])

print("\n=== OUTSIDE OPTION (row scale) ===")
reroute = np.maximum(P - 3, 0)
print("  reroute value per slot", reroute, "total", reroute.sum())
vals = []
for x in X:
    V = P @ x - harms(x).sum() + reroute[x == 0].sum()
    vals.append((lab(x), V, V - 6.5))
for n, V, gpie in sorted(vals, key=lambda r: -r[1])[:4]:
    print(f"  {n:5s} joint value {V:.2f} gain over reroute {gpie:.2f}")
print(f"  equal split of 1.5: {1.5/4:.3f} each, product {(1.5/4)**4:.4f}")

print("\n=== k=2 coalition values and core (rows enforcer, incumbent, pact) ===")
for pair in [(0, 1), (0, 2), (1, 2)]:
    bx = max(X, key=lambda x: P @ x - harms(x)[list(pair)].sum())
    v = P @ bx - harms(bx)[list(pair)].sum()
    excl = [i for i in range(3) if i not in pair][0]
    print(f"  fleet+residents {tuple(p+1 for p in pair)}: {lab(bx)} value {v:.1f}; excluded resident {excl+1} at {-harms(bx)[excl]:.1f}")
print("  sum of pair values 13.5+8.5+7.5 =", 13.5 + 8.5 + 7.5, "; 2*6 + u_F >= 29.5 -> u_F >= 17.5 > 6: core empty")
print("  consents compete to zero: (18.5; -2, -3, -8); arbitrary: resident 3 at", -harms(np.ones(4, int), True)[2])
# optimist's boycott threshold at k=2: fleet breaks iff 18.5 - 5 - 3/(1-d) > 1.5/(1-d)  <=> d < 2/3
for d in (0.5, 0.8, 0.95):
    print(f"  delta {d}: one-shot break vs grim boycott: {18.5-5-3/(1-d):.2f} vs stay {1.5/(1-d):.2f} -> {'breaks' if 18.5-5-3/(1-d) > 1.5/(1-d) else 'holds (if boycott credible)'}")
# fleet's own reneging at k=3 (row 9 logic): premium g per resident sustainable iff delta >= g/2
print("  k=3 fleet reneging bound: 1.5 each needs delta >= 0.75; at delta 0.5 best product 3.0 at (3;1,1,1)")

print("\n=== SYBIL (row incumbent) ===")
for m in (1, 2, 3, 10):
    share = 6 * m / (m + 3)
    print(f"  resident 2 as {m} agents: household {share:.2f}; per-person product {(6/(m+3))**m * (6/(m+3))**0 if False else ''}", end="")
    others = 6 / (m + 3)
    print(f" fleet/r1/r3 each {others:.3f}; product over four households {share*others**3:.2f}")

print("\n=== BUNDLING reopening cost (row bundling) ===")
for d in (0.5, 0.8, 0.95, 1.0):
    print(f"  delta {d}: drop E via bundle 1.5 - {d}*1.25 = {1.5 - d*1.25:.4f}; slot-by-slot own quarter of E = 0.25; "
          f"extra deadweight (1-d)*1.25 = {(1-d)*1.25:.4f}")

print("\n=== BITS: Segal 2007 Cor.4 bound (K-1) log2(1+1/(N-1)) (row bits) ===")
for m in (4, 8, 24, 48):
    K = 2 ** m
    print(f"  m={m}: N=4 -> {(K-1)*log2(1+1/3):.3g} bits; N=2 -> {(K-1):.3g} bits")

print("\n=== REMEDIATION (rows incumbent, optimist) ===")
Eins = E.copy(); Eins[2] *= 0.5
h_ins = S * (Eins @ np.ones(4, int))
print(f"  insulate resident 3, run MDEN: harms {h_ins}, pie {18.5 - h_ins.sum() - 2:.2f}; equal split {(18.5-h_ins.sum()-2)/4:.3f}, product {((18.5-h_ins.sum()-2)/4)**4:.2f}")
print("  at MDE, insulating resident 3 saves", harms(np.array([1,1,1,0]))[2] - (S*(Eins@np.array([1,1,1,0])))[2], "against cost 2")

print("\n=== SCALE: Mailath-Postlewaite limit thresholds (row scale) ===")
print("  top-of-support harm at proportional width a: MDE feasible iff 7.5(1+a) <= 13.5 -> a <=", round(13.5/7.5 - 1, 3))
print("  bounded residual +-w: 7.5 + 5.5w <= 13.5 -> w <=", round(6/5.5, 3), "; with reroute: MD 4.5+3.5w <= 6 -> w <=", round(1.5/3.5, 3))

print("\n=== FINITE BUDGET: fleet take-it-or-leave-it, parametric, k=3 (rows budgets, incumbent, wealth, bundling) ===")
def tioli_fleet(sigma, draws=40000, arb_truth=False, model_arb=False):
    """Fleet sees s_i + N(0, sigma^2), flat prior; chooses schedule and per-resident offers maximising
    expected profit given posterior N(shat_i, sigma^2) on s_i; resident i accepts iff offer >= true harm."""
    from scipy.stats import norm
    gains = np.zeros(4); deals = 0; eff = 0; night = 0
    for _ in range(draws):
        shat = S + rng.normal(0, sigma, 3)
        bestv = -1e9; bestx = None; bestoff = None
        for x in X:
            if not x.any(): continue
            ex = E @ x  # exposure per resident
            # offer o_i; acceptance prob Phi((o_i - shat_i*ex_i)/(sigma*ex_i)); choose o_i maximising (P.x - sum o) * prod Phi
            # separable approx: optimise each margin z_i on grid of standardised offsets
            zs = np.linspace(-1, 4, 41)
            # evaluate joint expected profit on a coarse grid per resident (independent FOC), iterate
            off = shat * ex + 1.0 * sigma * ex
            for it in range(3):
                for i in range(3):
                    if ex[i] == 0:
                        off[i] = 0.0; continue
                    bestz, bestval = None, -1e9
                    for z in zs:
                        o = off.copy(); o[i] = shat[i]*ex[i] + z*sigma*ex[i]
                        pacc = np.prod([norm.cdf((o[j]-shat[j]*ex[j])/(sigma*ex[j])) if ex[j] > 0 else 1.0 for j in range(3)])
                        val = (P @ x - o.sum()) * pacc
                        if val > bestval: bestval, bestz = val, z
                    off[i] = shat[i]*ex[i] + bestz*sigma*ex[i]
            pacc = np.prod([norm.cdf((off[j]-shat[j]*ex[j])/(sigma*ex[j])) if ex[j] > 0 else 1.0 for j in range(3)])
            val = (P @ x - off.sum()) * pacc
            if val > bestv: bestv, bestx, bestoff = val, x, off.copy()
        htrue = harms(bestx, arb_truth)
        if np.all(bestoff >= htrue - 1e-12):
            deals += 1
            gains += np.array([P @ bestx - bestoff.sum(), *(bestoff - htrue)])
            if lab(bestx) == ("MD" if arb_truth else "MDE"): eff += 1
            if bestx[3]: night += 1
    g = gains / draws
    return g, deals / draws, eff / draws, night / draws
for sigma in (1.0, 0.3, 0.1):
    g, dr, ef, ni = tioli_fleet(sigma, draws=600)
    print(f"  sigma {sigma}: deal {dr:.3f}, eff {ef:.3f}, night run {ni:.3f}, gains (f; r) ({g[0]:.3f}; {g[1]:.3f}, {g[2]:.3f}, {g[3]:.3f}), "
          f"residents' take {g[1:].sum():.3f}, pie {g.sum():.2f}, product {nash_product(g):.4f}, floor {g.min():.3f}")
print("  arbitrary truth, additive (misspecified) model:")
for sigma in (1.0, 0.3, 0.1):
    g, dr, ef, ni = tioli_fleet(sigma, draws=600, arb_truth=True)
    print(f"  sigma {sigma}: deal {dr:.3f}, MD chosen {ef:.3f}, gains ({g[0]:.3f}; {g[1]:.3f}, {g[2]:.3f}, {g[3]:.3f}), product {nash_product(g):.4f}")

print("\n=== FINITE BUDGET: bits-row Nash-split protocol (fleet estimates, pays estimated harm + quarter of estimated pie; veto if true gain < 0) ===")
def nash_proto(sigma, draws=40000, arb_truth=False):
    gains = np.zeros(4); deals = 0
    for _ in range(draws):
        shat = S + rng.normal(0, sigma, 3)
        bx = max(X, key=lambda x: pie(x, False, shat))
        est_pie = pie(bx, False, shat)
        if est_pie <= 0: continue
        offers = shat * (E @ bx) + est_pie / 4
        htrue = harms(bx, arb_truth)
        if np.all(offers - htrue >= 0):
            deals += 1
            gains += np.array([P @ bx - offers.sum(), *(offers - htrue)])
    g = gains / draws
    return g, deals / draws
for arb in (False, True):
    print(f"  truth {'arbitrary' if arb else 'parametric'}:")
    for sigma in (1.0, 0.3, 0.1, 0.01):
        g, dr = nash_proto(sigma, draws=20000, arb_truth=arb)
        print(f"    eps {sigma}: deal {dr:.3f}, gains ({g[0]:.3f}; {g[1]:.3f}, {g[2]:.3f}, {g[3]:.3f}), pie {g.sum():.2f}, product {nash_product(g):.4f}, floor {g.min():.3f}")
