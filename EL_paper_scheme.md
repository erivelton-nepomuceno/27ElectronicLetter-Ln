# Paper scheme — Electronics Letters: a gate-count law for digital chaos

Source project: 26ChaosBoolean ("Efficient Chaos"), Erivelton Nepomuceno.
Purpose: a short, self-contained brief to start a quick Electronics Letters (EL) paper in a separate project.
Check the current EL author guidelines for length, figure and reference limits before drafting.

## 1. Core message (one sentence)

The number of logic gates needed per iteration by a fixed-point chaotic map or flow follows L(n) ≈ a·M·n² + b·C·n² + O(n), where n is the word width, M the number of products between state variables and C the number of non-dyadic constants; so the digital cost of chaos can be predicted from the equations alone, and the simplest digital chaos is the one with M = C = 0.

## 2. Working title options

1. Predicting the gate cost of digital chaotic systems
2. A gate-count law for fixed-point chaotic maps and flows
3. How many logic gates does chaos need?

## 3. Draft abstract (about 100 words)

The digital cost of chaotic systems is usually reported case by case. We implement chaotic maps and flows using only two-input AND, OR, XOR and NOT gates in n-bit fixed point and show that the gate count per iteration follows L(n) ≈ a·M·n² + b·C·n² + O(n), where M counts products between state variables and C counts non-dyadic constants. Systems with M = C = 0 (e.g. Lozi, Gingerbreadman, tent map with μ = 2 − 2⁻⁷) are linear in n; products make them quadratic; sin, cos and exp add a cubic term. Estimated energy per bit is proportional to gates per bit (R² = 0.975), and FPGA synthesis confirms the classes.

## 4. Structure of the letter

| Section | Content | Approx. length |
| --- | --- | --- |
| Introduction | Chaos in hardware (cryptography, random numbers); simplicity is usually judged by the equations (Sprott), not by digital cost; contribution: a predictive gate-count law | 1 paragraph |
| Method | Fixed point, n bits; only AND/OR/XOR/NOT; ripple adders, radix-4 Booth multipliers, canonical-signed-digit constants; Euler with dt = 2⁻ᵏ (dt is wiring); netlist optimisation (constant folding, shared gates, dead-gate removal) | 1–2 paragraphs |
| The law | L(n) ≈ a·M·n² + b·C·n² + O(n); a ≈ 5.75 and b ≈ 2.5 for this architecture; three classes (linear, polynomial, transcendental) | 1 paragraph + Fig. 1 |
| Design rule | Avoid state products, use dyadic constants; example tent μ = 1.99 → 2 − 2⁻⁷: about 134n → 14n − 17, same Lyapunov exponent | 1 paragraph |
| Validation | Architecture swap (exponents and classes unchanged); FPGA synthesis of 4–5 systems; energy per bit against gates per bit | 1–2 paragraphs + Table 1, Fig. 2 |
| Fidelity | One sentence + values: the digital system remains chaotic (λ, 64-bit vs float64 checks) | 2–3 sentences |
| Conclusion | Cost predictable from equations; simplest digital chaos; outlook (full 73-system ranking in a longer paper) | 1 paragraph |

## 5. Figures and table

- **Fig. 1 — L(n) on log-log axes** for about 8 systems (Gingerbreadman, Lozi, tent μ = 2 − 2⁻⁷, MDCS, Chua, Rössler, Lorenz, sine map), n = 16–256, slopes 1, 2 and 3 marked.
- **Fig. 2 — energy per bit against gates per bit** for the 69 non-degenerate systems, log-log, fitted line (slope ≈ 0.97, R² ≈ 0.975).
- **Table 1 — representative systems:** M, C, fitted L(n), gates at 32 and 64 bits, FPGA LUT count, pJ/bit.

Key values already available (32 / 64-bit gates): Gingerbreadman 7n + 2 (226 / 450); Lozi a = 1.75, 12n − 14 (370 / 754); tent μ = 2 − 2⁻⁷, 14n − 17 (431 / 879); MDCS ≈ 1.50n² + 4.7n − 26 (1,662 / 6,432); Chua (Euler) 6,891 / 22,647; Rössler 8.25n² − 27n − 169 (7,426 / 31,925); Lorenz 14.0n² − 51n − 281 (12,423 / 53,799); sine map ≈ 0.27n³ + 82n² + … (43,313 / 293,018).

## 6. Data and code to bring from 26ChaosBoolean

- `code/full_list/zoo.py`, `ext.py`, `zoo2.py` — system definitions and gate-level backends.
- `code/full_list/res2.json`, `e64.json`, `energy_all.json` — L(n), integer bits, pJ/bit at 32 and 64 bits.
- `code/full_list/energy_fn.py` — energy model (40 fJ per LUT toggle, 10 fJ per flip-flop).
- `vhdl/` — gate-level VHDL and testbenches for Gingerbreadman, Lozi, MDCS, Lorenz, sine map.
- `web/rows.json` — the full table (117 rows) for any extra numbers.

## 7. Work still needed (short list)

1. [ ] **Novelty search:** FPGA implementations of chaotic systems, multiplier-free chaotic oscillators, hardware cost of chaos, Sprott's simplest flows; position the law as a general predictive rule.
2. [ ] **Architecture swap:** recount 5–8 systems with carry-lookahead adders and array (non-Booth) multipliers; show a and b change but the exponents and classes do not.
3. [ ] **FPGA synthesis:** synthesise the five VHDL designs (plus the tent map) in Quartus or Vivado; report LUTs and, if possible, measured or tool-estimated power.
4. [ ] **Figures 1–2 and Table 1** from the saved data.
5. [ ] **Draft, then cut to the EL length limit;** about 10–15 references.

## 8. Main risks and replies to reviewers

- "Counts depend on the architecture" → state a and b as architecture constants; show the swap result.
- "Only estimates" → FPGA synthesis numbers in Table 1.
- "Is it still the same chaos?" → Lyapunov exponents and the 64-bit fidelity check.
- "Not new" → the novelty search; the contribution is the predictive law and the M, C design rule, not one more implementation.

## 9. Key references to start from

- Nepomuceno, E. G., Lima, A. M., Arias-García, J., Perc, M., & Repnik, R. (2019). Minimal digital chaotic system. Chaos, Solitons & Fractals, 120, 62–66. doi:10.1016/j.chaos.2019.01.019
- Sprott, J. C. (1994). Some simple chaotic flows. Physical Review E, 50, R647.
- Original references for Lorenz (1963), Rössler (1976), Chua (Matsumoto, 1984), Lozi (1978), Hénon (1976), Devaney's Gingerbreadman (1984). Verify every reference before submission.
