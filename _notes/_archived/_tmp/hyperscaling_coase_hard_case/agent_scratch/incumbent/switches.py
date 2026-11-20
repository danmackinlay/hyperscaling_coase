import numpy as np, itertools
from base import *
# outside option: reroute any slot at cost 3; fleet no-deal = reroute all
out=(p-3).clip(0).sum()
best=max(S,key=lambda x: p@np.array(x)-harms(x).sum()+((p-3)*(1-np.array(x))).clip(0).sum())
tot=p@np.array(best)-harms(best).sum()+((p-3)*(1-np.array(best))).clip(0).sum()
print('outside option: fleet no-deal',out,'best river set',lab(best),'total',tot,'pie over no deal',tot-out, ' Nash each',(tot-out)/4)
# clause language
for name,blocks in [('4 slots',[[0],[1],[2],[3]]),('day MDE / night N',[[0,1,2],[3]]),('day MD / night EN',[[0,1],[2,3]]),('all or nothing',[[0,1,2,3]])]:
    pies=[]
    for c in itertools.product([0,1],repeat=len(blocks)):
        x=np.zeros(4,int)
        for b,on in zip(blocks,c):
            if on: x[b]=1
        pies.append((p@x-harms(tuple(x)).sum(),lab(x)))
    print('clauses',name,max(pies))
# remediation: insulate any subset, cost 2 each
best=None
for ins in itertools.product([0,1],repeat=3):
    Rm=R*np.where(np.array(ins)[:,None]==1,0.5,1)
    for x in S:
        v=p@np.array(x)-(Rm@np.array(x)).sum()-2*sum(ins)
        if best is None or v>best[0]: best=(v,ins,lab(x))
print('remediation best',best)
# repeated: grim trigger premium g<=2 delta
for d in (0.5,0.8,0.95):
    g=min(1.5,2*d); print('delta',d,'max premium',g,'NP',(6-3*g)*g**3)
# k=2 pact breaking (no enforcer): fleet+1+2 gain per year vs pact, resident 3 loss per year
print('k=2: coalition {F,1,2} gain/yr over pact',13.5-4.5,' resident 3 loss/yr',1.5+8)
