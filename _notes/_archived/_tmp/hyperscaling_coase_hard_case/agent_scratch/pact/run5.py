"""Informed principal (resident 3 proposes; bloc proposes), regret table, veil thresholds by delta."""
import json, sys
import numpy as np
from core2 import *

P2 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
pr2 = (P2,) * 3
pt = lambda th: P2 if th == 2 else 1 - P2
KEYS = ["F"] + [f"r{i+1}s{th}" for i in range(3) for th in TYPES]
run3 = json.load(open(f"run3_P{P2}.json"))
run4 = json.load(open(f"run4_P{P2}.json"))

# ---- resident 3 as informed principal under SQ0 (interim veto for others), Myerson's safe-and-undominated test
m = M(pr2, full_t=False)
base = dict(sq_res=[{1: 0.0, 2: 0.0}] * 3, sq_f=0.0, ir="interim")
c = m.cons(**base)
# 'safe': others' IR and IC must hold conditional on each type of resident 3 separately
def safe_rows(th3):
    rows = []
    A = ((1, 2), (1, 2), (th3,))
    for i in (0, 1):
        for th in TYPES:
            rows.append((-m.U(i, th, th, A=A), 0.0))
            for r in TYPES:
                if r != th:
                    rows.append((m.U(i, r, th, A=A) - m.U(i, th, th, A=A), 0.0))
    rows.append((-m.F(A=A), 0.0))
    return rows
safe = safe_rows(1) + safe_rows(2)
best = {}
for th in TYPES:
    z = m.lp(m.U(2, th, th), c, extra=safe)
    best[th] = float(m.U(2, th, th) @ z)
zj = m.lp(m.U(2, 1, 1) + m.U(2, 2, 2), c, extra=safe + [(-m.U(2, th, th), -best[th] + 1e-7) for th in TYPES])
ip3 = dict(typewise_best=best, joint_achievable=zj is not None)
if zj is not None:
    ip3["interim"] = {k: round(float(r @ zj), 4) for k, r in zip(KEYS, [m.F()] + [m.U(i, th, th) for i in range(3) for th in TYPES])}
    ip3["exp_surplus"] = round(float(m.Wrow() @ zj), 4)
    # full-information benchmark for resident 3: FB(s) given s3, others held to 0 conditional on s3
    ip3["full_info_bench"] = {th: round(sum(m.P[s] / pt(th) * FB[s] for s in PROFILES if s[2] == th), 4) for th in TYPES}
print("resident 3 as informed principal:", json.dumps(ip3))

# ---- bloc as informed principal (residents pool information, propose to the fleet): fleet's payoff does not
# depend on s, so offering x*(s) at price p.x*(s) is safe; check it is undominated: residents get FB(s), fleet 0.
bloc = {s: FB[s] for s in PROFILES}
print("bloc strong solution: residents take FB(s) at each profile, fleet 0; at true", FB[S_TRUE])

# ---- regret table at P2: veil (AGV and the veil-Nash range) against exit (SQ) and against waiting (durable HS-Nash)
reg = {}
for sq in ("nodeal", "liab1.5", "liab1.0"):
    tag = "nodeal/interim" if sq == "nodeal" else f"{sq}/interim"
    wait = run3[tag]["eff"]["hs_nash"]["interim"]
    agv = run4[sq]["agv_interim"]
    sqi = {k: run4[sq]["agv_interim"][k] - run4[sq]["agv_minus_sq_interim"][k] for k in KEYS}
    rng = run4[sq]["veil_nash_range_when_r3high_lo_hi"]
    reg[sq] = {k: dict(sq=round(sqi[k], 4), wait=wait[k], veil_agv=agv[k], veil_range=sorted(rng[k]),
                       agv_vs_exit=round(agv[k] - sqi[k], 4), agv_vs_wait=round(agv[k] - wait[k], 4)) for k in KEYS}
    G = run4[sq]["G_each"]
    # recurring with iid redraws: stay with AGV iff shortfall_vs_exit + d/(1-d)*G >= 0 (exit = back to SQ forever)
    thr = {}
    for k in KEYS:
        short = agv[k] - sqi[k]
        thr[k] = 0.0 if short >= 0 else round((-short / G) / (1 + (-short / G)), 4)
    reg[sq]["_delta_needed_to_keep_each_type_in_AGV"] = thr
    reg[sq]["_G_each"] = G
    print(sq, json.dumps(reg[sq]))
json.dump(dict(ip3=ip3, regret=reg), open(f"run5_P{P2}.json", "w"), indent=1, default=float)
