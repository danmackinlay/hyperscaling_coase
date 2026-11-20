import sys; sys.path.insert(0, "/private/tmp/claude-501/-Users-dan-Source-livingthing/ba681c6b-2fa0-4067-ae93-aaf86e99fe48/scratchpad")
import numpy as np, budgets as B
# Converged fixed point: 400 iterations, n=3000, common random numbers; print final step size.
def run(delta, w=0.25, n=3000, iters=400, arb=False):
    print(f"\n=== multi-round delta={delta} w={w} {'arb' if arb else 'param'} (converged) ===")
    for ef in B.EPS:
        for eN in B.EPS:
            v = np.array([w*6]+[(1-w)*2]*3); step=None
            for it in range(iters):
                B.rng = np.random.default_rng(7)
                pf, df = B.fleet_round(ef, n, arb, res=delta*v[1:], cf=delta*v[0], cont=delta*v)
                pb, db = B.bloc_round(eN, n, arb, cf=delta*v[0], cN=delta*v[1:].sum(), cont=delta*v)
                vnew = w*pf.mean(0)+(1-w)*pb.mean(0); step=np.max(np.abs(vnew-v)); v=vnew
                if step<2e-5: break
            g=v; prod=np.prod(g) if np.all(g>=0) else float('nan')
            print(f"eps_f={ef:4} eps_N={eN:4}: v=({g[0]:.2f}; {g[1]:.2f},{g[2]:.2f},{g[3]:.2f}) tot {g.sum():.2f} NP {prod:.3f} floor {g.min():.2f} | per-round deal f {df['deal']:.3f} b {db['deal']:.3f}; its {it+1} step {step:.1e}")
for d in (0.8, 0.95): run(d)
