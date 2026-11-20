"""Row 1 analytic grid: factory-optimal margin, expected gains, floor. Run with uv run python -I."""
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import norm

def prof(m, s):
    z = m / s
    return norm.cdf(z)**3 * (6 - 3*m) - 3*norm.cdf(z)**2 * s * norm.pdf(z)

best = None
for s in np.geomspace(1.5, 0.01, 60):
    m = minimize_scalar(lambda x: -prof(x, s), bounds=(0, 2), method="bounded").x
    z = m / s
    P = norm.cdf(z)**3
    gf = prof(m, s)
    gr = norm.cdf(z)**2 * (m*norm.cdf(z) + s*norm.pdf(z))
    fl = min(gf, gr)
    if best is None or fl > best[0]:
        best = (fl, s, m, P, gf, gr)
    if abs(np.log(s/1.0)) < 0.05 or abs(np.log(s/0.5)) < 0.05 or abs(np.log(s/0.1)) < 0.05:
        print(f"sigma={s:.3f} m*={m:.3f} deal={P:.3f} Gf={gf:.3f} Gr={gr:.3f} floor={fl:.3f}")
print("floor peak: floor=%.3f sigma=%.3f m*=%.3f deal=%.3f Gf=%.3f Gr=%.3f" % best)
# residents' own peak
rs = []
for s in np.geomspace(1.5, 0.01, 200):
    m = minimize_scalar(lambda x: -prof(x, s), bounds=(0, 2), method="bounded").x
    z = m/s
    rs.append((norm.cdf(z)**2*(m*norm.cdf(z)+s*norm.pdf(z)), s))
print("resident gain peak: Gr=%.3f at sigma=%.3f" % max(rs))
