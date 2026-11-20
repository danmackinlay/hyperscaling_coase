import numpy as np
from tioli import run_fleet, summ
from bloc import run_bloc
sigs=(1.0,0.316,0.1,0.0316)
F={s:run_fleet(s,500)[:,:4].mean(0) for s in sigs}
B={s:run_bloc(s,800)[:,:4].mean(0) for s in sigs}
def rep(sf,sn):
    g=0.5*F[sf]+0.5*B[sn]
    npd=np.prod(g)
    print(f'random proposer sig_f={sf} sig_N={sn}: (F;1,2,3)=({g[0]:.2f};{g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) resShare {g[1:].sum()/g.sum():.2f} NP {npd:.3f} floor {g.min():.2f}')
for (sf,sn) in [(1.0,1.0),(0.316,0.316),(0.1,0.1),(0.0316,0.0316),(0.1,0.316),(0.316,0.1),(0.0316,0.1),(0.1,0.0316),(0.316,1.0),(1.0,0.316)]:
    rep(sf,sn)
