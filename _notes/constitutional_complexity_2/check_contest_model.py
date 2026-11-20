# Unified model: firm buys effort B at price c. Each of n residents (stake v/n) supplies personal
# effort a at cost a^(1+alpha)/(1+alpha) and may also buy effort b at price c. Group effort A = sum(a+b).
# Claim: p_G = 1/(1+r), where r = B/A solves r^(1/alpha) (1+r)^2 = v n^((1-alpha)/alpha) c^-(1+1/alpha) while r<=n,
# and r = n (p_G = 1/(n+1)) for c below c* = (v/(n (n+1)^2))^(alpha/(1+alpha)).
import numpy as np
from scipy.optimize import brentq, minimize_scalar

def closed(v, n, alpha, c):
    rhs = v * n**((1-alpha)/alpha) * c**(-(1+1/alpha))
    f = lambda r: r**(1/alpha)*(1+r)**2 - rhs
    r = brentq(f, 1e-12, 1e12)
    return min(r, n)

def member_cost(e, alpha, c):
    # cheapest way to supply total effort e: personal up to c^(1/alpha), purchased beyond
    k = c**(1/alpha)
    return np.where(e <= k, e**(1+alpha)/(1+alpha), k**(1+alpha)/(1+alpha) + c*(e-k))

def nash(v, n, alpha, c, iters=4000):
    # symmetric equilibrium by damped best-response iteration on (e, B)
    e, B = (v/(c*(n+1)**2))/n, v/(4*c)
    for _ in range(iters):
        A_others = (n-1)*e
        # resident best response in own effort x
        obj = lambda x: -((v/n)*(A_others+x)/(A_others+x+B) - float(member_cost(x, alpha, c)))
        x = minimize_scalar(obj, bounds=(0, 50*v/c), method="bounded", options={"xatol":1e-12}).x
        A = n*e
        objB = lambda y: -(v*y/(A+y) - c*y)
        y = minimize_scalar(objB, bounds=(0, 50*v/c), method="bounded", options={"xatol":1e-12}).x
        e, B = 0.9*e + 0.1*x, 0.9*B + 0.1*y
    return n*e, B

v, n = 100.0, 20
for alpha in (0.5, 1.0, 2.0):
    cstar = (v/(n*(n+1)**2))**(alpha/(1+alpha))
    print(f"alpha={alpha}  c*={cstar:.4f}  floor 1/(n+1)={1/(n+1):.4f}")
    for c in (8*cstar, 3*cstar, 1.5*cstar, 1.0*cstar, 0.5*cstar, 0.1*cstar):
        r = closed(v, n, alpha, c)
        A, B = nash(v, n, alpha, c)
        print(f"   c={c:9.4f}  closed p_G={1/(1+r):.4f}   numeric p_G={A/(A+B):.4f}   spend firm={c*B:7.3f}")
# dependence on n at a fixed high price (personal-effort regime)
print("fixed c=3.0 (personal regime), v=100:")
for alpha in (0.5, 1.0, 2.0):
    print("  alpha", alpha, [round(1/(1+closed(100.0, m, alpha, 3.0)),3) for m in (2, 5, 20)],
          "floors", [round(1/(m+1),3) for m in (2,5,20)])
