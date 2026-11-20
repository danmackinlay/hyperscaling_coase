"""Arm 2c climb under drawn sensitivities. Each street's s_i iid in {1,2}, P(2)=p2.
Club demand d: fixed 1.5, or 'street' = that street's pie/4 (needs residents to know the pie).
Averages over N draws of streets; seeds 1 and 2. Reports residents' share, fraction of
deals at harm-only, chosen-street Carol gain, floor vs status quo (ordinance by lot).
"""
import sys, numpy as np
from model import E,P,SCHEDS,efficient,principal_policy

def run(K,q,d_mode,p2,seed,N=20000):
    rng=np.random.default_rng(seed)
    tot_prin=tot_res=0.0; harm_only=0.0; gm_acc=[]; res_by_slot=np.zeros(3); sq_res=np.zeros(3)
    for _ in range(N):
        s_list=[np.where(rng.random(3)<p2,2,1) for _ in range(K)]
        d = 1.5 if d_mode=='fixed' else None
        if d is None:
            # street-specific fair share: use the mean pie/4 across streets as one common price (club rule),
            # since the club posts one price; report also the per-street exact variant below
            d = np.mean([efficient(s)[0]/4 for s in s_list])
        prin,pol,res,p_deal=principal_policy(K,q,d,s_list)
        tot_prin+=prin; tot_res+=res.sum(); res_by_slot+=res.sum(axis=0)
        harm_only+= sum(1 for k in range(K) if pol[k]=='L')*((1-q)**3)  # expected low acceptances per period (approx share of deals at harm-only)
        # ordinance by lot: expected positions
        x=np.array([1,1,1,0])
        sq_res+= -np.mean([s*(E@x) for s in s_list],axis=0)
    return tot_prin/N, tot_res/N, res_by_slot/N, sq_res/N

for p2 in [0.5,0.25]:
    for d_mode in ['fixed','street']:
        for q in [0.5,0.75]:
            for K in [1,2,3]:
                for seed in [1,2]:
                    pr,rs,slot,sq=run(K,q,d_mode,p2,seed,N=4000)
                    pie=pr+rs
                    print(f"p2={p2} d={d_mode} q={q} K={K} seed={seed} | prin={pr:.3f} res={rs:.3f} share={rs/pie:.3f} | per-slot res gain (A,B,C) summed over streets={np.round(slot,3)} | ordinance-by-lot expected pos (A,B,C) in a street={np.round(sq,2)}")
