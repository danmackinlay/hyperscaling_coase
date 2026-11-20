"""Base instance, finite-budgets switch, proposer drawn by party (fast version).

Same model as seat_noise.py. The proposer's optimal shade depends on one
scalar (fleet: its estimated margin M = 13.5 - sum of estimated harms;
resident: her estimated pie), so it is tabulated once per seat and
interpolated. Reports money gains and, under wealth effects, utility gains,
the criterion (geometric mean of expected gains as a fraction of its maximum),
the floor, the deal rate, per-seat residuals, and each resident against the
ordinance status quo.
"""
import sys
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize_scalar, minimize

PROFIT = 13.5
HARM = np.array([1.0, 2.5, 4.0])
PIE = PROFIT - HARM.sum()
W0LOG = np.array([10.0, 10.0, 2.0, 100.0])  # A, B, C, F
ORDINANCE = np.array([-1.0, -2.5, -4.0, 13.5])  # night closed, no compensation


def ugain(x, w0):
    return x if w0 is None else np.log1p(x / w0)


def cdf(z, shape):
    if shape == "normal":
        return norm.cdf(z)
    a = np.sqrt(3.0)
    return np.clip((z + a) / (2 * a), 0.0, 1.0)


def noise(size, sig, shape, rng):
    if shape == "normal":
        return sig * rng.standard_normal(size)
    return sig * np.sqrt(3) * rng.uniform(-1, 1, size)


def fleet_shade_table(sig_f, wf, shape):
    Ms = np.linspace(-6, 14, 401)
    ms = np.empty_like(Ms)
    for k, M in enumerate(Ms):
        def neg(m):
            p = cdf(m / sig_f, shape) ** 3
            return -p * ugain(max(M - 3 * m, -0.999 * (wf or 1e9)) if wf else M - 3 * m, wf)
        r = minimize_scalar(neg, bounds=(-2.0, 6.0), method="bounded")
        ms[k] = r.x
    return Ms, ms


def resident_shade_table(sig_pie, wi, shape):
    Ps = np.linspace(-4, 16, 401)
    xs = np.empty_like(Ps)
    for k, P in enumerate(Ps):
        def neg(x):
            return -cdf((P - x) / sig_pie, shape) * ugain(x, wi)
        r = minimize_scalar(neg, bounds=(0.0, 14.0), method="bounded")
        xs[k] = r.x
    return Ps, xs


def fleet_seat(sig_f, util, shape, rng, n):
    """Returns (n,4) money gains when the fleet proposes."""
    g = np.zeros((n, 4))
    if sig_f == 0:
        g[:, 3] = PIE
        return g
    wf = None if util == "lin" else W0LOG[3]
    Ms, ms = fleet_shade_table(sig_f, wf, shape)
    est = HARM + noise((n, 3), sig_f, shape, rng)
    M = PROFIT - est.sum(1)
    m = np.interp(M, Ms, ms)
    offers = est + m[:, None]
    ok = np.all(offers >= HARM, axis=1)
    g[ok, :3] = offers[ok] - HARM
    g[ok, 3] = PROFIT - offers[ok].sum(1)
    return g


def resident_seat(i, sig_n, util, shape, rng, n):
    """Regime R1: residents know each other's harms; the fleet's pie is the gamble."""
    g = np.zeros((n, 4))
    if sig_n == 0:
        g[:, i] = PIE
        return g
    wi = None if util == "lin" else W0LOG[i]
    sig_pie = sig_n * np.sqrt(3)
    Ps, xs = resident_shade_table(sig_pie, wi, shape)
    pest = PIE + noise(n, sig_pie, shape, rng)
    x = np.interp(pest, Ps, xs)
    ok = x <= PIE
    g[ok, i] = x[ok]
    g[ok, 3] = PIE - x[ok]
    return g


def utility_max(util):
    """Largest geometric mean over divisions of the pie: equal split (lin) or
    the utility-Nash division (log)."""
    if util == "lin":
        return 1.5, np.array([1.5] * 4)

    def neg(v):
        x = np.append(v, PIE - v.sum())
        if np.any(x <= 0):
            return 1e6
        return -np.log(np.log1p(x / W0LOG)).sum()
    r = minimize(neg, x0=[1.5, 1.5, 1.5], method="Nelder-Mead",
                 options={"xatol": 1e-8, "fatol": 1e-10})
    x = np.append(r.x, PIE - r.x.sum())
    u = np.log1p(x / W0LOG)
    return np.exp(np.log(u).mean()), x


def run(sig_f, sig_n, util, shape, n, seed=0):
    rng = np.random.default_rng(seed)
    seats = [fleet_seat(sig_f, util, shape, rng, n)]
    for i in range(3):
        seats.append(resident_seat(i, sig_n, util, shape, rng, n))
    seats = np.array(seats)  # (4 seats, n, 4 parties) money gains
    w0 = None if util == "lin" else W0LOG
    ug = seats if w0 is None else np.log1p(seats / w0)
    exp_money = seats.mean(1).mean(0)
    exp_util = ug.mean(1).mean(0)
    deal = (seats.sum(2) > 0).mean()
    seat_money = seats.mean(1)  # (4 seats, 4 parties)
    return exp_money, exp_util, deal, seat_money


def report(util, shape, cases, n):
    gmax, xmax = utility_max(util)
    print(f"\n=== utility={util} noise={shape} regime=R1 draws={n} "
          f"| max gm {gmax:.4f} at division {np.round(xmax, 3)} ===")
    print("case (sig_f:sig_n)   | E[gain] A B C F (money) | E[gain] in criterion units "
          "| deal | gm/max | floor | Carol vs ordinance | fleet residual per resident seat (A,B,C) | Carol windfall on fleet seat")
    for name, sf, sn in cases:
        em, eu, d, sm = run(sf, sn, util, shape, n)
        pos = eu[eu > 0]
        gm = np.exp(np.log(pos).mean()) if len(pos) else 0.0
        print(f"{name:18s} | {em[0]:.3f} {em[1]:.3f} {em[2]:.3f} {em[3]:.3f} "
              f"| {eu[0]:.3f} {eu[1]:.3f} {eu[2]:.3f} {eu[3]:.3f} "
              f"| {d:.3f} | {gm / gmax:.3f} | {eu.min():.3f} "
              f"| {em[2] - ORDINANCE[2]:+.2f} "
              f"| {sm[1, 3]:.3f} {sm[2, 3]:.3f} {sm[3, 3]:.3f} | {sm[0, 2]:.3f}")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
    cases = [
        ("limit 0:0", 0.0, 0.0),
        ("1:1   1:1", 1.0, 1.0),
        ("1:1   .3:.3", 0.3, 0.3),
        ("1:1   .1:.1", 0.1, 0.1),
        ("10:1  .3:1", 0.3, 1.0),
        ("10:1  .1:.3", 0.1, 0.3),
        ("1:10  1:.3", 1.0, 0.3),
        ("1:10  .3:.1", 0.3, 0.1),
        ("100:1 .1:1", 0.1, 1.0),
        ("1:100 1:.1", 1.0, 0.1),
    ]
    for util in ["lin", "log"]:
        for shape in ["normal", "uniform"]:
            report(util, shape, cases, n)
