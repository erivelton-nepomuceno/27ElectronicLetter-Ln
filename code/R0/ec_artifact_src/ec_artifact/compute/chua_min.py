# Minimal gate-level Chua circuit.
# Only AND/OR/XOR/NOT. The design is flattened into one netlist with constant
# folding and structural hashing, so it no longer mirrors the arithmetic.
#
# Algebraic rewrite used to build it (dt = 2^-7, alpha=15.6, beta=28, m0=-8/7, m1=-5/7):
#   (|x+1| - |x-1|)/2 = sat(x) = clamp(x,-1,1)  -> pure bit logic, no adders
#   x' = x + cxx*x + cxy*y + cxs*sat(x)          (dt and alpha folded into constants)
#   y' = y + (x - y + z) * 2^-7
#   z' = z - 28*2^-7 * y
W, FRAC = 20, 16            # 4 integer bits (|x|,|z| < 8) + 16 fraction bits

class Net:
    def __init__(s): s.ops=[]; s.h={}
    def _g(s,op,a,b=None):
        k=(op,a,b); 
        if k in s.h: return s.h[k]
        s.ops.append(k); n=('n',len(s.ops)-1); s.h[k]=n; return n
    def NOT(s,a):
        if a in (0,1): return 1-a
        if a[0]=='n' and s.ops[a[1]][0]=='NOT': return s.ops[a[1]][1]
        return s._g('NOT',a)
    def AND(s,a,b):
        if a==0 or b==0: return 0
        if a==1: return b
        if b==1: return a
        if a==b: return a
        if a>b: a,b=b,a
        return s._g('AND',a,b)
    def OR(s,a,b):
        if a==1 or b==1: return 1
        if a==0: return b
        if b==0: return a
        if a==b: return a
        if a>b: a,b=b,a
        return s._g('OR',a,b)
    def XOR(s,a,b):
        if a==0: return b
        if b==0: return a
        if a==1: return s.NOT(b)
        if b==1: return s.NOT(a)
        if a==b: return 0
        if a>b: a,b=b,a
        return s._g('XOR',a,b)

def build(digits_budget=5, G=4):
    g=Net()
    X=[('x',i) for i in range(W)]; Y=[('y',i) for i in range(W)]; Z=[('z',i) for i in range(W)]
    def add(A,B,cin=0):
        o=[];c=cin
        for a,b in zip(A,B):
            s1=g.XOR(a,b); o.append(g.XOR(s1,c)); c=g.OR(g.AND(a,b),g.AND(s1,c))
        return o
    def sub(A,B): return add(A,[g.NOT(b) for b in B],1)
    def asr(A,k): return A[k:]+[A[-1]]*k
    def shl(A,k): return [0]*k+A[:W-k]
    # sat(x) = clamp(x,-1,1), pure logic
    s=X[-1]
    inr=1
    for i in range(FRAC,W-1): inr=g.AND(inr, g.NOT(g.XOR(X[i],s)))
    SAT=[g.AND(inr,X[i]) for i in range(FRAC)] + [g.OR(g.NOT(inr),s)] + [s]*(W-FRAC-1)
    def csd(c):
        v=round(c*(1<<FRAC)); t=[]; i=0
        while v:
            if v&1: d=2-(v&3); t.append((d,i)); v-=d
            v>>=1; i+=1
        t.sort(key=lambda q:-q[1]); return t
    def lin(acc, terms):            # acc + sum(coef*signal), with G guard bits, rounded once
        WW=W+G
        up=lambda A:[0]*G+A
        acc=up(acc); acc[G-1]=1      # +half LSB -> round to nearest at the end
        def shl(A,k): return [0]*k+A[:WW-k]
        def asr(A,k): return A[k:]+[A[-1]]*k
        for sig,c in terms:
            sig=up(sig)
            ds=csd(c)
            if digits_budget: ds=ds[:digits_budget]
            for d,i in ds:
                k=i-FRAC; t=shl(sig,k) if k>=0 else asr(sig,-k)
                acc = add(acc,t) if d>0 else sub(acc,t)
        return acc[G:]
    dta=15.6/128; m0,m1=-8/7,-5/7
    Xn=lin(X,[(X,-dta*(1+m1)),(Y,dta),(SAT,-dta*(m0-m1))])
    Yn=add(Y, asr(add(sub(X,Y),Z),7))
    Zn=lin(Z,[(Y,-28/128)])
    return g,Xn,Yn,Zn

def simulate(g,outs,state):
    val={}
    def v(a):
        if a in (0,1): return a
        if a[0]=='n': return val[a[1]]
        return state[a[0]][a[1]]
    for i,(op,a,b) in enumerate(g.ops):
        val[i]={'NOT':lambda:1-v(a),'AND':lambda:v(a)&v(b),'OR':lambda:v(a)|v(b),'XOR':lambda:v(a)^v(b)}[op]()
    return {k:[v(bit) for bit in o] for k,o in zip('xyz',outs)}

def tob(x): v=round(x*(1<<FRAC))&((1<<W)-1); return [(v>>i)&1 for i in range(W)]
def tof(A): v=sum(b<<i for i,b in enumerate(A)); return (v-(1<<W) if A[-1] else v)/(1<<FRAC)
