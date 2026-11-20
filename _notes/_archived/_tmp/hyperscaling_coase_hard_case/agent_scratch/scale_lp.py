"""Scaling the hard-case instance: m copies of the three profiles, one fleet, one timetable,
unanimity (k = 3m), private sensitivities, voluntary participation (interim IR), incentive
compatibility, ex ante budget balance for the fleet.  Mailath-Postlewaite / Rob setting.

Prior: s_i in {sbar_i(1-alpha), sbar_i(1+alpha)} each w.p. 1/2, independent.
State = counts of high types per class, n = (n1, n2, n3), n_i ~ Bin(m, 1/2).

LP1 (second best): max expected total surplus.
LP2: among second-best mechanisms, minimise expected transfers (fleet's max take; residents' rents floor).
LP3 (fleet-optimal): max fleet expected profit net of transfers.
LP4 (lottery over 16 schedules): max P(realised schedule == ex post efficient schedule).

usage: python scale_lp.py m alpha outside(0|1) [lottery(0|1)] [trunc_sd]
"""
import itertools
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, lil_matrix, vstack, hstack, identity
from scipy.stats import binom

m = int(sys.argv[1]); alpha = float(sys.argv[2]); outside = int(sys.argv[3])
lottery = int(sys.argv[4]) if len(sys.argv) > 4 else 0
trunc_sd = float(sys.argv[5]) if len(sys.argv) > 5 else None

p = np.array([4.0, 5.5, 4.0, 5.0])
e = np.array([[0.5, 0, 0.5, 1.0], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
sbar = np.array([1.0, 1.0, 2.0])
s_lo, s_hi = sbar * (1 - alpha), sbar * (1 + alpha)
rr = np.maximum(p - 3.0, 0) if outside else np.zeros(4)
d_F = rr.sum() * m

# state space
rng = range(m + 1)
if trunc_sd is not None:
    sd = np.sqrt(m / 4); lo = max(0, int(np.floor(m / 2 - trunc_sd * sd))); hi = min(m, int(np.ceil(m / 2 + trunc_sd * sd)))
    rng = range(lo, hi + 1)
states = np.array(list(itertools.product(rng, rng, rng)))  # S x 3
S = len(states)
pm = binom.pmf(np.arange(m + 1), m, 0.5)
pm1 = binom.pmf(np.arange(m), m - 1, 0.5) if m > 1 else np.array([1.0])
P = pm[states[:, 0]] * pm[states[:, 1]] * pm[states[:, 2]]
P = P / P.sum()  # renormalise if truncated
# conditional on own report, class i: own class count k: hi -> k-1 ~ Bin(m-1), lo -> k ~ Bin(m-1)
def P_cond(i, rep):
    k = states[:, i]
    if rep == "hi":
        own = np.where(k >= 1, pm1[np.clip(k - 1, 0, m - 1)], 0.0)
    else:
        own = np.where(k <= m - 1, pm1[np.clip(k, 0, m - 1)], 0.0)
    others = np.prod([pm[states[:, j]] for j in range(3) if j != i], axis=0)
    w = own * others
    return w / w.sum()

# total harm per slot at each state (whole population): S x 4
Harm = ((m - states) * s_lo + states * s_hi) @ e  # S x 4
surplus_slot = m * p[None, :] - Harm + 0  # if slot runs (vs rerouted: -m*rr)
slot_gain = surplus_slot - m * rr[None, :]  # gain from running slot t through, relative to reroute/not
print(f"m={m} alpha={alpha} outside={outside} states={S} s_lo={s_lo} s_hi={s_hi}")

if not lottery:
    # variables: y[s, t] (S*4), then T[i, theta] (6)  index T: 4S + 2i + (0 hi, 1 lo)
    nv = 4 * S + 6
    def yidx(t): return np.arange(S) * 4 + t
    def Tidx(i, th): return 4 * S + 2 * i + (0 if th == "hi" else 1)
    def H_row(i, rep):  # coefficients on y giving H_i(rep) (per resident, expected exposure)
        w = P_cond(i, rep); row = np.zeros(nv)
        for t in range(4): row[yidx(t)] = w * e[i, t]
        return row
    A = []; b = []
    for i in range(3):
        Hh, Hl = H_row(i, "hi"), H_row(i, "lo")
        # IC hi: T_hi - s_hi H_hi >= T_lo - s_hi H_lo  ->  -(T_hi - T_lo) + s_hi (H_hi - H_lo) <= 0
        r = s_hi[i] * (Hh - Hl); r[Tidx(i, "hi")] -= 1; r[Tidx(i, "lo")] += 1; A.append(r); b.append(0)
        # IC lo: T_lo - s_lo H_lo >= T_hi - s_lo H_hi
        r = s_lo[i] * (Hl - Hh); r[Tidx(i, "lo")] -= 1; r[Tidx(i, "hi")] += 1; A.append(r); b.append(0)
        # IR hi: T_hi - s_hi H_hi >= 0 ; IR lo
        r = s_hi[i] * Hh; r[Tidx(i, "hi")] -= 1; A.append(r); b.append(0)
        r = s_lo[i] * Hl; r[Tidx(i, "lo")] -= 1; A.append(r); b.append(0)
    # fleet: E[profit] - m sum_i (T_hi+T_lo)/2 >= d_F ; profit = sum_t y (m p_t - m rr_t) + m rr_t
    prof = np.zeros(nv)
    for t in range(4): prof[yidx(t)] = P * m * (p[t] - rr[t])
    const_prof = m * rr.sum()
    r = -prof.copy()
    for i in range(3): r[Tidx(i, "hi")] += m / 2; r[Tidx(i, "lo")] += m / 2
    A.append(r); b.append(const_prof - d_F)
    A = np.array(A); b = np.array(b)
    bounds = [(0, 1)] * (4 * S) + [(None, None)] * 6
    # objective 1: expected total surplus (gain over all-reroute/no-deal baseline)
    c_surp = np.zeros(nv)
    for t in range(4): c_surp[yidx(t)] = P * slot_gain[:, t]
    res = linprog(-c_surp, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    assert res.status == 0, res.message
    y = res.x[:4 * S].reshape(S, 4); T = res.x[4 * S:]
    best_gain = -res.fun
    first_best = (P * np.maximum(slot_gain, 0).sum(1)).sum()
    eff = (slot_gain > 0).astype(float)
    p_all_correct = (P * np.all(np.abs(y - eff) < 1e-6, axis=1)).sum()
    p_slot = [(P * (1 - np.abs(y[:, t] - eff[:, t]))).sum() for t in range(4)]
    frac_vars = np.sum((y > 1e-6) & (y < 1 - 1e-6))
    print(f"LP1 second-best: expected gain over no-deal/reroute per copy {best_gain/m:.4f} vs first-best {first_best/m:.4f} ({best_gain/first_best:.4f})")
    print(f"  P(all four slots decided efficiently) = {p_all_correct:.4f}; P(slot correct) M,D,E,N = {np.round(p_slot,4)}; fractional y's: {frac_vars}")
    print(f"  E[y_t] run prob M,D,E,N = {np.round(P @ y, 4)}; E[eff_t] = {np.round(P @ eff, 4)}")
    # LP2: fix surplus, minimise expected transfers
    A2 = np.vstack([A, -c_surp[None, :]]); b2 = np.append(b, -(best_gain * (1 - 1e-6)))
    c_T = np.zeros(nv)
    for i in range(3): c_T[Tidx(i, "hi")] = m / 2; c_T[Tidx(i, "lo")] = m / 2
    res2 = linprog(c_T, A_ub=A2, b_ub=b2, bounds=bounds, method="highs")
    assert res2.status == 0, res2.message
    y2 = res2.x[:4 * S].reshape(S, 4); T2 = res2.x[4 * S:]
    rents = []
    for i in range(3):
        for th, sv, rep in (("hi", s_hi[i], "hi"), ("lo", s_lo[i], "lo")):
            H = (P_cond(i, rep) * (y2 @ e[i])).sum()
            rents.append(T2[Tidx(i, th) - 4 * S] - sv * H)
    rents = np.array(rents).reshape(3, 2)
    exp_rent = rents.mean(1)
    fleet_gain = best_gain - m * exp_rent.sum()
    print(f"LP2 minimal transfers at second best: residents' expected gains (rent) per resident by class {np.round(exp_rent,4)} (hi,lo rows {np.round(rents,4)}); fleet gain per copy {fleet_gain/m:.4f}")
    resid = fleet_gain / m
    g = np.array([resid / 4, *(exp_rent + resid / 4)])
    print(f"  per-copy four-party gains if fleet's residual split equally (F; r1,r2,r3) {np.round(g,4)}, product {np.prod(g):.4f}, floor {g.min():.4f}; residents' min share of gains {m*exp_rent.sum()/best_gain:.3f}")
    # LP3: fleet-optimal
    c_fleet = prof.copy()
    for i in range(3): c_fleet[Tidx(i, "hi")] -= m / 2; c_fleet[Tidx(i, "lo")] -= m / 2
    res3 = linprog(-c_fleet, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    assert res3.status == 0, res3.message
    y3 = res3.x[:4 * S].reshape(S, 4); T3 = res3.x[4 * S:]
    gain3 = (c_surp @ res3.x); fleet3 = -res3.fun + const_prof - d_F
    rents3 = []
    for i in range(3):
        for th, sv, rep in (("hi", s_hi[i], "hi"), ("lo", s_lo[i], "lo")):
            H = (P_cond(i, rep) * (y3 @ e[i])).sum(); rents3.append(T3[Tidx(i, th) - 4 * S] - sv * H)
    rents3 = np.array(rents3).reshape(3, 2).mean(1)
    p_all3 = (P * np.all(np.abs(y3 - eff) < 1e-6, axis=1)).sum()
    print(f"LP3 fleet-optimal mechanism: total gain per copy {gain3/m:.4f} ({gain3/first_best:.3f} of first best), fleet gain per copy {fleet3/m:.4f}, residents' expected gains {np.round(rents3,4)}, P(all slots efficient) {p_all3:.4f}, E[y] {np.round(P @ y3,4)}")
else:
    X = np.array(list(itertools.product([0, 1], repeat=4)), float)  # 16 x 4
    gain_sx = slot_gain @ X.T  # S x 16
    xstar = gain_sx.argmax(1)
    nv = 16 * S + 6
    def Tidx(i, th): return 16 * S + 2 * i + (0 if th == "hi" else 1)
    expo = e @ X.T  # 3 x 16 exposure per schedule
    def H_row(i, rep):
        w = P_cond(i, rep); row = np.zeros(nv)
        row[:16 * S] = (w[:, None] * expo[i][None, :]).ravel(); return row
    A = []; b = []
    for i in range(3):
        Hh, Hl = H_row(i, "hi"), H_row(i, "lo")
        r = s_hi[i] * (Hh - Hl); r[Tidx(i, "hi")] -= 1; r[Tidx(i, "lo")] += 1; A.append(r); b.append(0)
        r = s_lo[i] * (Hl - Hh); r[Tidx(i, "lo")] -= 1; r[Tidx(i, "hi")] += 1; A.append(r); b.append(0)
        r = s_hi[i] * Hh; r[Tidx(i, "hi")] -= 1; A.append(r); b.append(0)
        r = s_lo[i] * Hl; r[Tidx(i, "lo")] -= 1; A.append(r); b.append(0)
    prof = np.zeros(nv)
    prof[:16 * S] = (P[:, None] * (m * (p - rr) @ X.T)[None, :]).ravel()
    const_prof = m * rr.sum()
    r = -prof.copy()
    for i in range(3): r[Tidx(i, "hi")] += m / 2; r[Tidx(i, "lo")] += m / 2
    A.append(r); b.append(const_prof - d_F)
    A = csr_matrix(np.array(A)); b = np.array(b)
    # simplex equalities
    Aeq = hstack([csr_matrix((np.ones(16 * S), (np.repeat(np.arange(S), 16), np.arange(16 * S))), shape=(S, 16 * S)), csr_matrix((S, 6))])
    beq = np.ones(S)
    bounds = [(0, 1)] * (16 * S) + [(None, None)] * 6
    c = np.zeros(nv)
    c[np.arange(S) * 16 + xstar] = -P
    res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    assert res.status == 0, res.message
    pi = res.x[:16 * S].reshape(S, 16)
    print(f"LP4 max P(efficient schedule) = {-res.fun:.4f}; expected gain under it per copy {(P * (pi * gain_sx).sum(1)).sum()/m:.4f}; first best {(P * gain_sx.max(1)).sum()/m:.4f}")
    # which schedules are used
    use = P @ pi
    labels = ["".join(ch for ch, bb in zip("MDEN", x) if bb) or "none" for x in X]
    print("  schedule probabilities:", {labels[j]: round(use[j], 4) for j in range(16) if use[j] > 1e-4})
    print("  efficient-schedule probabilities:", {labels[j]: round(v, 4) for j, v in enumerate(np.bincount(xstar, weights=P, minlength=16)) if v > 1e-4})
