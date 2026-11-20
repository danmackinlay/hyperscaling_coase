import random, statistics
random.seed(1)
# k=2, egalitarian pact a_i=1.5; fleet estimates s_i with error sd; exposures under all-four: E=(2,3,4); true s=(1,1,2)
E={1:2,2:3,3:4}; s={1:1,2:1,3:2}; a={1:1.5,2:1.5,3:1.5}
fleet_gain=17.0   # per period, egalitarian pact
for sd in (1.0,0.3,0.1):
    for d in (0.5,0.8,0.95):
        breaks=0; fleet_pay=[]; N=200000
        for _ in range(N):
            sh={i:s[i]+random.gauss(0,sd) for i in (1,2,3)}
            req_hat={i:(a[i]+max(sh[i],0)*E[i])/(1-d) for i in (1,2,3)}
            pair=sorted(req_hat,key=req_hat.get)[:2]
            bribe=sum(req_hat[i] for i in pair)
            if bribe>fleet_gain/(1-d): continue  # fleet declines (never happens here)
            req_true={i:(a[i]+s[i]*E[i])/(1-d) for i in pair}
            if all(req_hat[i]>=req_true[i] for i in pair):
                breaks+=1; fleet_pay.append(bribe)
        print(f"sd={sd} delta={d}: break probability per attempt={breaks/N:.3f}; mean bribe when broken={statistics.mean(fleet_pay) if fleet_pay else 0:.1f} vs windfall {fleet_gain/(1-d):.1f}")
