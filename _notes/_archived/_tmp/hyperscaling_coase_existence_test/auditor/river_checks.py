"""Auditor re-runs on the river: harms (2,3,9), pi in {10,20}, k of 3."""
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize_scalar

H = np.array([2.0, 3.0, 9.0]); PI = 20.0; PIE = PI - H.sum()

def factory_tioli(sig):
    """Factory offers h_i + e_i + m to each resident (e_i ~ N(0, sig_i^2)); resident accepts iff offer >= h_i.
    Factory picks one margin m to maximise E[(PIE - sum(e_i+m)) * 1{all accept}]."""
    sig = np.broadcast_to(np.asarray(sig, float), (3,))
    def stats(m):
        z = m / sig
        P = norm.cdf(z)                      # P(accept_i)
        cond = sig * norm.pdf(z) / P        # E[e_i | accept_i]
        pdeal = P.prod()
        gain_i = m + cond                    # resident i's net gain given deal
        f = pdeal * (PIE - gain_i.sum())
        return f, pdeal, gain_i
    res = minimize_scalar(lambda m: -stats(m)[0], bounds=(-5, 10), method="bounded")
    f, pdeal, gain_i = stats(res.x)
    return dict(m=res.x, pdeal=pdeal, factory_E=f, S_given_deal=gain_i.sum() / PIE,
                res_E=pdeal * gain_i, res_E_total=pdeal * gain_i.sum(), total_E=pdeal * PIE)

def bloc_tioli(sig):
    """Residents as one bloc demand pihat - m, pihat = pi + e; factory accepts iff demand <= pi."""
    def stats(m):
        z = m / sig
        P = norm.cdf(z)
        bloc = P * (PIE - m) - sig * norm.pdf(z)   # E[(PIE + e - m) 1{e<=m}]
        return bloc, P
    res = minimize_scalar(lambda m: -stats(m)[0], bounds=(-5, 15), method="bounded")
    bloc, P = stats(res.x)
    fac = P * PIE - bloc
    return dict(m=res.x, pdeal=P, bloc_E=bloc, factory_E=fac, factory_share_given_deal=fac / (P * PIE))

print("Row 1: factory TIOLI, equal noise sigma per resident")
for s in [1.5, 1.0, 0.5, 0.25, 0.1, 0.01]:
    r = factory_tioli(s)
    print(f" sig={s:5}: m={r['m']:.3f} deal={r['pdeal']:.4f} S|deal={r['S_given_deal']:.3f} "
          f"res_E_total={r['res_E_total']:.3f} each={np.round(r['res_E'],3)} factory_E={r['factory_E']:.3f} total_E={r['total_E']:.3f}")
print("Row 1 variant: noise proportional to harm, sig_i = c*h_i/h_mean (same mean sigma)")
for s in [1.5, 0.5, 0.1]:
    r = factory_tioli(s * H / H.mean())
    print(f" mean sig={s:4}: deal={r['pdeal']:.4f} res_E each={np.round(r['res_E'],3)} factory_E={r['factory_E']:.3f}")
print("Row 1 variant: harm 9 has an unmeasurable part sd 1.0 that compute cannot reduce")
for s in [1.5, 0.5, 0.1, 0.01]:
    sig = np.array([s, s, np.hypot(s, 1.0)])
    r = factory_tioli(sig)
    print(f" sig={s:4}: deal={r['pdeal']:.4f} res_E each={np.round(r['res_E'],3)} factory_E={r['factory_E']:.3f}")

print("\nRow 2: residents' bloc TIOLI, noise sigma on pi")
for s in [1.5, 1.0, 0.5, 0.1, 0.01]:
    r = bloc_tioli(s)
    print(f" sig={s:5}: deal={r['pdeal']:.4f} bloc_E={r['bloc_E']:.3f} factory_E={r['factory_E']:.3f} fac share|deal={r['factory_share_given_deal']:.3f}")
print(" internal splits of a bloc take of 6: equal-gain", [2, 2, 2], " harm-proportional", np.round(6 * H / H.sum(), 3))

print("\nRow 5: Ellingsen-Miettinen on the river, factory v. residents' bloc, fallback split b")
for q in [0.5, 0.9, 0.99]:
    for bF in [3.0, 1.5]:
        pc = q * q; f = 6 * q * (1 - q) + (1 - q) ** 2 * bF; r = 6 * q * (1 - q) + (1 - q) ** 2 * (6 - bF)
        print(f" q={q}: P(conflict)={pc:.4f} E[factory]={f:.3f} E[bloc]={r:.3f} (fallback factory {bF})")
print(" n-player naive analogue (4 separate committers, any two incompatible commitments => conflict):")
for q in [0.5, 0.9]:
    p_le1 = (1 - q) ** 4 + 4 * q * (1 - q) ** 3
    print(f"  q={q}: P(>=2 stick)={1 - p_le1:.4f}")

print("\nk=1 and k=2 one-shot divide and conquer (token price -> 0):")
for pi in [10, 20]:
    print(f" pi={pi}: factory {pi}, residents {(-H).tolist()}, total {pi - H.sum()}")
print(" core check k=1 pi=10: pairs need 10-h =", (10 - H).tolist(), "sum", (10 - H).sum(), "vs v(N)=0")

print("\nLiability rule, pi=20: damages = own harm v. uniform average harm")
D = np.full(3, H.mean())
print(" own harm: residents net", [0, 0, 0], "factory", PI - H.sum())
print(" uniform", round(H.mean(), 3), ": residents net", np.round(D - H, 3).tolist(), "factory", PI - D.sum())

print("\nGroup contest (Baik 2008): residents contribute individually, only the highest stake (9) is active")
for V1, label in [(14, "pooled 14"), (9, "Baik 9")]:
    V2 = 10.0; p = V1 / (V1 + V2); e1 = V1 ** 2 * V2 / (V1 + V2) ** 2; e2 = V1 * V2 ** 2 / (V1 + V2) ** 2
    print(f" {label} v 10: P(residents win)={p:.3f} efforts residents={e1:.2f} factory={e2:.2f}")

print("\nRepeated factory-TIOLI at k=3, residents boycott forever after a deviation:")
for g in [0.5, 1.0, 1.5, 1.9]:
    print(f" premium g={g} each (factory keeps {6 - 3 * g}): need delta >= {g / 2:.3f}")
print("Minmax floor per resident per year by k (others can consent without you):")
for k in [0, 1, 2, 3]:
    print(f" k={k}:", [0.0] * 3 if k == 3 else (-H).tolist())

print("\nYoung-style weighted Nash split of 6 with linear utility, factory sample s_F, residents s_R each:")
for sF, sR in [(1, 1), (3, 1), (10, 1)]:
    w = np.array([sF, sR, sR, sR], float); print(f" s_F={sF}, s_R={sR}: shares", np.round(6 * w / w.sum(), 3).tolist())
