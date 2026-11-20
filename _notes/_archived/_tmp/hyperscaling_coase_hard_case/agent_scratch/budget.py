import itertools, math, random
random.seed(1)
p=[4,5.5,4,5]; e=[[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]; s=[1,1,2]
X=list(itertools.product([0,1],repeat=4))
def hp(i,x,si): return si*sum(e[i][t]*x[t] for t in range(4))
def ha(i,x): 
    v=hp(i,x,s[i]); 
    if i==2 and x[0] and x[2]: v+=1.5
    return v
def profit(x): return sum(p[t]*x[t] for t in range(4))
# Protocol (parametric standard form, fleet proposes, k=3): fleet estimates s_i with error err,
# picks the schedule maximising estimated surplus (per-slot comparison), offers each resident
# estimated harm + 1/4 of estimated pie (the Nash split on its estimates); each resident accepts
# iff offer >= true harm; any refusal = no deal, everyone 0. Residents' estimate of p is idle here.
def run(err, truth, N=200000):
    h = (lambda i,x: hp(i,x,s[i])) if truth=="param" else ha
    tot=[0.0]*4; deals=0; pie=0.0; floor=0.0; logs=0.0; nprod=0
    for _ in range(N):
        sh=[s[i]+random.gauss(0,err) for i in range(3)]
        x=tuple(int(p[t]-sum(sh[i]*e[i][t] for i in range(3))>0) for t in range(4))
        if sum(x)==0: continue
        Hh=[hp(i,x,sh[i]) for i in range(3)]; pieh=profit(x)-sum(Hh)
        if pieh<=0: continue
        T=[Hh[i]+pieh/4 for i in range(3)]
        H=[h(i,x) for i in range(3)]
        if all(T[i]>=H[i] for i in range(3)):
            deals+=1; g=[profit(x)-sum(T)]+[T[i]-H[i] for i in range(3)]
            for j in range(4): tot[j]+=g[j]
            pie+=sum(g); floor+=min(g)
    Eg=[v/N for v in tot]
    prod=math.prod(Eg) if min(Eg)>=0 else float('nan')
    return deals/N, Eg, pie/N, prod, floor/N
for truth in ("param","arb"):
    print("truth:",truth)
    for err in (1.0,0.3,0.1,0.03,0.0):
        d,Eg,pie,prod,fl=run(err,truth, N=200000 if err>0 else 1)
        res=sum(Eg[1:])
        print(f"  err={err}: deal rate {d:.3f}, E gains (f;r1,r2,r3)={[round(v,3) for v in Eg]}, E pie {pie:.3f}, residents' share {res/pie if pie else float('nan'):.3f}, product of E gains {prod:.4f}, E floor {fl:.3f}")
