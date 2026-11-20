"""Checks for four derivations discussed with Dan but NOT yet in draft.md: pledgeable-gain lending, capped (solvable) matters, the cost of a subsidy, and complexity chosen by a participant. See HANDOVER.md, "Derived but not written up".

Run from the repository root:
  uv run --no-project --with numpy --with scipy python _notes/personal_budget_2/check_pending_derivations.py
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq

# 1. Pledgeable-gain lending at r=1, single matter S, R=1, opponent unconstrained.
S = 4000.0
def opp_br(xi):
    f = lambda xj: -(S * xj / (xi + xj) - xj)
    return minimize_scalar(f, bounds=(1e-9, S), method="bounded", options={"xatol": 1e-10}).x
def share(xi):
    xj = opp_br(xi)
    return xi / (xi + xj)
for w, psi in [(160, 0.0), (160, 0.2), (160, 1/3), (0.0, 0.3), (160, 0.42), (160, 0.6)]:
    rho = w / S
    # fixed point: spend = w + psi * s * S, capped at parity spend S/4
    g = lambda s: share(min(w + psi * s * S, S / 4)) - s
    s_num = brentq(g, 1e-6, 0.999)
    s_formula = min(0.5, (psi + np.sqrt(psi**2 + 4 * rho)) / 2)
    net = s_num * S - min(psi * s_num * S, max(S / 4 - w, 0)) + max(w - S/4, 0)
    print(f"w={w:6.0f} psi={psi:.3f}  s_num={s_num:.4f}  s_formula={s_formula:.4f}  threshold psi*={0.5-2*rho:.3f}  net={net:8.1f}")

# 2. Capped compute: effective compute min(c, G). Symmetric equilibrium spend and waste.
def eq_spend(r, S, p, G):
    cstar = r * S / (4 * p)
    c = min(cstar, G)
    # verify no profitable deviation on a grid
    cj = c
    def pay(ci):
        zi, zj = min(ci, G) ** r, min(cj, G) ** r
        return S * zi / (zi + zj) - p * ci
    grid = np.linspace(1e-6, 3 * max(c, 1e-6), 20001)
    best = grid[np.argmax([pay(x) for x in grid])]
    return c, best, 2 * p * c / S
for p in [1e-1, 1e-2, 1e-3, 1e-4]:
    c, best, waste = eq_spend(1.0, 1.0, p, G=50.0)
    print(f"p={p:7.0e}  G=50  eq c={c:8.2f}  best dev={best:8.2f}  waste/S={waste:.4f}  solved iff pG<rS/4: {p*50 < 0.25}")

# 3. Subsidy to a liquidity-constrained principal at r=1, R=1, one matter of surplus S.
#    Claim: per subsidy dollar the recipient gains 1/(2s), the opponent loses (1-s)/s,
#    the payer loses 1; so others lose 2 dollars per dollar the recipient gains.
print()
w = 160.0
def outcome(sigma):
    xi = w + sigma
    xj = opp_br(xi)
    s = xi / (xi + xj)
    return s, s * S, (1 - s) * S - xj   # share, recipient income, opponent net
for sigma in [0.0, 200.0, 500.0, 800.0]:
    h = 1e-2
    s, yi, yj = outcome(sigma)
    _, yi2, yj2 = outcome(sigma + h)
    gi, lj = (yi2 - yi) / h, -(yj2 - yj) / h
    print(f"subsidy={sigma:5.0f} s={s:.3f}  recipient +{gi:.3f} (1/2s={1/(2*s):.3f})  opponent -{lj:.3f} ((1-s)/s={(1-s)/s:.3f})  others lose per $ gained: {(lj+1)/gi:.3f}  total net surplus={yi + yj:8.1f} (S(1-s)={S*(1-s):8.1f})")

# 4. Complexity chosen by a participant. Detail n gives surplus S(n) = Sbar (1 - delta^n) and
#    costs G(n) = G0 gamma^n to solve outright. Both sides unconstrained, r = 1, merit share 1/2.
#    A side's payoff is S(n)/2 - p G(n) if the matter is solved in equilibrium (p G(n) < r S(n)/4),
#    and S(n) (1/2 - r/4) otherwise. Which n does a drafter facing an equal opponent choose?
print()
Sbar, delta, gamma, G0, r = 1.0, 0.7, 2.0, 1.0, 1.0
n = np.linspace(0.0, 60.0, 600001)
Sn, Gn = Sbar * (1 - delta**n), G0 * gamma**n
for p in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-9]:
    solved = p * Gn < r * Sn / 4
    pay = np.where(solved, Sn / 2 - p * Gn, Sn * (0.5 - r / 4))
    k = int(np.argmax(pay))
    best_solved = np.max(np.where(solved, pay, -np.inf))
    waste = 2 * p * Gn[k] / Sn[k] if solved[k] else r / 2
    print(f"p={p:6.0e}  chosen n={n[k]:6.2f}  solved={bool(solved[k])}  payoff={pay[k]:.4f}  "
          f"best solved payoff={best_solved:.4f}  contest ceiling={Sbar*(0.5-r/4):.4f}  waste/S={waste:.4f}")
