# Reopening one slot after agreement. Parametric baseline, k=3, complete info after the shock, linear money.
# Agreed: MDE at the symmetric (Nash) split, 1.5 each; per-slot shares (0.375, 0.875, 0.25) each.
# Shock: resident 3's harm from slot E rises by v.  Renegotiation, if opened, reaches the Nash split of whatever is
# reopened with prob 1-phi after one period's delay (factor delta); with prob phi it fails and what was reopened is lost.
# SLOT contracts: R3 may (a) revoke E alone (unilateral, no renegotiation) or (b) reopen E alone.
# BUNDLE: R3's only lever is to revoke the bundle; all of MDE is renegotiated.
import numpy as np
share={'M':0.375,'D':0.875,'E':0.25}; pie=6.0
def outcomes(v,d,phi):
    g=d*(1-phi)
    sq=np.array([1.5,1.5,1.5,1.5-v])
    # slot (a) drop E
    dropE=np.array([1.25,1.25,1.25,1.25])
    # slot (b) renegotiate E: E surplus 1-v (if >0) split 4 ways, expected g*
    eS=max(1-v,0); renE=np.array([1.25+g*eS/4]*4)
    # bundle: renegotiate everything: new pie 6-v if v<1 else 5
    newpie=6-min(v,1.0); renB=np.array([g*newpie/4]*4)
    slot_opts={'status quo':sq,'drop E':dropE,'reopen E':renE}
    sbest=max(slot_opts,key=lambda k: slot_opts[k][3])
    bbest='status quo' if sq[3]>=renB[3] else 'reopen bundle'
    return sbest,slot_opts[sbest],bbest,(sq if bbest=='status quo' else renB)
def thr(d,phi,which):
    vs=np.linspace(0,1.6,160001)
    for v in vs:
        sb,so,bb,bo=outcomes(v,d,phi)
        if which=='slot' and sb!='status quo': return v
        if which=='bundle' and bb!='status quo': return v
for phi in (0,0.81):
  for d in (0.5,0.8,0.95,1.0):
    ts,tb=thr(d,phi,'slot'),thr(d,phi,'bundle')
    print('phi=%.2f delta=%.2f: R3 overrides E once v > %.4f (slot) vs %.4f (bundle); ratio %s; closed forms (1-g)/(4-g)=%.4f, 6(1-g)/(4-g)=%.4f'%(
        phi,d,ts,tb, 'n/a' if ts==0 else round(tb/ts,3),(1-d*(1-phi))/(4-d*(1-phi)),6*(1-d*(1-phi))/(4-d*(1-phi))))
print()
# extra deadweight a resident risks by reopening one slot under the bundle rather than the slot alone, Nash shares:
for t in 'MDE':
    rest=sum(v for k,v in share.items() if k!=t)
    print('reopen %s: slot stake %.3f, rest-of-bundle stake %.3f, ratio whole/slot %.3f; extra cost (1-delta(1-phi))*rest at delta .5/.8/.95, phi 0: %s; phi .81, delta 1: %.3f'%(
        t,share[t],rest,1.5/share[t],[round((1-d)*rest,4) for d in (0.5,0.8,0.95)],0.81*rest))
print()
# window outcomes, v=0.3
for d in (0.5,0.8,0.95,1.0):
    for v in (0.3,0.6):
        sb,so,bb,bo=outcomes(v,d,0)
        pr=lambda o: np.prod(o) if (o>0).all() else float('nan')
        print('v=%.1f delta=%.2f  slot: %-10s %s prod %.3f floor %.3f | bundle: %-13s %s prod %.3f floor %.3f'%(v,d,sb,np.round(so,3),pr(so),so.min(),bb,np.round(bo,3),pr(bo),bo.min()))
print()
# Interaction discovered after a parametric MDE bundle (arbitrary switch revealed ex post): v = 1.5 on E given M
for phi in (0,0.81):
  for d in (0.5,0.8,0.95,1.0):
    g=d*(1-phi); b=np.array([g*1.25]*4)
    print('arb revealed, phi=%.2f delta=%.2f: status quo (1.5;1.5,1.5,0) prod 0; slot drop E (1.25 x4) prod %.3f; bundle reopen %s prod %.4f'%(phi,d,1.25**4,np.round(b,4),np.prod(b)))
print()
# hold-up of a fleet take-it-or-leave-it bundle (6;0,0,0) when consents are revocable and renegotiation is symmetric
for d in (0.5,0.8,0.95,1.0):
    print('fleet TIOLI bundle, revocable consent, delta=%.2f: a resident revokes (0 -> %.3f); fleet 6 -> %.3f; product 0 -> %.3f'%(d,1.5*d,1.5*d,(1.5*d)**4))
