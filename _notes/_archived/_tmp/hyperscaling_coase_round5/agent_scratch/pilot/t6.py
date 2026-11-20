import sys, time; sys.path.insert(0,'.')
from sim import *
import l3
def br_zero(S, G):
    # ties broken toward d = 0
    mx = S.max(-1, keepdims=True)
    ok = S >= mx - 1e-12
    dist = np.where(ok, np.abs(G), np.inf)
    return G[dist.argmin(-1)]
orig = l3.br
for tb in ['highest','zero']:
    l3.br = orig if tb=='highest' else br_zero
    for sc in ['counterfactual','own_offer']:
        for m in [5,50]:
            for H in [1,10]:
                c=Cfg(res_class="L3",m=m,H=H,scoring=sc)
                rs=[run_one((c,[1,r])) for r in range(6)]
                s=summarise(rs); print(tb, sc, m, H, {k:np.round(v,2) for k,v in s.items()})
