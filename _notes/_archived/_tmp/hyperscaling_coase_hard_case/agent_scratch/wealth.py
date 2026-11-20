"""Wealth-effects row on the hard-case instance (noise schedule).

Switches on: wealth effects (log utility, w0 = (10, 10, 2) residents, 100 fleet).
Everything else at baseline: parametric (additive) harms, once, enforcer assumed,
closed, k = 3 where residents hold the right, no outside option, no remediation.

Two treatments of harm, because the instance writes payoff = t - h in money
(treatment A) and that is undefined when h exceeds wealth; treatment B reads the
harm as a utility loss calibrated at the endowment, h_i / w0_i, which is the
reading under which "sleeps badly" is not a money loss.
"""
import itertools
import math

import numpy as np
from scipy.optimize import minimize

SLOTS = "MDEN"
P = np.array([4.0, 5.5, 4.0, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
S = np.array([1.0, 1.0, 2.0])
W0 = np.array([10.0, 10.0, 2.0])
WF = 100.0

SCHEDULES = [np.array(b) for b in itertools.product([0, 1], repeat=4)]


def name(x):
    return "".join(SLOTS[t] for t in range(4) if x[t]) or "none"


def profit(x):
    return float(P @ x)


def harms(x):
    return S * (E @ x)


def pie(x):
    return profit(x) - harms(x).sum()


def nash_max(gains_fn, n_free, bounds, cons, starts):
    """Maximise sum log(gains) over free transfer vector; return (value, argmax)
    or None when no all-positive gains point is found."""
    best = None
    for s0 in starts:
        def obj(v):
            g = gains_fn(v)
            if np.any(g <= 1e-12):
                return 1e6 + 1e3 * float(np.sum(np.clip(1e-12 - g, 0, None)))
            return -float(np.sum(np.log(g)))
        r = minimize(obj, s0, method="SLSQP", bounds=bounds, constraints=cons,
                     options={"maxiter": 2000, "ftol": 1e-12})
        g = gains_fn(r.x)
        if np.all(g > 1e-9):
            val = float(np.sum(np.log(g)))
            if best is None or val > best[0]:
                best = (val, r.x.copy(), g)
    return best


# ---------------------------------------------------------------- linear baseline
def linear_residents_hold():
    out = {}
    for x in SCHEDULES:
        pi = pie(x)
        if pi <= 0:
            continue
        # transfers t_i to residents; fleet keeps profit - sum t; gains = money
        def gains(t, x=x):
            return np.array([profit(x) - t.sum(), *(t - harms(x))])
        b = nash_max(gains, 3, [(-50, 50)] * 3, (), [harms(x) + pi / 4])
        if b:
            out[name(x)] = (b[0], b[1], b[2])
    return out


# ---------------------------------------------------------------- treatment A
def A_residents_hold():
    """Origin: no slots, everyone at endowment. gains in utility units."""
    out = {}
    for x in SCHEDULES:
        def gains(t, x=x):
            mf = profit(x) - t.sum()
            m = t - harms(x)
            if np.any(W0 + m <= 0) or WF + mf <= 0:
                return np.full(4, -1.0)
            return np.array([math.log(1 + mf / WF), *np.log(1 + m / W0)])
        b = nash_max(gains, 3, [(-50, 50)] * 3, (),
                     [harms(x) + pie(x) / 4, harms(x) + np.array([1, 1, 0.5])])
        if b:
            t = b[1]
            out[name(x)] = dict(logprod=b[0], prod=math.exp(b[0]), t=t,
                                money=np.array([profit(x) - t.sum(), *(t - harms(x))]),
                                gains=b[2])
    return out


def A_fleet_hold_domain():
    """Origin: all four slots. Report resident wealth at the origin."""
    x = np.ones(4)
    return WF + profit(x), W0 - harms(x)


def A_liability(premium=0.0):
    x = max(SCHEDULES, key=pie)
    h = harms(x)
    t = h + premium
    mf = profit(x) - t.sum()
    m = t - h
    g = np.array([math.log(1 + mf / WF), *np.log(1 + m / W0)])
    return name(x), np.array([mf, *m]), g


def A_equal_utility_gain_split(pie_=6.0):
    """Leximin / equal utility gain over no deal: log(1+m_j/w_j) equal -> m_j ∝ w_j."""
    w = np.array([WF, *W0])
    return pie_ * w / w.sum()


# ---------------------------------------------------------------- treatment B
def B_util_harm(x):
    return harms(x) / W0


def B_residents_hold():
    out = {}
    for x in SCHEDULES:
        hu = B_util_harm(x)
        def gains(t, x=x, hu=hu):
            mf = profit(x) - t.sum()
            if WF + mf <= 0 or np.any(W0 + t <= 0):
                return np.full(4, -1.0)
            return np.array([math.log(1 + mf / WF), *(np.log(1 + t / W0) - hu)])
        # WTA_i = w0_i (exp(hu_i) - 1)
        wta = W0 * (np.exp(hu) - 1)
        if wta.sum() >= profit(x):
            out[name(x)] = dict(feasible=False, wta=wta, slack=profit(x) - wta.sum())
            continue
        slack = profit(x) - wta.sum()
        b = nash_max(gains, 3, [(0, 200)] * 3, (),
                     [wta + slack / 4, wta + slack / 8])
        if b:
            t = b[1]
            out[name(x)] = dict(feasible=True, logprod=b[0], prod=math.exp(b[0]), t=t,
                                fleet_money=profit(x) - t.sum(), wta=wta,
                                slack=slack, gains=b[2])
    return out


def B_fleet_hold():
    """Origin: all four slots. Residents pay t_i >= 0 to the fleet, t_i < w0_i."""
    x0 = np.ones(4)
    hu0 = B_util_harm(x0)
    out = {}
    for x in SCHEDULES:
        hu = B_util_harm(x)
        relief = hu0 - hu  # utility relief from moving to x
        wtp = W0 * (1 - np.exp(-relief))  # max payment keeping gain >= 0
        loss = profit(x0) - profit(x)
        out[name(x)] = dict(relief=relief, wtp=wtp, wtp_sum=wtp.sum(), fleet_loss=loss,
                            feasible=wtp.sum() > loss)
    return out


def B_liability():
    """Court awards (i) money damages = harm in money; (ii) damages = WTA."""
    res = {}
    # (i)
    x = max(SCHEDULES, key=pie)
    hu = B_util_harm(x)
    g_money = np.log(1 + harms(x) / W0) - hu
    res["money_damages"] = (name(x), harms(x), g_money)
    # (ii) fleet maximises profit - sum WTA_i(x)
    def net(x):
        return profit(x) - (W0 * (np.exp(B_util_harm(x)) - 1)).sum()
    xb = max(SCHEDULES, key=net)
    res["wta_damages"] = (name(xb), net(xb), W0 * (np.exp(B_util_harm(xb)) - 1))
    res["wta_table"] = {name(x): net(x) for x in SCHEDULES}
    return res


# ---------------------------------------------------------------- compute dial
def flip_probs():
    """Fleet estimates each s_i with error e (sd); slot t's estimated harm error has
    sd e * sqrt(sum_i e_it^2). Slot flips when the error crosses its margin."""
    from math import erf, sqrt
    def Phi(z):
        return 0.5 * (1 + erf(z / sqrt(2)))
    margins = P - (S * E.T).sum(axis=1)  # surplus per slot: (1.5, 3.5, 1, -0.5)
    out = {}
    for e in (1.0, 0.3, 0.1):
        row = {}
        for t in range(4):
            sd = e * math.sqrt((E[:, t] ** 2).sum())
            # N: included wrongly if est surplus > 0, i.e. err_h < margin (margin<0)
            # others: dropped wrongly if err_h > margin
            if margins[t] < 0:
                p = Phi(margins[t] / sd)  # P(err < margin) with margin negative
            else:
                p = 1 - Phi(margins[t] / sd)
            row[SLOTS[t]] = p
        out[e] = row
    return margins, out


def shortfall_cost(eps):
    """Utility loss to each resident of a money shortfall eps from the equal split 1.5
    (treatment A, residents hold the right, MDE)."""
    base = np.log(1 + 1.5 / W0)
    with np.errstate(invalid="ignore", divide="ignore"):
        after = np.log(1 + (1.5 - eps) / W0)
    return base - after


if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    print("== pies ==")
    for x in SCHEDULES:
        print(f"{name(x):5s} profit {profit(x):5.1f} harms {harms(x)} pie {pie(x):5.2f}")

    print("\n== linear, residents hold right: Nash product in money ==")
    lin = linear_residents_hold()
    for k, v in sorted(lin.items(), key=lambda kv: -kv[1][0]):
        print(f"{k:5s} logprod {v[0]:.4f} prod {math.exp(v[0]):.4f} transfers {v[1]} gains {v[2]}")

    print("\n== A: residents hold right, log utility, harm money ==")
    a = A_residents_hold()
    for k, v in sorted(a.items(), key=lambda kv: -kv[1]["logprod"]):
        print(f"{k:5s} logprod {v['logprod']:.5f} prod {v['prod']:.3e} money(f,r1,r2,r3) {v['money']} "
              f"transfers {v['t']} ugains {v['gains']}")

    print("\n== A: fleet holds right, origin wealth ==")
    print(A_fleet_hold_domain())

    print("\n== A: liability ==")
    for prem in (0.0, 1.5):
        print(prem, A_liability(prem))

    print("\n== A: equal utility-gain split of 6 (leximin in utility units) ==")
    print(A_equal_utility_gain_split())
    print("  equal money split 1.5 each: utility gains",
          np.array([math.log(1.015), *np.log(1 + 1.5 / W0)]),
          "product", math.log(1.015) * np.prod(np.log(1 + 1.5 / W0)))

    print("\n== B: residents hold right, harm as utility loss h/w0 ==")
    b = B_residents_hold()
    for k, v in b.items():
        if v["feasible"]:
            print(f"{k:5s} FEASIBLE logprod {v['logprod']:.4f} prod {v['prod']:.3e} t {v['t']} "
                  f"fleet money {v['fleet_money']:.3f} WTA {v['wta']} slack {v['slack']:.3f} ugains {v['gains']}")
        else:
            print(f"{k:5s} infeasible  WTA {v['wta']} sumWTA-profit {-v['slack']:.3f}")

    print("\n== B: fleet holds right ==")
    for k, v in B_fleet_hold().items():
        print(f"{k:5s} wtp {v['wtp']} sum {v['wtp_sum']:.3f} fleet loss {v['fleet_loss']:.1f} feasible {v['feasible']}")

    print("\n== B: liability ==")
    bl = B_liability()
    print("money damages:", bl["money_damages"])
    print("WTA damages:", bl["wta_damages"])
    print("net profit - sum WTA by schedule:", {k: round(v, 3) for k, v in bl["wta_table"].items()})

    print("\n== compute: flip probabilities per slot by fleet estimation error ==")
    margins, fp = flip_probs()
    print("margins", margins)
    for e, row in fp.items():
        print(e, {k: round(v, 4) for k, v in row.items()})

    print("\n== shortfall cost in utility, residents at 1.5 money each ==")
    for eps in (0.5, 1.0, 2.0, 3.0, 3.5):
        print(eps, shortfall_cost(eps))
