import numpy as np
from haggle import Arm
grid=np.linspace(-1.5,3,451)
for closure in ("sd","nash"):
  for (sf,sN) in [(1,1),(0.316,1),(1,0.316)]:
    arm=Arm(sf,sN,closure=closure,seed=7); n=20000
    sh,h3,ph=arm.draw_signals(n); gf0,gN0s=arm.L0(sh,h3,ph); gN0=np.repeat(gN0s[:,None],3,1)
    def brf(mN): return grid[int(np.argmax([arm.payoff(gf0-m,gN0-mN)[0][:,0].mean() for m in grid]))]
    def brr(mf,mN): return grid[int(np.argmax([arm.payoff(gf0-mf,np.column_stack([gN0[:,0]-m,gN0[:,1]-mN,gN0[:,2]-mN]))[0][:,1].mean() for m in grid]))]
    mf=mN=0.0; tr=[]
    for it in range(25):
        bf=brf(mN); br=brr(mf,mN); tr.append((round(mf,3),round(mN,3),bf,br))
        mf,mN=0.6*mf+0.4*bf,0.6*mN+0.4*br
    print(closure,sf,sN,tr[-3:])
