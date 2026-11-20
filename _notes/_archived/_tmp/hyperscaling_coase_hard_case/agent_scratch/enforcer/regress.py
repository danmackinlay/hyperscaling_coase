import itertools, math
p=[4,5.5,4,5]
E=[[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]; s=[1,1,2]
S=list(itertools.product([0,1],repeat=4))
def harm(i,x,arb=False):
    h=s[i]*sum(e*xx for e,xx in zip(E[i],x))
    if arb and i==2 and x[0] and x[2]: h+=1.5
    return h
def prof(x): return sum(a*b for a,b in zip(p,x))
def name(x): return ''.join(c for c,b in zip('MDEN',x) if b) or '-'
for arb in (False,True):
    print('=== arbitrary' if arb else '=== parametric')
    best=max(S,key=lambda x:prof(x)-sum(harm(i,x,arb) for i in range(3)))
    pie=prof(best)-sum(harm(i,best,arb) for i in range(3))
    print('efficient',name(best),'pie',pie)
    # k=2 stage: competition to sign -> fleet runs profit-max schedule, pays ~0
    H=[harm(i,(1,1,1,1),arb) for i in range(3)]
    print('k=2 stage outcome (18.5; %s)'%[-h for h in H])
    vF={}
    for pair in itertools.combinations(range(3),2):
        xs=max(S,key=lambda x:prof(x)-sum(harm(i,x,arb) for i in pair))
        vF[pair]=prof(xs)-sum(harm(i,xs,arb) for i in pair)
        print(' v(F,%s)='%(tuple(i+1 for i in pair),),vF[pair],name(xs),
              ' check MDEN value',prof((1,1,1,1))-sum(H[i] for i in pair))
    tot=sum(vF.values())
    print(' sum of pair values',tot,'-> core needs F>=',tot-2*pie,'(and resident pairs >=0): empty' )
    # clause languages
    langs={'4 slots':S,'2 clauses (MDE|N)':[x for x in S if x[0]==x[1]==x[2]],
           '2 clauses alt (MD|EN)':[x for x in S if x[0]==x[1] and x[2]==x[3]],
           '1 clause':[(0,0,0,0),(1,1,1,1)]}
    for L,xs in langs.items():
        b=max(xs,key=lambda x:prof(x)-sum(harm(i,x,arb) for i in range(3)))
        print(' clause',L,'best',name(b),'pie',prof(b)-sum(harm(i,b,arb) for i in range(3)))
