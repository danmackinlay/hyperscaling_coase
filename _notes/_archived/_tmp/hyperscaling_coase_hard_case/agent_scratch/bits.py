import itertools, math, random
slots = "MDEN"
p = [4, 5.5, 4, 5]
e = [[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]
s = [1,1,2]
def h_param(i,x): return s[i]*sum(e[i][t]*x[t] for t in range(4))
def h_arb(i,x):
    v = h_param(i,x)
    if i==2 and x[0] and x[2]: v += 1.5
    return v
def profit(x): return sum(p[t]*x[t] for t in range(4))
def name(x): return "".join(slots[t] for t in range(4) if x[t]) or "none"
X = list(itertools.product([0,1],repeat=4))
print("=== enumeration: pie under parametric and arbitrary ===")
best = {}
for lab,h in (("param",h_param),("arb",h_arb)):
    rows=[]
    for x in X:
        H=[h(i,x) for i in range(3)]
        rows.append((profit(x)-sum(H), name(x), profit(x), H))
    rows.sort(reverse=True)
    best[lab]=rows[0]
    print(lab, "top3:", [(r[1],round(r[0],2)) for r in rows[:3]])
print("param optimum", best["param"]); print("arb optimum", best["arb"])
# per-slot parametric comparison
for t in range(4):
    print("slot",slots[t],"p",p[t],"sum s_i e_it",sum(s[i]*e[i][t] for i in range(3)),"surplus",p[t]-sum(s[i]*e[i][t] for i in range(3)))
print("MDE under arbitrary truth: pie", profit((1,1,1,0))-sum(h_arb(i,(1,1,1,0)) for i in range(3)))
print("MD under arbitrary truth: pie", profit((1,1,0,0))-sum(h_arb(i,(1,1,0,0)) for i in range(3)))

print("\n=== clause menus (platform fixes language), arbitrary truth ===")
menus = {"1 clause (all/none)":[(0,0,0,0),(1,1,1,1)],
         "2 clauses (day=MDE, night=N)":[(0,0,0,0),(1,1,1,0),(0,0,0,1),(1,1,1,1)],
         "4 clauses":X}
for lab,opts in menus.items():
    for truth,h in (("param",h_param),("arb",h_arb)):
        b=max(opts,key=lambda x: profit(x)-sum(h(i,x) for i in range(3)))
        print(lab,truth,"best",name(b),"pie",round(profit(b)-sum(h(i,b) for i in range(3)),2))

print("\n=== Nash product under equal split of the pie (k=3, no deal origin 0) ===")
def nash(g): 
    if min(g)<0: return float('nan')
    return math.prod(g)
for lab,pie,n in (("param truth, param found",6,4),("arb truth, arb found",5,4)):
    g=[pie/4]*4; print(lab,"gains",g,"product",round(nash(g),3),"floor",min(g))
# misfit: arbitrary truth, parametric form: fleet picks MDE, pays parametric harm + 1.5
x=(1,1,1,0); Hp=[h_param(i,x) for i in range(3)]; Ha=[h_arb(i,x) for i in range(3)]
T=[Hp[i]+1.5 for i in range(3)]; gf=profit(x)-sum(T); gr=[T[i]-Ha[i] for i in range(3)]
print("misfit (arb truth, param form, transfers true-param-harm+1.5): transfers",T,"gains",[gf]+gr,"product",nash([gf]+gr),"floor",min([gf]+gr),"pie realised",gf+sum(gr))
# resident 3 steering by exaggerating s3 under the parametric form
print("\n=== resident 3's exaggeration gambit under the parametric form ===")
for s3 in [2,2.5,3,3.01,3.5,4,4.99,5,6]:
    sr=[1,1,s3]
    surplus=[p[t]-sum(sr[i]*e[i][t] for i in range(3)) for t in range(4)]
    x=tuple(int(v>0) for v in surplus)
    Hrep=[sr[i]*sum(e[i][t]*x[t] for t in range(4)) for i in range(3)]
    pie_rep=profit(x)-sum(Hrep)
    T=[Hrep[i]+pie_rep/4 for i in range(3)]
    Ha=[h_arb(i,x) for i in range(3)]
    gains=[profit(x)-sum(T)]+[T[i]-Ha[i] for i in range(3)]
    print("s3 reported",s3,"schedule",name(x),"reported pie",round(pie_rep,2),"true gains",[round(g,3) for g in gains],"product",round(nash(gains),3) if min(gains)>=0 else "undef")

print("\n=== communication counts on the instance ===")
m=4
print("parametric: residents send 1 scalar each =",3,"numbers; certificate: m per-slot harm totals =",m,"; operations: m comparisons =",m)
print("arbitrary: resident 3's table 2^m-1 =",2**m-1,"numbers (+1 each from residents 1,2 if known additive) =",2**m-1+2,"; certificate 2^m-1 personalised prices =",2**m-1,"; brute-force operations 2^m =",2**m)
for mm in (4,8,24,168):
    print(f"m={mm}: parametric per-resident 1, per-slot additive {mm}, pairwise interactions {mm*(mm-1)//2}, arbitrary {2**mm-1:.3g}")
