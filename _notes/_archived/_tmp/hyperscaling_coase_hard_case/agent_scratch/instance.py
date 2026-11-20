import itertools, math
import numpy as np

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]])
s = np.array([1,1,2.0])
names = "MDEN"

def harms(x, arbitrary=False):
    h = s * (E @ x)
    if arbitrary and x[0]==1 and x[2]==1:
        h = h.copy(); h[2] += 1.5
    return h

def lab(x): return "".join(n for n,b in zip(names,x) if b) or "none"

print("== 16 schedules (parametric | arbitrary) ==")
rows=[]
for bits in itertools.product([0,1],repeat=4):
    x=np.array(bits)
    prof=p@x; h=harms(x); ha=harms(x,True)
    rows.append((lab(x),prof,h,prof-h.sum(),ha,prof-ha.sum()))
for r in sorted(rows,key=lambda r:-r[3]):
    print(f"{r[0]:5s} profit {r[1]:5.1f} harms {np.round(r[2],2)} pie {r[3]:5.2f} | arb harms {np.round(r[4],2)} pie {r[5]:5.2f}")

print("\n== clause languages: best pie under each menu ==")
menus = {
 "four slots": [np.array(b) for b in itertools.product([0,1],repeat=4)],
 "two: day={M,D}, night={E,N}": [np.array([a,a,b,b]) for a in (0,1) for b in (0,1)],
 "two: day={M,D,E}, night={N}": [np.array([a,a,a,b]) for a in (0,1) for b in (0,1)],
 "one: all or nothing": [np.zeros(4,int), np.ones(4,int)],
}
for nm,ms in menus.items():
    for arb in (False,True):
        best=max(ms,key=lambda x: p@x-harms(x,arb).sum())
        pie=p@best-harms(best,arb).sum()
        print(f"{nm:32s} {'arb' if arb else 'par'}: {lab(best):5s} pie {pie:4.2f} equal split {pie/4:5.3f} each, Nash product {(pie/4)**4:5.3f}")

print("\n== k=2 coalition values (fleet + two residents), parametric ==")
X=[np.array(b) for b in itertools.product([0,1],repeat=4)]
for pair in [(0,1),(0,2),(1,2)]:
    best=max(X,key=lambda x: p@x-harms(x)[list(pair)].sum())
    v=p@best-harms(best)[list(pair)].sum()
    print(f"F+{pair}: schedule {lab(best)} value {v:.2f}")
grand=max(X,key=lambda x:p@x-harms(x).sum()); vg=p@grand-harms(grand).sum()
print(f"grand coalition: {lab(grand)} value {vg:.2f}")
# core test: sum of three pair-coalition constraints: 2*(total) + u_F >= sum v
vs=[13.5,8.5,7.5]
print(f"core: 2*{vg}+u_F >= {sum(vs)} -> u_F >= {sum(vs)-2*vg:.1f} > {vg}: core empty, deficit {sum(vs)-2*vg-vg:.1f}")
# one-shot divide and conquer at k=2: fleet buys two cheapest consents at tokens, runs the schedule maximising profit
allfour=np.ones(4,int)
print(f"divide and conquer k=2, tokens: fleet {p@allfour:.1f}, residents {-harms(allfour)}, pie {p@allfour-harms(allfour).sum():.1f}, floor {-harms(allfour).max():.0f}")
