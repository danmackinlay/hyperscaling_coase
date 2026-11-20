"""Print the repeated-dealing tables.  Usage: uv run python repeat_tables.py KIND [prior] [delta]"""
import json, sys
kind = sys.argv[1]
prior = sys.argv[2] if len(sys.argv) > 2 else "uniform"
delta = sys.argv[3] if len(sys.argv) > 3 else "1.0"
for s in ("inf", "1.0", "0.3", "0.1", "0.03"):
    try:
        r = json.load(open(f"repeat_{kind}_{prior}_sigma{s}_delta{delta}.json"))
    except FileNotFoundError:
        continue
    print(f"error {s}: best possible {r['first_best']:.2f}, draws {r['n_draws']}, cutoff offers passing check {r['cut_offers_valid_share']:.2f}, {r['seconds']:.0f}s")
    for k in ("forget", "myopic", "strategic", "unchecked"):
        d = r[k]
        extra = "" if k == "forget" else f"   cut/all/none {d['share_cut']:.2f}/{d['share_all']:.2f}/{d['share_none']:.2f} slots r1 {d['slots_named_round1']:.2f} hiding {d['hiding_rate']:.3f}"
        print(f"  {k:10s} total {d['total']:.2f} company {d['company']:.2f} households {d['households']:.2f}  (A {d['alice']:.2f} B {d['bob']:.2f} C {d['carol']:.2f}){extra}")
    for k in ("strategic-myopic", "strategic-forget", "myopic-forget", "unchecked-forget"):
        d = r[k]
        print(f"  {k:18s} households {d['households']:+.2f} (se {d['households_se']:.2f})  total {d['total']:+.2f} (se {d['total_se']:.2f})")
