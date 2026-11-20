import json
import sys

o = json.load(open(sys.argv[1]))


def f(x):
    return f"{x[0]:.2f}±{x[1]:.2f}"


for key in ("off", "on"):
    d = o[key]
    print(f"\n=== insulation {key} ===  full-info {f(d['full_info'])}")
    for k, v in d.items():
        if k == "full_info":
            continue
        line = f"{k:28s} total {f(v['total'])}  comp {f(v['company'])}  hh {f(v['households'])}  each " + " ".join(f(e) for e in v["each"])
        if "p_neg_avg" in v:
            line += f"  Pneg avg {f(v['p_neg_avg'])} each " + " ".join(f(e) for e in v["p_neg_each"]) + f" ties {v['tie_frac']:.3f}"
        print(line)
print("\n=== worked ===")
for k, v in o["worked"].items():
    if isinstance(v["total"], list):
        print(f"{k:28s} total {f(v['total'])} comp {f(v['company'])} each " + " ".join(f(e) for e in v["each"]))
    else:
        print(f"{k:28s} total {v['total']:.2f} comp {v['company']:.2f} each " + " ".join(f"{e:.2f}" for e in v["each"]) + f" tie {v['tie']}")
