# Divide and conquer by contingent offers (Winter 2004 / Segal 2003) on the noise schedule.
# Company proposes take-it-or-leave-it contracts to each resident; executes schedule x iff >= k sign.
# Resident agent types: adaptive (prob q, best-replies; signs any contract under which signing is dominant)
# or rigid pact-holder (signs only contract F, paying h_i(x)+prem).  Menu per resident:
#  N: not approached. F: pay h_i+prem on execution. H: pay h_i+eps on execution (flat).
#  C: pay h_i+eps if executed with exactly k signers incl. i (pivotal), eps if more sign (contingent).
# Signing fee eps paid on signing regardless, so dominance is strict.
import itertools, math
p=[4,5.5,4,5]; e=[[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]; s=[1,1,2]
X=list(itertools.product([0,1],repeat=4))
def h(i,x): return s[i]*sum(e[i][t]*x[t] for t in range(4))
def prof(x): return sum(p[t]*x[t] for t in range(4))
EPS=0.01
def adaptive_signs(c,k):  # is signing (weakly+eps) dominant for an adaptive agent under contract c?
    if c=='N': return False
    if c in ('F','H'): return True
    if c=='C': return True   # pivotal: h+eps-h>0; non-pivotal executed: eps-h vs -h; fail: eps vs 0
def pay(c,i,x,nsign,k,prem):
    if c=='F': return h(i,x)+prem
    if c=='H': return h(i,x)+EPS
    if c=='C': return h(i,x)+EPS if nsign==k else EPS
def evaluate(x,menu,q,k,prem,corr):
    # returns expected (company, r1,r2,r3)
    if corr: types=[((1,)*3,q),((0,)*3,1-q)]
    else: types=[(t,math.prod(q if a else 1-q for a in t)) for t in itertools.product([0,1],repeat=3)]
    E=[0,0,0,0]
    for t,pr in types:
        if pr==0: continue
        sign=[ (menu[i]=='F') or (t[i] and adaptive_signs(menu[i],k)) for i in range(3)]
        ns=sum(sign); ex=ns>=k
        comp=-EPS*ns; r=[EPS if sign[i] else 0 for i in range(3)]
        if ex:
            comp+=prof(x)
            for i in range(3):
                r[i]-=h(i,x)
                if sign[i]:
                    py=pay(menu[i],i,x,ns,k,prem); r[i]+=py; comp-=py
        E[0]+=pr*comp
        for i in range(3): E[i+1]+=pr*r[i]
    return E
def best(q,k,prem,corr,allowed='NFHC'):
    bestv=(0,None,None,[0,0,0,0])
    for x in X:
        for menu in itertools.product(allowed,repeat=3):
            E=evaluate(x,menu,q,k,prem,corr)
            if E[0]>bestv[0]+1e-9: bestv=(E[0],x,menu,E)
    return bestv
def sched(x): return ''.join(n for n,v in zip('MDEN',x) if v) if x else '-'
def criterion(E):
    g=E  # gains over no deal
    if min(g)<-1e-9:
        return 'losers: worst %.2f, frac residents below %.2f'%(min(g),sum(1 for v in g[1:] if v< -1e-9)/3)
    pos=[v for v in g if v>1e-9]
    gm=math.prod(pos)**(1/len(pos)) if pos else 0
    return 'no losers: GM %.3f (%d positive), /max %.3f'%(gm,len(pos),gm/1.5)
SQ=[13.5,-1,-2.5,-4]
import sys
if __name__=='__main__':
    for k in (3,2):
      for corr in (False,True):
        for prem in (0.5,1.5,3.0):
          print(f'--- k={k} prem={prem} types={"correlated" if corr else "independent"}')
          prev=None
          for q in [0,0.25,0.5,0.75,0.9,1.0]:
            v,x,menu,E=best(q,k,prem,corr)
            print(f'q={q:.2f} sched={sched(x):5s} menu={"".join(menu) if menu else "-"} co={E[0]:6.2f} A={E[1]:6.2f} B={E[2]:6.2f} C={E[3]:6.2f} sumR={sum(E[1:]):6.2f} vsSQ=({E[1]-SQ[1]:+.2f},{E[2]-SQ[2]:+.2f},{E[3]-SQ[3]:+.2f}) | {criterion(E)}')
