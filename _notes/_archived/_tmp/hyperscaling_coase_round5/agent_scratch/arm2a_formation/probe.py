import time, sys
from arm2a import *
n,k,q,c = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
econ = Economy(n,k,q)
t0=time.time()
for tp in range(3):
    for sp in (1,2):
        v,g,sig = econ.proposer_choice(tp,sp,c)
        print("ABC"[tp], "s=",sp, "value=%.3f"%v, "g=",g, "sig=",sig, "|", describe(econ, sig or (0,0,0), g or 0.0))
        if sig:
            for t in range(3):
                print("     type",'ABC'[t], "signer gains s1,s2:", [round(econ.gain_of(sig,g,t,True,s),3) if sig[t] else None for s in (1,2)],
                      "non-signer:", [round(econ.gain_of(sig,g,t,False,s),3) if sig[t]<econ.m else None for s in (1,2)])
print("time", time.time()-t0, "cache", len(econ.cache))
