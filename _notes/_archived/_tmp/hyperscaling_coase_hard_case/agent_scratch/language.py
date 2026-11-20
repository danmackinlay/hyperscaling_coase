import itertools, math
import numpy as np

SLOTS = ["M","D","E","N"]
p = np.array([4.0, 5.5, 4.0, 5.0])
e = np.array([[0.5,0,0.5,1.0],[1,1,0.5,0.5],[0.5,0.5,1,2]])
s = np.array([1.0,1.0,2.0])
w0 = np.array([10.0,10.0,2.0]); w0f = 100.0

ALL = [np.array(x) for x in itertools.product([0,1],repeat=4)]

def harms(x, arbitrary):
    h = s * (e @ x)
    if arbitrary and x[0]==1 and x[2]==1:
        h = h.copy(); h[2] += 1.5
    return h

def profit(x): return float(p @ x)
def pie(x, arb): return profit(x) - harms(x,arb).sum()

# clause languages: set of expressible schedules
LANG = {
 "4-slot": ALL,
 "2-slot A day={M,D} night={E,N}": [np.array(x) for x in [(0,0,0,0),(1,1,0,0),(0,0,1,1),(1,1,1,1)]],
 "2-slot B day={M,D,E} night={N}": [np.array(x) for x in [(0,0,0,0),(1,1,1,0),(0,0,0,1),(1,1,1,1)]],
 "1-slot all-or-nothing": [np.array(x) for x in [(0,0,0,0),(1,1,1,1)]],
}

def name(x): return "".join(SLOTS[i] for i in range(4) if x[i]) or "none"

def nash_uniform(x, arb):
    """Nash product over a single per-head price t paid to every resident."""
    h = harms(x,arb); P = profit(x)
    lo = h.max(); hi = P/3
    if hi <= lo: return None
    best=None
    for t in np.linspace(lo, hi, 20001)[1:-1]:
        g = np.array([P-3*t, t-h[0], t-h[1], t-h[2]])
        prod = float(np.prod(g))
        if best is None or prod>best[0]: best=(prod,t,g)
    return best

def nash_wealth(x, arb):
    """Nash bargaining in utility units: max sum log(u_i(g_i)) s.t. sum g = pie."""
    P = pie(x,arb)
    if P<=0: return None
    from scipy.optimize import minimize
    W = np.array([w0f, *w0])
    def obj(g3):
        g = np.array([P-g3.sum(), *g3])
        if (g<=1e-9).any(): return 1e9
        u = np.log(W+g)-np.log(W)
        return -np.sum(np.log(u))
    r = minimize(obj, np.full(3,P/4), method="Nelder-Mead", options=dict(xatol=1e-10,fatol=1e-12,maxiter=20000))
    g = np.array([P-r.x.sum(), *r.x]); u = np.log(W+g)-np.log(W)
    return g, u, float(np.prod(u))

print("=== Enumeration of 16 schedules ===")
for arb in [False, True]:
    print(f"\n-- {'ARBITRARY' if arb else 'PARAMETRIC'} preferences --")
    for x in ALL:
        print(f"{name(x):5s} profit {profit(x):5.1f} harms {harms(x,arb)} pie {pie(x,arb):5.2f}")

print("\n=== Best expressible schedule per language ===")
for arb in [False, True]:
    print(f"\n-- {'ARBITRARY' if arb else 'PARAMETRIC'} (max pie {max(pie(x,arb) for x in ALL):.2f}) --")
    for L, xs in LANG.items():
        xb = max(xs, key=lambda x: pie(x,arb))
        P = pie(xb,arb); h = harms(xb,arb)
        q = P/4
        print(f"{L:34s} -> {name(xb):5s} pie {P:4.2f} harms {h} Nash equal gains {q:.4f} each, transfers {h+q}, product {q**4:.4f}, floor {q:.4f}, residents' share 3/4")
        u = nash_uniform(xb,arb)
        if u: print(f"   uniform per-head price: t={u[1]:.3f} gains (f;r1,r2,r3)={np.round(u[2],3)} product {u[0]:.4f} floor {u[2].min():.3f}")
        else: print(f"   uniform per-head price: NO DEAL (3*max harm {3*h.max():.1f} > profit {profit(xb):.1f})")
        # uniform price over any expressible schedule
        best=None
        for x in xs:
            uu = nash_uniform(x,arb)
            if uu and (best is None or uu[0]>best[0][0]): best=(uu,x)
        if best: print(f"   best uniform-price deal in language: {name(best[1])} product {best[0][0]:.4f} gains {np.round(best[0][2],3)}")
        else: print("   best uniform-price deal in language: none")
        w = nash_wealth(xb,arb)
        if w: print(f"   wealth effects: money gains {np.round(w[0],3)} utility gains {np.round(w[1],4)} product {w[2]:.3e}")
