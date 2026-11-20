import itertools, numpy as np
p = np.array([4,5.5,4,5.0]); slots="MDEN"
e = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s=np.array([1,1,2.0])
w0 = np.array([10,10,2.0]); wf=100.0
def harm(x, arb=False, ins=()):
    ee = e.copy()
    for i in ins: ee[i]=ee[i]/2
    h = s*(ee@x)
    if arb and x[0] and x[2]: h[2]+=1.5
    return h
def name(x): return "".join(c for c,b in zip(slots,x) if b) or "none"
print("16 schedules, baseline / arbitrary / remediation(ins 3) / outside option (fleet threat 6.5)")
rows=[]
for x in itertools.product([0,1],repeat=4):
    x=np.array(x); P=p@x
    hb=harm(x); ha=harm(x,arb=True); hr=harm(x,ins=(2,))
    oo = P + sum((p[t]-3) for t in range(4) if not x[t]) - 6.5 - hb.sum()  # pie over threat point
    rows.append((name(x),P,hb,P-hb.sum(),ha,P-ha.sum(),hr,P-hr.sum()-2,oo))
    print(f"{name(x):5s} P={P:5.1f} h={hb} pie={P-hb.sum():5.2f} | arb h3={ha[2]:4.1f} pie={P-ha.sum():5.2f} | ins3 h={hr} pie={P-hr.sum()-2:5.2f} | outside pie={oo:5.2f}")
for lab,i in [("baseline",3),("arbitrary",5),("ins3",7),("outside",8)]:
    best=max(rows,key=lambda r:r[i]); print(lab,"efficient:",best[0],round(best[i],3))
# remediation full search
best=None
for x in itertools.product([0,1],repeat=4):
    x=np.array(x)
    for I in itertools.chain.from_iterable(itertools.combinations(range(3),r) for r in range(4)):
        v=p@x-harm(x,ins=I).sum()-2*len(I)
        if best is None or v>best[0]: best=(v,name(x),I,harm(x,ins=I))
print("remediation efficient:",best)
# wealth-effects Nash maximiser on pie 6 and 5 and 7.5
from scipy.optimize import minimize
def ug(g,w): return np.log(w+g)-np.log(w)
def nash_wealth(pie, weights=(1,1,1,1)):
    W=np.array([wf,*w0]); wts=np.array(weights,float)
    def obj(g3):
        g=np.append(g3, pie-g3.sum())
        if np.any(g<=0): return 1e9
        return -(wts*np.log(ug(g,W))).sum()
    r=minimize(obj,np.full(3,pie/4),method="Nelder-Mead",options=dict(xatol=1e-9,fatol=1e-12,maxiter=20000))
    g=np.append(r.x,pie-r.x.sum()); return g, ug(g,W)
for pie in (6,5,7.5,1.5):
    g,u=nash_wealth(pie); print(f"pie {pie}: Nash-in-utility money split (f;r1,r2,r3)={np.round(g,3)} utils={np.round(u,4)} product={np.prod(u):.3e}; linear equal split utils={np.round(ug(np.full(4,pie/4),np.array([wf,*w0])),4)} product={np.prod(ug(np.full(4,pie/4),np.array([wf,*w0]))):.3e}")
