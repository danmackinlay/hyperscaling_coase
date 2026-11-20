import sys; sys.path.insert(0, "/private/tmp/claude-501/-Users-dan-Source-livingthing/ba681c6b-2fa0-4067-ae93-aaf86e99fe48/scratchpad")
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize
import budgets as B

# 1. brute-force check of fleet_offer (schedule MDE, eps 0.3, a few A values)
x = np.array([1, 1, 1, 0]); Ex = B.E @ x; sds = 0.3 * Ex; active = Ex > 0
for A in (6.0, 3.0, 0.5, -1.0):
    gain, z = B.fleet_offer(np.array([A]), sds, active)
    obj = lambda m: -((A - m.sum()) * np.prod(norm.cdf(m / sds)))
    best = min((minimize(obj, x0, method="Nelder-Mead", options=dict(xatol=1e-8, fatol=1e-10)) for x0 in
                (np.zeros(3), sds, -sds, 0.5 * sds)), key=lambda r: r.fun)
    print(f"fleet A={A:5}: closed {gain[0]:.5f}  brute {-best.fun:.5f}  m closed {np.round(sds*z[0],4)} brute {np.round(best.x,4)}")
# 2. bloc_offer
sd = 0.3 * np.sqrt(3)
for Bv in (6.0, 3.0, 0.5, -1.0):
    val, z = B.bloc_offer(np.array([Bv]), sd)
    obj = lambda m: -((Bv - m[0]) * norm.cdf(m[0] / sd))
    best = min((minimize(obj, [x0], method="Nelder-Mead", options=dict(xatol=1e-8, fatol=1e-10)) for x0 in (0, sd, -sd)), key=lambda r: r.fun)
    print(f"bloc  B={Bv:5}: closed {val[0]:.5f}  brute {-best.fun:.5f}  m closed {sd*z[0]:.4f} brute {best.x[0]:.4f}")

# 3. re-seed the T block (fleet and bloc, parametric), 20000 draws
B.rng = np.random.default_rng(99)
for ef in B.EPS:
    pay, d = B.fleet_round(ef, 20000, False); print("reseed fleet", ef, B.fmt(B.summarise(pay), d))
for eN in B.EPS:
    pay, d = B.bloc_round(eN, 20000, False); print("reseed bloc ", eN, B.fmt(B.summarise(pay), d))

# 4. fleet's night-slot cases at eps_f=1: how many chosen, how many accepted
B.rng = np.random.default_rng(5)
pay, d = B.fleet_round(1.0, 40000, False)
print("fleet eps 1: N chosen", d["N_chosen"], "N dealt", d["N_dealt"], "deal", d["deal"])
# naive flip rates for comparison
for e in B.EPS:
    print(f"naive flip P(est. night surplus>0): fleet {norm.cdf(-0.5/(e*np.sqrt(5.25))):.3f}  residents {norm.cdf(-0.5/e):.3f}")
