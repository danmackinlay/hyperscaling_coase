"""Row 1 with a separate margin per resident (the factory can price-discriminate by name)."""
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize

H = np.array([2.0, 3.0, 9.0]); PIE = 20.0 - H.sum()

def run(sig):
    sig = np.asarray(sig, float)
    def stats(m):
        z = m / sig; P = norm.cdf(z); g = m + sig * norm.pdf(z) / P
        pd = P.prod(); return pd * (PIE - g.sum()), pd, g
    best = None
    for m0 in [0.0, 0.5, 1.0, 2.0]:
        r = minimize(lambda m: -stats(m)[0], x0=np.full(3, m0), method="Nelder-Mead", options=dict(xatol=1e-6, fatol=1e-9, maxiter=4000))
        if best is None or r.fun < best.fun: best = r
    f, pd, g = stats(best.x)
    return best.x, pd, f, pd * g

for label, mk in [("equal noise", lambda s: [s, s, s]),
                  ("unmeasurable sd 1.0 on harm 9", lambda s: [s, s, np.hypot(s, 1.0)])]:
    print(label)
    for s in [1.5, 1.0, 0.5, 0.1, 0.01]:
        m, pd, f, rE = run(mk(s))
        mins = min(f, rE.min())
        print(f" sig={s:5}: margins={np.round(m,3)} deal={pd:.4f} factory_E={f:.3f} res_E={np.round(rE,3)} res_total={rE.sum():.3f} min payoff={mins:.3f}")
