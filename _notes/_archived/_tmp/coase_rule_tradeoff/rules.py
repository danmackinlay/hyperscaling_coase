"""Deal-level outcomes on the noise-schedule instance under four fixed rules.

Instance: _plans/hyperscaling_coase_hard_case_instance.md (four delivery slots,
three households, public exposure, private sensitivity, optional insulation).
Added here: the company's profit is m * P, with the multiplier m private to it.

Rules
  A  tailored offers: the company makes each household a final per-slot offer,
     at a rate per unit of exposure that may differ by household and slot; a slot
     runs only if every exposed household accepts.
  B1 uniform rate, consent kept: one rate per unit of exposure for everyone, set
     from the population distribution; any exposed household may veto a slot.
  B2 uniform rate, no individual consent: the company may run any slot if it pays
     the rate (a liability rule).
  C  lottery: each of the four parties is the offer-maker with probability 1/4.
     A household offer-maker names the company's price per slot and the other
     households' rates, and keeps the remainder.

The dial is sigma, the error of an offer-maker's signal about each household's
sensitivity (inf = population distribution only, 0 = exact).  Its signal about
the company's multiplier has error M_SCALE * sigma.

Usage: uv run python rules.py [n_draws] [prior]      prior in {uniform, lognormal}
"""

import itertools
import json
import sys

import numpy as np

P = np.array([4.0, 5.5, 4.0, 5.0])  # company profit per slot M, D, E, N at m = 1
EXPO = np.array([[0.5, 0, 0.5, 1], [1, 1, 0.5, 0.5], [0.5, 0.5, 1, 2]])  # Alice, Bob, Carol
INSTANCE_S = np.array([1.0, 1.0, 2.0])
INS_COST = 2.0
SCHEDS = np.array(list(itertools.product([0, 1], repeat=4)), float)  # 16 x 4
INSUL = np.array(list(itertools.product([0, 1], repeat=3)), float)  # 8 x 3
QS = np.concatenate([np.arange(0.05, 0.951, 0.05), [0.975, 0.99, 0.995, 1.0]])
SIGMAS = [np.inf, 1.0, 0.3, 0.1, 0.03, 0.0]
M_GRID = np.linspace(0.6, 1.4, 801)
M_W = np.ones_like(M_GRID) / len(M_GRID)
M_SCALE = 0.4  # the multiplier's range is 0.4 of the sensitivity's
TOL = 1e-9


def make_prior(kind):
    if kind == "uniform":
        grid = np.linspace(0.5, 2.5, 2001)
        w = np.ones_like(grid)
    else:  # lognormal, median 1.3, log-sd 0.4, truncated
        grid = np.linspace(0.3, 4.0, 3701)
        w = np.exp(-0.5 * ((np.log(grid) - np.log(1.3)) / 0.4) ** 2) / grid
    return grid, w / w.sum()


def posterior(grid, w, signal, sigma):
    if np.isinf(sigma):
        return w
    post = w * np.exp(-0.5 * ((signal - grid) / sigma) ** 2)
    return post / post.sum()


def household_cands(grid, w, s_true, signal, sigma):
    """Rates worth offering one household, with the probability each is accepted."""
    if sigma == 0:
        return np.array([s_true]), np.array([1.0])
    cdf = np.cumsum(posterior(grid, w, signal, sigma))
    idx = np.unique(np.minimum(np.searchsorted(cdf, QS - 1e-12), len(grid) - 1))
    return grid[idx], np.minimum(cdf[idx], 1.0)


def company_cands(m_true, signal, sigma):
    """Prices (as a multiple d of P) worth demanding of the company; it accepts if m >= d."""
    if sigma == 0:
        return np.array([m_true]), np.array([1.0])
    post = posterior(M_GRID, M_W, signal, sigma)
    surv = 1 - np.cumsum(post) + post  # P(m >= grid value)
    idx = np.unique([np.nonzero(surv >= q - 1e-12)[0].max() for q in QS])
    return M_GRID[idx], np.minimum(surv[idx], 1.0)


def best_offers(cc, hc, insul_options):
    """The offer-maker's profit-maximising insulation set and per-slot terms.

    cc = (d values, accept prob) for the company; hc[i] likewise for household i.
    A party that is itself the offer-maker has one candidate, its true value.
    Returns (z, d[4], rates[4,3], offered[4]).
    """
    best = (-np.inf, None, None, None, None)
    for z in insul_options:
        total = -INS_COST * z.sum()
        ds = np.zeros(4)
        rates = np.zeros((4, 3))
        offered = np.zeros(4, bool)
        for t in range(4):
            a = EXPO[:, t] * (1 - z / 2)
            rs, gs = [], []
            for i in range(3):
                if a[i] == 0:
                    rs.append(np.array([0.0]))
                    gs.append(np.array([1.0]))
                else:
                    rs.append(hc[i][0])
                    gs.append(hc[i][1])
            margin = (
                P[t] * cc[0][:, None, None, None]
                - a[0] * rs[0][None, :, None, None]
                - a[1] * rs[1][None, None, :, None]
                - a[2] * rs[2][None, None, None, :]
            )
            prob = (
                cc[1][:, None, None, None]
                * gs[0][None, :, None, None]
                * gs[1][None, None, :, None]
                * gs[2][None, None, None, :]
            )
            val = prob * margin
            k = np.unravel_index(val.argmax(), val.shape)
            if val[k] > 1e-12:
                total += val[k]
                offered[t] = True
                ds[t] = cc[0][k[0]]
                rates[t] = [rs[0][k[1]], rs[1][k[2]], rs[2][k[3]]]
        if total > best[0] + 1e-12:
            best = (total, z, ds, rates, offered)
    return best[1:]


def realise(s, m, z, ds, rates, offered, proposer):
    """Gains (company, Alice, Bob, Carol) over no deal, given the true values."""
    g = np.zeros(4)
    g[proposer] -= INS_COST * z.sum()  # insulation is bought before the answers come in
    for t in range(4):
        if not offered[t]:
            continue
        a = EXPO[:, t] * (1 - z / 2)
        if m >= ds[t] - TOL and np.all((a == 0) | (s <= rates[t] + TOL)):
            g[0] += (m - ds[t]) * P[t]
            g[1:] += (rates[t] - s) * a
            g[proposer] += ds[t] * P[t] - (rates[t] * a).sum()
    return g


def offer_rule(grid, w, s_draws, m_draws, eps, sigma, proposer, insul_options):
    """Per-draw gains when `proposer` (0 company, 1-3 household) makes the offers."""
    out = np.zeros((len(s_draws), 4))
    sg = 0.0 if np.isinf(sigma) else sigma
    for n, (s, m) in enumerate(zip(s_draws, m_draws)):
        if proposer == 0:
            cc = (np.array([m]), np.array([1.0]))
        else:
            cc = company_cands(m, m + M_SCALE * sg * eps[n, 3], M_SCALE * sigma)
        hc = []
        for i in range(3):
            if proposer == i + 1:
                hc.append((np.array([s[i]]), np.array([1.0])))
            else:
                hc.append(household_cands(grid, w, s[i], s[i] + sg * eps[n, i], sigma))
        out[n] = realise(s, m, *best_offers(cc, hc, insul_options), proposer)
    return out


def options(insul_options):
    rows = []
    for z in insul_options:
        a = EXPO * (1 - z[:, None] / 2)
        for x in SCHEDS:
            rows.append((x, a @ x, INS_COST * z.sum()))
    xs = np.array([r[0] for r in rows])
    expo = np.array([r[1] for r in rows])  # options x 3
    cost = np.array([r[2] for r in rows])
    return xs, expo, cost


def first_best(s_draws, m_draws, insul_options):
    xs, expo, cost = options(insul_options)
    val = m_draws[:, None] * (xs @ P)[None] - s_draws @ expo.T - cost[None]
    return val.max(1)


def uniform_rule(s_draws, m_draws, r, consent, insul_options):
    """Per-draw gains under one posted rate r per unit of exposure."""
    xs, expo, cost = options(insul_options)
    profit = m_draws[:, None] * (xs @ P)[None] - r * expo.sum(1)[None] - cost[None]
    score = profit + 1e-9 * xs.sum(1)[None]  # an indifferent company runs the slot
    if consent:
        veto = s_draws > r + TOL  # household i vetoes every slot it is exposed to
        blocked = (veto[:, :, None] & (EXPO[None] > 0)).any(1)  # n x 4
        allowed = ~((xs[None] > 0) & blocked[:, None, :]).any(2)  # n x options
        score = np.where(allowed, score, -np.inf)
    k = score.argmax(1)
    g = np.zeros((len(s_draws), 4))
    g[:, 0] = profit[np.arange(len(k)), k]
    g[:, 1:] = (r - s_draws) * expo[k]
    return g


def summarise(g):
    h = g[:, 1:]
    worse = h < -1e-9
    return {
        "total": float(g.sum(1).mean()),
        "total_se": float(g.sum(1).std() / np.sqrt(len(g))),
        "company": float(g[:, 0].mean()),
        "households": float(h.sum(1).mean()),
        "alice": float(h[:, 0].mean()),
        "bob": float(h[:, 1].mean()),
        "carol": float(h[:, 2].mean()),
        "p_household_worse_off": float(worse.mean()),
        "mean_loss_if_worse_off": float(h[worse].mean()) if worse.any() else 0.0,
    }


def run(n_draws, prior_kind, seed=0):
    rng = np.random.default_rng(seed)
    grid, w = make_prior(prior_kind)
    pop_s = grid[rng.choice(len(grid), size=(n_draws, 3), p=w)]
    pop_m = M_GRID[rng.choice(len(M_GRID), size=n_draws, p=M_W)]
    inst_s = np.tile(INSTANCE_S, (n_draws, 1))
    inst_m = np.ones(n_draws)
    eps = rng.standard_normal((4, n_draws, 4))  # one signal set per possible offer-maker
    res = {"prior": prior_kind, "n_draws": n_draws}
    for world, s_draws, m_draws in [("population", pop_s, pop_m), ("instance", inst_s, inst_m)]:
        for search, zopts in [("schedule_only", INSUL[:1]), ("with_insulation", INSUL)]:
            key = f"{world}/{search}"
            r = res[key] = {}
            r["first_best"] = float(first_best(s_draws, m_draws, zopts).mean())
            seat = {}
            for sigma in SIGMAS:
                for prop in range(4):
                    seat[(sigma, prop)] = offer_rule(grid, w, s_draws, m_draws, eps[prop], sigma, prop, zopts)
                r[f"A sigma={sigma}"] = summarise(seat[(sigma, 0)])
                # the mirror of A: one of the households always holds the seat
                r[f"household seat sigma={sigma}"] = summarise(sum(seat[(sigma, j)] for j in (1, 2, 3)) / 3)
            for sc in SIGMAS:
                for sh in SIGMAS:
                    g = seat[(sc, 0)] / 4 + sum(seat[(sh, j)] for j in (1, 2, 3)) / 4
                    r[f"C company={sc} households={sh}"] = summarise(g)
            for consent, name in [(True, "B1"), (False, "B2")]:
                for rate in np.round(np.arange(0.5, 4.001, 0.05), 2):
                    r[f"{name} r={rate}"] = summarise(uniform_rule(s_draws, m_draws, rate, consent, zopts))
            print("done", key, flush=True)
    return res


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    kind = sys.argv[2] if len(sys.argv) > 2 else "uniform"
    out = run(n, kind)
    with open(f"results_{kind}.json", "w") as f:
        json.dump(out, f, indent=1)
