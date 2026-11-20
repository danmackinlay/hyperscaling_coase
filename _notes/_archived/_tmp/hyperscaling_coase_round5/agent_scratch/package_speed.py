"""One contract vs four: how fast a growing speed advantage converts to share.

Base instance (noise schedule): p0 = (4, 5.5, 4, 5); exposures e_i; sensitivities s = (1, 1, 2).
Recurring switch on at delta; clause-language switch: 'one' (package) or 'four' (slot by slot).

Period 0: all four agents equal compute -> proposer drawn by party uniformly -> fair deal.
Periods >= 1: company's compute is R times each resident's.
Each period, with prob lam, one slot t (uniform) has p_t shifted by +-shock (persistent).
A shock is cause to reopen the contract covering slot t: under 'one', the whole deal;
under 'four', slot t alone. A reopened contract is void; the parties bargain over the
surplus in play by random-proposer unanimity bargaining (Baron-Ferejohn with unanimity):
recognition prob pi_i = c_i^a / sum c^a; expected gain V_i = pi_i * S exactly, every delta.
Slot surplus S_t = p_t - H_t with H = (2.5, 2, 3, 5.5); a slot runs iff S_t > 0.
Optional: arbitrary-preferences switch (Carol's +1.5 when M and E both run); only the
package form can price it; slot by slot Carol bears it unpaid.
"""
import numpy as np
import itertools

P0 = np.array([4.0, 5.5, 4.0, 5.0])
E = np.array([[0.5, 0, 0.5, 1.0], [1.0, 1.0, 0.5, 0.5], [0.5, 0.5, 1.0, 2.0]])
S_I = np.array([1.0, 1.0, 2.0])
H = (S_I[:, None] * E).sum(0)          # (2.5, 2, 3, 5.5)
HARM_I = S_I[:, None] * E              # per-resident harm per slot
STATUS_QUO = -(HARM_I[:, :3].sum(1))   # ordinance: M, D, E run unpaid -> (-1, -2.5, -4)


def shares(cf, cn, a=1.0):
    c = np.array([cf, cn, cn, cn]) ** a
    return c / c.sum()                  # company, Alice, Bob, Carol


def package_pie(p, arbitrary):
    """Efficient schedule and its pie under the package (every schedule priceable)."""
    best, bx = -1e9, None
    for x in itertools.product([0, 1], repeat=4):
        x = np.array(x)
        harm = (HARM_I * x).sum()
        if arbitrary and x[0] and x[2]:
            harm += 1.5
        pie = (p * x).sum() - harm
        if pie > best:
            best, bx = pie, x
    return max(best, 0.0), bx


def simulate(form, R, delta, lam, shock, a=1.0, arbitrary=False, T=240, sims=4000, seed=0):
    rng = np.random.default_rng(seed)
    disc = (1 - delta) * delta ** np.arange(T)   # normalise PV to a per-period equivalent
    gains = np.zeros((sims, 4))
    first_shock = np.zeros(sims)
    for k in range(sims):
        p = P0.copy()
        # period-0 contract at equal compute
        pi = shares(1, 1, a)
        if form == "one":
            pie, _ = package_pie(p, arbitrary)
            g = pi * pie
            if arbitrary:  # package prices Carol's term: already inside pie
                pass
        else:
            S = np.maximum(p - H, 0)
            g = (pi[:, None] * S[None, :]).sum(1)
            if arbitrary and S[0] > 0 and S[2] > 0:
                g[3] -= 1.5           # Carol bears the unpaid interaction
            slot_share = np.tile(pi[:, None], (1, 4))   # share of each slot per party
        total = np.zeros(4)
        fs = T
        for t in range(T):
            total += disc[t] * g
            if t >= 0 and rng.random() < lam:
                if fs == T:
                    fs = t
                j = rng.integers(4)
                p[j] += shock if rng.random() < 0.5 else -shock
                pi = shares(R, 1, a)
                if form == "one":
                    pie, _ = package_pie(p, arbitrary)
                    g = pi * pie
                else:
                    S = np.maximum(p - H, 0)
                    slot_share[:, j] = pi
                    g = (slot_share * S[None, :]).sum(1)
                    if arbitrary and S[0] > 0 and S[2] > 0:
                        g[3] -= 1.5
        gains[k] = total
        first_shock[k] = fs
    return gains.mean(0), first_shock.mean()


def gm_fraction(g):
    pos = g[g > 0]
    gm = np.exp(np.log(pos).mean()) if len(pos) else 0.0
    return gm / (g.sum() / 4), gm


def row(label, g):
    frac, gm = gm_fraction(g)
    res = g[1:]
    print(f"{label:38s} co {g[0]:5.2f} | A {g[1]:5.2f} B {g[2]:5.2f} C {g[3]:5.2f} | "
          f"GM {gm:4.2f} ({frac:4.2f} of max) floor {g.min():5.2f} res share {res.sum()/g.sum():4.2f} "
          f"| vs ordinance A {g[1]-STATUS_QUO[0]:+.2f} B {g[2]-STATUS_QUO[1]:+.2f} C {g[3]-STATUS_QUO[2]:+.2f}")


if __name__ == "__main__":
    print("H per slot", H, " surplus at p0", P0 - H, " pie", np.maximum(P0 - H, 0).sum())
    print("status quo (ordinance) resident positions", STATUS_QUO)
    print("\n== Main: delta=0.95 lam=0.2 shock=1, company compute R x each resident after period 0 ==")
    for R in (1, 3, 10):
        for form in ("four", "one"):
            g, fs = simulate(form, R, 0.95, 0.2, 1.0)
            row(f"R={R:2d} form={form}", g)
        print(f"   (mean time to first shock anywhere {fs:.1f} periods; per slot {4/0.2:.0f})")
    print("\n== Mirror: residents 10x each, company 1 ==")
    for form in ("four", "one"):
        g, _ = simulate(form, 0.1, 0.95, 0.2, 1.0)
        row(f"residents 10x form={form}", g)
    print("\n== Robustness: sign of (one - four) on each resident's gain, R=10 ==")
    for delta in (0.5, 0.8, 0.95):
        for lam in (0.05, 0.2, 0.5):
            for shock in (0.5, 1.0, 2.0):
                for a in (0.5, 1.0, 2.0):
                    g1, _ = simulate("one", 10, delta, lam, shock, a, sims=1500, seed=1)
                    g4, _ = simulate("four", 10, delta, lam, shock, a, sims=1500, seed=1)
                    d = g1 - g4
                    print(f"delta={delta} lam={lam:4.2f} shock={shock} a={a}: one-four co {d[0]:+.2f} A {d[1]:+.2f} B {d[2]:+.2f} C {d[3]:+.2f}")
    print("\n== Arbitrary-preferences switch on (Carol's sleep term), delta=0.95 lam=0.2 shock=1 ==")
    for R in (1, 10):
        for form in ("four", "one"):
            g, _ = simulate(form, R, 0.95, 0.2, 1.0, arbitrary=True)
            row(f"ARB R={R:2d} form={form}", g)
    print("\n== Long run (delta -> 1 proxy: delta=0.999, T=4000, few sims) R=10 ==")
    for form in ("four", "one"):
        g, _ = simulate(form, 10, 0.999, 0.2, 1.0, T=4000, sims=300, seed=2)
        row(f"long-run form={form}", g)
