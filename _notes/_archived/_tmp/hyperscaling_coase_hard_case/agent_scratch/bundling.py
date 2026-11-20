"""Bundling as a commitment device: computations on the hard-case instance.

Four slots M, D, E, N; profit p; three residents with exposure e_i and sensitivity s_i.
Switches reported per block. All sixteen schedules enumerated.
"""
import itertools
import math

import numpy as np
from scipy.stats import norm

SLOTS = "MDEN"
p = np.array([4.0, 5.5, 4.0, 5.0])
e = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1.0, 1.0, 2.0])
W0 = np.array([100.0, 10.0, 10.0, 2.0])  # fleet, r1, r2, r3

SCHEDULES = [np.array(x) for x in itertools.product([0, 1], repeat=4)]


def name(x):
    return "".join(c for c, b in zip(SLOTS, x) if b) or "none"


def harm(x, arbitrary=False):
    h = s * (e @ x)
    if arbitrary and x[0] == 1 and x[2] == 1:
        h = h.copy()
        h[2] += 1.5
    return h


def pie(x, arbitrary=False):
    return p @ x - harm(x, arbitrary).sum()


def nash(g):
    g = np.asarray(g, float)
    if (g < 0).any():
        return float("nan")
    return float(np.prod(g))


def util_gain(payoff):
    return np.log(W0 + payoff) - np.log(W0)


print("=" * 70)
print("A. Enumeration of the sixteen schedules (switches: all off / arbitrary on)")
print("=" * 70)
for arb in (False, True):
    print(f"\n-- arbitrary={arb}")
    rows = []
    for x in SCHEDULES:
        rows.append((pie(x, arb), name(x), p @ x, harm(x, arb)))
    rows.sort(reverse=True)
    for pi, nm, prof, h in rows[:5]:
        print(f"  {nm:5s} profit {prof:5.1f} harms {h} pie {pi:5.2f}")
    best = rows[0]
    print(f"  efficient: {best[1]} pie {best[0]}")
    allfour = next(r for r in rows if r[1] == "MDEN")
    print(f"  all-or-nothing (MDEN): pie {allfour[0]} -> clause menu worth {best[0]-allfour[0]:.2f}")

print()
print("=" * 70)
print("B. Transparent: bundled fleet TIOLI vs slot-by-slot symmetric Nash")
print("=" * 70)
for arb in (False, True):
    print(f"\n-- arbitrary={arb}")
    xs = max(SCHEDULES, key=lambda x: pie(x, arb))
    P = pie(xs, arb)
    # bundled TIOLI by the fleet, transfers = harms
    g = np.array([P, 0, 0, 0])
    print(f"  bundled fleet TIOLI on {name(xs)}: gains {g}, product {nash(g)}, floor {g.min()}, "
          f"residents' share 0")
    # bundled symmetric Nash
    g = np.full(4, P / 4)
    print(f"  bundled symmetric Nash on {name(xs)}: gains {g}, product {nash(g):.3f}, floor {g.min():.3f}, "
          f"residents' share 3/4, split equal")
    # slot-by-slot symmetric Nash, additive (myopic) pricing per slot
    gains = np.zeros(4)
    run = []
    for t in range(4):
        x = np.zeros(4, int); x[t] = 1
        pt = pie(x, False)  # per-slot bargains see only additive harm
        if pt > 0:
            run.append(t)
            gains += pt / 4
    xr = np.zeros(4, int); xr[run] = 1
    true_h = harm(xr, arb)
    add_h = harm(xr, False)
    gains_true = gains.copy()
    gains_true[1:] -= (true_h - add_h)  # unpaid interaction harm
    print(f"  slot-by-slot Nash, additive clauses, runs {name(xr)}: nominal gains {gains}, "
          f"true gains {gains_true}, product {nash(gains_true):.3f}, floor {gains_true.min():.3f}, "
          f"pie realised {pie(xr, arb):.2f} of {P}, residents' share {gains_true[1:].sum()/pie(xr,arb):.3f}")
    if arb:
        # slot-by-slot, forward-looking, order M D E N, marginal harm given the slots already agreed
        agreed = np.zeros(4, int)
        gains = np.zeros(4)
        for t in range(4):
            trial = agreed.copy(); trial[t] = 1
            marg = pie(trial, arb) - pie(agreed, arb)
            if marg > 0:
                agreed = trial
                gains += marg / 4
        print(f"  slot-by-slot Nash, order MDEN, marginal pricing: runs {name(agreed)}, gains {gains}, "
              f"product {nash(gains):.3f}")
        # order E first
        agreed = np.zeros(4, int)
        gains = np.zeros(4)
        for t in [2, 1, 0, 3]:
            trial = agreed.copy(); trial[t] = 1
            marg = pie(trial, arb) - pie(agreed, arb)
            if marg > 0:
                agreed = trial
                gains += marg / 4
        print(f"  slot-by-slot Nash, order EDMN, marginal pricing, myopic order: runs {name(agreed)}, "
              f"gains {gains}, product {nash(gains):.3f}, pie {pie(agreed, arb)}")

print()
print("=" * 70)
print("C. Reopening cost of one slot after the bundle is agreed (transparent, parametric)")
print("   Bundle at symmetric Nash on MDE: each party holds 1.5.")
print("   Slot-by-slot at symmetric Nash: a party's stake in slot t is pie_t/4.")
print("   Protocol (a): renegotiation reproduces the Nash split on the changed schedule, discounted by delta.")
print("   Protocol (b): the three others TIOLI the reopener, who ends at 0.")
print("=" * 70)
xs = np.array([1, 1, 1, 0])
P = pie(xs)
for t in range(3):
    xd = xs.copy(); xd[t] = 0
    Pd = pie(xd)
    x1 = np.zeros(4, int); x1[t] = 1
    stake_slot = pie(x1) / 4
    print(f"\n  drop slot {SLOTS[t]}: pie {P} -> {Pd}; slot-by-slot cost = own quarter of slot = {stake_slot:.3f}")
    for d in (0.5, 0.8, 0.95, 1.0):
        cost_a = P / 4 - d * Pd / 4
        print(f"    bundle, protocol (a), delta={d}: cost {cost_a:.4f}  (x{cost_a/stake_slot:.2f} the slot-by-slot cost)")
    print(f"    bundle, protocol (b): cost {P/4:.3f}  (x{(P/4)/stake_slot:.2f})")

print()
print("  Under bundled fleet TIOLI the residents hold 0, so their reopening cost is 0 under both protocols;")
print("  the fleet holds 6 and its reopening cost under (a) is 6 - delta*pie_after.")

print()
print("=" * 70)
print("D. Arbitrary on: resident 3 locked into MDE by additive clauses; does reopening pay?")
print("=" * 70)
# After slot-by-slot additive Nash on MDE, resident 3 nominal 1.5, true 0.
# If the four slots are one bundle, fixing E means reopening all; renegotiation lands at MD, pie 5.
for d in (0.5, 0.8, 0.95, 1.0):
    after_a = d * 5 / 4
    print(f"  delta={d}: resident 3 now 0; reopen under (a) -> {after_a:.4f}  (gain {after_a:.4f}); under (b) -> 0")
print("  Slot-by-slot contract: resident 3 withdraws consent to E alone, loses 0.25 (its quarter of E),")
print("  removes the 1.5 interaction harm: net +1.25, no renegotiation needed. (M, D stand.)")

print()
print("=" * 70)
print("E. Wealth effects on: stakes in utility units at the symmetric Nash bundle (1.5 each in money)")
print("=" * 70)
pay = np.array([1.5, 1.5, 1.5, 1.5])
ug = util_gain(pay)
print(f"  utility gains {ug.round(4)}, Nash product in utility {np.prod(ug):.3e}")
print("  Reopening under (b) forfeits these; the poor resident forfeits the most per unit of money.")
# Utility-Nash bundle: split that maximises sum log(u(w0+t)-u(w0)) over splits of 6 (grid)
best = None
for a in np.arange(0, 6.001, 0.05):
    for b in np.arange(0, 6.001 - a, 0.05):
        for c in np.arange(0, 6.001 - a - b, 0.05):
            f = 6 - a - b - c
            g = util_gain(np.array([f, a, b, c]))
            if (g <= 0).any():
                continue
            v = np.log(g).sum()
            if best is None or v > best[0]:
                best = (v, f, a, b, c)
print(f"  utility-Nash split of 6 (fleet, r1, r2, r3): {np.round(best[1:], 2)}; the poor resident takes least money")

print()
print("=" * 70)
print("F. Finite budgets: fleet TIOLI, bundled vs slot-by-slot, fleet estimates s_i with error sigma")
print("   (switches: finite budgets on for the fleet only; residents know their own harm; enforcer assumed;")
print("    parametric). Expectations count failed deals as zero. Product = product of expected gains.")
print("=" * 70)
rng = np.random.default_rng(0)
NSIM = 20000


def opt_bundle(shat, sig):
    """Fleet picks schedule and transfers maximising expected profit, flat prior on s given shat."""
    best = (0.0, None, None)
    for x in SCHEDULES:
        if x.sum() == 0:
            continue
        E = e @ x
        prof = p @ x
        # optimise margins m_i >= 0 per resident over a grid (in units of sigma*E_i)
        # separable up to the shared (prof - sum t) factor: do coordinate ascent
        z = np.full(3, 1.0)
        for _ in range(30):
            for i in range(3):
                if E[i] == 0:
                    z[i] = 0; continue
                cand = np.linspace(-1, 4, 101)
                vals = []
                for zi in cand:
                    zz = z.copy(); zz[i] = zi
                    t = shat * E + zz * sig * E
                    probs = np.where(E > 0, norm.cdf(zz), 1.0)
                    vals.append((prof - t.sum()) * probs.prod())
                z[i] = cand[int(np.argmax(vals))]
        t = shat * E + z * sig * E
        probs = np.where(E > 0, norm.cdf(z), 1.0)
        val = (prof - t.sum()) * probs.prod()
        if val > best[0]:
            best = (val, x, t)
    return best


def opt_slot(shat, sig):
    """Per slot, fleet picks transfers maximising that slot's expected profit."""
    out = []
    for tslot in range(4):
        E = e[:, tslot]
        prof = p[tslot]
        z = np.full(3, 1.0)
        for _ in range(30):
            for i in range(3):
                if E[i] == 0:
                    z[i] = 0; continue
                cand = np.linspace(-1, 4, 101)
                vals = []
                for zi in cand:
                    zz = z.copy(); zz[i] = zi
                    t = shat * E + zz * sig * E
                    probs = np.where(E > 0, norm.cdf(zz), 1.0)
                    vals.append((prof - t.sum()) * probs.prod())
                z[i] = cand[int(np.argmax(vals))]
        t = shat * E + z * sig * E
        probs = np.where(E > 0, norm.cdf(z), 1.0)
        val = (prof - t.sum()) * probs.prod()
        out.append((val, t) if val > 0 else (0.0, None))
    return out


for sig in (1.0, 0.3, 0.1):
    # Fleet's optimisation depends on shat only through a shift, so precompute on a coarse set of shat draws
    eps = rng.normal(0, sig, size=(NSIM, 3))
    gains_b = np.zeros((NSIM, 4)); pie_b = np.zeros(NSIM); deal_b = np.zeros(NSIM)
    gains_s = np.zeros((NSIM, 4)); pie_s = np.zeros(NSIM); slots_s = np.zeros(NSIM)
    # the optimal z does not depend on shat (profit - sum t = prof - shat.E - z sig E, shat shifts a constant),
    # so compute once per sigma with shat=s and reuse the z by re-deriving t = shat*E + z*sig*E
    val, xb, tb = opt_bundle(s, sig)
    Eb = e @ xb
    zb = np.where(Eb > 0, (tb - s * Eb) / (sig * Eb), 0.0)
    slot_opt = opt_slot(s, sig)
    for n in range(NSIM):
        shat = s + eps[n]
        # bundle
        t = shat * Eb + zb * sig * Eb
        acc = (t >= s * Eb - 1e-12).all()
        if acc:
            gains_b[n, 0] = p @ xb - t.sum()
            gains_b[n, 1:] = t - s * Eb
            pie_b[n] = pie(xb); deal_b[n] = 1
        # slot by slot
        for tslot in range(4):
            v, tt = slot_opt[tslot]
            if tt is None:
                continue
            E = e[:, tslot]
            z = np.where(E > 0, (tt - s * E) / (sig * E), 0.0)
            t = shat * E + z * sig * E
            if (t >= s * E - 1e-12).all():
                gains_s[n, 0] += p[tslot] - t.sum()
                gains_s[n, 1:] += t - s * E
                x1 = np.zeros(4, int); x1[tslot] = 1
                pie_s[n] += pie(x1); slots_s[n] += 1
    gb = gains_b.mean(0); gs = gains_s.mean(0)
    print(f"\n-- sigma={sig}  bundle schedule {name(xb)}  slot-by-slot runs {[SLOTS[t] for t in range(4) if slot_opt[t][1] is not None]}")
    print(f"  bundled : deal rate {deal_b.mean():.3f}  E[pie] {pie_b.mean():.3f}  E[gains] {gb.round(3)}  "
          f"product {nash(gb):.4f}  floor {gb.min():.3f}  residents' share {gb[1:].sum()/max(pie_b.mean(),1e-9):.3f}")
    print(f"  slotwise: slots/run {slots_s.mean():.2f}  E[pie] {pie_s.mean():.3f}  E[gains] {gs.round(3)}  "
          f"product {nash(gs):.4f}  floor {gs.min():.3f}  residents' share {gs[1:].sum()/max(pie_s.mean(),1e-9):.3f}")
print("\n  Limit sigma->0: both (6; 0,0,0), product 0, floor 0.")
