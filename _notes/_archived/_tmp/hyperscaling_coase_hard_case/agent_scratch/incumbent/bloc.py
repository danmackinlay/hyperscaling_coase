import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import norm
from base import *
from tioli import X, summ
rng=np.random.default_rng(1)
H=[R@x for x in X]
def bloc_offer(phat,sig):
    best=(0,None,None)
    for x,h in zip(X,H):
        mu=phat@x; sd=sig*np.sqrt(x.sum()); Ht=h.sum()
        f=lambda T: -(T-Ht)*norm.cdf((mu-T)/sd)
        r=minimize_scalar(f,bounds=(Ht,mu+5*sd+1),method='bounded')
        if -r.fun>best[0]: best=(-r.fun,x,r.x)
    return best
def run_bloc(sig,n=1500,split='equal'):
    out=[]
    for _ in range(n):
        phat=p+sig*rng.standard_normal(4)
        v,x,T=bloc_offer(phat,sig)
        if x is None or T>p@x: out.append((0,0,0,0,0)); continue
        h=R@x; G=T-h.sum()
        if split=='equal': g=np.full(3,G/3)
        else: g=G*h/h.sum()
        out.append((p@x-T,*g,1))
    return np.array(out)
if __name__=='__main__':
    for sp in ('equal','prop'):
        for sig in (1.0,0.316,0.1,0.0316,0.01):
            summ(run_bloc(sig,800,sp),f'bloc TIOLI sig_N={sig} split={sp}')
