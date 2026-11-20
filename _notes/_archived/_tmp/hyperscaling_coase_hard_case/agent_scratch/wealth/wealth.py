"""Wealth-effects row on the hard-case instance (parametric, once, enforcer, closed).

Enumerates the 16 schedules. Residents: U_i = log(w_i) - v_i(h_i(x)), w_i = w0_i + t_i.
Fleet: U_f = log(100 + P(x) - sum t). Calibrations of the non-money harm v(h):
  marg: v = h/w0            (harm worth h at the margin at the endowment)
  wta : v = log(1 + h/w0)   (h is exactly the compensation needed at the endowment)
  wtp : v = -log(1 - h/w0)  (h is exactly what the resident would pay at the endowment; inf if h>=w0)
  money: harm is a money loss, U_i = log(w0 + t - h)
Linear: U = money payoff, harm = h.
"""
import itertools, math
import numpy as np

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1, 1, 2.0])
W0 = np.array([100.0, 10, 10, 2])  # fleet, r1, r2, r3
SCHED = [np.array(x) for x in itertools.product([0, 1], repeat=4)]
NAME = lambda x: "".join(c for c, b in zip("MDEN", x) if b) or "none"
ALL = np.array([1, 1, 1, 1])
NONE = np.array([0, 0, 0, 0])


def harms(x, s=s):
    return s * (E @ x)


def v(h, w0, cal):
    if cal == "marg":
        return h / w0
    if cal == "wta":
        return math.log1p(h / w0)
    if cal == "wtp":
        return -math.log1p(-h / w0) if h < w0 else math.inf
    raise ValueError(cal)


def util(j, w, x, cal, s=s):
    """utility of party j (0 fleet) at final wealth w under schedule x"""
    if w <= 0:
        return -math.inf
    if j == 0:
        return math.log(w)
    h = harms(x, s)[j - 1]
    if cal == "money":
        return math.log(w - h) if w - h > 0 else -math.inf
    return math.log(w) - v(h, W0[j], cal)


def origin_utils(x0, cal):
    """utilities at no deal: schedule x0, no transfers"""
    w = W0.copy()
    w[0] += p @ x0
    return np.array([util(j, w[j], x0, cal) for j in range(4)])


def wmin(j, x, target, cal):
    """least wealth giving party j utility >= target"""
    if j == 0:
        return math.exp(target)
    h = harms(x)[j - 1]
    if cal == "money":
        return math.exp(target) + h
    vv = v(h, W0[j], cal)
    return math.exp(target + vv) if math.isfinite(vv) else math.inf


def nbs(x, U0, cal):
    """max sum log(U_j - U0_j) over money splits for schedule x. Returns (wealth, gains, logNP) or None."""
    total = W0.sum() + p @ x
    lo = np.array([wmin(j, x, U0[j], cal) for j in range(4)])
    if not np.all(np.isfinite(lo)) or lo.sum() >= total:
        return None
    # FOC: u'(w)/G(w) = lam, with u'(w)=1/w (money reading: 1/(w-h)); solve w_j(lam) by bisection
    def wj(j, lam):
        a, b = lo[j] * (1 + 1e-15) + 1e-15, total
        for _ in range(200):
            m = 0.5 * (a + b)
            g = util(j, m, x, cal) - U0[j]
            du = 1 / (m - (harms(x)[j - 1] if (cal == "money" and j) else 0))
            if du / g > lam:
                a = m
            else:
                b = m
        return 0.5 * (a + b)
    la, lb = 1e-12, 1e12
    for _ in range(200):
        lam = math.sqrt(la * lb)
        w = np.array([wj(j, lam) for j in range(4)])
        if w.sum() > total:
            la = lam
        else:
            lb = lam
    w = np.array([wj(j, lam) for j in range(4)])
    w *= 1  # sum ~ total
    G = np.array([util(j, w[j], x, cal) - U0[j] for j in range(4)])
    return w, G, float(np.sum(np.log(G)))


def linear_nbs(x, x0):
    """linear: equal split of money gain over origin x0"""
    pie = (p @ x - harms(x).sum()) - (p @ x0 - harms(x0).sum())
    return pie, (np.full(4, pie / 4) if pie > 0 else None)


def report(cal):
    print(f"\n===== calibration {cal} =====")
    for ent, x0 in [("residents' right (origin none)", NONE), ("fleet's right (origin all)", ALL)]:
        U0 = origin_utils(x0, cal)
        print(f"\n-- {ent}; origin utilities finite: {np.all(np.isfinite(U0))}")
        if not np.all(np.isfinite(U0)):
            print("   origin undefined (a resident's wealth or utility is -inf at no deal)")
            continue
        # compensation test: money surplus net of WTA (res right) / WTP (fleet right) for each x
        rows = []
        for x in SCHED:
            r = nbs(x, U0, cal)
            # KH: least total money the four need at x to reach origin utility, vs money available
            lo = [wmin(j, x, U0[j], cal) for j in range(4)]
            net = W0.sum() + p @ x - sum(lo)
            rows.append((NAME(x), net, r))
        rows.sort(key=lambda r: -r[1])
        print("   compensation-test surplus (money left after restoring everyone to no-deal utility):")
        print("   " + ", ".join(f"{n}:{net:.3f}" for n, net, _ in rows[:6]))
        feas=[r for r in rows if r[2]]
        if not feas:
            print("   NO schedule gives every party a positive gain: no deal, origin schedule stands")
            continue
        best = max(feas, key=lambda r: r[2][2])
        n, net, (w, G, lnp) = best
        pay = w - W0
        pay[0] -= 0  # fleet money payoff relative to endowment includes profit
        print(f"   NBS schedule {n}: Nash product (utility) {math.exp(lnp):.3e}, log {lnp:.3f}")
        print(f"   final money payoff vs endowment (f; r1,r2,r3): {np.round(pay, 3)}")
        print(f"   utility gains: {np.round(G, 4)}; floor {G.min():.4f} (party {int(G.argmin())})")
        w_or = W0.copy(); w_or[0] += p @ x0
        meq = w_or * (np.exp(G) - 1)
        print(f"   money-equivalent gains at origin wealth (EV): {np.round(meq, 3)}; product {np.prod(meq):.4g}; sum {meq.sum():.3f}")
        # money gains vs origin money
        m0 = np.array([p @ x0, 0, 0, 0])
        mg = pay - m0
        print(f"   money transfers to residents t: {np.round(pay[1:], 3)}; fleet money gain over origin {mg[0]:.3f}")
        # second best schedule
        others = sorted((r for r in rows if r[2]), key=lambda r: -r[2][2])[:4]
        print("   top schedules by Nash product: " + ", ".join(f"{r[0]}:{math.exp(r[2][2]):.3e}" for r in others))


def linear_report():
    print("\n===== linear =====")
    for ent, x0 in [("residents' right", NONE), ("fleet's right", ALL)]:
        best = max(SCHED, key=lambda x: p @ x - harms(x).sum())
        pie, g = linear_nbs(best, x0)
        pay = np.array([p @ best, 0, 0, 0.0]) - np.r_[0, harms(best)]
        base = np.array([p @ x0, *(-harms(x0))])
        final = base + g
        print(f"-- {ent}: schedule {NAME(best)}, pie over origin {pie}, gains {g}, product {np.prod(g):.4g};"
              f" final money (f;r) {final}; transfers t = {final[1:] + harms(best)}")


def liability(cal):
    print(f"\n===== liability rule, calibration {cal}; origin = residents' right (none) =====")
    U0 = origin_utils(NONE, cal)
    for dmg in ["money harm", "full compensation"]:
        best = None
        for x in SCHED:
            h = harms(x)
            if dmg == "money harm":
                d = h.copy()
            else:
                d = np.array([wmin(j, x, U0[j], cal) - W0[j] for j in (1, 2, 3)])
            prof = p @ x - d.sum()
            if best is None or prof > best[1]:
                best = (x, prof, d)
        x, prof, d = best
        w = W0.copy(); w[0] += prof; w[1:] += d
        G = np.array([util(j, w[j], x, cal) - U0[j] for j in range(4)])
        npd = np.prod(G) if np.all(G > 0) else (0.0 if np.all(G >= -1e-12) else float("nan"))
        print(f"-- damages = {dmg}: fleet picks {NAME(x)}, keeps {prof:.3f}; damages {np.round(d, 3)};"
              f" utility gains {np.round(G, 4)}; product {npd}; floor {G.min():.4f}")
        # money-equivalent of resident gains (CV at endowment): w0*(exp(G)-1)
        print(f"   residents' gains as money at endowment: {np.round(W0[1:] * (np.exp(G[1:]) - 1), 3)}")


if __name__ == "__main__":
    linear_report()
    for cal in ["marg", "wta", "wtp", "money"]:
        report(cal)
    for cal in ["marg", "wta"]:
        liability(cal)
