import random, statistics
random.seed(2)
E={1:2,2:3,3:4}; s={1:1,2:1,3:2}; a={1:1.5,2:1.5,3:1.5}
fleet_gain=17.0
for sd in (1.0,0.3,0.1):
    d=0.8; N=200000; breaks=0; pays=[]; wrongpair=0
    for _ in range(N):
        sh={i:s[i]+random.gauss(0,sd) for i in (1,2,3)}
        req_hat={i:(a[i]+max(sh[i],0)*E[i])/(1-d) for i in (1,2,3)}
        pair=sorted(req_hat,key=req_hat.get)[:2]
        if 3 in pair: wrongpair+=1
        est_bribe=sum(req_hat[i] for i in pair)
        windfall=fleet_gain/(1-d)
        # fleet offers each its estimate plus half the estimated margin, keeping the other half
        extra=(windfall-est_bribe)/2
        offer={i:req_hat[i]+extra/2 for i in pair}
        req_true={i:(a[i]+s[i]*E[i])/(1-d) for i in pair}
        if all(offer[i]>=req_true[i] for i in pair):
            breaks+=1; pays.append(sum(offer.values()))
    print(f"sd={sd} delta={d}: fleet spends half its estimated margin: break prob={breaks/N:.3f}; r3 in chosen pair {wrongpair/N:.3f}; mean bribe {statistics.mean(pays):.1f} of windfall {fleet_gain/(1-d):.1f}")
# expected per-period payoffs at delta=0.8 under the point-estimate bid, break prob q per attempt, pact (1.5 each) until broken then (18.5;-2,-3,-8), bribed pair net 1.5 in the break period only via lump sum... report the long-run average payoff weighting
for q in (0.18,0.25,1.0):
    d=0.8
    # expected discounted payoffs normalised by (1-d): pact until first break at geometric time T
    # resident 3: 1.5 until break, then -8; expectation of normalised discounted value
    # P(not yet broken at t) = (1-q)^t
    v3=sum((1-d)*d**t*((1-q)**t*1.5+(1-(1-q)**t)*(-8)) for t in range(2000))
    vf=sum((1-d)*d**t*((1-q)**t*1.5+(1-(1-q)**t)*18.5) for t in range(2000))
    print(f"q={q}: normalised expected payoff r3={v3:.2f}, fleet={vf:.2f} (r1,r2 held at 1.5 by the bribe)")
