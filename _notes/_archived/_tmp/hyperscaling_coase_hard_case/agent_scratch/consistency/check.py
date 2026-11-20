import itertools, math
import numpy as np
from scipy.optimize import minimize
p=np.array([4,5.5,4,5.]); e=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
S=list(itertools.product([0,1],repeat=4))
def harms(x,s=s,arb=False):
    h=(s[:,None]*e*np.array(x)).sum(1)
    if arb and x[0] and x[2]: h=h.copy(); h[2]+=1.5
    return h
nm=lambda x:''.join(c for c,b in zip('MDEN',x) if b)
for arb in (0,1):
    best=sorted(((p@np.array(x)-harms(x,arb=arb).sum(),nm(x)) for x in S),reverse=True)[:4]; print('arb',arb,best)
# k=2 coalition values
for pair in [(0,1),(0,2),(1,2)]:
    v=sum(max(0,p[t]-sum(s[i]*e[i,t] for i in pair)) for t in range(4)); print('fleet+',pair,v)
# outside option
oo=[max(p[t]-3,0) for t in range(4)]; print('threat',sum(oo),'best',sum(max(p[t]-3,p[t]-(s*e[:,t]).sum()) for t in range(4)))
# shading by resident 3 under additive model, arbitrary truth, Nash equal split on modelled pie
best=None
for sp in np.linspace(2,6,401):
    sv=s.copy(); sv[2]=sp
    vals=[(p@np.array(x)-harms(x,sv).sum(),x) for x in S]; mp,x=max(vals)
    if mp<=0: continue
    hm=harms(x,sv); ht=harms(x,arb=True); g=mp/4
    gains=[g,g,g,g+hm[2]-ht[2]]
    if best is None or gains[3]>best[0]: best=(gains[3],sp,nm(x),gains,np.prod(gains))
    if abs(sp-3.01)<1e-9 or abs(sp-4.99)<1e-9: print(sp,nm(x),np.round(gains,3),round(np.prod(gains),3))
print('r3 best response',best)
# KRS: Nash in utility units, MDE money harms, residents' right
w0=np.array([100,10,10,2.])
def neg(g):
    g=np.append(6-g.sum(),g)
    if (g<=0).any(): return 1e9
    return -np.sum(np.log(np.log(1+g/w0)))
r=minimize(neg,[1.5]*3,method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-12,'maxiter':20000})
g=np.append(6-r.x.sum(),r.x); print('KRS gains',np.round(g,3))
