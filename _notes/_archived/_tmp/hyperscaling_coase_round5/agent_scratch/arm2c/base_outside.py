"""Replication on the base instance via its outside-option switch: reroute at 3 per slot.
Two readings: (a) all-or-nothing: principal either contracts the efficient schedule or
reroutes its profit-max schedule; (b) slot by slot: each slot is consented or rerouted.
Residents' club agents demand d each (committed, q=1). Report whether a deal exists,
the pie over the outside option, the max the residents can hold, and positions."""
import numpy as np, itertools
from model import E,P,SCHEDS,S_BASE,efficient
s=S_BASE; harm_t = s@E  # total harm per slot
print("harm per slot",harm_t,"profit per slot",P,"reroute cost 3")
# (a) all-or-nothing
oo = max(P@x-3*x.sum() for x in SCHEDS); xo=max(SCHEDS,key=lambda x:P@x-3*x.sum())
pie,x,h,prof=efficient(s)
print(f"(a) outside option (reroute best schedule {xo}) = {oo}; efficient-deal pie over no deal = {pie}; pie over outside option = {pie-oo}")
for d in [0,0.375,0.5,1.5]:
    pay=h.sum()+3*d; prin=prof-pay
    print(f"   club demand d={d}: deal pays {pay}, principal {prin:.3f} vs reroute {oo} -> {'deal' if prin>=oo else 'REROUTE, residents 0, noise exported'}")
# (b) slot by slot
print("(b) slot by slot: surplus of consent over reroute per slot =",3-harm_t)
cons=[t for t in range(4) if 3-harm_t[t]>0]
pie_b=sum(3-harm_t[t] for t in cons)
print(f"   consent slots {cons}, pie over outside option {pie_b}, fair share each {pie_b/4:.3f} (base fair share 1.5)")
for d in [0.375,1.5]:
    ok=[t for t in cons if 3-harm_t[t]>=3*d]
    print(f"   club demand d={d} per resident per slot-bundle: principal consents only where slot surplus >= 3d: {ok}")
