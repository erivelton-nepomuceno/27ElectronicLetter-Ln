# Architecture swap: gate counts of products, constants and systems for four adder and
# multiplier choices, with exact constants. Checks every netlist against the
# ripple + Booth netlist on random inputs. Writes analysis/arch_swap.json.
# Usage (from code/R0): python analysis/arch_swap.py
import json, random, os
import numpy as np
from archs import ARCHS, zoo
import mdcs

NS = [16, 24, 32, 48, 64, 96, 128]
SYS = [('Gingerbreadman', zoo.gingerbread, 5, 2), ('Lozi', zoo.lozi, 3, 2),
       ('Tent', zoo.tent, 2, 1), ('Logistic', zoo.logistic, 2, 1),
       ('Chua', zoo.chua, 4, 3), ('Rossler', zoo.rossler, 10, 3), ('Lorenz', zoo.lorenz, 12, 3)]


def build(cls, fn, n, I, nv):
    B = cls(n, I); st = [[(chr(97 + v), i) for i in range(n)] for v in range(nv)]
    return B, fn(B, *st)


def same(fn, n, I, nv, cls, trials=50):
    ref = zoo.compile_net(*build(ARCHS['ripple + Booth'], fn, n, I, nv), nv)
    B, o = build(cls, fn, n, I, nv); alt = zoo.compile_net(B, o, nv)
    rnd = random.Random(1)
    for _ in range(trials):
        s = [[rnd.getrandbits(1) for _ in range(n)] for _ in range(nv)]
        if ref(*s) != alt(*s): return False
    return True


def unit(cls, what, n, I=4):
    B = cls(n, I); x = [('a', i) for i in range(n)]; y = [('b', i) for i in range(n)]
    out = B.mul(x, y) if what == 'product' else B.lin(zoo.Z(B), [(x, 0.2)])
    return mdcs.live(B.g, [out])


res = {}
for an, cls in ARCHS.items():
    r = res[an] = {}
    for what in ('product', 'constant 1/5'):
        L = [unit(cls, what, n) for n in NS]
        r[what] = {'L': L, 'n2': float(np.polyfit(NS, L, 2)[0])}
    for name, fn, I, nv in SYS:
        L = [mdcs.live(*(lambda B, o: (B.g, o))(*build(cls, fn, n, I, nv))) for n in NS]
        p = np.polyfit(np.log(NS[-3:]), np.log(L[-3:]), 1)[0]
        r[name] = {'L': L, 'n2': float(np.polyfit(NS, L, 2)[0]), 'loglog_slope': float(p),
                   'same_as_ref_32bit': same(fn, 32, I, nv, cls)}
    print(an, {k: round(v['n2'], 3) for k, v in r.items()}, flush=True)
json.dump({'ns': NS, 'results': res}, open(os.path.join(os.path.dirname(__file__), 'arch_swap.json'), 'w'), indent=1)
print('DONE')
