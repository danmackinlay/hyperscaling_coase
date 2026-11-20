"""Haggling arm at finite budgets: a four-party demand game (k=3, once, linear money, enforcer, closed).

Each party states a gain g_j it demands over no deal.  Residents' agents post per-schedule
prices h_i(x)+g_i (+ their slack share), so the fleet's agent faces the true net surplus
schedule by schedule and the schedule cleared is the true argmax (MDE parametric, MD arbitrary):
the schedule needs no estimate; only the division does.  Deal iff sum g <= V (true max pie).
Closure 'sd' (split the difference): each gets g_j + (V - sum g)/4.  Closure 'nash': each gets
g_j, slack unallocated (Nash's demand game).  Failure: everyone 0.

Information: the fleet knows p, estimates s with error sf; the residents know s (shared within
the bloc), estimate p with error sN.  Rules:
  L0  demand a quarter of your point-estimated maximal pie (the equal split on your estimate).
  L1  best response, computed with your own noisy posterior, to the other side playing L0
      (residents: symmetric fixed point among the three, who share information).
  ORC best response computed with the truth (an unbounded best-responder) to the other side's L0.
  MEQ equilibrium in the class 'L0 minus a constant margin', margins chosen against the true
      sampling distribution (both sides best-respond in rule space).
"""
import sys
import numpy as np
from inst import PROFIT, EX, S, SCHED, harms

P = np.array([4, 5.5, 4, 5.0])
ME = (SCHED[:, 0] == 1) & (SCHED[:, 2] == 1)


def vmax(profit, h):
    """profit (...,16), h (...,16,3) -> max over schedules of profit - sum h (empty schedule = 0)."""
    return (profit - h.sum(-1)).max(-1)


class Arm:
    def __init__(self, sf, sN, arbitrary=False, model="miss", closure="sd", seed=1):
        self.sf, self.sN, self.arb, self.model, self.closure = sf, sN, arbitrary, model, closure
        self.rng = np.random.default_rng(seed)
        self.htrue = harms(arbitrary)
        self.V = vmax(PROFIT, self.htrue)

    # point estimates
    def fleet_hat(self, shat, h3hat=None):
        h = EX[None] * np.clip(shat, 0, None)[:, None, :]
        if self.arb and self.model == "table":
            h[..., 2] = np.clip(h3hat, 0, None)
        return h

    def draw_signals(self, n):
        shat = S + self.sf * self.rng.standard_normal((n, 3))
        h3hat = self.htrue[None, :, 2] + np.sqrt(15) * self.sf * self.rng.standard_normal((n, 16))
        h3hat[:, self.htrue[:, 2] == 0] = 0
        phat = P + self.sN * self.rng.standard_normal((n, 4))
        return shat, h3hat, phat

    def L0(self, shat, h3hat, phat):
        Vf = vmax(PROFIT[None], self.fleet_hat(shat, h3hat))
        VN = vmax(phat @ SCHED.T, self.htrue[None])
        return Vf / 4, VN / 4

    def payoff(self, gf, gN):
        """gf (n,), gN (n,3) -> gains (n,4)."""
        tot = gf + gN.sum(1)
        ok = tot <= self.V + 1e-12
        g = np.column_stack([gf, gN])
        if self.closure == "sd":
            g = g + ((self.V - tot) / 4)[:, None]
        return np.where(ok[:, None], g, 0.0), ok

    def best_scalar(self, D, own_weight):
        """Maximise E[(w*g + (1-w)*D) 1{g<=D}] (sd) or E[g 1{g<=D}] (nash) over g, per row of D (n,M)."""
        Ds = -np.sort(-D, 1)  # descending
        M = D.shape[1]
        k = np.arange(1, M + 1)
        if self.closure == "sd":
            obj = (k * own_weight * Ds + (1 - own_weight) * np.cumsum(Ds, 1)) / M
        else:
            obj = k * Ds / M
        j = obj.argmax(1)
        return Ds[np.arange(len(D)), j]

    def fleet_L1(self, shat, h3hat, M=1500):
        n = len(shat)
        out = np.empty(n)
        for a in range(n):
            # fleet posterior on s (flat prior, truncated at 0) by rejection-free clipping resample
            s = shat[a] + self.sf * self.rng.standard_normal((M, 3))
            while (s < 0).any():
                bad = s < 0
                s[bad] = (shat[a] + self.sf * self.rng.standard_normal((M, 3)))[bad]
            h = EX[None] * s[:, None, :]
            if self.arb and self.model == "miss":
                pass  # fleet's model has no interaction term
            if self.arb and self.model == "table":
                h3 = h3hat[a][None] + np.sqrt(15) * self.sf * self.rng.standard_normal((M, 16))
                h3 = np.clip(h3, 0, None); h3[:, self.htrue[:, 2] == 0] = 0
                h[..., 2] = h3
            V = vmax(PROFIT[None], h)
            ph = P + self.sN * self.rng.standard_normal((M, 4))
            gN = vmax(ph @ SCHED.T, h) / 4
            D = V - 3 * gN
            out[a] = self.best_scalar(D[None], 0.75)[0]
        return out

    def res_L1(self, shat_unused, phat, M=1500, iters=40):
        n = len(phat)
        out = np.empty(n)
        for a in range(n):
            p = phat[a] + self.sN * self.rng.standard_normal((M, 4))
            V = vmax(p @ SCHED.T, self.htrue[None])
            sh = S + self.sf * self.rng.standard_normal((M, 3))
            h = EX[None] * np.clip(sh, 0, None)[:, None, :]
            if self.arb and self.model == "table":
                h3 = self.htrue[None, :, 2] + np.sqrt(15) * self.sf * self.rng.standard_normal((M, 16))
                h3 = np.clip(h3, 0, None); h3[:, self.htrue[:, 2] == 0] = 0
                h[..., 2] = h3
            gf = vmax(p @ SCHED.T, h) / 4
            g = 1.5
            for _ in range(iters):
                D = V - gf - 2 * g
                g = 0.5 * g + 0.5 * self.best_scalar(D[None], 0.75)[0]
            out[a] = g
        return out

    def oracle_fleet_vs_L0(self, gN0):
        D = self.V - gN0.sum(1)
        return self.best_scalar(D[None], 0.75)[0]

    def oracle_res_vs_L0(self, gf0, iters=60):
        g = 1.5
        for _ in range(iters):
            D = self.V - gf0 - 2 * g
            g = 0.5 * g + 0.5 * self.best_scalar(D[None], 0.75)[0]
        return g

    def margin_eq(self, gf0, gN0, grid=np.linspace(-1.5, 3, 451), iters=200):
        mf, mN = 0.0, 0.0
        for _ in range(iters):
            vf = [self.payoff(gf0 - m, gN0 - mN)[0][:, 0].mean() for m in grid]
            bf = grid[int(np.argmax(vf))]
            vr = [self.payoff(gf0 - mf, np.column_stack([gN0[:, 0] - m, gN0[:, 1] - mN, gN0[:, 2] - mN]))[0][:, 1].mean() for m in grid]
            br = grid[int(np.argmax(vr))]
            if abs(bf - mf) < 0.011 and abs(br - mN) < 0.011:
                break
            mf, mN = 0.7 * mf + 0.3 * bf, 0.7 * mN + 0.3 * br
        return mf, mN


def report(tag, gains, ok):
    E = gains.mean(0)
    NP = np.prod(E) if (E >= 0).all() else float("nan")
    pie = gains.sum(1).mean()
    print(f"  {tag:10s} deal {ok.mean():.3f} | f {E[0]:.3f} r ({E[1]:.3f},{E[2]:.3f},{E[3]:.3f}) | NP {NP:.4f} "
          f"floor {E.min():.3f} | pie {pie:.3f} Rshare {E[1:].sum() / max(pie, 1e-12):.2f}")
    return E


def run(sf, sN, arbitrary=False, model="miss", closure="sd", n=1500, do_L1=True):
    arm = Arm(sf, sN, arbitrary, model, closure)
    shat, h3hat, phat = arm.draw_signals(n)
    gf0, gN0s = arm.L0(shat, h3hat, phat)
    gN0 = np.repeat(gN0s[:, None], 3, 1)
    res = {}
    res["L0/L0"] = report("L0/L0", *arm.payoff(gf0, gN0))
    of = arm.oracle_fleet_vs_L0(gN0)
    res["ORCf/L0"] = report("ORCf/L0", *arm.payoff(np.full(n, of), gN0))
    orr = arm.oracle_res_vs_L0(gf0)
    res["L0/ORCr"] = report("L0/ORCr", *arm.payoff(gf0, np.full((n, 3), orr)))
    sh2, h32, ph2 = arm.draw_signals(20000)
    gf0b, gN0b = arm.L0(sh2, h32, ph2)
    gN0b = np.repeat(gN0b[:, None], 3, 1)
    mf, mN = arm.margin_eq(gf0b, gN0b)
    res["MEQ"] = report(f"MEQ", *arm.payoff(gf0b - mf, gN0b - mN))
    print(f"    margins fleet {mf:.3f} resident {mN:.3f}; mean L0 demands fleet {gf0.mean():.3f} resident {gN0s.mean():.3f}")
    if do_L1:
        m = min(n, 400)
        gf1 = arm.fleet_L1(shat[:m], h3hat[:m])
        gN1 = arm.res_L1(shat[:m], phat[:m])
        g0f, g0N = gf0[:m], gN0[:m]
        res["L1f/L0"] = report("L1f/L0", *arm.payoff(gf1, g0N))
        res["L0/L1r"] = report("L0/L1r", *arm.payoff(g0f, np.repeat(gN1[:, None], 3, 1)))
        res["L1/L1"] = report("L1/L1", *arm.payoff(gf1, np.repeat(gN1[:, None], 3, 1)))
    return res


if __name__ == "__main__":
    closure = sys.argv[1] if len(sys.argv) > 1 else "sd"
    arb = len(sys.argv) > 2 and sys.argv[2] != "par"
    model = sys.argv[2] if arb else "-"
    do_L1 = not (len(sys.argv) > 3 and sys.argv[3] == "noL1")
    for L in (1.0, 0.3, 0.1):
        for ratio, (sf, sN) in {"1:1": (L, L), "10:1": (L / np.sqrt(10), L), "1:10": (L, L / np.sqrt(10))}.items():
            print(f"[{closure} arb={arb} {model}] level {L} ratio {ratio}: sf={sf:.3f} sN={sN:.3f}")
            run(sf, sN, arb, model, closure, do_L1=do_L1)
