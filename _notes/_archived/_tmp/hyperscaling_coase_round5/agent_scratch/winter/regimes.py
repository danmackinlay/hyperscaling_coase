import itertools, math, sys
sys.path.insert(0,'.')
from dc import *
# Regimes at q=1 (all agents best-reply), k=2 and k=3
for k in (3,2):
    for name,allowed in (('contingent clauses allowed','NFHC'),('flat offers only (platform bans contingency)','NFH')):
        v,x,menu,E=best(1.0,k,1.5,False,allowed)
        print(f'k={k} {name:45s} sched={sched(x):5s} menu={"".join(menu)} co={E[0]:6.2f} A={E[1]:6.2f} B={E[2]:6.2f} C={E[3]:6.2f} | {criterion(E)}')
# binding all-or-none pact at fair demand (h_i+1.5): company must pay all three F or nothing
bestv=(0,None)
for x in X:
    co=prof(x)-sum(h(i,x)+1.5 for i in range(3))
    if co>bestv[0]: bestv=(co,x)
co,x=bestv; print(f'k=2 binding all-or-none pact (prem 1.5)              sched={sched(x)} co={co:.2f} residents=(1.5,1.5,1.5)')
# commitment sweep: pact binds (all-or-none) with prob r, else all three agents adaptive (best-reply); company sees nothing, picks a contract
# that is either the pact price (FFF on best x) or the contingent CCC; if CCC offered and pact binds, deal fails.
print('\nsweep: pact binds with prob r; contingent clauses allowed; k=2')
for prem in (0.5,1.5,3.0):
  for r in (0,0.25,0.5,0.75,0.9,1.0):
    opts=[]
    for x in X:
        fff=prof(x)-sum(h(i,x)+prem for i in range(3))   # accepted by both
        opts.append((fff,'FFF',x,[prem]*3))
        # CCC: adaptive sign for eps each (all three), pact refuses -> no deal
        ccc=(1-r)*(prof(x)-3*EPS)
        opts.append((ccc,'CCC',x,[(1-r)*(EPS-h(i,x)) for i in range(3)]))
    opts.append((0,'none',None,[0,0,0]))
    co,m,x,R=max(opts,key=lambda o:o[0])
    print(f'prem={prem} r={r:.2f} offer={m} sched={sched(x):5s} co={co:6.2f} A={R[0]:6.2f} B={R[1]:6.2f} C={R[2]:6.2f} sumR={sum(R):6.2f} vsSQ=({R[0]+1:+.2f},{R[1]+2.5:+.2f},{R[2]+4:+.2f})')
