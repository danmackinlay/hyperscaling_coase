import numpy as np
from street import *
rng=np.random.default_rng(0)
# intervals like those in the grids
cv=[L+(U-L)*q for q in sorted(set([round(0.05*k,4) for k in range(1,20)]+[0.97,0.98,0.99,0.995]))]
ivs=[(L,U)]+[(L,c) for c in cv]+[(c,U) for c in cv]
K=4000
idx=rng.integers(0,len(ivs),(K,3))
a=np.array([[ivs[j][0] for j in row] for row in idx]); b=np.array([[ivs[j][1] for j in row] for row in idx])
res={}
for NG in (9,21,41):
    res[NG]=solve_round2(a,b,NG=NG)
for NG in (9,21):
    d=res[41][0]-res[NG][0]
    print(NG,"n>1e-6:",(d>1e-6).sum(),"max",d.max(), "min", d.min())
d=res[41][0]-res[9][0]; j=np.argmax(d)
print(a[j],b[j],res[9][0][j],res[9][1][j],SUBSETS[res[9][2][j]],res[41][0][j],res[41][1][j],SUBSETS[res[41][2][j]])
