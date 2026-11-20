import sys, time; sys.path.insert(0,'.')
from sim import *
for c in [Cfg(H="T"), Cfg(H=10,dyn="roll1"), Cfg(H=10,dyn="roll5"), Cfg(H=10,margins="line"), Cfg(H=10,margins="small"),
          Cfg(H=10,feedback="bandit"), Cfg(H=10,play="expected"), Cfg(H=10,play="expected",feedback="bandit"), Cfg(H=10, eta=0.5, scale=4, step=1)]:
    t0=time.time(); r=run_L1(c,1); print({k:v for k,v in c.__dict__.items() if v!=Cfg().__dict__[k]}, {k:np.round(v,3) for k,v in r.items()}, round(time.time()-t0,2))
