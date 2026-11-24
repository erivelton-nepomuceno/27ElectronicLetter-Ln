# Cost of one constant multiplication c*x in the BitB architecture, as a function of
# word width n and of the constant; and the Chua constants. Usage: python const_cost.py <compute dir>
import sys; sys.path.insert(0, sys.argv[1])
import numpy as np, zoo, mdcs

def cost(c, n, I=4):
    B = zoo.BitB(n, I); x = [('a', i) for i in range(n)]
    out = B.lin(zoo.Z(B), [(x, c)])
    return mdcs.live(B.g, [out]), len(B._csd(c))

ns = [16, 24, 32, 40, 48, 56, 64, 96, 128]
dt = 2**-7; a = 15.6; m0, m1 = -8/7, -5/7
cases = {'0.2': 0.2, '8/3': 8/3, '0.2*2^-8 (Rossler)': .2 * 2**-8,
         '8/3*2^-7 (Lorenz)': 8/3 * 2**-7,
         'chua dt*a*(1+m1)': dt*a*(1+m1), 'chua dt*a': dt*a, 'chua dt*a*(m0-m1)': dt*a*(m0-m1),
         '1.99 (tent)': 1.99}
for name, c in cases.items():
    L = [cost(c, n) for n in ns]
    g = [l[0] for l in L]; d = [l[1] for l in L]
    fit16_64 = np.polyfit(ns[:7], g[:7], 2)
    print(f"{name:22s} gates={g}  csd_digits={d}  fit16-64 n^2 coef={fit16_64[0]:.2f}")
