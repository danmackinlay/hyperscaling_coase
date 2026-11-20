"""Arm 2a, the formation stage, on the noise-schedule family.

Model (stated in full in the report):
  slots M,D,E,N, profit p=(4,5.5,4,5) per triple, scaled by m=n/3;
  exposures A=(.5,0,.5,1), B=(1,1,.5,.5), C=(.5,.5,1,2), unscaled harms s_i e_i.x;
  s_i private, P(s_i=2)=q (q=1/2 main, 1/4 robustness), base case s=(1,1,2).
  Protocol T, one shot, offers private.  Consent: deal iff #accepts >= k.
  L0 responder: accept iff payment - s_i e_i.x >= d_i  (d=0, or the pact's g).
  t=0 principal: expected-profit max under the prior (no pact).
  t=1 a proposer drawn uniformly among residents picks g in G (>0) and a recipient
      set, paying c per recipient; a pact forms only if each recipient would sign at
      either sensitivity (signing raises her expected gain vs staying out, others fixed).
  t=2 principal sees signatories (variant 'see'), revises schedule and offers once.
      Variant 'blind': principal keeps t=0 offers (does not observe or revise).
  t=3 responses.
  Organisation: every resident bound at d=g, g chosen by the body to maximise members'
      ex-ante total expected gain; F paid once, split equally; no message cost.
"""
import itertools, math, sys
import numpy as np

P = np.array([4, 5.5, 4, 5])
E = np.array([[.5, 0, .5, 1], [1, 1, .5, .5], [.5, .5, 1, 2]])
XS = [np.array(b) for b in itertools.product([0, 1], repeat=4)]
NAMES = "MDEN"
LMAX = 8
GGRID = [0.25 * i for i in range(1, 17)]  # positive part of G = {-2,...,4}


def binom_cdf(L, q, t):
    if t < 0:
        return 0.0
    return sum(math.comb(L, i) * q**i * (1 - q) ** (L - i) for i in range(0, min(L, t) + 1))


def solve_principal(groups, m, n, k, q):
    """groups: list of (type, d, N). Returns best (profit, x_index, levels) with
    levels a list of (H,L,Z) per group; profit 0 / None for no deal."""
    r = n - k
    best = (0.0, None, None)
    for xi, x in enumerate(XS):
        rev = m * float(P @ x)
        ex = [float(E[t] @ x) for (t, d, N) in groups]
        cand = []  # groups that need paying
        free = []
        for j, (t, d, N) in enumerate(groups):
            if ex[j] == 0 and d <= 0:
                free.append(j)
            else:
                cand.append(j)
        payH = {j: groups[j][1] + 2 * ex[j] for j in cand}
        payL = {j: groups[j][1] + ex[j] for j in cand}
        # a group with ex==0, d>0: L == H in payment and always accepted; forbid L
        lowok = {j: ex[j] > 0 for j in cand}
        sumH_all = sum(payH[j] * groups[j][2] for j in cand)
        zero_opts = [None] + ([j for j in cand] if r >= 1 else [])
        for zj in zero_opts:
            Zt = 0 if zj is None else 1
            cap = {j: groups[j][2] - (1 if j == zj else 0) for j in cand}
            base_H = sumH_all - (payH[zj] if zj is not None else 0)
            for Lt in range(0, LMAX + 1):
                PD = binom_cdf(Lt, q, r - Zt)
                if PD == 0:
                    break
                PD1 = binom_cdf(Lt - 1, q, r - Zt) if Lt > 0 else 0
                # greedy: weight of converting one resident of group j from H to L
                w = sorted(
                    [(PD * payH[j] - (1 - q) * PD1 * payL[j], j) for j in cand if lowok[j] for _ in range(min(cap[j], Lt))],
                    reverse=True,
                )
                if len(w) < Lt:
                    break
                chosen = w[:Lt]
                prof = PD * (rev - base_H) + sum(wj for wj, _ in chosen)
                if prof > best[0] + 1e-9:
                    lv = []
                    for j in range(len(groups)):
                        if j in free:
                            lv.append((groups[j][2], 0, 0))
                            continue
                        Lj = sum(1 for _, jj in chosen if jj == j)
                        Zj = 1 if j == zj else 0
                        lv.append((groups[j][2] - Lj - Zj, Lj, Zj))
                    best = (prof, xi, lv)
    return best


def member_gain(groups, sol, j, s, n, k, q):
    """Expected gain of a member of group j with own sensitivity s."""
    prof, xi, lv = sol
    if xi is None:
        return 0.0
    x = XS[xi]
    t, d, N = groups[j]
    ex = float(E[t] @ x)
    Lt = sum(l[1] for l in lv)
    Zt = sum(l[2] for l in lv)
    r = n - k
    H, L, Z = lv[j]
    free = ex == 0 and d <= 0
    out = 0.0
    for lvl, cnt in (("H", H), ("L", L), ("Z", Z)):
        if cnt == 0:
            continue
        if free:
            pay, acc = 0.0, True
        elif lvl == "H":
            pay, acc = d + 2 * ex, True
        elif lvl == "L":
            pay, acc = d + ex, s == 1
        else:
            pay, acc = 0.0, (0 - s * ex >= d)
        Lo = Lt - (lvl == "L")
        Zo = Zt - (lvl == "Z")
        pdeal = binom_cdf(Lo, q, r - Zo - (0 if acc else 1))
        g = (pay - s * ex) if acc else (-s * ex)
        out += cnt / N * pdeal * g
    return out


def exante_gain(groups, sol, j, n, k, q):
    return (1 - q) * member_gain(groups, sol, j, 1, n, k, q) + q * member_gain(groups, sol, j, 2, n, k, q)


class Economy:
    def __init__(self, n, k, q):
        self.n, self.k, self.q, self.m = n, k, q, n // 3
        self.cache = {}

    def groups(self, sig, g):
        """sig: signer counts per type (sA,sB,sC)."""
        gr = []
        for t in range(3):
            if sig[t] > 0:
                gr.append((t, g, sig[t]))
            if self.m - sig[t] > 0:
                gr.append((t, 0.0, self.m - sig[t]))
        return gr

    def solve(self, sig, g):
        key = (tuple(sig), g if sum(sig) else 0.0)
        if key not in self.cache:
            gr = self.groups(sig, g)
            self.cache[key] = (gr, solve_principal(gr, self.m, self.n, self.k, self.q))
        return self.cache[key]

    def gain_of(self, sig, g, t, signer, s):
        gr, sol = self.solve(sig, g)
        for j, (tt, d, N) in enumerate(gr):
            if tt == t and ((d == g and signer and sum(sig) > 0) or (d == 0 and not signer)):
                return member_gain(gr, sol, j, s, self.n, self.k, self.q)
        raise KeyError

    def proposer_choice(self, tp, sp, c, ggrid=GGRID, strict=True):
        """Best option for a proposer of type tp with own s=sp.
        Returns (value, g, sig) with sig=None for no pact."""
        zero = (0, 0, 0)
        best = (self.gain_of(zero, 0.0, tp, False, sp), None, None)
        m = self.m
        ranges = [range(0, m + 1)] * 3
        for g in ggrid:
            for sig in itertools.product(*ranges):
                if sig[tp] < 1:
                    continue
                nrec = sum(sig) - 1
                if nrec == 0:
                    continue  # a pact needs at least two signatories
                val = self.gain_of(sig, g, tp, True, sp) - c * nrec
                if val <= best[0] + 1e-9:
                    continue
                # stability: each recipient type present (excluding proposer) signs at both s
                ok = True
                for t in range(3):
                    nrec_t = sig[t] - (1 if t == tp else 0)
                    if nrec_t <= 0:
                        continue
                    out = list(sig)
                    out[t] -= 1
                    diffs = [self.gain_of(sig, g, t, True, s) - self.gain_of(tuple(out), g, t, False, s) for s in (1, 2)]
                    if min(diffs) < -1e-9 or (strict and max(diffs) <= 1e-9):
                        ok = False
                    if not ok:
                        break
                if ok:
                    best = (val, g, sig)
        return best


def describe(econ, sig, g):
    gr, sol = econ.solve(sig, g)
    prof, xi, lv = sol
    if xi is None:
        return "no deal"
    sched = "".join(NAMES[i] for i in range(4) if XS[xi][i]) or "-"
    parts = []
    for (t, d, N), (H, L, Z) in zip(gr, lv):
        parts.append(f"{'ABC'[t]}{'*' if d>0 else ''}[H{H} L{L} Z{Z}]")
    return f"{sched} profit={prof:.3f} " + " ".join(parts)


if __name__ == "__main__":
    n, k, q = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    econ = Economy(n, k, q)
    print("t=0:", describe(econ, (0, 0, 0), 0.0))
    for t in range(3):
        print("  ", "ABC"[t], [round(econ.gain_of((0, 0, 0), 0.0, t, False, s), 3) for s in (1, 2)])
