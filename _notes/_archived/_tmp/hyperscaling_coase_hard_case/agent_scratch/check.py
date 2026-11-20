import numpy as np, math, itertools
W0=np.array([10.,10.,2.]); WF=100.
P=np.array([4,5.5,4,5.]); E=np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); S=np.array([1,1,2.])
def harms(x): return S*(E@x)
def profit(x): return float(P@x)
# A, residents hold right, MDE: grid over money to residents, fleet gets rest
x=np.array([1,1,1,0]); h=harms(x); pi=profit(x)-h.sum()
best=(-1e9,None)
g=np.arange(0.9,2.0,0.005)
for m1 in g:
  for m2 in g:
    for m3 in g:
      mf=pi-m1-m2-m3
      if mf<=0: continue
      v=math.log(math.log(1+mf/WF))+math.log(math.log(1+m1/W0[0]))+math.log(math.log(1+m2/W0[1]))+math.log(math.log(1+m3/W0[2]))
      if v>best[0]: best=(v,(mf,m1,m2,m3))
print("A MDE grid:",best)
# FOC check
mf,m1,m2,m3=best[1]
print("FOC ratios", [(1/(WF+mf))/math.log(1+mf/WF)]+[(1/(W0[i]+m))/math.log(1+m/W0[i]) for i,m in enumerate((m1,m2,m3))])
# B, residents hold right: grid for D and MD
def Bval(x,t):
    hu=harms(x)/W0; mf=profit(x)-t.sum()
    if mf<=0: return -1e9
    gs=[math.log(1+mf/WF)]+list(np.log(1+t/W0)-hu)
    if min(gs)<=0: return -1e9
    return sum(math.log(a) for a in gs)
for xs,x in (("D",np.array([0,1,0,0])),("MD",np.array([1,1,0,0])),("M",np.array([1,0,0,0])),("DE",np.array([0,1,1,0]))):
    hu=harms(x)/W0; wta=W0*(np.exp(hu)-1); slack=profit(x)-wta.sum()
    best=(-1e9,None)
    for a in np.linspace(0,1,41):
      for b in np.linspace(0,1,41):
        for c in np.linspace(0,1,41):
          if a+b+c>=1: continue
          t=wta+slack*np.array([a,b,c])
          v=Bval(x,t)
          if v>best[0]: best=(v,t,profit(x)-t.sum())
    print("B",xs,"grid logprod",round(best[0],4),"t",np.round(best[1],3),"fleet",round(best[2],3))
# Monte Carlo flip probabilities
rng=np.random.default_rng(0)
for e in (1.0,0.3,0.1):
    eps=rng.normal(0,e,size=(400000,3))
    est_h=(S+eps)@E   # estimated total harm per slot
    surplus=P-est_h
    print(e,"P(N included)",(surplus[:,3]>0).mean(),"P(E dropped)",(surplus[:,2]<0).mean(),"P(M dropped)",(surplus[:,0]<0).mean())
# ruin probability for resident 3 if paid fleet's estimate of her harm +1.5, MDE and MDEN
for e in (1.0,0.3,0.1):
    eps=rng.normal(0,e,size=400000)
    for xs,expo in (("MDE",2.0),("MDEN",4.0)):
        shortfall=-eps*expo   # true - estimated harm = -eps*exposure
        print(e,xs,"P(ruin: shortfall>3.5)",(shortfall>3.5).mean())
