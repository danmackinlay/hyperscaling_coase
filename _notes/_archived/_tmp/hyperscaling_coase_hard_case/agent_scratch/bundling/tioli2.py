# Fleet take-it-or-leave-it under finite estimation budgets (parametric; k=3; once; linear money; enforcer; closed).
# Fleet sees shat_i = s_i + eps_i, eps~N(0,tau^2); flat prior => s_i|shat ~ N(shat_i,tau^2).
# Offer for schedule x to resident i: shat_i*E_i + M_i (money markup); accept iff >= s_i*E_i, i.e. M_i >= -eps_i*E_i.
# Fleet maximises prod_i Phi(M_i/sig_i) * (S - sum M_i), sig_i = tau*E_i, S = p.x - shat.E.
# FOC: lambda(M_i/sig_i)/sig_i = 1/R with R the margin, lambda = phi/Phi; solved on a grid in R, inverted in S.
# BUNDLE: fleet picks the best of 15 schedules. SLOTS: an independent offer per slot (k=3 per slot).
import itertools, numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
p=np.array([4,5.5,4,5.]); e=np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s=np.array([1,1,2.])
X=[np.array(x) for x in itertools.product([0,1],repeat=4) if any(x)]
from scipy.special import erfcx
lam=lambda z: np.sqrt(2/np.pi)/erfcx(-z/np.sqrt(2))
def zinv(c):  # solve lam(z)=c
    return brentq(lambda z: lam(z)-c, -(c+10), 40)
Rgrid=np.concatenate([np.geomspace(1e-6,1e-2,200),np.linspace(1e-2,30,4000)])
def table(sig):
    idx=[i for i in range(3) if sig[i]>0]
    M=np.zeros((len(Rgrid),3))
    for k,R in enumerate(Rgrid):
        for i in idx: M[k,i]=sig[i]*zinv(sig[i]/R)
    S=Rgrid+M.sum(1)
    V=Rgrid*np.prod([norm.cdf(M[:,i]/sig[i]) for i in idx],axis=0)
    return S,M,V
def plan(tables, Svec):
    """for each draw, value and markups at given S (interp); value 0 if S below table"""
    S,M,V=tables
    val=np.interp(Svec,S,V,left=0.0)
    Ms=np.stack([np.interp(Svec,S,M[:,i]) for i in range(3)],1)
    return val,Ms
def run(tau,n=200000,seed=7):
    rng=np.random.default_rng(seed); eps=rng.normal(0,tau,(n,3)); sh=s+eps
    T=[table(tau*(e@x)) for x in X]
    vals=[];Mss=[]
    for x,tb in zip(X,T):
        E=e@x; Sv=p@x-sh@E; v,Ms=plan(tb,Sv); vals.append(v);Mss.append(Ms)
    vals=np.stack(vals,1); best=vals.argmax(1); offer=vals.max(1)>0
    out=np.zeros((n,4)); pie=np.zeros(n); deal=np.zeros(n,bool)
    for j,x in enumerate(X):
        sel=offer&(best==j)
        if not sel.any(): continue
        E=e@x; M=Mss[j][sel]
        acc=np.all((M>=-eps[sel]*E)|(E==0),1)
        rows=np.where(sel)[0][acc]; Ma=M[acc]
        pay=sh[rows]*E+Ma
        out[rows,0]=p@x-pay.sum(1); out[rows,1:]=pay-s*E; pie[rows]=p@x-s@E; deal[rows]=True
    oB=out.mean(0); exB=np.array([out[deal].min(1).mean()]) if deal.any() else 0
    # slots
    outS=np.zeros((n,4)); pieS=np.zeros(n); runs=np.zeros(4)
    for t in range(4):
        x=np.zeros(4); x[t]=1; j=[k for k,xx in enumerate(X) if (xx==x).all()][0]
        E=e[:,t]; v=vals[:,j]; M=Mss[j]; sel=v>0
        acc=sel&np.all((M>=-eps*E)|(E==0),1)
        pay=sh*E+M
        outS[acc,0]+=p[t]-pay[acc].sum(1); outS[acc,1:]+=pay[acc]-s*E; pieS[acc]+=p[t]-s@E; runs[t]=acc.mean()
    oS=outS.mean(0)
    f=lambda o: '(%.3f; %.3f, %.3f, %.3f)  product %.4f  floor %.3f  residents %.3f (share %.3f)'%(o[0],o[1],o[2],o[3],np.prod(o),o.min(),o[1:].sum(),o[1:].sum()/max(o.sum(),1e-9))
    print('tau=%.2f BUNDLE: deal rate %.4f, E[pie] %.3f, %s'%(tau,deal.mean(),pie.mean(),f(oB)))
    sched={}
    for j,x in enumerate(X):
        c=(offer&(best==j)).mean()
        if c>0.01: sched[''.join('MDEN'[t] for t in range(4) if x[t])]=round(c,3)
    print('          bundle schedule offered:',sched)
    print('          SLOTS : run rates M,D,E,N %s, E[pie] %.3f, %s'%(np.round(runs,4),pieS.mean(),f(oS)))
    allrun=(outS!=0).any(1).mean()
for tau in (1.0,0.3,0.1,0.01): run(tau)
