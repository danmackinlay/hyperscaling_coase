import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm
from base import *
rng=np.random.default_rng(0)
X=[np.array(x) for x in S if sum(x)>0]
E=[e@x for x in X]          # exposure sums per resident
def fleet_offer(shat,sig,arb_blind=True):
    """fleet with flat posterior s_i~N(shat_i,sig^2); chooses x and margins m_i (in sd units)."""
    best=(0,None,None)
    for x,Ei in zip(X,E):
        A=p@x-Ei@shat
        act=Ei>0
        def f(m):
            mm=np.zeros(3); mm[act]=m
            return -(A-sig*(Ei*mm).sum())*np.prod(norm.cdf(mm[act]))
        k=act.sum()
        r=minimize(f,np.zeros(k),method='Nelder-Mead',options={'xatol':1e-4,'fatol':1e-7})
        if -r.fun>best[0]:
            mm=np.zeros(3); mm[act]=r.x; best=(-r.fun,x,mm)
    return best
def run_fleet(sig,n=1500,arb=False):
    out=[]
    for _ in range(n):
        z=rng.standard_normal(3); shat=s+sig*z
        val,x,m=fleet_offer(shat,sig)
        if x is None: out.append((0,0,0,0,0)); continue
        t=(e@x)*(shat+sig*m)
        h=harms(tuple(x),arb)
        if np.all(t>=h-1e-12):
            out.append((p@x-t.sum(),*(t-h),1))
        else: out.append((0,0,0,0,0))
    return np.array(out)
def summ(a,tag):
    g=a[:,:4].mean(0); dr=a[:,4].mean()
    npd=np.prod(g) if np.all(g>=0) else float('nan')
    print(f'{tag}: deal {dr:.3f} E gains (F;1,2,3)=({g[0]:.2f};{g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) pie {g.sum():.2f} resShare {g[1:].sum()/max(g.sum(),1e-9):.2f} NP {npd:.3f} floor {g.min():.3f}')
    return g
if __name__=='__main__':
    import sys
    arb = len(sys.argv)>1
    for sig in (1.0,0.316,0.1,0.0316,0.01):
        summ(run_fleet(sig,n=600 if sig>0.05 else 300,arb=arb),f'fleet TIOLI sig_f={sig} arb={arb}')
