# Bernheim-Whinston truthful menu-auction payoffs: sum_{i in S} u_i <= W(N)-W(N\S)
import itertools
from scipy.optimize import linprog
def run(alts,names,label):
    n=len(names); W=lambda S: max(sum(a[i] for i in S) for a in alts.values()) if S else 0.0
    N=list(range(n)); A=[];b=[]
    for r in range(1,n+1):
        for S in itertools.combinations(N,r):
            row=[1 if i in S else 0 for i in N]; A.append(row); b.append(W(N)-W([i for i in N if i not in S]))
    res=linprog([-1]*n,A_ub=A,b_ub=b,bounds=[(None,None)]*n)
    u=res.x; act=max(alts,key=lambda k:sum(alts[k]))
    print(label,'action',act,'principal net payoffs',dict(zip(names,[round(x,3) for x in u])),'platform takes',round(W(N)-sum(u),3))
# k=2: enforce residents' pact (4-party Nash, 1.5 each) vs not (fleet divide and conquer)
run({'enforce':[1.5,1.5,1.5,1.5],'not':[18.5,-2,-3,-8]},['F','r1','r2','r3'],'k=2 three resident bidders:')
run({'enforce':[1.5,4.5],'not':[18.5,-13]},['F','R'],'k=2 residents one bidder:')
# with clause language as a second dimension (enforce under L1 all-or-nothing: pie 5.5)
run({'enforce L4':[1.5]*4,'enforce L1':[5.5/4]*4,'not':[18.5,-2,-3,-8]},['F','r1','r2','r3'],'k=2 with clause choice:')
# k=3: platform sells commitment: fleet TIOLI, neutral haggling, bloc TIOLI (equal internal split)
run({'fleet commits':[6,0,0,0],'neutral':[1.5]*4,'bloc commits':[0,2,2,2]},['F','r1','r2','r3'],'k=3 commitment seller:')
