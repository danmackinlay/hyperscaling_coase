"""Print the tables the findings note quotes.  Usage: uv run python tables.py [prior]"""

import json
import sys

kind = sys.argv[1] if len(sys.argv) > 1 else "uniform"
res = json.load(open(f"results_{kind}.json"))
SIG = ["inf", "1.0", "0.3", "0.1", "0.03", "0.0"]
COLS = ["total", "company", "households", "alice", "bob", "carol"]


def row(label, d, extra=""):
    print(f"  {label:38s}" + "".join(f"{d[c]:8.2f}" for c in COLS) + extra)


for key in ["population/schedule_only", "population/with_insulation", "instance/schedule_only", "instance/with_insulation"]:
    d = res[key]
    print(f"\n== {key}   first best {d['first_best']:.2f}   (prior {kind}, n {res['n_draws']})")
    print("  " + " " * 38 + "".join(f"{c:>8s}" for c in COLS))
    for s in SIG:
        row(f"A company offers, error {s}", d[f"A sigma={s}"], f"   se {d[f'A sigma={s}']['total_se']:.3f}")
    for s in SIG:
        row(f"a household offers, error {s}", d[f"household seat sigma={s}"])
    for s in SIG:
        row(f"C lottery, all error {s}", d[f"C company={s} households={s}"])
    for s in SIG:
        row(f"C lottery, company exact, hh {s}", d[f"C company=0.0 households={s}"])
    for s in SIG:
        row(f"C lottery, company {s}, hh inf", d[f"C company={s} households=inf"])
    for name in ["B1", "B2"]:
        rates = sorted(float(k.split("=")[1]) for k in d if k.startswith(name + " r="))
        best_total = max(rates, key=lambda r: d[f"{name} r={r}"]["total"])
        best_hh = max(rates, key=lambda r: d[f"{name} r={r}"]["households"])
        for r in sorted({1.0, 1.5, 1.75, 1.9, 2.0, 2.25, 2.5, 3.0, best_total, best_hh}):
            e = d[f"{name} r={r}"]
            tag = (" <- best total" if r == best_total else "") + (" <- best for households" if r == best_hh else "")
            row(
                f"{name} uniform rate {r}",
                e,
                f"   worse off {e['p_household_worse_off']:.2f} by {e['mean_loss_if_worse_off']:.2f}{tag}",
            )
