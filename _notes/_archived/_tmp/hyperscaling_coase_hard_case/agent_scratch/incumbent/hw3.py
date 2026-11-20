import numpy as np, itertools
from hangwen import *
def solve_range(q,k,delta,order=None,E=E0,S=S0,burn=3000,keep=400):
    n=len(q); nres=n-1
    opts=[]
    for x in X:
        h=S*(E@x); P=p@x
        for r in range(k,nres+1):
            for C in itertools.combinations(range(nres),r): opts.append((x,C,P-sum(h[i] for i in C),h))
    V=np.zeros(n); Pp=proposer_probs(q,order); hist=[]
    for it in range(burn+keep):
        newV=np.zeros(n)
        for pr in range(n):
            best=None
            for x,C,val,h in opts:
                if pr>0 and (pr-1) not in C: continue
                members=[0]+[1+i for i in C]; pay=np.zeros(n)
                for i in range(nres): pay[1+i]=-h[i]
                for m in members:
                    if m!=pr: pay[m]=delta*V[m]
                pay[pr]=val-sum(delta*V[m] for m in members if m!=pr)
                if best is None or pay[pr]>best[0]+1e-12: best=(pay[pr],pay)
            newV+=Pp[pr]*best[1]
        V=newV
        if it>=burn: hist.append(V.copy())
    h=np.array(hist); return h.min(0),h.max(0),h.mean(0)
for d in (0.5,0.8,0.95):
    for lab,q,o in [("sym 0.9",[0.9]*4,None),("fleet .9 res .5",[0.9,0.5,0.5,0.5],None),("fleet .5 res .9",[0.5,0.9,0.9,0.9],None),("fleet first",[0.9]*4,(0,1,2,3)),("r3 first",[0.9]*4,(3,2,1,0)),("r3 q.99",[0.9,0.5,0.5,0.99],None)]:
        lo,hi,mu=solve_range(q,2,d,order=o)
        print(f"k=2 d={d} {lab:16s} mean={np.round(mu,2)} range=[{np.round(lo,2)} .. {np.round(hi,2)}] pie~{mu.sum():.2f} floor<={hi.min():.2f}")
E=np.vstack([E0[0],E0[1]/3,E0[1]/3,E0[1]/3,E0[2]]); S=np.array([1,1,1,1,2.0])
for kk in (4,2):
    lo,hi,mu=solve_range([0.9]*6,kk,0.8,E=E,S=S)
    print(f"sybil k={kk}/5 d=0.8 mean={np.round(mu,2)} hh2 mean={mu[2:5].sum():.2f} range hh2=[{lo[2:5].sum():.2f}..{hi[2:5].sum():.2f}] r3 range=[{lo[5]:.2f}..{hi[5]:.2f}]")
