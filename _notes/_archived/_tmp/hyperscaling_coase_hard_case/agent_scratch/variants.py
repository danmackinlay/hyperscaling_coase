import sys; sys.path.insert(0, "/private/tmp/claude-501/-Users-dan-Source-livingthing/ba681c6b-2fa0-4067-ae93-aaf86e99fe48/scratchpad")
import numpy as np, budgets as B
from scipy.stats import norm
rng = np.random.default_rng(11); n=20000
# A. Fleet proposes to a BLOC responder (club accepts on its total gain; pooled error), parametric, k=3.
print("=== Fleet TIOLI against a bloc responder (club accepts on total; equal split of what it gets) ===")
for ef in B.EPS:
    noise = rng.normal(0, ef, (n,3)); shat = B.s + noise
    best=np.full(n,-np.inf); bx=np.zeros(n,int); bz=np.zeros(n)
    for xi,x in enumerate(B.SCHEDS):
        if x.sum()==0: continue
        Ex=B.E@x; sd=ef*np.linalg.norm(Ex); A=B.p@x-(shat*Ex).sum(1)
        val,z=B.bloc_offer(A,sd); upd=val>best; best[upd]=val[upd]; bx[upd]=xi; bz[upd]=z[upd]
    pay=np.zeros((n,4)); acc=np.zeros(n,bool)
    for d in range(n):
        x=B.SCHEDS[bx[d]]; Ex=B.E@x; h=B.s*Ex; sd=ef*np.linalg.norm(Ex); T=(shat[d]*Ex).sum()+sd*bz[d]
        if T>=h.sum()-1e-12:
            acc[d]=True; pay[d,0]=B.p@x-T; pay[d,1:]=(T-h.sum())/3
    vals,cnts=np.unique(bx,return_counts=True); top=np.argsort(-cnts)[:3]
    print(f"eps_f={ef:4}: {B.fmt(B.summarise(pay))} | deal {acc.mean():.3f} top[{', '.join(f'{B.NAMES[vals[i]]} {cnts[i]/n:.2f}' for i in top)}]")
# B. Liability rule: veto removed; fleet pays assessed damages shat_i*E_i(x); assessor error eps per s_i; fleet picks x on assessed harms.
print("\n=== Liability rule, damages = assessed harm (assessor error eps per s_i), no veto ===")
print("limit: fleet picks MDE, pays true harms: (6; 0,0,0) NP 0 floor 0")
for e in B.EPS:
    noise=rng.normal(0,e,(n,3)); shat=B.s+noise
    vals=np.array([B.p@x-(shat*(B.E@x)).sum(1) for x in B.SCHEDS]).T  # (n,16)
    bx=vals.argmax(1); pay=np.zeros((n,4))
    for d in range(n):
        x=B.SCHEDS[bx[d]]; Ex=B.E@x; pay[d,0]=B.p@x-(shat[d]*Ex).sum(); pay[d,1:]=noise[d]*Ex
    sm=B.summarise(pay); g=sm['gains']
    Nrun=np.mean([B.SCHEDS[i][3]==1 for i in bx]); eff=np.mean([B.NAMES[i]=='MDE' for i in bx])
    pie=np.mean([B.p@B.SCHEDS[i]-(B.s*(B.E@B.SCHEDS[i])).sum() for i in bx])
    worst=np.mean(pay[:,1:].min(1)); below=np.mean(pay[:,1:].min(1)<0)
    print(f"eps={e:4}: gains ({g[0]:.2f}; {g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) pie {pie:.2f} N runs {Nrun:.3f} MDE {eff:.3f} E[worst resident] {worst:.2f} P(someone<0) {below:.3f}")
# C. Wealth-effects limit products for reference
W0=B.W0; lim=np.array([1.5,1.5,1.5,1.5]); u=np.log(W0+lim)-np.log(W0); print("\nlog-utility NP at the symmetric limit 1.5 each:", np.prod(u))
