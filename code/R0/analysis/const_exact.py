# Constant cost with exact rational constants (precision grows with n) vs float64 constants,
# and the cost of one product, in the BitB architecture. Usage: python const_exact.py <compute dir>
import sys; sys.path.insert(0, sys.argv[1])
from fractions import Fraction as Fr
import numpy as np, zoo, mdcs

def cost_const(c, n, I=4):
    B = zoo.BitB(n, I); x = [('a', i) for i in range(n)]
    return mdcs.live(B.g, [B.lin(zoo.Z(B), [(x, c)])]), len(B._csd(c))

def cost_mul(n, I=4):
    B = zoo.BitB(n, I); x = [('a', i) for i in range(n)]; y = [('b', i) for i in range(n)]
    return mdcs.live(B.g, [B.mul(x, y)])

ns = [16, 32, 48, 64, 96, 128, 192, 256]
for name, c in {'1/5 exact': Fr(1, 5), '8/3 exact': Fr(8, 3), '0.2 float64': 0.2, '8/3 float64': 8/3,
                'dt*15.6*2/7 exact': Fr(1, 128) * Fr(156, 10) * Fr(2, 7)}.items():
    r = [cost_const(c, n) for n in ns]; g = [a for a, _ in r]
    print(f"{name:20s} gates={g} digits={[d for _, d in r]} "
          f"n^2 coef (fit 16-256)={np.polyfit(ns, g, 2)[0]:.3f}  gates/n^2 at 256={g[-1]/256**2:.3f}")
gm = [cost_mul(n) for n in ns]
print(f"{'one product':20s} gates={gm} n^2 coef={np.polyfit(ns, gm, 2)[0]:.3f}")
for I in (2, 4, 12):
    gm = [cost_mul(n, I) for n in (32, 64, 128)]
    print(f"  product, I={I}: {gm}  n^2 coef={np.polyfit((32, 64, 128), gm, 2)[0]:.3f}")
