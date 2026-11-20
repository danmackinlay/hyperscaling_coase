import sys, time; sys.path.insert(0,'.')
from sim import *
rng=np.random.default_rng(0)
for step in [0.25,0.5,1]:
    G=grid(step)
    lw=rng.normal(size=(7,3,G.size))*2; mu=rng.random((7,3))*2
    for sc in ['counterfactual','own_offer']:
        c=Cfg(step=step, scoring=sc)
        a=exp_branches(lw,mu,c,G); b=exp_branches_fast(lw,mu,c,G)
        print(step, sc, max(np.abs(x[1]-y[1]).max()+np.abs(x[2]-y[2]).max() for x,y in zip(a,b)))
for H in [10,50]:
    t0=time.time(); r=run_L1(Cfg(H=H),1); print(H, r, time.time()-t0)
