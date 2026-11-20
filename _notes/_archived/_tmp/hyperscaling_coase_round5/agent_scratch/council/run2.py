import numpy as np, functools, sys
from council import *
N = int(sys.argv[1]) if len(sys.argv)>1 else 1500

@functools.lru_cache(None)
def comp(sf, prior_sd=None, grid=None, seed=11):
    rng=np.random.default_rng(seed); a=np.zeros(4); deal=0
    for _ in range(N):
        cp=company_proposal(rng, sf, prior_sd, grid); a+=cp; deal+= (np.any(cp!=0) or sf==0)
    return a/N, deal/N

@functools.lru_cache(None)
def res(sN, prior_sd=None, grid=None, seed=12):
    rng=np.random.default_rng(seed); c=d=0; deal=0
    for _ in range(N):
        ci,di=resident_proposal(rng, sN, prior_sd, grid); c+=ci; d+=di; deal+=(di>0)
    return c/N, d/N, deal/N

def combo(sf, sN, prior_sd=None, grid=None):
    a,dc=comp(sf,prior_sd,grid); c,d,dr=res(sN,prior_sd,grid)
    g=np.array([a[0]/4+3*c/4, *(a[1:]/4+d/4)])
    return g, dc/4+3*dr/4

def eff(sN, sa):  # residents combine own estimate with audit
    if sa==0 or sN==0: return 0.0
    if sa is None: return sN
    return (1/sN**2+1/sa**2)**-0.5

def line(name,g,dr):
    gm=np.prod(np.clip(g,1e-12,None))**0.25
    pos = g[1:]-ORD  # resident position against the ordinance
    print(f"{name:44s} co {g[0]:5.2f} A {g[1]:5.2f} B {g[2]:5.2f} C {g[3]:5.2f} | GM/1.5 {gm/1.5:4.2f} floor {g.min():5.2f} deal {dr:4.2f} | vs ordinance A {pos[0]:+.2f} B {pos[1]:+.2f} C {pos[2]:+.2f}")

print("== main: company 10:1 (sf=0.1, sN=0.316); council rules")
line("equal compute, full info", *combo(0,0))
line("equal compute 1:1 at 0.316", *combo(0.316,0.316))
line("equal compute 1:1 at 0.1", *combo(0.1,0.1))
line("R0 no rule, 10:1 (0.1 vs 0.316)", *combo(0.1,0.316))
line("R0 no rule, company perfect (0 vs 0.316)", *combo(0,0.316))
line("R0 no rule, 10:1 (0.316 vs 1)", *combo(0.316,1))
for sa in [0.3,0.1,0.03,0]:
    line(f"R2 open books audit sa={sa}, 10:1", *combo(0.1, round(eff(0.316,sa),4)))
for sa in [0.1,0]:
    line(f"R2 open books sa={sa}, company perfect", *combo(0, round(eff(0.316,sa),4)))
print("== company compute sweep, residents fixed sN=0.316, without / with open books (sa=0)")
for sf in [1,0.316,0.1,0.03,0]:
    line(f"no rule sf={sf}", *combo(sf,0.316))
    line(f"open books sf={sf}", *combo(sf,0))
print("== robustness: informative Gaussian prior (sd 1)")
line("R0 10:1 prior", *combo(0.1,0.316,prior_sd=1.0))
line("R2 10:1 open books prior", *combo(0.1,0,prior_sd=1.0))
line("1:1 0.316 prior", *combo(0.316,0.316,prior_sd=1.0))
print("== robustness: money grid 0.25")
line("R0 10:1 grid", *combo(0.1,0.316,grid=0.25))
line("R2 10:1 open books grid", *combo(0.1,0,grid=0.25))
line("1:1 0.316 grid", *combo(0.316,0.316,grid=0.25))
print("== robustness: seeds")
for sd in [21,31]:
    a,dc=comp(0.1,seed=sd); c,d,dr=res(0.316,seed=sd+1)
    g=np.array([a[0]/4+3*c/4,*(a[1:]/4+d/4)]); line(f"R0 10:1 seed {sd}", g, dc/4+3*dr/4)
print("== R3 assessed equal split (council estimates s and p, imposes)")
for sa in [1,0.316,0.1]:
    G=assessed(sa); m=G.mean(0)
    below=(G[:,1:]<0).mean(0); anyb=(G[:,1:]<0).any(1).mean()
    print(f"sa={sa}: mean co {m[0]:.2f} A {m[1]:.2f} B {m[2]:.2f} C {m[3]:.2f}; P(below no deal) A {below[0]:.2f} B {below[1]:.2f} C {below[2]:.2f} any {anyb:.2f}; E[min gain] {G.min(1).mean():.2f}; sd gain A {G[:,1].std():.2f} B {G[:,2].std():.2f} C {G[:,3].std():.2f}")
