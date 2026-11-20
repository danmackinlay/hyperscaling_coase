import sys; sys.path.insert(0,'.')
from sim import *
import collections
def trace(cfg, seed):
    rng = np.random.default_rng(seed); G = grid(cfg.step); lw = np.zeros((1,3,G.size))
    mus = collections.Counter(); T=cfg.T
    byprop = collections.defaultdict(list)
    for t in range(T):
        prop = rng.integers(0,4); u = rng.random((1,3)); mu = np.zeros((1,3))
        if prop==0:
            Heff = T-t if cfg.H=="T" else min(int(cfg.H), T-t)
            mu[0] = choose_margin(lw[0], cfg, G, Heff, rng)
            if t>T-100: mus[tuple(mu[0])]+=1
        a,b,lw,dl = sampled_step(lw, mu, np.array([prop]), u, cfg, G)
        if t>=T-100: byprop[prop].append((a[0], dl[0]))
        if t % 100 == 99:
            p = softmax(lw[0]); print(t, np.round((p*G).sum(-1),2), np.round(p.max(-1),2), G[p.argmax(-1)])
    print(mus.most_common(5))
    for k,v in sorted(byprop.items()): v=np.array(v); print('prop',k,len(v),'Ptake',v[:,0].mean().round(2),'deal',v[:,1].mean().round(2))
trace(Cfg(H=1),1); trace(Cfg(H=10),1)
