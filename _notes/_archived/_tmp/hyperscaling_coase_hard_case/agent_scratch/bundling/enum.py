import itertools, math
p=[4,5.5,4,5]; S=['M','D','E','N']
e=[[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]; s=[1,1,2]
def harms(x,arb):
    h=[s[i]*sum(e[i][t]*x[t] for t in range(4)) for i in range(3)]
    if arb and x[0] and x[2]: h[2]+=1.5
    return h
def name(x): return ''.join(S[t] for t in range(4) if x[t]) or '-'
for arb in (False,True):
    print('ARB' if arb else 'PARAM')
    rows=[]
    for x in itertools.product([0,1],repeat=4):
        pr=sum(p[t]*x[t] for t in range(4)); h=harms(x,arb); rows.append((pr-sum(h),name(x),pr,h))
    rows.sort(reverse=True)
    for r in rows: print('  %-5s profit %5.1f harms %s pie %5.2f'%(r[1],r[2],r[3],r[0]))
    # clause languages
    def best(groups):
        bestv=-1e9
        for c in itertools.product([0,1],repeat=len(groups)):
            x=[0]*4
            for g,ci in zip(groups,c):
                for t in g: x[t]=ci
            pr=sum(p[t]*x[t] for t in range(4)); v=pr-sum(harms(x,arb))
            if v>bestv: bestv,bx=v,name(x)
        return bestv,bx
    print('  4 clauses',best([[0],[1],[2],[3]]),' 2 clauses MDE|N',best([[0,1,2],[3]]),' 2 clauses MD|EN',best([[0,1],[2,3]]),' 1 clause',best([[0,1,2,3]]))
    # slot by slot marginal pricing: sequential orders, each slot added iff marginal surplus>0 (tie -> not added / added)
    for tie in ('strict','weak'):
        res={}
        for order in itertools.permutations(range(4)):
            x=[0]*4
            for t in order:
                base=sum(p[u]*x[u] for u in range(4))-sum(harms(x,arb))
                y=x.copy(); y[t]=1
                m=sum(p[u]*y[u] for u in range(4))-sum(harms(y,arb))-base
                if m>0 or (tie=='weak' and m>=0): x=y
            v=sum(p[u]*x[u] for u in range(4))-sum(harms(x,arb))
            res.setdefault((name(x),v),[]).append(''.join(S[t] for t in order))
        print('  sequential slot-by-slot (%s):'%tie,{k:len(v) for k,v in res.items()})
    # stable profiles: no slot's marginal surplus has the wrong sign
    stab=[]
    for x in itertools.product([0,1],repeat=4):
        ok=True
        for t in range(4):
            y=list(x); y[t]=1-y[t]
            vx=sum(p[u]*x[u] for u in range(4))-sum(harms(x,arb)); vy=sum(p[u]*y[u] for u in range(4))-sum(harms(y,arb))
            if vy>vx+1e-12: ok=False
        if ok: stab.append((name(x),sum(p[u]*x[u] for u in range(4))-sum(harms(x,arb))))
    print('  slot-wise stable (no single-slot improvement, weak):',stab)
# Nash per slot vs bundle, parametric
surp=[p[t]-sum(s[i]*e[i][t] for i in range(3)) for t in range(4)]
print('slot surplus',surp)
print('per-slot Nash quarter shares',[x/4 for x in surp])
print('bundle MDE Nash each', sum(surp[:3])/4, 'product',(sum(surp[:3])/4)**4)
print('arb MD Nash each',5/4,'product',(5/4)**4)
