import json
import sys
import time

import numpy as np

import model as M

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
NW = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
rng = np.random.default_rng(20261118)
s = rng.uniform(0.5, 2.5, (3, N))
m = rng.uniform(0.6, 1.4, N)
# independent standard-normal noise per (observer, target)
z_c = rng.standard_normal((3, N))  # company's signals of households
z_h = rng.standard_normal((3, 3, N))  # z_h[j, i]: household j's signal of household i
z_hm = rng.standard_normal((3, N))  # household j's signal of m

out = {}


def ms(x):
    return [float(x.mean()), float(x.std(ddof=1) / np.sqrt(x.size))]


def summ(comp, hh):
    return dict(total=ms(comp + hh.sum(0)), company=ms(comp), households=ms(hh.sum(0)),
                each=[ms(h) for h in hh])


def run_A(s, m, ins, sigma, z_c):
    sig = s + (0 if np.isinf(sigma) else sigma) * z_c
    return M.offer_maker(s, m, ins, -1, sig, m, sigma)


def run_seat(s, m, ins, sigma, z_h, z_hm):
    cs, hs = [], []
    for j in range(3):
        k = 0 if np.isinf(sigma) else sigma
        sig = s + k * z_h[j]
        sm = m + 0.4 * k * z_hm[j]
        c, h = M.offer_maker(s, m, ins, j, sig, sm, sigma)
        cs.append(c)
        hs.append(h)
    return sum(cs) / 3, sum(hs) / 3


t0 = time.time()
for ins in (False, True):
    key = "on" if ins else "off"
    o = out[key] = {}
    o["full_info"] = ms(M.full_info(s, m, ins))
    A = {}
    for sigma in (np.inf, 0.3, 0.1, 0.0):
        A[sigma] = run_A(s, m, ins, sigma, z_c)
        o[f"A_{sigma}"] = summ(*A[sigma])
        print(key, "A", sigma, time.time() - t0, flush=True)
    seat = {}
    for sigma in (0.3, 0.0):
        seat[sigma] = run_seat(s, m, ins, sigma, z_h, z_hm)
        o[f"seat_{sigma}"] = summ(*seat[sigma])
        print(key, "seat", sigma, time.time() - t0, flush=True)
    cC = 0.25 * A[0.3][0] + 0.75 * seat[0.3][0]
    hC = 0.25 * A[0.3][1] + 0.75 * seat[0.3][1]
    o["C_0.3"] = summ(cC, hC)
    for r in (1.5, 1.9, 2.0, 2.5):
        for name, cons in (("B1", True), ("B2", False)):
            for pref in (False, True):
                c, h, ties = M.uniform_rate(s, m, ins, r, cons, pref)
                d = summ(c, h)
                d["tie_frac"] = float(ties.mean())
                d["p_neg_each"] = [ms((hi < -1e-12).astype(float)) for hi in h]
                d["p_neg_avg"] = ms((h < -1e-12).mean(0).astype(float))
                o[f"{name}_{r}" + ("_insulate_on_tie" if pref else "")] = d

# Worked case
ws_ = np.tile(np.array([[1.0], [1.0], [2.0]]), (1, NW))
wm = np.ones(NW)
zw = rng.standard_normal((3, NW))
W = out["worked"] = {}
for ins in (False, True):
    key = "on" if ins else "off"
    for sigma in (0.3, 0.1):
        W[f"A_{sigma}_{key}"] = summ(*run_A(ws_, wm, ins, sigma, zw))
    for r in (1.9, 2.0, 2.5):
        for name, cons in (("B1", True), ("B2", False)):
            for pref in (False, True):
                c, h, ties = M.uniform_rate(ws_[:, :1], wm[:1], ins, r, cons, pref)
                W[f"{name}_{r}_{key}" + ("_insulate_on_tie" if pref else "")] = dict(
                    total=float(c[0] + h[:, 0].sum()), company=float(c[0]),
                    each=[float(x) for x in h[:, 0]], tie=bool(ties[0]))
print("time", time.time() - t0)
json.dump(out, open(f"/Users/dan/Source/livingthing/_tmp/coase_rule_tradeoff/check/out_{N}.json", "w"), indent=1)
