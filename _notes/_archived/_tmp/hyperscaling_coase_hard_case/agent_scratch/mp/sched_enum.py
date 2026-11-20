import itertools, math
import numpy as np
p=np.array([4,5.5,4,5.]); E=np.array([[.5,0,.5,1],[1,1,.5,.5],[.5,.5,1,2]]); s=np.array([1,1,2.])
def harms(x,arb=False):
    h=s*(E@x)
    if arb and x[0] and x[2]: h=h.copy(); h[2]+=1.5
    return h
R=3.0
def best(option,arb=False,mix=True):
    rows=[]
    for x in itertools.product([0,1],repeat=4):
        x=np.array(x); h=harms(x,arb)
        prof=p@x + (option*mix)*np.sum(np.maximum(p-R,0)*(1-x))
        rows.append((prof-h.sum(),tuple(x),prof,h))
    rows.sort(key=lambda r:-r[0]); return rows
names='MDEN'
for arb in [False,True]:
  for option in [0,1]:
    D=option*np.sum(np.maximum(p-R,0))
    rows=best(option,arb)
    top=rows[0]
    print(f"arb={arb} option={option} fleet no-deal D={D}; best road set {''.join(n for n,b in zip(names,top[1]) if b)} total {top[0]} pie over no deal {top[0]-D}; ties:",[ ''.join(n for n,b in zip(names,r[1]) if b) for r in rows if abs(r[0]-top[0])<1e-9], "harms",top[3])
# road-only deals (no mixing)
for option in [0,1]:
    D=option*6.5
    rows=best(option,False,mix=False)
    print("no-mix option",option,"best",rows[0][1],rows[0][0],"pie",rows[0][0]-D)
