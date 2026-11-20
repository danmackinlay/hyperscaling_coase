"""Collator re-runs for the sampling round, 2026-10-23: the closed-form and trivial claims."""
from math import sqrt
import numpy as np
P = np.array([4, 5.5, 4, 5.0]); E = np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); S = np.array([1,1,2.0])
MDEN = np.ones(4, int); MDE = np.array([1,1,1,0])
h_all = S*(E@MDEN); h_mde = S*(E@MDE)
print("=== E1 (runs 01, 04): k=2 flat fees to the cheapest pair on MDEN ===")
print("harms under MDEN", h_all, "-> fees (2,3,0): company", 18.5-5, "residents", (0,0,-h_all[2]))
print("contingent clauses, all sign, tokens only: company 18.5, residents", -h_all, "; ordinance (MDE unpaid):", -h_mde)
print("club at second-lowest harm 3 a head: company", 18.5-9, "residents", 3-h_all)
print("\n=== E2 (run 12): closed form ===")
for q in (0.3, 0.37, 0.5, 0.75):
    a = (1-q)**3
    print(f"q={q}: a={a:.3f} {'<=1/4: fair price offered to one street' if a <= 0.25 else '>1/4: floor everywhere, residents 0'}; residents' take at K=1,2,3,5:",
          [round(4.5*(1-a)**(K-1), 2) for K in (1,2,3,5)] if a <= 0.25 else [0,0,0,0])
print("reroute all four at 3 per slot:", (P-3).sum(), "vs pie 6; slot-by-slot consentable pie over reroute: M", 4-2.5-(4-3), "D", 5.5-2-(5.5-3), "-> 1.5")
print("\n=== E5 (run 08): closed form, residents pinned at one agent ===")
for ratio, kf in ((1, 0.3), (10, 0.03), (0.1, 3.0)):
    m0 = sqrt(18/kf) - 3; N = m0 + 3
    print(f"c_f:c_N={ratio}:1, kappa_f={kf}: m0={m0:.1f}, company net {6*m0/N - kf*(m0-1):.2f}, each resident {6/N:.3f} (sqrt(2 kappa_f)={sqrt(2*kf):.3f}); fair deal needs kappa_f >= {18/16:.3f}")
print("\n=== E3 (run 10): quick re-run of the by-party proposer with estimation asymmetry ===")
rng = np.random.default_rng(1)
pie = 6.0; harms = h_mde
def cell(sf, sN, draws=20000, grid=np.linspace(0, 6, 241)):
    # fleet seat: offers each resident estimated harm + common margin m chosen to maximise expected profit (exact, by grid on the posterior)
    gains = np.zeros(4); 
    # fleet proposer: residents accept iff offer >= true harm. fleet sees shat_i = h_i + sf*ex_i*z (noise on harm, sd sf*exposure)
    ex = E@MDE
    from scipy.stats import norm
    ms = np.linspace(0, 4, 81)
    # expected profit for margin m: (pie - sum(shat) - 3m) * prod Phi((m)/(sf*ex_i)) approx (treat shat as unbiased)
    if sf > 0:
        pacc = lambda m: np.prod([norm.cdf(m/(sf*e)) for e in ex])
        best = max(ms, key=lambda m: (pie - 3*m)*pacc(m)); 
    else: best = 0.0
    fl = np.zeros(4)
    for _ in range(draws):
        shat = harms + rng.normal(0, 1, 3)*sf*ex
        off = shat + best
        if np.all(off >= harms - 1e-12): fl += np.array([pie - (off - harms).sum() , *(off - harms)])
    fl /= draws
    # resident seat: proposer demands d for herself, gives others their harm; accepted iff true pie >= d; she sees pie + N(0, (sN*sqrt(3))^2)
    rs = np.zeros(4)
    sd = sN*sqrt(3)
    if sN > 0:
        ds = np.linspace(0, 6, 241)
        # her estimate piehat; choose d maximising d * P(pie >= d | piehat) with flat prior: P = Phi((piehat - d)/sd)
        for _ in range(draws):
            piehat = pie + rng.normal(0, sd)
            d = max(ds, key=lambda d: d*norm.cdf((piehat - d)/sd))
            if pie >= d: rs += np.array([pie - d, d, 0, 0])
        rs /= draws
    else: rs = np.array([0, 6, 0, 0.0])
    # average over four seats; resident seats symmetric by relabelling
    comp = (fl[0] + 3*rs[0])/4
    res_i = (fl[1:].mean()*1.0 + rs[1] + 2*rs[2])/4  # each resident: fleet seat gain (avg) + own seat demand + two others' seats (0)
    return comp, res_i
for sf, sN in ((0,0), (1,1), (0.3,1), (0.1,1), (1,0.3), (0.3,0.3)):
    c, r = cell(sf, sN, draws=4000)
    print(f"sf={sf} sN={sN}: fleet {c:.2f}, each resident {r:.2f}  (run10 reported: 1:1@1 1.48/1.05; 10:1@.3:1 2.04/1.04; 100:1@.1:1 2.35/0.97; 1:10@1:.3 1.08/1.37)")
