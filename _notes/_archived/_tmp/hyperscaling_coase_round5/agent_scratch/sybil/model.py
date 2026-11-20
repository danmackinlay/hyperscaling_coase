"""Agent-count contest on the base instance.

Base instance: fleet (company) vs residents Alice, Bob, Carol; efficient schedule M,D,E;
profit 13.5; harms (1, 2.5, 4); pie 6; unanimity.

Protocol (the agenda's default): the platform runs the symmetric Nash bargaining
solution among REGISTERED AGENTS. Each agent's no-deal payoff is 0, so every agent
gets an equal gain 6/N where N is the number of agents at the table.

Each party i (0 = company, 1..3 = residents) fields m_i >= 1 agents. The first agent
is free ("give everyone an agent"); each extra agent costs kappa_i = kappa / c_i,
c_i the party's compute. Party i's net gain = 6*m_i/N - kappa_i*(m_i - 1).

Nash equilibrium in m found by iterated best response over integers (and the
continuous closed form for comparison).

Criterion: geometric mean of PARTIES' gains (a party that splits counts once),
as a fraction of the maximum 1.5 at n+1 = 4 parties; floor = worst-off party.
Status quo (ordinance, night closed, no compensation): residents at (-1, -2.5, -4).
"""
import itertools, math, sys

PIE = 6.0
HARMS = (1.0, 2.5, 4.0)
ORDINANCE = (-1.0, -2.5, -4.0)
NAMES = ("Company", "Alice", "Bob", "Carol")

def payoffs(m, kappa, first_free=True):
    N = sum(m)
    out = []
    for i, mi in enumerate(m):
        extra = mi - 1 if first_free else mi
        out.append(PIE * mi / N - kappa[i] * extra)
    return out

def best_response(i, m, kappa, mmax=60, first_free=True):
    best, bestv = None, -1e9
    for mi in range(1, mmax + 1):
        mm = list(m); mm[i] = mi
        v = payoffs(mm, kappa, first_free)[i]
        if v > bestv + 1e-12:
            best, bestv = mi, v
    return best

def equilibrium(kappa, first_free=True, mmax=60, iters=500):
    m = [1, 1, 1, 1]
    for _ in range(iters):
        changed = False
        for i in range(4):
            b = best_response(i, m, kappa, mmax, first_free)
            if b != m[i]:
                m[i] = b; changed = True
        if not changed:
            break
    return m

def criterion(gains):
    pos = [g for g in gains if g > 0]
    losers = [g for g in gains if g < 0]
    gm = math.exp(sum(math.log(g) for g in pos) / len(pos)) if pos else 0.0
    return gm, min(gains), len(losers)

def report(label, kappa, first_free=True):
    m = equilibrium(kappa, first_free)
    g = payoffs(m, kappa, first_free)
    gm, floor, nlos = criterion(g)
    N = sum(m)
    spent = sum(kappa[i] * ((m[i] - 1) if first_free else m[i]) for i in range(4))
    res_pos = [g[i + 1] for i in range(3)]
    vs_sq = [res_pos[i] - ORDINANCE[i] for i in range(3)]
    print(f"{label:34s} kappa={tuple(round(k,3) for k in kappa)} m={tuple(m)} N={N}")
    print(f"   gains  C={g[0]:.3f} A={g[1]:.3f} B={g[2]:.3f} Ca={g[3]:.3f} | spent on agents {spent:.3f} of pie {PIE}")
    print(f"   geomean(parties)={gm:.3f} ({gm/1.5:.0%} of max) floor={floor:.3f} losers={nlos} | Carol vs ordinance {vs_sq[2]:+.3f} (above)" )
    return m, g

if __name__ == "__main__":
    # agent cost at equal compute, as a fraction of the pie
    base = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
    print(f"=== base agent cost kappa={base} (first agent free) ===")
    print("Fair deal (one agent each): gains 1.5 each, geomean 1.5 (100%), floor 1.5; Carol vs ordinance +5.5")
    for ratio, lab in ((1, "1:1 equal compute"), (10, "10:1 company compute"), (0.1, "1:10 residents compute")):
        kappa = (base / ratio, base, base, base)
        report(lab, kappa)
    print()
    print("--- robustness: cost level (sign of Carol's loss vs fair deal under 10:1) ---")
    for base2 in (0.03, 0.1, 0.3, 1.0, 1.2, 2.0):
        kappa = (base2 / 10, base2, base2, base2)
        m, g = report(f"kappa={base2}, 10:1", kappa)
    print()
    print("--- robustness: first agent NOT free (every agent costs kappa) ---")
    for ratio, lab in ((1, "1:1"), (10, "10:1"), (0.1, "1:10")):
        kappa = (base / ratio, base, base, base)
        report(lab, kappa, first_free=False)
    print()
    print("--- continuous closed form, 10:1, residents pinned at 1 agent ---")
    for kf in (0.03, 0.1, 0.3, 1.0):
        m0 = max(1.0, math.sqrt(3 * PIE / kf) - 3)
        share_res = PIE / (m0 + 3)
        print(f"   kappa_f={kf}: m0*={m0:.2f}, resident gain {share_res:.3f} = sqrt(2*kappa_f) when interior")
