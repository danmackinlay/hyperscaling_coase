"""Numerical checks for the personal-budget Coasean bargaining models.

Every closed form quoted in draft.md, beside this file, is checked here
against a direct numerical computation.
Run from the repository root:
  uv run --no-project --with numpy --with scipy python _notes/personal_budget/check_budget_contests.py
"""

import numpy as np
from scipy.optimize import brentq, minimize

rng = np.random.default_rng(20261119)


# ---------------------------------------------------------------- core solver
def solve_strengths(V, B, r=1.0, tol=1e-12, iters=20000, s0=None):
    """Equilibrium of a network of bilateral Tullock contests with budgets.

    V[i, j] = V[j, i] is the stake of the matter between i and j (0 if none).
    B[i] is i's liquid budget. Returns strengths s in (0, 1], spends x[i, j].
    share_ij = s_i^r / (s_i^r + s_j^r);  x_ij = r V_ij share_ij share_ji s_i.
    s_i = 1 if the budget is slack, else s_i solves sum_j x_ij = B_i.
    """
    n = len(B)
    s = np.ones(n) if s0 is None else np.array(s0, dtype=float)
    for _ in range(iters):
        sr = s**r
        sig = sr[:, None] / (sr[:, None] + sr[None, :])
        need = r * (V * sig * sig.T).sum(1)  # spend if s_i were 1 ... times s_i
        s_new = np.minimum(1.0, B / np.maximum(need, 1e-300))
        # damped update in logs (need depends on s_i through sig)
        s_next = np.exp(0.5 * np.log(s) + 0.5 * np.log(np.maximum(s_new, 1e-300)))
        if np.max(np.abs(s_next - s)) < tol:
            s = s_next
            break
        s = s_next
    sr = s**r
    sig = sr[:, None] / (sr[:, None] + sr[None, :])
    x = r * V * sig * sig.T * s[:, None]
    return s, sig, x


def payoff_i(xi, i, x, V, r):
    """Gross surplus won by i, net of spend, given own spends xi on row i."""
    xj = x[:, i]
    mask = V[i] > 0
    num = xi[mask] ** r
    den = num + xj[mask] ** r
    return (V[i][mask] * num / den).sum() - xi[mask].sum()


def check_nash(V, B, r, x, trials=3):
    """Max gain any player can get by deviating (should be ~0)."""
    n = len(B)
    worst = 0.0
    for i in range(n):
        mask = V[i] > 0
        k = mask.sum()
        base = payoff_i(x[i], i, x, V, r)

        def neg(z):
            xi = np.zeros(n)
            xi[mask] = np.abs(z)
            return -payoff_i(xi, i, x, V, r)

        cons = [{"type": "ineq", "fun": lambda z: B[i] - np.abs(z).sum()}]
        best = base
        for _ in range(trials):
            z0 = x[i][mask] * np.exp(0.3 * rng.standard_normal(k))
            z0 *= min(1.0, B[i] / z0.sum())
            res = minimize(neg, z0, constraints=cons, method="SLSQP",
                           options={"maxiter": 500, "ftol": 1e-13})
            if np.abs(res.x).sum() <= B[i] * (1 + 1e-9):
                best = max(best, -res.fun)
        worst = max(worst, (best - base) / max(abs(base), 1e-12))
    return worst


print("=== A. network equilibrium: Nash check on random small networks ===")
for r in (1.0, 0.5, 0.25):
    n = 7
    V = np.triu(rng.lognormal(0, 1, (n, n)) * (rng.random((n, n)) < 0.7), 1)
    V = V + V.T
    B = rng.lognormal(-2.5, 1.5, n) * V.sum(1)
    s, sig, x = solve_strengths(V, B, r)
    slack = B - x.sum(1)
    print(f"r={r}: strengths {np.round(s, 3)}; min budget slack {slack.min():.2e}; "
          f"max relative gain from deviating {check_nash(V, B, r, x):.2e}")
    restarts = [solve_strengths(V, B, r, s0=rng.uniform(1e-3, 1, n))[0] for _ in range(20)]
    print(f"   20 random starting points: largest difference in any strength "
          f"{max(np.abs(z - s).max() for z in restarts):.2e}")

# ----------------------------------------------- B. one constrained principal
print("\n=== B. constrained principal vs unconstrained counterparties ===")


def constrained_vs_strong(B, S, r=1.0):
    """Strength, share, gross take, opponents' spend. Stakes sum to S."""
    f = lambda s: r * S * s ** (1 + r) / (1 + s**r) ** 2 - B
    if f(1.0) <= 0:
        s = 1.0
    else:
        s = brentq(f, 1e-14, 1.0, xtol=1e-15)
    share = s**r / (1 + s**r)
    opp_spend = r * S * share * (1 - share)  # opponents have strength 1
    own_spend = opp_spend * s
    return s, share, share * S, own_spend, opp_spend


for S, label in ((25_000, "today"), (50_000, "matters doubled")):
    for r in (1.0, 0.5, 0.25):
        B = 400.0
        s, share, gross, own, opp = constrained_vs_strong(B, S, r)
        print(f"Asha {label:16s} r={r:4}: s={s:.4f} share={share:.3f} gross={gross:8.0f} "
              f"own spend={own:6.0f} opp spend={opp:7.0f} burned={(own + opp) / S:.3f} "
              f"opp net={(1 - share) * S - opp:8.0f} lambda={1 / s:.2f}")
print("closed form r=1: share sqrt(B/S) =", np.sqrt(400 / 25000), " gross sqrt(BS) =",
      np.sqrt(400 * 25000), " opp net (sqrt S - sqrt B)^2 =", (np.sqrt(25000) - 20) ** 2)
print("unconstrained pair r=1: each share .5, each spends S/4 =", 25000 / 4,
      "; r=.25: each spends rS/4 =", 0.25 * 25000 / 4)
for r in (1.0, 0.5, 0.25):
    print(f"  r={r}: budget needed to be unconstrained on S=25000: {r * 25000 / 4:.0f}")

# share as number of matters grows (fixed budget, fixed stake per matter)
print("\nshare vs number of matters m (stake 250 each, B=400, r=1):")
for m in (10, 100, 1000, 10000):
    s, share, gross, *_ = constrained_vs_strong(400, 250 * m, 1.0)
    print(f"  m={m:6d} share={share:.4f} (sqrt(B/S)={np.sqrt(400 / (250 * m)):.4f}) gross={gross:.0f}")

# ------------------------------------------------------ C. population sketch
print("\n=== C. population: households vs firms and vs each other ===")


def population(n_h=3000, m_peer=20, v_peer=250.0, voucher=0.0, r=1.0, seed=1):
    """Households with log-normal budgets; each has 20,000 at issue with
    unconstrained firms (strength 1) and m_peer matters of v_peer with random
    other households. Same seed gives the same budgets in every scenario."""
    g = np.random.default_rng(seed)
    B = np.maximum(g.lognormal(np.log(400), 1.5, n_h), voucher)
    g.lognormal(0, 1, n_h)  # keep the random stream aligned with the first run
    S_firm = np.full(n_h, 20_000.0)
    # peer matters: random regular-ish graph
    pairs = set()
    for i in range(n_h):
        for j in g.choice(n_h, m_peer // 2, replace=False):
            if i != j:
                pairs.add((min(i, j), max(i, j)))
    pairs = np.array(sorted(pairs))
    # iterate strengths: firms have strength 1
    s = np.ones(n_h)
    for _ in range(4000):
        sr = s**r
        sf = sr / (1 + sr)
        need = r * S_firm * sf * (1 - sf)
        si, sj = sr[pairs[:, 0]], sr[pairs[:, 1]]
        sg = si / (si + sj)
        pp = r * v_peer * sg * (1 - sg)
        need = need + np.bincount(pairs[:, 0], pp, n_h) + np.bincount(pairs[:, 1], pp, n_h)
        s_new = np.minimum(1.0, B / need)
        s_next = np.exp(0.5 * np.log(s) + 0.5 * np.log(s_new))
        if np.max(np.abs(s_next - s)) < 1e-13:
            break
        s = s_next
    sr = s**r
    sf = sr / (1 + sr)
    firm_spend = r * S_firm * sf * (1 - sf)  # firm strength 1
    hh_spend_firm = firm_spend * s
    si, sj = sr[pairs[:, 0]], sr[pairs[:, 1]]
    sg = si / (si + sj)
    pp = r * v_peer * sg * (1 - sg)
    peer_gross = np.bincount(pairs[:, 0], v_peer * sg, n_h) + np.bincount(pairs[:, 1], v_peer * (1 - sg), n_h)
    peer_spend = (np.bincount(pairs[:, 0], pp, n_h) + np.bincount(pairs[:, 1], pp, n_h)) * s
    S_peer = v_peer * (np.bincount(pairs[:, 0], minlength=n_h) + np.bincount(pairs[:, 1], minlength=n_h))
    out = dict(B=B, s=s, share_firm=sf, S_firm=S_firm, S_peer=S_peer,
               hh_spend=hh_spend_firm + peer_spend, firm_spend=firm_spend,
               hh_gross=sf * S_firm + peer_gross,
               firm_net=(1 - sf) * S_firm - firm_spend)
    return out


def report(tag, o):
    q = np.quantile(o["B"], [0.1, 0.5, 0.9, 0.99])
    order = np.argsort(o["B"])
    n = len(order)
    dec = [order[: n // 10], order[int(0.45 * n): int(0.55 * n)], order[int(0.9 * n):], order[int(0.99 * n):]]
    S_tot = o["S_firm"].sum() + o["S_peer"].sum() / 2
    burned = o["hh_spend"].sum() + o["firm_spend"].sum()
    print(f"-- {tag}: budget p10/p50/p90/p99 = {np.round(q)}; constrained share of households "
          f"{(o['s'] < 1 - 1e-9).mean():.3f}")
    for name, idx in zip(("bottom decile", "middle decile", "top decile", "top 1%"), dec):
        net = o["hh_gross"][idx] - o["hh_spend"][idx]
        print(f"   {name:14s} strength {o['s'][idx].mean():.3f}  share vs firms {o['share_firm'][idx].mean():.3f}  "
              f"net gain {net.mean():8.0f}  spend {o['hh_spend'][idx].mean():7.0f}")
    print(f"   surplus {S_tot:.3e}; burned {burned / S_tot:.3f}; households keep "
          f"{(o['hh_gross'].sum() - o['hh_spend'].sum()) / S_tot:.3f}; firms keep {o['firm_net'].sum() / S_tot:.3f}")
    return S_tot, burned


base = population()
report("baseline r=1, 20 peer matters", base)
report("r=1, 200 peer matters (10x)", population(m_peer=200))
v = population(voucher=2000.0)
S_tot, burned_v = report("r=1, voucher floor 2000", v)
raw = population()
cost = np.maximum(2000.0 - raw["B"], 0).sum()
print(f"   voucher cost {cost / S_tot:.3f} of surplus; extra burned vs baseline "
      f"{(burned_v - (raw['hh_spend'].sum() + raw['firm_spend'].sum())) / S_tot:.3f}")
v = population(voucher=6250.0)
S_tot, burned_v = report("r=1, voucher floor 6250 (=S/4 incl. peers approx)", v)
print(f"   voucher cost {np.maximum(6250.0 - raw['B'], 0).sum() / S_tot:.3f} of surplus")
report("r=0.25", population(r=0.25))

# ------------------------------------------- D. contestable entitlements
print("\n=== D. contested entitlements with defender advantage theta ===")


def attack_profit(V, b, theta):
    """Attacker's best-response profit against a defender who spends b (r=1)."""
    res = minimize(lambda z: -(V * abs(z[0]) / (theta * b + abs(z[0])) - abs(z[0])), [V / 4],
                   method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-12})
    return -res.fun


for theta in (1.0, 3.0):
    V, b = 10_000.0, 100.0
    print(f"theta={theta}: numeric attack profit {attack_profit(V, b, theta):.2f}  closed form "
          f"{(np.sqrt(V) - np.sqrt(theta * b)) ** 2:.2f};  defender keeps sqrt(theta b V)="
          f"{np.sqrt(theta * b * V):.0f}")
    # unconstrained pair: iterate best responses
    xa = xd = V / 4
    for _ in range(200):
        xa = max(np.sqrt(V * theta * xd) - theta * xd, 1e-12)
        xd = max((np.sqrt(V * theta * xa) - xa) / theta, 1e-12)
    print(f"   unconstrained: xa={xa:.1f} xd={xd:.1f} closed form {V * theta / (1 + theta) ** 2:.1f}; "
          f"attacker net {V * xa / (theta * xd + xa) - xa:.1f} closed form {V / (1 + theta) ** 2:.1f}")


def safe_stake(B, phi, theta):
    return (np.sqrt(theta * min(B, theta * phi)) + np.sqrt(phi)) ** 2


print("safe contestable stake V*(B) = (sqrt(theta min(B, theta phi)) + sqrt(phi))^2:")
for phi in (1000.0, 100.0, 1.0):
    print(f"  fee {phi:6.0f}: " + "  ".join(
        f"B={B:5.0f}->{safe_stake(B, phi, 3.0):8.0f}" for B in (0, 50, 400, 5000)) + "   (theta=3)")

print("pile-on: k challengers, each on a stake of 10000, defender budget 400, theta=3, fee 5500:")
for k in (1, 2, 4, 8):
    b = 400 / k
    print(f"  k={k}: profit per challenger {(100 - np.sqrt(3 * b)) ** 2:7.0f}; defender keeps "
          f"{np.sqrt(3 * b * 10000) / 10000:.3f} of each")

print("\nequal society, per pair: gain = V+/2 - 4 theta V-/(1+theta)^2; break-even V-/V+ =")
for theta in (1, 3, 9):
    print(f"  theta={theta}: {(1 + theta) ** 2 / (8 * theta):.3f}")

# ------------------------------------------------------------ E. dynamics
print("\n=== E. budget dynamics ===")
S = 25_000.0
B = 400.0
path = [B]
for t in range(6):
    B = np.sqrt(B * S) if B < S / 4 else B + S / 4
    path.append(B)
print("liquid gains, no drain: B_t =", np.round(path))
for d in (1000.0, 3000.0):
    lo = ((np.sqrt(S) - np.sqrt(S - 4 * d)) / 2) ** 2
    print(f"drain d={d:.0f}/period: trap threshold B_- = {lo:.1f} (approx d^2/S = {d * d / S:.1f})")
    for B0 in (0.5 * lo, 2 * lo):
        B = B0
        for t in range(12):
            B = max(np.sqrt(B * S) - d, 0.0) if B < S / 4 else B + S / 4 - d
        print(f"   start {B0:8.1f} -> after 12 periods {B:10.1f}")

# ------------------------------------------- F. showing-up cost and span
print("\n=== F. span of attention with a showing-up cost phi per matter ===")
B, V, phi = 400.0, 250.0, 2.0
ks = np.arange(1, int(B / phi))
gross = np.sqrt((B - phi * ks) * ks * V)
print(f"equal stakes: best k = {ks[gross.argmax()]} (closed form B/(2 phi) = {B / (2 * phi):.0f}); "
      f"gross {gross.max():.0f} (closed form (B/2) sqrt(V/phi) = {B / 2 * np.sqrt(V / phi):.0f})")
alpha, M, v0 = 1.5, 50.0, 250.0  # N(v) = M (v/v0)^-alpha matters with stake above v
vs = np.geomspace(1e-2, 1e4, 400000)
N = M * (vs / v0) ** -alpha
Sv = alpha / (alpha - 1) * M * v0**alpha * vs ** (1 - alpha)
obj = np.where(B - phi * N > 0, (B - phi * N) * Sv, -np.inf)
i = obj.argmax()
print(f"Pareto stakes alpha={alpha}: budget share spent on showing up {phi * N[i] / B:.4f} "
      f"(closed form (alpha-1)/(2alpha-1) = {(alpha - 1) / (2 * alpha - 1):.4f}); matters attended {N[i]:.0f}")
for phi_ in (20.0, 2.0, 0.2, 0.02):
    Nn = (alpha - 1) / (2 * alpha - 1) * B / phi_
    vstar = v0 * (Nn / M) ** (-1 / alpha)
    S_ = alpha / (alpha - 1) * M * v0**alpha * vstar ** (1 - alpha)
    Bf = B - phi_ * Nn
    print(f"  phi={phi_:5.2f}: attends {Nn:7.0f} matters, stakes in play {S_:9.0f}, "
          f"share {np.sqrt(Bf / S_):.4f}, gross {np.sqrt(Bf * S_):7.0f}")

# ------------------------------------------- G. repeat player
print("\n=== G. repeat player reusing one argument across N identical matters ===")
V, b = 6000.0, 100.0
for Nn in (1, 100, 10000):
    res = minimize(lambda z: -(Nn * V * abs(z[0]) / (abs(z[0]) + b) - abs(z[0])), [np.sqrt(Nn * V * b)],
                   method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-9})
    X = abs(res.x[0])
    print(f"N={Nn:6d}: firm spends {X:9.0f} once (closed form {np.sqrt(Nn * V * b) - b:9.0f}); "
          f"isolated household share {b / (X + b):.4f} (sqrt(b/(N V)) = {np.sqrt(b / (Nn * V)):.4f}); "
          f"if all N pool: {np.sqrt(b / V):.4f}")

# ------------------------------- H. saturating, non-saturating, mixed worlds
print("\n=== H. three worlds: matters that saturate and matters that do not ===")
from scipy.optimize import minimize_scalar  # noqa: E402
from scipy.special import expit  # noqa: E402
from scipy.stats import norm  # noqa: E402


def best_response(V, other, r, ub):
    """Spend in [0, ub] maximizing V x^r/(x^r + other^r) - x."""
    res = minimize_scalar(lambda z: -(V * z**r / (z**r + other**r) - z), bounds=(1e-12, ub),
                          method="bounded", options={"xatol": 1e-10})
    return res.x


def capped_pair(V, r, cap, B=np.inf):
    """One matter with stake V; side a has budget B, side b has none; a depth
    limit caps both sides' spend at `cap` dollars. Returns equilibrium spends."""
    xa, xb = min(cap, B, V / 4), min(cap, V / 4)
    for _ in range(400):
        xa = 0.5 * xa + 0.5 * best_response(V, xb, r, min(cap, B, V))
        xb = 0.5 * xb + 0.5 * best_response(V, xa, r, min(cap, V))
    return xa, xb


print("H1. unconstrained pair, stake 10,000, depth limit of `cap` dollars a side:")
for r in (1.0, 0.5):
    for cap in (1e9, 3000.0, 1000.0, 100.0):
        xa, xb = capped_pair(10_000.0, r, cap)
        print(f"  r={r} cap={cap:10.0f}: total spend {xa + xb:8.1f}  "
              f"closed form min(rV/2, 2 cap) = {min(r * 10_000 / 2, 2 * cap):8.1f}")

print("H2. Asha (B=400, S=25,000, r=1) as the depth limit falls with the price of compute:")
for cap in (1e9, 2762.0, 1600.0, 800.0, 400.0, 100.0, 10.0):
    xa, xb = capped_pair(25_000.0, 1.0, cap, B=400.0)
    closed = np.sqrt(400 / 25_000) if cap >= 2762 else (400 / (400 + cap) if cap >= 400 else 0.5)
    print(f"  cap={cap:10.0f}: Asha spends {xa:6.1f}, firms spend {xb:7.1f}, her share "
          f"{xa / (xa + xb):.3f} (closed form {closed:.3f}), dissipated {(xa + xb) / 25_000:.3f}")

print("H3. mixed world: a fraction phi of Asha's stakes never saturates, the rest "
      "saturates at negligible cost and splits evenly (r=1):")
for phi in (1.0, 0.5, 0.2, 0.064, 0.02):
    s, share, gross, own, opp = constrained_vs_strong(400.0, phi * 25_000, 1.0)
    total = (1 - phi) * 25_000 / 2 + gross
    closed = (1 - phi) / 2 + (np.sqrt(phi * 400 / 25_000) if phi > 4 * 400 / 25_000 else phi / 2)
    print(f"  phi={phi:5.3f}: share in non-saturating matters {share:.3f}; she takes {total:7.0f} "
          f"= {total / 25_000:.3f} of S (closed form {closed:.3f}); dissipated {(own + opp) / 25_000:.3f}")


def mixed_nash(V, cap, B, r=1.0, iters=200):
    """Direct equilibrium: one budget-limited principal against one
    unconstrained firm per matter, with a per-matter cap on both sides."""
    V, cap = np.asarray(V, float), np.asarray(cap, float)
    ub = np.minimum(cap, V)
    x = np.minimum(ub, B / len(V))
    y = np.minimum(ub, V / 4)
    for _ in range(iters):
        y = 0.5 * y + 0.5 * np.array([best_response(V[m], x[m], r, ub[m]) for m in range(len(V))])
        res = minimize(lambda z: -(V * z**r / (z**r + y**r)).sum() + z.sum(), x,
                       bounds=[(1e-9, u) for u in ub],
                       constraints=[{"type": "ineq", "fun": lambda z: B - z.sum()}],
                       method="SLSQP", options={"ftol": 1e-14, "maxiter": 500})
        x = 0.5 * x + 0.5 * res.x
    return x, y


stakes = np.array([12_000.0, 6_000.0, 2_000.0, 1_000.0, 4_000.0])  # job, lease, insurer, platforms, small
caps = np.array([5.0, 1e9, 5.0, 5.0, 5.0])  # only the lease never saturates
x, y = mixed_nash(stakes, caps, 400.0)
sh = x / (x + y)
pred = np.sqrt(380.0 / 6_000)
print(f"  direct check, lease alone non-saturating, cap 5 elsewhere: shares {np.round(sh, 3)}; "
      f"lease share closed form sqrt(380/6000) = {pred:.3f}; she takes {(sh * stakes).sum():.0f} "
      f"(closed form {19_000 / 2 + pred * 6_000:.0f}); spends {x.sum():.1f}")

print("H4. effective decisiveness when the decider compares the two best draws with error.")
print("    r_eff = slope of log-odds of winning on log compute ratio, at equal compute q.")


def best_draw(dist, logu, q):
    """Quantile transform of the best of q draws; logu = log of a uniform."""
    tail = -np.expm1(logu / q)  # 1 - u^(1/q), accurate when tiny
    if dist == "uniform":
        return 1.0 - tail
    if dist == "exponential":
        return -np.log(tail)
    if dist == "gaussian":
        return norm.isf(tail)
    if dist == "pareto3":
        return tail ** (-1 / 3)
    raise ValueError(dist)


NOISE = {"uniform": 12**-0.5, "exponential": 1.0, "gaussian": 1.0, "pareto3": 0.75**0.5}
_logu = np.log((np.arange(1500) + 0.5) / 1500)


def p_win(dist, qi, qj, s):
    gap = best_draw(dist, _logu, qi)[:, None] - best_draw(dist, _logu, qj)[None, :]
    return expit(gap / s).mean()


def r_eff(dist, q, s=None, h=0.01):
    s = NOISE[dist] if s is None else s
    return 4 * (p_win(dist, q * np.exp(h), q, s) - p_win(dist, q * np.exp(-h), q, s)) / (2 * h)


qs = (10, 100, 1000, 10_000, 1_000_000)
print("    decider's error: logistic, scale = one standard deviation of a single draw")
print("    tail of quality     " + "  ".join(f"q={q:<8d}" for q in qs))
for dist in ("uniform", "exponential", "gaussian", "pareto3"):
    print(f"    {dist:18s}  " + "  ".join(f"{r_eff(dist, q):10.4f}" for q in qs))
print(f"    predictions: uniform 1/(s q) = {[round(12**0.5 / q, 4) for q in qs]}; exponential 2/3; "
      f"gaussian about 1/sqrt(2 ln q) = {[round(float(1 / np.sqrt(2 * np.log(q))), 3) for q in qs]}; pareto -> 1")

print("    symmetric equilibrium spend per side, stake 10,000, as the price p of a draw falls:")
for dist in ("uniform", "exponential", "gaussian"):
    row = []
    for p in (1.0, 1e-2, 1e-4):
        q = brentq(lambda lq: p * np.exp(lq) - 10_000 * r_eff(dist, np.exp(lq)) / 4, 0.0, 40.0, xtol=1e-6)
        row.append(p * np.exp(q))
    extra = ""
    if dist == "uniform":
        extra = "  closed form sqrt(V p/(4 s)) = " + ", ".join(
            f"{np.sqrt(10_000 * p / (4 * NOISE['uniform'])):.2f}" for p in (1.0, 1e-2, 1e-4))
    print(f"    {dist:12s} p=1, 0.01, 0.0001: " + ", ".join(f"{v:9.2f}" for v in row) + extra)

print("H5. a firm that can choose whether its matter saturates (even split, no spend) or not:")


def firm_net_per_dollar(B, S_deep, r):
    """Firm's net per dollar of stake on a non-saturating matter, when the
    household has budget B and S_deep dollars of non-saturating stakes."""
    s, share, *_ = constrained_vs_strong(B, S_deep, r)
    return (1 - share) - r * share * (1 - share)


for r in (1.0, 0.5, 0.25):
    ratio = brentq(lambda b: firm_net_per_dollar(b, 1.0, r) - 0.5, 1e-9, r / 4)
    s, share, *_ = constrained_vs_strong(ratio, 1.0, r)
    print(f"  r={r}: firm prefers the non-saturating matter iff household share < {share:.3f}, "
          f"i.e. budget < {ratio:.4f} of its non-saturating stakes")
print(f"  closed form r=1: share < 1 - 1/sqrt(2) = {1 - 2**-0.5:.3f}; budget ratio (1 - 1/sqrt 2)^2 = "
      f"{(1 - 2**-0.5) ** 2:.4f}")


def depth_cascade(stakes, B, r=1.0, start_deep=False):
    """Firms revise in turn: make the matter non-saturating iff that nets more than half."""
    deep = np.full(len(stakes), start_deep)
    for _ in range(50):
        changed = False
        for m in np.argsort(-stakes):
            others = stakes[deep].sum() - (stakes[m] if deep[m] else 0.0)
            want = firm_net_per_dollar(B, others + stakes[m], r) > 0.5
            if want != deep[m]:
                deep[m], changed = want, True
        if not changed:
            break
    return deep


firm_stakes = np.array([12_000.0, 6_000.0, 2_000.0, 1_000.0])  # Asha's matters with firms
for B in (400.0, 1_500.0, 3_000.0):
    a = depth_cascade(firm_stakes, B, start_deep=False)
    b = depth_cascade(firm_stakes, B, start_deep=True)
    print(f"  budget {B:6.0f}: from all saturating -> non-saturating {a.astype(int)}; "
          f"from none saturating -> {b.astype(int)}   "
          f"(0.0858 x largest stake = {0.0858 * 12_000:.0f}, x all firm stakes = {0.0858 * 21_000:.0f})")

print("H6. share of total stake held by the largest 1% of matters, Pareto stakes with index alpha:")
for a in (2.0, 1.5, 1.2):
    v = np.random.default_rng(7).pareto(a, 4_000_000) + 1
    top = np.sort(v)[-len(v) // 100:].sum() / v.sum()
    print(f"  alpha={a}: closed form 0.01^(1-1/alpha) = {0.01 ** (1 - 1 / a):.3f}; simulated {top:.3f}")
