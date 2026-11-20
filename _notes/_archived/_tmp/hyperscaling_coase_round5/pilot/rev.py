"""Cross-check 2: the reversed cell. Residents plan jointly as a bloc (equal internal split) at
horizon H against a principal in L1 (multiplicative weights over its own demand on G).

Mirror of the main arm: when a resident is drawn to propose, the bloc offers the principal
gain dhat_P + mu (mu in the margin set, chosen by forward simulation of the principal's expected
L1 dynamics, delta = 0.95) and splits the rest equally; when the principal is drawn, it demands
its sampled d_P and offers each resident (6 - d_P)/3, which the bloc accepts iff that gain >= 0
(the same myopic responder rule the planner has in the main arm).
"""
from __future__ import annotations

import numpy as np

from sim import DELTA, EPS, MARGIN_SETS, PIE, grid, softmax


def exp_terms(lw, mu, G, first):
    """lw (B,Gn), mu (B,). Bloc reward and expected L1 score vector."""
    p = softmax(lw)
    dhat = (p * G).sum(-1)
    g = dhat + mu
    F = (p * (G[None, :] <= g[:, None] + EPS)).sum(-1)
    r_bloc_prop = (PIE - g) * F
    sc_resp = g[:, None] * (g[:, None] >= G - EPS)
    if first:
        return r_bloc_prop, sc_resp
    # principal proposes: demands d, residents accept iff (6-d)/3 >= 0, true for d <= 4
    acc = ((PIE - G) / 3 >= -EPS).astype(float)
    r_pp = (p * (PIE - G) * acc).sum(-1)
    sc_prop = G * acc
    return 0.75 * r_bloc_prop + 0.25 * r_pp, 0.75 * sc_resp + 0.25 * sc_prop[None, :]


def plan(lw0, cfg, G, Heff):
    M = np.array(MARGIN_SETS["std"], float)
    lw = np.tile(lw0, (M.size, 1))
    V = np.zeros(M.size)
    for h in range(Heff):
        r, sc = exp_terms(lw, M, G, first=(h == 0))
        V += DELTA**h * r
        lw = lw + cfg.eta / cfg.scale * sc
    return M[int(np.argmax(V))]


def run_rev(cfg, seed):
    rng = np.random.default_rng(seed)
    G = grid(cfg.step)
    lw = np.zeros(G.size)
    T = cfg.T
    rP = np.zeros(T)
    rB = np.zeros(T)
    deal = np.zeros(T, bool)
    for t in range(T):
        prop = rng.integers(0, 4)
        p = softmax(lw)
        d = G[min(int((np.cumsum(p) < rng.random()).sum()), G.size - 1)]
        dhat = (p * G).sum()
        if prop == 0:
            o = (PIE - d) / 3
            ok = o >= -EPS
            rP[t], rB[t], deal[t] = d * ok, (PIE - d) * ok, ok
            sc = G * ((PIE - G) / 3 >= -EPS)
        else:
            Heff = T - t if cfg.H == "T" else min(int(cfg.H), T - t)
            mu = plan(lw, cfg, G, Heff)
            g = dhat + mu
            ok = g >= d - EPS
            rP[t], rB[t], deal[t] = g * ok, (PIE - g) * ok, ok
            sc = g * (g >= G - EPS)
        lw = lw + cfg.eta / cfg.scale * sc
    W = min(cfg.window, T)
    r = rB[-W:].mean() / 3
    return dict(P=rP[-W:].mean(), R=np.array([r, r, r]), deal=deal[-W:].mean())
