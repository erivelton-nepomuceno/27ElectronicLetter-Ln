# Numbers quoted in the paper, from logical-chaos.md (main table) and ec_artifact data/rows.json.
# Usage (from code/R0): python analysis/paper_stats.py
import json, re, math
import numpy as np

rows = json.load(open('ec_artifact_src/ec_artifact/data/rows.json', encoding='utf-8'))
md = open('../../logical-chaos.md', encoding='utf-8').read().split('## Columns')[0]

# --- energy per bit against gates per bit (64-bit circuits, non-degenerate rows) ---
for scheme in ('all', 'maps+Euler'):
    xs, ys = [], []
    for r in rows:
        if '⚠' in r['flags'] or not r['L64']['v'] or not r['pj64']['v']:
            continue
        if scheme == 'maps+Euler' and 'RK4' in r['scheme']:
            continue
        xs.append(r['L64']['v'] / 64); ys.append(r['pj64']['v'])
    lx, ly = np.log10(xs), np.log10(ys)
    k, c = np.polyfit(lx, ly, 1); r2 = np.corrcoef(lx, ly)[0, 1] ** 2
    print(f"energy vs gates/bit ({scheme}): N={len(xs)} slope={k:.3f} R2={r2:.3f} "
          f"pJ per gate={10**c:.2e}")

# --- fidelity columns of the main table (64-bit circuit vs float64) ---
lines = [l for l in md.splitlines() if re.match(r'\| \d+ \|', l)]
tot = ok_lam = ok_den = out = deg = 0
for l in lines:
    c = [x.strip() for x in l.split('|')[1:-1]]
    lam, den = c[15], c[16]
    tot += 1
    if 'n/a' in lam: deg += 1; continue
    ok_lam += '✓' in lam; ok_den += '✓' in den; out += '✗' in lam or '✗' in den
print(f"rows={tot} degenerate={deg} lambda at noise floor={ok_lam} density at noise floor={ok_den} "
      f"left attractor={out}")

def lam_err(c):
    v = c.replace('✓', '').replace('✗', '').strip()
    m = re.match(r'([\d.]+)×10⁻(\S+)', v)
    sup = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
    return float(m.group(1)) * 10 ** -int(m.group(2).translate(sup)) if m else float(v)

errs = []
for l in lines:
    c = [x.strip() for x in l.split('|')[1:-1]]
    if 'n/a' in c[15] or '✗' in c[15]: continue
    errs.append(lam_err(c[15]))
errs = np.array(errs)
print(f"lambda rel. error: median={np.median(errs):.2e}, <1%: {np.mean(errs < 0.01):.0%}, "
      f"<5%: {np.mean(errs < 0.05):.0%} of {len(errs)} rows")

# --- LUTs against gate count (authors' Vivado runs, 64 bits) ---
luts = {'Gingerbreadman': (450, 450), 'Lozi': (754, 758), 'Tent': (879, 915), 'MDCS': (6432, 6838),
        'Logistic': (23705, 23994), 'Chua': (22647, 25724), 'Rossler': (31925, 29704),
        'Lorenz': (53799, 49450)}
g = np.array([v[0] for v in luts.values()]); u = np.array([v[1] for v in luts.values()])
for k_, (a, b) in luts.items(): print(f"  {k_:15s} gates={a:6d} LUTs={b:6d} ratio={b/a:.3f}")
k, c = np.polyfit(np.log10(g), np.log10(u), 1)
print(f"LUTs vs gates: ratio range {min(u/g):.3f}-{max(u/g):.3f}, log-log slope={k:.3f}, "
      f"R2={np.corrcoef(np.log10(g), np.log10(u))[0,1]**2:.4f}")
