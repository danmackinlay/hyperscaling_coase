# fleet uninformed, s_i ~ U[s_i-a, s_i+a] prior (assumed); one-shot TIOLI vs frequent-offer limit (gap case)
import numpy as np, itertools
from scipy.optimize import minimize
from base import *
from tioli import X,E
def oneshot(a):
    best=None
    for x,Ei in zip(X,E):
        act=Ei>0
        def f(tau):
            tt=np.array(s,dtype=float); tt[act]=tau
            P=np.clip((tt-(s-a))/(2*a),0,1)
            return -((p@x-(Ei*tt).sum())*np.prod(P[act]))
        bestx=None
        for st in itertools.product(*[np.linspace(si-a,si+a,9) for si in s[act]]):
            r=minimize(f,np.array(st),method='Nelder-Mead')
            if bestx is None or r.fun<bestx.fun: bestx=r
        if best is None or bestx.fun<best[0]: best=(bestx.fun,x,bestx.x,Ei,act)
    v,x,tau,Ei,act=best
    tt=np.array(s,dtype=float); tt[act]=tau
    P=np.clip((tt-(s-a))/(2*a),0,1); Pd=np.prod(P[act])
    # expected gains over prior: resident i gets (tau-s_true)E_i when all accept; E[ (tau - s)|s<=tau] = (tau-(s-a))/2
    gres=np.where(act,Pd*(tt-(s-a))/2*Ei,0)
    gf=-v
    return x,tt,Pd,gf,gres
def limit(a):
    # gap case: fleet pays the top type on the efficient schedule (check best x)
    best=max(zip(X,E),key=lambda z: z[0]@p-((s+a)*z[1]).sum())
    x,Ei=best; gf=p@x-((s+a)*Ei).sum(); gres=a*Ei
    return x,gf,gres
for a in (0.25,0.5,0.75,1.0):
    x,tt,Pd,gf,gres=oneshot(a)
    g=np.r_[gf,gres]
    xl,gfl,grl=limit(a); gl=np.r_[gfl,grl]
    print(f'a={a}: one-shot {lab(x)} deal {Pd:.3f} gains ({g[0]:.2f};{g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) NP {np.prod(g):.3f} floor {g.min():.2f} | frequent {lab(xl)} ({gl[0]:.2f};{gl[1]:.2f},{gl[2]:.2f},{gl[3]:.2f}) NP {np.prod(gl) if gl.min()>=0 else float("nan"):.3f} floor {gl.min():.2f}')
