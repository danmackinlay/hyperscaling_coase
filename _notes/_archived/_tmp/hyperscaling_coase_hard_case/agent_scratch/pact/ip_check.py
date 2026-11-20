import numpy as np, json
from core2 import *
exec(open('run5.py').read().split('# ---- bloc')[0].split('best = {}')[0])
for th_fix, other in ((1,2),(2,1)):
    for tol in (1e-6,1e-4,1e-2):
        b1 = float(m.U(2,th_fix,th_fix) @ m.lp(m.U(2,th_fix,th_fix), c, extra=safe))
        z = m.lp(m.U(2,other,other), c, extra=safe+[(-m.U(2,th_fix,th_fix), -b1+tol)])
        print(f"fix type {th_fix} at best {b1:.4f}-{tol}: max type {other} =", None if z is None else round(float(m.U(2,other,other)@z),4))
# without safety (standard IC, IR prior-based): typewise max
for th in TYPES:
    z=m.lp(m.U(2,th,th), c); print("unsafe typewise best", th, round(float(m.U(2,th,th)@z),4))
# neutral-optimum style: maximise prior-weighted sum with safety
z=m.lp(0.5*m.U(2,1,1)+0.5*m.U(2,2,2), c, extra=safe); print("safe, max E U3:", round(float(m.U(2,1,1)@z),4), round(float(m.U(2,2,2)@z),4), "F", round(float(m.F()@z),4), "r1", [round(float(m.U(0,t,t)@z),4) for t in TYPES], "r2", [round(float(m.U(1,t,t)@z),4) for t in TYPES], "Esurp", round(float(m.Wrow()@z),4))
pay,sched=m.expost(z,S_TRUE); print("expost at true", [round(x,3) for x in pay], sched)
