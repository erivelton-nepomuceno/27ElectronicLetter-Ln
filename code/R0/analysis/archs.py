# Gate-level backends for the architecture study, built on zoo.BitB:
#  - exact constants: float constants are converted to the nearest simple fraction, so a
#    constant is stored to the resolution of the word instead of to 53 bits;
#  - carry-lookahead adder: 4-bit lookahead blocks, rippled between blocks;
#  - array multiplier: one AND row and one adder per multiplier bit (shift-and-add,
#    two's complement), keeping the same columns as the Booth multiplier.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ec_artifact_src', 'ec_artifact', 'compute'))
from fractions import Fraction
import zoo


def exact(c):
    return Fraction(c).limit_denominator(10**7) if isinstance(c, float) else c


class Exact(zoo.BitB):
    def K(s, c, W=None, F=None): return super().K(exact(c), W, F)
    def _csd(s, c): return super()._csd(exact(c))


class CLA:
    def _add(s, A, B, cin=0):
        g = s.g; o = []; c = cin
        for k in range(0, len(A), 4):
            a, b = A[k:k + 4], B[k:k + 4]
            G = [g.AND(x, y) for x, y in zip(a, b)]; P = [g.XOR(x, y) for x, y in zip(a, b)]
            cs = [c]
            for i in range(len(a)):
                # c_{i+1} = G_i | P_i G_{i-1} | ... | P_i...P_0 c, flattened per bit
                t = G[i]; pp = P[i]
                for j in range(i - 1, -1, -1):
                    t = g.OR(t, g.AND(pp, G[j])); pp = g.AND(pp, P[j])
                cs.append(g.OR(t, g.AND(pp, c)))
            o += [g.XOR(P[i], cs[i]) for i in range(len(a))]; c = cs[-1]
        return o


class Array:
    def mul(s, A, B):
        g = s.g; W, F = s.W, s.F; HI = F + W
        ext = lambda k: A[k] if 0 <= k < W else (A[-1] if k >= W else 0)
        acc = [0] * HI
        for j in range(W):
            pp = [g.AND(ext(c - j), B[j]) for c in range(j, HI)]
            acc[j:] = s.sub(acc[j:], pp) if j == W - 1 else s._add(acc[j:], pp)
        return acc[F:HI]


ARCHS = {
    'ripple + Booth': Exact,
    'CLA + Booth': type('CB', (CLA, Exact), {}),
    'ripple + array': type('RA', (Array, Exact), {}),
    'CLA + array': type('CA', (CLA, Array, Exact), {}),
}
