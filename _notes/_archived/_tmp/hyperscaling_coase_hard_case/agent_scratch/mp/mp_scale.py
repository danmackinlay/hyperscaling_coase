# Mailath-Postlewaite on the instance: replicate the 3 profiles m times (n=3m), profits (and reroute cost) scaled by m.
# Sensitivities private, iid uniform on [sbar(1-a), sbar(1+a)]. Mechanisms: IC, interim IR (voluntary), ex ante budget balance.
# Second-best (designer maximises expected surplus): road slot t iff V_t - sum_j (s_j + mu (s_j-L_j)) e_jt >= 0, smallest feasible mu.
# Fleet-optimal mechanism: mu = 1.  Expected gains per replica.
import numpy as np, sys
rng=np.random.default_rng(1)
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); sbar=np.array([1,1,2.])
def run(m,a,opt,ndraw):
    L=sbar*(1-a); U=sbar*(1+a)
    V=(np.minimum(p,3) if opt else p)*m          # road value per slot over the fleet's no-deal action
    S=L[None,None,:]+(U-L)[None,None,:]*rng.random((ndraw,m,3))   # draws x replicas x profiles
    H=np.einsum('dmi,it->dt',S,E)                 # total harm per slot
    R=np.einsum('dmi,it->dt',S-L,E)               # total F/f term per slot
    xeff=(V-H>0)
    def x_mu(mu): return (V-H-mu*R>=0)
    def cons(x): return np.mean(np.sum(x*(V-H-R),axis=1))   # E[virtual surplus] >= 0
    if cons(xeff)>=0: mu=0.0
    else:
        lo,hi=0.0,1.0
        if cons(x_mu(1.0))<0: mu=None
        else:
            for _ in range(40):
                mid=(lo+hi)/2
                if cons(x_mu(mid))>=0: hi=mid
                else: lo=mid
            mu=hi
    out={}
    maxpie=np.mean(np.sum(np.maximum(V-H,0),axis=1))/m
    for name,mm in [('second-best',mu),('fleet-optimal',1.0)]:
        if mm is None: out[name]=None; continue
        x=x_mu(mm)
        pe=np.mean(np.all(x==xeff,axis=1))
        pie=np.mean(np.sum(x*(V-H),axis=1))/m
        # resident gains per profile per replica: E[(s-L) E_i(x)]
        Ex=np.einsum('dt,it->di',x.astype(float),E)          # exposure used, per profile
        rg=np.mean((S-L).mean(axis=1)*Ex,axis=0)               # per resident of each profile
        fg=pie-rg.sum()
        out[name]=(mm,pe,pie,maxpie,fg,rg)
    return out
for opt in [0,1]:
  for a in [1.0,0.5,0.2]:
    for m in [1,10,100]:
        nd=20000 if m<100 else 4000
        o=run(m,a,opt,nd)
        for k,v in o.items():
            if v is None: print(f"opt={opt} a={a} n={3*m:3d} {k}: infeasible"); continue
            mm,pe,pie,mx,fg,rg=v
            g=np.r_[fg,rg]
            print(f"opt={opt} a={a} n={3*m:3d} {k:13s} mu={mm:.3f} P(efficient sched)={pe:.3f} pie/replica {pie:.3f} of {mx:.3f}  gains/replica fleet {fg:.3f} res {np.round(rg,3)} prod(fleet/rep, residents) {np.prod(g):.4f}")
