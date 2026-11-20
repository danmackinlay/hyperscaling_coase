"""Collator's checks, existence-test round, 2026-10-21.
1. Miettinen-Vanberg 2024 symmetric most-aggressive equilibrium on the river:
   fraction of the pie surviving delay, and the ex post split, for n=3 (residents alone)
   and n=4 (factory + three residents as symmetric veto players), from Prop. 2 / Sec. 3.2.
   Efficient-equilibrium threshold from Theorem 3.
2. Hang-Wen 2026 eq. (6) with a FIXED order (the single principal always attempts first)
   against a random order, on the river (pie 6, four veto players).
3. Grim-trigger threshold for a premium g per resident under repeated factory TIOLI at k=3.
"""
from itertools import permutations

def mv_aggressive(n, rho, delta, pie):
    # most aggressive symmetric profile: agreement iff at most one commitment sticks
    eta = n*rho*(1-rho)**(n-1) + (1-rho)**n
    surviving = eta/(1-delta*(1-eta))          # = n * v*  (fraction of pie)
    v = surviving/n                            # per-player expected payoff fraction
    x_star = 1 - (n-1)*delta*v                 # the lone successful committer's share
    return eta, surviving, v*pie, x_star*pie, delta*v*pie

def mv_threshold(n):
    return ((n-1)/(2*n-1))**(1/(n-1))

print("== Miettinen-Vanberg most-aggressive symmetric SSPE on the river ==")
for n, pie, label in [(3, 6.0, "n=3 (residents dividing 6 among themselves, factory out)"),
                      (4, 6.0, "n=4 (factory + 3 residents, symmetric veto players, pie 6)")]:
    print(label, f" efficient eq. exists iff rho >= {mv_threshold(n):.3f}")
    for rho in (0.5, 0.7, 0.9, 0.99):
        for delta in (0.9, 0.99):
            eta, surv, v, x, cont = mv_aggressive(n, rho, delta, pie)
            print(f"  rho={rho:<5} delta={delta:<5} P(agree/round)={eta:.4f} pie surviving={surv:.3f} of {pie:.0f}"
                  f"  E[payoff] each={v:.3f}  ex post: lone committer {x:.2f}, each other {cont:.2f}")

def hw_weights(rho, prop, orders):
    n = len(rho); w = [0.0]*n
    for mu, q in orders:
        fail = 1.0
        for i in mu:
            w[i] += q*rho[i]*fail
            fail *= 1-rho[i]
        for i in range(n):
            w[i] += q*prop[i]*fail
    return w

print("\n== Hang-Wen eq. (6) on the river: random order v. factory always first ==")
pie = 6.0; prop = [0.25]*4
allperms = list(permutations(range(4))); random_orders = [(mu, 1/len(allperms)) for mu in allperms]
for label, rho in [("all rho=0.9", [0.9]*4), ("all rho=0.5", [0.5]*4),
                   ("factory 0.9, residents 0.5", [0.9, 0.5, 0.5, 0.5])]:
    wr = hw_weights(rho, prop, random_orders)
    wf = hw_weights(rho, prop, [((0,1,2,3), 1.0)])
    print(f"  {label:28s} random order: {[round(x*pie,2) for x in wr]}   factory first every period: {[round(x*pie,3) for x in wf]}")
# ex post split in one period, symmetric rho, pie 6, four players, discount delta:
for delta in (0.5, 0.9, 0.99):
    print(f"  ex post, symmetric: first committer {6-4.5*delta:.2f}, each other {1.5*delta:.2f}  (delta={delta})")

print("\n== Grim trigger, repeated factory TIOLI at k=3, premium g per resident ==")
for g in (0.5, 1.0, 1.5, 1.9):
    print(f"  g={g}: factory keeps {6-3*g:.1f}/yr; cooperate iff (6-3g)/(1-d) >= 6  <=> d >= {g/2:.3f}")
