"""Optimist's advocate: enumeration on the hard-case instance (16 schedules).
Rows: bits, language, scale, wealth, bundling. Every number quoted in the report
comes from here."""
import itertools, math
import numpy as np

SLOTS = ["M", "D", "E", "N"]
p = np.array([4.0, 5.5, 4.0, 5.0])
e = np.array([[0.5, 0, 0.5, 1.0], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1.0, 1.0, 2.0])
w0 = np.array([100.0, 10.0, 10.0, 2.0])  # fleet, r1, r2, r3
X = [np.array(b, float) for b in itertools.product([0, 1], repeat=4)]

def name(x):
    return "".join(SLOTS[t] for t in range(4) if x[t]) or "none"

def harms(x, arbitrary=False, insul=(0, 0, 0), halve_interaction=True):
    ee = e.copy()
    for i in range(3):
        if insul[i]:
            ee[i] = ee[i] / 2
    h = s * (ee @ x)
    if arbitrary and x[0] and x[2]:
        h[2] += 1.5 * (0.5 if (insul[2] and halve_interaction) else 1.0)
    return h

def surplus(x, **kw):
    h = harms(x, **kw)
    return p @ x - h.sum(), h

def nash_money(pie, n=4):
    return pie / n

def product(g):
    g = np.asarray(g, float)
    if (g < 0).any():
        return float("nan")
    return float(np.prod(g))

print("=== BASELINE (parametric, once, linear, enforcer, closed, k=3) ===")
rows = []
for x in X:
    S, h = surplus(x)
    rows.append((S, name(x), p @ x, h))
for S, nm, prof, h in sorted(rows, reverse=True):
    print(f"{nm:5s} profit {prof:5.1f} harms {h} pie {S:5.2f}")
best = max(rows)
print("efficient:", best[1], "pie", best[0])
g = nash_money(best[0])
print(f"Nash split {g} each; product {g**4:.4f}; transfers {best[3] + g}; residents' share {3*g/best[0]:.3f}")

print("\n=== BITS: arbitrary preferences (resident 3 table) ===")
rows_a = []
for x in X:
    S, h = surplus(x, arbitrary=True)
    rows_a.append((S, name(x), p @ x, h))
for S, nm, prof, h in sorted(rows_a, reverse=True)[:6]:
    print(f"{nm:5s} profit {prof:5.1f} harms {h} pie {S:5.2f}")
best_a = max(rows_a)
ga = nash_money(best_a[0])
print("efficient:", best_a[1], "pie", best_a[0], f"Nash {ga} each, product {ga**4:.4f}, transfers {best_a[3]+ga}")
# parametric agent's contract (MDE, payments on scalar model) evaluated under true table
x_mde = np.array([1, 1, 1, 0.0])
S_par, h_par = surplus(x_mde)  # believed
S_true, h_true = surplus(x_mde, arbitrary=True)
t_par = h_par + nash_money(S_par)
gains = np.concatenate([[p @ x_mde - t_par.sum()], t_par - h_true])
print(f"parametric contract MDE under true prefs: pie {S_true}, transfers {t_par}, gains {gains}, product {product(gains):.4f}, floor {gains.min()}")
# scalar fit: fleet fits s3 by least squares to resident 3's true table over 16 schedules
A = np.array([e[2] @ x for x in X]); b = np.array([harms(x, arbitrary=True)[2] for x in X])
s3_fit = (A @ b) / (A @ A)
print(f"best scalar fit for resident 3: s3 = {s3_fit:.3f} (true additive 2)")
rows_fit = []
for x in X:
    h = s * (e @ x); h[2] = s3_fit * (e[2] @ x)
    rows_fit.append((p @ x - h.sum(), name(x), h))
bf = max(rows_fit)
print("schedule a scalar-fitting agent picks:", bf[1], "believed pie", round(bf[0], 3))
xx = X[[name(x) for x in X].index(bf[1])]
S_t, h_t = surplus(xx, arbitrary=True)
t_fit = bf[2] + nash_money(bf[0])
gains = np.concatenate([[p @ xx - t_fit.sum()], t_fit - h_t])
print(f"  under true prefs: pie {S_t}, gains {gains}, product {product(gains):.4f}, floor {gains.min():.3f}")

print("\n=== LANGUAGE: clause menus ===")
langs = {
    "4 slots": X,
    "2 clauses day{M,D,E}/night{N}": [np.array([a, a, a, b], float) for a in (0, 1) for b in (0, 1)],
    "2 clauses day{M,D}/night{E,N}": [np.array([a, a, b, b], float) for a in (0, 1) for b in (0, 1)],
    "1 clause all-or-nothing": [np.zeros(4), np.ones(4)],
}
for arb in (False, True):
    print(" arbitrary preferences:", arb)
    for L, xs in langs.items():
        cands = [(surplus(x, arbitrary=arb)[0], name(x)) for x in xs]
        S, nm = max(cands)
        gg = nash_money(S) if S > 0 else 0
        print(f"  {L:32s} best {nm:5s} pie {S:5.2f} Nash {gg:.3f} each product {gg**4:.4f}")

print("\n=== WEALTH EFFECTS: log utility, w0 = (100,10,10,2) ===")
def ugain(gm):
    return np.log(w0 + gm) - np.log(w0)

def nash_utility(pie, iters=200000):
    # maximise sum log(ugain) s.t. sum g = pie, by projected gradient / Lagrange via bisection on multiplier
    # derivative of log(log(1+g/w0)) wrt g = 1/((w0+g) log(1+g/w0)); decreasing in g. Solve for each j: deriv = lam.
    def g_of_lam(lam):
        out = []
        for w in w0:
            lo, hi = 1e-9, pie
            for _ in range(200):
                mid = (lo + hi) / 2
                d = 1 / ((w + mid) * math.log(1 + mid / w))
                if d > lam: lo = mid
                else: hi = mid
            out.append((lo + hi) / 2)
        return np.array(out)
    lo, hi = 1e-6, 1e6
    for _ in range(300):
        lam = math.sqrt(lo * hi)
        if g_of_lam(lam).sum() > pie: lo = lam
        else: hi = lam
    return g_of_lam(math.sqrt(lo * hi))

for pie, label in ((6.0, "parametric MDE"), (5.0, "arbitrary MD"), (7.5, "bundled, insulate r3, all four")):
    gstar = nash_utility(pie)
    ug = ugain(gstar)
    geq = np.full(4, pie / 4)
    print(f" {label}: pie {pie}")
    print(f"  utility-Nash money gains (f,r1,r2,r3) = {np.round(gstar,3)}, sum {gstar.sum():.3f}")
    print(f"  utility gains {np.round(ug,4)}, product {np.prod(ug):.3e}, floor(utility) {ug.min():.4f} ({['f','r1','r2','r3'][ug.argmin()]}), floor(money) {gstar.min():.3f} ({['f','r1','r2','r3'][gstar.argmin()]})")
    ug_eq = ugain(geq)
    print(f"  equal-money split {geq[0]:.3f} each: utility gains {np.round(ug_eq,4)}, product {np.prod(ug_eq):.3e}")
    print(f"  residents' share of money: utility-Nash {gstar[1:].sum()/pie:.3f}, equal-money 0.750")
# wealth and k=2 exclusion of resident 3 at MDE
print(" k=2 exclusion of resident 3 at MDE: resident 3 wealth 2 - 4 =", 2 - 4, "(log undefined: ruin)")
print(" k=2 exclusion at arbitrary MD: harm 2 -> wealth 0, utility -inf")

print("\n=== BUNDLING: remediation (insulation halves e_i, public cost 2 each) ===")
for arb in (False, True):
    for hi_ in ((True,) if not arb else (True, False)):
        best_b = None
        for ins in itertools.product([0, 1], repeat=3):
            for x in X:
                S, h = surplus(x, arbitrary=arb, insul=ins, halve_interaction=hi_)
                S -= 2 * sum(ins)
                if best_b is None or S > best_b[0]:
                    best_b = (S, name(x), ins, h, p @ x)
        S, nm, ins, h, prof = best_b
        gg = nash_money(S)
        tag = "" if not arb else (" (interaction halved too)" if hi_ else " (interaction not halved)")
        print(f" arbitrary={arb}{tag}: best schedule {nm}, insulate {ins}, profit {prof}, harms {h}, cost {2*sum(ins)}, pie {S:.2f}; Nash {gg:.4f} each, product {gg**4:.4f}")
# separate decision: resident i alone, paying the 2, at the unbundled efficient schedule
for arb, xs in ((False, x_mde), (True, np.array([1, 1, 0, 0.0]))):
    h0 = harms(xs, arbitrary=arb)
    for i in range(3):
        ins = [0, 0, 0]; ins[i] = 1
        h1 = harms(xs, arbitrary=arb, insul=tuple(ins))
        print(f" arbitrary={arb} schedule {name(xs)}: resident {i+1} alone saves {h0[i]-h1[i]:.2f} against cost 2 -> {'insulates' if h0[i]-h1[i] > 2 else 'does not (or indifferent)'}")

print("\n=== OUTSIDE OPTION (comparison only): reroute at 3 per slot ===")
best_o = None
for road in X:
    for rer in X:
        if (road * rer).any():
            continue
        prof = p @ road + (p - 3) @ rer
        h = s * (e @ road)
        tot = prof - h.sum()
        if best_o is None or tot > best_o[0]:
            best_o = (tot, name(road), name(rer), prof, h)
dis = (p - 3).sum()
print(f" disagreement: fleet reroutes all, {dis}; best joint: road {best_o[1]} reroute {best_o[2]} profit {best_o[3]} harms {best_o[4]} total {best_o[0]}; pie over disagreement {best_o[0]-dis:.2f}; Nash {(best_o[0]-dis)/4:.4f} each, product {((best_o[0]-dis)/4)**4:.5f}")

print("\n=== SCALE: party count with the pie held fixed (each resident split into m principals, e_i/m) ===")
for m in (1, 2, 3, 10):
    n = 3 * m + 1
    gg = 6 / n
    print(f" m={m}: {n} parties, Nash {gg:.3f} each, fleet share {gg/6:.3f}, residents' share {1-gg/6:.3f}, a resident who splits into m takes {m*gg:.3f}")
print(" replicated residents (harm scales, profit does not):")
for m in (1, 2, 3):
    sl = p - m * (s @ e)
    print(f"  m={m}: per-slot surplus {sl}, pie {sl[sl>0].sum():.2f}")

print("\n=== FINITE BUDGETS: Monte Carlo, parametric prefs, k=3, Nash split on the proposer's estimates ===")
rng = np.random.default_rng(20261021)
N = 200000
E_mat = np.array([e @ x for x in X])  # 16 x 3 exposure sums
P_vec = np.array([p @ x for x in X])
true_h = np.array([s * (e @ x) for x in X])  # 16 x 3

def run_fleet_proposes(sig_f):
    eps = rng.normal(0, sig_f, (N, 3))
    s_hat = s + eps
    h_hat = s_hat[:, None, :] * E_mat[None, :, :]  # N x 16 x 3
    pie_hat = P_vec[None, :] - h_hat.sum(2)
    j = pie_hat.argmax(1)
    pie_j = pie_hat[np.arange(N), j]
    deal_possible = pie_j > 0
    hh = h_hat[np.arange(N), j]  # N x 3
    t = hh + pie_j[:, None] / 4
    th = true_h[j]
    accept = (t >= th).all(1) & deal_possible
    gf = np.where(accept, P_vec[j] - t.sum(1), 0)
    gr = np.where(accept[:, None], t - th, 0)
    return summarise(accept, j, gf, gr)

def run_residents_propose(sig_n):
    eta = rng.normal(0, sig_n, (N, 4))
    p_hat = p + eta
    pie_hat = p_hat @ np.array(X).T - true_h.sum(1)[None, :]
    j = pie_hat.argmax(1)
    pie_j = pie_hat[np.arange(N), j]
    deal_possible = pie_j > 0
    th = true_h[j]
    t = th + pie_j[:, None] / 4
    gf_raw = P_vec[j] - t.sum(1)
    accept = (gf_raw >= 0) & deal_possible
    gf = np.where(accept, gf_raw, 0)
    gr = np.where(accept[:, None], t - th, 0)
    return summarise(accept, j, gf, gr)

def summarise(accept, j, gf, gr):
    eff = (j == [name(x) for x in X].index("MDE")) & accept
    Eg = np.array([gf.mean(), *gr.mean(0)])
    pie_real = (gf + gr.sum(1))
    return dict(deal=accept.mean(), efficient=eff.mean(), Epie=pie_real.mean(), Eg=np.round(Eg, 3),
                product=product(Eg), floor=Eg.min(), res_share=(gr.sum(1).mean() / max(pie_real.mean(), 1e-9)),
                Eprod_realised=np.mean(np.where(accept, np.prod(np.column_stack([gf, gr]).clip(min=0), 1), 0)))

for sf in (1.0, 0.3, 0.1, 0.03):
    r = run_fleet_proposes(sf)
    print(f" fleet proposes, fleet error {sf}: deal {r['deal']:.3f} efficient {r['efficient']:.3f} E[pie] {r['Epie']:.3f} E[gains] {r['Eg']} product {r['product']:.4f} floor {r['floor']:.3f} residents' share {r['res_share']:.3f}")
for sn in (1.0, 0.3, 0.1, 0.03):
    r = run_residents_propose(sn)
    print(f" residents propose, residents' error {sn}: deal {r['deal']:.3f} efficient {r['efficient']:.3f} E[pie] {r['Epie']:.3f} E[gains] {r['Eg']} product {r['product']:.4f} floor {r['floor']:.3f} residents' share {r['res_share']:.3f}")
print(" limit (either side, transparent): deal 1, efficient 1, pie 6, gains 1.5 each, product 5.0625, floor 1.5, residents' share 0.75")
print(" ratio reading: 10:1 fleet-favoured at level 1 = fleet 0.316 vs residents 1; at level 0.3 = 0.1 vs 0.3; at level 0.1 = 0.03 vs 0.1 (mirror for 1:10)")

print("\n=== FINITE BUDGETS with exchange of estimates (each side reveals; checked against the other's estimate) ===")
# resident i reports s_i' ; fleet accepts a report if |s_i' - s_hat_i| <= 2 sig_f. Residents report truthfully (Krier's court) or overstate to the tolerance.
for sf in (1.0, 0.3, 0.1):
    for overstate in (0.0, 2.0):
        eps = rng.normal(0, sf, (N, 3))
        s_rep = s + overstate * sf  # overstated by the tolerance
        s_hat = s + eps
        ok = (np.abs(s_rep - s_hat) <= 2 * sf).all(1)
        # if accepted, contract on reported s: schedule argmax of reported pie, transfers reported harm + pie/4
        h_rep = np.array([s_rep * (e @ x) for x in X])
        pie_rep = P_vec - h_rep.sum(1)
        j = pie_rep.argmax(); x = X[j]
        t = h_rep[j] + pie_rep[j] / 4
        th = true_h[j]
        gf = P_vec[j] - t.sum(); gr = t - th
        Eg = np.array([gf, *gr]) * ok.mean()
        print(f" fleet error {sf}, residents overstate by {overstate}sigma_f: accepted {ok.mean():.3f}, schedule {name(x)}, E[gains] {np.round(Eg,3)}, product {product(Eg):.4f}, floor {Eg.min():.3f}")
