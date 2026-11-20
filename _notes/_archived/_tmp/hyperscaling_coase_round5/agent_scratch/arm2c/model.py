"""Arm 2c (two neighbourhoods competing) and its climb.

Base triple: exposures e, sensitivities s, profits p. Protocol T, k=3 per street.
Principal offers every street a schedule and payments; contracts with the street
that accepts at the lowest total payment, ties by lot.

Climb: residents' agents commit to the fair share d (default 1.5 = pie/4) with
reliability q per period (commitment dial); the principal has reach K streets.
Principal's policy: for each street, offer 'low' (gain 0, i.e. pay harm) or
'high' (gain d each, pay harm + 3d); chosen to maximise expected profit by
enumeration. Residents' commitment failures independent per resident unless
corr='street'.
"""
import itertools, math, random, statistics
import numpy as np

E = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]])
P = np.array([4,5.5,4,5])
S_BASE = np.array([1,1,2])
SCHEDS = [np.array(x) for x in itertools.product([0,1],repeat=4)]

def harms(x, s):
    return s * (E @ x)

def efficient(s):
    best=None
    for x in SCHEDS:
        pie = P@x - harms(x,s).sum()
        if best is None or pie>best[0]: best=(pie,x)
    pie,x=best
    return pie, x, harms(x,s), P@x

def ordinance(s):
    x=np.array([1,1,1,0]); return P@x, -harms(x,s)

def liability_positions(s, sigma=0.3, n=20000, rng=None, K=1):
    """Principal picks (street, schedule) maximising profit net of assessed damages;
    pays assessed damages. Returns mean resident positions (per street slot) and principal."""
    rng = rng or np.random.default_rng(1)
    res=np.zeros((K,3)); prin=0.0
    for _ in range(n):
        shat=[s+rng.normal(0,sigma,3) for _ in range(K)]
        best=None
        for k in range(K):
            for x in SCHEDS:
                net=P@x-(shat[k]*(E@x)).sum()
                if best is None or net>best[0]: best=(net,k,x)
        net,k,x=best
        prin+=net
        res[k]+= shat[k]*(E@x) - harms(x,s)
    return res/n, prin/n

def principal_policy(K, q, d, s_list, corr='resident'):
    """Enumerate low/high per street. Returns best policy and expected takes.
    s_list: list of K sensitivity vectors. A 'low' offer to street k pays harm_k (gain 0),
    accepted iff all three commitments fail that period (prob a_k).
    A 'high' offer pays harm_k + 3d (gain d each), always accepted.
    Contract goes to lowest accepted total; ties by lot."""
    piefx=[efficient(s) for s in s_list]
    a = (1-q)**3 if corr=='resident' else (1-q)
    best=None
    for pol in itertools.product(['L','H'],repeat=K):
        # enumerate acceptance patterns of low streets
        lows=[k for k in range(K) if pol[k]=='L']; highs=[k for k in range(K) if pol[k]=='H']
        exp_prin=0.0; exp_res=np.zeros((K,3)); p_deal=0.0
        for acc in itertools.product([0,1],repeat=len(lows)):
            pr=1.0
            for ac in acc: pr*= a if ac else (1-a)
            cands=[]  # (total payment, street, gains vector, profit)
            for i,k in enumerate(lows):
                if acc[i]:
                    pie,x,h,prof=piefx[k]; cands.append((h.sum(),k,np.zeros(3),prof-h.sum()))
            for k in highs:
                pie,x,h,prof=piefx[k]; cands.append((h.sum()+3*d,k,np.full(3,d),prof-h.sum()-3*d))
            if not cands: continue
            m=min(c[0] for c in cands); win=[c for c in cands if abs(c[0]-m)<1e-12]
            for c in win:
                w=pr/len(win); exp_prin+=w*c[3]; exp_res[c[1]]+=w*c[2]; p_deal+=w
        if best is None or exp_prin>best[0]+1e-12:
            best=(exp_prin,pol,exp_res,p_deal)
    return best

def criterion(gains):
    g=np.array(gains); pos=g[g>1e-12]
    gm = math.exp(np.log(pos).mean()) if len(pos) else 0.0
    return gm, len(pos), (g<=1e-12).mean()

def report(K,q,d,s_list,corr='resident',label=''):
    prin,pol,res,p_deal=principal_policy(K,q,d,s_list,corr)
    pies=[efficient(s)[0] for s in s_list]
    allg=[prin]+list(res.flatten())
    gm,npos,frac=criterion(allg)
    gm_res,_,frac_res=criterion(res.flatten())
    n_parties=3*K+1
    # max GM at that n: equal split of expected realised pie
    exp_pie=prin+res.sum()
    gm_max=exp_pie/n_parties if exp_pie>0 else float('nan')
    floor=min(allg)
    print(f"{label} K={K} q={q} d={d} corr={corr} pol={''.join(pol)} | pies={np.round(pies,2)} "
          f"| prin={prin:.3f} res_total={res.sum():.3f} share={res.sum()/max(exp_pie,1e-9):.3f} "
          f"| GM+={gm:.3f}/{npos} frac_res<=0={frac:.2f} GMmax={gm_max:.3f} floor={floor:.2f} Pdeal={p_deal:.3f}")
    return dict(K=K,q=q,d=d,prin=prin,res=res,share=res.sum()/max(exp_pie,1e-9),pol=pol,p_deal=p_deal)

if __name__=='__main__':
    s=S_BASE
    pie,x,h,prof=efficient(s)
    print("base: pie",pie,"sched",x,"harms",h,"profit",prof)
    print("ordinance:",ordinance(s))
    # 1. Arm 2c as written: L0 residents = q=0 (commitments never stick) or d=0
    print("\n== Arm 2c as written (L0, base sens, K=2) ==")
    report(2,0.0,1.5,[s,s],label='2c')
    report(1,0.0,1.5,[s],label='1 street L0')
    print("\n== Climb: club agent d=1.5 with reliability q, reach K ==")
    for q in [0.3,0.5,0.75,0.9,1.0]:
        for K in [1,2,3,5]:
            report(K,q,1.5,[s]*K)
    print("\n== Incidental: demand level d ==")
    for d in [0.5,1.0,1.5]:
        for K in [1,2,3,5]:
            report(K,0.5,d,[s]*K)
    print("\n== Incidental: correlation of commitment failure (street-level) ==")
    for K in [1,2,3,5]:
        report(K,0.5,1.5,[s]*K,corr='street')
    for K in [1,2,3,5]:
        report(K,0.75,1.5,[s]*K,corr='street')
    print("\n== Liability rule status quo (base sens) ==")
    for K in [1,2]:
        r,pr=liability_positions(s,K=K)
        print(f"K={K} resident positions per street {np.round(r,3)} principal {pr:.3f}")
