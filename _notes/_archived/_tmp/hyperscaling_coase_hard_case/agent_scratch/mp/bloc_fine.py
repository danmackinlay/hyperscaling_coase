import itertools, numpy as np
from scipy.stats import norm
from scipy.optimize import minimize
rng=np.random.default_rng(0)
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
X=[np.array(x) for x in itertools.product([0,1],repeat=4)]
def prof(x,opt,pp=p): return pp@x + opt*np.sum(np.maximum(pp-3,0)*(1-x))
N=1500
# bloc TIOLI: bloc estimates p_t; posterior p_t ~ N(phat, sig^2); bloc proposes road set R and demand T (net of nothing: fleet pays T total, split equal)
for sig in [1,0.3,0.1]:
  for opt in [0,1]:
    D=opt*6.5; G=np.zeros(4); deal=0; eff=0
    for n in range(N):
        ph=p+sig*rng.standard_normal(4)
        sims=ph+sig*rng.standard_normal((400,4))  # posterior draws
        best=(0,None,None)
        for x in X:
            if x.sum()==0: continue
            H=s@(E@x)
            wtp=sims@x - (opt*np.sum(np.maximum(sims-3,0)*x,axis=1))  # road value minus reroute value forgone
            Ts=np.linspace(H,H+15,1501)-1e-9
            ev=[(np.mean(wtp>=T))*(T-H) for T in Ts]; k=int(np.argmax(ev))
            if ev[k]>best[0]: best=(ev[k],x,Ts[k])
        if best[1] is None: continue
        x,T=best[1],best[2]; H=s*(E@x)
        truewtp=p@x - opt*np.sum(np.maximum(p-3,0)*x)
        if truewtp>=T:
            deal+=1; G+=np.r_[truewtp-T, np.full(3,(T-H.sum())/3)]; eff+=truewtp-H.sum()
    G/=N; pie=6.0 if opt==0 else 1.5
    print(f"bloc TIOLI sig={sig} opt={opt}: deal {deal/N:.3f} realised pie {eff/N:.3f} of {pie} exp gains {np.round(G,3)} product {np.prod(G):.5f} floor {G.min():.3f}")
