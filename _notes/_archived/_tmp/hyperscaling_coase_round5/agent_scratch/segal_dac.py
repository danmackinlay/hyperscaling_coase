"""Segal-2003 divide-and-conquer on the noise schedule, consent rule k=2.

Base instance numbers (hard_case_instance.md): slots M,D,E,N; profit per slot
p=(4,5.5,4,5); exposures e_i; private sensitivities s=(1,1,2).
Resident 1 = Alice, 2 = Bob, 3 = Carol.

Contracting as in Segal 2003 sec 2.3: the principal publicly posts one bilateral,
non-contingent offer per resident, a signing fee t_i paid for consent x_i=1
whatever the others do.  Residents then play the induced game.  Under k=2 the
schedule runs iff at least two consent; a resident bears h_i(x) whenever it runs,
consenting or not.  Payoff_i = t_i x_i - h_i(x) 1[sum x >= 2].

Unique implementation (Segal Lemma 3 logic, by direct enumeration of the 8
profiles since the pivot game is not supermodular): all-consent is reached from
the no-consent origin by round-robin best response iff at least two residents are
offered t_i >= h_i(x); a pair with one underpaid member is not stable, because that
member is pivotal and backs out.  The principal therefore buys the cheapest winning
coalition at exactly its harm (discrimination) or posts one price equal to the
second-lowest harm (the agenda's club, Segal's nondiscrimination).

Finite estimation: the principal sees s_hat = s + N(0, err^2); the residents'
estimation of p_t is irrelevant to the outcome (they only accept or refuse).
"""
import itertools

import numpy as np

P = np.array([4.0, 5.5, 4.0, 5.0])
E = np.array([[0.5, 0.0, 0.5, 1.0],
              [1.0, 1.0, 0.5, 0.5],
              [0.5, 0.5, 1.0, 2.0]])
S_TRUE = np.array([1.0, 1.0, 2.0])
SCHEDS = [np.array(x) for x in itertools.product([0, 1], repeat=4)]
SLOTNAMES = "MDEN"


def sname(x):
    return "".join(c for c, b in zip(SLOTNAMES, x) if b) or "none"


def harms(x, s=S_TRUE):
    return s * (E @ x)


def ordinance():
    x = np.array([1, 1, 1, 0])
    return P @ x, -harms(x)


def full_info(k, p=P):
    rows = []
    for x in SCHEDS:
        prof = p @ x
        h = harms(x)
        if k == 3:
            t = h.copy()
            rows.append(("IR", x, prof - t.sum(), t - h, t))
        else:
            order = np.argsort(h)
            t = np.zeros(3); t[order[:2]] = h[order[:2]]
            rows.append(("DAC", x, prof - t.sum(), t - h, t))
            price = np.sort(h)[1]
            tc = np.full(3, price)
            rows.append(("club", x, prof - tc.sum(), tc - h, tc))
    return rows


def best(rows, regime):
    cand = [r for r in rows if r[0] == regime and r[2] > 0]
    return max(cand, key=lambda r: r[2])


def induced_pass(t, h, rng, mode="roundrobin"):
    x = np.zeros(3, dtype=int)
    def payoff(xi, i, xo):
        n = xi + xo.sum()
        return t[i] * xi - h[i] * (1 if n >= 2 else 0)
    def br(i, x):
        xo = np.delete(x, i)
        u0, u1 = payoff(0, i, xo), payoff(1, i, xo)
        if u1 > u0 + 1e-12: return 1
        if u0 > u1 + 1e-12: return 0
        return x[i]
    for _ in range(20):
        if mode == "roundrobin":
            moved = False
            for i in rng.permutation(3):
                b = br(i, x)
                if b != x[i]:
                    x[i] = b; moved = True
            if not moved: break
        else:
            nx = np.array([br(i, x) for i in range(3)])
            if (nx == x).all(): break
            x = nx
    return x.sum() >= 2, x


def principal_plan(s_hat, err, margin, cautious, rng, p=P, ndraw=400):
    bestv, bestplan = -1e9, None
    margins = [margin] if not cautious else [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
    draws = s_hat + err * rng.standard_normal((ndraw, 3)) if cautious else None
    for x in SCHEDS:
        if x.sum() == 0: continue
        prof = p @ x
        hh = s_hat * (E @ x)
        for pair in itertools.combinations(range(3), 2):
            for m in margins:
                t = np.zeros(3)
                for i in pair: t[i] = max(hh[i], 0) + m
                if not cautious:
                    v = prof - t.sum()
                else:
                    htrue = draws * (E @ x)
                    ok = (t[list(pair)] >= htrue[:, list(pair)])
                    ppass = (ok.sum(1) == 2).astype(float)
                    lone_cost = t[list(pair)].mean()
                    v = (ppass * (prof - t.sum()) - (1 - ppass) * lone_cost).mean()
                if v > bestv:
                    bestv, bestplan = v, (x, t)
    return None if bestv <= 0 else bestplan


def simulate(err, margin=0.0, cautious=False, mode="roundrobin", n=3000, seed=0, p=P):
    rng = np.random.default_rng(seed)
    out = {"pass": 0, "pos": np.zeros(4), "carol_below_ord": 0, "four": 0}
    _, ord_pos = ordinance()
    for _ in range(n):
        s_hat = S_TRUE + err * rng.standard_normal(3)
        plan = principal_plan(s_hat, err, margin, cautious, rng, p=p)
        if plan is None:
            continue
        x, t = plan
        h = harms(x)
        ok, xfin = induced_pass(t, h, rng, mode)
        paid = t * xfin
        if ok:
            res = paid - h; prin = p @ x - paid.sum()
            out["pass"] += 1; out["four"] += int(x.sum() == 4)
        else:
            res = paid; prin = -paid.sum()
        out["pos"] += np.r_[prin, res]
        out["carol_below_ord"] += int(res[2] < ord_pos[2] - 1e-9)
    for k in ("pass", "carol_below_ord", "four"):
        out[k] /= n
    out["pos"] /= n
    return out


def tiers(g, label):
    res = g[1:]
    losers = (g < -1e-9).any()
    pos = g[g > 1e-9]
    gm = float(np.exp(np.log(pos).mean())) if len(pos) else float("nan")
    tier = "LOSER tier" if losers else "no-loser tier"
    print(f"{label}: worst-off {g.min():.2f}; residents at/below no deal {int((res <= 1e-9).sum())}/3; "
          f"GM over positive-gain parties {gm:.2f} ({len(pos)} parties); {tier}")


def main():
    print("== Status quo (ordinance: MDE, no compensation) ==")
    prof, res = ordinance(); print(f"  company {prof}, residents {res}")
    print("\n== Fair deal (equal split of pie 6 on MDE): gains 1.5 each; payments (2.5, 4.0, 5.5); company 1.5 ==")
    print("\n== Full information, k=3 (base instance): unique implementation = IR for all ==")
    r = best(full_info(3), "IR")
    print(f"  schedule {sname(r[1])}, company {r[2]:.2f}, resident gains {r[3]}, payments {r[4]}")
    print("\n== Full information, k=2 ==")
    rows = full_info(2)
    for reg in ("DAC", "club"):
        print(f"  -- {reg} --")
        for rr in sorted([q for q in rows if q[0] == reg], key=lambda q: -q[2])[:5]:
            print(f"   {sname(rr[1]):5s} company {rr[2]:6.2f}  resident gains {np.round(rr[3],2)}  pay {np.round(rr[4],2)}")
        b = best(rows, reg)
        print(f"   CHOSEN {sname(b[1])}: company {b[2]:.2f}, Alice {b[3][0]:.2f}, Bob {b[3][1]:.2f}, Carol {b[3][2]:.2f}")
        tiers(np.r_[b[2], b[3]], "   mission tiers")
    print("\n== Mission tiers for the comparators ==")
    tiers(np.r_[13.5, -1.0, -2.5, -4.0], "  ordinance")
    tiers(np.r_[1.5, 1.5, 1.5, 1.5], "  fair deal")
    tiers(np.r_[6.0, 0.0, 0.0, 0.0], "  k=3 base, IR-binding")
    print("\n== Robustness: night profit p_N varied, k=2 DAC schedule choice ==")
    for pn in (2.0, 3.0, 4.0, 5.0):
        p = P.copy(); p[3] = pn
        b = best(full_info(2, p), "DAC")
        print(f"  p_N={pn}: chosen {sname(b[1])}, company {b[2]:.2f}, Carol {b[3][2]:.2f}")
    print("\n== Finite estimation, k=2. err = sigma/sqrt(c_f); residents' c_N irrelevant ==")
    print("  columns: pass rate | four-slot rate | E[company] | E[Alice] E[Bob] E[Carol] | P(Carol < ordinance -4)")
    runs = [("naive m=0", dict(margin=0.0)), ("naive m=0.5", dict(margin=0.5)),
            ("cautious (planning)", dict(cautious=True, n=1200)),
            ("naive m=0.5, SIMULTANEOUS updating", dict(margin=0.5, mode="simultaneous"))]
    for label, kw in runs:
        print(f"  -- principal {label} --")
        for err in (1.0, 0.3, 0.1):
            o = simulate(err, **kw)
            print(f"   err {err:3.1f}: pass {o['pass']:.2f} | four {o['four']:.2f} | {o['pos'][0]:6.2f} | "
                  f"{o['pos'][1]:5.2f} {o['pos'][2]:5.2f} {o['pos'][3]:6.2f} | {o['carol_below_ord']:.2f}")


if __name__ == "__main__":
    main()
