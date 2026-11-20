# Fleet take-it-or-leave-it under finite estimation budgets (parametric switch only; k=3; once; linear money).
# Fleet observes shat_i = s_i + eps_i, eps ~ N(0,tau^2); flat prior => posterior s_i ~ N(shat_i, tau^2).
# Bundle: one offer per resident for a whole schedule x: transfer (shat_i + m_i) * E_i(x); accept iff >= s_i E_i(x).
# Slot-by-slot: one offer per resident per slot t: (shat_i + m_it) e_it; slot runs iff all exposed residents accept.
import itertools, numpy as np
from scipy.stats import norm
from scipy.optimize import minimize
p=np.array([4,5.5,4,5.]); e=np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s=np.array([1,1,2.])
X=[np.array(x) for x in itertools.product([0,1],repeat=4) if any(x)]
def opt_offer(S, E, tau):
    """max over m (per unit exposure, one per exposed resident) of prod Phi(m_i/tau) * (S - sum m_i E_i); S = profit - sum shat_i E_i"""
    idx=[i for i in range(3) if E[i]>0]
    if S<=-50: return -1, None
    best=(-1e9,None)
    for start in (0.0, tau, 2*tau, -tau):
        f=lambda m: -np.prod(norm.cdf(m/tau))*(S-np.dot(m,E[idx]))
        r=minimize(f, np.full(len(idx),start), method='Nelder-Mead', options={'xatol':1e-6,'fatol':1e-9,'maxiter':4000})
        if -r.fun>best[0]: best=(-r.fun,r.x)
    m=np.zeros(3); m[idx]=best[1]
    return best[0], m
def run(tau, n=4000, seed=1):
    rng=np.random.default_rng(seed)
    outB=np.zeros(4); outS=np.zeros(4); dealB=0; slotsS=np.zeros(4); pieB=0; pieS=0
    for _ in range(n):
        eps=rng.normal(0,tau,3); sh=s+eps
        # bundle
        bv=0; bx=None; bm=None
        for x in X:
            E=e@x; S=p@x-sh@E
            v,m=opt_offer(S,E,tau)
            if v>bv: bv,bx,bm=v,x,m
        if bx is not None:
            E=e@bx; acc=all((bm[i]>=-eps[i]) or E[i]==0 for i in range(3))
            if acc:
                dealB+=1
                pay=(sh+bm)*E; outB[0]+=p@bx-pay.sum(); outB[1:]+=pay-s*E; pieB+=p@bx-(s*E).sum()
        # slot by slot
        for t in range(4):
            E=e[:,t]; S=p[t]-sh@E
            v,m=opt_offer(S,E,tau)
            if v>0:
                acc=all((m[i]>=-eps[i]) or E[i]==0 for i in range(3))
                if acc:
                    slotsS[t]+=1; pay=(sh+m)*E; outS[0]+=p[t]-pay.sum(); outS[1:]+=pay-s*E; pieS+=p[t]-(s*E).sum()
    outB/=n; outS/=n
    rep=lambda o: '(%.3f; %.3f, %.3f, %.3f) product %.4f floor %.3f residents %.3f'%(o[0],o[1],o[2],o[3],np.prod(o),o.min(),o[1:].sum())
    print('tau=%.2f BUNDLE deal %.3f pie %.3f %s'%(tau,dealB/n,pieB/n,rep(outB)))
    print('          SLOTS  slot run rates M,D,E,N %s pie %.3f %s'%(np.round(slotsS/n,3),pieS/n,rep(outS)))
import sys
for tau in [float(a) for a in sys.argv[1:]]: run(tau)
