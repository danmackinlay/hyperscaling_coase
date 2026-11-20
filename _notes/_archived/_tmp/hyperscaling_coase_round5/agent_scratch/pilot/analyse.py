"""Collate the screen: forty-point table, per-parameter sign/ordering/size verdicts."""
from __future__ import annotations

import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pilot import LEVELS, OUT, lhs  # noqa: E402

SEAT = 1.5
H_ORDER = [1, 3, 10, 50, "T"]


def load(pattern):
    out = []
    for f in sorted(glob.glob(os.path.join(OUT, pattern))):
        out += json.load(open(f))["out"]
    return out


def ptH(label):
    a, b = label.split()
    return int(a[2:]), (b[2:] if b[2:] == "T" else int(b[2:]))


def design_matrix(pts, names):
    cols, owners = [np.ones(len(pts))], [None]
    for n in names:
        lev = LEVELS[n]
        for lv in lev[1:]:
            cols.append(np.array([1.0 if str(p[n]) == str(lv) else 0.0 for p in pts]))
            owners.append(n)
    return np.array(cols).T, owners


def ols_partial(X, owners, y, names):
    """Partial F test for each parameter's dummies; adjusted level effects."""
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    rss_full = ((y - X @ beta) ** 2).sum()
    n, k = X.shape
    dof = n - k
    res = {}
    for nm in names:
        keep = [i for i, o in enumerate(owners) if o != nm]
        b2, *_ = np.linalg.lstsq(X[:, keep], y, rcond=None)
        rss_red = ((y - X[:, keep] @ b2) ** 2).sum()
        q = k - len(keep)
        F = ((rss_red - rss_full) / q) / (rss_full / dof) if dof > 0 and rss_full > 0 else np.nan
        try:
            from scipy.stats import f as fdist

            p = 1 - fdist.cdf(F, q, dof)
        except Exception:
            p = np.nan
        eff = [0.0] + [beta[i] for i, o in enumerate(owners) if o == nm]
        res[nm] = dict(F=F, p=p, eff=eff, span=max(eff) - min(eff))
    return res, dof


def level_means(pts, y, nm):
    out = {}
    for lv in LEVELS[nm]:
        idx = [i for i, p in enumerate(pts) if str(p[nm]) == str(lv)]
        out[str(lv)] = (float(np.mean(y[idx])), len(idx), float(np.mean(y[idx] > SEAT)))
    return out


def main():
    pts = lhs()
    sc = sys.argv[1] if len(sys.argv) > 1 else "own_offer"
    print(f"scoring reading: {sc}; design seed 1; run seeds [1, r], r = 0..49")
    own = {ptH(s["label"])[0]: s for s in load(f"lhs_{sc}_*_own.json")}
    prof = {}
    for s in load(f"lhs_{sc}_*.json"):
        i, h = ptH(s["label"])
        prof.setdefault(i, {})[str(h)] = s
    ids = sorted(own)
    P = np.array([own[i]["P"] for i in ids])
    se = np.array([own[i]["P_se"] for i in ids])
    names = list(LEVELS)
    sub = [pts[i] for i in ids]

    # ---- the table
    hdr = "| pt | eta | step | /scale | H | T | win | margins | feedback | play | planner dyn | P take (se) | R1 | R2 | R3 | deal | floor | GM/max | P-1.5 | cpu s/pt |"
    print(hdr)
    print("|" + "|".join(["---"] * (hdr.count("|") - 1)) + "|")
    for i in ids:
        p, s = pts[i], own[i]
        sign = "+" if s["P"] - SEAT > 2 * s["P_se"] else ("-" if SEAT - s["P"] > 2 * s["P_se"] else "0")
        print(f"| {i} | {p['eta']} | {p['step']} | {p['scale']:g} | {p['H']} | {p['T']} | {p['window']} | {p['margins']} | {p['feedback']} | {p['play']} | {p['dyn']} | "
              f"{s['P']:.3f} ({s['P_se']:.3f}) | {s['R1']:.3f} | {s['R2']:.3f} | {s['R3']:.3f} | {s['deal']:.3f} | {s['floor']:.3f} | {s['gm_frac']:.3f} | {sign}{abs(s['P']-SEAT):.3f} | {s['cpu_sec']:.0f} |")

    # ---- per-parameter: sign and size
    X, owners = design_matrix(sub, names)
    sgn = (P > SEAT).astype(float)
    size, dof = ols_partial(X, owners, P, names)
    sres, _ = ols_partial(X, owners, sgn, names)
    print(f"\nOLS on dummies, residual dof {dof}; n points {len(ids)}; points above 1.5: {int(sgn.sum())}")
    for nm in names:
        lm = level_means(sub, P, nm)
        print(f"{nm}: size partial F={size[nm]['F']:.2f} p={size[nm]['p']:.3f} adj-span={size[nm]['span']:.3f}; "
              f"sign LPM F={sres[nm]['F']:.2f} p={sres[nm]['p']:.3f}; level means (mean P, n, frac>1.5): "
              + "; ".join(f"{k}: {v[0]:.2f}/{v[1]}/{v[2]:.2f}" for k, v in lm.items()))

    # ---- ordering across H, from the profile
    if prof:
        print("\nH profile (principal take by H):")
        Delta, ordr, pi = [], [], []
        for i in ids:
            row = {**{str(own[i]["cfg"]["H"]): own[i]}, **prof.get(i, {})}
            vals = [(h, row[str(h)]["P"], row[str(h)]["P_se"]) for h in H_ORDER if str(h) in row]
            if len(vals) < 4:
                continue
            hs = [v[0] for v in vals]
            ps = np.array([v[1] for v in vals])
            ses = np.array([v[2] for v in vals])
            r_hi, r_lo = np.array(row[str(hs[-1])]["P_runs"]), np.array(row[str(hs[0])]["P_runs"])
            d = ps[-1] - ps[0]
            noise = 2 * (r_hi - r_lo).std(ddof=1) / np.sqrt(len(r_hi))  # paired: same run seeds at every H
            o = "up" if d > noise else ("down" if d < -noise else "flat")
            rank = "".join(str(int(r)) for r in np.argsort(np.argsort(-ps)) + 1)
            print(f"pt{i}: " + ", ".join(f"H={h}:{p:.3f}" for h, p in zip(hs, ps)) + f" | P(Hmax)-P(1)={d:+.3f} (2se {noise:.3f}) {o} | rank by take {rank}")
            Delta.append(d)
            ordr.append(o)
            pi.append(i)
        Delta = np.array(Delta)
        sub2 = [pts[i] for i in pi]
        names2 = [n for n in names if n != "H"]
        X2, ow2 = design_matrix(sub2, names2)
        dres, dof2 = ols_partial(X2, ow2, Delta, names2)
        up = np.array([o == "up" for o in ordr], float)
        ures, _ = ols_partial(X2, ow2, up, names2)
        print(f"\nordering: up {sum(o=='up' for o in ordr)}, flat {sum(o=='flat' for o in ordr)}, down {sum(o=='down' for o in ordr)}; dof {dof2}")
        for nm in names2:
            lm = {}
            for lv in LEVELS[nm]:
                idx = [k for k, p in enumerate(sub2) if str(p[nm]) == str(lv)]
                lm[str(lv)] = (np.mean(Delta[idx]), len(idx), "".join(ordr[k][0] for k in idx))
            print(f"{nm}: Delta partial F={dres[nm]['F']:.2f} p={dres[nm]['p']:.3f} adj-span={dres[nm]['span']:.3f}; up-LPM p={ures[nm]['p']:.3f}; "
                  + "; ".join(f"{k}: {v[0]:+.2f}/{v[1]}/{v[2]}" for k, v in lm.items()))

    # ---- cost per point by the parameters that drive it
    cpu = np.array([own[i]["cpu_sec"] for i in ids])
    print("\ncpu seconds per point (50 runs, single core): median %.0f, max %.0f" % (np.median(cpu), cpu.max()))
    for nm in names:
        print(nm, {str(lv): round(float(np.mean([own[i]["cpu_sec"] for i in ids if str(pts[i][nm]) == str(lv)])), 1) for lv in LEVELS[nm]})


if __name__ == "__main__":
    main()
