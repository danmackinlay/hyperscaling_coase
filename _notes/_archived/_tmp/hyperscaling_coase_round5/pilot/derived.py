"""P take against the learning budget eta*T/scale, by play rule and feedback (screen, seed 1)."""
import sys, json, glob; sys.path.insert(0,'.')
import numpy as np
from pilot import lhs, OUT
sc = sys.argv[1] if len(sys.argv) > 1 else "own_offer"
pts = lhs()
own = {}
for f in glob.glob(f"{OUT}/lhs_{sc}_*_own.json"):
    for s in json.load(open(f))["out"]:
        own[int(s["label"].split()[0][2:])] = s
rows = []
for i, s in sorted(own.items()):
    p = pts[i]; L = p["eta"] * p["T"] / p["scale"]
    rows.append((p["play"], p["feedback"], L, s["P"], s["deal"], i, p["H"]))
for play in ["sampled", "expected"]:
    for fb in ["full", "bandit"]:
        r = sorted([x for x in rows if x[0] == play and x[1] == fb], key=lambda x: x[2])
        print(play, fb, " ".join(f"[pt{x[5]} L={x[2]:.1f} H={x[6]} P={x[3]:.2f} deal={x[4]:.2f}]" for x in r))
samp = [x for x in rows if x[0] == "sampled"]
lL = np.log([x[2] for x in samp]); P = np.array([x[3] for x in samp]); fb = np.array([x[1] == "bandit" for x in samp], float)
X = np.c_[np.ones_like(lL), lL, fb]
b, *_ = np.linalg.lstsq(X, P, rcond=None)
res = P - X @ b
print("sampled play: P ~ %.3f + %.3f log(L) %+.3f bandit; R2=%.2f; n=%d" % (b[0], b[1], b[2], 1 - res.var() / P.var(), len(P)))
print("crossing 1.5 at L = %.1f (full information)" % np.exp((1.5 - b[0]) / b[1]))
