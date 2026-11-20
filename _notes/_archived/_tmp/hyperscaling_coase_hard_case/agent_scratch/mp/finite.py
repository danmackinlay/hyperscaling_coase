# Finite budgets, fleet TIOLI (fleet estimates s_i with error sig) and bloc TIOLI (bloc estimates p_t with error sig), k=3,
# parametric, once, linear, enforcer, closed; option off/on. Expected gains count failed deals as zero.
import itertools, numpy as np
from scipy.stats import norm
from scipy.optimize import minimize
rng=np.random.default_rng(0)
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
X=[np.array(x) for x in itertools.product([0,1],repeat=4)]
def prof(x,opt,pp=p): return pp@x + opt*np.sum(np.maximum(pp-3,0)*(1-x))
def g_opt(A,c):
    # max_z prod Phi(z_i) (A - sum c_i z_i) over residents with c_i>0
    c=c[c>0]
    if len(c)==0: return max(A,0),np.array([])
    f=lambda z: -np.prod(norm.cdf(z))*(A-np.sum(c*z))
    best=(0.0,None)
    for z0 in [0.0,1.0,2.0]:
        r=minimize(f,np.full(len(c),z0),method='Nelder-Mead',options={'xatol':1e-6,'fatol':1e-9})
        if -r.fun>best[0]: best=(-r.fun,r.x)
    return best
N=4000
for sig in [1,0.3,0.1]:
  for opt in [0,1]:
    D=opt*6.5
    # precompute g_R(A) on grid
    Ag=np.linspace(-15,20,141); tab={}
    for j,x in enumerate(X):
        c=sig*(E@x)
        vals=[];zs=[]
        for A in Ag:
            v,z=g_opt(A,c); vals.append(v); zs.append(z)
        tab[j]=(np.array(vals),zs,c)
    G=np.zeros(4); eff=0; deal=0; prodsum=0
    for n in range(N):
        sh=s+sig*rng.standard_normal(3)
        best=(0,None,None)
        for j,x in enumerate(X):
            Ex=E@x; A=prof(x,opt)-D-sh@Ex
            vals,zs,c=tab[j]; k=int(np.clip(np.round((A+15)/(35/140)),0,140))
            if vals[k]>best[0]: best=(vals[k],j,zs[k])
        if best[1] is None: continue
        x=X[best[1]]; Ex=E@x; c=sig*Ex; o=sh*Ex; z=best[2]
        o=o.copy(); idx=np.where(c>0)[0]; o[idx]+=c[idx]*z
        if np.all(o>=s*Ex-1e-12):
            deal+=1; G+=np.r_[prof(x,opt)-D-o.sum(), o-s*Ex]; eff+=prof(x,opt)-s@Ex-D
    G/=N; pie=6.0 if opt==0 else 1.5
    print(f"fleet TIOLI sig={sig} opt={opt}: deal {deal/N:.3f} realised pie {eff/N:.3f} of {pie} exp gains {np.round(G,3)} product {np.prod(G):.4f} floor {G.min():.3f}")
# bloc TIOLI: bloc estimates p_t; posterior p_t ~ N(phat, sig^2); bloc proposes road set R and demand T (net of nothing: fleet pays T total, split equal)
for sig in [1,0.3,0.1]:
  for opt in [0,1]:
    D=opt*6.5; G=np.zeros(4); deal=0; eff=0
    for n in range(N):
        ph=p+sig*rng.standard_normal(4)
        sims=ph+sig*rng.standard_normal((400,4))  # posterior draws
        best=(0,None,None)
        for x in X:
            if x.sum()==0: continue
            H=s@(E@x)
            wtp=sims@x - (opt*np.sum(np.maximum(sims-3,0)*x,axis=1))  # road value minus reroute value forgone
            Ts=np.linspace(H,H+15,151)
            ev=[(np.mean(wtp>=T))*(T-H) for T in Ts]; k=int(np.argmax(ev))
            if ev[k]>best[0]: best=(ev[k],x,Ts[k])
        if best[1] is None: continue
        x,T=best[1],best[2]; H=s*(E@x)
        truewtp=p@x - opt*np.sum(np.maximum(p-3,0)*x)
        if truewtp>=T:
            deal+=1; G+=np.r_[truewtp-T, np.full(3,(T-H.sum())/3)]; eff+=truewtp-H.sum()
    G/=N; pie=6.0 if opt==0 else 1.5
    print(f"bloc TIOLI sig={sig} opt={opt}: deal {deal/N:.3f} realised pie {eff/N:.3f} of {pie} exp gains {np.round(G,3)} product {np.prod(G):.5f} floor {G.min():.3f}")
