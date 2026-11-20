import itertools, numpy as np
from scipy.optimize import minimize_scalar, minimize
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
def prof(x,opt): return p@x + opt*np.sum(np.maximum(p-3,0)*(1-x))
X=[np.array(x) for x in itertools.product([0,1],repeat=4)]
def eff(opt):
    v=[prof(x,opt)-s@(E@x) for x in X]; i=int(np.argmax(v)); return X[i], v[i]
for opt in [0,1]:
    D=opt*6.5; x,tot=eff(opt); h=s*(E@x); pie=tot-D
    print(f"\n=== option {opt}: no-deal fleet {D}, efficient road {x}, harms {h}, pie {pie}")
    # arms (gains over no deal)
    arms={}
    arms['fleet TIOLI']=np.array([pie,0,0,0])
    arms['bloc TIOLI, equal']=np.array([0,pie/3,pie/3,pie/3])
    arms['bloc TIOLI, prop harm']=np.r_[0,pie*h/h.sum()]
    arms['Nash 4-party']=np.full(4,pie/4)
    arms['Nash 2-party, bloc equal']=np.r_[pie/2,np.full(3,pie/6)]
    for k,g in arms.items():
        prod=np.prod(g); absol=g+np.r_[D,0,0,0]
        print(f"{k:28s} gains {np.round(g,3)} product {prod:.4f} floor {g.min():.3f} abs payoffs {np.round(absol,3)} res share {g[1:].sum()/pie:.2f}")
    # k=2 divide and conquer: fleet runs whatever maximises own profit at zero price
    v=[prof(x,opt) for x in X]; i=int(np.argmax(v)); x2=X[i]; h2=s*(E@x2)
    g=np.r_[prof(x2,opt)-D,-h2]
    print(f"k=2 D&C road {x2} gains {g} total {g.sum()+D - 0:.2f} (welfare {prof(x2,opt)-h2.sum():.2f} vs max {tot:.2f}) floor {g.min()}")
# wealth effects, symmetric Nash in utility, efficient schedule, transfers free
w0=np.array([100,10,10,2.])
for opt in [0,1]:
    D=opt*6.5; x,tot=eff(opt); h=s*(E@x)
    # payoffs: fleet = prof - sum t ; resident i = t_i - h_i ; no deal: fleet D, residents 0
    def negobj(t):
        pay=np.r_[prof(x,opt)-t.sum(), t-h]
        nd=np.r_[D,0,0,0]
        if np.any(w0+pay<=0): return 1e9
        g=np.log(w0+pay)-np.log(w0+nd)
        if np.any(g<=0): return 1e9
        return -np.sum(np.log(g))
    best=None
    for start in [h+tot/4 if opt==0 else h+(tot-D)/4]:
        r=minimize(negobj,start,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':20000})
    t=r.x; pay=np.r_[prof(x,opt)-t.sum(), t-h]; nd=np.r_[D,0,0,0]
    g=np.log(w0+pay)-np.log(w0+nd)
    print(f"wealth on, option {opt}: money gains {np.round(pay-nd,3)} util gains {np.round(g,5)} product {np.prod(g):.3e}")
    # compare equal-money split product in utils
    pie=tot-D; pe=nd+pie/4; ge=np.log(w0+pe)-np.log(w0+nd); print("   equal money split util product",f"{np.prod(ge):.3e}")
