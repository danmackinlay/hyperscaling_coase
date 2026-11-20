import numpy as np, itertools
from scipy.optimize import linprog, minimize
from base import *
# k=2 core: players F,1,2,3. v(N)=6. v(F+pair)=fleet+pair value ignoring excluded. v(any two residents)=0 (block). v(singletons): F 0, resident i guarantee -h_i(MDEN)
v={('F',1,2):13.5,('F',1,3):8.5,('F',2,3):7.5,(1,2):0,(1,3):0,(2,3):0,(1,2,3):0,('F',):0,(1,):-2,(2,):-3,(3,):-8}
idx={'F':0,1:1,2:2,3:3}
A=[];b=[]
for C,val in v.items():
    row=np.zeros(4)
    for c in C: row[idx[c]]=1
    A.append(-row); b.append(-val)
res=linprog(np.ones(4),A_ub=A,b_ub=b,bounds=[(None,None)]*4)
print('k=2 min total to satisfy all coalition claims',res.fun,res.x,' deficit',res.fun-6)
# k=3 Nash: equal split 1.5
print('k=3 Nash product',1.5**4)
# wealth effects: Nash product in utility gains
w0=np.array([100,10,10,2.0])
def negNP(g):
    g=np.asarray(g); 
    if np.any(g<=0): return 1e9
    return -np.sum(np.log(np.log1p(g/w0)))
cons={'type':'eq','fun':lambda g: g.sum()-6}
r=minimize(negNP,np.ones(4)*1.5,constraints=[cons],method='SLSQP')
g=r.x; print('utility-Nash money gains (F,1,2,3)',g.round(3),'transfers to residents',(g[1:]+np.array([1,2.5,4])).round(3))
print('  utility gains',np.log1p(g/w0).round(4),' product',np.prod(np.log1p(g/w0)))
print('  equal money split in utility: product',np.prod(np.log1p(1.5/w0)))
# Sybil: resident 2 -> 2a,2b,2c each 1/3 exposure
print('--- Sybil')
for m in (1,3,10):
    n_agents=1+2+m  # fleet + r1 + r3 + m sybils
    each=6/n_agents
    gains_h=[each,each,m*each,each]
    print(f'unanimity, m={m}: per-agent {each:.3f}; per human (F,1,2,3)',np.round(gains_h,3),'human NP',round(np.prod(gains_h),3),'floor',round(min(gains_h),3))
# literal k=3 of 5 with coordinated sybils: F + resident2 alone winning
val=p.sum()-R[1].sum()
print('k=3-of-5, sybils coordinated: F+2 runs MDEN, value',val,'Nash between F and 2 ->',val/2,'each; r1,r3',-R[0].sum(),-R[2].sum())
# uncoordinated: price of signature ->0, MDEN
print('k=3-of-5 uncoordinated: (18.5; -2,-3,-8)')
# sybil also at k=2 (2-of-5)
