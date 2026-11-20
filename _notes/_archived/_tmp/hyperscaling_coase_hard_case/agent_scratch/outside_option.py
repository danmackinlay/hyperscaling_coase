"""Hard-case instance, outside-option arm. Enumerate the 16 schedules.

Switches: parametric harms, once, linear money (a wealth-effects variant at the end),
enforcer assumed, closed, k=3 (and k=2 variant), outside option ON: reroute at 3/slot.
"""
import itertools
import numpy as np
from scipy.optimize import minimize

SLOTS = "MDEN"
p = np.array([4.0, 5.5, 4.0, 5.0])
e = np.array([[0.5, 0, 0.5, 1.0], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
s = np.array([1.0, 1.0, 2.0])
REROUTE = 3.0


def harms(x):
    return s * (e @ x)


def label(x):
    return "".join(c for c, b in zip(SLOTS, x) if b) or "none"


schedules = [np.array(b, dtype=float) for b in itertools.product([0, 1], repeat=4)]
reroute_value = np.maximum(p - REROUTE, 0)  # per slot, if rerouted
d_F = reroute_value.sum()  # fleet's disagreement payoff, all four slots rerouted
print(f"reroute value per slot {reroute_value}, fleet disagreement payoff {d_F}")

print("\n== k=3, transparent, outside option ON, four-slot clauses (fleet may reroute slots not run through) ==")
rows = []
for x in schedules:
    h = harms(x)
    through = p @ x - h.sum()
    joint = through + reroute_value @ (1 - x)
    rows.append((label(x), through, joint, joint - d_F, h))
for lab, through, joint, gains, h in sorted(rows, key=lambda r: -r[2]):
    print(f"{lab:5s} surplus-through {through:5.2f} joint {joint:5.2f} gains-over-no-deal {gains:5.2f} harms {h}")

best = max(rows, key=lambda r: r[2])
pie = best[3]
print(f"\nmax joint {best[2]}, pie of gains over no deal {pie}; symmetric Nash gain each {pie/4}; product {(pie/4)**4:.4f}")
print(f"baseline (no outside option): pie 6, 1.5 each, product {1.5**4:.4f}")
for lab, through, joint, gains, h in rows:
    if abs(joint - best[2]) < 1e-9:
        t = h + pie / 4
        fleet = p @ np.array([c in lab for c in SLOTS], float) + reroute_value @ (1 - np.array([c in lab for c in SLOTS], float)) - t.sum()
        print(f"  {lab}: transfers {t}, fleet payoff {fleet:.3f} (gain {fleet-d_F:.3f}), residents {pie/4} each")

print("\n== k=3, outside option ON, all-or-nothing clause (deal = all four slots through, else reroute all) ==")
x = np.ones(4)
joint = p @ x - harms(x).sum()
print(f"MDEN through: joint {joint} vs fleet reroute {d_F}: {'deal' if joint > d_F else 'no deal; fleet reroutes, residents 0, gains 0 for all'}")
print("== two-clause menu (day = M,D ; night = E,N) ==")
for day, night in itertools.product([0, 1], repeat=2):
    x = np.array([day, day, night, night], float)
    joint = p @ x - harms(x).sum() + reroute_value @ (1 - x)
    print(f"  day={day} night={night}: joint {joint:.2f} gains {joint - d_F:.2f}")

print("\n== k=2, transparent, outside option ON: fleet buys the two cheapest consents, excluded resident unpaid ==")
best_k2 = None
for x in schedules:
    h = harms(x)
    for excl in range(3):
        paid = h.sum() - h[excl]
        fleet = p @ x - paid + reroute_value @ (1 - x)
        if best_k2 is None or fleet > best_k2[0]:
            best_k2 = (fleet, label(x), excl, h)
fleet, lab, excl, h = best_k2
res = np.zeros(3); res[excl] = -h[excl]
print(f"fleet runs {lab}, excludes resident {excl+1}: payoffs fleet {fleet}, residents {res}; total surplus {fleet + res.sum():.2f}")
print("same without outside option (reroute of unused slots adds nothing since all four run)")

print("\n== wealth effects ON for the outside-option arm: Nash product in utility units ==")
w0 = np.array([100.0, 10, 10, 2])  # fleet, r1, r2, r3


def nash_util(g):
    # g = money gains over no deal, sum = pie
    return np.sum(np.log(np.log(w0 + g) - np.log(w0)))


for pie_, name in [(6.0, "baseline, no outside option"), (1.5, "outside option on")]:
    cons = {"type": "eq", "fun": lambda g: g.sum() - pie_}
    r = minimize(lambda g: -nash_util(g), np.full(4, pie_ / 4), constraints=[cons], bounds=[(1e-6, pie_)] * 4)
    g = r.x
    print(f"{name}: money gains (F; r1,r2,r3) {np.round(g,3)}; utility gains {np.round(np.log(w0+g)-np.log(w0),4)}; floor (money) {g.min():.3f}")
