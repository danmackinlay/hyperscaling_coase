"""Render the sampling round's results.json per run for reading."""
import json, sys
from pathlib import Path
r = json.load(open(Path(__file__).with_name("results.json")))
out = [f"# Sampling round {r['date']}: {len(r['runs'])} runs returned; missing {r.get('missing')}\n"]
for x in r["runs"]:
    out.append(f"\n\n# {x['id']} (pool {x['pool']}, {x['model']})\n\nSTART: {x['dealt']}\n")
    for k in ["entailment", "story", "mechanism", "best_reply", "dial", "sign_on_loser", "who_pays", "grounding", "replication", "expressible_on_base", "robustness_check", "sequel_not_finding", "delta", "proposed_open_rows"]:
        if k in x: out.append(f"**{k}:** {x[k]}\n")
    out.append("**sources:**")
    for s in x.get("sources", []): out.append(f"- {json.dumps(s, ensure_ascii=False)}")
Path(__file__).with_name("results_readable.md").write_text("\n".join(out))
print("rendered", len(r["runs"]), "runs")
