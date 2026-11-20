"""Street model, sigma = inf (uniform beliefs on intervals). Exact integration throughout.

Round-two solver: for every named-slot subset S, maximise expected profit over the
rates of the households exposed to S. Global search = full grid (NG points per
household on its belief interval) followed by exact coordinate ascent (each
coordinate's optimum is closed form because F_i is linear on its interval).
"""
import itertools
import numpy as np

L, U = 0.5, 2.5
P = np.array([4.0, 5.5, 4.0, 5.0])
EXP = np.array([[0.5, 0, 0.5, 1],
                [1, 1, 0.5, 0.5],
                [0.5, 0.5, 1, 2]])
NH, NS = 3, 4
SUBSETS = [tuple(t for t in range(NS) if (m >> t) & 1) for m in range(1, 16)]
SLOTN = 'MDEN'


def exposed(S):
    return sorted({i for t in S for i in range(NH) if EXP[i, t] > 0})


def F(r, a, b):
    return np.clip((r - a) / (b - a), 0.0, 1.0)


def profit(S, r, a, b):
    """Expected profit, broadcasting. r, a, b shape (..., 3)."""
    Fs = F(r, a, b)
    tot = 0.0
    for t in S:
        q = 1.0
        pay = 0.0
        for i in range(NH):
            if EXP[i, t] > 0:
                q = q * Fs[..., i]
                pay = pay + r[..., i] * EXP[i, t]
        tot = tot + q * (P[t] - pay)
    return tot


def exposure_after(S, r, a, b, i):
    """Expected exposure of household i (if it accepts) given others' acceptance probs."""
    Fs = F(r, a, b)
    X = 0.0
    for t in S:
        if EXP[i, t] == 0:
            continue
        q = 1.0
        for j in range(NH):
            if j != i and EXP[j, t] > 0:
                q = q * Fs[..., j]
        X = X + EXP[i, t] * q
    return X


def solve_round2(a, b, NG=9, sweeps=80, chunk=1500):
    """a, b: (K, 3) belief intervals. Returns profit (K,), rates (K,3; 0 = not asked), subset index (K,; -1 = none)."""
    K = a.shape[0]
    best = np.zeros(K)
    best_r = np.zeros((K, NH))
    best_s = -np.ones(K, int)
    u = np.linspace(0, 1, NG)
    for si, S in enumerate(SUBSETS):
        H = exposed(S)
        grids = np.array(list(itertools.product(u, repeat=len(H))))  # (G, |H|)
        r = np.zeros((K, NH))
        for k0 in range(0, K, chunk):
            aa, bb = a[k0:k0 + chunk], b[k0:k0 + chunk]
            k = aa.shape[0]
            R = np.zeros((k, len(grids), NH))
            for h, i in enumerate(H):
                R[:, :, i] = aa[:, None, i] + grids[None, :, h] * (bb[:, None, i] - aa[:, None, i])
            val = profit(S, R, aa[:, None, :], bb[:, None, :])
            g = np.argmax(val, axis=1)
            r[k0:k0 + chunk] = R[np.arange(k), g]
        aa, bb = a, b
        for _ in range(sweeps):
            for i in H:
                Fs = F(r, aa, bb)
                A = np.zeros(K); B = np.zeros(K)
                for t in S:
                    if EXP[i, t] == 0:
                        continue
                    q = np.ones(K); pay = np.zeros(K)
                    for j in range(NH):
                        if j != i and EXP[j, t] > 0:
                            q = q * Fs[:, j]
                            pay = pay + r[:, j] * EXP[j, t]
                    A += q * (P[t] - pay)
                    B += q * EXP[i, t]
                with np.errstate(divide='ignore', invalid='ignore'):
                    rstar = np.where(B > 0, (A / B + aa[:, i]) / 2, r[:, i])
                r[:, i] = np.clip(rstar, aa[:, i], bb[:, i])
        v = profit(S, r, aa, bb)
        m = v > best + 1e-14
        best = np.where(m, v, best)
        rr = np.zeros_like(r); rr[:, H] = r[:, H]
        best_r = np.where(m[:, None], rr, best_r)
        best_s = np.where(m, si, best_s)
    return best, best_r, best_s


def gain_integral(r, a, b):
    """E over s~U[a,b] of (r - s)^+."""
    top = np.clip(r, a, b)
    return ((r - a) ** 2 - (r - top) ** 2) / 2 / (b - a)
