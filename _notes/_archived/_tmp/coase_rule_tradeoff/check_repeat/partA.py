"""Part A: Carol alone. Exact (quadrature) integration, no Monte Carlo.

Belief given signal x: normal(x, sigma) restricted to [L, U] (uniform if sigma=inf).
All per-x quantities are closed-form truncated-normal integrals; x is integrated
numerically against its marginal density with the trapezoid rule.
"""
import sys
import numpy as np
from scipy.special import ndtr

L, U = 0.5, 2.5
P, e = 5.0, 2.0
DELTA = 1.0


def phi(z):
    return np.exp(-0.5 * z * z) / np.sqrt(2 * np.pi)


def ndiff(a, b):
    """ndtr(b) - ndtr(a), stable in both tails (a <= b)."""
    pos = a > 0
    return np.where(pos, ndtr(-a) - ndtr(-b), ndtr(b) - ndtr(a))


class Belief:
    def __init__(self, x, sig):
        self.x = x
        self.sig = sig

    def M(self, lo, hi):
        hi = np.maximum(hi, lo)
        if self.sig is None:
            return (hi - lo) / (U - L)
        a = (lo - self.x) / self.sig
        b = (hi - self.x) / self.sig
        return ndiff(a, b)

    def PM(self, lo, hi):
        hi = np.maximum(hi, lo)
        if self.sig is None:
            return (hi**2 - lo**2) / 2 / (U - L)
        a = (lo - self.x) / self.sig
        b = (hi - self.x) / self.sig
        return self.x * ndiff(a, b) - self.sig * (phi(b) - phi(a))


def golden_max(f, a, b, iters=90):
    g = (np.sqrt(5) - 1) / 2
    a = np.array(a, float)
    b = np.array(b, float)
    c = b - g * (b - a)
    d = a + g * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(iters):
        m = fc > fd
        # m: keep [a, d]; new interior c' = b' - g(b'-a), old c becomes d
        # ~m: keep [c, b]; new interior d' = a' + g(b-a'), old d becomes c
        nb = np.where(m, d, b)
        na = np.where(m, a, c)
        newpt = np.where(m, nb - g * (nb - na), na + g * (nb - na))
        fnew = f(newpt)
        c_new = np.where(m, newpt, d)
        fc_new = np.where(m, fnew, fd)
        d_new = np.where(m, c, newpt)
        fd_new = np.where(m, fc, fnew)
        a, b, c, d, fc, fd = na, nb, c_new, d_new, fc_new, fd_new
    return (a + b) / 2


def one_round(bel, lo, hi):
    """Optimal one-round rate on interval belief [lo, hi]. Returns (rate, profit, asked)."""
    Z = bel.M(lo, hi)
    f = lambda r: bel.M(lo, r) / Z * (P - e * r)
    r = golden_max(f, lo, hi)
    pr = f(r)
    pend = P - e * hi
    r = np.where(pend > pr, hi, r)
    pr = np.maximum(pr, pend)
    asked = pr > 0
    return r, np.where(asked, pr, 0.0), asked


def carol_gain(bel, lo, hi, r, asked, Ztot):
    """Carol's gain integrated over types in [lo, hi] (unnormalised by Ztot) at rate r."""
    top = np.clip(r, lo, hi)
    g = e * (r * bel.M(lo, top) - bel.PM(lo, top)) / Ztot
    return np.where(asked, g, 0.0)


def two_round(bel, c, kind):
    """kind: 'strategic' (c is the cutoff, rate from indifference) or 'myopic' (c = r1).
    Returns dict of two-round sums (company, carol) as arrays over c."""
    Ztot = bel.M(L, U)
    pa = bel.M(L, c) / Ztot
    r2a, pia, aska = one_round(bel, L + 0 * c, c)
    r2r, pir, askr = one_round(bel, c, U + 0 * c)
    if kind == 'strategic':
        G = np.where(askr, e * (r2r - c), 0.0)
        r1 = c + DELTA * G / e
    else:
        r1 = c
    comp = pa * (P - e * r1) + DELTA * (pa * pia + (1 - pa) * pir)
    car1 = e * (r1 * bel.M(L, c) - bel.PM(L, c)) / Ztot
    car2 = carol_gain(bel, L + 0 * c, c, r2a, aska, Ztot) + carol_gain(bel, c, U + 0 * c, r2r, askr, Ztot)
    car = car1 + DELTA * car2
    return dict(comp=comp, car=car, r1=r1, r2a=r2a, r2r=r2r, pa=pa)


def check_eq_strategic(bel, c, out, ngrid=2001):
    """Return min over types of the sign-correct margin (should be >= -tol)."""
    s = np.linspace(L, U, ngrid)
    r1, r2a, r2r = out['r1'], out['r2a'], out['r2r']
    acc = (r1 - s) * e + DELTA * e * np.maximum(r2a - s, 0)
    ref = DELTA * e * np.maximum(r2r - s, 0)
    D = acc - ref
    bad_below = np.min(np.where(s < c, D, np.inf))
    bad_above = np.min(np.where(s > c, -D, np.inf))
    return min(bad_below, bad_above)


def solve_given_x(x, sig, ngrid=401):
    bel = Belief(x, sig)
    Ztot = bel.M(L, U)
    # forget
    r0, pi0, ask0 = one_round(bel, np.array(L), np.array(U))
    car0 = carol_gain(bel, np.array(L), np.array(U), r0, ask0, Ztot)
    res = {'forget': (float(pi0), float(car0), {'rate': float(r0)})}
    # options none/top for both two-round regimes
    none_c = (DELTA * pi0, DELTA * car0)  # round one nothing; round two = forget
    top_comp = (P - e * U) + DELTA * pi0
    top_car = e * (U * Ztot - bel.PM(L, U)) / Ztot + DELTA * car0
    for kind in ('myopic', 'strategic'):
        cg = L + (U - L) * np.arange(1, ngrid + 1) / (ngrid + 1)
        out = two_round(bel, cg, kind)
        k = int(np.argmax(out['comp']))
        lo = cg[max(k - 1, 0)] if k > 0 else L + 1e-9
        hi = cg[min(k + 1, ngrid - 1)] if k < ngrid - 1 else U - 1e-9
        cbest = float(golden_max(lambda cc: two_round(bel, cc, kind)['comp'], np.array(lo), np.array(hi)))
        ob = two_round(bel, np.array(cbest), kind)
        cand = [('cut', float(ob['comp']), float(ob['car']), cbest, float(ob['r1']))]
        cand.append(('none', float(none_c[0]), float(none_c[1]), None, None))
        cand.append(('top', float(top_comp), float(top_car), None, U))
        best = max(cand, key=lambda t: t[1])
        info = {'choice': best[0], 'cutoff': best[3], 'r1': best[4],
                'cands': cand}
        if kind == 'strategic' and best[0] == 'cut':
            info['eq_margin'] = check_eq_strategic(bel, cbest, {k2: float(v) for k2, v in ob.items()})
            info['r2a'] = float(ob['r2a']); info['r2r'] = float(ob['r2r'])
        res[kind] = (best[1] / (1 + DELTA), best[2] / (1 + DELTA), info)
    return res


def main():
    print("Sanity anchor (uniform [0.5,2.5], e=1, P=3):")
    global P, e
    P0, e0 = P, e
    P, e = 3.0, 1.0
    r = solve_given_x(0.0, None)
    print("  one-round rate %.6f profit %.6f" % (r['forget'][2]['rate'], r['forget'][0]))
    i = r['strategic'][2]
    print("  strategic cutoff %.6f r1 %.6f total two-round profit %.6f" % (i['cutoff'], i['r1'], 2 * r['strategic'][0]))
    P, e = P0, e0

    for sig in (None, 0.3, 0.1):
        if sig is None:
            r = solve_given_x(0.0, None)
            print("\nsigma=inf")
            for k in ('forget', 'myopic', 'strategic'):
                comp, car, info = r[k]
                print("  %-9s total %.6f company %.6f carol %.6f" % (k, comp + car, comp, car))
                print("     ", {kk: v for kk, v in info.items() if kk != 'cands'})
                if k != 'forget':
                    print("      candidates:", info['cands'])
            continue
        for nx in (int(sys.argv[1]) if len(sys.argv) > 1 else 241, ):
            xs = np.linspace(L - 7 * sig, U + 7 * sig, nx)
            px = 0.5 * ndiff((xs - U) / sig, (xs - L) / sig) / (U - L) * 2  # density of x: (1/(U-L)) * int phi
            px = px / 2  # uniform density 1/2 times integral of normal pdf over s
            px = ndiff((xs - U) / sig, (xs - L) / sig) / (U - L)
            w = np.trapezoid(px, xs) if hasattr(np, 'trapezoid') else np.trapz(px, xs)
            acc = {k: np.zeros((nx, 2)) for k in ('forget', 'myopic', 'strategic')}
            choices = {'myopic': {}, 'strategic': {}}
            minmargin = np.inf
            for j, x in enumerate(xs):
                r = solve_given_x(x, sig)
                for k in acc:
                    acc[k][j] = r[k][0], r[k][1]
                for k in choices:
                    ch = r[k][2]['choice']
                    choices[k][ch] = choices[k].get(ch, 0) + 1
                if 'eq_margin' in r['strategic'][2]:
                    minmargin = min(minmargin, r['strategic'][2]['eq_margin'])
            print("\nsigma=%g  (x grid %d points on [L-7s, U+7s], mass of x density on grid %.8f)" % (sig, nx, w))
            for k in acc:
                integ = lambda v: (np.trapezoid(v * px, xs) if hasattr(np, 'trapezoid') else np.trapz(v * px, xs)) / w
                comp = integ(acc[k][:, 0]); car = integ(acc[k][:, 1])
                print("  %-9s total %.6f company %.6f carol %.6f" % (k, comp + car, comp, car))
            print("  choices per x-node:", choices, " min eq margin (strategic):", minmargin)


if __name__ == '__main__':
    main()
