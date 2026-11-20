import numpy as np, model as M
rng=np.random.default_rng(7); N=1000
s=rng.uniform(.5,2.5,(3,N)); m=rng.uniform(.6,1.4,N)
for ins in (False,True):
    fi=M.full_info(s,m,ins)
    for sigma in (np.inf,0.3):
        k=0 if np.isinf(sigma) else sigma
        c,h=M.offer_maker(s,m,ins,-1,s+k*rng.standard_normal((3,N)),m,sigma)
        tot=c+h.sum(0)
        print(ins,sigma,"A: max(tot-fi)",(tot-fi).max(),"min comp",c.min(),"P(comp<0)",(c<0).mean(),"min hh",h.min())
        for j in range(3):
            c,h=M.offer_maker(s,m,ins,j,s+k*rng.standard_normal((3,N)),m+0.4*k*rng.standard_normal(N),sigma)
            tot=c+h.sum(0)
            print("  seat",j,"max(tot-fi)",(tot-fi).max(),"min comp",c.min(),"min maker",h[j].min(),"P(maker<0)",(h[j]<0).mean(),"min other",np.delete(h,j,0).min())
