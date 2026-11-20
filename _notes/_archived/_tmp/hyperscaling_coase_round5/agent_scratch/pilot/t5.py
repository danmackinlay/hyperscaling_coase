import sys, time; sys.path.insert(0,'.')
from sim import *
for c in [Cfg(res_class="L3",m=5,H=1),Cfg(res_class="L3",m=50,H=1),Cfg(res_class="L3",m=5,H=10),Cfg(res_class="REV",H=10),Cfg(res_class="REV",H=1)]:
    t0=time.time(); r=run_one((c,[1,0])); print(c.res_class,c.m,c.H,{k:np.round(v,3) for k,v in r.items()}, round(time.time()-t0,2))
