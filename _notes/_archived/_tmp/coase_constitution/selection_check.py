"""Scratch check for the forecasting-thesis test (safe to delete).

One household, K candidate night slots. True harm h_k; the household's own
estimate c_k = h_k + eps_k; the company's estimate of the truth m_k = h_k + delta_k;
the company's prediction of the household's answer a_k = c_k + nu_k.
Rule: the household is paid its honest report c_k for the one slot that is proposed
(a truthful rule: the payment does not reward misreporting). We measure the
household's mean net position, payment minus true harm, per proposed slot.
"""

import numpy as np

rng = np.random.default_rng(0)
N, K = 200_000, 10
mu, s_h, s_c = 5.0, 1.0, 1.0  # harm spread and the household's own error


def run(s_truth, s_answer):
    h = rng.normal(mu, s_h, (N, K))
    c = h + rng.normal(0, s_c, (N, K))
    m = h + rng.normal(0, s_truth, (N, K))  # company's estimate of true harm
    a = c + rng.normal(0, s_answer, (N, K))  # company's prediction of the answer
    rows = np.arange(N)
    out = {}
    out["random slot"] = (c[:, 0] - h[:, 0]).mean()
    k = m.argmin(1)
    out["company picks on truth"] = (c[rows, k] - h[rows, k]).mean()
    k = a.argmin(1)
    out["company picks on predicted answer"] = (c[rows, k] - h[rows, k]).mean()
    # household's agent corrects: it knows the slot was picked for a low predicted answer
    shade = -(c[rows, k] - h[rows, k]).mean()
    out["  same, household corrects by"] = shade
    return out


for label, s_truth, s_answer in [
    ("company knows truth well, answer badly", 0.2, 3.0),
    ("company knows truth badly, answer well", 3.0, 0.2),
    ("company knows both well", 0.2, 0.2),
    ("company knows both badly", 3.0, 3.0),
]:
    print(label)
    for name, v in run(s_truth, s_answer).items():
        print(f"   {name:36s} {v:+.2f}")
