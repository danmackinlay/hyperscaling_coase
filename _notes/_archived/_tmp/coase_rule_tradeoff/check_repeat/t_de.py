# independent cross-check of the round-two solver by differential evolution over rates (all subsets)
import numpy as np
from scipy.optimize import differential_evolution
from street import *
rng=np.random.default_rng(1)
cases=[np.array([[0.5,0.5,0.5],[2.5,2.5,2.5]]), np.array([[0.5,0.5,0.5],[0.8,2.44,2.5]]), np.array([[0.8,0.5,0.5],[2.5,2.44,2.5]])]
for _ in range(5):
    lo=rng.uniform(0.5,2.3,3); hi=lo+rng.uniform(0.05,2.5-lo); cases.append(np.array([lo,hi]))
for ab in cases:
    a,b=ab[0],ab[1]
    v,r,s=solve_round2(a[None],b[None],NG=9)
    bestde=0
    for S in SUBSETS:
        f=lambda x: -profit(S,np.array(x),a,b)
        o=differential_evolution(f,list(zip(a,b)),tol=1e-12,seed=0,polish=True,maxiter=2000)
        bestde=max(bestde,-o.fun)
    print(np.round(a,3),np.round(b,3),"solver %.10f DE %.10f diff %.2e"%(v[0],bestde,bestde-v[0]))
