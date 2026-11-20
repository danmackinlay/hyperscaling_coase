"""Town model: one slot, n households each with a veto, private harms in [1,2].

Company proposes per-household take-it-or-leave-it payments (the proposer seat).
Company's estimation dial: signal shat_i = s_i + tau*z, tau = sigma/sqrt(c_f), sigma=1.
m = what the company earns per household from the deal over its no-deal point:
  wide margin, no detour: m = v = 2.5; thin margin, detour at cost r=1.8: m = r = 1.8.
Households accept iff payment >= own harm. Deal needs all n.
"""
import sys
import numpy as np

rng_master = np.random.default_rng(20261023)


def prior_weights(grid, shape):
    u = (grid - 1.0)
    if shape == "uniform":
        w = np.ones_like(grid)
    elif shape == "beta22":
        w = u * (1 - u)
    elif shape == "beta55":  # Beta(0.5,0.5), U-shaped
        w = 1.0 / np.sqrt(np.clip(u * (1 - u), 1e-6, None))
    w = w / w.sum()
    return w


def sample_prior(rng, n, shape):
    if shape == "uniform":
        return 1 + rng.random(n)
    if shape == "beta22":
        return 1 + rng.beta(2, 2, n)
    if shape == "beta55":
        return 1 + rng.beta(0.5, 0.5, n)


def company_offers(shat, tau, n, m, grid, w, noise):
    """Return offers t_i (on grid) maximising (n m - sum t) prod F_i(t_i)."""
    G = len(grid)
    if tau is None:  # no information: posterior = prior
        post = np.tile(w, (n, 1))
    elif tau == 0:
        return None  # handled by caller (exact)
    else:
        d = (grid[None, :] - shat[:, None]) / tau
        if noise == "gauss":
            like = np.exp(-0.5 * d ** 2)
        else:  # laplace with same sd
            like = np.exp(-np.sqrt(2) * np.abs(d))
        post = like * w[None, :]
        post /= post.sum(axis=1, keepdims=True)
    F = np.cumsum(post, axis=1)  # P(s_i <= grid[k])
    F = np.clip(F, 1e-300, 1.0)
    logF = np.log(F)
    t_idx = np.full(n, G - 1)
    for _ in range(200):
        tsum = grid[t_idx].sum()
        A = n * m - tsum + grid[t_idx]  # value available to household i's offer
        # maximise log(A_i - t) + logF_i(t)
        val = A[:, None] - grid[None, :]
        obj = np.where(val > 0, np.log(np.clip(val, 1e-300, None)) + logF, -np.inf)
        new = obj.argmax(axis=1)
        if np.array_equal(new, t_idx):
            break
        t_idx = new
    t = grid[t_idx]
    exp_profit = (n * m - t.sum()) * np.exp(logF[np.arange(n), t_idx].sum())
    if exp_profit <= 0:
        return np.zeros(n) * np.nan
    return t


def run(n, m, tau, shape="uniform", noise="gauss", G=401, draws=400, seed=1):
    rng = np.random.default_rng(seed)
    grid = np.linspace(1, 2, G)
    w = prior_weights(grid, shape)
    co, res, pie, maxpie, floor, deals = [], [], [], [], [], []
    for _ in range(draws):
        s = sample_prior(rng, n, shape)
        mp = max(n * m - s.sum(), 0.0)
        if tau == 0:
            t = s.copy()
        else:
            if tau is None:
                shat = None
            else:
                z = rng.standard_normal(n) if noise == "gauss" else rng.laplace(0, 1 / np.sqrt(2), n)
                shat = s + tau * z
            t = company_offers(shat, tau, n, m, grid, w, noise)
        if np.any(np.isnan(t)) or np.any(t < s - 1e-12):
            g = np.zeros(n); gc = 0.0; d = 0
        else:
            g = t - s; gc = n * m - t.sum(); d = 1
        co.append(gc); res.append(g.mean()); pie.append(gc + g.sum())
        maxpie.append(mp); floor.append(g.min()); deals.append(d)
    co, res, pie, maxpie, floor = map(np.array, (co, res, pie, maxpie, floor))
    Eco, Eres = co.mean(), res.mean()
    # criterion: geometric mean of expected gains over n+1 parties, / (E maxpie/(n+1))
    if Eco > 0 and Eres > 0:
        gm = np.exp((n * np.log(Eres) + np.log(Eco)) / (n + 1))
    else:
        gm = 0.0
    crit = gm / (maxpie.mean() / (n + 1))
    return dict(n=n, m=m, tau=tau, deal=np.mean(deals), eff=pie.mean() / maxpie.mean(),
                res_share=(n * Eres) / max(pie.mean(), 1e-12), Eres=Eres, Eco=Eco,
                crit=crit, floor=floor.mean())


def club(n, m, shape="uniform", draws=400, seed=1):
    """Residents' club posts one price per household, the most anyone could mind (2)."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(draws):
        s = sample_prior(rng, n, shape)
        mp = max(n * m - s.sum(), 0)
        if m >= 2:
            g = 2 - s; gc = n * (m - 2)
        else:
            g = np.zeros(n); gc = 0
        out.append((gc, g.mean(), gc + g.sum(), mp, g.min()))
    a = np.array(out)
    Eco, Eres = a[:, 0].mean(), a[:, 1].mean()
    gm = np.exp((n * np.log(Eres) + np.log(Eco)) / (n + 1)) if Eco > 0 and Eres > 0 else 0.0
    return dict(deal=float(m >= 2), eff=a[:, 2].mean() / a[:, 3].mean(), Eres=Eres, Eco=Eco,
                crit=gm / (a[:, 3].mean() / (n + 1)), floor=a[:, 4].mean())


def court(n, m, tau_c=0.3, shape="uniform", draws=400, seed=1):
    """Liability rule: council assesses each harm with error tau_c; company runs iff n m > sum assessed."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(draws):
        s = sample_prior(rng, n, shape)
        a = s + tau_c * rng.standard_normal(n)
        mp = max(n * m - s.sum(), 0)
        if n * m > a.sum():
            g = a - s; gc = n * m - a.sum()
        else:
            g = np.zeros(n); gc = 0
        out.append((gc, g.mean(), gc + g.sum(), mp, g.min(), (g < 0).mean()))
    a = np.array(out)
    return dict(eff=a[:, 2].mean() / a[:, 3].mean(), Eres=a[:, 1].mean(), Eco=a[:, 0].mean(),
                floor=a[:, 4].mean(), frac_below=a[:, 5].mean())


if __name__ == "__main__":
    shape = sys.argv[1] if len(sys.argv) > 1 else "uniform"
    noise = sys.argv[2] if len(sys.argv) > 2 else "gauss"
    G = int(sys.argv[3]) if len(sys.argv) > 3 else 401
    taus = [None, 1.0, 0.3, 0.1, 0.03, 0]
    print(f"shape={shape} noise={noise} G={G}")
    for m, lab in [(2.5, "wide, no detour (v=2.5)"), (1.8, "thin, detour r=1.8")]:
        print(f"\n== margin {lab}")
        print("   n  tau    deal   eff  resShare  Eres/hh   Eco      crit   floor")
        for n in [3, 30, 300]:
            draws = 400 if n < 300 else 150
            for tau in taus:
                r = run(n, m, tau, shape, noise, G, draws)
                print(f"{n:4d} {str(tau):5s} {r['deal']:6.2f} {r['eff']:5.2f} {r['res_share']:8.2f}"
                      f" {r['Eres']:8.3f} {r['Eco']:8.2f} {r['crit']:7.3f} {r['floor']:7.3f}")
            c = club(n, m, shape)
            k = court(n, m, 0.3, shape)
            print(f"{n:4d} club  {c['deal']:6.2f} {c['eff']:5.2f}          {c['Eres']:8.3f} {c['Eco']:8.2f} {c['crit']:7.3f} {c['floor']:7.3f}")
            print(f"{n:4d} court        {k['eff']:5.2f}          {k['Eres']:8.3f} {k['Eco']:8.2f}  floor {k['floor']:.3f} below0 {k['frac_below']:.2f}")
