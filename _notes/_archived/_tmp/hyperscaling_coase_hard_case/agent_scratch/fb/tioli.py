"""Take-it-or-leave-it arms at finite budgets (k=3, once, linear money, enforcer, closed).

T-f: the fleet proposes a schedule and a transfer to each resident; all three must accept.
     The fleet knows p; it estimates s_i with error sf (flat prior on s>=0, so its posterior
     is N(shat, sf^2) truncated at 0).  Residents accept iff t_i >= true harm.
     Arbitrary switch, two fleet models: 'miss' (additive model, never sees the +1.5 term)
     and 'table' (estimates resident 3's harm schedule by schedule, budget split 15 ways,
     error sqrt(15)*sf per entry in harm units).
T-b: the residents as one bloc (they know s) propose a schedule and a price; the fleet
     accepts iff price <= p.x.  The bloc estimates each p_t with error sN; posterior on
     p.x approx N(phat.x, sN^2 |x|).  Internal split: equal gains.
Failed deal = no deal = everyone 0.  Payoffs are gains over no deal.
"""
import sys
import numpy as np
from scipy.stats import norm
from inst import PROFIT, EX, S, SCHED, harms, NAMES

RNG = np.random.default_rng(20261021)
ZG = np.linspace(-4, 6, 401)


def accept_prob(t, mu, tau):
    """P(true harm <= t) under N(mu,tau^2) truncated to [0,inf)."""
    lo = norm.cdf(-mu / tau)
    return np.clip((norm.cdf((t - mu) / tau) - lo) / (1 - lo + 1e-300), 0, 1) * (t >= 0)


def fleet_offer(mu, tau, R):
    """mu,tau: (n,16,3) posterior on each resident's harm per schedule; R: (16,).
    Returns t (n,16,3) and expected profit (n,16) by coordinate ascent on a grid."""
    n = mu.shape[0]
    active = tau > 1e-12
    t = np.where(active, np.maximum(mu, 0) + tau, 0.0)
    for sweep in range(6):
        for i in range(3):
            a_others = np.ones(mu.shape[:2])
            for j in range(3):
                if j != i:
                    a_others *= np.where(active[..., j], accept_prob(t[..., j], mu[..., j], np.where(active[..., j], tau[..., j], 1)), 1)
            rest = t.sum(-1) - t[..., i]
            grid = np.maximum(mu[..., i, None] + tau[..., i, None] * ZG, 0)  # n,16,G
            a = accept_prob(grid, mu[..., i, None], np.where(active[..., i], tau[..., i], 1)[..., None])
            val = a * (R[None, :, None] - rest[..., None] - grid)
            best = np.argmax(val, -1)
            newt = np.take_along_axis(grid, best[..., None], -1)[..., 0]
            t[..., i] = np.where(active[..., i], newt, 0.0)
    a_all = np.ones(mu.shape[:2])
    for j in range(3):
        a_all *= np.where(active[..., j], accept_prob(t[..., j], mu[..., j], np.where(active[..., j], tau[..., j], 1)), 1)
    return t, a_all * (R[None, :] - t.sum(-1))


def run_tf(sf, arbitrary=False, model="miss", n=4000):
    htrue = harms(arbitrary)                                   # 16,3
    shat = S + sf * RNG.standard_normal((n, 3))
    mu = EX[None] * shat[:, None, :]                           # n,16,3 harm means
    tau = np.broadcast_to(EX[None] * sf, mu.shape).copy()
    if arbitrary and model == "table":
        tau3 = np.sqrt(15) * sf
        mu[..., 2] = htrue[None, :, 2] + tau3 * RNG.standard_normal((n, 16))
        tau[..., 2] = np.where(htrue[:, 2] > 0, tau3, 0)[None]
    t, eprof = fleet_offer(mu, tau, PROFIT)
    eprof[:, 0] = 0
    choice = np.argmax(eprof, 1)
    idx = np.arange(n)
    tc = t[idx, choice]
    hc = htrue[choice]
    deal = np.all(tc >= hc - 1e-12, 1) & (choice > 0)
    gain_r = np.where(deal[:, None], tc - hc, 0)
    gain_f = np.where(deal, PROFIT[choice] - tc.sum(1), 0)
    night = SCHED[choice, 3] == 1
    # point-estimate night flip: fleet's estimated surplus of N > 0
    flipN = (5.0 - (shat.clip(0) * np.array([1, 0.5, 2])).sum(1)) > 0
    return summarize(gain_f, gain_r, deal, night, choice, extra={"pointflipN": flipN.mean()})


def run_tb(sN, arbitrary=False, n=4000):
    htrue = harms(arbitrary)
    H = htrue.sum(1)                                           # 16
    phat = np.array([4, 5.5, 4, 5]) + sN * RNG.standard_normal((n, 4))
    Rhat = phat @ SCHED.T                                      # n,16
    sd = sN * np.sqrt(SCHED.sum(1))                            # 16
    sd[0] = 1
    grid = Rhat[..., None] + sd[None, :, None] * ZG            # price grid n,16,G
    val = (grid - H[None, :, None]) * norm.cdf((Rhat[..., None] - grid) / sd[None, :, None])
    best = np.argmax(val, -1)
    price = np.take_along_axis(grid, best[..., None], -1)[..., 0]
    ev = np.take_along_axis(val, best[..., None], -1)[..., 0]
    ev[:, 0] = 0
    choice = np.argmax(ev, 1)
    idx = np.arange(n)
    pc = price[idx, choice]
    deal = (pc <= PROFIT[choice] + 1e-12) & (choice > 0) & (pc - H[choice] > 0)
    g_bloc = np.where(deal, pc - H[choice], 0)
    gain_r = np.repeat(g_bloc[:, None] / 3, 3, 1)
    gain_f = np.where(deal, PROFIT[choice] - pc, 0)
    night = SCHED[choice, 3] == 1
    flipN = phat[:, 3] - 5.5 > 0
    return summarize(gain_f, gain_r, deal, night, choice, extra={"pointflipN": flipN.mean()})


def summarize(gf, gr, deal, night, choice, extra=None):
    Ef, Er = gf.mean(), gr.mean(0)
    g = np.array([Ef, *Er])
    out = dict(deal=deal.mean(), Ef=Ef, Er=Er, NP=np.prod(g) if (g >= 0).all() else np.nan,
               floor=g.min(), pie=gf.mean() + gr.sum(1).mean(), Rshare=gr.sum(1).mean() / max(gf.mean() + gr.sum(1).mean(), 1e-12),
               night_offered=night.mean(), night_in_deal=(night & deal).mean(),
               top=NAMES[np.bincount(choice, minlength=16).argmax()])
    if extra:
        out.update(extra)
    return out


def fmt(d):
    return (f"deal {d['deal']:.3f} | f {d['Ef']:.3f} r ({d['Er'][0]:.3f},{d['Er'][1]:.3f},{d['Er'][2]:.3f}) | "
            f"NP {d['NP']:.4f} floor {d['floor']:.3f} | pie {d['pie']:.3f} Rshare {d['Rshare']:.2f} | "
            f"N offered {d['night_offered']:.3f} N in deal {d['night_in_deal']:.3f} pointflipN {d['pointflipN']:.3f} | mode {d['top']}")


if __name__ == "__main__":
    sigmas = [1.0, 1 / np.sqrt(10), 0.3, 0.1, 0.3 / np.sqrt(10), 0.1 / np.sqrt(10)]
    for arb, model in [(False, "-"), (True, "miss"), (True, "table")]:
        print(f"\n=== T-f fleet TIOLI, arbitrary={arb} model={model}")
        for sf in sigmas:
            print(f"sf={sf:.4f}: " + fmt(run_tf(sf, arb, model)))
    for arb in (False, True):
        print(f"\n=== T-b bloc TIOLI, arbitrary={arb}")
        for sN in sigmas:
            print(f"sN={sN:.4f}: " + fmt(run_tb(sN, arb)))
