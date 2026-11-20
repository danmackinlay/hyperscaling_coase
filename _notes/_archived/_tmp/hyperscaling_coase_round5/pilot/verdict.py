"""Per-parameter verdicts: sign of (P - 1.5), ordering across H, largest change, cost.
Sources: the forty-point screen (between points), its H profile (within point, paired seeds),
and one-factor-at-a-time runs around the stated cell (paired seeds)."""
from __future__ import annotations

import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pilot import LEVELS, OUT, lhs  # noqa: E402

SEAT = 1.5
sc = sys.argv[1] if len(sys.argv) > 1 else "own_offer"
pts = lhs()


def loadf(pat):
    out = []
    for f in sorted(glob.glob(os.path.join(OUT, pat))):
        out += json.load(open(f))["out"]
    return out


def sgn(s):
    d = s["P"] - SEAT
    return "+" if d > 2 * s["P_se"] else ("-" if d < -2 * s["P_se"] else "0")


# ---------------- screen + profile
cells = {}
for s in loadf(f"lhs_{sc}_*.json"):
    a, b = s["label"].split()
    cells.setdefault(int(a[2:]), {})[b[2:]] = s
own = {i: cells[i][str(pts[i]["H"])] for i in cells}
degenerate = {i for i in own if pts[i]["play"] == "expected" and pts[i]["feedback"] == "bandit"}

Hk = ["1", "3", "10", "50", "T"]
order = {}
for i, row in cells.items():
    hs = [h for h in Hk if h in row]
    if len(hs) < 4:
        continue
    lo, hi = row[hs[0]], row[hs[-1]]
    n = min(len(hi["P_runs"]), len(lo["P_runs"]))  # run seeds [1, r], r < n, are common
    diff = np.array(hi["P_runs"][:n]) - np.array(lo["P_runs"][:n])
    d, se = diff.mean(), diff.std(ddof=1) / np.sqrt(len(diff))
    # monotone? count adjacent steps that move beyond 2 paired se
    steps = []
    for h1, h2 in zip(hs, hs[1:]):
        n2 = min(len(row[h2]["P_runs"]), len(row[h1]["P_runs"]))
        dd = np.array(row[h2]["P_runs"][:n2]) - np.array(row[h1]["P_runs"][:n2])
        m, e = dd.mean(), dd.std(ddof=1) / np.sqrt(len(dd))
        steps.append("+" if m > max(2 * e, 0.01) else ("-" if m < -max(2 * e, 0.01) else "0"))
    order[i] = dict(hs=hs, P=[row[h]["P"] for h in hs], d=d, se=se,
                    cls="up" if d > max(2 * se, 0.01) else ("down" if d < -max(2 * se, 0.01) else "flat"), steps="".join(steps),
                    signs="".join(sgn(row[h]) for h in hs))

print(f"== scoring reading {sc}; LHS seed 1; run seeds [1,r]; degenerate (expected play + bandit) points: {sorted(degenerate)}")
print("\n== H profile per point (P by H; paired P(Hmax)-P(1); adjacent-step signs; sign of P-1.5 at each H)")
for i in sorted(order):
    o = order[i]
    print(f"pt{i:2d} " + " ".join(f"{h}:{p:.3f}" for h, p in zip(o['hs'], o['P'])) +
          f" | d={o['d']:+.3f}±{2*o['se']:.3f} {o['cls']:4s} steps {o['steps']} | sign {o['signs']}" + (" [degenerate]" if i in degenerate else ""))


def coded(p):
    H = p["T"] if p["H"] == "T" else p["H"]
    return [np.log2(p["eta"]), np.log2(p["step"]), np.log2(p["scale"]), np.log2(H), np.log2(p["T"]), p["window"] / 100,
            p["margins"] == "small", p["margins"] == "line", p["feedback"] == "bandit", p["play"] == "expected",
            p["dyn"] == "roll1", p["dyn"] == "roll5"]


names = ["log2 eta", "log2 step", "log2 scale", "log2 H", "log2 T", "window/100", "margins small", "margins line",
         "bandit", "expected play", "dyn roll1", "dyn roll5"]
span = [np.log2(25), np.log2(4), 2, np.log2(2000), np.log2(10), 2, 1, 1, 1, 1, 1, 1]


def ols(ids, y):
    X = np.array([[1.0] + [float(v) for v in coded(pts[i])] for i in ids])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    dof = len(y) - X.shape[1]
    s2 = (r @ r) / dof
    cov = s2 * np.linalg.pinv(X.T @ X)
    return b[1:], np.sqrt(np.diag(cov))[1:], dof, 1 - r.var() / y.var()


for label, ids in [("all 40", sorted(own)), ("excluding the degenerate expected+bandit points", sorted(set(own) - degenerate))]:
    y = np.array([own[i]["P"] for i in ids])
    b, se, dof, r2 = ols(ids, y)
    ys = np.array([float(own[i]["P"] > SEAT) for i in ids])
    bs, ses, _, r2s = ols(ids, ys)
    print(f"\n== compact OLS on {label}: n={len(ids)}, dof={dof}, R2(P)={r2:.2f}, R2(sign)={r2s:.2f}")
    print("regressor | coef on P (se) | change over the screened range | coef on 1[P>1.5] (se)")
    for k, nm in enumerate(names):
        print(f"{nm} | {b[k]:+.3f} ({se[k]:.3f}) | {b[k]*span[k]:+.3f} | {bs[k]:+.3f} ({ses[k]:.3f})")

ids = [i for i in order if i not in degenerate]
if ids:
    y = np.array([order[i]["d"] for i in ids])
    b, se, dof, r2 = ols(ids, y)
    print(f"\n== OLS of P(Hmax)-P(1) on the other parameters (non-degenerate points with a profile): n={len(ids)}, dof={dof}, R2={r2:.2f}")
    for k, nm in enumerate(names):
        if nm == "log2 H":
            continue
        print(f"{nm} | {b[k]:+.3f} ({se[k]:.3f}) | {b[k]*span[k]:+.3f}")
    for nm, lev in LEVELS.items():
        if nm == "H":
            continue
        parts = []
        for lv in lev:
            g = [order[i] for i in ids if str(pts[i][nm]) == str(lv)]
            parts.append(f"{lv}: n={len(g)} up/flat/down={sum(o['cls']=='up' for o in g)}/{sum(o['cls']=='flat' for o in g)}/{sum(o['cls']=='down' for o in g)} mean d={np.mean([o['d'] for o in g]) if g else float('nan'):+.3f}")
        print(f"ordering by {nm}: " + "; ".join(parts))

# ---------------- one factor at a time around the stated cell
st = {}
for f in glob.glob(os.path.join(OUT, f"stated_{sc}_seed1_n50_*.json")):
    for s in json.load(open(f))["out"]:
        if s["label"].startswith("stated"):
            st[s["label"].split("H=")[1]] = s
oat = {}
for s in loadf(f"oat_{sc}_seed1.json"):
    _, kv, h = s["label"].split()
    oat.setdefault(kv, {})[h[2:]] = s
if oat:
    print("\n== one factor at a time from the stated cell (seed 1, paired runs). P at H=1 / 10 / T; sign of P-1.5; P(T)-P(1) paired")
    rows = [("stated", st)] + sorted(oat.items())
    for kv, row in rows:
        hs = [h for h in ["1", "10", "T"] if h in row]
        line = " / ".join(f"{row[h]['P']:.3f}" for h in hs)
        signs = "".join(sgn(row[h]) for h in hs)
        dd = ""
        if "1" in row and "T" in row and len(row["1"]["P_runs"]) == len(row["T"]["P_runs"]):
            diff = np.array(row["T"]["P_runs"]) - np.array(row["1"]["P_runs"])
            dd = f"{diff.mean():+.3f}±{2*diff.std(ddof=1)/np.sqrt(len(diff)):.3f}"
        elif "1" in row and "T" in row:
            n = len(row["T"]["P_runs"])
            diff = np.array(row["T"]["P_runs"]) - np.array(row["1"]["P_runs"][:n])
            dd = f"{diff.mean():+.3f}±{2*diff.std(ddof=1)/np.sqrt(n):.3f} (n={n})"
        cost = " / ".join(f"{row[h]['cpu_sec']/row[h]['n_runs']:.1f}" for h in hs)
        print(f"{kv:22s} P {line} | sign {signs} | P(T)-P(1) {dd} | deal {row[hs[-1]]['deal']:.3f} | cpu s/run {cost}")
