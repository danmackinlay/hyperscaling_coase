import itertools, numpy as np
p=np.array([4,5.5,4,5.0]); E=np.array([[0.5,0,0.5,1],[1,1,0.5,0.5],[0.5,0.5,1,2]]); s=np.array([1,1,2.0])
def harms(x): return s*(E@x)
X=[np.array(b) for b in itertools.product([0,1],repeat=4)]
pact_pay=1.5  # pact: MDE, each party 1.5
# Fleet's one-period gain from breaking the pact with two consents, net of the bribe that makes the two bribed residents
# whole for THAT period only (forgiving continuation): bribe_i = h_i(x) + 1.5
best=None
for x in X:
    h=harms(x)
    for pair in itertools.combinations(range(3),2):
        bribe=sum(h[i]+pact_pay for i in pair)
        net=p@x-bribe
        if best is None or net>best[0]: best=(net,x,pair,bribe,h)
net,x,pair,bribe,h=best
print(f"fleet's best break (one period, forgiving): schedule {x}, bribe residents {pair}, bribe total {bribe}, fleet nets {net:.2f} vs pact 1.5 -> one-shot pact breaks")
excluded=[i for i in range(3) if i not in pair][0]
print(f"excluded resident {excluded} harmed {h[excluded]} unpaid")
# Grim boycott: after any sale, all three refuse forever (fleet 0, residents 0). SPE at k=2 since no single resident can change the outcome.
# Resident i accepting: b_i - h_i(x) now, 0 forever, vs 1.5/(1-d). Needs b_i >= h_i + 1.5/(1-d).
# Fleet: profit - sum b_i now then 0 forever vs 1.5/(1-d).
for d in (0.5,0.8,0.95):
    bribes=sum(h[i]+pact_pay/(1-d) for i in pair)
    dev=p@x-bribes; stay=pact_pay/(1-d)
    print(f"delta={d}: grim boycott: fleet deviation {dev:.2f} vs staying {stay:.2f} -> {'pact holds' if dev<=stay else 'pact breaks'}")
# threshold: 18.5 - 5 - 3/(1-d) <= 1.5/(1-d) -> 13.5 <= 4.5/(1-d) -> d >= 2/3
print("threshold delta* = 1 - 4.5/13.5 =",1-4.5/13.5)
# T-period boycott then return to pact: A=(1-d^(T+1))/(1-d); holds iff 4.5*A >= 13.5 i.e. A>=3
for d in (0.5,0.8,0.95):
    found=None
    for T in range(0,200):
        A=(1-d**(T+1))/(1-d)
        if 4.5*A>=13.5: found=T; break
    print(f"delta={d}: minimum boycott length T = {found} (A_max={1/(1-d):.2f})")
# Grim collapse to divide-and-conquer instead (the bribed pair not punished by boycott, pact simply dies): fleet gains 17/(1-d) per period stream
for d in (0.5,0.8,0.95):
    need=sum(h[i]+ (pact_pay+h[i]*d/(1-d))/1 for i in pair)  # b_i >= h_i + 1.5/(1-d) + h_i d/(1-d) ... compute directly
    need=sum(h[i] + pact_pay/(1-d) + h[i]*d/(1-d) for i in pair)
    avail=(p@x-1.5)/(1-d)  # fleet's gain stream from collapse (tokens thereafter)
    print(f"delta={d}: collapse-to-divide-and-conquer: bribes needed {need:.1f}, fleet's gain from collapse {avail:.1f} -> breaks")
