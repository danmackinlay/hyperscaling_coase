"""Two rounds of company-made offers on the noise-schedule street (extends rules.py).

Each round the company names a set of slots and offers each household it asks
one rate per unit of exposure.  A slot runs if every household exposed to it
accepts.  Sensitivities persist across the two rounds, and the company cannot
commit in round one to its round-two offers.  The company's profit multiplier m
and its signals are public here; only each household's sensitivity is private.

Regimes
  forget     round-two offers ignore round-one answers (the one-round deal twice)
  myopic     the company uses the answers; households answer each offer on its
             own merits (accept when the rate covers the harm)
  strategic  the company uses the answers and households anticipate that: a
             perfect Bayesian equilibrium in which each asked household accepts
             in round one when its sensitivity is below a cutoff
  unchecked  a diagnostic, not an equilibrium: as strategic, but round-one
             offers are kept even when some household types would rather
             deviate from the cutoff

Usage
  uv run python repeat.py anchor
  uv run python repeat.py population SIGMA [n_draws] [prior] [delta] [workers]
  uv run python repeat.py instance SIGMA [n_draws] [prior] [delta] [workers]
  uv run python repeat.py solo SIGMA [n_draws] [prior] [delta] [workers]     (one household, one slot)
"""

import itertools
import json
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np
from rules import EXPO, INSTANCE_S, M_GRID, QS, P, make_prior, posterior

TOL = 1e-9
CUT_QS = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99)
CUT_QS_FINE = tuple(np.round(np.arange(0.025, 0.976, 0.025), 3)) + (0.99,)  # when one household is exposed
P_SOLO = np.array([0.0, 0.0, 0.0, 5.0])  # Carol alone with the night slot
EXPO_SOLO = np.array([[0.0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2.0]])
REGIMES = ("forget", "myopic", "strategic", "unchecked")


def cands(grid, w, qs=QS, not_asked=True):
    """Rates worth offering a household with belief w, and the chance each is accepted.

    With not_asked, the first candidate is "not asked": rate 0, accepted by nobody.
    """
    cdf = np.cumsum(w)
    cdf = cdf / cdf[-1]
    idx = np.unique(np.minimum(np.searchsorted(cdf, qs - 1e-9), len(grid) - 1))
    if not not_asked:
        return grid[idx], cdf[idx]
    return np.concatenate([[0.0], grid[idx]]), np.concatenate([[0.0], cdf[idx]])


def others_weight(expo, g):
    """a[i, t] = e_it times the chance every other household exposed to t accepts."""
    n, n_slots = expo.shape
    a = np.zeros((n, n_slots))
    for i in range(n):
        for t in range(n_slots):
            if expo[i, t] > 0:
                a[i, t] = expo[i, t] * np.prod([g[j] for j in range(n) if j != i and expo[j, t] > 0])
    return a


def solve_final(grid, ws, m, p, expo):
    """The company's best one-round offers given its beliefs ws.

    Returns (expected profit, rate per household, acceptance chance per
    household, slots named).
    """
    n = len(ws)
    rs, gs = [], []
    for i in range(n):
        r, g = cands(grid, ws[i]) if expo[i].any() else (np.array([0.0]), np.array([1.0]))
        rs.append(r)
        gs.append(g)
    _, r, g, _ = _best(rs, gs, m, p, expo)
    # second pass: quantiles one point apart, around the first pass's choice
    for i in range(n):
        if expo[i].any() and g[i] > 0:
            qs = np.clip(g[i] + np.arange(-0.05, 0.0501, 0.01), 0.002, 1.0)
            rs[i], gs[i] = cands(grid, ws[i], qs, not_asked=False)
        else:
            rs[i], gs[i] = np.array([r[i]]), np.array([g[i]])
    return _best(rs, gs, m, p, expo)


def _best(rs, gs, m, p, expo):
    n = len(rs)
    rr = np.ix_(*rs)
    gg = np.ix_(*gs)
    val = np.zeros(tuple(len(r) for r in rs))
    for t in range(len(p)):
        margin = m * p[t] - sum(expo[i, t] * rr[i] for i in range(n))
        prob = 1.0
        for i in range(n):
            if expo[i, t] > 0:
                prob = prob * gg[i]
        val = val + prob * np.maximum(margin, 0.0)
    k = np.unravel_index(np.argmax(val), val.shape)
    r = np.array([rs[i][k[i]] for i in range(n)])
    g = np.array([gs[i][k[i]] for i in range(n)])
    named = (m * p - r @ expo) > 1e-12
    return float(val[k]), r, g, named


def options(grid, w, exposed, cut_qs):
    """Round-one choices for one household: not asked, asked at a rate every
    type accepts, or asked so that types up to a cutoff accept."""
    if not exposed:
        return [("none", -1, 0.0)]
    cdf = np.cumsum(w)
    cdf = cdf / cdf[-1]
    top = int(min(np.searchsorted(cdf, 1 - 1e-9), len(grid) - 1))
    out = [("none", -1, 0.0), ("all", top, 1.0)]
    seen = set()
    for q in cut_qs:
        k = int(np.searchsorted(cdf, q - 1e-9))
        if k in seen or cdf[k] > 1 - 1e-6:
            continue
        seen.add(k)
        out.append(("cut", k, float(cdf[k])))
    return out


def type_grid(grid, w, k_cut, n_points=41):
    """Indices of the types at which a household's best response is checked."""
    cdf = np.cumsum(w)
    cdf = cdf / cdf[-1]
    lo = int(np.searchsorted(cdf, 1e-3))
    hi = int(min(np.searchsorted(cdf, 1 - 1e-3), len(grid) - 1))
    idx = np.unique(np.concatenate([np.linspace(lo, hi, n_points).astype(int), [max(k_cut - 1, lo), k_cut, min(k_cut + 1, hi)]]))
    return idx


def solve_two_rounds(grid, ws, m, p, expo, delta):
    """Best round-one offers for the company under each regime.

    Returns {regime: equilibrium record}, plus counts of how many candidate
    round-one offers with a cutoff pass the households' best-response check.
    """
    n, n_slots = expo.shape
    cut_qs = CUT_QS_FINE if expo.any(1).sum() == 1 else CUT_QS
    opts = [options(grid, ws[i], expo[i].any(), cut_qs) for i in range(n)]
    slotsets = np.array(list(itertools.product([0, 1], repeat=n_slots)), float)
    exposed = expo > 0
    best = {"myopic": (-np.inf, None), "strategic": (-np.inf, None), "unchecked": (-np.inf, None)}
    n_cut = n_cut_valid = 0

    val0, r0, g0, named0 = solve_final(grid, ws, m, p, expo)
    forget = {"profit": val0 * (1 + delta), "r": r0, "named": named0}

    for choice in itertools.product(*opts):
        kinds = [c[0] for c in choice]
        f = np.array([c[2] for c in choice])
        asked = np.array([k != "none" for k in kinds])
        branch = []
        for i, (kind, k, fi) in enumerate(choice):
            if kind == "cut":
                lo = ws[i].copy()
                lo[k + 1 :] = 0
                hi = ws[i].copy()
                hi[: k + 1] = 0
                branch.append({0: (hi / hi.sum(), 1 - fi), 1: (lo / lo.sum(), fi)})
            elif kind == "all":
                branch.append({1: (ws[i], 1.0)})
            else:
                branch.append({0: (ws[i], 1.0)})
        sols = {}
        v2 = 0.0
        for rho in itertools.product(*[b.keys() for b in branch]):
            prob = float(np.prod([branch[i][rho[i]][1] for i in range(n)]))
            val, r2, g2, named2 = solve_final(grid, [branch[i][rho[i]][0] for i in range(n)], m, p, expo)
            a2 = (others_weight(expo, g2) * named2).sum(1)
            sols[rho] = (prob, r2, named2, a2)
            v2 += prob * val

        # what a household of each type expects from round two after each of its own answers
        cuts = [i for i in range(n) if kinds[i] == "cut"]
        tg, v_acc, v_ref, gain_at_cut = {}, {}, {}, np.zeros(n)
        for i in cuts:
            k = choice[i][1]
            idx = type_grid(grid, ws[i], k)
            s = grid[idx]
            va = np.zeros(len(s))
            vr = np.zeros(len(s))
            g_cut = 0.0
            for rho, (prob, r2, _, a2) in sols.items():
                if rho[i] == 1:
                    va += prob / f[i] * np.where(s <= r2[i] + TOL, r2[i] - s, 0.0) * a2[i]
                else:
                    vr += prob / (1 - f[i]) * np.where(s <= r2[i] + TOL, r2[i] - s, 0.0) * a2[i]
                    g_cut += prob / (1 - f[i]) * max(r2[i] - grid[k], 0.0) * a2[i]
            tg[i], v_acc[i], v_ref[i], gain_at_cut[i] = idx, va, vr, g_cut

        # round one, for every set of slots the company could name
        a1 = others_weight(expo, f)
        e1 = slotsets @ a1.T  # sets x households: expected exposure if the household accepts
        run = np.array([np.prod(f[exposed[:, t]]) for t in range(n_slots)])
        bad_slot = np.array([(exposed[:, t] & ~asked).any() for t in range(n_slots)])
        ok = ~(slotsets[:, bad_slot] > 0).any(1)
        for i in range(n):
            if asked[i]:
                ok &= e1[:, i] > 1e-12
        if not ok.any():
            continue
        base = (slotsets * run * (m * p)).sum(1)
        paid = np.stack([(slotsets * run * expo[i]).sum(1) for i in range(n)], 1)

        r_my = np.zeros((len(slotsets), n))
        r_st = np.zeros((len(slotsets), n))
        valid = ok.copy()
        for i in range(n):
            if kinds[i] == "all":
                r_my[:, i] = r_st[:, i] = grid[choice[i][1]]
            elif kinds[i] == "cut":
                c = grid[choice[i][1]]
                r_my[:, i] = c
                with np.errstate(divide="ignore", invalid="ignore"):
                    r_st[:, i] = np.where(ok, c + delta * gain_at_cut[i] / e1[:, i], 0.0)
                s = grid[tg[i]]
                d = (r_st[:, i, None] - s[None]) * e1[:, i, None] + delta * (v_acc[i] - v_ref[i])[None]
                below = s <= c + TOL
                valid &= (d[:, below] >= -1e-7).all(1) & (d[:, ~below] <= 1e-7).all(1)
        if cuts:
            n_cut += int(ok.sum())
            n_cut_valid += int(valid.sum())

        for name, rates, mask in (("myopic", r_my, ok), ("strategic", r_st, valid), ("unchecked", r_st, ok)):
            if not mask.any():
                continue
            total = np.where(mask, base - (rates * paid).sum(1) + delta * v2, -np.inf)
            j = int(np.argmax(total))
            if total[j] > best[name][0] + 1e-12:
                cutoff = np.array([grid[c[1]] if c[0] == "cut" else (np.inf if c[0] == "all" else -np.inf) for c in choice])
                best[name] = (
                    float(total[j]),
                    {
                        "profit": float(total[j]),
                        "kinds": kinds,
                        "cutoff": cutoff,
                        "accept_prob": f.copy(),
                        "named": slotsets[j] > 0,
                        "r": rates[j].copy(),
                        "sols": {rho: (v[1], v[2]) for rho, v in sols.items()},
                    },
                )
    return {"forget": forget, **{k: v[1] for k, v in best.items()}}, (n_cut, n_cut_valid)


def one_round_gains(s, m, r, named, p, expo):
    """Gains (company, households...) for sensitivities s (samples x households)."""
    n = expo.shape[0]
    g = np.zeros((len(s), n + 1))
    acc = s <= r[None] + TOL
    for t in np.nonzero(named)[0]:
        ex = expo[:, t] > 0
        runs = acc[:, ex].all(1)
        g[:, 0] += runs * (m * p[t] - r @ expo[:, t])
        g[:, 1:] += runs[:, None] * (r[None] - s) * expo[None, :, t]
    return g


def realise(eq, regime, s, m, p, expo, delta):
    """Per-round average gains for sensitivities s under one regime's equilibrium."""
    if regime == "forget":
        return one_round_gains(s, m, eq["r"], eq["named"], p, expo)
    cutoff = eq["cutoff"]
    acc1 = s <= cutoff[None] + TOL
    r1 = eq["r"]
    g = np.zeros((len(s), expo.shape[0] + 1))
    for t in np.nonzero(eq["named"])[0]:
        ex = expo[:, t] > 0
        runs = acc1[:, ex].all(1)
        g[:, 0] += runs * (m * p[t] - r1 @ expo[:, t])
        g[:, 1:] += runs[:, None] * (r1[None] - s) * expo[None, :, t]
    for rho, (r2, named2) in eq["sols"].items():
        mask = (acc1 == np.array(rho, bool)[None]).all(1)
        if mask.any():
            g[mask] += delta * one_round_gains(s[mask], m, r2, named2, p, expo)
    return g / (1 + delta)


def hiding_rate(eq, s):
    """Share of asked households refusing a round-one rate that covers their harm."""
    cut = np.array([k == "cut" for k in eq["kinds"]])
    if not cut.any():
        return 0.0, 0.0
    hid = (s > eq["cutoff"][None] + TOL) & (s <= eq["r"][None] + TOL) & cut[None]
    return float(hid.mean()), float(cut.mean())


def one_draw(args):
    kind, sigma, prior_kind, delta, seed, m, n_samples = args
    rng = np.random.default_rng(seed)
    grid, w = make_prior(prior_kind)
    if kind == "instance":
        s_true = INSTANCE_S.copy()
        m = 1.0
    else:
        s_true = grid[rng.choice(len(grid), size=3, p=w)]
    sg = 0.0 if np.isinf(sigma) else sigma
    signal = s_true + sg * rng.standard_normal(3)
    ws = [posterior(grid, w, signal[i], sigma) for i in range(3)]
    p, expo = (P_SOLO, EXPO_SOLO) if kind == "solo" else (P, EXPO)
    eqs, (n_cut, n_cut_valid) = solve_two_rounds(grid, ws, m, p, expo, delta)
    if kind == "instance":
        s = s_true[None]
    else:  # sensitivities consistent with the public signals
        s = np.stack([grid[rng.choice(len(grid), size=n_samples, p=ws[i])] for i in range(3)], 1)
    out = {"m": m, "n_cut": n_cut, "n_cut_valid": n_cut_valid}
    for regime in REGIMES:
        g = realise(eqs[regime], regime, s, m, p, expo, delta)
        out[regime] = g.mean(0).tolist()
        if regime != "forget":
            out[regime + "_kinds"] = eqs[regime]["kinds"]
            out[regime + "_named1"] = int(eqs[regime]["named"].sum())
            out[regime + "_hiding"] = hiding_rate(eqs[regime], s)
    xs = np.array(list(itertools.product([0, 1], repeat=4)), float)
    out["first_best"] = float((m * (xs @ p)[None] - s @ (xs @ expo.T).T).max(1).mean())
    return out


def summarise(rows):
    res = {"n_draws": len(rows)}
    res["first_best"] = float(np.mean([r["first_best"] for r in rows]))
    res["cut_offers_valid_share"] = float(sum(r["n_cut_valid"] for r in rows) / max(sum(r["n_cut"] for r in rows), 1))
    for regime in REGIMES:
        g = np.array([r[regime] for r in rows])
        d = {
            "total": float(g.sum(1).mean()),
            "total_se": float(g.sum(1).std() / np.sqrt(len(g))),
            "company": float(g[:, 0].mean()),
            "households": float(g[:, 1:].sum(1).mean()),
            "households_se": float(g[:, 1:].sum(1).std() / np.sqrt(len(g))),
            "alice": float(g[:, 1].mean()),
            "bob": float(g[:, 2].mean()),
            "carol": float(g[:, 3].mean()),
        }
        if regime != "forget":
            kinds = [k for r in rows for k in r[regime + "_kinds"]]
            d["share_cut"] = kinds.count("cut") / len(kinds)
            d["share_all"] = kinds.count("all") / len(kinds)
            d["share_none"] = kinds.count("none") / len(kinds)
            d["slots_named_round1"] = float(np.mean([r[regime + "_named1"] for r in rows]))
            d["hiding_rate"] = float(np.mean([r[regime + "_hiding"][0] for r in rows]))
        res[regime] = d
    for a, b in (("strategic", "myopic"), ("strategic", "forget"), ("myopic", "forget"), ("unchecked", "forget")):
        ga = np.array([r[a] for r in rows])
        gb = np.array([r[b] for r in rows])
        dh = ga[:, 1:].sum(1) - gb[:, 1:].sum(1)
        dt = ga.sum(1) - gb.sum(1)
        res[f"{a}-{b}"] = {
            "households": float(dh.mean()),
            "households_se": float(dh.std() / np.sqrt(len(dh))),
            "total": float(dt.mean()),
            "total_se": float(dt.std() / np.sqrt(len(dt))),
        }
    return res


def run(kind, sigma, n_draws, prior_kind, delta, workers):
    if kind == "instance" and np.isinf(sigma):
        n_draws = 1
    n_m = 8  # the multiplier is public here: cycle through equal-probability bins
    ms = M_GRID[0] + (M_GRID[-1] - M_GRID[0]) * (np.arange(n_m) + 0.5) / n_m
    jobs = [(kind, sigma, prior_kind, delta, 1000 + n, float(ms[n % n_m]), 60) for n in range(n_draws)]
    if workers > 1:
        with ProcessPoolExecutor(workers) as ex:
            rows = list(ex.map(one_draw, jobs, chunksize=2))
    else:
        rows = [one_draw(j) for j in jobs]
    return summarise(rows)


def anchor():
    """One household, one slot: compare with the textbook two-round calculation."""
    grid, w = make_prior("uniform")
    p = np.array([3.0, 0.0, 0.0, 0.0])
    expo = np.zeros((3, 4))
    expo[0, 0] = 1.0
    lo, hi, v = 0.5, 2.5, 3.0
    eqs, counts = solve_two_rounds(grid, [w, w, w], 1.0, p, expo, 1.0)

    def one_shot(a, b):  # best rate against a sensitivity uniform on [a, b]
        r = min(b, max(a, (v + a) / 2))
        return r, (v - r) * (r - a) / (b - a)

    best = (-np.inf, None)
    rows = []
    for c in np.linspace(lo, hi, 2001)[1:-1]:
        _, pa = one_shot(lo, c)
        rr, pr = one_shot(c, hi)
        fc = (c - lo) / (hi - lo)
        r1 = c + (rr - c)
        tot = fc * (v - r1) + fc * pa + (1 - fc) * pr
        rows.append((c, r1, tot))
        if tot > best[0]:
            best = (tot, c, r1)
    _, p1 = one_shot(lo, hi)
    print(f"one round, textbook profit {p1:.4f}; code {eqs['forget']['profit'] / 2:.4f}")
    print(f"two rounds strategic, textbook best profit {best[0]:.4f} at cutoff {best[1]:.3f}, rate {best[2]:.3f}")
    e = eqs["strategic"]
    print(f"  code: profit {e['profit']:.4f}, kind {e['kinds'][0]}, cutoff {e['cutoff'][0]:.3f}, rate {e['r'][0]:.3f}")
    c = e["cutoff"][0]
    if np.isfinite(c):
        near = min(rows, key=lambda row: abs(row[0] - c))
        print(f"  textbook at the code's cutoff: rate {near[1]:.3f}, profit {near[2]:.4f}")
    print("  cutoff offers passing the best-response check:", counts)
    e = eqs["myopic"]
    print(f"two rounds myopic, code: profit {e['profit']:.4f}, cutoff {e['cutoff'][0]:.3f}, rate {e['r'][0]:.3f}")


if __name__ == "__main__":
    if sys.argv[1] == "anchor":
        anchor()
        sys.exit()
    kind = sys.argv[1]
    sigma = float(sys.argv[2])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    prior_kind = sys.argv[4] if len(sys.argv) > 4 else "uniform"
    delta = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
    workers = int(sys.argv[6]) if len(sys.argv) > 6 else 6
    t0 = time.time()
    res = run(kind, sigma, n, prior_kind, delta, workers)
    res.update({"kind": kind, "sigma": sigma, "prior": prior_kind, "delta": delta, "seconds": time.time() - t0})
    name = f"repeat_{kind}_{prior_kind}_sigma{sigma}_delta{delta}.json"
    with open(name, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
