import itertools, math
from scipy.optimize import minimize

slots = "MDEN"
p = [4, 5.5, 4, 5]
e = {1:[0.5,0,0.5,1], 2:[1,1,0.5,0.5], 3:[0.5,0.5,1,2]}
s = {1:1, 2:1, 3:2}

def harms(x, arbitrary=False):
    h = {i: s[i]*sum(e[i][t]*x[t] for t in range(4)) for i in (1,2,3)}
    if arbitrary and x[0] and x[2]:
        h[3] += 1.5
    return h

def profit(x): return sum(p[t]*x[t] for t in range(4))

print("== enumeration of 16 schedules (baseline, additive) ==")
rows=[]
for x in itertools.product([0,1], repeat=4):
    h = harms(x); pie = profit(x)-sum(h.values())
    ha = harms(x, True); piea = profit(x)-sum(ha.values())
    rows.append((pie, piea, x, profit(x), h, ha))
    name = "".join(slots[t] for t in range(4) if x[t]) or "none"
    print(f"{name:5s} profit={profit(x):5.1f} harms={tuple(h.values())} pie={pie:5.2f} | arbitrary harms={tuple(ha.values())} pie={piea:5.2f}")
best = max(rows, key=lambda r:r[0]); besta = max(rows, key=lambda r:r[1])
print("efficient additive:", best[2], "pie", best[0]); print("efficient arbitrary:", besta[2], "pie", besta[1])
per_slot_harm = [sum(s[i]*e[i][t] for i in (1,2,3)) for t in range(4)]
print("per-slot total harm", per_slot_harm, "per-slot surplus", [p[t]-per_slot_harm[t] for t in range(4)])

print("\n== wealth effects: Nash product in utility units at the equal money split (MDE, 1.5 each) ==")
w0 = {1:10, 2:10, 3:2}; wf = 100
h = harms((1,1,1,0))
def ugain_res(i, t): return math.log(w0[i]+t-h[i]) - math.log(w0[i])
def ugain_f(T): return math.log(wf+13.5-T) - math.log(wf)
t_eq = {i: h[i]+1.5 for i in (1,2,3)}
g = [ugain_res(i,t_eq[i]) for i in (1,2,3)] + [ugain_f(sum(t_eq.values()))]
print("utility gains (r1,r2,r3,f):", [round(v,4) for v in g], "product", round(math.prod(g),6), "sum log", round(sum(math.log(v) for v in g),4))
# utility-Nash maximiser over money transfers
def negNP(v):
    t = {1:v[0],2:v[1],3:v[2]}
    gs = [ugain_res(i,t[i]) for i in (1,2,3)] + [ugain_f(sum(t.values()))]
    if min(gs) <= 0: return 1e9
    return -sum(math.log(x) for x in gs)
res = minimize(negNP, [h[1]+1.5,h[2]+1.5,h[3]+1.5], method="Nelder-Mead", options={"xatol":1e-9,"fatol":1e-12,"maxiter":20000})
t = res.x; gains_money = [t[i-1]-h[i] for i in (1,2,3)] + [13.5-sum(t)]
print("utility-Nash maximiser, money gains (r1,r2,r3,f):", [round(v,3) for v in gains_money])

print("\n== Case C: residents are also customers; delivery value v withholdable ==")
v = {1:1, 2:1, 3:3}
pie_b = 6 + sum(v.values())
each = pie_b/4
print("bundled pie", pie_b, "equal gain", each)
for i in (1,2,3):
    print(f"resident {i}: money gain over clean river = {each - v[i]:+.2f}  (unbundled: +1.50)")
print("fleet gain", each, "(unbundled 1.50); residents' money share of the 6:", round((3*each - sum(v.values()))/6,3), "vs 0.75")
print("Nash product on the bundled origin", round(each**4,2), "vs 5.06 unbundled")

print("\n== Case D: cross-bargain scoring, a refusing resident loses r in other bargains ==")
r = {1:1,2:1,3:1}
offers = {i: h[i]-r[i] for i in (1,2,3)}   # plus epsilon
print("fleet TIOLI offers (harm - r):", offers, "total", sum(offers.values()), "fleet payoff", 13.5-sum(offers.values()))
print("residents vs clean river:", {i: offers[i]-h[i] for i in (1,2,3)})

print("\n== Case B: two neighbourhoods, fleet needs one (Bertrand between triples) ==")
print("competitive transfer = harms", h, "total", sum(h.values()), "residents' gains 0, fleet 6, product 0, floor 0")

print("\n== Case G: reroute cost 3 = fleet cost c + harm (3-c) to neighbourhood B, not at the table ==")
for c in (3, 1.5, 1):
    tot_true = 0; tot_table = 0; harmB = 0; through=[]
    for tslot in range(4):
        thr = p[tslot]-per_slot_harm[tslot]; rer_table = p[tslot]-c; rer_true = p[tslot]-3
        choice = max([(thr,"through"),(rer_table,"reroute"),(0,"off")], key=lambda z:z[0])
        through.append(choice[1][0])
        tot_table += choice[0]
        tot_true += {"through":thr, "reroute":rer_true, "off":0}[choice[1]]
        harmB += (3-c) if choice[1]=="reroute" else 0
    opt_true = sum(max(p[t]-per_slot_harm[t], p[t]-3, 0) for t in range(4))
    print(f"c={c}: at-table choice per slot {through} apparent surplus {tot_table:.1f} true surplus {tot_true:.1f} (true optimum {opt_true:.1f}) harm exported to B {harmB:.1f}")

print("\n== outside option switch as given (reroute 3, all borne by fleet): pie over the fleet's outside option ==")
out = sum(p)-12
opt = sum(max(p[t]-per_slot_harm[t], p[t]-3, 0) for t in range(4))
print("fleet alone (reroute all four):", out, "joint optimum", opt, "pie over no deal", opt-out, "equal gain", (opt-out)/4, "product", round(((opt-out)/4)**4,4))
