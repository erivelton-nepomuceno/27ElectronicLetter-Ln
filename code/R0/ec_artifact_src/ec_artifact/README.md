# Efficient Chaos — interactive table: code and data

Everything needed to rebuild and update the "Efficient Chaos" artifact
(https://claude.ai/artifact/CFRf1MxemUBP21vUthP5yY): 117 rows (27 map rows, 45 flows × Euler/RK4).

## Quick start

```
python make_rows.py    # computed results  -> data/rows.json
python build_page.py   # template + data   -> web/index.html
```
`web/index.html` is the self-contained page (open it in a browser, or publish it to the artifact link from a claude.ai chat).
Rebuilding reproduces the published page exactly (the only difference is 879 vs 879.0 in the tent-map row, which is identical in JavaScript).

## Layout

| Path | Contents |
| --- | --- |
| `web/template.html` | Page code (HTML, CSS, JS: sorting, filters, pinned columns, top/bottom scrollbars, profile pop-up) with `__ROWS__` and `__PROFILES__` placeholders |
| `data/rows.json` | Table data, one object per row (name, type, class, scheme, L(n), gates at 16–256 bits, pJ/bit at 32/64 bits, 64-bit metrics) |
| `data/profiles.json` | Full system profiles for the pop-up (equations, plots as inline SVG, metrics, reference, BibTeX); currently the MDCS |
| `data/table_rk4.md` | Gate counts, L(n) and 32-bit pJ/bit for every row (input to `make_rows.py`) |
| `data/mdcs_metrics.json` | MDCS 64-bit vs float64 metrics shown in the table |
| `build_page.py` | Injects the data into the template |
| `make_rows.py` | Rebuilds `rows.json` from the computed results (includes the tent map with μ = 2 − 2⁻⁷) |
| `compute/` | Code that produced the numbers (below) |

## compute/

| File | Role |
| --- | --- |
| `chua_min.py` | `Net`: gate netlist with constant folding and structural hashing |
| `zoo.py` | Original 20 systems; float (`FloatB`) and gate-level (`BitB`) backends; `compile_net` |
| `ext.py` | Gate-level sin, cos, exp, division, square root, sign; `FloatX` |
| `zoo2.py` | Systems from Wikipedia's list of chaotic maps (`MAPS`, `FLOWS`, `EXCLUDED`) |
| `mdcs.py`, `mdcs_gate.py` | MDCS (Nepomuceno et al., 2019); `live()` counts gates that drive an output |
| `tune.py` | Lyapunov exponent helper |
| `vhdl_power.py`, `energy_fn.py` | LUT packing and switching-activity energy model (40 fJ per LUT toggle, 10 fJ per flip-flop) |
| `run3.py` → `res2.json` | Integer bits, L(n) and checks for the zoo2 systems |
| `energy_all.py` → `energy_all.json` | pJ/bit at 32 bits (maps and Euler flows) |
| `rk4_all.py` → `rk4_all.json` | RK4 versions of all flows: dt, L(n), pJ/bit at 32 bits |
| `energy64.py` → `e64.json` | pJ/bit at 64 bits for every row |

Note: `run3.py`, `energy_all.py`, `rk4_all.py` and `energy64.py` run their whole job when executed or imported; they skip rows already in their JSON files. Run them from inside `compute/`. Requires Python 3 with NumPy and SciPy.
