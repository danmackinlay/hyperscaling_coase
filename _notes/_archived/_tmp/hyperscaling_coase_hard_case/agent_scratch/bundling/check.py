import numpy as np, itertools
from scipy.stats import norm
from scipy.optimize import minimize
import importlib.util,sys
spec=importlib.util.spec_from_file_location('t','tioli2.py'); src=open('tioli2.py').read().split('for tau in (1.0')[0]
ns={}; exec(src,ns)
p,e,s,X,table,plan=ns['p'],ns['e'],ns['s'],ns['X'],ns['table'],ns['plan']
rng=np.random.default_rng(3)
for tau in (1.0,0.3):
  T=[table(tau*(e@x)) for x in X]
  for _ in range(3):
    sh=s+rng.normal(0,tau,3)
    for j in (6,14):  # two schedules
        x=X[j]; E=e@x; S=p@x-sh@E; sig=tau*E; idx=[i for i in range(3) if E[i]>0]
        v,_=plan(T[j],np.array([S]))
        f=lambda M: -np.prod(norm.cdf(M/sig[idx]))*(S-M.sum())
        best=max((-minimize(f,np.full(len(idx),st),method='Nelder-Mead',options={'xatol':1e-8,'fatol':1e-10,'maxiter':20000}).fun) for st in (0,0.5,1,2))
        print(tau,''.join('MDEN'[t] for t in range(4) if x[t]),'table %.5f brute %.5f'%(v[0],max(best,0)))
