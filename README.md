# Logic-gate complexity of digital chaotic systems

Letter for Electronics Letters by E. Nepomuceno, T. Nazaré, A. M. Lima and C.-T. Cheng.

## Structure

| Path | Contents |
| --- | --- |
| `Paper/R0/` | Manuscript (`paper.tex`), references (`refs.bib`), figures, Wiley/IET template |
| `code/R0/` | Code to reproduce the results: `reproduce_paper.py`, `analysis/`, `ec_artifact_src/` |
| `CoverLetter/` | Cover letter |
| `logical-chaos.md` | Full results table and system profiles (73 systems, 117 implementations) |
| `EL_paper_scheme.md` | Paper plan |

`R0` is the original submission; revisions go in `R1`, `R2`, ...

## Build the paper

    cd Paper/R0
    latexmk paper.tex        # XeLaTeX; settings in latexmkrc

## Reproduce the results

    cd code/R0
    pip install numpy matplotlib
    python reproduce_paper.py              # full run
    python reproduce_paper.py --skip-slow  # quick check
    python analysis/paper_stats.py         # statistics quoted in the paper
    python analysis/figures.py             # writes the figures to Paper/R0

`reproduce_paper.py` recomputes the Table 1 gate counts and fits, a and b, the
tent-map rule, the architecture swap and Fig. 1 from gate netlists. It uses stored
results for the Fig. 2 energy estimates, the fidelity metrics and the Vivado LUT counts.

## Open items

- Default-synthesis HDL results (Paper/R0/paper.tex, Section 5, marked TODO)
- Zenodo DOI for the data availability statement
