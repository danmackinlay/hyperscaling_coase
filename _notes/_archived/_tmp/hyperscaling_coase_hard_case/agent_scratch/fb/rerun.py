import numpy as np, tioli
tioli.RNG=np.random.default_rng(99)
for s in (1.0,0.3,0.1,0.1/np.sqrt(10)):
    print("T-f",round(s,4),tioli.fmt(tioli.run_tf(s,n=8000)))
for s in (1.0,0.3,0.1,0.1/np.sqrt(10)):
    print("T-b",round(s,4),tioli.fmt(tioli.run_tb(s,n=8000)))
