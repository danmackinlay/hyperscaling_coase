# Same mechanism problem, but residual private information = uniform +-w around sbar (w = the fleet's estimation error read as a bounded posterior half-width)
import numpy as np
exec(open('mp_scale.py').read().split('for opt in [0,1]:')[0].replace('L=sbar*(1-a); U=sbar*(1+a)','L=sbar-a; U=sbar+a'))
# closed-form limits: E[virtual harm] = top of support
p=np.array([4,5.5,4,5.]); H=np.array([2.5,2,3,5.5]); Ecol=E.sum(axis=0)
for opt in [0,1]:
  V=np.minimum(p,3) if opt else p
  for w in [1.0,0.3,0.1]:
    vs=V-(H+w*Ecol)   # limit virtual surplus per slot, per replica
    eff=(V-H)>0
    print(f"opt={opt} w={w}: limit virtual surplus per slot {np.round(vs,2)}; efficient slots {eff.astype(int)}; sum over efficient {vs[eff].sum():.2f}")
    for m in [1,10,100]:
        o=run(m,w,opt,20000 if m<100 else 4000)['second-best']
        if o is None: print('   infeasible'); continue
        mm,pe,pie,mx,fg,rg=o
        print(f"   n={3*m:3d} mu={mm:.3f} P(eff sched)={pe:.3f} pie/rep {pie:.3f} of {mx:.3f} fleet {fg:.3f} res {np.round(rg,3)}")
