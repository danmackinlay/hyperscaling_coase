"""Decompose the principal's take at the stated cell by who proposed (last 100 periods)."""
import sys; sys.path.insert(0,'.')
from sim import *
def decomp(cfg, seeds):
    acc = {k: [] for k in range(4)}; dm=[]
    for sd in seeds:
        rng = np.random.default_rng(sd); G = grid(cfg.step); lw = np.zeros((1,3,G.size)); T=cfg.T
        for t in range(T):
            prop = rng.integers(0,4); u = rng.random((1,3)); mu = np.zeros((1,3))
            if prop==0:
                Heff = T-t if cfg.H=="T" else min(int(cfg.H), T-t)
                mu[0] = choose_margin(lw[0], cfg, G, Heff, rng)
            a,b,lw2,dl = sampled_step(lw, mu, np.array([prop]), u, cfg, G)
            if t >= T-100: acc[prop].append((a[0], dl[0], b[0].sum()))
            lw = lw2
        p = softmax(lw[0]); dm.append((p*G).sum(-1).mean())
    for k,v in acc.items():
        v=np.array(v); print(cfg.scoring, 'H',cfg.H,'proposer',k,'n',len(v),'principal take | proposer',v[:,0].mean().round(3),'deal',v[:,1].mean().round(3),'residents total',v[:,2].mean().round(3))
    print('contribution to P take: ', {k: round(np.array(v)[:,0].sum()/sum(len(x) for x in acc.values()),3) for k,v in acc.items()}, 'mean final demand', np.mean(dm).round(3))
for sc in ['own_offer','counterfactual']:
    decomp(Cfg(scoring=sc, H=1), [[1,r] for r in range(50)])
