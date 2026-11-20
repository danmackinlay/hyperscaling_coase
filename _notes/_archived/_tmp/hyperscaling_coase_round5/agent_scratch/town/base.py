"""Base instance replication: four slots, three residents, pie 6 at sbar=(1,1,2), k=3.

Fleet proposes schedule x and per-resident take-it-or-leave-it payments t_i.
Private s_i ~ U[2/3 sbar_i, 4/3 sbar_i] (unsure within a factor of two, mean sbar_i).
Fleet's estimation dial: shat_i = s_i + tau z, tau in {none, 1, 0.3, 0.1, 0}.
detour=False: value per slot p_t over no deal 0.  detour=True: reroute at 3 per slot, so the
deal is worth min(p_t,3)=3 per slot over the fleet's no-deal (rerouting everything, payoff 6.5).
"""
import itertools, sys
import numpy as np

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
sbar = np.array([1, 1, 2.0])
X = np.array(list(itertools.product([0, 1], repeat=4)))[1:]  # 15 non-empty schedules
EX = X @ E.T  # (15,3) exposure sums per schedule per resident
G = 201
u = np.linspace(0, 1, G)


def grids(lo_f, hi_f):
    return np.array([sbar[i] * (lo_f + (hi_f - lo_f) * u) for i in range(3)])  # (3,G)


def fleet(shat, tau, val, sg):
    """Best (schedule, offers) given posterior; returns (xi, t) or None."""
    if tau is None:
        post = np.ones((3, G))
    else:
        post = np.exp(-0.5 * ((sg - shat[:, None]) / tau) ** 2)
    post /= post.sum(axis=1, keepdims=True)
    F = np.clip(np.cumsum(post, axis=1), 1e-300, 1)
    logF = np.log(F)
    best = (0.0, None, None)
    for xi in range(len(X)):
        V = val[X[xi] == 1].sum()
        ex = EX[xi]
        idx = np.full(3, G - 1)
        cost = lambda idx: sum(sg[i, idx[i]] * ex[i] for i in range(3))
        for _ in range(50):
            changed = False
            for i in range(3):
                if ex[i] == 0:
                    idx[i] = 0; continue
                rest = cost(idx) - sg[i, idx[i]] * ex[i]
                A = V - rest - sg[i] * ex[i]
                lf = sum(logF[j, idx[j]] for j in range(3) if j != i and ex[j] > 0)
                obj = np.where(A > 0, np.log(np.clip(A, 1e-300, None)) + logF[i] + lf, -np.inf)
                k = int(obj.argmax())
                if k != idx[i]:
                    idx[i] = k; changed = True
            if not changed:
                break
        pa = np.exp(sum(logF[i, idx[i]] for i in range(3) if ex[i] > 0))
        ep = (V - cost(idx)) * pa
        if ep > best[0]:
            t = np.array([sg[i, idx[i]] * ex[i] if ex[i] > 0 else 0 for i in range(3)])
            best = (ep, xi, t)
    return best[1], best[2]


def outcome(s, xi, t, val):
    if xi is None:
        return np.zeros(4)
    h = s * EX[xi]
    if np.any(t < h - 1e-12):
        return np.zeros(4)
    return np.array([val[X[xi] == 1].sum() - t.sum(), *(t - h)])


def maxpie(s, val):
    sur = val - (s[:, None] * E).sum(axis=0)
    return np.clip(sur, 0, None).sum()


def run(tau, detour, draws, lo_f=2/3, hi_f=4/3, seed=7):
    rng = np.random.default_rng(seed)
    val = np.full(4, 3.0) if detour else p
    sg = grids(lo_f, hi_f)
    G_ = []; MP = []
    for _ in range(draws):
        s = sbar * (lo_f + (hi_f - lo_f) * rng.random(3))
        if tau == 0:
            # full information: best schedule, pay harms exactly
            sur = [(val[X[xi] == 1].sum() - (s * EX[xi]).sum(), xi) for xi in range(len(X))]
            b, xi = max(sur)
            g = outcome(s, xi, s * EX[xi], val) if b > 0 else np.zeros(4)
        else:
            shat = None if tau is None else s + tau * rng.standard_normal(3)
            xi, t = fleet(shat, tau, val, sg)
            g = outcome(s, xi, t, val)
        G_.append(g); MP.append(maxpie(s, val))
    G_ = np.array(G_); MP = np.array(MP)
    Eg = G_.mean(axis=0)
    gm = np.exp(np.log(Eg).mean()) if np.all(Eg > 0) else 0.0
    return Eg, gm / (MP.mean() / 4), G_.sum(axis=1).mean() / MP.mean(), (G_[:, 1:].min(axis=1)).mean(), (G_.sum(1) > 0).mean()


def club(detour, draws, lo_f=2/3, hi_f=4/3, seed=7):
    """Each resident posts the most it could mind given public info: hi_f*sbar_i*exposure."""
    rng = np.random.default_rng(seed)
    val = np.full(4, 3.0) if detour else p
    G_ = []; MP = []
    for _ in range(draws):
        s = sbar * (lo_f + (hi_f - lo_f) * rng.random(3))
        best = (0, None)
        for xi in range(len(X)):
            t = hi_f * sbar * EX[xi]
            gain = val[X[xi] == 1].sum() - t.sum()
            if gain > best[0] + 1e-12:
                best = (gain, xi)
        xi = best[1]
        g = outcome(s, xi, hi_f * sbar * EX[xi], val) if xi is not None else np.zeros(4)
        G_.append(g); MP.append(maxpie(s, val))
    G_ = np.array(G_); MP = np.array(MP)
    Eg = G_.mean(axis=0)
    gm = np.exp(np.log(Eg).mean()) if np.all(Eg > 0) else 0.0
    return Eg, gm / (MP.mean() / 4), G_.sum(axis=1).mean() / MP.mean(), (G_[:, 1:].min(axis=1)).mean(), (G_.sum(1) > 0).mean()


if __name__ == "__main__":
    draws = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    lo_f = float(sys.argv[2]) if len(sys.argv) > 2 else 2/3
    hi_f = float(sys.argv[3]) if len(sys.argv) > 3 else 4/3
    print(f"prior s_i ~ U[{lo_f:.3f}, {hi_f:.3f}] * sbar; draws={draws}")
    for detour in [False, True]:
        print("\n== detour" if detour else "\n== no detour (base)")
        print("tau    E[gain] fleet, Alice, Bob, Carol      crit  eff   floor  dealrate")
        for tau in [None, 1.0, 0.3, 0.1, 0]:
            Eg, c, eff, fl, dr = run(tau, detour, draws, lo_f, hi_f)
            print(f"{str(tau):5s} " + " ".join(f"{v:6.3f}" for v in Eg) + f"   {c:5.3f} {eff:5.2f} {fl:6.3f} {dr:5.2f}")
        Eg, c, eff, fl, dr = club(detour, draws, lo_f, hi_f)
        print("club  " + " ".join(f"{v:6.3f}" for v in Eg) + f"   {c:5.3f} {eff:5.2f} {fl:6.3f} {dr:5.2f}")
