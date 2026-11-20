import itertools, math
from fractions import Fraction as F

slots = "MDEN"
p = [F(4), F(11,2), F(4), F(5)]
e = {1:[F(1,2),F(0),F(1,2),F(1)], 2:[F(1),F(1),F(1,2),F(1,2)], 3:[F(1,2),F(1,2),F(1),F(2)]}
s = {1:F(1),2:F(1),3:F(2)}

def harm(i,x,arb=False):
    h = s[i]*sum(e[i][t]*x[t] for t in range(4))
    if arb and i==3 and x[0] and x[2]: h += F(3,2)
    return h
def profit(x): return sum(p[t]*x[t] for t in range(4))
def name(x): return "".join(slots[t] for t in range(4) if x[t]) or "none"
X = list(itertools.product([0,1],repeat=4))

print("== 16 schedules (parametric): profit, harms, pie")
for x in X:
    hs=[harm(i,x) for i in (1,2,3)]
    print(f"{name(x):5} profit={float(profit(x)):5} harms={[float(h) for h in hs]} pie={float(profit(x)-sum(hs))}")
best = max(X,key=lambda x: profit(x)-sum(harm(i,x) for i in (1,2,3)))
print("efficient:",name(best), float(profit(best)-sum(harm(i,best) for i in (1,2,3))))
besta = max(X,key=lambda x: profit(x)-sum(harm(i,x,True) for i in (1,2,3)))
print("efficient (arbitrary):",name(besta), float(profit(besta)-sum(harm(i,besta,True) for i in (1,2,3))))

# coalition worths: fleet + subset S of residents, k consents needed
def v(S,k,arb=False):
    if len(S)<k: return F(0)
    return max(profit(x)-sum(harm(i,x,arb) for i in S) for x in X)
for arb in (False,True):
    print(f"\n== coalition worths, arb={arb}")
    for S in [(1,2),(1,3),(2,3),(1,2,3)]:
        xs = max(X,key=lambda x: profit(x)-sum(harm(i,x,arb) for i in S))
        print(f"  fleet+{S}: {float(v(S,3 if len(S)==3 else 2,arb))} via {name(xs)}; excluded harms under it:",
              {j: float(harm(j,xs,arb)) for j in (1,2,3) if j not in S})

# k=2 core, no enforcer, transparent: allocations summing to pie(6) s.t. every winning coalition S gets >= v(S),
# residents individually >= -harm under the all-four schedule (they cannot stop it alone at k=2)
print("\n== k=2 core (parametric), grid search in steps of 1/4")
allx=(1,1,1,1)
guar={i:-harm(i,allx) for i in (1,2,3)}
pie=F(6); core=[]
rng=lambda lo,hi:[lo+F(j,4) for j in range(int((hi-lo)*4)+1)]
for r1 in rng(guar[1],pie):
  for r2 in rng(guar[2],pie):
    for r3 in rng(guar[3],pie):
      f=pie-r1-r2-r3
      if f<0: continue
      ok = (f+r1+r2>=v((1,2),2)) and (f+r1+r3>=v((1,3),2)) and (f+r2+r3>=v((2,3),2))
      if ok: core.append((float(f),float(r1),float(r2),float(r3)))
print("core points:",len(core)); print("fleet range",min(c[0] for c in core),max(c[0] for c in core))
for i,nm in ((1,"r1"),(2,"r2"),(3,"r3")): print(nm,"range",min(c[i] for c in core),max(c[i] for c in core))
print("floor (worst resident) range:",min(min(c[1:]) for c in core),max(min(c[1:]) for c in core))

# k=3 core
print("\n== k=3 core: residents guaranteed 0 (veto), fleet 0; any split of 6 with all >=0 is in it (winning coalitions = grand only)")

# Pact self-enforcement at k=2 against the fleet's best side offer.
hall={i:harm(i,allx) for i in (1,2,3)}  # (2,3,8)
pacts={"egalitarian 1.5 each (fleet 1.5)":{1:F(3,2),2:F(3,2),3:F(3,2)},
       "bloc takes all, 2 each (fleet 0)":{1:F(2),2:F(2),3:F(2)},
       "bloc takes all, proportional to MDE harm (fleet 0)":{1:F(6)*F(1)/F(15,2),2:F(6)*F(5,2)/F(15,2),3:F(6)*F(4)/F(15,2)},
       "harm-only, fleet takes all 6":{1:F(0),2:F(0),3:F(0)}}
print("\n== k=2 pacts vs the fleet's side offer (grim trigger: after a break, consents compete to 0, fleet runs all four)")
for nm,a in pacts.items():
    G=sum(a.values()); fp=F(6)-G
    # cheapest two to bribe: per-period loss a_i + hall_i
    losses=sorted(((a[i]+hall[i],i) for i in (1,2,3)))
    two=losses[:2]; per_period_bribe=sum(l for l,_ in two)
    fleet_gain_pp = F(37,2)-fp   # 18.5 - fleet's pact payoff
    print(f"\n {nm}: G={float(G)}, fleet pact payoff={float(fp)}; cheapest pair={[i for _,i in two]}, per-period bribe={float(per_period_bribe)}, fleet per-period gain from collapse={float(fleet_gain_pp)}")
    print(f"   long-run fleet (bribe and gain both scale 1/(1-d)): margin per period = {float(fleet_gain_pp-per_period_bribe)}  -> pact broken at every delta" if fleet_gain_pp>per_period_bribe else "   pact holds")
    for d in (F(1,2),F(4,5),F(19,20)):
        need=per_period_bribe/(1-d)
        print(f"   delta={float(d)}: lump-sum bribe needed={float(need):8.2f}; long-run fleet windfall={float(fleet_gain_pp/(1-d)):8.2f} -> {'BROKEN' if fleet_gain_pp/(1-d)>=need else 'holds'}; short-run fleet (one period's profit, {float(fleet_gain_pp)}) -> {'BROKEN' if fleet_gain_pp>=need else 'holds'}")
    thr = 1-per_period_bribe/fleet_gain_pp
    print(f"   short-run-fleet threshold delta > {float(thr):.3f}")

# Nash products
def nash(gains):
    if any(g<=0 for g in gains): return "0 or undefined (floor %.3g)"%min(gains)
    return "%.3f"%math.prod(gains)
print("\n== Nash products / floors")
for lab,vec in [("k=3 equal split, full menu",(1.5,1.5,1.5,1.5)),("k=2 core (midpoint)",(18.25,-1.75,-2.75,-7.75)),
                ("k=2 consents compete, all four",(18.5,-2,-3,-8)),("k=2 broken egalitarian pact, bribed each period",(10.5,1.5,1.5,-8))]:
    print(f" {lab}: {vec} -> {nash(vec)}")

# Clause menus
print("\n== clause menus: max pie available")
menus={"four slots":X,
       "two: day=MD | night=EN":[(a,a,b,b) for a in (0,1) for b in (0,1)],
       "two: day=MDE | night=N":[(a,a,a,b) for a in (0,1) for b in (0,1)],
       "one: all or nothing":[(0,0,0,0),(1,1,1,1)]}
for arb in (False,True):
    for nm,M in menus.items():
        bx=max(M,key=lambda x: profit(x)-sum(harm(i,x,arb) for i in (1,2,3)))
        pie_=profit(bx)-sum(harm(i,bx,arb) for i in (1,2,3))
        print(f" arb={arb} {nm:26}: pie={float(pie_):4} via {name(bx)}; equal split product={(float(pie_)/4)**4:.3f}")

# Platform: WTP for enforcement at k=2 vs no-enforcer outcomes
print("\n== willingness to pay a platform per period, k=2, egalitarian pact enforced vs unenforced")
for lab,base in [("vs consents-compete (18.5;-2,-3,-8)",(F(37,2),F(-2),F(-3),F(-8))),("vs core midpoint (18.25;-1.75,-2.75,-7.75)",(F(73,4),F(-7,4),F(-11,4),F(-31,4)))]:
    pact=(F(3,2),)*4
    print(f" {lab}: fleet WTP against enforcement={float(base[0]-pact[0])}; residents WTP for={[float(pact[i]-base[i]) for i in (1,2,3)]}, total={float(sum(pact[i]-base[i] for i in (1,2,3)))}")
print(" wealth check (log utility, w0=(10,10,2) residents, 100 fleet): resident 3 at -8 has w0+payoff = -6 -> ruin, utility undefined; at -7.5 likewise")
print(" r3's maximum feasible payment to a platform in a period = endowment 2 + pact share 1.5 = 3.5, against a money WTP of 9.5")
