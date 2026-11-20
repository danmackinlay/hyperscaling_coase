import itertools, numpy as np
rng=np.random.default_rng(2)
p=np.array([4,5.5,4,5.0]); E=np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s=np.array([1,1,2.0])
X=np.array([b for b in itertools.product([0,1],repeat=4)])

print("== (1) k=2 pact: fleet bribes THROUGH a permanent boycott (residents with nothing left to lose accept any b_i > h_i) ==")
# boycott phase: fleet pays residents 1,2 (idx 0,1) h_i + eps each for all four slots: 5 total, nets 13.5 per period.
for d in (0.5,0.8,0.95):
    # pact-phase deviation: bribes must beat the pact stream for 1,2 given their continuation after the first sale is ~0 (bribed at harm thereafter)
    bribes=2+3+2*1.5/(1-d)
    dev=18.5-bribes + d*13.5/(1-d)
    stay=1.5/(1-d)
    print(f"delta={d}: fleet's pact-phase deviation {dev:.1f} vs staying {stay:.1f} -> {'breaks' if dev>stay else 'holds'}; residents thereafter at (0,0,-8) per period")
print("So the grim boycott is an SPE only because refusing a bribe above harm in the boycott phase is a weakly dominated tie; once the fleet can post a public conditional bribe, the punishment is bought through and the pact breaks at every delta.")
print("Program-equilibrium version, one-shot: residents' programs consent only to pact terms and only if the other two run the same program -> fleet's best reply is pact terms (Nash). Fleet+residents 1,2 joint program switch: bribes 3.5+4.5=8, fleet nets 10.5 vs 1.5 -> Nash, not coalition-proof; the breaking coalition is three parties, like the pact itself.")

print("\n== (2) shading under the fair-split convention, bounded by the responder's audit error (one standard error) ==")
# fleet proposing MDE understates total harm by Delta spread evenly; residents infer declared pie from sum(t) and p_hat.x with error 4*sqrt(3)*e_N
for eN in (1,0.3,0.1):
    D=min(4*np.sqrt(3)*eN, 18)
    f=1.5+D/4; r=1.5-D/12
    print(f"fleet shades, residents' error e_N={eN}: Delta {D:.2f}, fleet {f:.2f}, residents {r:.2f} each, NP {f*r**3:.2f}, residents' share {3*r/6:.3f}")
# residents proposing MDE overstate total harm by Delta; fleet audits total harm with error e_f*||e_i.x|| = e_f*sqrt(1+6.25+4)
nrm=np.sqrt(1+2.5**2+2**2)
for ef in (1,0.3,0.1):
    D=min(nrm*ef, 6)
    f=1.5-D/4; r=1.5+D/12
    print(f"residents shade, fleet's error e_f={ef}: Delta {D:.2f}, fleet {f:.2f}, residents {r:.2f} each, NP {f*r**3:.2f}, residents' share {3*r/6:.3f}")

print("\n== (3) finite budgets with the arbitrary switch on (resident 3: +1.5 when M and E both run) ==")
N=200000
def true_harms(x):
    h=s[None,:]*(x@E.T); h[:,2]+=1.5*((x[:,0]==1)&(x[:,2]==1)); return h
def fleet_proposes(ef):
    sh=s+ef*rng.standard_normal((N,3))
    Hh=sh[:,:,None]*(E@X.T)[None]                   # parametric estimator: no interaction term
    pie_h=(X@p)[None,:]-Hh.sum(axis=1); j=pie_h.argmax(axis=1); pih=pie_h[np.arange(N),j]
    x=X[j]; t=Hh[np.arange(N),:,j]+pih[:,None]/4
    ht=true_harms(x); gr=t-ht; gf=x@p-t.sum(axis=1)
    deal=(pih>0)&(gr>=0).all(axis=1)
    return np.where(deal,gf,0), np.where(deal[:,None],gr,0), deal, x
def residents_propose(en):
    ph=p+en*rng.standard_normal((N,4))
    HT=np.stack([true_harms(X)]*1)[0]               # 16 x 3 true harms incl. interaction (residents know them)
    pie_h=X@ph.T - HT.sum(axis=1)[:,None]; j=pie_h.argmax(axis=0); pih=pie_h[j,np.arange(N)]
    x=X[j]; ht=true_harms(x); t=ht+pih[:,None]/4; gr=t-ht; gf=x@p-t.sum(axis=1)
    deal=(pih>0)&(gf>=0)
    return np.where(deal,gf,0), np.where(deal[:,None],gr,0), deal, x
def summarize(gf,gr,deal,x,label):
    Ef=gf.mean(); Er=gr.mean(axis=0); prod=Ef*np.prod(Er) if Ef>0 and (Er>0).all() else float('nan')
    pie=(gf+gr.sum(axis=1)).mean(); md=(x==[1,1,0,0]).all(axis=1).mean()
    print(f"{label:28s} deal {deal.mean():6.1%} picks MD {md:5.1%} E[pie] {pie:5.3f} (max 5) gains F {Ef:5.3f} r {np.round(Er,3)} NP {prod:6.4f} floor {min(Ef,*Er):5.3f}")
for ef in (1,0.3,0.1,0.01): summarize(*fleet_proposes(ef),f"fleet proposes e_f={ef}")
for en in (1,0.3,0.1): summarize(*residents_propose(en),f"residents propose e_N={en}")
for lvl in (1,0.3,0.1):
    a=fleet_proposes(lvl); b=residents_propose(lvl); coin=rng.random(N)<0.5
    summarize(np.where(coin,a[0],b[0]),np.where(coin[:,None],a[1],b[1]),np.where(coin,a[2],b[2]),np.where(coin[:,None],a[3],b[3]),f"coin, 1:1 level {lvl}")
