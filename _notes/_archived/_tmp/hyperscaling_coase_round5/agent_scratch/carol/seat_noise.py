"""Base instance (noise schedule), finite-budgets switch, proposer drawn by party.

Four parties: fleet F, Alice (1), Bob (2), Carol (3). Schedule fixed at M,D,E:
profit 13.5, harms (1, 2.5, 4), pie 6. Consent k=3, transfers, one shot, enforcer.

Protocol: one party is drawn uniformly to propose a payment vector; every other
party accepts iff its gain over no deal is >= 0; otherwise no deal (0 for all).

Estimation (the dial): the fleet estimates each resident's harm with error
sigma_f (normal, independent); a resident estimates each slot profit with error
sigma_N, so the pie with error sigma_N*sqrt(3). Residents observe each other's
harms (neighbours; info regime R1). Regime R2 (robustness): a resident also
estimates the other two harms with error sigma_N.

Each proposer is Bayesian with a flat prior and maximises its own expected gain
(money, or log-utility gain when wealth effects are on) by choosing how far to
shade. Robustness: uniform noise of the same sd; grid resolution.
"""
import sys
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize_scalar

PROFIT = 13.5
HARM = np.array([1.0, 2.5, 4.0])
PIE = PROFIT - HARM.sum()
W0 = {"lin": None, "log": np.array([10.0, 10.0, 2.0, 100.0])}  # A, B, C, F
RNG = np.random.default_rng(0)
NDRAW = 20000


def ugain(x, w0):
    """Gain over no deal in the party's units: money, or log-utility."""
    if w0 is None:
        return x
    return np.log1p(np.maximum(x, -w0 + 1e-9) / w0)


def cdf(z, shape):
    if shape == "normal":
        return norm.cdf(z)
    # uniform with sd 1: half-width sqrt(3)
    a = np.sqrt(3.0)
    return np.clip((z + a) / (2 * a), 0.0, 1.0)


def fleet_seat(sig_f, util, shape):
    """Fleet proposes. Returns expected gains (A,B,C,F) and deal rate."""
    if sig_f == 0:
        g = np.array([0.0, 0.0, 0.0, PIE])
        return g, 1.0
    w0 = W0[util]
    est = HARM + sig_f * RNG.standard_normal((NDRAW, 3)) if shape == "normal" else \
        HARM + sig_f * np.sqrt(3) * RNG.uniform(-1, 1, (NDRAW, 3))
    gains = np.zeros((NDRAW, 4))
    deals = np.zeros(NDRAW)
    # by symmetry of the three errors the optimal shade m is common; 1-D search
    for n in range(NDRAW):
        M = PROFIT - est[n].sum()
        wf = None if w0 is None else w0[3]

        def neg(m):
            p = cdf(m / sig_f, shape) ** 3
            return -p * ugain(M - 3 * m, wf)

        r = minimize_scalar(neg, bounds=(-2.0, 6.0), method="bounded")
        m = r.x
        offers = est[n] + m
        if np.all(offers >= HARM):
            deals[n] = 1
            gains[n, :3] = offers - HARM
            gains[n, 3] = PROFIT - offers.sum()
    return gains.mean(0), deals.mean()


def resident_seat(i, sig_n, util, shape, regime):
    """Resident i proposes. Returns expected gains (A,B,C,F) and deal rate."""
    w0 = W0[util]
    wi = None if w0 is None else w0[i]
    others = [j for j in range(3) if j != i]
    if sig_n == 0:
        g = np.zeros(4)
        g[i] = PIE
        return g, 1.0
    sig_pie = sig_n * np.sqrt(3)
    if shape == "normal":
        pie_est = PIE + sig_pie * RNG.standard_normal(NDRAW)
        harm_est = HARM[others] + sig_n * RNG.standard_normal((NDRAW, 2))
    else:
        pie_est = PIE + sig_pie * np.sqrt(3) * RNG.uniform(-1, 1, NDRAW)
        harm_est = HARM[others] + sig_n * np.sqrt(3) * RNG.uniform(-1, 1, (NDRAW, 2))
    gains = np.zeros((NDRAW, 4))
    deals = np.zeros(NDRAW)
    for n in range(NDRAW):
        if regime == "R1":
            # knows the others' harms; pays them harm exactly; only the fleet is a gamble
            def neg(x):
                return -cdf((pie_est[n] - x) / sig_pie, shape) * ugain(x, wi)
            r = minimize_scalar(neg, bounds=(0.0, 12.0), method="bounded")
            x = r.x
            offers = HARM.copy()
            offers[i] = HARM[i] + x
        else:
            # R2: also gambles on the neighbours' harms, shading each by m
            def neg2(v):
                x, m = v
                pa = cdf(m / sig_n, shape) ** 2
                pf = cdf((pie_est[n] - x - 2 * m) / sig_pie, shape)
                return -pa * pf * ugain(x, wi)
            best = None
            for m0 in np.linspace(-0.5, 2.5, 13):
                for x0 in np.linspace(0.5, 6.0, 12):
                    val = neg2((x0, m0))
                    if best is None or val < best[0]:
                        best = (val, x0, m0)
            # refine
            from scipy.optimize import minimize
            r = minimize(neg2, x0=[best[1], best[2]], method="Nelder-Mead",
                         options={"xatol": 1e-3, "fatol": 1e-6})
            x, m = r.x
            offers = np.zeros(3)
            offers[i] = HARM[i] + x
            offers[others] = harm_est[n] + m
        fleet_gain = PROFIT - offers.sum()
        if fleet_gain >= 0 and np.all(offers >= HARM):
            deals[n] = 1
            gains[n, :3] = offers - HARM
            gains[n, 3] = fleet_gain
    return gains.mean(0), deals.mean()


def run(sig_f, sig_n, util="lin", shape="normal", regime="R1"):
    gF, dF = fleet_seat(sig_f, util, shape)
    seats = [gF]
    deals = [dF]
    for i in range(3):
        g, d = resident_seat(i, sig_n, util, shape, regime)
        seats.append(g)
        deals.append(d)
    exp_gain = np.mean(seats, axis=0)  # proposer drawn by party, 1/4 each
    deal_rate = np.mean(deals)
    w0 = W0[util]
    ug = exp_gain if w0 is None else ugain(exp_gain, w0)  # expected money gain -> utility? no: see below
    return exp_gain, deal_rate, seats


def criterion(exp_gain_money, util):
    """Geometric mean of expected gains (failed deal = 0), fraction of max.

    Under wealth effects the gain is in utility units: we convert each party's
    expected money gain per outcome realisation inside the seats, so here we
    pass utility gains already. Max at n=4 under linear money: equal split 1.5
    each -> gm 1.5."""
    g = np.array(exp_gain_money)
    pos = g[g > 0]
    gm = np.exp(np.log(pos).mean()) if len(pos) else 0.0
    return gm, g.min(), (g[:3] <= 0).sum()


def fmt(v):
    return " ".join(f"{x:6.3f}" for x in v)


if __name__ == "__main__":
    NDRAW = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    cases = [
        ("limit  0  :0  ", 0.0, 0.0),
        ("1:1   1  :1  ", 1.0, 1.0),
        ("1:1   .3 :.3 ", 0.3, 0.3),
        ("1:1   .1 :.1 ", 0.1, 0.1),
        ("10:1  .3 :1  ", 0.3, 1.0),
        ("10:1  .1 :.3 ", 0.1, 0.3),
        ("1:10  1  :.3 ", 1.0, 0.3),
        ("1:10  .3 :.1 ", 0.3, 0.1),
    ]
    for util in ["lin", "log"]:
        for shape in ["normal", "uniform"]:
            for regime in ["R1", "R2"]:
                if (shape == "uniform" or regime == "R2") and util == "log":
                    continue
                if shape == "uniform" and regime == "R2":
                    continue
                print(f"\n=== utility={util} noise={shape} regime={regime} "
                      f"(expected gains A B C F; deal rate; gm; floor; n_below) ===")
                for name, sf, sn in cases:
                    g, d, seats = run(sf, sn, util, shape, regime)
                    gm, fl, nb = criterion(g, util)
                    print(f"{name} | {fmt(g)} | deal {d:5.3f} | gm {gm:5.3f} "
                          f"| floor {fl:6.3f} | below {nb} || carol-seat {fmt(seats[3])}")
