import sys, time, itertools; sys.path.insert(0,'.')
from sim import *
# seconds per (plan step) for each planner variant, measured on one decision at H=40
rng=np.random.default_rng(0)
res={}
for margins, dyn, play, fb in itertools.product(["std","small","line"],["expected","roll1","roll5"],["sampled","expected"],["full","bandit"]):
    c=Cfg(margins=margins,dyn=dyn,play=play,feedback=fb,step=0.25)
    G=grid(c.step); lw=rng.normal(size=(3,G.size))
    t0=time.time(); n=3
    for _ in range(n): choose_margin(lw,c,G,40,rng)
    res[(margins,dyn,play,fb)]=(time.time()-t0)/n/40
for k,v in res.items(): print(k, round(v*1e3,3),'ms/step')
