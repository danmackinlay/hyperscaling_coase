"""Chain-store bargaining: one company, M streets in sequence, record public.

Per street (base instance: schedule M,D,E; pie 6; three residents, k=3):
  The company posts an offer: each resident is paid her harm plus L/3
  (block premium L).  All three accept -> company 6-L, residents L/3 each.
  Any refusal ->
     committed company (prob q, the commitment dial: its posted 'final
     offer' sticks) walks: street gets no deal, all gains 0;
     uncommitted company either walks (to protect its record) or raises
     to the fair deal: equal split 1.5 each, after a delay factor delta,
     so company C = 1.5*delta, residents V = 4.5*delta (1.5*delta each).
  Kreps-Wilson (1982) sequential equilibrium of the finite chain store,
  with the 'entrant' = the street's residents (reject = enter),
  'fight' = walk, 'accommodate' = raise to fair.
The company chooses L (grid) to maximise its ex-ante take; it may instead
reveal itself and offer the fair-after-delay level V on every street.
"""
import math
import sys
from functools import lru_cache
sys.setrecursionlimit(20000)

PIE = 6.0
N_RES = 3
FAIR_EACH = PIE / (N_RES + 1)  # 1.5
HARMS = {"Alice": 1.0, "Bob": 2.5, "Carol": 4.0}
SQ = {"company": 13.5, "Alice": -1.0, "Bob": -2.5, "Carol": -4.0}  # ordinance


def solve(M, q, L, delta, check=True):
    C = FAIR_EACH * delta          # uncommitted company's take if it raises
    V = N_RES * FAIR_EACH * delta  # residents' block take if it raises
    A = PIE - L                    # company take on an accepted street
    F = 0.0
    b = 1.0 - L / V
    a = (A - C) / (C - F)
    if not (0 < b < 1) or a <= 0:
        return None
    eps = 1e-12
    viol = []

    @lru_cache(maxsize=None)
    def rec(n, p):
        # returns (W, T, RW, RT, DW, DT): weak/tough company take, residents'
        # take given weak/tough, deals given weak/tough, over n streets left
        if n == 0:
            return (0.0,) * 6
        thr = b ** n
        if p > 0 and p > thr + eps:
            m = int(math.floor(math.log(p) / math.log(b)))  # b^m >= p
            if m + 1 < n:  # jump over the sure-acceptance phase
                r = rec(m + 1, p)
                k = n - m - 1
                return (r[0] + k * A, r[1] + k * A, r[2] + k * L,
                        r[3] + k * L, r[4] + k, r[5] + k)
        if p > thr + eps:
            sigma = 1.0
        elif p < thr - eps:
            sigma = 0.0
        else:
            sigma = 1.0 / a
            if sigma > 1:
                viol.append(('a<1 mixing', n, p))
                sigma = 1.0
        if n == 1:
            phi = 0.0
            p_f = p
        else:
            t1 = b ** (n - 1)
            if p >= t1 - eps:
                phi, p_f = 1.0, p
            else:
                phi = p * (1 - t1) / ((1 - p) * t1)
                p_f = t1
        p_f = round(p_f, 12)
        so = rec(n - 1, round(p, 12))
        fi = rec(n - 1, p_f)
        ac = rec(n - 1, 0.0)
        if check:
            # residents: accept iff L >= P(raise | refuse) * V
            praise = (1 - p) * (1 - phi)
            gain_refuse = praise * V
            if sigma == 1.0 and gain_refuse > L + 1e-9:
                viol.append(("res-accept", n, p))
            if sigma == 0.0 and gain_refuse < L - 1e-9:
                viol.append(("res-refuse", n, p))
            # weak company after refusal: walk vs raise
            v_walk = F + fi[0]
            v_raise = C + ac[0]
            if phi == 1.0 and n > 1 and v_walk < v_raise - 1e-9:
                viol.append(("weak-walk", n, p, v_walk, v_raise))
            if phi == 0.0 and v_walk > v_raise + 1e-9 and n > 1:
                viol.append(("weak-raise", n, p))
        W = sigma * (A + so[0]) + (1 - sigma) * (
            phi * (F + fi[0]) + (1 - phi) * (C + ac[0]))
        RW = sigma * (L + so[2]) + (1 - sigma) * (
            phi * fi[2] + (1 - phi) * (V + ac[2]))
        DW = sigma * (1 + so[4]) + (1 - sigma) * (
            phi * fi[4] + (1 - phi) * (1 + ac[4]))
        T = sigma * (A + so[1]) + (1 - sigma) * (F + fi[1])
        RT = sigma * (L + so[3]) + (1 - sigma) * fi[3]
        DT = sigma * (1 + so[5]) + (1 - sigma) * fi[5]
        return (W, T, RW, RT, DW, DT)

    W, T, RW, RT, DW, DT = rec(M, round(q, 12))
    tail = math.ceil(math.log(q) / math.log(b)) if q > 0 else M
    return dict(W=W / M, T=T / M, RW=RW / M, RT=RT / M, DW=DW / M,
                DT=DT / M, comp=(q * T + (1 - q) * W) / M,
                res=(q * RT + (1 - q) * RW) / M,
                deals=(q * DT + (1 - q) * DW) / M,
                tail=min(tail, M), L=L, viol=viol)


def best(M, q, delta, grid):
    V = N_RES * FAIR_EACH * delta
    reveal = dict(comp=PIE - V, res=V, W=PIE - V, RW=V, deals=1.0, L=V,
                  tail=0, viol=[], T=PIE - V, RT=V, DW=1, DT=1)
    out = reveal
    for L in grid:
        r = solve(M, q, L, delta) if q > 0 else None
        if r and not r["viol"] and r["comp"] > out["comp"] + 1e-12:
            out = r
    return out


def gm_frac(comp, res):
    each = res / N_RES
    if comp <= 0 or each <= 0:
        return 0.0
    return (comp * each ** N_RES) ** 0.25 / FAIR_EACH


def main(step=0.01):
    grid = [round(step * i, 6) for i in range(1, int(4.5 / step))]
    rows = []
    for delta in (1.0, 0.95, 0.8, 0.5):
        for M in (1, 10, 100, 1000):
            for q in (0.0, 0.01, 0.05, 0.2, 0.5, 1.0 - 1e-9):
                r = best(M, q, delta, grid)
                nv = len(r["viol"])
                rows.append((delta, M, q, r["L"], r["comp"], r["res"],
                             r["res"] / N_RES, r["deals"], r["tail"],
                             gm_frac(r["comp"], r["res"]), nv))
    hdr = ("delta", "M", "q", "L*", "company/street", "residents/street",
           "each/street", "deal rate", "tail", "GM/max", "viol")
    print("\t".join(hdr))
    for row in rows:
        print("\t".join(f"{x:.4g}" if isinstance(x, float) else str(x)
                        for x in row))


if __name__ == "__main__":
    main(float(sys.argv[1]) if len(sys.argv) > 1 else 0.01)
