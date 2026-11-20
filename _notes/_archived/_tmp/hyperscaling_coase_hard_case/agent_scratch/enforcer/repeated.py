import itertools, math
from regress import S,prof,harm,name
D=[0.5,0.8,0.95]
MDE=(1,1,1,0); ALL=(1,1,1,1)
def grid(pie=6.0,step=0.25):
    n=int(round(pie/step))
    for a in range(n+1):
        for b in range(n+1-a):
            for c in range(n+1-a-b):
                F=pie-step*(a+b+c); yield (F,step*a,step*b,step*c)
def nash(v): 
    return math.prod(v) if min(v)>0 else (0.0 if min(v)==0 else float('nan'))
def best_side_offer(pact,d,k,arb=False,cash=None,reversion='robust'):
    """Fleet's best side offer to a winning coalition C (|C|>=k) in one period.
    Deviators' continuation and fleet's continuation after collapse:
      robust: stage eq of the k-game (k=3: fleet TIOLI (6;0,0,0); k=2: (18.5;-H))
      naive : all residents refuse forever (0 for all)
    Returns max over C,x of fleet PV gain from deviating minus PV of pact."""
    F,*v=pact
    H=[harm(i,ALL,arb) for i in range(3)]
    if reversion=='robust':
        if k==3: sF,sR=6.0 if not arb else 5.0,[0,0,0]
        else: sF,sR=prof(ALL),[-h for h in H]
    else: sF,sR=0.0,[0,0,0]
    best=-1e9; arg=None
    for r in range(k,4):
        for C in itertools.combinations(range(3),r):
            for x in S:
                # minimal bribe to each deviator: t_i - h_i(x) + d*sR_i/(1-d) = v_i/(1-d)
                t=[harm(i,x,arb)+(v[i]-d*sR[i])/(1-d) for i in C]
                # residents outside C: k>len? no, C is winning
                B=sum(t)
                if cash is not None and B>cash+prof(x): continue
                gain=prof(x)-B+d*sF/(1-d)-F/(1-d)
                if gain>best: best,arg=gain,(C,name(x),round(B,2))
    return best,arg
out=[]
for arb in (False,True):
    pie=5.0 if arb else 6.0
    print('==== arbitrary' if arb else '==== parametric', 'pie',pie)
    for k in (3,2):
        for rev in ('robust','naive'):
            for d in D:
                ok=[pc for pc in grid(pie) if best_side_offer(pc,d,k,arb,reversion=rev)[0]<=1e-9]
                bestp=max(ok,key=lambda pc:nash(pc) if not math.isnan(nash(pc)) else -1,default=None)
                print(f'k={k} {rev:6s} d={d}: {len(ok)}/{len(list(grid(pie)))} pacts self-enforcing;',
                      'max Nash product', None if bestp is None else (bestp, round(nash(bestp),3)))
    # cash-constrained (fleet w0=100, promises unenforceable): k=2 robust reversion
    for d in D:
        ok=[pc for pc in grid(pie) if best_side_offer(pc,d,2,arb,cash=100,reversion='robust')[0]<=1e-9]
        bestp=max(ok,key=lambda pc:nash(pc),default=None)
        eq=(pie/4,)*4
        g,arg=best_side_offer(eq,d,2,arb,cash=None)
        print(f'k=2 cash<=100+p(x) d={d}: {len(ok)} pacts survive; equal split bribe needed (no cash cap): {arg}',
              'max product', None if bestp is None else (bestp,round(nash(bestp),3)))
# fleet-commitment variant at k=3 (river row 9/13 convention): fleet's deviation gains pie once, then 0
for d in D:
    ok=[pc for pc in grid(6.0) if pc[0]>=6*(1-d)-1e-9]
    b=max(ok,key=nash); print('k=3 fleet-commit variant d',d,'F*>=',6*(1-d),'max product',b,round(nash(b),3))
