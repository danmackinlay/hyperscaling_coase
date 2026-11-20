"""Independent re-implementation of spec.md (four bargaining rules)."""

import itertools

import numpy as np
from scipy.special import log_ndtr

P = np.array([4.0, 5.5, 4.0, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
S_LO, S_HI = 0.5, 2.5
M_LO, M_HI = 0.6, 1.4
INS_COST = 2.0
SUBSETS = [tuple(c) for k in range(4) for c in itertools.combinations(range(3), k)]
# SUBSETS ordered by size: (), (0,), (1,), (2,), (0,1), ... ; index 0 = no insulation
LOG2PI = 0.5 * np.log(2 * np.pi)


def weights(S):
    """Exposure after insulation, shape (3,4)."""
    w = E.copy()
    for i in S:
        w[i] *= 0.5
    return w


def logdiff(a, b):
    """log(Phi(b)-Phi(a)) for a<=b, stable."""
    flip = a > 0
    a2 = np.where(flip, -b, a)
    b2 = np.where(flip, -a, b)
    la, lb = log_ndtr(a2), log_ndtr(b2)
    with np.errstate(divide="ignore", invalid="ignore"):
        return lb + np.log(-np.expm1(la - lb))


class Belief:
    """Posterior on [lo,hi]: uniform (sd=inf) or truncated normal (mu, sd)."""

    def __init__(self, mu, sd, lo, hi):
        self.mu, self.sd, self.lo, self.hi = mu, sd, lo, hi
        self.uniform = np.isinf(sd)
        if not self.uniform:
            self.a = (lo - mu) / sd
            self.b = (hi - mu) / sd
            self.logZ = logdiff(self.a, self.b)

    def logF(self, r):
        if self.uniform:
            with np.errstate(divide="ignore"):
                return np.log(np.clip((r - self.lo) / (self.hi - self.lo), 0, 1))
        x = np.clip((r - self.mu) / self.sd, self.a, self.b)
        return logdiff(self.a, x) - self.logZ

    def logS(self, r):
        if self.uniform:
            with np.errstate(divide="ignore"):
                return np.log(np.clip((self.hi - r) / (self.hi - self.lo), 0, 1))
        x = np.clip((r - self.mu) / self.sd, self.a, self.b)
        return logdiff(x, self.b) - self.logZ

    def log_F_over_f(self, r):
        if self.uniform:
            with np.errstate(divide="ignore"):
                return np.log(r - self.lo)
        x = (r - self.mu) / self.sd
        return np.log(self.sd) + logdiff(self.a, x) + x * x / 2 + LOG2PI

    def log_S_over_f(self, r):
        if self.uniform:
            with np.errstate(divide="ignore"):
                return np.log(self.hi - r)
        x = (r - self.mu) / self.sd
        return np.log(self.sd) + logdiff(x, self.b) + x * x / 2 + LOG2PI


def invert_inc(belief, logtarget, lo, hi, iters=48):
    """Solve log(F/f)(r) = logtarget on [lo,hi] (increasing); clamps to hi."""
    a = np.full_like(logtarget, lo)
    b = np.full_like(logtarget, hi)
    for _ in range(iters):
        mid = 0.5 * (a + b)
        go_up = belief.log_F_over_f(mid) < logtarget
        a = np.where(go_up, mid, a)
        b = np.where(go_up, b, mid)
    return 0.5 * (a + b)


def invert_dec(belief, logtarget, lo, hi, iters=48):
    """Solve log(S/f)(d) = logtarget on [lo,hi] (decreasing); clamps to lo."""
    a = np.full_like(logtarget, lo)
    b = np.full_like(logtarget, hi)
    for _ in range(iters):
        mid = 0.5 * (a + b)
        go_up = belief.log_S_over_f(mid) > logtarget
        a = np.where(go_up, mid, a)
        b = np.where(go_up, b, mid)
    return 0.5 * (a + b)


def solve_slot(V, ws, hbeliefs, mbelief=None, Pt=None, c=None, iters=56):
    """Maximise prob * margin for one slot.

    Rule A form (mbelief None): margin = V - sum w_i r_i.
    Rule C form: margin = d*Pt - sum w_i r_i - c, company accepts iff m>=d.
    ws: list of scalar weights (>0); hbeliefs: matching Beliefs.
    Returns (ev, rs list, d or None, offer flag); all arrays of shape (N,).
    Method: log-concave objective; FOCs give r_i(Pi), d(Pi) monotone in the
    margin Pi; bisect the fixed point Pi = margin(r(Pi), d(Pi)).
    """
    sumw = sum(ws)
    if mbelief is None:
        pimax = V - S_LO * sumw
    else:
        pimax = M_HI * Pt - c - S_LO * sumw
    pimax = np.asarray(pimax, dtype=float)
    offer = pimax > 0
    top = np.where(offer, pimax, 1.0)

    def resp(pi):
        lp = np.log(np.maximum(pi, 1e-300))
        rs = [invert_inc(hb, lp - np.log(w), S_LO, S_HI) for w, hb in zip(ws, hbeliefs)]
        d = None if mbelief is None else invert_dec(mbelief, lp - np.log(Pt), M_LO, M_HI)
        return rs, d

    def margin(rs, d):
        base = V if mbelief is None else d * Pt - c
        return base - sum(w * r for w, r in zip(ws, rs))

    a = np.zeros_like(top)
    b = top.copy()
    for _ in range(iters):
        mid = 0.5 * (a + b)
        rs, d = resp(mid)
        g = mid - margin(rs, d)
        a = np.where(g < 0, mid, a)
        b = np.where(g < 0, b, mid)
    rs, d = resp(0.5 * (a + b))
    mg = margin(rs, d)
    logp = sum(hb.logF(r) for hb, r in zip(hbeliefs, rs))
    if mbelief is not None:
        logp = logp + mbelief.logS(d)
    ev = np.where(offer, np.exp(logp) * mg, 0.0)
    offer = offer & (ev > 0)
    return np.where(offer, ev, 0.0), rs, d, offer


def full_info(s, m, insul):
    """Returns total (N,) of the full-information optimum."""
    best = None
    for k, S in enumerate(SUBSETS if insul else SUBSETS[:1]):
        w = weights(S)
        harm = np.einsum("in,it->nt", s, w)
        tot = np.maximum(0, m[:, None] * P - harm).sum(1) - INS_COST * len(S)
        best = tot if best is None else np.maximum(best, tot)
    return best


def offer_maker(s, m, insul, maker, sig_s, sig_m, sigma):
    """Rule A (maker=-1, company) or household seat (maker=j).

    s: (3,N), m: (N,), sig_s: (3,N) signals of households held by the maker,
    sig_m: (N,) signal of m held by the maker (unused for company).
    Returns realised gains: company (N,), households (3,N).
    """
    N = m.shape[0]
    subsets = SUBSETS if insul else SUBSETS[:1]
    point = sigma == 0
    hb = None if point else [Belief(sig_s[i], sigma, S_LO, S_HI) for i in range(3)]
    mb = None
    if maker >= 0 and not point:
        mb = Belief(sig_m, 0.4 * sigma, M_LO, M_HI)
    best_ev = np.full(N, -np.inf)
    comp = np.zeros(N)
    hh = np.zeros((3, N))
    for S in subsets:
        w = weights(S)
        ev_tot = -INS_COST * len(S) * np.ones(N)
        comp_S = np.zeros(N)
        hh_S = np.zeros((3, N))
        # maker pays insulation
        if maker < 0:
            comp_S -= INS_COST * len(S)
        else:
            hh_S[maker] -= INS_COST * len(S)
        for t in range(4):
            others = [i for i in range(3) if w[i, t] > 0 and i != maker]
            ws = [w[i, t] for i in others]
            cj = s[maker] * w[maker, t] if maker >= 0 else None
            if point:
                # exact knowledge: r_i = s_i, d = m
                rs = [s[i] for i in others]
                if maker < 0:
                    mg = m * P[t] - sum(wi * r for wi, r in zip(ws, rs))
                    d = None
                else:
                    d = m.copy()
                    mg = d * P[t] - sum(wi * r for wi, r in zip(ws, rs)) - cj
                offer = mg > 0
                ev = np.where(offer, mg, 0.0)
            elif maker < 0:
                ev, rs, d, offer = solve_slot(m * P[t], ws, [hb[i] for i in others])
            else:
                ev, rs, d, offer = solve_slot(
                    None, ws, [hb[i] for i in others], mb, P[t], cj
                )
            ev_tot = ev_tot + ev
            run = offer.copy()
            for i, r in zip(others, rs):
                run &= s[i] <= r
            if maker >= 0:
                run &= m >= d
            pay = sum(wi * r for wi, r in zip(ws, rs))
            for i, r, wi in zip(others, rs, ws):
                hh_S[i] += np.where(run, wi * (r - s[i]), 0.0)
            if maker < 0:
                comp_S += np.where(run, m * P[t] - pay, 0.0)
            else:
                comp_S += np.where(run, (m - d) * P[t], 0.0)
                hh_S[maker] += np.where(run, d * P[t] - pay - cj, 0.0)
        better = ev_tot > best_ev
        best_ev = np.where(better, ev_tot, best_ev)
        comp = np.where(better, comp_S, comp)
        hh = np.where(better, hh_S, hh)
    return comp, hh


def uniform_rate(s, m, insul, r, consent, prefer_insulate=False):
    """Rules B1 (consent=True) and B2. Returns company (N,), households (3,N), ties (N,)."""
    N = m.shape[0]
    veto = s > r  # (3,N)
    subsets = SUBSETS if insul else SUBSETS[:1]
    cands = []
    for S in subsets:
        w = weights(S)
        cS = -INS_COST * len(S) * np.ones(N)
        hS = np.zeros((3, N))
        for t in range(4):
            allowed = np.ones(N, bool)
            if consent:
                for i in range(3):
                    if w[i, t] > 0:
                        allowed &= ~veto[i]
            pi = m * P[t] - r * w[:, t].sum()
            run = allowed & (pi >= -1e-12)
            cS += np.where(run, pi, 0)
            for i in range(3):
                hS[i] += np.where(run, w[i, t] * (r - s[i]), 0)
        cands.append((cS, hS))
    allc = np.array([c for c, _ in cands])  # (K,N)
    best = allc.max(0)
    near = allc >= best - 1e-9
    ties = near.sum(0) > 1
    # among maximisers: fewest insulated (first index) or most (last index)
    K = len(cands)
    if prefer_insulate:
        k = K - 1 - np.argmax(near[::-1], axis=0)
    else:
        k = np.argmax(near, axis=0)
    comp = allc[k, np.arange(N)]
    allh = np.array([h for _, h in cands])  # (K,3,N)
    hh = allh[k, :, np.arange(N)].T
    return comp, hh, ties
