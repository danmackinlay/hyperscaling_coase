# How often do personalized per-slot (linear) prices support the efficient schedule?
# If yes, verification needs n*m numbers (Segal 2007: communication = supporting budget sets).
import itertools, numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(1)
def lindahl_ok(p,H,S):
    n=H.shape[1]; m=S.shape[1]; W=S@p-H.sum(1); j=np.argmax(W); opt=S[j]
    A=[];b=[]
    for k,x in enumerate(S):
        d=x-opt
        if not d.any(): continue
        row=np.zeros(n*m)
        for i in range(n): row[i*m:(i+1)*m]=-d
        A.append(row); b.append(-(p@d))
        for i in range(n):
            row=np.zeros(n*m); row[i*m:(i+1)*m]=d; A.append(row); b.append(H[k,i]-H[j,i])
    return linprog(np.zeros(n*m),A_ub=A,b_ub=b,bounds=[(None,None)]*(n*m),method='highs').status==0
def trial(m,kind,narb):
    S=np.array(list(itertools.product([0,1],repeat=m)),float)
    p=rng.uniform(2,6,m); e=rng.uniform(0,1.5,(3,m)); H=S@e.T
    for i in range(narb):
        if kind=='pair':      # random supermodular pairwise terms
            Q=np.triu(rng.uniform(0,1.5,(m,m))*(rng.random((m,m))<0.3),1)
            H[:,i]+=np.einsum('ka,ab,kb->k',S,Q,S)
        elif kind=='rest':    # +R unless some run of >=L consecutive quiet slots (circular day)
            L=max(2,m//3); R=rng.uniform(1,3)
            for k,x in enumerate(S):
                q=np.r_[1-x,1-x]; run=best=0
                for v in q: run=run+1 if v else 0; best=max(best,run)
                H[k,i]+=R*(min(best,m)<L)
        elif kind=='arb':     # arbitrary nonneg table
            H[:,i]+=rng.uniform(0,2,len(S))*(S.sum(1)>0)
    return lindahl_ok(p,H,S)
if __name__=="__main__":
  for m in (4,6,8):
     for kind in ('pair','rest','arb'):
         for narb in (1,3):
             T=200 if m<8 else 60
             r=np.mean([trial(m,kind,narb) for _ in range(T)])
             print(m,kind,'arbitrary residents',narb,'linear supporting prices exist in',round(r,2))
