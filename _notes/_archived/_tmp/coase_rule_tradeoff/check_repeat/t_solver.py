import numpy as np, time
from street import *
a=np.full((1,3),L); b=np.full((1,3),U)
for NG in (7,13,31,61):
    t=time.time(); v,r,s=solve_round2(a,b,NG=NG); print(NG, v, r, [SLOTN[t] for t in SUBSETS[s[0]]], time.time()-t)
# per subset optimum at NG=31
for si,S in enumerate(SUBSETS):
    pass
