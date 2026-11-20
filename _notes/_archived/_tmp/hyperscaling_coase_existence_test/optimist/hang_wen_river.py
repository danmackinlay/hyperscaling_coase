"""Hang & Wen (2026) eq. (6) on the river at pi=20, k=3: pie 6, four veto players.
Player i's recognition weight pi_i = sum over random orders of
P(i is first to commit successfully) + P(i proposes) * P(nobody commits).
As delta -> 1 the SMPE split converges to pi_i * pie (Eraslan-McLennan).
"""
from itertools import permutations

def weights(rho, prop):
    n = len(rho)
    w = [0.0] * n
    orders = list(permutations(range(n)))
    for mu in orders:
        q = 1.0 / len(orders)
        fail = 1.0
        for i in mu:
            w[i] += q * rho[i] * fail
            fail *= 1 - rho[i]
        for i in range(n):
            w[i] += q * prop[i] * fail
    return w

pie = 6.0
prop = [0.25] * 4
for label, rho in [("symmetric rho=0.5", [0.5] * 4),
                   ("symmetric rho=0.9", [0.9] * 4),
                   ("factory rho=0.9, residents 0.5", [0.9, 0.5, 0.5, 0.5]),
                   ("factory rho=0.99, residents 0.5", [0.99, 0.5, 0.5, 0.5])]:
    w = weights(rho, prop)
    split = [round(x * pie, 3) for x in w]
    print(f"{label:35s} weights={[round(x,3) for x in w]} split(delta->1)={split} residents' share={round(sum(split[1:])/pie,3)}")
