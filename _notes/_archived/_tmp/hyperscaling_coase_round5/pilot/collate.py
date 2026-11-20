"""Forty-point table for the return: literal scoring reading (primary) with the counterfactual
reading's principal take beside it. Seeds: design 1; runs [1, r], r = 0..n-1."""
import json, sys
sys.path.insert(0, '.')
from pilot import lhs
pts = lhs()
A = {int(s['label'].split()[0][2:]): s for s in json.load(open('results/lhs_own_offer_0_40_own.json'))['out']}
B = {int(s['label'].split()[0][2:]): s for s in json.load(open('results/lhs_counterfactual_0_40_own.json'))['out']}
print("| pt | eta | step | /s | H | T | win | margins | fb | play | dyn | runs | P (se) | R1 | R2 | R3 | deal | floor | P, cf reading | cpu s/pt |")
print("|" + "|".join(["---"] * 20) + "|")
for i in range(40):
    p, a, b = pts[i], A[i], B[i]
    flag = "*" if p["play"] == "expected" and p["feedback"] == "bandit" else ""
    print(f"| {i}{flag} | {p['eta']} | {p['step']:g} | {p['scale']:g} | {p['H']} | {p['T']} | {p['window']} | {p['margins']} | {p['feedback']} | {p['play']} | {p['dyn']} | {a['n_runs']} | "
          f"{a['P']:.2f} ({a['P_se']:.2f}) | {a['R1']:.2f} | {a['R2']:.2f} | {a['R3']:.2f} | {a['deal']:.2f} | {a['floor']:.2f} | {b['P']:.2f} | {a['cpu_sec']:.0f} |")
