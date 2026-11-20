"""Pact stage on the hard-case instance: durable mechanisms relative to two status quos, and the veil.

Switches: parametric harms, once, linear money (one wealth-effects remark at the end),
enforcer assumed, closed. Sensitivities s_i private to each resident; exposures public.
Prior for the veil: s_i in {1,2} iid, P(2)=1/2 (alternative P(2)=1/3 reported).
"""
import itertools, math

p = (4.0, 5.5, 4.0, 5.0)
e = {1: (0.5, 0, 0.5, 1), 2: (1, 1, 0.5, 0.5), 3: (0.5, 0.5, 1, 2)}
s_real = {1: 1, 2: 1, 3: 2}
R = (1, 2, 3)
scheds = list(itertools.product((0, 1), repeat=4))

def profit(x): return sum(pt * xt for pt, xt in zip(p, x))
def expo(i, x): return sum(et * xt for et, xt in zip(e[i], x))
def harm(i, si, x): return si * expo(i, x)
def surplus(s, x): return profit(x) - sum(harm(i, s[i], x) for i in R)

def xstar(s):
    # efficient schedule; ties broken toward running (reported if they occur)
    best = max(scheds, key=lambda x: (surplus(s, x), sum(x)))
    return best

def nash(gains):
    if any(g < 0 for g in gains): return float('nan')  # undefined
    return math.prod(gains)

def show(label, F, r, origin='no deal'):
    gains = [F, r[1], r[2], r[3]]
    print(f"  {label}: fleet {F:.3f}; residents ({r[1]:.3f}, {r[2]:.3f}, {r[3]:.3f}); "
          f"total {sum(gains):.3f}; Nash product {nash(gains):.4f}; floor {min(gains):.3f}; "
          f"residents' share {(sum(r.values())/sum(gains) if sum(gains) else float('nan')):.3f}")

print("=== Part 1: full information at s=(1,1,2), no-deal status quo ===")
x_full = xstar(s_real)
W_full = surplus(s_real, x_full)
print("efficient schedule (M,D,E,N) =", x_full, "profit", profit(x_full),
      "harms", [harm(i, s_real[i], x_full) for i in R], "pie", W_full)
# check tie-free
alts = sorted(((surplus(s_real, x), x) for x in scheds), reverse=True)[:3]
print("top three schedules:", alts)
show("Nash-max split (1.5 each)", W_full/4, {i: W_full/4 for i in R})

print("\n=== Part 2: private s, prior {1,2} iid; efficient schedule per profile ===")
def run(P2=0.5, verbose=True):
    types = (1, 2)
    prob = {1: 1-P2, 2: P2}
    profiles = list(itertools.product(types, repeat=3))
    def pr(sv): return math.prod(prob[sv[i-1]] for i in R)
    Wstar = 0.0
    tab = {}
    for sv in profiles:
        s = {i: sv[i-1] for i in R}
        x = xstar(s)
        W = surplus(s, x)
        # tie check
        top = sorted((surplus(s, y) for y in scheds), reverse=True)
        tie = abs(top[0]-top[1]) < 1e-9
        tab[sv] = (x, W, tie)
        Wstar += pr(sv) * W
        if verbose: print(f"  s={sv}: x*={x} pie={W:.2f}{'  TIE' if tie else ''}")
    # information rents: low type (1) mimicking high (2): R_i = E_{s_-i}[ e_i . x*(2, s_-i) ]
    # and L_i = E[e_i . x*(1, s_-i)] (monotonicity check L_i >= R_i)
    Rr, Ll = {}, {}
    for i in R:
        others = [j for j in R if j != i]
        Rr[i] = 0.0; Ll[i] = 0.0
        for so in itertools.product(types, repeat=2):
            w = math.prod(prob[v] for v in so)
            s_hi = {i: 2}; s_lo = {i: 1}
            for j, v in zip(others, so): s_hi[j] = v; s_lo[j] = v
            Rr[i] += w * expo(i, xstar(s_hi))
            Ll[i] += w * expo(i, xstar(s_lo))
    exp_rent = sum(prob[1] * Rr[i] for i in R)
    print(f"  expected efficient pie W* = {Wstar:.4f}")
    print(f"  low-type rents R_i = {Rr}; monotonicity L_i = {Ll}")
    print(f"  expected rent paid to low types = {exp_rent:.4f}; fleet residual with all u_i=0: {Wstar-exp_rent:.4f}")
    return Wstar, Rr, Ll, tab, prob

Wstar, Rr, Ll, tab, prob = run(0.5)

print("\n--- Part 2a: durable (interim-efficient, IC, IR) mechanisms relative to NO DEAL ---")
print("  mechanism family: x*(s); t_i(s) = s_i e_i.x*(s) + u_i + R_i [s_i=1]; u_i >= 0 is type-2's interim gain.")
print("  frontier: sum_i (u_i + R_i/2) <= W*. Realised gains at s=(1,1,2): residents (u1+R1, u2+R2, u3); fleet residual.")
def realised(u):
    r = {1: u[1] + Rr[1], 2: u[2] + Rr[2], 3: u[3]}
    F = W_full - sum(r.values())
    return F, r
def expected(u):
    r = {i: u[i] + prob[1]*Rr[i] for i in R}
    F = Wstar - sum(r.values())
    return F, r
u0 = {1: 0, 2: 0, 3: 0}
F, r = realised(u0); show("residents at IR floor, realised", F, r)
F, r = expected(u0); show("residents at IR floor, expected", F, r)
# fleet at floor, surplus to residents equally in u
slack = Wstar - sum(prob[1]*Rr[i] for i in R)
uF = {i: slack/3 for i in R}
F, r = realised(uF); show("fleet at IR floor, u equal, realised", F, r)
F, r = expected(uF); show("fleet at IR floor, u equal, expected", F, r)
# fleet at floor, all slack to resident 3
u3 = {1: 0, 2: 0, 3: slack}
F, r = realised(u3); show("fleet at floor, all slack to resident 3, realised", F, r)
# ex-ante Nash-max: equal expected gains W*/4
uN = {i: Wstar/4 - prob[1]*Rr[i] for i in R}
print("  ex-ante Nash-max u_i =", {i: round(v, 4) for i, v in uN.items()}, "(all >= 0?)", all(v >= -1e-12 for v in uN.values()))
F, r = expected(uN); show("ex-ante Nash-max, expected", F, r)
F, r = realised(uN); show("ex-ante Nash-max, realised at (1,1,2)", F, r)
# realised Nash-max subject to IC: maximise product of realised gains at (1,1,2) over u >= 0 with frontier
# realised gains: (W_full - u1-R1-u2-R2-u3, u1+R1, u2+R2, u3) with sum(u_i + R_i/2) <= W*.
best = None
import numpy as np
grid = np.linspace(0, 3, 121)
for a in grid:
    for b in grid:
        for c in grid:
            u = {1: a, 2: b, 3: c}
            if sum(u[i] + prob[1]*Rr[i] for i in R) > Wstar + 1e-9: continue
            F, r = realised(u)
            g = [F, r[1], r[2], r[3]]
            if min(g) < 0: continue
            val = nash(g)
            if best is None or val > best[0]: best = (val, u)
print("  best realised-(1,1,2) Nash product over IC-IR mechanisms:", round(best[0], 4), {i: round(v, 3) for i, v in best[1].items()})
F, r = realised(best[1]); show("  that mechanism, realised", F, r)
F, r = expected(best[1]); show("  that mechanism, expected", F, r)

print("\n--- Part 2b: is realised-equal-split (W(s)/4 each) IC? ---")
for i in R:
    others = [j for j in R if j != i]
    lhs = 0.0  # E[(W(1,.) - W(2,.))/4]
    for so in itertools.product((1, 2), repeat=2):
        w = math.prod(prob[v] for v in so)
        s1 = {i: 1}; s2 = {i: 2}
        for j, v in zip(others, so): s1[j] = v; s2[j] = v
        lhs += w * (tab[tuple(s1[k] for k in R)][1] - tab[tuple(s2[k] for k in R)][1]) / 4
    print(f"  resident {i}: pie drop/4 = {lhs:.4f} vs rent R_i = {Rr[i]:.4f} -> {'IC ok' if lhs >= Rr[i] - 1e-9 else 'low type mimics high: NOT IC'}")

print("\n=== Part 3: liability-rule status quo: fleet runs any slot on paying s_hat * e_it per resident ===")
def liability(s_hat, s, run_ties=True):
    x = []
    for t in range(4):
        due = s_hat * sum(e[i][t] for i in R)
        x.append(1 if (p[t] > due or (run_ties and abs(p[t]-due) < 1e-9)) else 0)
    x = tuple(x)
    F = profit(x) - s_hat * sum(expo(i, x) for i in R)
    r = {i: s_hat * expo(i, x) - harm(i, s[i], x) for i in R}
    return x, F, r
for s_hat in (1.0, 1.5, 2.0):
    x, F, r = liability(s_hat, s_real)
    print(f"  s_hat={s_hat}: fleet runs {x}; statutory outcome vs clean river:")
    show("   ", F, r)
    if s_hat == 2.0:
        x, F, r = liability(s_hat, s_real, run_ties=False)
        print(f"   (ties not run: {x})"); show("   ", F, r)

print("\n--- Part 3a: durable mechanisms relative to the liability status quo, s_hat=1 ---")
s_hat = 1.0
# interim status-quo utilities: fleet runs all four regardless of s (p_t > sum e_it for all t at s_hat=1)
xL = liability(s_hat, s_real)[0]
print("  liability schedule at s_hat=1:", xL)
SQ_F = profit(xL) - s_hat*sum(expo(i, xL) for i in R)
SQ = {i: {si: s_hat*expo(i, xL) - si*expo(i, xL) for si in (1, 2)} for i in R}
print("  status-quo fleet:", SQ_F, "; residents by type:", SQ)
# efficient mechanism relative to L: residents' interim utility must be >= SQ[i][si]; IC as before.
# U_i(2) = SQ[i][2] + u_i, U_i(1) = U_i(2) + R_i >= SQ[i][1] = 0 ? check
for i in R:
    print(f"  resident {i}: U_i(1) at u=0 is {SQ[i][2] + Rr[i]:.3f} vs type-1 floor {SQ[i][1]:.3f} -> "
          f"{'type-1 IR binds too' if SQ[i][2] + Rr[i] < SQ[i][1] else 'type-2 IR binds'}")
# Expected total over the status quo
exp_SQ_total = SQ_F + sum(sum(prob[si]*SQ[i][si] for si in (1, 2)) for i in R)
print(f"  expected total at status quo {exp_SQ_total:.4f}; expected efficient W* {Wstar:.4f}; gain available {Wstar-exp_SQ_total:.4f}")
# Mechanism: t_i(s) = s_i e_i.x*(s) + c_i(s_i), with c_i(2) = SQ[i][2] + u_i, c_i(1) = max(c_i(2) + R_i, SQ[i][1]) -- if type-1 IR binds, need c_i(1)=SQ[i][1] and then IC for type 2 (needs c_i(1)-c_i(2) <= L_i) still fine.
def mechL(u):
    c = {}
    for i in R:
        c2 = SQ[i][2] + u[i]
        c1 = max(c2 + Rr[i], SQ[i][1])
        c[i] = {1: c1, 2: c2}
    # fleet expected: W* - sum_i E[c_i]
    EF = Wstar - sum(prob[1]*c[i][1] + prob[2]*c[i][2] for i in R)
    # realised at (1,1,2)
    rr = {i: c[i][s_real[i]] for i in R}
    RF = W_full - sum(rr.values())
    return c, EF, rr, RF
c, EF, rr, RF = mechL(u0)
print("  u=0: c =", {i: {k: round(v, 3) for k, v in c[i].items()} for i in R})
print(f"  fleet expected {EF:.4f} (status quo {SQ_F}); fleet expected GAIN over its status quo {EF-SQ_F:.4f}")
print(f"  realised at (1,1,2): fleet {RF:.3f} (gain over SQ {RF-SQ_F:.3f}); residents payoff vs clean river {rr}")
gl = [RF-SQ_F] + [rr[i]-SQ[i][s_real[i]] for i in R]
print(f"  realised gains over the LIABILITY origin: {[round(g,3) for g in gl]}; product {nash(gl):.5f}; floor {min(gl):.3f}")
gc = [RF] + [rr[i] for i in R]
print(f"  realised gains over the CLEAN-RIVER origin: {[round(g,3) for g in gc]}; product {nash(gc)}; floor {min(gc):.3f}")
# fleet at its floor, slack to resident 3
slackL = EF - SQ_F
uL3 = {1: 0, 2: 0, 3: slackL}
c, EF2, rr, RF = mechL(uL3)
print(f"  all slack ({slackL:.4f}) to resident 3: fleet expected {EF2:.4f}; realised at (1,1,2): fleet {RF:.3f}; residents vs clean river {({i: round(v,3) for i,v in rr.items()})}")
gc = [RF] + [rr[i] for i in R]
print(f"  realised gains over the CLEAN-RIVER origin: {[round(g,3) for g in gc]}; product {nash(gc)}; floor {min(gc):.3f}")

print("\n=== Part 4: the veil. Residents pick the mechanism before knowing s_i ===")
for P2 in (0.5, 1/3):
    print(f"\n  prior P(s_i=2) = {P2:.3f}")
    Wstar2, Rr2, Ll2, tab2, prob2 = run(P2, verbose=False)
    # ex ante Nash-max (equal expected gains) with efficient x*: U_i(1) - U_i(2) = R_i by payoff equivalence
    for i in R:
        U2 = Wstar2/4 - prob2[1]*Rr2[i]
        U1 = U2 + Rr2[i]
        print(f"    resident {i}: ex ante expected gain {Wstar2/4:.4f}; interim U(s=1) = {U1:.4f}, U(s=2) = {U2:.4f} "
              f"{'<0: type-2 regrets (would veto)' if U2 < 0 else '>=0: no veto, but below the 1.5 full-info fair share' if U2 < 1.5 else ''}")
    # realised at (1,1,2)
    rr = {1: Wstar2/4 + prob2[2]*Rr2[1], 2: Wstar2/4 + prob2[2]*Rr2[2], 3: Wstar2/4 - prob2[1]*Rr2[3]}
    RF = W_full - sum(rr.values())
    g = [RF] + [rr[i] for i in R]
    print(f"    realised at (1,1,2): fleet {RF:.3f}; residents {[round(rr[i],3) for i in R]}; product {nash(g):.4f}; floor {min(g):.3f}; vs full-info 5.0625")
    # what the AGV-chosen rule gives if the fleet is also at ex ante equal share: that's the above. Also: residents choose
    # to squeeze the fleet to 0 ex ante (they hold the veto):
    slack2 = Wstar2 - sum(prob2[1]*Rr2[i] for i in R)
    rr = {1: slack2/3 + Rr2[1], 2: slack2/3 + Rr2[2], 3: slack2/3}
    RF = W_full - sum(rr.values())
    g = [RF] + [rr[i] for i in R]
    print(f"    residents squeeze fleet to 0 ex ante, realised at (1,1,2): fleet {RF:.3f}; residents {[round(rr[i],3) for i in R]}; floor {min(g):.3f}")

print("\n=== Part 5: Krier's club: one price per unit of public exposure, s_hat, every resident must join (k=3) ===")
for s_hat in (1.0, 1.5, 2.0):
    x, F, r = liability(s_hat, s_real)  # fleet buys slots where p_t >= s_hat*sum e
    print(f"  s_hat={s_hat}: schedule {x}; fleet {F:.3f}; residents {[round(r[i],3) for i in R]}; "
          f"resident 3 joins? {'yes' if r[3] >= -1e-9 else 'NO'}; product {nash([F]+[r[i] for i in R])}")

print("\n=== Part 6: wealth effects remark (switch on): resident 3's utility gain for payoff g with w0=2 ===")
for g in (-4, -1, 0, 0.5, 1.5):
    print(f"  payoff {g}: ", "ruin (log of non-positive wealth)" if 2+g <= 0 else f"{math.log(2+g)-math.log(2):.4f}")
