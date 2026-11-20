"""Arm C: sequential short-lived commitment attempts (Hang-Wen 2026 as the state describes it).
Parties attempt in an order; attempt i sticks w.p. q_i; first to stick proposes and takes the
coalition value minus discounted continuation values of included members; excluded residents get -h_i(x).
If every attempt fails, a proposer is drawn uniformly (my simplification). Stationary values by iteration.
k = residents needed (unanimity = all). Fleet is in every coalition."""
import itertools, numpy as np
p=np.array([4,5.5,4,5.0]); slots="MDEN"
E0=np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); S0=np.array([1,1,2.0])
X=[np.array(x) for x in itertools.product([0,1],repeat=4) if any(x)]
def nm(x): return "".join(c for c,b in zip(slots,x) if b)
def proposer_probs(q,order=None,orders=None):
    n=len(q); P=np.zeros(n)
    ords=[order] if order is not None else (orders if orders is not None else list(itertools.permutations(range(n))))
    for o in ords:
        surv=1.0
        for i in o: P[i]+=surv*q[i]; surv*=1-q[i]
        P+=surv/n
    return P/len(ords)
def solve(q,k,delta,order=None,E=E0,S=S0,arb=False,tol=1e-10):
    n=len(q); nres=n-1
    def harm(x):
        h=S*(E@x)
        if arb and x[0] and x[2]: h[-1]+=1.5
        return h
    opts=[]  # (x, coalition residents)
    for x in X:
        h=harm(x); P=p@x
        for r in range(k,nres+1):
            for C in itertools.combinations(range(nres),r):
                val=P-sum(h[i] for i in C); opts.append((x,C,val,h))
    V=np.zeros(n); Pp=proposer_probs(q,order)
    for it in range(5000):
        newV=np.zeros(n); choice={}
        for pr in range(n):
            best=None
            for x,C,val,h in opts:
                if pr>0 and (pr-1) not in C: continue
                members=[0]+[1+i for i in C]
                pay=np.zeros(n)
                for i in range(nres): pay[1+i]=-h[i]
                for m in members:
                    if m!=pr: pay[m]=delta*V[m]
                pay[pr]=val-sum(delta*V[m] for m in members if m!=pr)
                if best is None or pay[pr]>best[0]: best=(pay[pr],pay,nm(x),C)
            choice[pr]=best; newV+=Pp[pr]*best[1]
        if np.max(np.abs(newV-V))<tol: V=newV; break
        V=newV
    return V,Pp,choice
def rep(lab,V,Pp,choice):
    tot=V.sum(); prod=np.prod(V) if np.all(V>0) else (0.0 if np.any(V==0) else float('nan'))
    print(f"{lab:46s} P(propose)={np.round(Pp,3)} V={np.round(V,3)} pie={tot:.3f} resshare={V[1:].sum()/tot if tot else float('nan'):.3f} NP={prod:.4f} floor={V.min():.3f}")
    for pr,(_,pay,x,C) in choice.items(): print(f"      proposer {pr}: {x} coalition res{tuple(c+1 for c in C)} payoffs={np.round(pay,2)}")
if __name__=="__main__":
    for k in (3,2):
        for d in (0.5,0.8,0.95):
            print(f"\n### k={k} delta={d}")
            V,Pp,ch=solve([0.9]*4,k,d); rep("symmetric q=0.9 random order",V,Pp,ch)
            V,Pp,ch=solve([0.9,0.5,0.5,0.5],k,d); rep("fleet q=0.9, residents 0.5, random order",V,Pp,ch)
            V,Pp,ch=solve([0.5,0.9,0.9,0.9],k,d); rep("fleet q=0.5, residents 0.9, random order",V,Pp,ch)
            V,Pp,ch=solve([0.99,0.5,0.5,0.5],k,d); rep("fleet q=0.99, residents 0.5",V,Pp,ch)
            V,Pp,ch=solve([0.9]*4,k,d,order=(0,1,2,3)); rep("fleet always first, q=0.9",V,Pp,ch)
            V,Pp,ch=solve([0.9]*4,k,d,order=(3,2,1,0)); rep("resident 3 first, fleet last, q=0.9",V,Pp,ch)
            V,Pp,ch=solve([0.9,0.5,0.5,0.99],k,d); rep("resident 3 q=0.99, fleet 0.9, others 0.5",V,Pp,ch)
    print("\n### arbitrary prefs, k=3 delta=0.8")
    V,Pp,ch=solve([0.9]*4,3,0.8,arb=True); rep("symmetric q=0.9 arb",V,Pp,ch)
    V,Pp,ch=solve([0.9]*4,3,0.8,order=(0,1,2,3),arb=True); rep("fleet first arb",V,Pp,ch)
    print("\n### Sybil: resident 2 as three agents (exposure/3 each)")
    E=np.vstack([E0[0],E0[1]/3,E0[1]/3,E0[1]/3,E0[2]]); S=np.array([1,1,1,1,2.0])
    for d in (0.8,):
        V,Pp,ch=solve([0.9]*6,5,d,E=E,S=S); rep(f"sybil unanimity 5/5, q=0.9 random, d={d}",V,Pp,ch)
        print("   household 2 total:",round(V[2:5].sum(),3))
        V,Pp,ch=solve([0.9]*6,4,d,E=E,S=S); rep(f"sybil k=4/5 (one excludable), d={d}",V,Pp,ch); print("   household 2 total:",round(V[2:5].sum(),3))
        V,Pp,ch=solve([0.9]*6,2,d,E=E,S=S); rep(f"sybil k=2/5, d={d}",V,Pp,ch); print("   household 2 total:",round(V[2:5].sum(),3))
