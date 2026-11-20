import itertools, math, random
import numpy as np
from regress import S,prof,harm,name,E,s
D=[0.5,0.8,0.95]
# 1. outside instrument (GMW-style rents r_i lost by a deviator) needed at k=2
vF={(0,1):13.5,(0,2):8.5,(1,2):7.5}; vFa={(0,1):13.5,(0,2):7.0,(1,2):6.0}
def min_r(pact,vf,d):
    F,*v=pact; best=None
    # brute force r on grid
    g=np.arange(0,40.01,0.05)
    need={pr:max(0,vf[pr]-F-v[pr[0]]-v[pr[1]])/d for pr in vf}
    # minimise r1+r2+r3 s.t. r_i+r_j>=need_ij : LP vertex enumeration
    import itertools
    cands=[]
    for r3 in g:
        r1=max(need[(0,2)]-r3,0); r2=max(need[(1,2)]-r3,0)
        if r1+r2<need[(0,1)]:
            extra=need[(0,1)]-r1-r2; r1+=extra
        cands.append((r1+r2+r3,(round(r1,2),round(r2,2),round(r3,2))))
    return min(cands)
for d in D:
    print('d',d,'equal split param: min sum r',min_r((1.5,)*4,vF,d),
          '| fleet-takes-all pact (6;0,0,0):',min_r((6,0,0,0),vF,d)[0],
          '| arbitrary equal split',min_r((1.25,)*4,vFa,d)[0])
# 2. Nash-product max under wealth effects (k=3 pact, pie 6)
w0=[100,10,10,2]
best=None
for a in np.arange(0.01,6,0.01):
  for b in np.arange(0.01,6-a,0.05):
    for c in np.arange(0.01,6-a-b,0.05):
      dd=6-a-b-c
      if dd<=1e-6: continue
      g=[a,b,c,dd]; val=sum(math.log(math.log(1+gi/wi)) for gi,wi in zip(g,w0))
      if best is None or val>best[0]: best=(val,[round(x,2) for x in g])
print('wealth effects: Nash-max money split (F,r1,r2,r3)',best[1])
print('k=2 stage under wealth: resident 3 wealth',2-8,'-> log undefined (ruin); r1,r2 wealth',10-2,10-3)
# 3. finite budgets: fleet estimates s_i with sd sig; bribes pair (1,2) to defect from equal-split pact
random.seed(1); rng=np.random.default_rng(1)
ALL=(1,1,1,1)
def req(i,si,d,v=1.5):  # minimal bribe for resident i, x=MDEN, robust reversion
    H=si*sum(E[i]); return H+(v+d*H)/(1-d)
for sig in (1.0,0.3,0.1):
  for d in D:
    gainPV=prof(ALL)+d*prof(ALL)/(1-d)-1.5/(1-d)
    best=(-1e9,None)
    for z in np.arange(0,4.01,0.25):
      n=20000; e1=rng.normal(0,sig,n); e2=rng.normal(0,sig,n)
      # bid = required at estimate + z*sd of that estimate's effect
      k1=sum(E[0])*(1+d/(1-d)); k2=sum(E[1])*(1+d/(1-d))
      b1=req(0,1+e1,d)+z*sig*k1; b2=req(1,1+e2,d)+z*sig*k2
      acc=(b1>=req(0,1,d))&(b2>=req(1,1,d))
      eg=np.mean(acc*(gainPV-b1-b2))
      if eg>best[0]: best=(eg,z,acc.mean())
    p=best[2]; print(f'sig={sig} d={d}: best margin z={best[1]}, P(break per attempt)={p:.3f}, expected periods pact survives={(1-p)/p:.2f}')
