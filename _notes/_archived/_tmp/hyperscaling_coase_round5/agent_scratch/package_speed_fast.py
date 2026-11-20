"""Vectorised version of package_speed.py (same model, same parameters; see its docstring)."""
import numpy as np
import itertools

P0 = np.array([4.0, 5.5, 4.0, 5.0])
E = np.array([[0.5, 0, 0.5, 1.0], [1.0, 1.0, 0.5, 0.5], [0.5, 0.5, 1.0, 2.0]])
S_I = np.array([1.0, 1.0, 2.0])
HARM_I = S_I[:, None] * E
H = HARM_I.sum(0)
STATUS_QUO = -(HARM_I[:, :3].sum(1))
X = np.array(list(itertools.product([0, 1], repeat=4)), dtype=float)   # 16 schedules
HX = (X @ HARM_I.T).sum(1)                                              # additive harm per schedule
ME = (X[:, 0] * X[:, 2])                                                # M and E both run


def shares(cf, cn, a=1.0):
    c = np.array([cf, cn, cn, cn]) ** a
    return c / c.sum()


def pies(p, arbitrary):
    """p: (sims,4) -> package pie (sims,), per-slot surplus (sims,4)."""
    prof = p @ X.T                                      # (sims,16)
    harm = HX[None, :] + (1.5 * ME[None, :] if arbitrary else 0)
    pie = np.maximum((prof - harm).max(1), 0)
    S = np.maximum(p - H, 0)
    return pie, S


def simulate(form, R, delta, lam, shock, a=1.0, arbitrary=False, T=240, sims=4000, seed=0):
    rng = np.random.default_rng(seed)
    disc = (1 - delta) * delta ** np.arange(T)
    p = np.tile(P0, (sims, 1))
    pi0 = shares(1, 1, a)
    piR = shares(R, 1, a)
    pie, S = pies(p, arbitrary)
    if form == "one":
        g = pi0[None, :] * pie[:, None]
    else:
        slot_share = np.tile(pi0[None, :, None], (sims, 1, 4))     # (sims, party, slot)
        g = (slot_share * S[:, None, :]).sum(2)
        if arbitrary:
            g[:, 3] -= 1.5 * ((S[:, 0] > 0) & (S[:, 2] > 0))
    total = np.zeros((sims, 4))
    first = np.full(sims, T)
    for t in range(T):
        total += disc[t] * g
        hit = rng.random(sims) < lam
        if not hit.any():
            continue
        first = np.where(hit & (first == T), t, first)
        j = rng.integers(4, size=sims)
        sign = np.where(rng.random(sims) < 0.5, shock, -shock)
        p[hit, j[hit]] += sign[hit]
        pie, S = pies(p, arbitrary)
        if form == "one":
            g = np.where(hit[:, None], piR[None, :] * pie[:, None], g)
        else:
            idx = np.where(hit)[0]
            slot_share[idx, :, j[idx]] = piR[None, :]
            g_new = (slot_share * S[:, None, :]).sum(2)
            if arbitrary:
                g_new[:, 3] -= 1.5 * ((S[:, 0] > 0) & (S[:, 2] > 0))
            g = g_new   # unchanged slots keep their shares; S recomputed only where p changed
    return total.mean(0), first.mean()


def gm_fraction(g):
    pos = g[g > 0]
    gm = np.exp(np.log(pos).mean()) if len(pos) else 0.0
    return gm / (g.sum() / 4), gm


def row(label, g):
    frac, gm = gm_fraction(g)
    res = g[1:]
    print(f"{label:34s} co {g[0]:5.2f} | A {g[1]:5.2f} B {g[2]:5.2f} C {g[3]:5.2f} | "
          f"GM {gm:4.2f} ({frac:4.2f} of max) floor {g.min():5.2f} res {res.sum()/g.sum():4.2f} "
          f"| vs ordinance A {g[1]-STATUS_QUO[0]:+.2f} B {g[2]-STATUS_QUO[1]:+.2f} C {g[3]-STATUS_QUO[2]:+.2f}")


if __name__ == "__main__":
    print("H", H, "surplus at p0", P0 - H, "pie", np.maximum(P0 - H, 0).sum(), "ordinance positions", STATUS_QUO)
    print("\n== Main: delta=0.95 lam=0.2 shock=1; company compute R x each resident after period 0 ==")
    for R in (1, 3, 10):
        for form in ("four", "one"):
            g, fs = simulate(form, R, 0.95, 0.2, 1.0)
            row(f"R={R:2d} form={form}", g)
    print(f"   mean period of first shock anywhere {fs:.1f}; expected per slot {4/0.2:.0f}")
    print("\n== One-shot (no shocks): lam=0 ==")
    for form in ("four", "one"):
        g, _ = simulate(form, 10, 0.95, 0.0, 1.0)
        row(f"R=10 lam=0 form={form}", g)
    print("\n== Mirror: residents 10x each, company 1 ==")
    for form in ("four", "one"):
        g, _ = simulate(form, 0.1, 0.95, 0.2, 1.0)
        row(f"residents 10x form={form}", g)
    print("\n== Robustness: (one - four) per party, R=10 ==")
    for delta in (0.5, 0.8, 0.95):
        for lam in (0.05, 0.2, 0.5):
            for shock in (0.5, 1.0, 2.0):
                for a in (0.5, 1.0, 2.0):
                    g1, _ = simulate("one", 10, delta, lam, shock, a, sims=3000, seed=1)
                    g4, _ = simulate("four", 10, delta, lam, shock, a, sims=3000, seed=1)
                    d = g1 - g4
                    print(f"delta={delta} lam={lam:4.2f} shock={shock} a={a}: one-four co {d[0]:+.2f} A {d[1]:+.2f} B {d[2]:+.2f} C {d[3]:+.2f}")
    print("\n== Arbitrary-preferences switch on (Carol's sleep term), delta=0.95 lam=0.2 shock=1 ==")
    for R in (1, 10):
        for form in ("four", "one"):
            g, _ = simulate(form, R, 0.95, 0.2, 1.0, arbitrary=True)
            row(f"ARB R={R:2d} form={form}", g)
    print("\n== Long run proxy: delta=0.999, T=6000, R=10 ==")
    for form in ("four", "one"):
        g, _ = simulate(form, 10, 0.999, 0.2, 1.0, T=6000, sims=500, seed=2)
        row(f"long-run form={form}", g)
    print("\n== Lifetime of the fair deal: P(fair deal intact at t) under each form, lam=0.2 ==")
    lam = 0.2
    for t in (1, 5, 10, 20, 40):
        print(f"t={t:3d}: one {(1-lam)**t:.3f}   four (evening slot) {(1-lam/4)**t:.3f}   four (all three slots) {((1-lam/4)**t)**3:.3f}")
