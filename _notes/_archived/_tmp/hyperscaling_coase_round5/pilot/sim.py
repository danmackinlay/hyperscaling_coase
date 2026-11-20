"""Arm 1a pilot: principal planner vs L1 (multiplicative-weights) residents, protocol P, n=3, k=3.

Base instance: pie 6 on the efficient schedule M,D,E (profit 13.5, harms 1, 2.5, 4).
All rules are stated over gains, so the schedule choice decouples from the learning
dynamics (see IMPLEMENTATION CHOICES in the report); x = MDE always.
"""
from __future__ import annotations

import itertools
import os
from dataclasses import dataclass, replace

import numpy as np

os.environ.setdefault("OMP_NUM_THREADS", "1")

PIE = 6.0
EPS = 1e-9
DELTA = 0.95

# --- base instance (used only to confirm the schedule choice) -----------------
P_SLOT = np.array([4, 5.5, 4, 5.0])
EXPO = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
SENS = np.array([1.0, 1.0, 2.0])


def efficient_schedule():
    best = None
    for x in itertools.product([0, 1], repeat=4):
        x = np.array(x)
        s = P_SLOT @ x - ((SENS[:, None] * EXPO) @ x).sum()
        if best is None or s > best[0]:
            best = (s, x)
    return best


@dataclass(frozen=True)
class Cfg:
    eta: float = 0.1
    step: float = 0.25
    scale: float = 8.0
    H: object = 10  # int or "T"
    T: int = 500
    window: int = 100
    margins: str = "std"  # std | small | line
    feedback: str = "full"  # full | bandit
    play: str = "sampled"  # sampled | expected
    dyn: str = "expected"  # expected | roll1 | roll5
    scoring: str = "counterfactual"  # counterfactual | own_offer (literal reading, ignores others' refusals)
    res_class: str = "L1"  # L1 | L0 | L3
    m: int = 5  # L3 memory
    tie: str = "highest"  # L3 tie-break among best responses: highest | zero (nearest 0)
    l0_proposer: str = "take_rest"  # take_rest | literal (L0 proposer demands 0)
    principal_class: str = "planner"  # planner | L0


MARGIN_SETS = {"std": [0, 0.25, 0.5, 1, 2], "small": [0, 0.5, 1],
               "neg": [-1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2]}  # side check only: undercutting allowed
LINE_GRID = np.round(np.arange(0, 3.0001, 0.1), 10)


def grid(step):
    return np.round(np.arange(-2, 4 + 1e-9, step), 10)


def softmax(lw):
    z = lw - lw.max(-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(-1, keepdims=True)


# =============================================================================
# Expected (mean-field) learner dynamics, batched over candidate policies
# =============================================================================
def _cdf(supp, q, x):
    """P(d <= x). supp,q: (B,S); x: (B,X) -> (B,X)."""
    return (q[:, None, :] * (supp[:, None, :] <= x[:, :, None] + EPS)).sum(-1)


def exp_branches(lw, mu, cfg, G, need_resident_branches=True):
    """Return list of (prob, principal_reward (B,), score (B,3,Gn)) for each proposer."""
    probs = softmax(lw)
    B = lw.shape[0]
    Gn = G.size
    dhat = (probs * G).sum(-1)  # (B,3)
    if cfg.play == "sampled":
        supp = np.broadcast_to(G, probs.shape)
        q = probs
    else:
        supp = dhat[:, :, None]
        q = np.ones_like(supp)
    out = []
    cf = cfg.scoring == "counterfactual"
    # principal proposes
    ab = np.isnan(mu).any(-1)  # abstain: propose nothing
    g = dhat + np.nan_to_num(mu)  # (B,3)
    A = np.stack([_cdf(supp[:, k], q[:, k], g[:, k : k + 1])[:, 0] for k in range(3)], 1)
    rP = np.where(ab, 0.0, (PIE - g.sum(1)) * A.prod(1))
    sc = np.empty((B, 3, Gn))
    for i in range(3):
        others = np.prod([A[:, k] for k in range(3) if k != i], axis=0) if cf else 1.0
        sc[:, i] = g[:, i, None] * (g[:, i, None] >= G - EPS) * np.reshape(others, (-1, 1)) * ~ab[:, None]
    out.append((0.25, rP, sc))
    if not need_resident_branches:
        return out
    xg = np.broadcast_to((PIE - G) / 3.0, (B, Gn))
    Fx = np.stack([_cdf(supp[:, k], q[:, k], xg) for k in range(3)], 1)  # (B,3,Gn)
    for j in range(3):
        s = supp[:, j]
        qj = q[:, j]
        o = (PIE - s) / 3.0  # (B,S)
        pacc = (o >= -EPS).astype(float)
        Bk = {k: _cdf(supp[:, k], q[:, k], o) for k in range(3) if k != j}
        allacc = pacc * np.prod([Bk[k] for k in Bk], axis=0)
        r = (qj * o * allacc).sum(1)
        sc = np.empty((B, 3, Gn))
        for i in range(3):
            if i == j:
                sc[:, i] = G * np.prod([Fx[:, k] for k in range(3) if k != j], axis=0) * ((PIE - G) / 3 >= -EPS)
            else:
                other = 3 - i - j
                w = qj * o * pacc * (Bk[other] if cf else 1.0)  # (B,S)
                sc[:, i] = np.einsum("bs,bsg->bg", w, (o[:, :, None] >= G - EPS))
        out.append((0.25, r, sc))
    return out


def _gridconsts(G):
    o = (PIE - G) / 3.0
    cidx = np.searchsorted(G, o + EPS, side="right")  # F_k(o_s) = Cpad[cidx_s]
    nidx = np.searchsorted(G, PIE - 3 * G + EPS, side="right")  # o_s >= G_g  <=>  s < nidx_g
    return o, cidx, nidx


_GC = {}


def exp_branches_fast(lw, mu, cfg, G, need_resident_branches=True):
    """Same as exp_branches for sampled play, O(B*G) via cumulative sums."""
    key = G.size
    if key not in _GC:
        _GC[key] = _gridconsts(G)
    o, cidx, nidx = _GC[key]
    probs = softmax(lw)
    B, _, Gn = probs.shape
    dhat = (probs * G).sum(-1)
    Cpad = np.concatenate([np.zeros((B, 3, 1)), np.cumsum(probs, -1)], -1)  # (B,3,Gn+1)
    cf = cfg.scoring == "counterfactual"
    ab = np.isnan(mu).any(-1)
    g = dhat + np.nan_to_num(mu)
    gi = np.searchsorted(G, (g + EPS).ravel(), side="right").reshape(B, 3)
    A = np.take_along_axis(Cpad, gi[:, :, None], -1)[:, :, 0]
    rP = np.where(ab, 0.0, (PIE - g.sum(1)) * A.prod(1))
    sc = np.empty((B, 3, Gn))
    for i in range(3):
        oth = [k for k in range(3) if k != i]
        f = (A[:, oth[0]] * A[:, oth[1]]) if cf else 1.0
        sc[:, i] = g[:, i, None] * (g[:, i, None] >= G - EPS) * np.reshape(f, (-1, 1)) * ~ab[:, None]
    out = [(0.25, rP, sc)]
    if not need_resident_branches:
        return out
    Fo = Cpad[:, :, cidx]  # (B,3,Gn): F_k(o_s)
    pacc = (o >= -EPS).astype(float)
    for j in range(3):
        qj = probs[:, j]
        oth = [k for k in range(3) if k != j]
        allacc = pacc * Fo[:, oth[0]] * Fo[:, oth[1]]
        r = (qj * o * allacc).sum(1)
        sc = np.empty((B, 3, Gn))
        sc[:, j] = G * allacc
        for i in oth:
            other = 3 - i - j
            w = qj * o * pacc * (Fo[:, other] if cf else 1.0)
            Wpad = np.concatenate([np.zeros((B, 1)), np.cumsum(w, -1)], -1)
            sc[:, i] = Wpad[:, nidx]
        out.append((0.25, r, sc))
    return out


def plan_expected(lw0, M, cfg, G, Heff):
    br_fn = exp_branches_fast if cfg.play == "sampled" else exp_branches
    B = M.shape[0]
    lw = np.broadcast_to(lw0, (B,) + lw0.shape).copy()
    V = np.zeros(B)
    for h in range(Heff):
        if h == 0:
            (_, r, sc), = br_fn(lw, M, cfg, G, need_resident_branches=False)
        else:
            br = br_fn(lw, M, cfg, G)
            r = sum(p * rr for p, rr, _ in br)
            sc = sum(p * s for p, _, s in br)
        V += DELTA**h * r
        if h < Heff - 1:
            lw += cfg.eta / cfg.scale * sc
    return V


# =============================================================================
# Sampled step (used for the real game and for rollout planning), batched
# =============================================================================
def core_step(d, dhat, mu, prop, cfg, G, want_scores=True):
    """Outcome of one period given demands d (B,3) and the principal's estimate dhat (B,3).
    Returns rP (B,), rR (B,3), deal (B,), full-information score vectors (B,3,Gn) or None."""
    B = d.shape[0]
    Gn = G.size
    isP = prop == 0
    ab = np.isnan(mu).any(-1)
    g = dhat + np.nan_to_num(mu)
    # offered gain to each party (residents) and principal gain if deal
    gainR = np.where(isP[:, None], g, 0.0)
    gainP = np.where(isP, PIE - g.sum(1), 0.0)
    acc = np.where(isP[:, None], g >= d - EPS, True)
    jr = np.clip(prop - 1, 0, 2)
    dj = d[np.arange(B), jr]
    o = (PIE - dj) / 3.0
    for j in range(3):
        mj = prop == j + 1
        if not mj.any():
            continue
        for k in range(3):
            if k == j:
                gainR[mj, k] = dj[mj]
            else:
                gainR[mj, k] = o[mj]
                acc[mj, k] = o[mj] >= d[mj, k] - EPS
        gainP[mj] = o[mj]
    pacc = np.where(isP, True, o >= -EPS)
    deal = acc.all(1) & pacc & ~(isP & ab)
    rR = gainR * deal[:, None]
    rP = gainP * deal
    sc = None
    if want_scores:
        sc = np.zeros((B, 3, Gn))
        cf = cfg.scoring == "counterfactual"
        xg = (PIE - G) / 3.0
        for i in range(3):
            oth = [k for k in range(3) if k != i]
            # principal proposes: responder i
            m0 = isP
            if m0.any():
                f = acc[m0][:, oth].all(1) if cf else np.ones(m0.sum(), bool)
                sc[m0, i] = g[m0, i, None] * (g[m0, i, None] >= G - EPS) * (f & ~ab[m0])[:, None]
            for j in range(3):
                mj = prop == j + 1
                if not mj.any():
                    continue
                if i == j:
                    ok = np.ones((mj.sum(), Gn), bool)
                    for k in oth:
                        ok &= xg[None, :] >= d[mj, k, None] - EPS
                    sc[mj, i] = G * ok * (xg >= -EPS)
                else:
                    other = 3 - i - j
                    f = (acc[mj, other] & pacc[mj]) if cf else pacc[mj]
                    sc[mj, i] = o[mj, None] * (o[mj, None] >= G - EPS) * f[:, None]
    return rP, rR, deal, sc


def sampled_step(lw, mu, prop, u, cfg, G):
    """lw (B,3,Gn); mu (B,3); prop (B,) in {0..3}; u (B,3).
    Returns rP (B,), rR (B,3), new lw, deal (B,)."""
    B, _, Gn = lw.shape
    probs = softmax(lw)
    dhat = (probs * G).sum(-1)
    if cfg.play == "sampled":
        idx = (np.cumsum(probs, -1) < u[:, :, None]).sum(-1)
        idx = np.minimum(idx, Gn - 1)
        d = G[idx]
        pplay = np.take_along_axis(probs, idx[:, :, None], -1)[:, :, 0]
    else:
        d = dhat
        idx = np.abs(dhat[:, :, None] - G).argmin(-1)
        pplay = np.ones_like(d)
    rP, rR, deal, sc = core_step(d, dhat, mu, prop, cfg, G, want_scores=cfg.feedback == "full")
    if cfg.feedback == "full":
        lw = lw + cfg.eta / cfg.scale * sc
    else:  # bandit, EXP3 on losses (6-u)/scale >= 0, importance weighted
        loss = (PIE - rR) / cfg.scale / pplay
        lw = lw.copy()
        bi = np.arange(B)[:, None]
        ri = np.arange(3)[None, :]
        lw[bi, ri, idx] -= cfg.eta * loss
    return rP, rR, lw, deal


def plan_rollout(lw0, M, cfg, G, Heff, K, rng):
    P = M.shape[0]
    B = P * K
    lw = np.broadcast_to(lw0, (B,) + lw0.shape).copy()
    Mb = np.repeat(M, K, axis=0)
    V = np.zeros(B)
    # common random numbers across policies; independent across the K rollouts
    props = rng.integers(0, 4, size=(Heff, K))
    props[0] = 0
    us = rng.random((Heff, K, 3))
    for h in range(Heff):
        prop = np.tile(props[h], P)
        u = np.tile(us[h], (P, 1))
        rP, _, lw, _ = sampled_step(lw, Mb, prop, u, cfg, G)
        V += DELTA**h * rP
    return V.reshape(P, K).mean(1)


def evaluate(lw, M, cfg, G, Heff, crn_seed):
    if cfg.dyn == "expected":
        return plan_expected(lw, M, cfg, G, Heff)
    K = 1 if cfg.dyn == "roll1" else 5
    return plan_rollout(lw, M, cfg, G, Heff, K, np.random.default_rng(crn_seed))


def choose_margin(lw, cfg, G, Heff, rng):
    rng = int(rng.integers(2**62))  # one common-random-number seed for every candidate of this decision
    if cfg.margins in MARGIN_SETS:
        ms = MARGIN_SETS[cfg.margins]
        M = np.array(list(itertools.product(ms, repeat=3)) + [(np.nan,) * 3], float)
        V = evaluate(lw, M, cfg, G, Heff, rng)
        return M[int(np.argmax(V))]
    # continuous margin: coordinate-wise grid line search on [0,3], step 0.1, two sweeps
    mu = np.zeros(3)
    for _ in range(2):
        for i in range(3):
            M = np.tile(mu, (LINE_GRID.size, 1))
            M[:, i] = LINE_GRID
            V = evaluate(lw, M, cfg, G, Heff, rng)
            mu = M[int(np.argmax(V))].copy()
    V = evaluate(lw, np.array([mu, (np.nan,) * 3]), cfg, G, Heff, rng)
    return mu if V[0] >= V[1] else np.full(3, np.nan)


# =============================================================================
# The real game
# =============================================================================
def run_L1(cfg: Cfg, seed: int):
    rng = np.random.default_rng(seed)
    G = grid(cfg.step)
    lw = np.zeros((1, 3, G.size))
    T = cfg.T
    rP = np.zeros(T)
    rR = np.zeros((T, 3))
    deal = np.zeros(T, bool)
    for t in range(T):
        prop = rng.integers(0, 4)
        u = rng.random((1, 3))
        mu = np.zeros((1, 3))
        if prop == 0 and cfg.principal_class == "planner":
            Heff = T - t if cfg.H == "T" else min(int(cfg.H), T - t)
            mu[0] = choose_margin(lw[0], cfg, G, Heff, rng)
        a, b, lw, dl = sampled_step(lw, mu, np.array([prop]), u, cfg, G)
        rP[t], rR[t], deal[t] = a[0], b[0], dl[0]
    W = min(cfg.window, T)
    return dict(P=rP[-W:].mean(), R=rR[-W:].mean(0), deal=deal[-W:].mean())


def run_L0(cfg: Cfg, seed: int):
    """Reference cell: every party L0 (d=0); principal at H=1 is identical to L0 here."""
    rng = np.random.default_rng(seed)
    T = cfg.T
    rP = np.zeros(T)
    rR = np.zeros((T, 3))
    for t in range(T):
        prop = rng.integers(0, 4)
        if prop == 0:
            # principal at H=1 against residents who accept any gain >= 0: offers 0 each
            rP[t] = PIE
        else:
            j = prop - 1
            dj = PIE if cfg.l0_proposer == "take_rest" else 0.0
            o = (PIE - dj) / 3
            rP[t] = o
            rR[t] = o
            rR[t, j] = dj
    W = min(cfg.window, T)
    return dict(P=rP[-W:].mean(), R=rR[-W:].mean(0), deal=1.0)


def run_one(args):
    cfg, seed = args
    if cfg.res_class == "L0":
        return run_L0(cfg, seed)
    if cfg.res_class == "REV":
        from rev import run_rev

        return run_rev(cfg, seed)
    if cfg.res_class == "L3":
        from l3 import run_L3

        return run_L3(cfg, seed)
    return run_L1(cfg, seed)


def summarise(results):
    P = np.array([r["P"] for r in results])
    R = np.array([r["R"] for r in results])
    D = np.array([r["deal"] for r in results])
    takes = np.concatenate([P[:, None], R], 1).mean(0)
    pos = takes[takes > 0]
    gm = np.exp(np.log(pos).mean()) if pos.size else 0.0
    return dict(
        P=P.mean(),
        P_se=P.std(ddof=1) / np.sqrt(len(P)) if len(P) > 1 else 0.0,
        R1=R[:, 0].mean(),
        R2=R[:, 1].mean(),
        R3=R[:, 2].mean(),
        deal=D.mean(),
        floor=takes.min(),
        gm_frac=gm / 1.5,
        n_pos=int(pos.size),
        pie_real=takes.sum(),
    )


if __name__ == "__main__":
    print("efficient schedule", efficient_schedule())
