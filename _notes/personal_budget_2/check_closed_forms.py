"""Numerical checks for _notes/personal_budget_2/draft.md, plus the wealth simulation behind its table.

Every closed form quoted in the article is checked here against a direct
numerical solution. Run from the repository root:
  uv run --no-project --with numpy --with scipy python _notes/personal_budget_2/check_closed_forms.py

Notation (matches the article):
  S_m   surplus of matter m, a bilateral bargain between principals i and j
  c_im  compute principal i spends on matter m
  r     decisiveness of compute in the contest success function
        share_i = c_i^r / (c_i^r + c_j^r)
  C_i   hard compute budget;  w_i wealth;  p price of compute;  R gross return
        on object-level capital;  a_i = 1/lambda_i the "strength" (inverse
        shadow price of compute).
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq, minimize

rng = np.random.default_rng(20261119)


# ---------------------------------------------------------------- utilities
def gini(x: np.ndarray) -> float:
    x = np.sort(np.asarray(x, dtype=float))
    n = len(x)
    if x.sum() <= 0:
        return 0.0
    return float((2 * np.arange(1, n + 1) - n - 1).dot(x) / (n * x.sum()))


def random_matters(n: int, per_head: int, sigma: float = 0.5):
    """Random bilateral matters, about `per_head` per principal, lognormal stakes with mean 1.
    Every principal opens per_head/2 matters, so nobody is left with none."""
    half = max(per_head // 2, 1)
    i = np.repeat(np.arange(n), half)
    j = (i + rng.integers(1, n, len(i))) % n  # never i itself
    s = rng.lognormal(-0.5 * sigma**2, sigma, len(i))
    return i, j, s


def shares(a, i, j, r):
    ai, aj = a[i] ** r, a[j] ** r
    return ai / (ai + aj)


def spend(a, i, j, s_stake, r, n):
    """Equilibrium compute per principal implied by strengths a (KKT conditions)."""
    sh = shares(a, i, j, r)
    core = r * s_stake * sh * (1 - sh)
    ci, cj = a[i] * core, a[j] * core
    tot = np.bincount(i, ci, n) + np.bincount(j, cj, n)
    return tot, ci, cj, sh


def solve_hard_budget(i, j, s_stake, budget, r, cap=None, iters=20000, tol=1e-11):
    """Strengths a_i with sum_m c_im = C_i (or a_i = cap where the budget is slack)."""
    n = len(budget)
    a = np.ones(n)
    for _ in range(iters):
        tot, *_ = spend(a, i, j, s_stake, r, n)
        new = a * (budget / tot) ** (0.5 / (1 + r))
        if cap is not None:
            new = np.minimum(new, cap)
        if np.max(np.abs(np.log(new / a))) < tol:
            a = new
            break
        a = new
    return a


def exposure(i, j, s_stake, n):
    return np.bincount(i, s_stake, n) + np.bincount(j, s_stake, n)


def income(a, i, j, s_stake, r, n):
    sh = shares(a, i, j, r)
    return np.bincount(i, s_stake * sh, n) + np.bincount(j, s_stake * (1 - sh), n)


# ------------------------------------------------- 1. single matter, price p
def check_single_matter():
    print("\n[1] Single matter: spend is invariant to the price of compute")
    print("    r     p        c*          p*c*/S   dissipated share (theory r/2)")
    for r in (0.5, 1.0, 1.5):
        for p in (1.0, 1e-3, 1e-6):
            S = 1.0
            c = r * S / (4 * p)  # candidate
            # verify best response numerically
            # optimise over u = x / c so the problem is well scaled at any price
            f = lambda u: -(S * u**r / (u**r + 1) - p * c * u)  # noqa: E731
            res = minimize(f, x0=[1.3], bounds=[(1e-9, None)], method="L-BFGS-B",
                           options={"ftol": 1e-15, "gtol": 1e-12})
            assert abs(res.x[0] - 1) < 1e-3, (r, p, res.x[0])
            print(f"    {r:<4} {p:<8g} {c:<11.4g} {p * c / S:<8.4f} {2 * p * c / S:.3f}  ({r / 2:.3f})")


# ----------------------------------- 2. creation versus claiming as p -> 0
def check_creation_claiming(r=1.0, Sbar=1.0, k=1.0):
    print("\n[2] Creation vs claiming, S(A) = Sbar (1 - exp(-A/k)), r =", r)
    print("    p        discovery$/S   claiming$/S   total transaction cost / S   planner cost / S")
    for p in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6):
        A_eq = k * np.log(Sbar / (2 * p * k))
        S_eq = Sbar * (1 - np.exp(-A_eq / k))
        disc = p * A_eq / S_eq
        claim = r / 2
        A_pl = k * np.log(Sbar / (p * k))
        S_pl = Sbar * (1 - np.exp(-A_pl / k))
        print(f"    {p:<8g} {disc:<14.4f} {claim:<13.3f} {disc + claim:<28.4f} {p * A_pl / S_pl:.4f}")


# -------------------------------- 3. many matters, hard budgets (KKT check)
def check_hard_budget(r=1.0, n=60):
    print("\n[3] Hard budgets over many matters: KKT strengths are a Nash equilibrium, r =", r)
    i, j, s_stake = random_matters(n, 6)
    budget = rng.lognormal(0, 1.0, n)
    a = solve_hard_budget(i, j, s_stake, budget, r)
    tot, ci, cj, sh = spend(a, i, j, s_stake, r, n)
    print(f"    budget residual max |spend/C - 1| = {np.max(np.abs(tot / budget - 1)):.2e}")
    # brute-force best response for three principals, opponents' compute held fixed
    worst, gap = 0.0, 0.0
    for who in (0, 1, 2):
        mi, mj = np.where(i == who)[0], np.where(j == who)[0]
        opp = np.concatenate([cj[mi], ci[mj]])
        stake = np.concatenate([s_stake[mi], s_stake[mj]])
        mine = np.concatenate([ci[mi], cj[mj]])
        f = lambda x: -np.sum(stake * x**r / (x**r + opp**r))  # noqa: E731
        cons = {"type": "eq", "fun": lambda x: x.sum() - budget[who]}
        start = np.full(len(mine), budget[who] / len(mine))  # uninformed start
        res = minimize(f, start, constraints=[cons], bounds=[(1e-12, None)] * len(mine),
                       method="SLSQP", options={"ftol": 1e-15, "maxiter": 5000})
        worst = max(worst, (-res.fun) / (-f(mine)) - 1)
        gap = max(gap, float(np.max(np.abs(res.x - mine) / budget[who])))
    print(f"    best response from an uninformed start: payoff gain over the KKT allocation "
          f"{worst:.1e}, allocation gap {gap:.1e}")
    # homogeneity: doubling every budget changes no share
    a2 = solve_hard_budget(i, j, s_stake, 2 * budget, r)
    print(f"    doubling all budgets: max change in any share = "
          f"{np.max(np.abs(shares(a2, i, j, r) - sh)):.2e}")
    # two-principal case reproduces Friedman's proportional rule
    ii, jj = np.zeros(5, int), np.ones(5, int)
    st = rng.uniform(0.5, 2, 5)
    bud = np.array([3.0, 1.0])
    a_f = solve_hard_budget(ii, jj, st, bud, r)
    print(f"    two principals, budgets 3:1 -> share {shares(a_f, ii, jj, r)[0]:.4f} "
          f"(Friedman: {3**r / (3**r + 1):.4f}) on every matter")


def check_walkover():
    print("\n[3b] r = 1, hard budgets: a weak principal abandons a matter against overwhelming compute")
    # j (budget 1) has a matter against i (budget C_i, no other matter) and one against k (budget 1)
    print("    C_i      j's compute against i   j's share against i   threshold S a_j (abandon above it)")
    for Ci in (0.5, 2.0, 3.9, 4.1, 100.0):
        f = lambda x: -(x[0] / (x[0] + Ci) + x[1] / (x[1] + 1.0))  # noqa: E731
        cons = {"type": "eq", "fun": lambda x: x.sum() - 1.0}
        res = minimize(f, [0.5, 0.5], constraints=[cons], bounds=[(0, None)] * 2, method="SLSQP",
                       options={"ftol": 1e-15})
        c1, c2 = res.x
        lam = 1.0 / (c2 + 1.0) ** 2  # j's shadow price from the matter against k
        print(f"    {Ci:<8g} {c1:<23.4f} {c1 / (c1 + Ci):<21.4f} {1.0 / lam:.2f}")


# --------------------- 4. square-root law for a small principal at r = 1
def check_sqrt_law():
    print("\n[4] r = 1: a small principal facing a field of strength abar earns sqrt(E C / abar)")
    abar = 2.0
    stakes = rng.lognormal(0, 0.5, 12)
    E = stakes.sum()
    print("    C/(abar E)   share (numeric)   sqrt(C/(abar E))   compute burnt by both / S   (= weak share)")
    for frac in (0.0025, 0.01, 0.04, 0.16, 0.25):
        C = frac * abar * E
        # own strength x*abar solving budget: sum_m r a S s(1-s) = C with s = x/(1+x)
        g = lambda x: abar * x * E * x / (1 + x) ** 2 - C  # noqa: E731
        x = brentq(g, 1e-9, 50)
        s = x / (1 + x)
        burnt = (x * abar + abar) * s * (1 - s)  # (c_i + c_j)/S in compute units
        burnt_dollars = burnt / abar  # priced at the field's shadow price 1/abar
        print(f"    {frac:<12g} {s:<17.4f} {np.sqrt(frac):<18.4f} {burnt_dollars:<27.4f} {s:.4f}")


# ---------------------- 5. price-taking economy with wealth dynamics (B)
def simulate_dynamics(r=1.0, n=600, per_head=8, T=300, R=1.05, beta=0.9, cbar=1.2,
                      p=1e-3, basic_compute_dollars=0.0, sufficiency=False, w0=None, label=""):
    """Each period: buy compute out of wealth (opportunity cost R per dollar),
    bargain over every matter, add object-level output R*k, consume cbar, save beta of the rest."""
    i, j, s_stake = random_matters(n, per_head)
    E = exposure(i, j, s_stake, n)
    w = rng.lognormal(0.0, 1.5, n) if w0 is None else w0.copy()
    abar = 1.0 / (p * R)
    out = {}
    for t in range(T):
        if sufficiency:
            y = E / 2
            k = w
            burnt = 0.0
            a = np.full(n, abar)
        else:
            budget = (w + basic_compute_dollars) / p
            budget = np.maximum(budget, 1e-9 / p)
            a = solve_hard_budget(i, j, s_stake, budget, r, cap=abar, iters=4000, tol=1e-9)
            tot, *_ = spend(a, i, j, s_stake, r, n)
            binding = a < abar * (1 - 1e-6)
            assert np.all(tot <= budget * (1 + 1e-5)), "spend exceeds budget"
            assert np.allclose(tot[binding], budget[binding], rtol=1e-4), "binding budget not met"
            own_dollars = np.clip(p * tot - basic_compute_dollars, 0, w)
            k = w - own_dollars
            y = income(a, i, j, s_stake, r, n)
            burnt = p * tot.sum()
        resources = R * k + y
        w = beta * np.maximum(resources - cbar, 0.0)
        if t in (0, T - 1):
            sh_i = y / E
            out[t] = dict(gini=gini(w), mean_share=float(np.mean(sh_i)),
                          frac_constrained=float(np.mean(a < abar * (1 - 1e-6))),
                          frac_destitute=float(np.mean(w < 1e-6)),
                          burnt_frac=float(burnt / s_stake.sum()),
                          p10_share=float(np.quantile(sh_i, 0.1)),
                          mean_w=float(w.mean()))
    return out, w, E


def check_dynamics():
    global rng
    print("\n[5] Price-taking economy with subsistence consumption (r = 1)")
    n = 600
    w0 = rng.lognormal(0.0, 1.5, n)
    rows = [
        ("sufficiency world (r = 0)", dict(sufficiency=True)),
        ("contest, p = 1e-3", dict(p=1e-3)),
        ("contest, p = 1e-6", dict(p=1e-6)),
        ("contest + basic compute $0.05", dict(p=1e-3, basic_compute_dollars=0.05)),
        ("contest + basic compute $0.5", dict(p=1e-3, basic_compute_dollars=0.5)),
    ]
    print("    scenario                         Gini(w)  destitute  constrained  10th-pct share  burnt/surplus  mean w")
    for name, kw in rows:
        rng = np.random.default_rng(7)  # same matter graph each scenario
        out, w, E = simulate_dynamics(n=n, w0=w0, **kw)
        o = out[max(out)]
        print(f"    {name:<32} {o['gini']:<8.3f} {o['frac_destitute']:<10.3f} {o['frac_constrained']:<12.3f} "
              f"{o['p10_share']:<15.3f} {o['burnt_frac']:<14.3f} {o['mean_w']:.2f}")
    # closed-form trap threshold against a fully unconstrained field
    beta, R, cbar = 0.9, 1.05, 1.2
    Ebar = float(np.mean(E))
    disc = beta**2 * R * Ebar - 4 * beta * cbar
    if disc > 0:
        lo = ((beta * np.sqrt(R * Ebar) - np.sqrt(disc)) / 2) ** 2
        print(f"    closed-form trap threshold at mean exposure E = {Ebar:.2f}: w_- = {lo:.3f} "
              f"(parity needs R w >= E/4 = {Ebar / 4:.2f})")


# ------------------------------------------- 6. repeat player (scope economies)
def check_repeat_player(r=1.0):
    print("\n[6] Repeat player with M matters against M one-shot counterparties")
    print("    effective compute z = g^phi * l^(1-phi), g reusable across the firm's M matters")
    print("    phi    M        firm share (numeric)   M^(phi r)/(1+M^(phi r))")
    S, lam = 1.0, 1.0
    for phi in (0.2, 0.5):
        for M in (10, 1_000, 1_000_000):
            # best-response iteration in (z_f, z_c)
            def br_z(z_opp, mult):
                # choose total per-matter spend e; effective z = mult * e (after optimal g/l split)
                f = lambda e: -(S * (mult * e) ** r / ((mult * e) ** r + z_opp**r) - lam * e)  # noqa: E731
                res = minimize(f, [0.1], bounds=[(1e-14, None)], method="L-BFGS-B",
                               options={"ftol": 1e-16, "gtol": 1e-14})
                return mult * res.x[0]
            base = (phi ** phi) * ((1 - phi) ** (1 - phi))
            mult_f, mult_c = base * M**phi, base
            zf, zc = 0.1, 0.1
            for _ in range(400):
                zf = 0.5 * zf + 0.5 * br_z(zc, mult_f)
                zc = 0.5 * zc + 0.5 * br_z(zf, mult_c)
            s_num = zf**r / (zf**r + zc**r)
            s_th = M ** (phi * r) / (1 + M ** (phi * r))
            print(f"    {phi:<6} {M:<8} {s_num:<22.5f} {s_th:.5f}")


# ------------------------------------------- 7. game size and satiation (Jones 2021)
def jones_table():
    print("\n[7] Jones (2021) Hex fit: Elo = clamp(510 log10 f - 430 b - 4400, -270 b + 570, 0)")
    print(f"    implied decisiveness r = 510/400 = {510 / 400:.2f}; "
          f"2x compute wins {2 ** (510 / 400) / (1 + 2 ** (510 / 400)):.3f}")
    print(f"    compute to reach perfect play multiplies by 10^(430/510) = {10 ** (430 / 510):.2f} per unit board size")
    print("    board size b   log10 compute for perfect play")
    for b in (3, 5, 7, 9, 11, 13, 19):
        print(f"    {b:<14} {(430 * b + 4400) / 510:.1f}")
    print(f"    a 10^6-fold fall in compute price buys {6 * 510 / 430:.1f} extra board sizes, "
          f"or {6 / np.log10(2):.1f} extra binary contingencies under exhaustive checking")


if __name__ == "__main__":
    check_single_matter()
    check_creation_claiming()
    check_hard_budget(r=0.9)
    check_hard_budget(r=0.5)
    check_walkover()
    check_sqrt_law()
    check_dynamics()
    check_repeat_player()
    jones_table()
