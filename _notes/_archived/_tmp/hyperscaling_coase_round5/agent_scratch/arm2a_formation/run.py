"""Driver: formation-stage outcomes per cell, Monte Carlo over the prior or base s."""
import sys, json, math, random
import numpy as np
from arm2a import *

ORD_EX = np.array([float(E[t] @ np.array([1,1,1,0])) for t in range(3)])  # ordinance M,D,E

def structure(econ, sig, g):
    gr, sol = econ.solve(sig, g)
    return gr, sol

def simulate(econ, table, c, draws, seed, base_s=None, org=None):
    """table[(tp,sp)] -> (val,g,sig). org: (g, F) -> every resident bound at g, no proposer.
    Returns dict of summaries."""
    rng = random.Random(seed)
    n, m, k, q = econ.n, econ.m, econ.k, econ.q
    types = [i // m for i in range(n)]
    tot_res = np.zeros(n); tot_pr = 0.0; below = 0.0; deals = 0; formed = 0
    kinds = {"none":0, "holds":0, "divided":0, "blocked":0}
    msg = 0.0
    for _ in range(draws):
        s = [base_s[types[i]] if base_s else (2 if rng.random() < q else 1) for i in range(n)]
        if org is not None:
            g, F = org
            sig = (m, m, m); signers = set(range(n)); prop = None
        else:
            prop = rng.randrange(n)
            val, g, sigc = table[(types[prop], s[prop])]
            if sigc is None:
                sig = (0, 0, 0); signers = set(); g = 0.0
            else:
                sig = sigc; signers = {prop}
                for t in range(3):
                    need = sig[t] - (1 if t == types[prop] else 0)
                    pool = [i for i in range(n) if types[i] == t and i != prop]
                    rng.shuffle(pool)
                    signers.update(pool[:need])
                formed += 1
                msg += c * (sum(sig) - 1)
        gr, sol = econ.solve(sig, g)
        prof, xi, lv = sol
        gains = np.zeros(n); pr = 0.0
        if xi is not None:
            x = XS[xi]
            # assign levels within groups
            level = {}
            for (t, d, N), (H, L, Z) in zip(gr, lv):
                mem = [i for i in range(n) if types[i] == t and ((i in signers) == (d > 0))]
                rng.shuffle(mem)
                labs = ["H"] * H + ["L"] * L + ["Z"] * Z
                for i, lab in zip(mem, labs):
                    level[i] = (lab, d)
            acc = []; pay = np.zeros(n)
            for i in range(n):
                lab, d = level[i]
                ex = float(E[types[i]] @ x)
                if ex == 0 and d <= 0:
                    p_ = 0.0
                elif lab == "H": p_ = d + 2 * ex
                elif lab == "L": p_ = d + ex
                else: p_ = 0.0
                a = p_ - s[i] * ex >= d - 1e-12
                acc.append(a); pay[i] = p_ if a else 0.0
            if sum(acc) >= k:
                deals += 1
                harm = np.array([s[i] * float(E[types[i]] @ x) for i in range(n)])
                gains = pay - harm
                pr = m * float(P @ x) - pay.sum()
            # classify
            if signers:
                sl = [level[i][0] for i in signers]
                kinds["divided" if any(l == "Z" for l in sl) else "holds"] += 1
        else:
            if signers: kinds["blocked"] += 1
        if signers == set(): kinds["none"] += 1
        if org is not None:
            gains = gains - org[1] / n
        elif prop is not None and sig != (0,0,0):
            gains[prop] -= c * (sum(sig) - 1)
        tot_res += gains; tot_pr += pr
        below += np.mean(gains < -1e-12)
    R = tot_res / draws
    by_type = [float(R[[i for i in range(n) if types[i] == t]].mean()) for t in range(3)]
    PR = tot_pr / draws
    parties = [PR] + list(R)
    pos = [v for v in parties if v > 1e-12]
    gm = math.exp(sum(math.log(v) for v in pos) / len(pos)) if pos else 0.0
    pie = PR + R.sum() + (msg / draws if org is None else org[1])  # realised pie before coordination costs
    eq = (PR + R.sum()) / (n + 1)
    if org is not None: s_ord = None
    return dict(principal=round(PR, 3), A=round(by_type[0], 3), B=round(by_type[1], 3), C=round(by_type[2], 3),
                floor=round(min(parties), 3), frac_below=round(below / draws, 4), deal_rate=round(deals / draws, 4),
                formed=round(formed / draws, 4), kinds={k_: round(v / draws, 4) for k_, v in kinds.items()},
                msg_per_res=round(msg / draws / n, 4), gm_pos=round(gm, 3), n_pos=len(pos),
                crit=round(gm / eq, 3) if eq > 0 and len(pos) == n + 1 else None, pie=round(pie, 3))

def ordinance(q, base_s):
    Es = [base_s[t] for t in range(3)] if base_s else [1 + q] * 3
    return [round(-Es[t] * ORD_EX[t], 3) for t in range(3)]

def build_table(econ, c, ggrid, strict):
    return {(tp, sp): econ.proposer_choice(tp, sp, c, ggrid, strict) for tp in range(3) for sp in (1, 2)}

def best_org(econ, F, ggrid, objective="total"):
    best = None
    for g in ggrid:
        gr, sol = econ.solve((econ.m,)*3, g)
        vals = []
        for j,(t,d,N) in enumerate(gr):
            vals += [exante_gain(gr, sol, j, econ.n, econ.k, econ.q)] * N
        score = sum(vals) if objective == "total" else min(vals)
        if best is None or score > best[0] + 1e-9:
            best = (score, g)
    return best[1]

if __name__ == "__main__":
    n, k, q = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    gmax = float(sys.argv[4]) if len(sys.argv) > 4 else 4.0
    strict = (sys.argv[5] != "weak") if len(sys.argv) > 5 else True
    draws = int(sys.argv[6]) if len(sys.argv) > 6 else 20000
    ggrid = [0.25 * i for i in range(1, int(gmax / 0.25) + 1)]
    econ = Economy(n, k, q)
    bases = [None] + ([(1, 1, 2)] if n == 3 else [])
    print(f"### n={n} k={k} q={q} gmax={gmax} strict={strict}")
    print("t=0:", describe(econ, (0, 0, 0), 0.0))
    for c in (0.01, 0.1):
        table = build_table(econ, c, ggrid, strict)
        for (tp, sp), (v, g, sig) in sorted(table.items()):
            print(f"  c={c} proposer {'ABC'[tp]} s={sp}: g={g} sig={sig} -> {describe(econ, sig or (0,0,0), g or 0.0)}")
        for base in bases:
            for seed in (1, 2):
                r = simulate(econ, table, c, draws, seed, base_s=base)
                print(f"  PACT c={c} s={'base' if base else 'prior'} seed={seed}:", json.dumps(r))
    # no-pact benchmark
    for base in bases:
        r = simulate(econ, {(t, s): (0, None, None) for t in range(3) for s in (1, 2)}, 0, draws, 1, base_s=base)
        print(f"  NOPACT s={'base' if base else 'prior'}:", json.dumps(r), "ordinance:", ordinance(q, base))
    for obj in ("total", "min"):
        g = best_org(econ, 0, ggrid, obj)
        print(f"  ORG objective={obj}: g={g} ->", describe(econ, (econ.m,)*3, g))
        for F in (0.5, 2):
            for base in bases:
                for seed in (1, 2):
                    r = simulate(econ, None, 0, draws, seed, base_s=base, org=(g, F))
                    print(f"  ORG {obj} F={F} s={'base' if base else 'prior'} seed={seed}:", json.dumps(r))
