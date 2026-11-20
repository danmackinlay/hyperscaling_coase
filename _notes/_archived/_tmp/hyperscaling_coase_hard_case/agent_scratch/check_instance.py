import itertools, numpy as np
p = np.array([4,5.5,4,5.0]); E = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s=np.array([1,1,2.0])
names="MDEN"
def harms(x, arb=False):
    h = s*(E@x)
    if arb and x[0]==1 and x[2]==1: h[2]+=1.5
    return h
for arb in (False, True):
    print("arbitrary" if arb else "parametric")
    rows=[]
    for x in itertools.product([0,1],repeat=4):
        x=np.array(x); h=harms(x,arb); pie=p@x-h.sum()
        rows.append((pie, "".join(n for n,b in zip(names,x) if b) or "-", p@x, tuple(h)))
    for r in sorted(rows, reverse=True)[:5]: print("  ", r)
