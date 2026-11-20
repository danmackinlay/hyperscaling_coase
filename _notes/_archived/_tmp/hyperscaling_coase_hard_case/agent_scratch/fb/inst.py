"""Hard-case instance: enumeration of the 16 schedules (switches: parametric or arbitrary)."""
import itertools
import numpy as np

P = np.array([4.0, 5.5, 4.0, 5.0])            # M, D, E, N
EXP = np.array([[0.5, 0, 0.5, 1],
                [1, 1, 0.5, 0.5],
                [0.5, 0.5, 1, 2]])
S = np.array([1.0, 1.0, 2.0])
SCHED = np.array(list(itertools.product([0, 1], repeat=4)), dtype=float)  # 16 x 4
NAMES = ["".join(c for c, b in zip("MDEN", x) if b) or "-" for x in SCHED]
EX = SCHED @ EXP.T                            # 16 x 3 exposure per resident
PROFIT = SCHED @ P                            # 16
ME = (SCHED[:, 0] == 1) & (SCHED[:, 2] == 1)  # interaction term flag


def harms(arbitrary=False, s=S):
    h = EX * s                                # 16 x 3
    if arbitrary:
        h = h.copy()
        h[:, 2] += 1.5 * ME
    return h


if __name__ == "__main__":
    for arb in (False, True):
        h = harms(arb)
        pie = PROFIT - h.sum(1)
        order = np.argsort(-pie)
        print("arbitrary" if arb else "parametric")
        for j in order[:6]:
            print(f"  {NAMES[j]:5s} profit {PROFIT[j]:5.1f} harms {h[j]} pie {pie[j]:5.2f}")
