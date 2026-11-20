# Independent re-derivation of headline numbers (no LP), prior s_i in {1,2} w.p. 1/2.
import itertools as it, math
p=[4,5.5,4,5]; e=[[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]
sched=list(it.product([0,1],repeat=4))
def W(x,s): return sum(p[t]*x[t] for t in range(4))-sum(s[i]*e[i][t]*x[t] for i in range(3) for t in range(4))
prof=list(it.product([1,2],repeat=3))
FB={s:max(W(x,s) for x in sched) for s in prof}
Ws=sum(FB.values())/8; print("W*",Ws, "FB(1,1,2)",FB[(1,1,2)])
# fleet-best efficient: high types at 0, low type rent = H_i(2) under rent-minimising efficient ties
def exp_i(i,x): return sum(e[i][t]*x[t] for t in range(4))
rent=[]
for i in range(3):
    tot=0
    for s in prof:
        if s[i]!=2: continue
        effs=[x for x in sched if abs(W(x,s)-FB[s])<1e-9]
        tot+=min(exp_i(i,x) for x in effs)/4
    rent.append(tot)
print("rents H_i(2):",rent,"fleet-best durable fleet:",Ws-0.5*sum(rent))
# AGV interim = E[W|s_i] + const; with equal ex ante gains Ws/4
for i in range(3):
    c={th:sum(FB[s] for s in prof if s[i]==th)/4 for th in (1,2)}
    print(f"r{i+1}: E[W|1]={c[1]}, E[W|2]={c[2]}, AGV interim (1,2)=",[round(Ws/4+c[th]-Ws,4) for th in (1,2)])
# liability status quos
for sb in (1.5,1.0):
    xL=[1 if p[t]>sb*sum(e[i][t] for i in range(3)) else 0 for t in range(4)]
    s=(1,1,2); f=sum(p[t]*xL[t] for t in range(4))-sb*sum(e[i][t]*xL[t] for i in range(3) for t in range(4))
    r=[(sb-s[i])*exp_i(i,xL) for i in range(3)]
    print("liab",sb,xL,"at true",[f]+r,"total",f+sum(r))
# Nash complete info
print("complete-info Nash 1.5^4 =",1.5**4)
# wealth-effect conversion of ex post at true
for lab,v in (("AGV veil",[0.6979,2.9896,3.3646,-1.0521]),("durable HS (wait)",[0.632,2.267,3.156,-0.055])):
    w0=[100,10,10,2]; u=[math.log((w0[k]+v[k])/w0[k]) for k in range(4)]
    print(lab,"utility gains",[round(x,4) for x in u])
# delta thresholds: shortfall/G -> delta = r/(1+r)
for lab,short,G in (("liab1.5 r3s2",0.28125,0.09375),("liab1.5 r1s2",0.15625,0.09375),("liab1.0 r3s1",0.46875,0.15625)):
    r=short/G; print(lab,"delta >=",r/(1+r))
