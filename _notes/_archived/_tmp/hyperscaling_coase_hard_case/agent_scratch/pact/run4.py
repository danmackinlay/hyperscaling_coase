"""The veil: mechanism chosen before s is drawn (ex ante IR only); AGV; regret; recurring redraws."""
import json, sys
import numpy as np
from core2 import *

P2 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
pr2 = (P2,) * 3
m = M(pr2, full_t=False)
pt = lambda th: P2 if th == 2 else 1 - P2
KEYS = ["F"] + [f"r{i+1}s{th}" for i in range(3) for th in TYPES]


def sq_liab(sbar):
    xL = (p > sbar * E.sum(0) + 1e-12).astype(float)
    res = [{th: (sbar - th) * (E[i] @ xL) for th in TYPES} for i in range(3)]
    return res, p @ xL - sbar * (E.sum(0) @ xL)


SQ = {"nodeal": ([{1: 0.0, 2: 0.0}] * 3, 0.0), "liab1.5": sq_liab(1.5), "liab1.0": sq_liab(1.0)}
Wstar = sum(m.P[s] * FB[s] for s in PROFILES)
print("W* =", Wstar)

# AGV with strict tie-break (run a slot iff strictly positive surplus)
def xstar(s):
    return np.array([1.0 if p[t] - sum(s[i] * E[i, t] for i in range(3)) > 1e-12 else 0.0 for t in range(4)])

def v(k, x, s):  # k=0 fleet, 1..3 residents
    return p @ x if k == 0 else -s[k - 1] * (E[k - 1] @ x)

def xi(k, th):  # expected externality of resident k (1..3) at type th on all others
    tot = 0.0
    for s in PROFILES:
        if s[k - 1] != th:
            continue
        w = m.P[s] / pt(th)
        x = xstar(s)
        tot += w * sum(v(j, x, s) for j in range(4) if j != k)
    return tot

xi_f = sum(m.P[s] * sum(v(j, xstar(s), s) for j in range(1, 4)) for s in PROFILES)  # fleet's (constant)

def agv_payoffs(s):
    x = xstar(s)
    XI = [xi_f] + [xi(k, s[k - 1]) for k in (1, 2, 3)]
    t = [XI[k] - sum(XI[j] for j in range(4) if j != k) / 3 for k in range(4)]
    return [v(k, x, s) + t[k] for k in range(4)]

ex_agv = [sum(m.P[s] * agv_payoffs(s)[k] for s in PROFILES) for k in range(4)]
interim_agv = {}
for k in (1, 2, 3):
    for th in TYPES:
        interim_agv[f"r{k}s{th}"] = sum(m.P[s] / pt(th) * agv_payoffs(s)[k] for s in PROFILES if s[k - 1] == th)
interim_agv["F"] = ex_agv[0]
print("AGV raw ex ante", [round(x, 4) for x in ex_agv], "sum", round(sum(ex_agv), 4))

out = {"W*": Wstar}
for sqname, (sq_res, sq_f) in SQ.items():
    sq_ex = [sq_f] + [sum(pt(th) * sq_res[i][th] for th in TYPES) for i in range(3)]
    G = (Wstar - sum(sq_ex)) / 4
    L = [sq_ex[k] + G - ex_agv[k] for k in range(4)]  # lump sums -> equal ex ante gains
    agv_i = {key: val + L[0 if key == "F" else int(key[1])] for key, val in interim_agv.items()}
    agv_true = [a + l for a, l in zip(agv_payoffs(S_TRUE), L)]
    # range of r3-high interim among efficient IC mechanisms with ex ante gains all = G (Nash optimum under the veil)
    c = m.cons(ir=None, sq_f=None, efficient=True)
    eqs = [(m.F(), sq_ex[0] + G)] + [(m.exante(i), sq_ex[i + 1] + G) for i in range(3)]
    lo = m.lp(-m.U(2, 2, 2), c, extra_eq=eqs); hi = m.lp(m.U(2, 2, 2), c, extra_eq=eqs)
    rows = [m.F()] + [m.U(i, th, th) for i in range(3) for th in TYPES]
    rng = {key: (round(float(r @ lo), 4), round(float(r @ hi), 4)) for key, r in zip(KEYS, rows)}
    # does any veil-Nash mechanism also satisfy interim IR vs this SQ (so nobody regrets vs exit)?
    ir_rows = [(-m.U(i, th, th), -sq_res[i][th]) for i in range(3) for th in TYPES]
    z_ir = m.lp(m.U(2, 2, 2), c, extra=ir_rows, extra_eq=eqs)
    sqi = {"F": sq_f, **{f"r{i+1}s{th}": sq_res[i][th] for i in range(3) for th in TYPES}}
    regret_exit_agv = {k: round(agv_i[k] - sqi[k], 4) for k in KEYS}
    out[sqname] = dict(G_each=round(G, 4), agv_interim={k: round(x, 4) for k, x in agv_i.items()},
                       agv_minus_sq_interim=regret_exit_agv,
                       agv_expost_true=[round(x, 4) for x in agv_true],
                       veil_nash_range_when_r3high_lo_hi=rng,
                       veil_nash_with_interim_IR_exists=z_ir is not None,
                       veil_nash_with_interim_IR_r3high=None if z_ir is None else round(float(m.U(2, 2, 2) @ z_ir), 4))
    print(sqname, json.dumps(out[sqname]))
json.dump(out, open(f"run4_P{P2}.json", "w"), indent=1)
