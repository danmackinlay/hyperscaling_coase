# Finite budgets, fleet take-it-or-leave-it: fleet sees s_hat = s + eps*z, offers each resident
# its estimated harm on schedule x plus a common margin m (m chosen ex ante to maximise the
# fleet's expected payoff); deal iff every resident's offer covers its true harm (k=3).
# The fleet's model is the parametric one in both arms (it does not know resident 3's 1.5 term).
import itertools, numpy as np
p = np.array([4, 5.5, 4, 5.0]); E = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s = np.array([1,1,2.0])
LANGS = {"four": list(itertools.product([0,1],repeat=4)),
         "two MDE|N": [(0,0,0,0),(1,1,1,0),(0,0,0,1),(1,1,1,1)],
         "two MD|EN": [(0,0,0,0),(1,1,0,0),(0,0,1,1),(1,1,1,1)],
         "one": [(0,0,0,0),(1,1,1,1)]}
rng = np.random.default_rng(1); R = 40000
def run(lang, eps, arb, m, Z):
    X = np.array(lang, float)                    # L x 4
    expo = E @ X.T                               # 3 x L
    htrue = s[:,None]*expo                        # 3 x L
    if arb: htrue[2] += 1.5*(X[:,0]*X[:,2])
    shat = s[None,:] + eps*Z                      # R x 3
    hhat = shat[:,:,None]*expo[None]              # R x 3 x L
    offer = hhat + m*(X.sum(1)>0)[None,None,:]
    fleet_hat = (p@X.T)[None] - offer.sum(1)      # R x L, fleet's estimated payoff
    fleet_hat[:, X.sum(1)==0] = 0
    j = fleet_hat.argmax(1)
    off = offer[np.arange(R),:,j]; ht = htrue[:,j].T
    ok = np.all(off >= ht, axis=1) & (X[j].sum(1)>0)
    g = np.zeros((R,4))
    g[ok,0] = (p@X.T)[j[ok]] - off[ok].sum(1)
    g[ok,1:] = off[ok] - ht[ok]
    return g, ok, j
for arb in (0,1):
    print("ARBITRARY" if arb else "PARAMETRIC")
    for eps in (1.0, 0.3, 0.1, 0.0):
        Z = rng.standard_normal((R,3))
        for ln, lang in LANGS.items():
            best=None
            for m in np.linspace(0, 3, 301):
                g, ok, j = run(lang, eps, arb, m, Z)
                v = g[:,0].mean()
                if best is None or v > best[0]+1e-12: best=(v,m,g,ok)
            v,m,g,ok = best
            G = g.mean(0); pie = g.sum(1).mean()
            prod = np.prod(G) if np.all(G>0) else 0.0
            print(f"  eps={eps:<4} {ln:10s} m*={m:.2f} deal {ok.mean():.3f} E[pie] {pie:.3f} E[gains] {np.round(G,3)} product {prod:.4f} floor {G.min():.3f} res.share {G[1:].sum()/max(pie,1e-9):.2f}")
