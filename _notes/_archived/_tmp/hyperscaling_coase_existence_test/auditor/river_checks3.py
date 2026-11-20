"""Row 1, posterior variant: factory sees hhat = h + e, flat prior, picks margin m(hhat) to maximise
Phi(m/sig)^3 * (20 - sum(hhat) - 3m); realised outcome scored against the true harms (2,3,9)."""
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize_scalar

rng = np.random.default_rng(0); H = np.array([2., 3., 9.]); N = 40000
for sig in [1.5, 1.0, 0.5, 0.1, 0.01]:
    e = rng.normal(0, sig, (N, 3)); Phat = 6 - e.sum(1)
    grid = np.linspace(-6 * sig - 3, 6 * sig + 3, 2001)
    obj = norm.cdf(grid[None, :] / sig) ** 3 * (Phat[:, None] - 3 * grid[None, :])
    m = grid[obj.argmax(1)]
    acc = (e + m[:, None] >= 0).all(1)
    t = H + e + m[:, None]
    fac = np.where(acc, 20 - t.sum(1), 0.0); res = np.where(acc[:, None], t - H, 0.0)
    print(f"sig={sig:5}: deal={acc.mean():.4f} factory_E={fac.mean():.3f} (P(factory<0)={(fac < 0).mean():.3f}) "
          f"res_E={np.round(res.mean(0), 3)} res_total={res.sum(1).mean():.3f}")
