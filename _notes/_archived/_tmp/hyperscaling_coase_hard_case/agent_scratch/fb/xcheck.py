# independent check of the fleet TIOLI optimiser: Nelder-Mead on log objective vs coordinate grid ascent
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm
from inst import PROFIT, EX, S, NAMES
from tioli import fleet_offer, accept_prob
rng=np.random.default_rng(5)
for sf in (1.0,0.3,0.1):
    n=40; shat=S+sf*rng.standard_normal((n,3))
    mu=EX[None]*shat[:,None,:]; tau=np.broadcast_to(EX[None]*sf,mu.shape).copy()
    t,ep=fleet_offer(mu,tau,PROFIT); ep[:,0]=0
    diffs=[]
    for a in range(n):
        best=0
        for j in range(1,16):
            act=[i for i in range(3) if tau[a,j,i]>0]
            def f(z):
                tt=np.zeros(3)
                for k,i in enumerate(act): tt[i]=max(mu[a,j,i]+tau[a,j,i]*z[k],0)
                acc=np.prod([accept_prob(tt[i],mu[a,j,i],tau[a,j,i]) for i in act])
                return -acc*(PROFIT[j]-tt.sum())
            r=min((minimize(f,np.full(len(act),z0),method="Nelder-Mead",options=dict(xatol=1e-6,fatol=1e-9)) for z0 in (0.5,1.5,2.5)),key=lambda r:r.fun)
            best=max(best,-r.fun)
        diffs.append(best-ep[a].max())
    print(f"sf {sf}: NM minus grid, max {max(diffs):.4f} mean {np.mean(diffs):.5f}")
