import itertools as it
import numpy as np
from scipy.optimize import linprog
from core2 import *

def screen(m, z):
    """durability screen (H-M voting story, passive beliefs on rejection, learning on approval)."""
    found = []
    for A in it.product([(1,), (2,), (1, 2)], repeat=3):
        n = m.n + 1
        pad = lambda r: np.concatenate([r, [0.0]])
        rows, b = [], []
        for i in range(3):
            for th in TYPES:
                Ud = m.U(i, th, th, A=A) @ z
                if th in A[i]:
                    for rep in TYPES:
                        if rep != th:
                            rows.append(pad(m.U(i, rep, th, A=A) - m.U(i, th, th, A=A))); b.append(0.0)
                    r = -pad(m.U(i, th, th, A=A)); r[-1] = 1; rows.append(r); b.append(-Ud)
                else:
                    for rep in TYPES:
                        rows.append(pad(m.U(i, rep, th, A=A))); b.append(Ud)
        r = -pad(m.F(A=A)); r[-1] = 1; rows.append(r); b.append(-(m.F(A=A) @ z))
        Aeq = []
        for s in PROFILES:
            row = np.zeros(n); row[m.k[s] * 16:(m.k[s] + 1) * 16] = 1; Aeq.append(row)
        c = np.zeros(n); c[-1] = -1
        res = linprog(c, A_ub=np.array(rows), b_ub=b, A_eq=np.array(Aeq), b_eq=np.ones(8),
                      bounds=[(0, 1)] * m.nq + [(None, None)] * (m.n - m.nq) + [(None, 1)], method="highs")
        if res.status == 0 and res.x[-1] > 1e-7:
            found.append(["".join(map(str, a)) for a in A] + [round(res.x[-1], 4)])
    return found


