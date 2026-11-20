import numpy as np, itertools
import hangwen as H
from hangwen import *
def solve_chk(q,k,delta,order=None,E=E0,S=S0,arb=False,tol=1e-9,damp=0.5):
    n=len(q); nres=n-1
    def harm(x):
        h=S*(E@x)
        if arb and x[0] and x[2]: h[-1]+=1.5
        return h
    opts=[]
    for x in X:
        h=harm(x); P=p@x
        for r in range(k,nres+1):
            for C in itertools.combinations(range(nres),r): opts.append((x,C,P-sum(h[i] for i in C),h))
    V=np.zeros(n); Pp=proposer_probs(q,order); conv=False
    for it in range(20000):
        newV=np.zeros(n); choice={}
        for pr in range(n):
            best=None
            for x,C,val,h in opts:
                if pr>0 and (pr-1) not in C: continue
                members=[0]+[1+i for i in C]; pay=np.zeros(n)
                for i in range(nres): pay[1+i]=-h[i]
                for m in members:
                    if m!=pr: pay[m]=delta*V[m]
                pay[pr]=val-sum(delta*V[m] for m in members if m!=pr)
                if best is None or pay[pr]>best[0]+1e-12: best=(pay[pr],pay,nm(x),C)
            choice[pr]=best; newV+=Pp[pr]*best[1]
        if np.max(np.abs(newV-V))<tol: V=newV; conv=True; break
        V=damp*newV+(1-damp)*V
    # verify fixed point residual without damping
    return V,Pp,choice,conv,it
for k in (2,):
    for d in (0.5,0.8,0.95):
        for lab,q,o in [("sym 0.9",[0.9]*4,None),("fleet .9 res .5",[0.9,0.5,0.5,0.5],None),("fleet .5 res .9",[0.5,0.9,0.9,0.9],None),("fleet first",[0.9]*4,(0,1,2,3)),("r3 first",[0.9]*4,(3,2,1,0)),("r3 q.99",[0.9,0.5,0.5,0.99],None)]:
            V,Pp,ch,conv,it=solve_chk(q,k,d,order=o)
            print(f"k={k} d={d} {lab:16s} conv={conv} it={it} V={np.round(V,3)} pie={V.sum():.3f} floor={V.min():.3f} | " + "; ".join(f"p{pr}:{x}/{tuple(c+1 for c in C)}" for pr,(_,_,x,C) in ch.items()))
E=np.vstack([E0[0],E0[1]/3,E0[1]/3,E0[1]/3,E0[2]]); S=np.array([1,1,1,1,2.0])
for kk in (5,4,2):
    V,Pp,ch,conv,it=solve_chk([0.9]*6,kk,0.8,E=E,S=S)
    print(f"sybil k={kk}/5 d=0.8 conv={conv} it={it} V={np.round(V,3)} hh2={V[2:5].sum():.3f} pie={V.sum():.3f}")
