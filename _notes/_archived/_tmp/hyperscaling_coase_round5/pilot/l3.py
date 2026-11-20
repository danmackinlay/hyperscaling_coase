"""Cross-check 1: residents in L3 (adaptive play, memory m) against the planning principal.

L3: each period a resident's demand is the best response (highest d among ties) to the summed
full-information score vectors of a uniform sample, with replacement, of m of her past periods.
No closed-form expected dynamics exists for this rule, so the principal plans by five averaged
sampled rollouts for h >= 1, with the h = 0 term computed exactly from a 100-draw Monte Carlo of
the current demand distribution. Its point estimate of a resident's demand is the best response to
her whole history (the fictitious-play prediction), at h = 0 and in rollouts alike.
"""
from __future__ import annotations

import itertools

import numpy as np

from sim import DELTA, EPS, MARGIN_SETS, PIE, core_step, grid

K_ROLL = 5
N_MC = 100


TIE = {"rule": "highest"}


def br(S, G):
    """Best response to summed score vectors S (...,Gn); ties to the highest d, or to the d nearest 0."""
    if TIE["rule"] == "zero":
        ok = S >= S.max(-1, keepdims=True) - 1e-12
        return G[np.where(ok, np.abs(G), np.inf).argmin(-1)]
    rev = S[..., ::-1]
    return G[G.size - 1 - rev.argmax(-1)]


def draws(hist_n, ext, n_ext, m, rng, size, G):
    """Demand draws (size,3). hist_n: (n,3,Gn) base history; ext: (size,Hx,3,Gn) or None."""
    n = hist_n.shape[0]
    tot = n + n_ext
    if tot == 0:
        return G[rng.integers(0, G.size, size=(size, 3))]
    idx = rng.integers(0, tot, size=(size, 3, m))
    S = np.zeros((size, 3, G.size))
    r = np.arange(3)[None, :, None]
    base = idx < n
    if n > 0:
        bi = np.where(base, idx, 0)
        S += (hist_n[bi, r] * base[..., None]).sum(2)
    if n_ext > 0:
        ei = np.where(base, 0, idx - n)
        b = np.arange(size)[:, None, None]
        S += (ext[b, ei, r] * (~base)[..., None]).sum(2)
    return br(S, G)


def plan(hist_n, cfg, G, Heff, rng, dhat0):
    ms = MARGIN_SETS["std"]
    M = np.array(list(itertools.product(ms, repeat=3)) + [(np.nan,) * 3], float)
    P = M.shape[0]
    # exact h=0 term from the Monte Carlo demand distribution
    mc = draws(hist_n, None, 0, cfg.m, rng, N_MC, G)  # (N_MC,3)
    ab = np.isnan(M).any(1)
    g = dhat0[None, :] + np.nan_to_num(M)  # (P,3)
    F = (mc[None, :, :] <= g[:, None, :] + EPS).mean(1)  # (P,3)
    V = np.where(ab, 0.0, (PIE - g.sum(1)) * F.prod(1))
    if Heff <= 1:
        return M[int(np.argmax(V))]
    B = P * K_ROLL
    crn = np.random.default_rng(int(rng.integers(2**62)))
    Mb = np.repeat(M, K_ROLL, 0)
    ext = np.zeros((B, Heff, 3, G.size))
    run_sum = np.broadcast_to(hist_n.sum(0), (B, 3, G.size)).copy()
    props = crn.integers(0, 4, size=(Heff, K_ROLL))
    props[0] = 0
    for h in range(Heff):
        # common random numbers across policies: same draws for every policy within a rollout
        if h == 0:
            d = np.tile(mc[crn.integers(0, N_MC, size=K_ROLL)], (P, 1))
            dhat = np.tile(dhat0, (B, 1))
        else:
            d = draws(hist_n, ext, h, cfg.m, crn, B, G)
            dhat = br(run_sum, G)
        prop = np.tile(props[h], P)
        rP, _, _, sc = core_step(d, dhat, Mb, prop, cfg, G)
        if h > 0:
            V += DELTA**h * rP.reshape(P, K_ROLL).mean(1)
        ext[:, h] = sc
        run_sum += sc
    return M[int(np.argmax(V))]


def run_L3(cfg, seed):
    TIE["rule"] = cfg.tie
    rng = np.random.default_rng(seed)
    G = grid(cfg.step)
    T = cfg.T
    hist = np.zeros((T, 3, G.size))
    rP = np.zeros(T)
    rR = np.zeros((T, 3))
    deal = np.zeros(T, bool)
    for t in range(T):
        prop = rng.integers(0, 4)
        d = draws(hist[:t], None, 0, cfg.m, rng, 1, G)
        dhat = br(hist[:t].sum(0), G) if t > 0 else np.zeros(3)
        mu = np.zeros(3)
        if prop == 0:
            Heff = T - t if cfg.H == "T" else min(int(cfg.H), T - t)
            mu = plan(hist[:t], cfg, G, Heff, rng, dhat)
        a, b, dl, sc = core_step(d, dhat[None], mu[None], np.array([prop]), cfg, G)
        rP[t], rR[t], deal[t] = a[0], b[0], dl[0]
        hist[t] = sc[0]
    W = min(cfg.window, T)
    return dict(P=rP[-W:].mean(), R=rR[-W:].mean(0), deal=deal[-W:].mean())
