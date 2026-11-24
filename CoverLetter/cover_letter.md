Maynooth University, Maynooth, Ireland
[Date]

The Editor-in-Chief
Electronics Letters, IET

Dear Editor,

We submit the Letter "Logic-gate complexity of digital chaotic systems" by
Erivelton Nepomuceno, Thalita Nazaré, Arthur M. Lima and Chi-Tsun Cheng for
consideration in Electronics Letters.

Chaotic generators are candidates for random number generation and encryption in
lightweight hardware, but their digital cost is usually reported system by system,
after synthesis. This Letter shows that the cost can be predicted before synthesis.
We give a construction from the equations of a map or flow to a network of two-input
logic gates in n-bit fixed point, and show that the gate count per iteration is
bounded by (5.75M + 2.5C)n² + O(n), where M counts products between state variables
and C counts non-dyadic constants. Piecewise-linear systems therefore have linear
cost in n.

The main results are:

- a gate-count law that separates quadratic-cost operations from linear-cost ones,
  with architecture-dependent coefficients;
- a design rule: replacing a non-dyadic constant with a dyadic one reduces the 64-bit
  tent map from 5571 to 879 gates with a nearly unchanged Lyapunov exponent;
- FPGA lookup-table counts for eight systems within 14% of the predicted gate counts,
  and fidelity checks of each 64-bit circuit against float64.

These results give designers of chaos-based hardware a simple screening tool, which
we expect to interest the broad engineering readership of Electronics Letters. Code
and data for all 73 systems studied are openly available.

The manuscript is original, has not been published, and is not under consideration
elsewhere. All authors have approved the submission and declare no conflicts of
interest.

Yours sincerely,

Erivelton Nepomuceno
Hamilton Institute and Department of Electronic Engineering
Maynooth University, Ireland
erivelton.nepomuceno@mu.ie
