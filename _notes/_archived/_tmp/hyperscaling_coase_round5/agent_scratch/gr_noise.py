"""Genicot-Ray (2006) sequencing on the noise schedule, consent rule k=2 of 3.

Base instance: four slots (M, D, E, N), profits p, exposures e_i, sensitivities s_i.
Switches on: recurring (discount delta), consent k=2. Protocol (Genicot-Ray):
each period the fleet offers bilateral per-period payments c_i to any subset of
free residents; offered residents accept/reject simultaneously and publicly;
residents coordinate (their A.2: no subset of offerees can jointly change
responses and all be strictly better off); once k=2 are contracted the fleet runs
schedule x for life, paying c_i to each contracted resident per period run.
Free residents bear h_i(x) unpaid. Origin: no deal (nothing runs). Tie-break:
accept when indifferent (their convention), plus a strict variant with eps.

Model 1 (fleet commits never to return to a refuser): plans
  P2 "temptation": date 0 offer {i full comp, j low}, run from date 0.
  P1 "exploitation": date 0 offer i at 0 (fleet not running yet, so refusing
      gains her nothing), date 1 offer j at (1-delta) h_j, run from date 1.
  Static: one round, no return: both offerees pivotal, full comp each.
Model 2 (fleet may return): best = low offer to {i at 0, j at (1-delta) h_j}
  simultaneously, supported by the standard-offer punishment; worst = standard
  offer {i at 0, j at h_j}; maximal delay T = floor(ln(Pworst/Pbest)/ln delta).
Normalised payoffs: multiply lifetime sums by (1-delta), as in the paper.
"""
import itertools
import math

SLOTS = "MDEN"
P = (4.0, 5.5, 4.0, 5.0)
E = {"Alice": (0.5, 0, 0.5, 1), "Bob": (1, 1, 0.5, 0.5), "Carol": (0.5, 0.5, 1, 2)}
S0 = {"Alice": 1.0, "Bob": 1.0, "Carol": 2.0}
ORDINANCE_X = (1, 1, 1, 0)  # night closed, no compensation


def harms(x, s):
    return {r: s[r] * sum(e * xi for e, xi in zip(E[r], x)) for r in E}


def profit(x):
    return sum(p * xi for p, xi in zip(P, x))


def plans(x, delta, s, eps=0.0):
    """Return dict plan -> (fleet, gains dict, start_period)."""
    h = harms(x, s)
    pi = profit(x)
    out = {}
    pairs = list(itertools.combinations(E, 2))
    # static one round: full comp to both
    best = None
    for i, j in pairs:
        f = pi - (h[i] + eps) - (h[j] + eps)
        if best is None or f > best[0]:
            best = (f, i, j)
    f, i, j = best
    g = {r: -h[r] for r in E}
    g[i] = eps
    g[j] = eps
    out["static"] = (f, g, 0)
    # P2 temptation: i full, j low, run date 0
    best = None
    for i, j in itertools.permutations(E, 2):
        f = pi - (h[i] + eps) - ((1 - delta) * h[j] + eps)
        if best is None or f > best[0]:
            best = (f, i, j)
    f, i, j = best
    g = {r: -h[r] for r in E}
    g[i] = eps
    g[j] = (1 - delta) * h[j] + eps - h[j]
    out["P2_temptation"] = (f, g, 0)
    # P1 exploitation: i at 0 date 0, j at (1-delta)h_j date 1, run from date 1
    best = None
    for i, j in itertools.permutations(E, 2):
        l = [r for r in E if r not in (i, j)][0]
        # credibility: after i refuses, fleet buys j,l at full; after j refuses, buys l full
        if pi - h[j] - h[l] < 0 or pi - h[l] < 0:
            continue
        f = delta * (pi - eps - ((1 - delta) * h[j] + eps))
        if best is None or f > best[0]:
            best = (f, i, j)
    f, i, j = best
    g = {r: delta * (-h[r]) for r in E}
    g[i] = delta * (eps - h[i])
    g[j] = delta * ((1 - delta) * h[j] + eps - h[j])
    out["P1_exploitation"] = (f, g, 1)
    # Model 2 best (low offer, simultaneous, no delay) and worst (standard offer)
    best = None
    for i, j in itertools.permutations(E, 2):
        f = pi - eps - ((1 - delta) * h[j] + eps)
        if best is None or f > best[0]:
            best = (f, i, j)
    f, i, j = best
    g = {r: -h[r] for r in E}
    g[i] = eps - h[i]
    g[j] = (1 - delta) * h[j] + eps - h[j]
    out["M2_best"] = (f, g, 0)
    worst = None
    for i, j in itertools.permutations(E, 2):
        f = pi - eps - (h[j] + eps)
        if worst is None or f > worst[0]:
            worst = (f, i, j)
    f, i, j = worst
    g = {r: -h[r] for r in E}
    g[i] = eps - h[i]
    g[j] = eps
    out["M2_worst"] = (f, g, 0)
    return out


def model1(delta, s, eps=0.0):
    """Fleet picks x and plan maximising its normalised payoff under model 1."""
    best = None
    for x in itertools.product((0, 1), repeat=4):
        if sum(x) == 0:
            continue
        pl = plans(x, delta, s, eps)
        for name in ("P1_exploitation", "P2_temptation"):
            f, g, t0 = pl[name]
            if best is None or f > best[0]:
                best = (f, g, name, x)
    return best


def static(delta, s, eps=0.0):
    best = None
    for x in itertools.product((0, 1), repeat=4):
        if sum(x) == 0:
            continue
        f, g, _ = plans(x, delta, s, eps)["static"]
        if best is None or f > best[0]:
            best = (f, g, "static", x)
    return best


def model2(delta, s, eps=0.0):
    bestx = None
    for x in itertools.product((0, 1), repeat=4):
        if sum(x) == 0:
            continue
        pl = plans(x, delta, s, eps)
        f, g, _ = pl["M2_best"]
        if bestx is None or f > bestx[0]:
            bestx = (f, g, x, pl["M2_worst"])
    f, g, x, (fw, gw, _) = bestx
    T = math.floor(math.log(fw / f) / math.log(delta)) if fw > 0 else 0
    return f, g, x, fw, gw, T


def status_quo(s):
    h = harms(ORDINANCE_X, s)
    return profit(ORDINANCE_X), {r: -h[r] for r in E}


def criterion(g):
    vals = list(g.values())
    losers = [v for v in vals if v < 0]
    if losers:
        tier = "losers"
    elif any(v == 0 for v in vals):
        tier = "zero"
    else:
        tier = "positive"
    return tier, min(vals), sum(1 for v in vals if v < 0) / len(vals)


def fmt(x):
    return "".join(SLOTS[i] for i in range(4) if x[i])


def report(s, label, eps=0.0):
    print(f"\n=== {label}  (s={s}, eps={eps}) ===")
    sq_f, sq_g = status_quo(s)
    print(f"status quo (ordinance MDE, no pay): fleet {sq_f:.3f}, "
          + ", ".join(f"{r} {v:+.3f}" for r, v in sq_g.items()))
    hdr = f"{'delta':>5} {'regime':<16} {'x':<5} {'fleet':>7} {'Alice':>7} {'Bob':>7} {'Carol':>7} {'pie':>5} {'floor':>7} {'frac<0':>6} {'vs ordinance (A,B,C)':<22}"
    print(hdr)
    for delta in (0.5, 0.8, 0.95, 0.99):
        rows = []
        f, g, name, x = static(delta, s, eps)
        rows.append(("static 1-round", x, f, g))
        f, g, name, x = model1(delta, s, eps)
        rows.append((f"M1 {name[:2]}", x, f, g))
        f, g, x, fw, gw, T = model2(delta, s, eps)
        rows.append((f"M2 best(T<={T})", x, f, g))
        rows.append(("M2 worst", x, fw, gw))
        for regime, x, f, g in rows:
            h = harms(x, s)
            pie = profit(x) - sum(h.values())
            tier, floor, frac = criterion(g)
            vs = ",".join("W" if g[r] < sq_g[r] - 1e-9 else ("=" if abs(g[r] - sq_g[r]) < 1e-9 else "B") for r in E)
            print(f"{delta:>5} {regime:<16} {fmt(x):<5} {f:>7.3f} {g['Alice']:>7.3f} {g['Bob']:>7.3f} {g['Carol']:>7.3f} {pie:>5.1f} {floor:>7.3f} {frac:>6.2f} {vs:<22}")


if __name__ == "__main__":
    report(S0, "base sensitivities, k=2, fleet free to choose x")
    report(S0, "tie-break eps=0.01 (strict acceptance)", eps=0.01)
    report({"Alice": 1.0, "Bob": 1.0, "Carol": 1.5}, "Carol less sensitive s_C=1.5")
    report({"Alice": 1.0, "Bob": 1.0, "Carol": 3.0}, "Carol more sensitive s_C=3")
    report({"Alice": 1.0, "Bob": 1.0, "Carol": 0.5}, "Carol cheap s_C=0.5 (who is left out?)")
    # structural variant: night closed by ordinance, bargaining only over permitted slots
    print("\n=== structural: night slot closed by ordinance, bargaining over MDE only ===")
    sq_f, sq_g = status_quo(S0)
    for delta in (0.5, 0.8, 0.95):
        pl = plans(ORDINANCE_X, delta, S0)
        for name in ("static", "P2_temptation", "P1_exploitation"):
            f, g, _ = pl[name]
            vs = ",".join("W" if g[r] < sq_g[r] - 1e-9 else ("=" if abs(g[r] - sq_g[r]) < 1e-9 else "B") for r in E)
            print(f"{delta:>5} {name:<16} fleet {f:>7.3f} A {g['Alice']:>7.3f} B {g['Bob']:>7.3f} C {g['Carol']:>7.3f}  vs ordinance {vs}")
    # threshold delta where P1 overtakes P2 at all-four schedule
    print("\nP1 vs P2 threshold (all four slots):")
    for d in (0.85, 0.88, 0.884, 0.89, 0.9):
        pl = plans((1, 1, 1, 1), d, S0)
        print(f"  delta={d}: P1 {pl['P1_exploitation'][0]:.3f}  P2 {pl['P2_temptation'][0]:.3f}")
