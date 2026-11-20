import time, sys
sys.path.insert(0, '.')
from sim import *
print(efficient_schedule())
for H in [1, 10]:
    c = Cfg(H=H)
    t0=time.time(); r = run_L1(c, 1); print(H, r, time.time()-t0)
c = Cfg(res_class="L0"); print(run_L0(c,1)); print(run_L0(replace(c,l0_proposer="literal"),1))
