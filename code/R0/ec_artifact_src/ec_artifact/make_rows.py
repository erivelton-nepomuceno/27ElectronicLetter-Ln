#!/usr/bin/env python3
"""Rebuild data/rows.json from the computed results.

Inputs: data/table_rk4.md (gate counts, L(n), 32-bit pJ/bit for every map, Euler and RK4 row),
compute/e64.json (64-bit pJ/bit), data/mdcs_metrics.json (64-bit vs float64 metrics),
plus the tent-map update (mu = 2 - 2^-7)."""
import json, re, pathlib
root = pathlib.Path(__file__).parent
E = json.loads((root / "compute/e64.json").read_text())
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
idx = {}
for k, v in E.items():
    p, nm = k.split("|", 1); idx.setdefault(p, {})[norm(nm)] = v
alias = {"rssler": "rossler", "l": "lu", "halvorsena14": "halvorsen", "tent199": "tentmu199", "sinemap099": "sinemapmu099",
         "hnon": "henon", "bernoulli": "bernoullidyadic", "mdcsnepomucenoetal2019": "mdcs"}
def look(p, nm):
    k = norm(nm); k = alias.get(k, k); d = idx[p]
    if k in d: return d[k]
    c = [v for kk, v in d.items() if kk[:9] == k[:9]]
    return c[0] if c else None
def num(s):
    s = re.sub(r"[,*‡ᵉ⚠—]", "", s).strip()
    try: return float(s)
    except ValueError: return None
cell = lambda s: {"t": s, "v": num(s), "m": "".join(f for f in "*‡ᵉ⚠" if f in s)}
rows, last = [], None
for line in (root / "data/table_rk4.md").read_text().split("\n")[2:]:
    c = [x.strip() for x in line.split("|")][1:-1]
    rk = c[1].startswith("↳")
    name = (last if rk else c[1]).replace("**", "")
    if not rk: last = name
    flags = "" if rk else "".join(f for f in "⚠◊" if f in name)
    clean = name.replace("⚠", "").replace("◊", "").strip()
    v64 = look("R" if rk else "E", clean); deg = "⚠" in c[11]
    rows.append({"rank": int(c[0]) if c[0] else rows[-1]["rank"], "name": clean.replace("Rossler", "Rössler").replace("Henon", "Hénon"),
                 "flags": flags, "type": c[2], "cls": c[3].split(" ")[0], "scheme": c[4], "law": c[5],
                 "L64": cell(c[6]), "L16": cell(c[7]), "L32": cell(c[8]), "L128": cell(c[9]), "L256": cell(c[10]),
                 "pj32": cell(c[11]), "pj64": {"t": "0.010 ⚠" if deg else f"{v64:.3f}", "v": 0.010 if deg else v64, "m": "⚠" if deg else ""}})
for r in rows:   # tent map rebuilt with mu = 2 - 2^-7 (linear class)
    if r["name"].startswith("Tent"):
        r.update(name="Tent (μ = 2 − 2⁻⁷)", cls="L", law="14n − 17",
                 L64=cell("879"), L16=cell("207"), L32=cell("431"), L128=cell("1,775"), L256=cell("3,567"),
                 pj32={"t": "0.133", "v": 0.1334, "m": ""}, pj64={"t": "0.140", "v": 0.140, "m": ""})
    if r["name"].startswith("MDCS"):
        r.update(json.loads((root / "data/mdcs_metrics.json").read_text()))
(root / "data/rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=0))
print(f"data/rows.json: {len(rows)} rows")
