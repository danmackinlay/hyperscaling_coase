import numpy as np
from haggle import Arm
grid=np.linspace(-1.5,3,451)
for (sf,sN) in [(1,1),(0.3,0.3),(0.1,0.1),(0.0316,0.1),(0.1,0.0316)]:
    arm=Arm(sf,sN,closure="sd",seed=7); n=20000
    sh,h3,ph=arm.draw_signals(n); gf0,gN0s=arm.L0(sh,h3,ph); gN0=np.repeat(gN0s[:,None],3,1)
    mf,mN=0.0,0.0
    for it in range(200):
        vf=[arm.payoff(gf0-m,gN0-mN)[0][:,0].mean() for m in grid]; bf=grid[int(np.argmax(vf))]
        vr=[arm.payoff(gf0-mf,np.column_stack([gN0[:,0]-m,gN0[:,1]-mN,gN0[:,2]-mN]))[0][:,1].mean() for m in grid]; br=grid[int(np.argmax(vr))]
        if abs(bf-mf)<0.011 and abs(br-mN)<0.011: break
        mf,mN=0.7*mf+0.3*bf,0.7*mN+0.3*br
    g,ok=arm.payoff(gf0-mf,gN0-mN); E=g.mean(0)
    print(f"sf {sf} sN {sN}: it {it} margins f {mf:.3f} r {mN:.3f} (BR {bf:.3f},{br:.3f}) deal {ok.mean():.3f} E {np.round(E,3)} NP {np.prod(E):.3f}")
