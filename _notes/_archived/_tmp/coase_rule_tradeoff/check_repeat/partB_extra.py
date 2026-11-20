"""Extra checks for Part B: local refinement of the strategic cutoffs, myopic refinement
from every S1's best grid point, and NG robustness of the round-two solver."""
import numpy as np
from scipy.optimize import minimize
from partB import *

sgrid = np.linspace(L, U, 2001)
cache = R2Cache(NG=9)

# 1. strategic local refinement around the fine-grid optimum (and around the claimed one)
for label, (ca, cb) in (('fine-grid optimum', (1.0, 2.2)), ('coarse-grid optimum', (0.8, 2.3))):
    A = np.round(np.arange(ca - 0.1, ca + 0.1001, 0.01), 6)
    B = np.round(np.arange(cb - 0.1, min(cb + 0.1001, 2.49), 0.01), 6)
    profs = [((0, 1), (('cut', float(a)), ('cut', float(b)), ('top',))) for a in A for b in B]
    keys = []
    for S1, k in profs:
        keys += profile_keys(k)
    cache.ensure(keys)
    best = None; npass = 0
    for S1, k in profs:
        res = evaluate(S1, k, cache, 'strategic', sgrid)
        if res is None or not res['eq']:
            continue
        npass += 1
        v = res['R1'] + res['R2']
        if best is None or v > best[0]:
            best = (v, S1, k, res)
    print("local step-0.01 grid around %s: %d/%d pass" % (label, npass, len(profs)))
    summarize("  Strategic (local)", best[1], best[2], best[3])

# 2. myopic: best grid point per S1, then Nelder-Mead
mv = [L + (U - L) * k / 20 for k in range(1, 20)]
best_by = {}
profs = list(all_profiles(mv))
keys = []
for S1, k in profs:
    keys += profile_keys(k)
cache.ensure(keys)
for S1, k in profs:
    res = evaluate(S1, k, cache, 'myopic')
    v = res['R1'] + res['R2']
    if S1 not in best_by or v > best_by[S1][0]:
        best_by[S1] = (v, k)
out = []
for S1, (v, kinds) in best_by.items():
    idx = [i for i in range(NH) if kinds[i][0] == 'cut']
    if not idx:
        out.append((v, S1, kinds)); continue

    def neg(x):
        kk = list(kinds)
        for i, c in zip(idx, x):
            if not (L < c < U):
                return 1e3
            kk[i] = ('cut', float(c))
        kk = tuple(kk)
        cache.ensure(profile_keys(kk))
        r = evaluate(S1, kk, cache, 'myopic')
        return -(r['R1'] + r['R2'])
    o = minimize(neg, [kinds[i][1] for i in idx], method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-11, maxiter=600))
    kk = list(kinds)
    for i, c in zip(idx, o.x):
        kk[i] = ('cut', round(float(c), 6))
    out.append((-o.fun, S1, tuple(kk)))
out.sort(key=lambda r: -r[0])
print("\nmyopic: refined best per round-one slot set (two-round company profit)")
for v, S1, k in out[:8]:
    print("   %.6f %s %s" % (v, ''.join(SLOTN[t] for t in S1) or '-', k))

# 3. NG robustness on a random sample of cached problems
rng = np.random.default_rng(0)
ks = list(cache.d)
sel = [ks[j] for j in rng.choice(len(ks), 3000, replace=False)]
a = np.array([[iv[0] for iv in k] for k in sel]); b = np.array([[iv[1] for iv in k] for k in sel])
v9 = np.array([cache[k][0] for k in sel])
v21, _, _ = solve_round2(a, b, NG=21)
print("\nNG=21 vs NG=9 on 3000 random round-two problems: max |diff| %.3e, max (NG21-NG9) %.3e" % (np.abs(v21 - v9).max(), (v21 - v9).max()))
