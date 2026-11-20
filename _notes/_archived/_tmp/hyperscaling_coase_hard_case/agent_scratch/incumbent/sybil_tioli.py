import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm
from base import p,S
rng=np.random.default_rng(2)
def make(sybil):
    if not sybil: return np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]),np.array([1,1,2.]),[0,1,2]
    e2=np.array([1,1,0.5,0.5])/3
    return np.array([[0.5,0,0.5,1],e2,e2,e2,[0.5,0.5,1,2]]),np.array([1,1,1,1,2.]),[0,1,1,1,2]
X=[np.array(x) for x in S if sum(x)>0]
def run(sig,sybil,n=300):
    e,s,owner=make(sybil); out=[]
    for _ in range(n):
        shat=s+sig*rng.standard_normal(len(s)); best=(0,None,None)
        for x in X:
            Ei=e@x; act=Ei>0; A=p@x-Ei@shat
            f=lambda m:-(A-sig*(Ei[act]*m).sum())*np.prod(norm.cdf(m))
            r=minimize(f,np.zeros(act.sum()),method='Nelder-Mead',options={'maxiter':4000})
            if -r.fun>best[0]:
                mm=np.zeros(len(s)); mm[act]=r.x; best=(-r.fun,x,mm)
        v,x,m=best
        g=np.zeros(4)
        if x is not None:
            Ei=e@x; t=Ei*(shat+sig*m); h=Ei*s
            if np.all(t>=h-1e-12):
                g[0]=p@x-t.sum()
                for k,o in enumerate(owner): g[1+o]+=t[k]-h[k]
        out.append(g)
    g=np.mean(out,0); return g
for sig in (1.0,0.316,0.1):
    for sy in (False,True):
        g=run(sig,sy)
        print(f'sig={sig} sybil={sy}: (F;1,2,3)=({g[0]:.2f};{g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) NP {np.prod(g):.3f}')
