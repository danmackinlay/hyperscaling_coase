import sys; sys.path.insert(0,".")
import dc
for eps in (0.01,0.1,0.3):
    dc.EPS=eps
    row=[]
    for q in (0,0.5,0.75,0.9,1.0):
        v,x,menu,E=dc.best(q,2,1.5,False)
        row.append(f'q={q}:{dc.sched(x)}/{"".join(menu)} sumR={sum(E[1:]):.2f} C={E[3]:.2f}')
    print(f'eps={eps}: '+' | '.join(row))
