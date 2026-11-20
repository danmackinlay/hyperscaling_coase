import numpy as np, collections
from council import *
for sN in [0.05,0.1,0.2,0.3,0.5,1,2]:
    rng=np.random.default_rng(3); ch=collections.Counter(); co=[];dd=[]
    for _ in range(3000):
        ph = p + sN*rng.standard_normal(4)
        best=(-np.inf,None,None)
        for xi in range(1,16):
            m = X[xi]@ph - H[xi].sum(); sd=sN*np.sqrt(X[xi].sum())
            ev = DGRID*norm.sf((DGRID-m)/sd); j=ev.argmax()
            if ev[j]>best[0]: best=(ev[j],xi,DGRID[j])
        _,xi,d=best; ch[tuple(X[xi].astype(int))]+=1
        ok=PIE[xi]>=d; co.append((PIE[xi]-d)*ok); dd.append(d*ok)
    print(sN, dict(ch.most_common(3)), 'company per res-proposal %.3f proposer %.3f'%(np.mean(co),np.mean(dd)))
