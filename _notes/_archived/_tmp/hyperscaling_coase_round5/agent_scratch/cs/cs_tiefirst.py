"""Chipty-Snyder curvature on the noise schedule: residents bargaining one by one
(proposer drawn by party, stationary SPE) vs as a club (proposer drawn by side),
at consent rule k=3 and k=2. Base instance numbers."""
import itertools, math
import numpy as np

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1, 1, 2.0])
H = (E * s[:, None])            # harm per slot per resident
X = [np.array(x) for x in itertools.product([0, 1], repeat=4)]
harm = lambda x: H @ x          # vector of resident harms
names = ["company", "Alice", "Bob", "Carol"]

def by_party(k, delta, iters=20000, damp=0.05):
    v = np.zeros(4)  # continuation values: company, r1, r2, r3
    for it in range(iters):
        out = np.zeros(4)
        # proposer = company
        best, cands = -1e9, []
        for x in X:
            h = harm(x)
            for S in itertools.combinations(range(3), k):
                val = p @ x - sum(delta * v[1 + i] + h[i] for i in S)
                pay = np.zeros(4); pay[0] = val
                for i in range(3):
                    pay[1 + i] = delta * v[1 + i] if i in S else -h[i]
                if val > best + 1e-9: best, cands = val, [pay]
                elif abs(val - best) <= 1e-9: cands.append(pay)
        if best < delta * v[0]:
            cands = [delta * v]
        out += 0.25 * cands[0]
        # proposer = resident r
        for r in range(3):
            best, cands = -1e9, []
            others = [i for i in range(3) if i != r]
            for x in X:
                h = harm(x)
                for S in itertools.combinations(others, k - 1):
                    val = p @ x - delta * v[0] - sum(delta * v[1 + i] + h[i] for i in S) - h[r]
                    pay = np.zeros(4); pay[0] = delta * v[0]; pay[1 + r] = val
                    for i in others:
                        pay[1 + i] = delta * v[1 + i] if i in S else -h[i]
                    if val > best + 1e-9: best, cands = val, [pay]
                    elif abs(val - best) <= 1e-9: cands.append(pay)
            if best < delta * v[1 + r]:
                cands = [delta * v]
            out += 0.25 * cands[0]
        nv = (1 - damp) * v + damp * out
        if np.max(abs(nv - v)) < 1e-11: v = nv; break
        v = nv
    return v, it

def club(split):
    # two-party random proposer by side: each side gets half the pie 6 at any delta
    pie, hz = 6.0, harm(np.array([1, 1, 1, 0]))   # harms (1, 2.5, 4)
    take = pie / 2
    if split == "common_price":      # one price per unit of harm
        price = (hz.sum() + take) / hz.sum(); g = price * hz - hz
    elif split == "equal":
        g = np.full(3, take / 3)
    return np.concatenate([[pie - take], g])

def nash_in_nash_k2():
    # Chipty-Snyder's own solution: each pair splits its increment holding the others' contracts fixed.
    # Below unanimity the other two signatures carry the deal, so the pair's increment is 0.
    hz = harm(np.array([1, 1, 1, 0]))
    return np.concatenate([[13.5], -hz])

def gm(g):
    return float(np.prod(g) ** (1 / len(g))) if np.all(g > 0) else None

SQ = -harm(np.array([1, 1, 1, 0]))   # ordinance: night closed, M,D,E unpaid
def report(label, g):
    sq = " ".join(f"{g[1+i]-SQ[i]:+.2f}" for i in range(3))
    G = gm(g)
    print(f"{label:38s} " + " ".join(f"{x:6.2f}" for x in g) +
          f" | floor {g.min():+.2f} | GM/max {('%.3f' % (G/1.5)) if G else 'n/a (loser)':>12s} | vs ordinance (A,B,C) {sq}")

print("columns: company Alice Bob Carol (gain over no deal); fair deal = 1.5 each")
for d in [0.5, 0.8, 0.95, 0.99]:
    for k in [3, 2]:
        v, it = by_party(k, d)
        report(f"one-by-one k={k} delta={d}", v)
report("club, common price (any delta, any k)", club("common_price"))
report("club, equal split", club("equal"))
report("Nash-in-Nash (C&S) k=2", nash_in_nash_k2())
