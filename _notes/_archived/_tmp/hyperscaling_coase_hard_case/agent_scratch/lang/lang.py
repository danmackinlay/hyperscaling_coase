import itertools, math
import numpy as np
from scipy.optimize import minimize

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1, 1, 2.0])
SLOTS = "MDEN"
scheds = [tuple(x) for x in itertools.product([0, 1], repeat=4)]

def harms(x, arb):
    x = np.array(x)
    h = s * (E @ x)
    if arb and x[0] and x[2]:
        h = h.copy(); h[2] += 1.5
    return h

def name(x):
    return "".join(c for c, b in zip(SLOTS, x) if b) or "none"

LANGS = {
    "four-slot": scheds,
    "two-slot day=MDE|night=N": [(0,0,0,0), (1,1,1,0), (0,0,0,1), (1,1,1,1)],
    "two-slot alt day=MD|EN": [(0,0,0,0), (1,1,0,0), (0,0,1,1), (1,1,1,1)],
    "one-slot": [(0,0,0,0), (1,1,1,1)],
}

def best(lang, arb):
    out = max(lang, key=lambda x: p @ np.array(x) - harms(x, arb).sum())
    return out, p @ np.array(out) - harms(out, arb).sum()

print("== enumeration check, arbitrary efficient")
for arb in (0, 1):
    top = sorted(scheds, key=lambda x: -(p @ np.array(x) - harms(x, arb).sum()))[:4]
    print(arb, [(name(x), round(p @ np.array(x) - harms(x, arb).sum(), 2)) for x in top])

w0 = np.array([100, 10, 10, 2.0])

def nbs_log(pie_x, x, arb):
    # money gains g (fleet, r1..r3) summing to pie, maximise sum log(log(w0+g)-log(w0))
    def f(z):
        g = np.append(z, pie_x - z.sum())
        if np.any(g <= 1e-9): return 1e9
        return -np.sum(np.log(np.log(w0 + g) - np.log(w0)))
    r = minimize(f, np.full(3, pie_x / 4), method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-12, maxiter=20000))
    g = np.append(r.x, pie_x - r.x.sum())
    ug = np.log(w0 + g) - np.log(w0)
    return g, ug

def nbs_uniform(lang, arb):
    # standard form: one transfer t to every resident; deal (x,t) needs t>=h_i(x) all i and fleet gain>=0
    bestv = None
    for x in lang:
        if sum(x) == 0: continue
        h = harms(x, arb); px = p @ np.array(x)
        lo, hi = h.max(), px / 3
        if hi <= lo: continue
        ts = np.linspace(lo, hi, 200001)[1:-1]
        prod = (px - 3 * ts) * np.prod(ts[:, None] - h[None, :], axis=1)
        i = prod.argmax()
        cand = (prod[i], x, ts[i], px - 3 * ts[i], ts[i] - h)
        if bestv is None or cand[0] > bestv[0]: bestv = cand
    return bestv

for arb in (0, 1):
    print(f"\n######## {'ARBITRARY' if arb else 'PARAMETRIC'} ########")
    for ln, lang in LANGS.items():
        x, pie = best(lang, arb)
        h = harms(x, arb)
        g = pie / 4
        print(f"\n[{ln}] schedule {name(x)} pie {pie:.3f}; harms {h}")
        print(f"  NBS linear: gains {g:.3f} each; transfers {np.round(h+g,3)}; Nash product {g**4:.4f}; residents' share {0.75*pie:.3f}")
        gm, ug = nbs_log(pie, x, arb)
        print(f"  NBS log-utility: money gains (f;r1,r2,r3) {np.round(gm,3)}; utility gains {np.round(ug,4)}; product {np.prod(ug):.3e}; floor {ug.min():.4f}; residents' money share {gm[1:].sum():.3f}")
        u = nbs_uniform(lang, arb)
        if u is None:
            print("  uniform standard form: no deal")
        else:
            prod, xu, t, gf, gr = u
            print(f"  uniform standard form: schedule {name(xu)} t={t:.3f} gains (f;r) ({gf:.3f};{np.round(gr,3)}) pie {gf+gr.sum():.3f} product {prod:.4f} floor {min(gf, gr.min()):.3f}")

print("\n== k=2: fleet + cheapest pair, excluded resident unpaid")
for arb in (0, 1):
    for ln, lang in LANGS.items():
        res = []
        for pair in [(0, 1), (0, 2), (1, 2)]:
            x = max(lang, key=lambda x: p @ np.array(x) - harms(x, arb)[list(pair)].sum())
            v = p @ np.array(x) - harms(x, arb)[list(pair)].sum()
            out = [i for i in range(3) if i not in pair][0]
            res.append((round(v, 2), name(x), f"excl r{out+1}", round(-harms(x, arb)[out], 2)))
        print(arb, ln, res)
