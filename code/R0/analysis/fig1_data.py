# Data for Fig. 1: gates per iteration L(n) of eight systems, ripple + Booth with exact
# constants, n = 16..256.
# Writes analysis/fig1_data.json. Usage (from code/R0): python analysis/fig1_data.py
import json, os
import numpy as np
from archs import ARCHS, zoo
import mdcs, mdcs_gate

HERE = os.path.dirname(__file__)
NS = [16, 24, 32, 48, 64, 96, 128, 192, 256]
SYS = [('Gingerbreadman', zoo.gingerbread, 5, 2), ('Lozi', zoo.lozi, 3, 2),
       ('Tent', zoo.tent, 2, 1), ('Logistic', zoo.logistic, 2, 1), ('Chua', zoo.chua, 4, 3),
       ('Rossler', zoo.rossler, 10, 3), ('Lorenz', zoo.lorenz, 12, 3)]
out = {}
for name, fn, I, nv in SYS:
    L = []
    for n in NS:
        B = ARCHS['ripple + Booth'](n, I); st = [[(chr(97 + v), i) for i in range(n)] for v in range(nv)]
        L.append(mdcs.live(B.g, fn(B, *st)))
    out[name] = {'n': NS, 'L': L, 'fit': [float(c) for c in np.polyfit(NS, L, 2)]}
    print(name, L, flush=True)
L = []
for n in NS:
    g, o = mdcs_gate.build(n, 2, 5); L.append(mdcs.live(g, o))  # as in Table 1 and Vivado
out['MDCS'] = {'n': NS, 'L': L, 'fit': [float(c) for c in np.polyfit(NS, L, 2)]}
json.dump(out, open(os.path.join(HERE, 'fig1_data.json'), 'w'), indent=1)
print('DONE')
