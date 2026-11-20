import itertools, numpy as np, lindahl2 as L
from lindahl import lindahl_ok
# patch: record whether the optimum is interior (neither all slots nor none)
rng=np.random.default_rng(3); L.rng=rng
orig=L.lindahl_ok; stats=[]
def rec(p,H,S):
    W=S@p-H.sum(1); j=np.argmax(W); k=S[j].sum(); stats.append(0<k<S.shape[1]); return orig(p,H,S)
L.lindahl_ok=rec
for kind in ('single','rest','arb'):
    stats.clear(); r=np.mean([L.trial(8,kind) for _ in range(80)]); print(kind,'support',round(r,2),'interior optimum share',round(np.mean(stats),2))
