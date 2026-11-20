import itertools, numpy as np
from scipy.optimize import linprog
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
S=[np.array(x) for x in itertools.product([0,1],repeat=4)]
name=lambda x:''.join(c for c,b in zip('MDEN',x) if b) or '-'
def harms(x,arb):
    h=s*(E@x)
    if arb and x[0] and x[2]: h=h.copy(); h[2]+=1.5
    return h
for arb in (0,1):
    rows=sorted(((p@x-harms(x,arb).sum(),name(x),p@x,harms(x,arb)) for x in S),key=lambda r:-r[0])
    print('arb' if arb else 'par', [(n,round(w,2)) for w,n,_,_ in rows[:5]])
    w,n,pr,h=rows[0]; g=w/4; print('  opt',n,'profit',pr,'harms',h,'pie',w,'Nash equal',g,'product',g**4)
# parametric schedule under arbitrary truth
x=np.array([1,1,1,0]); print('MDE under arb: pie',p@x-harms(x,1).sum())
# resident 3 shading scalar s3' (parametric message space), Nash split on reported pie
def shade(r):
    ss=s.copy(); ss[2]=r
    best=max(S,key=lambda x:(p@x-(ss*(E@x)).sum()))
    rep=ss*(E@best); P=p@best-rep.sum(); true=harms(best,1)
    gains=np.r_[P/4, rep-true+P/4]; return name(best),gains
for r in (2,3.01,4,4.99,6,8.99):
    n,g=shade(r); print('s3 report',r,n,g.round(3),'pie',g.sum().round(3),'prod',np.prod(g).round(4) if (g>=0).all() else 'undef','floor',g.min().round(3))
# Lindahl: personalized per-slot prices tau[i,t] supporting MD (arb). Fleet pays sum_i tau_it per slot used.
# need each party's chosen schedule = MD among all 16. Feasibility LP.
opt=np.array([1,1,0,0]); A=[];b=[]
nv=12
for x in S:
    d=x-opt
    if not d.any(): continue
    # fleet: (p - sum_i tau_i)·x <= same at opt  -> p·d - sum_i tau_i·d <= 0
    row=np.zeros(nv)
    for i in range(3): row[i*4:(i+1)*4]=-d
    A.append(row); b.append(-(p@d))
    for i in range(3):
        # resident i: tau_i·x - h_i(x) <= tau_i·opt - h_i(opt)
        row=np.zeros(nv); row[i*4:(i+1)*4]=d
        A.append(row); b.append(harms(x,1)[i]-harms(opt,1)[i])
res=linprog(np.zeros(nv),A_ub=A,b_ub=b,bounds=[(None,None)]*nv)
print('linear per-slot Lindahl prices supporting MD exist?',res.status==0, res.x.round(2) if res.status==0 else res.message)
# also check: parametric case MDE
opt=np.array([1,1,1,0]); A=[];b=[]
for x in S:
    d=x-opt
    if not d.any(): continue
    row=np.zeros(nv)
    for i in range(3): row[i*4:(i+1)*4]=-d
    A.append(row); b.append(-(p@d))
    for i in range(3):
        row=np.zeros(nv); row[i*4:(i+1)*4]=d
        A.append(row); b.append(harms(x,0)[i]-harms(opt,0)[i])
res=linprog(np.zeros(nv),A_ub=A,b_ub=b,bounds=[(None,None)]*nv)
print('parametric MDE Lindahl exists?',res.status==0, res.x.round(2) if res.status==0 else '')
