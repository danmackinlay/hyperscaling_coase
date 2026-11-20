"""Part C: check the claimed equilibrium in claimed_equilibrium.json."""
import json
import itertools
import numpy as np
from street import L, U, P, EXP, NH, SUBSETS, SLOTN, solve_round2, exposure_after, gain_integral, profit

DELTA = 1.0
NAMES = ['Alice', 'Bob', 'Carol']
cl = json.load(open('claimed_equilibrium.json'))
r1c = cl['round_one']
S1 = tuple(SLOTN.index(t) for t in r1c['named_slots'])
kinds = r1c['kinds']; cuts = r1c['cutoffs']; rates1 = np.array(r1c['rates'], float)


def interval(i, ans):
    if kinds[i] in ('all', 'none'):
        return (L, U)
    c = cuts[i]
    return (L, c) if ans == 'accept' else (c, U)


def prob(i, ans):
    if kinds[i] == 'all':
        return 1.0 if ans == 'accept' else 0.0
    if kinds[i] == 'none':
        return 1.0
    pa = (cuts[i] - L) / (U - L)
    return pa if ans == 'accept' else 1 - pa


claimed2 = {}
for row in cl['round_two']:
    claimed2[tuple(row['round_one_answers'])] = (tuple(SLOTN.index(t) for t in row['named_slots']), np.array(row['rates'], float))

print("(a) round-two optimality")
pats = list(claimed2)
a = np.array([[interval(i, p[i])[0] for i in range(NH)] for p in pats])
b = np.array([[interval(i, p[i])[1] for i in range(NH)] for p in pats])
for NG in (9, 25, 41):
    v, r, s = solve_round2(a, b, NG=NG, sweeps=300)
    print("  NG=%d optimum profits:" % NG, np.round(v, 10))
mine = {}
for k, p in enumerate(pats):
    S, rc = claimed2[p]
    vc = profit(S, rc, a[k], b[k])
    Sopt = SUBSETS[s[k]]
    print("  pattern %s beliefs %s" % (p, [(round(a[k, i], 4), round(b[k, i], 4)) for i in range(NH)]))
    print("     claimed: slots %s rates %s profit %.10f" % (''.join(SLOTN[t] for t in S), rc, vc))
    print("     mine   : slots %s rates %s profit %.10f   shortfall of claimed = %.3e" % (
        ''.join(SLOTN[t] for t in Sopt), np.round(r[k], 10), v[k], v[k] - vc))
    # effective slots that can run under the claimed offer
    Fs = np.clip((rc - a[k]) / (b[k] - a[k]), 0, 1)
    run = {SLOTN[t]: float(np.prod([Fs[i] for i in range(NH) if EXP[i, t] > 0])) for t in S}
    print("     claimed run probabilities:", {k2: round(v2, 6) for k2, v2 in run.items()})
    mine[p] = (Sopt, r[k].copy())

# (b) indifference
print("\n(b) indifference")
pacc = np.array([prob(i, 'accept') for i in range(NH)])
E = np.zeros(NH)
for i in range(NH):
    for t in S1:
        if EXP[i, t] > 0:
            E[i] += EXP[i, t] * np.prod([pacc[j] for j in range(NH) if j != i and EXP[j, t] > 0])
print("  E (round-one expected exposure if accept):", E)


def G_of(i, offers):
    """Expected round-two gain of type c_i after refusing, under the given round-two offers."""
    G = 0.0; Xref = 0.0
    others = [j for j in range(NH) if j != i]
    for ans in itertools.product(['accept', 'refuse'], repeat=2):
        pat = [None] * NH; pat[i] = 'refuse'
        pr = 1.0
        for j, aj in zip(others, ans):
            pat[j] = aj; pr *= prob(j, aj)
        if pr == 0:
            continue
        pat = tuple(pat)
        if pat not in offers:
            print("    missing pattern", pat); continue
        S, r = offers[pat]
        aa = np.array([interval(j, pat[j])[0] for j in range(NH)]); bb = np.array([interval(j, pat[j])[1] for j in range(NH)])
        X = exposure_after(S, r, aa, bb, i)
        G += pr * max(r[i] - cuts[i], 0) * X
        Xref += pr * X
    return G, Xref


for i in range(NH):
    if kinds[i] != 'cut':
        print("  %s: kind %s, rate %.10f (top of support = %.1f)" % (NAMES[i], kinds[i], rates1[i], U))
        continue
    for lab, off in (('claimed round-two offers', claimed2), ('my optimal round-two offers', mine)):
        G, Xref = G_of(i, off)
        r1 = cuts[i] + DELTA * G / E[i]
        print("  %s (%s): G=%.12f  implied r1=%.15f  claimed r1=%.15f  diff(claimed-implied)=%.3e" % (
            NAMES[i], lab, G, r1, rates1[i], rates1[i] - r1))

# (c) deviations
print("\n(c) round-one deviations (claimed offers)")
sg = np.linspace(L, U, 200001)
for i in range(NH):
    others = [j for j in range(NH) if j != i]
    Vacc = np.zeros_like(sg); Vref = np.zeros_like(sg)
    for ans in itertools.product(['accept', 'refuse'], repeat=2):
        pr = 1.0
        for j, aj in zip(others, ans):
            pr *= prob(j, aj)
        if pr == 0:
            continue
        for my in ('accept', 'refuse'):
            pat = [None] * NH; pat[i] = my
            for j, aj in zip(others, ans):
                pat[j] = aj
            pat = tuple(pat)
            if pat not in claimed2:
                # off-path: 'all' household refusing; belief unchanged -> same offer as accepting
                assert kinds[i] == 'all'
                pat2 = list(pat); pat2[i] = 'accept'; pat = tuple(pat2)
            S, r = claimed2[pat]
            aa = np.array([interval(j, pat[j])[0] for j in range(NH)]); bb = np.array([interval(j, pat[j])[1] for j in range(NH)])
            X = exposure_after(S, r, aa, bb, i)
            g = pr * np.maximum(r[i] - sg, 0) * X
            if my == 'accept':
                Vacc += g
            else:
                Vref += g
    D = (rates1[i] - sg) * E[i] + DELTA * (Vacc - Vref)  # accept minus refuse
    c = cuts[i] if kinds[i] == 'cut' else U
    below = sg <= c if kinds[i] == 'cut' else np.ones_like(sg, bool)
    above = sg > c
    worst_b = D[below].min(); sb = sg[below][np.argmin(D[below])]
    msg = "  %s: min over types<=cut of (accept-refuse) = %.3e at s=%.6f" % (NAMES[i], worst_b, sb)
    if above.any():
        worst_a = (-D[above]).min(); sa = sg[above][np.argmin(-D[above])]
        msg += "; min over types>cut of (refuse-accept) = %.3e at s=%.6f" % (worst_a, sa)
        # where does D change sign
        neg = np.where(D[above] > 1e-12)[0]
        if len(neg):
            msg += "; types above cut preferring to accept: s in [%.6f, %.6f]" % (sg[above][neg[0]], sg[above][neg[-1]])
    print(msg)
    print("     D at cut = %.3e" % np.interp(c, sg, D))

# value of claimed profile
print("\nCompany two-round value of claimed profile (claimed offers):")
R1 = sum(np.prod([pacc[j] for j in range(NH) if EXP[j, t] > 0]) * (P[t] - sum(rates1[j] * EXP[j, t] for j in range(NH) if EXP[j, t] > 0)) for t in S1)
R2 = 0.0
for k, p in enumerate(pats):
    pr = np.prod([prob(i, p[i]) for i in range(NH)])
    S, rc = claimed2[p]
    R2 += pr * profit(S, rc, a[k], b[k])
print("  R1 %.10f R2 %.10f per-round company %.10f" % (R1, R2, (R1 + R2) / 2))
