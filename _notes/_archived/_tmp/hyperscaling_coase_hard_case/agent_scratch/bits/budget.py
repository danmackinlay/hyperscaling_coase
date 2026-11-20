# Fleet estimates residents' harms, proposes the schedule maximising estimated surplus,
# pays each resident estimated harm + 1/4 of estimated pie; k=3: any resident whose
# true gain < 0 vetoes -> no deal, all zero. Expectations count failed deals as zero.
import itertools, numpy as np
rng=np.random.default_rng(0)
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
S=np.array(list(itertools.product([0,1],repeat=4)),float)
Htrue_par=(S@E.T)*s                       # 16x3
inter=(S[:,0]*S[:,2])*1.5
Htrue_arb=Htrue_par.copy(); Htrue_arb[:,2]+=inter
def run(Htrue, model, eps, T=200000):
    out=np.zeros((T,4)); deals=0; pies=np.zeros(T)
    for t in range(T):
        if model=='par':
            sh=s+eps*rng.standard_normal(3); Hh=(S@E.T)*sh
        else:  # residents 1,2 parametric; resident 3 full table, each nonempty entry its own noise
            sh=s[:2]+eps[0]*rng.standard_normal(2)
            Hh=np.c_[(S@E[:2].T)*sh, Htrue[:,2]+eps[1]*rng.standard_normal(16)*(S.sum(1)>0)]
        W=S@p-Hh.sum(1); j=np.argmax(W); P=W[j]
        if P<=0: continue
        g=np.r_[P/4, Hh[j]-Htrue[j]+P/4]
        if (g[1:]<0).any(): continue
        out[t]=g; deals+=1; pies[t]=S[j]@p-Htrue[j].sum()
    m=out.mean(0)
    return dict(deal=deals/T, gains=m.round(3), pie=pies.mean().round(3), prod=(np.prod(m) if (m>0).all() else 0).round(4), floor=m.min().round(3), resshare=(m[1:].sum()/max(m.sum(),1e-9)).round(3))
for eps in (1,0.3,0.1,0.01):
    print('eps',eps)
    print('  truth par, model par      ', run(Htrue_par,'par',eps,40000))
    print('  truth arb, model par      ', run(Htrue_arb,'par',eps,40000))
    print('  truth arb, full table, same per-param err', run(Htrue_arb,'arb',(eps,eps),40000))
    # same total budget: parametric spends C=3/eps^2 over 3 params; full model has 2+15=17 params
    e2=eps*np.sqrt(17/3)
    print('  truth arb, full table, same total budget (err %.2f)'%e2, run(Htrue_arb,'arb',(e2,e2),40000))
