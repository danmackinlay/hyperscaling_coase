"""Criterion recomputation for the river table. Run: uv run python -I <this file>.

Payoffs are on the model's own scale, u_f = pi*x - sum(t), u_i = t_i - h_i*x,
so the clean river with no transfers is (0;0,0,0) under every rule.
Order of parties in every vector: (factory, r1[h=2], r2[h=3], r3[h=9]).
An outcome is a list of (probability, payoff-vector) pairs.
"""

import math

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import norm

H = np.array([2.0, 3.0, 9.0])
RNG = np.random.default_rng(0)
N_MC = 400_000


def expect(outcome):
    return sum(p * np.asarray(v, float) for p, v in outcome)


def floor_ex_ante(outcome):
    return float(expect(outcome).min())


def floor_ex_post(outcome):
    return float(sum(p * min(v) for p, v in outcome))


def leximin(outcome):
    return tuple(round(x, 3) for x in sorted(expect(outcome)))


def nash(outcome):
    e = expect(outcome)
    return -math.inf if (e < -1e-12).any() else float(np.prod(np.clip(e, 0, None)))


def below(outcome):
    """Probability that someone ends strictly below the no-deal payoff 0."""
    return float(sum(p for p, v in outcome if min(v) < -1e-9))


def kolm_pollak(outcome, alpha=1.0):
    e = expect(outcome)
    return float(-math.log(np.mean(np.exp(-alpha * e))) / alpha)


def total(outcome):
    return float(expect(outcome).sum())


def report(label, outcome, extra=""):
    e = expect(outcome)
    print(
        f"{label:<44} E[u]=({e[0]:.3f};{e[1]:.3f},{e[2]:.3f},{e[3]:.3f}) "
        f"floor={floor_ex_ante(outcome):.3f} expost={floor_ex_post(outcome):.3f} "
        f"nash={nash(outcome):.4g} P(below)={below(outcome):.4f} "
        f"KP1={kolm_pollak(outcome, 1):.3f} KP.5={kolm_pollak(outcome, .5):.3f} "
        f"tot={total(outcome):.3f} {extra}"
    )


def mc_outcome(fail_prob, deal_vectors):
    """Monte Carlo outcome: failures at zero, deals as equal-weight samples."""
    w = (1 - fail_prob) / len(deal_vectors)
    return [(fail_prob, (0, 0, 0, 0))] + [(w, v) for v in deal_vectors]


# --- Row 1: take-it-or-leave-it by the factory, harms estimated with error sigma.
# NB rows 1-2: the printed expost= field is taken on the collapsed mean vector, so it
# repeats the ex-ante floor; the ex-post floor is the bracketed Monte Carlo figure.
def factory_profit(m, s):
    z = m / s
    return norm.cdf(z) ** 3 * (6 - 3 * m) - 3 * norm.cdf(z) ** 2 * s * norm.pdf(z)


def row1(s, m=None):
    if m is None:
        m = minimize_scalar(lambda x: -factory_profit(x, s), bounds=(0, 2), method="bounded").x
    eps = RNG.normal(0, s, size=(N_MC, 3))
    acc = (eps >= -m).all(axis=1)
    d = eps[acc]
    vec = np.column_stack([6 - 3 * m - d.sum(axis=1), d + m])
    p_deal = acc.mean()
    # summarise analytically-weighted: use sample mean via an outcome with chunked vectors
    out = [(1 - p_deal, (0, 0, 0, 0))]
    # collapse samples into an outcome with the exact ex-ante means and ex-post floor
    out_mean = vec.mean(axis=0)
    expost_floor = p_deal * vec.min(axis=1).mean()
    below_p = p_deal * (vec.min(axis=1) < 0).mean()
    return m, p_deal, out + [(p_deal, tuple(out_mean))], expost_floor, below_p


print("== Row 1: TIOLI by factory (estimation dial) ==")
for s in [1.5, 0.5, 0.2, 0.05, 0.01]:
    m, pd, out, ef, bp = row1(s)
    report(f"sigma={s} m*={m:.3f} deal={pd:.4f}", out,
           f"[expost floor (MC)={ef:.4f} P(below,MC)={bp:.4f}]")
# margins backed out from the row's deal rates, P=Phi(m/sigma)^3
for s, rate in [(1.5, 0.34), (0.01, 0.9985)]:
    m = s * norm.ppf(rate ** (1 / 3))
    _, pd, out, ef, bp = row1(s, m)
    report(f"sigma={s} m(backed)={m:.4f} deal={pd:.4f}", out,
           f"[expost floor (MC)={ef:.4f} P(below,MC)={bp:.4f}]")


# --- Row 2: take-it-or-leave-it by the residents, pi estimated with error sigma.
def resid_gain(m, s):
    z = m / s
    return norm.cdf(z) * (6 - m) - s * norm.pdf(z)


def row2(s, split):
    m = minimize_scalar(lambda x: -resid_gain(x, s), bounds=(0, 6), method="bounded").x
    eps = RNG.normal(0, s, size=N_MC)
    acc = eps <= m
    d = eps[acc]
    g_r = 6 + d - m
    vec = np.column_stack([m - d, np.outer(g_r, split)])
    p_deal = acc.mean()
    out = [(1 - p_deal, (0, 0, 0, 0)), (p_deal, tuple(vec.mean(axis=0)))]
    ef = p_deal * vec.min(axis=1).mean()
    bp = p_deal * (vec.min(axis=1) < 0).mean()
    return m, p_deal, out, ef, bp


print("\n== Row 2: TIOLI by residents (estimation dial) ==")
for name, split in [("equal gains", np.array([1, 1, 1]) / 3), ("prop. to harm", H / H.sum())]:
    for s in [1.5, 0.01]:
        m, pd, out, ef, bp = row2(s, split)
        report(f"{name} sigma={s} m*={m:.3f} deal={pd:.4f}", out,
               f"[expost floor={ef:.4f} P(below)={bp:.4f}]")


# --- Row 3: haggling, all known (capability asymmetry).
print("\n== Row 3: haggling, all known ==")
report("symmetric agents", [(1, (1.5, 1.5, 1.5, 1.5))])
d = 0.6
report(f"factory better agent, takes d={d} evenly", [(1, (1.5 + d, 1.5 - d / 3, 1.5 - d / 3, 1.5 - d / 3))])
report(f"resident 1 weaker agent, loses d={d}", [(1, (1.5 + d, 1.5 - d, 1.5, 1.5))])


# --- Row 4: private harms, uninformed factory offers; speed dial (Coase conjecture).
print("\n== Row 4: private harms, H_i ~ U[h_i-a, h_i+a] ==")
for a in [1.0, 1.5, 1.75, 2.0]:
    y = min((6 + 3 * a) / 4, 2 * a)
    pa = y / (2 * a)
    f_slow = pa ** 3 * (6 + 3 * a - 3 * y)
    r_slow = (y ** 2 / (4 * a)) * pa ** 2
    slow = [(1 - pa ** 3, (0, 0, 0, 0)), (pa ** 3, (f_slow / pa ** 3, r_slow / pa ** 3, r_slow / pa ** 3, r_slow / pa ** 3))]
    # ex-post floor for slow: residents' realised gain uniform on [0,y] given acceptance
    U = RNG.uniform(0, y, size=(N_MC, 3))
    ef_slow = pa ** 3 * np.minimum(U.min(axis=1), 6 + 3 * a - 3 * y).mean()
    fast_f = max(6 - 3 * a, 0.0)
    fast = [(1, (fast_f, a, a, a))]
    U2 = RNG.uniform(0, 2 * a, size=(N_MC, 3))
    ef_fast = np.minimum(U2.min(axis=1), fast_f).mean()
    report(f"a={a} slow (one-shot) y*={y:.3f} deal={pa**3:.3f}", slow, f"[expost floor={ef_slow:.3f}]")
    report(f"a={a} fast offers (limit)", fast, f"[expost floor={ef_fast:.3f}]")


# --- Row 5: both commit, sealed, unconditional (Ellingsen-Miettinen 2008).
print("\n== Row 5: sealed commitment, residents' bloc splits its take equally ==")
B = (1.5, 1.5, 1.5, 1.5)
report("costly commitment: nobody commits", [(1, B)])
for q in [0.5, 0.9, 0.99]:
    out = [(q * q, (0, 0, 0, 0)), (q * (1 - q), (6, 0, 0, 0)), (q * (1 - q), (0, 2, 2, 2)), ((1 - q) ** 2, B)]
    report(f"cheap commitment, q={q}", out)
for name, v in [("q=1 outcome: conflict", (0, 0, 0, 0)), ("q=1 outcome: factory takes all", (6, 0, 0, 0)),
                ("q=1 outcome: residents take all", (0, 2, 2, 2))]:
    report(name, [(1, v)])


# --- Row 6: publication in sequence (speed dial).
print("\n== Row 6: publication in sequence ==")
report("equal speed: coin flip for first", [(0.5, (6, 0, 0, 0)), (0.5, (0, 2, 2, 2))])
report("factory faster (one principal)", [(1, (6, 0, 0, 0))])
report("residents' bloc faster", [(1, (0, 2, 2, 2))])


# --- Row 7 and 9: sets of equilibria at pi=20, k=3 (per period for row 9).
print("\n== Rows 7, 9: equilibrium sets ==")
for name, v in [("best: equal split", B), ("worst: no deal", (0, 0, 0, 0)),
                ("worst deal: factory takes all", (6, 0, 0, 0)), ("worst deal: residents take all, equal", (0, 2, 2, 2)),
                ("residents take all, prop. to harm", (0, *(6 * H / H.sum()))),
                ("tilt d=0.6 to factory (row 9)", (2.1, 1.3, 1.3, 1.3))]:
    report(name, [(1, v)])


# --- Row 8: unanimity with binding declarations: delay as pie fraction rho (not from the paper).
print("\n== Row 8: unanimity delay, symmetric, pie fraction rho ==")
for rho in [1.0, 0.8, 0.5]:
    report(f"rho={rho}", [(1, tuple(1.5 * rho for _ in range(4)))])
report("k=2 instead (factory buys r1,r2 at harm+1.5)", [(1, (12, 1.5, 1.5, -9))],
       "[illustrative: r3 uncompensated]")


# --- Row 10: k=1, pi=10, the race.
print("\n== Row 10: k=1, pi=10 ==")
eps = 0.01
report("race (r1 signs for eps)", [(1, (10 - eps, eps - 2, -3, -9))])
report("pact imposed: clean river", [(1, (0, 0, 0, 0))])
# Tullock lottery contest, stakes Vf=10 against residents
for name, vr in [("contest, residents as one bloc (needs the pact)", 14.0), ("contest, only r3 spends", 9.0)]:
    vf = 10.0
    xf = vf ** 2 * vr / (vf + vr) ** 2
    xr = vf * vr ** 2 / (vf + vr) ** 2
    p_poll = vf / (vf + vr)
    uf = vf * p_poll - xf
    if vr == 14.0:  # bloc spending split in proportion to harm
        ur = -H * p_poll - xr * H / H.sum()
    else:
        ur = -H * p_poll - np.array([0, 0, xr])
    report(name, [(1, (uf, *ur))], f"[xf={xf:.3f} xr={xr:.3f} P(pollute)={p_poll:.3f}]")


# --- Row 11: one side adapts, the other is fixed.
print("\n== Row 11: adaptation ==")
report("symmetric", [(1, B)])
report("residents adapt, factory rigid", [(1, (6, 0, 0, 0))])
report("factory adapts, residents rigid (equal)", [(1, (0, 2, 2, 2))])


# --- Row 12: liability rule.
print("\n== Row 12: liability rule ==")
report("compensatory damages, pi=20", [(1, (6, 0, 0, 0))])
report("compensatory damages, pi=10 (no pollution)", [(1, (0, 0, 0, 0))])
report("schedule h_i+1.5, pi=20", [(1, B)])
for s in [1.5, 0.01]:
    e = RNG.normal(0, s, size=(N_MC, 3))
    vec = np.column_stack([6 - e.sum(axis=1), e])
    ok = vec[:, 0] >= 0  # factory pollutes only if damages <= profit
    vec = np.where(ok[:, None], vec, 0)
    print(f"  court error sigma={s}: E[u]={vec.mean(axis=0).round(3)} expost floor={vec.min(axis=1).mean():.4f} "
          f"P(below)={(vec.min(axis=1) < 0).mean():.3f}")


# --- Blind-spot checks for the defence.
print("\n== Blind-spot checks ==")
for name, v in [("clean river", (0, 0, 0, 0)), ("pi=20 deal, all to factory", (6, 0, 0, 0)),
                ("pi=20 deal, equal", B), ("pi=20 equal transfers 18.5/3 (k=2 style)", (1.5, 18.5 / 3 - 2, 18.5 / 3 - 3, 18.5 / 3 - 9)),
                ("pi=10 pollution, r1 bought at 2.5, others not", (7.5, 0.5, -3, -9)),
                ("pi=10 k=0 deal, residents pay (1,2,7)", (10, -1, -2, -7))]:
    vv = np.array(v, float)
    raw = float(np.prod(vv))
    print(f"  {name:<48} min={vv.min():.3f} raw-Nash={raw:.3g} trunc-Nash={nash([(1, v)]):.4g} "
          f"KP1={kolm_pollak([(1, v)]):.3f} below={below([(1, v)]):.0f} lex={leximin([(1, v)])}")
