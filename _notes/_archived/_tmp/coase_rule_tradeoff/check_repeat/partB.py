"""Part B: the street, sigma = inf. Exact integration (uniform beliefs, closed forms)."""
import itertools
import sys
import time
import numpy as np
from street import (L, U, P, EXP, NH, SUBSETS, SLOTN, exposed, solve_round2,
                    exposure_after, gain_integral, profit)

DELTA = 1.0
NAMES = ['Alice', 'Bob', 'Carol']
PRIOR = (L, U)


def outcomes(kind):
    """List of (answer, prob, interval) for one household's round-one answer."""
    if kind[0] in ('none', 'top'):
        return [('accept' if kind[0] == 'top' else 'none', 1.0, PRIOR)]
    c = kind[1]
    pa = (c - L) / (U - L)
    return [('accept', pa, (L, c)), ('refuse', 1 - pa, (c, U))]


class R2Cache:
    def __init__(self, NG=9):
        self.d = {}
        self.NG = NG

    def ensure(self, keys):
        new = [k for k in set(keys) if k not in self.d]
        if not new:
            return
        a = np.array([[iv[0] for iv in k] for k in new])
        b = np.array([[iv[1] for iv in k] for k in new])
        v, r, s = solve_round2(a, b, NG=self.NG)
        for j, k in enumerate(new):
            S = SUBSETS[s[j]] if s[j] >= 0 else ()
            X = np.array([exposure_after(S, r[j], a[j], b[j], i) if S else 0.0 for i in range(NH)])
            self.d[k] = (v[j], r[j].copy(), S, X)

    def __getitem__(self, k):
        return self.d[k]


def profile_keys(kinds):
    outs = [outcomes(k) for k in kinds]
    return [tuple(o[2] for o in combo) for combo in itertools.product(*outs)]


def evaluate(S1, kinds, cache, regime, sgrid=None):
    """kinds: per household ('none',) | ('top',) | ('cut', c). For regime 'myopic', c is the rate."""
    outs = [outcomes(k) for k in kinds]
    combos = list(itertools.product(*outs))
    pacc = np.array([1.0 if k[0] == 'top' else (0.0 if k[0] == 'none' else (k[1] - L) / (U - L)) for k in kinds])
    cut = np.array([U if k[0] == 'top' else (k[1] if k[0] == 'cut' else np.nan) for k in kinds])
    # round-one expected exposure E_i
    E = np.zeros(NH)
    for i in range(NH):
        for t in S1:
            if EXP[i, t] > 0:
                q = np.prod([pacc[j] for j in range(NH) if j != i and EXP[j, t] > 0])
                E[i] += EXP[i, t] * q
    r1 = np.zeros(NH)
    info = {}
    for i in range(NH):
        if kinds[i][0] == 'top':
            r1[i] = U
        elif kinds[i][0] == 'cut':
            c = kinds[i][1]
            if regime == 'myopic':
                r1[i] = c
            else:
                if E[i] <= 0:
                    return None
                G = 0.0
                for combo in combos:
                    if combo[i][0] != 'refuse':
                        continue
                    pr = np.prod([combo[j][1] for j in range(NH) if j != i])
                    v, r, S, X = cache[tuple(o[2] for o in combo)]
                    G += pr * max(r[i] - c, 0.0) * X[i]
                r1[i] = c + DELTA * G / E[i]
                info.setdefault('G', {})[i] = G
    # company round one
    R1 = 0.0
    for t in S1:
        hh = [j for j in range(NH) if EXP[j, t] > 0]
        R1 += np.prod(pacc[hh]) * (P[t] - sum(r1[j] * EXP[j, t] for j in hh))
    # household round-one gains
    H1 = np.zeros(NH)
    for i in range(NH):
        if kinds[i][0] in ('cut', 'top'):
            c = cut[i]
            Eg = (c - L) / (U - L) * (r1[i] - (L + c) / 2)
            H1[i] = E[i] * Eg
    R2 = 0.0
    H2 = np.zeros(NH)
    for combo in combos:
        pr = np.prod([o[1] for o in combo])
        key = tuple(o[2] for o in combo)
        v, r, S, X = cache[key]
        R2 += pr * v
        for i in range(NH):
            if X[i] > 0:
                H2[i] += pr * X[i] * gain_integral(r[i], key[i][0], key[i][1])
    res = dict(R1=R1, R2=R2, H1=H1, H2=H2, r1=r1, E=E, pacc=pacc, **info)
    if regime == 'strategic' and sgrid is not None:
        res['eq'], res['eq_detail'] = eq_check(kinds, combos, cache, r1, E, sgrid)
    return res


def eq_check(kinds, combos, cache, r1, E, sgrid, tol=1e-9):
    ok = True
    detail = {}
    for i in range(NH):
        if kinds[i][0] != 'cut':
            continue
        c = kinds[i][1]
        Vacc = np.zeros_like(sgrid); Vref = np.zeros_like(sgrid)
        Xref = 0.0
        for combo in combos:
            pr = np.prod([combo[j][1] for j in range(NH) if j != i])
            v, r, S, X = cache[tuple(o[2] for o in combo)]
            g = pr * np.maximum(r[i] - sgrid, 0.0) * X[i]
            if combo[i][0] == 'accept':
                Vacc += g
            else:
                Vref += g
                Xref += pr * X[i]
        D = (r1[i] - sgrid) * E[i] + DELTA * (Vacc - Vref)
        below = D[sgrid < c].min() if np.any(sgrid < c) else 0.0
        above = (-D[sgrid > c]).min() if np.any(sgrid > c) else 0.0
        okk = below >= -tol and above >= -tol
        detail[i] = dict(min_below=below, min_above=above, Xref=Xref, E=E[i])
        ok = ok and okk
    return ok, detail


def summarize(name, S1, kinds, res):
    comp = (res['R1'] + DELTA * res['R2']) / (1 + DELTA)
    hh = (res['H1'] + DELTA * res['H2']) / (1 + DELTA)
    print("%s: per-round total %.6f company %.6f households %.6f (A %.6f B %.6f C %.6f)" % (
        name, comp + hh.sum(), comp, hh.sum(), *hh))
    print("   round-one slots %s; kinds %s; rates %s" % (
        ''.join(SLOTN[t] for t in S1) or '-', kinds, np.round(res['r1'], 6)))
    print("   R1 %.6f R2 %.6f E %s" % (res['R1'], res['R2'], np.round(res['E'], 6)))
    if 'eq_detail' in res:
        print("   eq check:", res['eq'], {NAMES[i]: {k: round(float(v), 6) for k, v in d.items()} for i, d in res['eq_detail'].items()})


def all_profiles(cut_values):
    opts = [('top',)] + [('cut', c) for c in cut_values]
    yield (), (('none',),) * NH
    for S1 in SUBSETS:
        H1 = exposed(S1)
        for choice in itertools.product(opts, repeat=len(H1)):
            kinds = [('none',)] * NH
            for i, k in zip(H1, choice):
                kinds[i] = k
            yield S1, tuple(kinds)


def run_grid(cut_values, regime, cache, sgrid):
    profs = list(all_profiles(cut_values))
    keys = []
    for S1, kinds in profs:
        keys.extend(profile_keys(kinds))
    t = time.time()
    cache.ensure(keys)
    print("  [%s] %d profiles, %d round-two problems solved in %.1fs" % (regime, len(profs), len(cache.d), time.time() - t))
    best = None
    n_cut = n_cut_pass = 0
    n_all = n_all_pass = 0
    rows = []
    for S1, kinds in profs:
        res = evaluate(S1, kinds, cache, regime, sgrid if regime == 'strategic' else None)
        has_cut = any(k[0] == 'cut' for k in kinds)
        if regime == 'strategic':
            n_all += 1
            passed = res is not None and res['eq']
            n_all_pass += passed
            if has_cut:
                n_cut += 1
                n_cut_pass += passed
            if not passed:
                continue
        val = res['R1'] + DELTA * res['R2']
        rows.append((val, S1, kinds))
        if best is None or val > best[0] + 1e-12:
            best = (val, S1, kinds, res)
    if regime == 'strategic':
        print("  equilibrium check: %d/%d profiles with >=1 cut household pass (%.4f); %d/%d of all profiles incl. no-cut ones" % (
            n_cut_pass, n_cut, n_cut_pass / n_cut, n_all_pass, n_all))
    rows.sort(key=lambda r: -r[0])
    return best, rows


def main():
    sgrid = np.linspace(L, U, 2001)
    cache = R2Cache(NG=int(sys.argv[1]) if len(sys.argv) > 1 else 9)
    # forget
    cache.ensure([(PRIOR,) * NH])
    v, r, S, X = cache[(PRIOR,) * NH]
    hh = np.array([X[i] * gain_integral(r[i], L, U) if X[i] > 0 else 0 for i in range(NH)])
    print("Forget: per-round total %.6f company %.6f households %.6f (A %.6f B %.6f C %.6f); offer slots %s rates %s" % (
        v + hh.sum(), v, hh.sum(), *hh, ''.join(SLOTN[t] for t in S), np.round(r, 6)))

    coarse_q = [0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 0.97, 0.99]
    fine_q = sorted(set([round(0.05 * k, 4) for k in range(1, 20)] + [0.97, 0.98, 0.99, 0.995]))
    for label, qs in (('coarse', coarse_q), ('fine', fine_q)):
        cv = [L + (U - L) * q for q in qs]
        print("\n=== cutoff grid %s: quantiles %s" % (label, qs))
        best, rows = run_grid(cv, 'strategic', cache, sgrid)
        summarize("Strategic", best[1], best[2], best[3])
        print("   top 5 equilibrium profiles (two-round company profit):")
        for val, S1, kinds in rows[:5]:
            print("     %.6f %s %s" % (val, ''.join(SLOTN[t] for t in S1) or '-', kinds))

    # myopic: grid in rates then local refinement
    mv = [L + (U - L) * k / 20 for k in range(1, 20)]
    print("\n=== myopic, rate grid step 0.1")
    best, rows = run_grid(mv, 'myopic', cache, sgrid)
    summarize("Myopic (grid)", best[1], best[2], best[3])
    print("   top 5:")
    for val, S1, kinds in rows[:5]:
        print("     %.6f %s %s" % (val, ''.join(SLOTN[t] for t in S1) or '-', kinds))
    # refine: coordinate search with shrinking step on the cut rates of the best few
    from scipy.optimize import minimize
    finals = []
    for val, S1, kinds in rows[:5]:
        idx = [i for i in range(NH) if kinds[i][0] == 'cut']
        if not idx:
            finals.append((val, S1, kinds)); continue

        def neg(x):
            kk = list(kinds)
            for i, c in zip(idx, x):
                if not (L < c < U):
                    return 1e3
                kk[i] = ('cut', float(c))
            kk = tuple(kk)
            cache.ensure(profile_keys(kk))
            res = evaluate(S1, kk, cache, 'myopic')
            return -(res['R1'] + DELTA * res['R2'])
        x0 = [kinds[i][1] for i in idx]
        o = minimize(neg, x0, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, initial_simplex=None, maxiter=400))
        kk = list(kinds)
        for i, c in zip(idx, o.x):
            kk[i] = ('cut', float(c))
        finals.append((-o.fun, S1, tuple(kk)))
    finals.sort(key=lambda r: -r[0])
    val, S1, kinds = finals[0]
    res = evaluate(S1, kinds, cache, 'myopic')
    summarize("Myopic (refined)", S1, kinds, res)
    for val, S1, kinds in finals:
        print("     %.6f %s %s" % (val, ''.join(SLOTN[t] for t in S1) or '-', kinds))


if __name__ == '__main__':
    main()
