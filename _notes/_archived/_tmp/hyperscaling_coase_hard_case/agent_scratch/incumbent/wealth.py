import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import norm
from base import *
from tioli import run_fleet
from bloc import run_bloc
w0=np.array([100,10,10,2.0])
def U(a):  # per-draw money gains -> utility gains, then expectation
    return np.log1p(a[:,:4]/w0).mean(0)
for sig in (1.0,0.316,0.1,0.0316):
    uf=U(run_fleet(sig,400)); ub=U(run_bloc(sig,800))
    print(f'sig={sig}: fleet TIOLI util gains {uf.round(4)} NP {np.prod(uf):.2e} | bloc(equal) util gains {ub.round(4)} NP {np.prod(ub):.2e}')
# bloc demand chosen by resident 3's expected utility vs linear, MDE, equal split of T-7.5, prior on total profit N(13.5, 3 sig^2) (phat=p)
for sig in (1.0,0.316,0.1):
    sd=sig*np.sqrt(3); H=7.5
    lin=minimize_scalar(lambda T:-(T-H)*norm.cdf((13.5-T)/sd),bounds=(H,20),method='bounded').x
    poor=minimize_scalar(lambda T:-(np.log(2+(T-H)/3)-np.log(2))*norm.cdf((13.5-T)/sd),bounds=(H,20),method='bounded').x
    print(f'sig_N={sig}: bloc demand above harms, linear {lin-H:.2f}, as chosen by poor resident 3 (log, w0=2) {poor-H:.2f}')
