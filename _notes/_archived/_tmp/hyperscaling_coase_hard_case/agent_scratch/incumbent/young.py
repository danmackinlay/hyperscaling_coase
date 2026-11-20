# Young (1993) adaptive play, two-class Nash demand game: fleet vs residents' bloc, pie 6 on a grid of 12 (step 0.5)
import numpy as np, math
n=12; xs=np.arange(1,n)/n   # fleet share
def r(i,j,sF,sB):
    x,y=xs[i],xs[j]
    if y<x: return min(math.ceil(sF*(x-y)/x-1e-12), math.ceil(sB*(1-x)/(1-y)-1e-12))
    return min(math.ceil(sB*(y-x)/(1-x)-1e-12), math.ceil(sF*x/y-1e-12))
def stationary(sF,sB,eps):
    m=len(xs); P=np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            if i!=j: P[i,j]=eps**r(i,j,sF,sB)
        P[i,i]=1-P[i].sum()
    w,v=np.linalg.eig(P.T); k=np.argmin(abs(w-1)); pi=np.real(v[:,k]); pi/=pi.sum()
    return pi
def exitres(i,sF,sB): return min(r(i,j,sF,sB) for j in range(len(xs)) if j!=i)
for sF,sB in [(10,10),(20,10),(10,20),(30,10),(10,30),(20,20),(40,40)]:
    pi=stationary(sF,sB,0.02); mode=xs[np.argmax(pi)]*6
    mean=(pi*xs).sum()*6
    print(f'sF={sF} sB={sB}: long-run mode fleet {mode:.2f} of 6 (mean {mean:.2f}); predicted sF/(sF+sB)*6={6*sF/(sF+sB):.2f}; exit resistance from fleet=5 of 6: {exitres(9,sF,sB)}, from fleet=3: {exitres(5,sF,sB)}, from fleet=1: {exitres(1,sF,sB)}')
