import itertools, numpy as np
from lindahl import lindahl_ok
rng=np.random.default_rng(2)
def trial(m,kind):
    S=np.array(list(itertools.product([0,1],repeat=m)),float)
    p=rng.uniform(2,6,m); e=rng.uniform(0,1.5,(3,m)); w=np.where(np.arange(m)>=m*3//4,10**(10/10),1.0)  # night weight x10 energy
    if kind=='single':   # Lden-like: phi_i(sum_t w_t e_it x_t), phi convex power 1.5 (dose-response steeper at high dose)
        D=S@(e*w).T; H=np.c_[[ (D[:,i]/w.max())**rng.uniform(1.2,2.0)*rng.uniform(1,4) for i in range(3)]].T
    if kind=='rest':
        H=S@e.T
        for i in range(3):
            L=max(2,m//3); R=rng.uniform(1,3)
            for k,x in enumerate(S):
                q=np.r_[1-x,1-x]; run=best=0
                for v in q: run=run+1 if v else 0; best=max(best,run)
                H[k,i]+=R*(best<L)
    if kind=='arb':
        H=S@e.T+np.c_[[rng.uniform(0,2,len(S))*(S.sum(1)>0) for _ in range(3)]].T
    if kind=='arb2':  # two arbitrary residents only
        H=S@e.T; H[:,1:]+=np.c_[[rng.uniform(0,2,len(S))*(S.sum(1)>0) for _ in range(2)]].T
    return lindahl_ok(p,H,S)
if __name__=="__main__":
 for m,T in ((4,300),(6,200),(8,100),(10,30)):
     print(m,{k:round(np.mean([trial(m,k) for _ in range(T)]),2) for k in ('single','rest','arb2','arb')})
