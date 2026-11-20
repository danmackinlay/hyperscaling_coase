"""Pact-stage computations on the hard-case instance (parametric switch, linear money,
one-shot, enforcer assumed, closed). Private sensitivities s_i in {1,2}, iid, P(s_i=2)=P2.
"""
import itertools as it
import numpy as np
from scipy.optimize import linprog, minimize

p = np.array([4, 5.5, 4, 5.0])
E = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])
S_TRUE = (1, 1, 2)
X = [np.array(x) for x in it.product([0, 1], repeat=4)]  # 16 schedules, index order MDEN
NAMES = ["".join(c for c, b in zip("MDEN", x) if b) or "none" for x in X]
TYPES = [1, 2]


def profiles(P2):
    out = []
    for s in it.product(TYPES, repeat=3):
        pr = np.prod([P2 if si == 2 else 1 - P2 for si in s])
        out.append((s, pr))
    return out


def surplus(x, s):
    return p @ x - sum(s[i] * E[i] @ x for i in range(3))


def first_best(s):
    vals = [surplus(x, s) for x in X]
    m = max(vals)
    return m, [NAMES[j] for j, v in enumerate(vals) if abs(v - m) < 1e-9]


class LP:
    """Variables: q[k,j] prob of schedule j at profile k (8x16), t[i,k] transfer to resident i."""

    def __init__(self, P2):
        self.P2 = P2
        self.prof = profiles(P2)
        self.K = len(self.prof)
        self.nq = self.K * 16
        self.n = self.nq + 3 * 2
        self.kidx = {s: k for k, (s, _) in enumerate(self.prof)}

    def qi(self, k, j):
        return k * 16 + j

    def ti(self, i, k):
        # k is a profile index; transfer depends on resident i's own report only
        s = self.prof[k][0]
        return self.nq + i * 2 + (s[i] - 1)

    def tau(self, i, th):
        return self.nq + i * 2 + (th - 1)

    def cond_prob(self, i, s_mi_set=None):
        """weights over profiles given resident i's type; returns dict theta-> list of (k_other, weight)"""
        pass

    def interim_row(self, i, report, theta, A=None):
        """Coefficient row: U_i(report|theta) (unnormalised conditional expectation over s_-i in A_-i)."""
        row = np.zeros(self.n)
        tot = 0.0
        for k, (s, pr) in enumerate(self.prof):
            if s[i] != report:
                continue
            if A is not None and any(s[j] not in A[j] for j in range(3) if j != i):
                continue
            w = pr / (self.P2 if report == 2 else 1 - self.P2)  # prob of s_-i
            tot += w
            row[self.ti(i, k)] += w
            for j in range(16):
                row[self.qi(k, j)] -= w * theta * (E[i] @ X[j])
        return row / tot

    def fleet_row(self, A=None):
        row = np.zeros(self.n)
        tot = 0.0
        for k, (s, pr) in enumerate(self.prof):
            if A is not None and any(s[j] not in A[j] for j in range(3)):
                continue
            tot += pr
            for j in range(16):
                row[self.qi(k, j)] += pr * (p @ X[j])
            for i in range(3):
                row[self.ti(i, k)] -= pr
        return row / tot

    def exante_row(self, i):
        row = np.zeros(self.n)
        for th in TYPES:
            w = self.P2 if th == 2 else 1 - self.P2
            row += w * self.interim_row(i, th, th)
        return row

    def base_constraints(self, sq_res, sq_fleet, ir=True):
        """IC for all residents; interim IR vs status quo sq_res[i][theta]; fleet ex ante IR."""
        A_ub, b_ub = [], []
        for i in range(3):
            for th in TYPES:
                for r in TYPES:
                    if r != th:
                        A_ub.append(self.interim_row(i, r, th) - self.interim_row(i, th, th))
                        b_ub.append(0.0)
                if ir:
                    A_ub.append(-self.interim_row(i, th, th))
                    b_ub.append(-sq_res[i][th])
        if sq_fleet is not None:
            A_ub.append(-self.fleet_row())
            b_ub.append(-sq_fleet)
        A_eq, b_eq = [], []
        for k in range(self.K):
            row = np.zeros(self.n)
            row[k * 16:(k + 1) * 16] = 1
            A_eq.append(row)
            b_eq.append(1.0)
        bounds = [(0, 1)] * self.nq + [(None, None)] * 6
        return np.array(A_ub), np.array(b_ub), np.array(A_eq), np.array(b_eq), bounds

    def solve(self, c, cons, extra_ub=None):
        A_ub, b_ub, A_eq, b_eq, bounds = cons
        if extra_ub:
            A_ub = np.vstack([A_ub] + [r for r, _ in extra_ub])
            b_ub = np.concatenate([b_ub, [b for _, b in extra_ub]])
        res = linprog(-c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
        assert res.status == 0, res.message
        return res.x

    # ---- reporting -----
    def report(self, z, sq_res, sq_fleet, sq_true=None, label=""):
        out = {}
        Gf = self.fleet_row() @ z - sq_fleet
        G = [self.exante_row(i) @ z - (sum((self.P2 if th == 2 else 1 - self.P2) * sq_res[i][th] for th in TYPES)) for i in range(3)]
        exp_surplus = sum(pr * sum(z[self.qi(k, j)] * surplus(X[j], s) for j in range(16)) for k, (s, pr) in enumerate(self.prof))
        k0 = self.kidx[S_TRUE]
        qs = {NAMES[j]: round(z[self.qi(k0, j)], 3) for j in range(16) if z[self.qi(k0, j)] > 1e-6}
        fleet_true = sum(z[self.qi(k0, j)] * p @ X[j] for j in range(16)) - sum(z[self.ti(i, k0)] for i in range(3))
        res_true = [z[self.ti(i, k0)] - S_TRUE[i] * sum(z[self.qi(k0, j)] * E[i] @ X[j] for j in range(16)) for i in range(3)]
        interim = {f"r{i+1}s{th}": round(self.interim_row(i, th, th) @ z, 3) for i in range(3) for th in TYPES}
        out.update(label=label, exante_gains=[round(Gf, 3)] + [round(g, 3) for g in G],
                   exante_nash=round(np.prod([Gf] + G), 4) if min([Gf] + G) >= -1e-9 else None,
                   exp_surplus=round(exp_surplus, 3), at_true_schedule=qs,
                   at_true_payoffs=[round(fleet_true, 3)] + [round(r, 3) for r in res_true],
                   interim=interim)
        if sq_true is not None:
            g = [fleet_true - sq_true[0]] + [res_true[i] - sq_true[i + 1] for i in range(3)]
            out["at_true_gains"] = [round(v, 3) for v in g]
            out["at_true_nash"] = round(np.prod(g), 4) if min(g) >= -1e-9 else None
            out["at_true_floor"] = round(min(g), 3)
            pie = sum(g)
            out["at_true_pie_over_sq"] = round(pie, 3)
            out["at_true_res_share"] = round(sum(g[1:]) / pie, 3) if pie > 1e-9 else None
        return out
