import numpy as np, functools
from council import *
N=1500
def comp(sf, seed=11):
    rng=np.random.default_rng(seed); a=np.zeros(4)
    for _ in range(N): a+=company_proposal(rng, sf)
    return a/N
def res(sN, seed=12):
    rng=np.random.default_rng(seed); c=d=0
    for _ in range(N):
        ci,di=resident_proposal(rng, sN); c+=ci; d+=di
    return c/N, d/N
a0=comp(0); a1=comp(0.1)
for sN in [0.316/np.sqrt(3), 0.05, 0.02]:
    c,d=res(sN)
    for nm,a in [("sf=0",a0),("sf=0.1",a1)]:
        g=np.array([a[0]/4+3*c/4,*(a[1:]/4+d/4)])
        print(f"sN={sN:.3f} {nm}: co {g[0]:.2f} A {g[1]:.2f} B {g[2]:.2f} C {g[3]:.2f}  company excess over 1.5 {g[0]-1.5:+.2f}")
