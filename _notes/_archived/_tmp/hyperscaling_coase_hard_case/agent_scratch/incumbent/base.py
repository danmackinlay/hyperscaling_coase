import itertools, numpy as np
p = np.array([4,5.5,4,5.0])
e = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]])
s = np.array([1,1,2.0])
R = e*s[:,None]   # per-slot harm
S = list(itertools.product([0,1],repeat=4))
names='MDEN'
def lab(x): return ''.join(n for n,b in zip(names,x) if b) or '-'
def harms(x, arb=False):
    x=np.array(x); h=R@x
    if arb and x[0] and x[2]: h=h.copy(); h[2]+=1.5
    return h
if __name__=='__main__':
    print('slot harm totals',R.sum(0),'surplus',p-R.sum(0))
    for arb in (False,True):
        best=max(S,key=lambda x: p@x-harms(x,arb).sum())
        x=best; print('arb',arb,'efficient',lab(x),'profit',p@np.array(x),'harms',harms(x,arb),'pie',p@np.array(x)-harms(x,arb).sum())
        print('  MDE pie',p@np.array([1,1,1,0])-harms((1,1,1,0),arb).sum(),' MDEN pie',p.sum()-harms((1,1,1,1),arb).sum(),' MD pie',p@np.array([1,1,0,0])-harms((1,1,0,0),arb).sum())
    # k=2 coalition values: fleet + pair, ignoring the excluded resident's harm
    for excl in range(3):
        pair=[i for i in range(3) if i!=excl]
        best=max(S,key=lambda x:(p@np.array(x)-sum(harms(x)[i] for i in pair), sum(x)))
        v=p@np.array(best)-sum(harms(best)[i] for i in pair)
        print('k=2 excl',excl+1,'best',lab(best),'value',v,'harm to excluded',harms(best)[excl])
    # fleet profit-max with zero signature price
    print('MDEN payoffs at zero price: fleet',p.sum(),'res',-harms((1,1,1,1)))
