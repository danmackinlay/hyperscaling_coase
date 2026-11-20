"""Finite-budget row on the hard-case instance.

Switches on: finite budgets; k=3 (k=2 in one extra block); once (multi-round block adds
within-negotiation discount delta with estimates re-drawn each round, no learning from
rejection); linear money (a log-utility column added at the end); enforcer assumed; closed.
Parametric first, arbitrary (resident 3's M&E interaction) second.

Information: fleet knows p exactly, estimates each s_i with sd eps_f (flat prior); each
resident knows own harm exactly; the residents, as a side, estimate each p_t with sd eps_N.

Arm T (take-it-or-leave-it): proposer = fleet (three separate acceptances, each resident
accepts iff t_i >= own true harm + reservation) or proposer = residents' bloc (bloc knows all
harms, demands a total T, fleet accepts iff p.x - T >= its reservation; bloc splits its
surplus equally among the three).
Arm H (haggling): random proposer, fleet with prob w (1/2 = two sides; 1/4 = four symmetric
parties), one round (rejection = no deal) or stationary multi-round with discount delta.
"""
import itertools, sys
import numpy as np
from scipy.stats import norm

rng = np.random.default_rng(20261021)
p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1, 1, 2.0])
W0 = np.array([100, 10, 10, 2.0])  # fleet, residents (wealth-effects switch)
SCHEDS = [np.array(x) for x in itertools.product([0, 1], repeat=4)]
NAMES = ["".join(n for n, b in zip("MDEN", x) if b) or "-" for x in SCHEDS]
IDX = {n: i for i, n in enumerate(NAMES)}

def true_harm(x, arb):
    h = s * (E @ x)
    if arb and x[0] == 1 and x[2] == 1:
        h = h.copy(); h[2] += 1.5
    return h

# --- 1-D inversions -----------------------------------------------------------
ZG = np.linspace(-8, 8, 16001)
G = norm.cdf(ZG) / norm.pdf(ZG)          # Phi/phi, increasing
PSI = ZG + G                              # z + Phi/phi, increasing
def ginv(y):  return np.interp(y, G, ZG)
def psiinv(y): return np.interp(y, PSI, ZG)

def fleet_offer(Ahat, sds, active):
    """Fleet's optimal markups for one schedule across draws.
    Ahat: (n,) estimated surplus net of reservations; sds: (3,) sd of each resident's estimated
    harm (0 if inactive). Returns (gain over continuation (n,), z (n,3))."""
    act = [i for i in range(3) if active[i]]
    # Psi(L) = L + sum_i sd_i g^{-1}(L/sd_i), increasing; root Psi(L) = A
    LG = np.logspace(-9, 3, 6000)
    Psi = LG + sum(sds[i] * ginv(LG / sds[i]) for i in act)
    L = np.interp(Ahat, Psi, LG)
    z = np.zeros((len(Ahat), 3))
    P = np.ones(len(Ahat))
    for i in act:
        z[:, i] = ginv(L / sds[i]); P *= norm.cdf(z[:, i])
    return L * P, z

def bloc_offer(Bhat, sd):
    z = psiinv(Bhat / sd)
    val = sd * norm.cdf(z) ** 2 / norm.pdf(z)
    return val, z

# --- one round, fleet proposes ----------------------------------------------------
def fleet_round(eps_f, n, arb=False, model="param", res=np.zeros(3), cf=0.0, k=3, cont=None):
    """Returns payoff matrix (n,4) [fleet, r1, r2, r3] for the round (failures -> cont or 0),
    plus diagnostics. model in {param, two, table} for resident 3 under the arbitrary switch."""
    noise = rng.normal(0, eps_f, (n, 3))            # fleet's error on s_i
    shat = s + noise
    # resident 3 under arbitrary: alternative fleet models
    if arb and model == "two":      # right class, two parameters, budget halved each
        e2 = np.sqrt(2) * eps_f
        shat3 = s[2] + rng.normal(0, e2, n); ihat = 1.5 + rng.normal(0, e2, n)
    if arb and model == "table":    # 16 independent entries, budget split 16 ways
        tab_noise = rng.normal(0, 4 * eps_f, (n, 16))
    best = np.full(n, -np.inf); bx = np.zeros(n, int); bz = np.zeros((n, 3)); bhat = np.zeros((n, 3))
    bpair = np.zeros((n, 3), bool); bsd = np.zeros((n, 3))
    pairs = [np.array([True, True, True])] if k == 3 else [np.array([i != j for i in range(3)]) for j in range(3)]
    for xi, x in enumerate(SCHEDS):
        if x.sum() == 0: continue
        Ex = E @ x
        for pay in pairs:
            hhat = shat * Ex                        # (n,3) estimated harms (param model)
            sds = eps_f * Ex
            if arb and model == "two":
                hhat = hhat.copy(); hhat[:, 2] = shat3 * Ex[2] + ihat * (x[0] * x[2])
                sds = sds.copy(); sds[2] = e2 * np.sqrt(Ex[2] ** 2 + (x[0] * x[2]) ** 2)
            if arb and model == "table":
                hhat = hhat.copy(); hhat[:, 2] = true_harm(x, True)[2] + tab_noise[:, xi]
                sds = sds.copy(); sds[2] = 4 * eps_f
            active = (Ex > 0) & pay
            sds = np.where(active, sds, 0.0)
            hh = np.where(active, hhat, 0.0)
            A = p @ x - hh.sum(1) - (res * pay).sum() - cf
            gain, z = fleet_offer(A, sds, active)
            upd = gain > best
            best[upd] = gain[upd]; bx[upd] = xi; bz[upd] = z[upd]; bhat[upd] = hh[upd]; bpair[upd] = pay; bsd[upd] = sds
    # realise
    pay = np.zeros((n, 4)); diag = {}
    accept = np.ones(n, bool)
    t = np.zeros((n, 3))
    for d in range(n):
        x = SCHEDS[bx[d]]; Ex = E @ x; h = true_harm(x, arb)
        sds = bsd[d]
        t[d] = np.where(bpair[d], bhat[d] + res + sds * bz[d], 0.0)
        ok = np.all((t[d] >= h + res - 1e-12) | ~bpair[d])
        accept[d] = ok
        if ok:
            pay[d, 0] = p @ x - t[d].sum(); pay[d, 1:] = t[d] - h
        elif cont is not None:
            pay[d] = cont
    diag["deal"] = accept.mean()
    diag["N_chosen"] = np.mean([SCHEDS[i][3] == 1 for i in bx])
    diag["N_dealt"] = np.mean([(SCHEDS[i][3] == 1) and a for i, a in zip(bx, accept)])
    diag["eff_chosen"] = np.mean([NAMES[i] == ("MD" if arb else "MDE") for i in bx])
    diag["pie_dealt"] = np.mean([(p @ SCHEDS[i] - true_harm(SCHEDS[i], arb).sum()) if a else 0 for i, a in zip(bx, accept)])
    diag["excluded"] = np.mean(~bpair, 0) if k < 3 else None
    vals, cnts = np.unique(bx, return_counts=True); top = np.argsort(-cnts)[:4]
    diag["top"] = ", ".join(f"{NAMES[vals[i]]} {cnts[i]/n:.2f}" for i in top)
    return pay, diag

# --- one round, bloc proposes -----------------------------------------------------
def bloc_round(eps_N, n, arb=False, cf=0.0, cN=0.0, cont=None, split="equal"):
    nu = rng.normal(0, eps_N, (n, 4))
    phat = p + nu
    best = np.full(n, -np.inf); bx = np.zeros(n, int); bz = np.zeros(n)
    for xi, x in enumerate(SCHEDS):
        if x.sum() == 0: continue
        H = true_harm(x, arb).sum(); sd = eps_N * np.sqrt(x.sum())
        B = phat @ x - cf - H - cN
        val, z = bloc_offer(B, sd)
        upd = val > best; best[upd] = val[upd]; bx[upd] = xi; bz[upd] = z[upd]
    pay = np.zeros((n, 4)); accept = np.zeros(n, bool)
    for d in range(n):
        x = SCHEDS[bx[d]]; h = true_harm(x, arb); H = h.sum(); sd = eps_N * np.sqrt(x.sum())
        m = sd * bz[d]; T = phat[d] @ x - cf - m
        fgain = p @ x - T
        if fgain >= cf - 1e-12:
            accept[d] = True; pay[d, 0] = fgain
            surplus = T - H
            if split == "equal": pay[d, 1:] = surplus / 3
            else: pay[d, 1:] = surplus * h / H
        elif cont is not None:
            pay[d] = cont
    diag = {"deal": accept.mean(),
            "N_chosen": np.mean([SCHEDS[i][3] == 1 for i in bx]),
            "N_dealt": np.mean([(SCHEDS[i][3] == 1) and a for i, a in zip(bx, accept)]),
            "eff_chosen": np.mean([NAMES[i] == ("MD" if arb else "MDE") for i in bx]),
            "pie_dealt": np.mean([(p @ SCHEDS[i] - true_harm(SCHEDS[i], arb).sum()) if a else 0 for i, a in zip(bx, accept)])}
    vals, cnts = np.unique(bx, return_counts=True); top = np.argsort(-cnts)[:4]
    diag["top"] = ", ".join(f"{NAMES[vals[i]]} {cnts[i]/n:.2f}" for i in top)
    return pay, diag

def summarise(pay):
    g = pay.mean(0)
    prod = np.prod(g) if np.all(g >= 0) else float("nan")
    u = (np.log(W0 + pay) - np.log(W0)).mean(0)
    uprod = np.prod(u) if np.all(u >= 0) else float("nan")
    tot = g.sum()
    share = g[1:].sum() / tot if tot > 0 else float("nan")
    return dict(gains=g, product=prod, floor=g.min(), total=tot, res_share=share, uprod=uprod)

def fmt(sm, diag=None, extra=""):
    g = sm["gains"]
    s_ = (f"gains ({g[0]:.2f}; {g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) tot {sm['total']:.2f} "
          f"NP {sm['product']:.3f} floor {sm['floor']:.2f} resS {sm['res_share']:.2f} uNP {sm['uprod']:.2e}")
    if diag:
        s_ += f" | deal {diag['deal']:.3f} pieE {diag['pie_dealt']:.2f} N:chosen {diag['N_chosen']:.3f} dealt {diag['N_dealt']:.3f} eff {diag['eff_chosen']:.3f} top[{diag['top']}]"
    return s_ + extra

EPS = [1.0, 0.3, 0.1]
N1 = 20000

def block_tioli(arb, model="param"):
    print(f"\n=== Arm T, fleet proposes, k=3, {'arbitrary' if arb else 'parametric'}, fleet model={model} ===")
    print("limit eps_f->0: (6; 0,0,0), NP 0, floor 0, deal 1, pie 6 (param) / 5 (arb, right model)")
    for ef in EPS:
        pay, d = fleet_round(ef, N1, arb, model)
        print(f"eps_f={ef:4}: {fmt(summarise(pay), d)}")
    print(f"\n=== Arm T, bloc proposes (equal split), {'arbitrary' if arb else 'parametric'} ===")
    print("limit eps_N->0: (0; 2,2,2) param / (0; 1.67x3) arb, NP 0, floor 0")
    for eN in EPS:
        pay, d = bloc_round(eN, N1, arb)
        print(f"eps_N={eN:4}: {fmt(summarise(pay), d)}")

def block_haggle_oneshot(arb, w, model="param"):
    print(f"\n=== Arm H one round, random proposer (fleet w={w}), {'arbitrary' if arb else 'parametric'}, fleet model={model} ===")
    lim = 6 if not arb else 5
    print(f"limit: fleet {w*lim:.2f}, residents {(1-w)*lim/3:.2f} each, NP {w*lim*((1-w)*lim/3)**3:.3f}")
    for ef in EPS:
        pf, df = fleet_round(ef, N1, arb, model)
        for eN in EPS:
            pb, db = bloc_round(eN, N1, arb)
            nf = int(round(w * N1)); pay = np.vstack([pf[:nf], pb[:N1 - nf]])
            sm = summarise(pay)
            ratio = (eN / ef) ** 2
            print(f"eps_f={ef:4} eps_N={eN:4} (c_f:c_N={ratio:6.1f}:1): {fmt(sm)} | deal f {df['deal']:.3f} b {db['deal']:.3f}; "
                  f"fleet-as-proposer takes {pf[:, 0].mean():.2f}, bloc-as-proposer total {pb[:, 1:].sum(1).mean():.2f}")

def block_haggle_multiround(arb, w, delta, model="param", n=4000, iters=40):
    print(f"\n=== Arm H stationary multi-round, delta={delta}, fleet proposes w={w}, {'arbitrary' if arb else 'parametric'} ===")
    for ef in EPS:
        for eN in EPS:
            v = np.array([w * 6, (1 - w) * 2, (1 - w) * 2, (1 - w) * 2])
            for it in range(iters):
                st = rng.bit_generator.state
                rng.bit_generator.state = np.random.default_rng(7).bit_generator.state  # common random numbers
                pf, df = fleet_round(ef, n, arb, model, res=delta * v[1:], cf=delta * v[0], cont=delta * v)
                pb, db = bloc_round(eN, n, arb, cf=delta * v[0], cN=delta * v[1:].sum(), cont=delta * v)
                rng.bit_generator.state = st
                vnew = w * pf.mean(0) + (1 - w) * pb.mean(0)
                if np.max(np.abs(vnew - v)) < 1e-4: v = vnew; break
                v = vnew
            g = v; prod = np.prod(g) if np.all(g >= 0) else float("nan")
            print(f"eps_f={ef:4} eps_N={eN:4}: v=({g[0]:.2f}; {g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) tot {g.sum():.2f} NP {prod:.3f} floor {g.min():.2f} "
                  f"| per-round deal f {df['deal']:.3f} b {db['deal']:.3f}; its {it+1}")

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "T"):
        block_tioli(False)
        print("\n=== Arm T, fleet proposes, k=2 (fleet buys two of three), parametric ===")
        for ef in EPS:
            pay, d = fleet_round(ef, N1, False, k=2)
            print(f"eps_f={ef:4}: {fmt(summarise(pay), d)} excluded freq (r1,r2,r3)={np.round(d['excluded'],3)}")
    if which in ("all", "H"):
        for w in (0.5, 0.25):
            block_haggle_oneshot(False, w)
    if which in ("all", "A"):
        for model in ("param", "two", "table"):
            block_tioli(True, model) if model == "param" else None
            if model != "param":
                print(f"\n=== Arm T, fleet proposes, arbitrary, fleet model={model} ===")
                for ef in EPS:
                    pay, d = fleet_round(ef, N1, True, model)
                    print(f"eps_f={ef:4}: {fmt(summarise(pay), d)}")
        block_haggle_oneshot(True, 0.25, "param")
        block_haggle_oneshot(True, 0.25, "two")
    if which in ("all", "M"):
        for delta in (0.5, 0.8, 0.95):
            block_haggle_multiround(False, 0.25, delta)
