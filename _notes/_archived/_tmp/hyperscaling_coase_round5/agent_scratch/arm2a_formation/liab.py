import numpy as np, itertools
P=np.array([4,5.5,4,5]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2])
XS=np.array(list(itertools.product([0,1],repeat=4)))
for seed in (1,2):
    rng=np.random.default_rng(seed); res=[]; pr=[]
    for _ in range(20000):
        sh=s+rng.normal(0,0.3,3)
        dam=(sh[:,None]*E)@XS.T  # 3 x 16
        val=XS@P - dam.sum(0); j=int(np.argmax(val)); x=XS[j]
        res.append(sh*(E@x)-s*(E@x)); pr.append(val[j])
    res=np.array(res); print(seed, "principal",round(np.mean(pr),3),"resident mean",res.mean(0).round(3),"P(below0)",(res<0).mean(0).round(3), "E[min resident]",res.min(1).mean().round(3))
