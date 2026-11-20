"""Mechanism LPs on the hard-case instance. Switches: parametric harms, linear money, one-shot,
enforcer assumed, closed system; profits p public (residents' estimation budget infinite);
each s_i private in {1,2}, independent, P(s_i=2)=pr2[i] (common prior / public posterior)."""
import itertools as it
import numpy as np
from scipy.optimize import linprog, minimize

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
S_TRUE = (1, 1, 2)
X = [np.array(x) for x in it.product([0, 1], repeat=4)]
NAMES = ["".join(c for c, b in zip("MDEN", x) if b) or "none" for x in X]
TYPES = (1, 2)
PROFILES = list(it.product(TYPES, repeat=3))


def surplus(x, s):
    return p @ x - sum(s[i] * E[i] @ x for i in range(3))


FB = {s: max(surplus(x, s) for x in X) for s in PROFILES}


class M:
    def __init__(self, pr2, full_t=True):
        self.pr2 = pr2
        self.pt = lambda i, th: pr2[i] if th == 2 else 1 - pr2[i]
        self.P = {s: np.prod([self.pt(i, s[i]) for i in range(3)]) for s in PROFILES}
        self.K = 8
        self.k = {s: n for n, s in enumerate(PROFILES)}
        self.nq = 8 * 16
        self.full_t = full_t
        self.n = self.nq + (24 if full_t else 6)

    def q(self, s, j):
        return self.k[s] * 16 + j

    def t(self, i, s):
        return self.nq + (i * 8 + self.k[s] if self.full_t else i * 2 + s[i] - 1)

    def _others(self, i, A=None):
        for s in PROFILES:
            if A is not None and any(s[j] not in A[j] for j in range(3) if j != i):
                continue
            yield s

    def U(self, i, rep, th, A=None):
        """row: interim utility of resident i, true type th, reporting rep, conditional on s_-i in A_-i."""
        row = np.zeros(self.n); tot = 0.0
        for s in self._others(i, A):
            if s[i] != rep:
                continue
            w = self.P[s] / self.pt(i, rep)
            if w == 0:
                continue
            tot += w
            row[self.t(i, s)] += w
            for j in range(16):
                row[self.q(s, j)] -= w * th * (E[i] @ X[j])
        return row / tot

    def F(self, A=None):
        row = np.zeros(self.n); tot = 0.0
        for s in PROFILES:
            if A is not None and any(s[j] not in A[j] for j in range(3)):
                continue
            w = self.P[s]
            if w == 0:
                continue
            tot += w
            for j in range(16):
                row[self.q(s, j)] += w * (p @ X[j])
            for i in range(3):
                row[self.t(i, s)] -= w
        return row / tot

    def Wrow(self):
        row = np.zeros(self.n)
        for s in PROFILES:
            for j in range(16):
                row[self.q(s, j)] += self.P[s] * surplus(X[j], s)
        return row

    def exante(self, i):
        return sum(self.pt(i, th) * self.U(i, th, th) for th in TYPES if self.pt(i, th) > 0)

    def cons(self, sq_res=None, sq_f=None, ir="interim", sq_res_expost=None, efficient=False, exante_ir=None):
        """IC always. ir: 'interim' (each type >= sq_res[i][th]), 'expost' (each profile >= sq_res_expost),
        'exante' (expected >= exante_ir[i]) or None. Fleet ex ante IR if sq_f given."""
        Aub, bub = [], []
        for i in range(3):
            for th in TYPES:
                if self.pt(i, th) == 0:
                    continue
                for r in TYPES:
                    if r != th and self.pt(i, r) > 0:
                        Aub.append(self.U(i, r, th) - self.U(i, th, th)); bub.append(0.0)
                if ir == "interim":
                    Aub.append(-self.U(i, th, th)); bub.append(-sq_res[i][th])
        if ir == "expost":
            for s in PROFILES:
                for i in range(3):
                    row = np.zeros(self.n); row[self.t(i, s)] = -1
                    for j in range(16):
                        row[self.q(s, j)] += s[i] * (E[i] @ X[j])
                    Aub.append(row); bub.append(-sq_res_expost(i, s))
        if ir == "exante":
            for i in range(3):
                Aub.append(-self.exante(i)); bub.append(-exante_ir[i])
        if sq_f is not None:
            Aub.append(-self.F()); bub.append(-sq_f)
        Aeq, beq = [], []
        for s in PROFILES:
            row = np.zeros(self.n); row[self.k[s] * 16:(self.k[s] + 1) * 16] = 1
            Aeq.append(row); beq.append(1.0)
            if efficient:
                row = np.zeros(self.n)
                for j in range(16):
                    if surplus(X[j], s) < FB[s] - 1e-9:
                        row[self.q(s, j)] = 1
                Aeq.append(row); beq.append(0.0)
        bounds = [(0, 1)] * self.nq + [(None, None)] * (self.n - self.nq)
        return [np.array(Aub), np.array(bub), np.array(Aeq), np.array(beq), bounds]

    def lp(self, c, cons, extra=(), extra_eq=()):
        Aub, bub, Aeq, beq, bounds = cons
        if extra:
            Aub = np.vstack([Aub] + [r for r, _ in extra]); bub = np.concatenate([bub, [b for _, b in extra]])
        if extra_eq:
            Aeq = np.vstack([Aeq] + [r for r, _ in extra_eq]); beq = np.concatenate([beq, [b for _, b in extra_eq]])
        r = linprog(-c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
        if r.status != 0:
            return None
        return r.x

    def logmax(self, cons, rows, base, w, z0):
        Aub, bub, Aeq, beq, bounds = cons
        R = np.array(rows); c0 = np.array(base); w = np.array(w)
        f = lambda z: -np.sum(w * np.log(np.maximum(R @ z - c0, 1e-12)))
        g = lambda z: -(R.T @ (w / np.maximum(R @ z - c0, 1e-12)))
        r = minimize(f, z0, jac=g, method="SLSQP", bounds=bounds,
                     constraints=[{"type": "ineq", "fun": lambda z: bub - Aub @ z, "jac": lambda z: -Aub},
                                  {"type": "eq", "fun": lambda z: Aeq @ z - beq, "jac": lambda z: Aeq}],
                     options={"maxiter": 3000, "ftol": 1e-14})
        return r.x, r.success

    def maximin(self, cons, rows, base, obj):
        lo, hi, best = -20.0, 20.0, None
        for _ in range(50):
            mid = (lo + hi) / 2
            z = self.lp(obj, cons, extra=[(-rows[j], -(base[j] + mid)) for j in range(len(rows))])
            if z is None:
                hi = mid
            else:
                lo, best = mid, z
        return best, lo

    def expost(self, z, s):
        pay = [sum(z[self.q(s, j)] * p @ X[j] for j in range(16)) - sum(z[self.t(i, s)] for i in range(3))]
        pay += [z[self.t(i, s)] - s[i] * sum(z[self.q(s, j)] * E[i] @ X[j] for j in range(16)) for i in range(3)]
        sched = {NAMES[j]: round(z[self.q(s, j)], 3) for j in range(16) if z[self.q(s, j)] > 1e-6}
        return pay, sched


def nash(v):
    return float(np.prod(v)) if min(v) >= -1e-9 else None


def logmax_cuts(m, cons, rows, base, w, iters=400, tol=1e-9):
    """max sum w_j log(rows_j z - base_j) by Kelley cutting planes on the hypograph (LP each step)."""
    Aub, bub, Aeq, beq, bounds = cons
    R = np.array(rows); c0 = np.array(base); w = np.array(w); J = len(rows); n = m.n
    # start: maximin point
    z0, lev = m.maximin(cons, rows, base, m.Wrow())
    if z0 is None or lev <= 0:
        return None, None
    cuts = []
    g = R @ z0 - c0
    best = (np.sum(w * np.log(g)), z0)
    for it_ in range(iters):
        for j in range(J):
            cuts.append((j, g[j]))
        # variables [z, y_1..y_J]; maximise sum w y; y_j <= log gk + (R_j z - c0_j - gk)/gk
        A = [np.hstack([Aub, np.zeros((len(Aub), J))])]; b = [bub]
        for j, gk in cuts:
            row = np.zeros(n + J); row[:n] = -R[j] / gk; row[n + j] = 1
            A.append(row[None, :]); b.append([np.log(gk) - 1 - (-c0[j]) / gk * 1.0 + 0.0])
            # y <= log gk + (R z - c0 - gk)/gk  <=>  y - R z/gk <= log gk - 1 - c0/gk
            b[-1] = [np.log(gk) - 1 - c0[j] / gk]
        A = np.vstack(A); b = np.concatenate(b)
        Ae = np.hstack([Aeq, np.zeros((len(Aeq), J))])
        c = np.concatenate([np.zeros(n), -w])
        r = linprog(c, A_ub=A, b_ub=b, A_eq=Ae, b_eq=beq,
                    bounds=list(bounds) + [(-50, 50)] * J, method="highs")
        z = r.x[:n]; g = R @ z - c0
        ub = -r.fun
        val = np.sum(w * np.log(np.maximum(g, 1e-300))) if min(g) > 0 else -np.inf
        if val > best[0]:
            best = (val, z)
        if ub - best[0] < tol:
            break
        g = np.maximum(g, 1e-6)
    return best[1], (best[0], ub, it_)
