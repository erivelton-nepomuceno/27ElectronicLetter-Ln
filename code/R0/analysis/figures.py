# Fig. 1 (gates per iteration against word width) and Fig. 2 (estimated energy per output
# bit against gates per state bit). Writes fig1_Ln.pdf and fig2_energy.pdf in Paper/R0 and prints the Fig. 2 fit. Usage (from code/R0): python analysis/figures.py
# Colours: first three slots of the default validated categorical palette (blue, orange,
# aqua), one per cost class; markers and direct labels keep the figures readable in grey.
# Size: 86 mm wide (the column width of the Wiley template, 244.7 pt), so the figures are
# included at scale 1; text in STIX at 9 pt (axis titles) and 8 pt (ticks, labels), the
# body size of the template; axes and text black, grid light grey.
import json, os, re, sys, unicodedata
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
PAPER = os.path.join(ROOT, '..', '..', 'Paper', 'R0')  # figures go next to paper.tex
COMPUTE = os.path.join(ROOT, 'ec_artifact_src', 'ec_artifact', 'compute')
sys.path.insert(0, COMPUTE)

CLASS = {'L': ('Piecewise linear', '#2a78d6', 'o'), 'P': ('Polynomial', '#eb6834', 's'),
         'D': ('Polynomial', '#eb6834', 's'), 'T': ('Transcendental', '#1baf7a', '^')}
INK, MUTED, GRID = 'black', '#555555', '#e6e6e6'
MM = 1 / 25.4
plt.rcParams.update({'font.family': 'serif', 'font.serif': ['STIX Two Text', 'STIXGeneral', 'Times New Roman'],
                     'mathtext.fontset': 'stix', 'font.size': 8, 'axes.labelsize': 9,
                     'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 8,
                     'axes.edgecolor': INK, 'axes.labelcolor': INK, 'xtick.color': INK,
                     'ytick.color': INK, 'text.color': INK, 'axes.linewidth': 0.6,
                     'xtick.major.width': 0.6, 'ytick.major.width': 0.6,
                     'xtick.minor.width': 0.4, 'ytick.minor.width': 0.4, 'pdf.fonttype': 42})
W = 86 * MM


def style(ax):
    ax.grid(True, which='major', color=GRID, linewidth=0.5); ax.set_axisbelow(True)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)


# ---------------- Fig. 1 ----------------
d = json.load(open(os.path.join(HERE, 'fig1_data.json')))
cls = {'Gingerbreadman': 'L', 'Lozi': 'L', 'Tent': 'L', 'MDCS': 'P', 'Logistic': 'P',
       'Chua': 'P', 'Rossler': 'P', 'Lorenz': 'P'}
# Direct labels at the right end; curves that end close together share one label.
label = {'Lorenz': 'Lorenz', 'Rossler': 'Rössler', 'Chua': 'Chua, logistic', 'MDCS': 'MDCS',
         'Tent': 'Tent, Lozi', 'Gingerbreadman': 'Gingerbreadman'}
fig, ax = plt.subplots(figsize=(W, 68 * MM))
for name, v in d.items():
    _, col, mk = CLASS[cls[name]]
    ax.plot(v['n'], v['L'], color=col, marker=mk, markersize=3, linewidth=1.0,
            markeredgecolor='white', markeredgewidth=0.4, zorder=3)
    if name in label:
        dy = {'Lorenz': 6, 'Rossler': 2, 'Chua': -3, 'MDCS': -3}.get(name, 0)
        ax.annotate(label[name], (v['n'][-1], v['L'][-1]), xytext=(4, dy),
                    textcoords='offset points', va='center', fontsize=8)
# Reference slopes, drawn in the empty space between the classes, labelled at the end.
for k, (c0, n0, n1) in {1: (2.0, 16, 256), 2: (0.49, 64, 256)}.items():
    nn = np.array([n0, n1], float)
    ax.plot(nn, c0 * nn ** k, color=MUTED, linestyle=(0, (3, 2)), linewidth=0.6, zorder=2)
    at, off = nn[-1], (3, -2)
    ax.annotate(f'slope {k}', (at, c0 * at ** k), xytext=off,
                textcoords='offset points', va='center', fontsize=8, color=MUTED)
ax.set_xscale('log', base=2); ax.set_yscale('log')
ax.set_xticks([16, 32, 64, 128, 256]); ax.set_xticklabels(['16', '32', '64', '128', '256'])
ax.set_xlim(14, 1100); ax.set_xlabel('Word width $n$ (bits)'); ax.set_ylabel('Gates per iteration $L(n)$')
for c in ('L', 'P'):
    lab, col, mk = CLASS[c]
    ax.plot([], [], color=col, marker=mk, markersize=3, linewidth=1.0, label=lab)
ax.set_ylim(20, 1e7)
ax.legend(loc='upper left', frameon=False, handlelength=1.6)
style(ax); fig.tight_layout(pad=0.3)
fig.savefig(os.path.join(PAPER, 'fig1_Ln.pdf')); plt.close(fig)

# ---------------- Fig. 2 ----------------
import zoo, zoo2  # noqa: E402  (number of state variables per system)


def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]', '', s.replace('mu', ''))


def base(s): return norm(re.split(r'\s*\(', s)[0])


nv = {}
for t in zoo2.all_systems(): nv[norm(t[0])] = len(t[2]); nv.setdefault(base(t[0]), len(t[2]))
for t in zoo.SYSTEMS: nv[norm(t[0])] = len(t[3]); nv.setdefault(base(t[0]), len(t[3]))
nv.update({base('MDCS'): 1, base('Bernoulli'): 1})
rows = json.load(open(os.path.join(ROOT, 'ec_artifact_src', 'ec_artifact', 'data', 'rows.json'), encoding='utf-8'))
pts, miss = [], []
for r in rows:
    if '⚠' in r['flags'] or not r['L64']['v'] or not r['pj64']['v']: continue
    nm = re.sub(r'[◊⚠]', '', r['name']).strip()
    v = nv.get(norm(nm)) or nv.get(base(nm))
    if v is None: miss.append(nm); continue
    pts.append((r['L64']['v'] / (64 * v), r['pj64']['v'], r['cls'], 'RK4' in r['scheme'], nm))
if miss: print('unmatched:', sorted(set(miss)))
x = np.array([p[0] for p in pts]); y = np.array([p[1] for p in pts])
k, c = np.polyfit(np.log10(x), np.log10(y), 1); r2 = np.corrcoef(np.log10(x), np.log10(y))[0, 1] ** 2
print(f'Fig. 2: N={len(pts)} (RK4 {sum(p[3] for p in pts)}), slope={k:.3f}, R2={r2:.3f}')
fig, ax = plt.subplots(figsize=(W, 66 * MM))
# Systems of Table 1 (maps and Euler flows): larger markers with a black edge and a label.
TAB = {'Gingerbreadman': (5, -9), 'Lozi': (5, -4), 'Tent': (-5, 6), 'MDCS': (-6, 6),
       'Chua': (6, -7), 'Rössler': (6, -2), 'Lorenz': (-6, 7), 'Logistic': (6, -6)}
key = lambda p: p[4].split(' (')[0]
for c_ in ('L', 'P', 'D', 'T'):
    sel = [p for p in pts if p[2] == c_]
    if not sel: continue
    lab, col, mk = CLASS[c_]
    ax.scatter([p[0] for p in sel], [p[1] for p in sel], s=12, marker=mk, color=col,
               edgecolors='white', linewidths=0.4, alpha=0.75,
               label=lab if c_ != 'D' else None, zorder=3)
xx = np.array([x.min() / 1.3, x.max() * 1.3])
ax.plot(xx, 10 ** c * xx ** k, color=INK, linewidth=0.8, zorder=2)
for p in pts:
    if p[3] or key(p) not in TAB: continue
    lab, col, mk = CLASS[p[2]]
    ax.scatter([p[0]], [p[1]], s=26, marker=mk, color=col, edgecolors=INK, linewidths=0.7, zorder=4)
    dx, dy = TAB[key(p)]
    ax.annotate(key(p), (p[0], p[1]), xytext=(dx, dy), textcoords='offset points',
                ha='left' if dx > 0 else 'right', va='center', fontsize=8)
ax.text(0.03, 0.97, f'Fit: slope {k:.2f}, $R^2 = {r2:.2f}$, {len(pts)} circuits',
        transform=ax.transAxes, va='top', fontsize=8)
ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xlabel('Gates per state bit'); ax.set_ylabel('Estimated energy per output bit (pJ)')
ax.legend(loc='lower right', frameon=False, handletextpad=0.2, borderaxespad=0.2)
style(ax); fig.tight_layout(pad=0.3)
fig.savefig(os.path.join(PAPER, 'fig2_energy.pdf')); plt.close(fig)
