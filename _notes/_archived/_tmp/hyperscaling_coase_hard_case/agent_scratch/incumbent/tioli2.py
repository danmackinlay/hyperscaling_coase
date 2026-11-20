import itertools, numpy as np, sys
from scipy.stats import norm
import tioli as T
from tioli import *
WF=100.0
def run2(ef=1.0,k=3,arb=False,missp=True,remed=False,outside=False,sybil=False,N=1500):
    E,S,W,hh=setup(sybil); n=len(S); Wall=np.array([WF,*W])
    fallback=6.5 if outside else 0.0
    rng=np.random.default_rng(1); xi=rng.standard_normal((N,n)); shat=S+ef*xi
    inssets=[()] if not remed else [I for r in range(n+1) for I in itertools.combinations(range(n),r)]
    need = n if k=="all" else k
    coals=[C for r in range(need,n+1) for C in itertools.combinations(range(n),r)]
    tot=np.zeros(1+n); utot=np.zeros(1+n); deals=0; condtot=np.zeros(1+n); sched={}; prop={}
    def harm_true(x,I):
        Ee=E.copy()
        for i in I: Ee[i]=Ee[i]/2
        h=S*(Ee@x)
        if arb and x[0] and x[2]: h[n-1]+=1.5
        return h,Ee
    for d in range(N):
        best=None
        for x in X:
            P=p@x
            if outside: P+=sum(p[t]-3 for t in range(4) if not x[t])
            for I in inssets:
                h,Ee=harm_true(x,I); Ex=Ee@x; mean=shat[d]*Ex
                if arb and not missp and x[0] and x[2]: mean[n-1]+=1.5
                for C in coals:
                    C=list(C); Sv=P-2*len(I)-mean[C].sum()-fallback; c=ef*Ex[C]
                    z,R,ev=margin(Sv,c)
                    if best is None or ev>best[0]: best=(ev,x,I,C,mean[C]+z*c,h)
        ev,x,I,C,t,h=best; key=(nm(x),I,tuple(C)); prop[key]=prop.get(key,0)+1
        g=np.zeros(1+n)
        if all(t[j]>=h[C[j]] for j in range(len(C))):
            deals+=1; P=p@x
            if outside: P+=sum(p[t_]-3 for t_ in range(4) if not x[t_])
            g[0]=P-2*len(I)-t.sum()-fallback
            for i in range(n): g[1+i]=-h[i]
            for j,i in enumerate(C): g[1+i]=t[j]-h[i]
            condtot+=g; sched[key]=sched.get(key,0)+1
        tot+=g
        with np.errstate(invalid="ignore",divide="ignore"): utot+=np.log(Wall+g)-np.log(Wall)
    return dict(deal=deals/N,eg=tot/N,ug=utot/N,cond=condtot/max(deals,1),sched=sorted(sched.items(),key=lambda kv:-kv[1])[:2],prop=sorted(prop.items(),key=lambda kv:-kv[1])[:2],hh=hh)
def rep2(lab,r):
    eg=r["eg"]; hh=r["hh"]; n=len(eg)-1; H=sorted(set(hh))
    agg=np.array([eg[0]]+[sum(eg[1+i] for i in range(n) if hh[i]==h) for h in H])
    uagg=np.array([r["ug"][0]]+[sum(r["ug"][1+i] for i in range(n) if hh[i]==h) for h in H])
    pie=agg.sum(); share=agg[1:].sum()/pie if pie>0 else float('nan')
    NP=lambda a: np.prod(a) if np.all(a>0) else (0.0 if np.any(a==0) else float('nan'))
    cond=r["cond"]; cagg=np.array([cond[0]]+[sum(cond[1+i] for i in range(n) if hh[i]==h) for h in H])
    top=r["prop"][0][0]
    print(f"{lab:34s} deal={r['deal']:.3f} E[gain]={np.round(agg,3)} pie={pie:.3f} resshare={share:.3f} NP={NP(agg):.4f} NPutil={NP(uagg):.3e} floor={agg.min():.3f} | cond={np.round(cagg,2)} | proposes {top[0]} ins={top[1]} coal={tuple(c+1 for c in top[2])} {r['prop'][0][1]/sum(v for _,v in r['prop']) if False else ''}")
# ---- bloc TIOLI: residents (or a sub-bloc) propose, estimating p_t with error eN
def bloc(eN=1.0,members=(0,1,2),outside=False,N=4000,split="equal"):
    rng=np.random.default_rng(2); n=3; W=np.array([WF,10,10,2.0])
    tot=np.zeros(4); utot=np.zeros(4); deals=0; cond=np.zeros(4)
    H=lambda x: S0*(E0@x)
    for d in range(N):
        phat=p+eN*rng.standard_normal(4); best=None
        for x in X:
            h=H(x); Hm=sum(h[i] for i in members)
            if outside:
                # fleet accepts iff 3*|x| >= T : known, no estimation needed
                Sv=3*x.sum()-Hm; z,R,ev=np.array([]),Sv,max(Sv,0); T=3*x.sum()
                if best is None or ev>best[0]: best=(ev,x,T,h)
            else:
                sig=eN*np.sqrt(x.sum()); Sv=phat@x-Hm
                z,R,ev=margin(Sv,[sig]); T=phat@x-z[0]*sig
                if best is None or ev>best[0]: best=(ev,x,T,h)
        ev,x,T,h=best; g=np.zeros(4)
        accept = (3*x.sum()>=T) if outside else (p@x>=T)
        if accept:
            deals+=1; g[0]=(3*x.sum()-T) if outside else (p@x-T)
            gain=T-sum(h[i] for i in members)
            for i in range(3): g[1+i]=-h[i]
            if split=="equal":
                for i in members: g[1+i]=gain/len(members)
            else:
                hm=np.array([h[i] for i in members]); wts=hm/hm.sum() if hm.sum()>0 else np.ones(len(members))/len(members)
                for j,i in enumerate(members): g[1+i]=gain*wts[j]
            cond+=g
        tot+=g
        with np.errstate(invalid="ignore",divide="ignore"): utot+=np.log(W+g)-np.log(W)
    eg=tot/N; ug=utot/N; NP=lambda a: np.prod(a) if np.all(a>0) else (0.0 if np.any(a==0) else float('nan'))
    print(f"bloc{tuple(m+1 for m in members)} e_N={eN} {split:5s} {'outside' if outside else ''} deal={deals/N:.3f} E[gain]={np.round(eg,3)} pie={eg.sum():.3f} resshare={eg[1:].sum()/eg.sum():.3f} NP={NP(eg):.4f} NPutil={NP(ug):.3e} floor={eg.min():.3f} | cond={np.round(cond/max(deals,1),2)}")
if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 1500
    print("=== remediation, k=3 ===")
    for ef in (1,0.3,0.1): rep2(f"e_f={ef} remed",run2(ef=ef,k=3,remed=True,N=N))
    print("=== outside option, k=3 (gains over fleet threat 6.5) ===")
    for ef in (1,0.3,0.1): rep2(f"e_f={ef} outside",run2(ef=ef,k=3,outside=True,N=N))
    print("=== Sybil, fleet TIOLI (household 2 aggregated) ===")
    for ef in (1,0.3,0.1): rep2(f"e_f={ef} sybil 5/5",run2(ef=ef,k="all",sybil=True,N=N))
    for ef in (1,0.3,0.1): rep2(f"e_f={ef} sybil 4/5",run2(ef=ef,k=4,sybil=True,N=N))
    for ef in (1,0.3,0.1): rep2(f"e_f={ef} sybil 2/5",run2(ef=ef,k=2,sybil=True,N=N))
    print("=== Residents' bloc TIOLI (estimates p_t), k=3 ===")
    for eN in (1,0.3,0.1): bloc(eN=eN)
    for eN in (1,0.3,0.1): bloc(eN=eN,split="harm")
    print("--- bloc of {1,2} at k=2, excluding 3 ---")
    for eN in (1,0.3,0.1): bloc(eN=eN,members=(0,1))
    print("--- outside option: fleet's willingness to pay is 3 per slot, known ---")
    bloc(eN=1,outside=True); bloc(eN=0.1,outside=True)
