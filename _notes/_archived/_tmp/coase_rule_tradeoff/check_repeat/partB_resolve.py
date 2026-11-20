"""Re-solve the round-two problems of the top strategic/myopic profiles with NG=25 (vs NG=9)."""
import numpy as np, time
import partB
from partB import *

sgrid = np.linspace(L, U, 2001)
coarse_q = [0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 0.97, 0.99]
fine_q = sorted(set([round(0.05 * k, 4) for k in range(1, 20)] + [0.97, 0.98, 0.99, 0.995]))
TOP = 400
for label, qs in (('coarse', coarse_q), ('fine', fine_q)):
    cache = R2Cache(NG=9)
    cv = [L + (U - L) * q for q in qs]
    best, rows = run_grid(cv, 'strategic', cache, sgrid)
    print("  NG=9 best %.6f; %d-th best %.6f" % (rows[0][0], TOP, rows[min(TOP, len(rows)) - 1][0]))
    keys = set()
    for v, S1, k in rows[:TOP]:
        keys |= set(profile_keys(k))
    keys = list(keys)
    a = np.array([[iv[0] for iv in k] for k in keys]); b = np.array([[iv[1] for iv in k] for k in keys])
    t = time.time()
    v, r, s = solve_round2(a, b, NG=25)
    old = np.array([cache[k][0] for k in keys])
    print("  re-solved %d problems at NG=25 in %.0fs: max improvement %.3e, count >1e-9: %d" % (len(keys), time.time() - t, (v - old).max(), ((v - old) > 1e-9).sum()))
    for j, k in enumerate(keys):
        S = SUBSETS[s[j]] if s[j] >= 0 else ()
        X = np.array([exposure_after(S, r[j], a[j], b[j], i) if S else 0.0 for i in range(NH)])
        cache.d[k] = (v[j], r[j].copy(), S, X)
    new = []
    for _, S1, k in rows[:TOP]:
        res = evaluate(S1, k, cache, 'strategic', sgrid)
        if res is not None and res['eq']:
            new.append((res['R1'] + res['R2'], S1, k, res))
    new.sort(key=lambda z: -z[0])
    print("  after re-solve: %d/%d of top profiles still pass" % (len(new), TOP))
    summarize("Strategic %s (NG=25 re-solve)" % label, new[0][1], new[0][2], new[0][3])
    for z in new[:4]:
        print("     %.6f %s %s" % (z[0], ''.join(SLOTN[t] for t in z[1]), z[2]))
