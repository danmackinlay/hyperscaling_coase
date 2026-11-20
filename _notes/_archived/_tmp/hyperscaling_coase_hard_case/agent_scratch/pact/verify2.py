import itertools as it
p=[4,5.5,4,5]; e=[[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]
prof=list(it.product([1,2],repeat=3))
def xs(s): return [1 if p[t]-sum(s[i]*e[i][t] for i in range(3))>1e-12 else 0 for t in range(4)]
def val(k,s):
    x=xs(s); return sum(p[t]*x[t] for t in range(4)) if k==0 else -s[k-1]*sum(e[k-1][t]*x[t] for t in range(4))
def xi(k,th): return sum(sum(val(j,s) for j in range(4) if j!=k) for s in prof if s[k-1]==th)/4
xf=sum(sum(val(j,s) for j in (1,2,3)) for s in prof)/8
def pay(s):
    XI=[xf]+[xi(k,s[k-1]) for k in (1,2,3)]
    return [val(k,s)+XI[k]-sum(XI[j] for j in range(4) if j!=k)/3 for k in range(4)]
ex=[sum(pay(s)[k] for s in prof)/8 for k in range(4)]
G=sum(ex)/4; L=[G-x for x in ex]
print("AGV ex post at (1,1,2):",[round(a+b,4) for a,b in zip(pay((1,1,2)),L)])
print("budget balanced at each profile:",all(abs(sum(pay(s))-sum(val(k,s) for k in range(4)))<1e-9 for s in prof))
