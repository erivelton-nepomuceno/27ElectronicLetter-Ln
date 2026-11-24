# 20 chaotic systems (10 maps, 10 flows), each written ONCE against a backend,
# run either in floating point or as an optimised AND/OR/XOR/NOT netlist.
import math
from chua_min import Net

class FloatB:
    def K(s,c): return c
    def add(s,a,b): return a+b
    def sub(s,a,b): return a-b
    def mul(s,a,b): return a*b
    def abs(s,a): return abs(a)
    def lin(s,acc,terms,const=0.0): return acc+const+sum(c*v for v,c in terms)
    def frac(s,a): return a%1.0
    def shl(s,a,k): return a*2**k
    def asr(s,a,k): return a/2**k
    def ge_half(s,a): return 0.5 if a>=0.5 else 0.0
    def sat(s,a): return max(-1.0,min(1.0,a))

class BitB:
    def __init__(s,W,I,digits=None,G=4):
        s.W,s.I,s.F,s.G,s.d=W,I,W-I,G,digits; s.g=Net()
    def _add(s,A,B,cin=0):
        g=s.g;o=[];c=cin
        for a,b in zip(A,B):
            x=g.XOR(a,b); o.append(g.XOR(x,c)); c=g.OR(g.AND(a,b),g.AND(x,c))
        return o
    def K(s,c,W=None,F=None):
        W=W or s.W; F=s.F if F is None else F
        v=round(c*(1<<F))&((1<<W)-1); return [(v>>i)&1 for i in range(W)]
    def add(s,A,B): return s._add(A,B)
    def sub(s,A,B): return s._add(A,[s.g.NOT(b) for b in B],1)
    def shl(s,A,k): return [0]*k+A[:len(A)-k]
    def asr(s,A,k): return A[k:]+[A[-1]]*k
    def abs(s,A): return [s.g.XOR(a,A[-1]) for a in A]
    def frac(s,A): return A[:s.F]+[0]*s.I
    def ge_half(s,A): return [0]*(s.F-1)+[A[s.F-1]]+[0]*s.I
    def sat(s,A):
        g=s.g; sg=A[-1]; inr=1
        for i in range(s.F,s.W-1): inr=g.AND(inr,g.NOT(g.XOR(A[i],sg)))
        return [g.AND(inr,A[i]) for i in range(s.F)]+[g.OR(g.NOT(inr),sg)]+[sg]*(s.I-1)
    def _csd(s,c):
        v=round(c*(1<<(s.F+s.G))); t=[]; i=0
        while v:
            if v&1: d=2-(v&3); t.append((d,i)); v-=d
            v>>=1; i+=1
        t.sort(key=lambda q:-q[1]); return t[:s.d] if s.d else t
    def lin(s,acc,terms,const=0.0):
        G=s.G; WW=s.W+G; up=lambda A:[0]*G+A
        acc=up(acc); acc[G-1]=1
        if const: acc=s._add(acc,s.K(const,WW,s.F+G))
        for sig,c in terms:
            v=up(sig)
            for d,i in s._csd(c):
                k=i-(s.F+G); t=s.shl(v,k) if k>=0 else s.asr(v,-k)
                acc=s._add(acc,t) if d>0 else s.sub(acc,t)
        return acc[G:]
    def mul(s,A,B):
        g=s.g; W,F=s.W,s.F; HI=F+W
        ext=lambda k: A[k] if 0<=k<W else (A[-1] if k>=W else 0)
        acc=[0]*HI
        for j in range(W//2):
            bh,bm=B[2*j+1],B[2*j]; bl=B[2*j-1] if j else 0
            one=g.XOR(bm,bl)
            two=g.OR(g.AND(bh,g.AND(g.NOT(bm),g.NOT(bl))),g.AND(g.NOT(bh),g.AND(bm,bl)))
            pp=[g.XOR(g.OR(g.AND(one,ext(c-2*j)),g.AND(two,ext(c-2*j-1))),bh) for c in range(2*j,HI)]
            acc[2*j:]=s._add(acc[2*j:],pp,bh)
        return acc[F:HI]

Z=lambda B:B.K(0.0)
# ---------------- 10 maps ----------------
def logistic(B,x):       return [B.lin(Z(B),[(B.mul(x,B.sub(B.K(1.0),x)),3.9375)])]
def tent(B,x):           return [B.lin(Z(B),[(B.sub(B.K(.5),B.abs(B.sub(x,B.K(.5)))),1.9921875)])]
def bernoulli(B,x):      return [B.frac(B.shl(x,1))]
def henon(B,x,y):        return [B.lin(y,[(B.mul(x,x),-1.4)],1.0), B.lin(Z(B),[(x,.3)])]
def lozi(B,x,y):         return [B.lin(y,[(B.abs(x),-1.75)],1.0), B.asr(x,1)]
def cat(B,x,y):
    xn=B.frac(B.add(x,y)); return [xn, B.frac(B.add(xn,y))]
def baker(B,x,y):        return [B.frac(B.shl(x,1)), B.add(B.asr(B.frac(y),1),B.ge_half(x))]
def gingerbread(B,x,y):  return [B.lin(B.abs(x),[(y,-1)],1.0), x]
def duffing_map(B,x,y):  return [y, B.lin(Z(B),[(x,-.2),(y,2.75),(B.mul(B.mul(y,y),y),-1)])]
def tinkerbell(B,x,y):
    return [B.lin(Z(B),[(B.mul(x,x),1),(B.mul(y,y),-1),(x,.9),(y,-.6013)]),
            B.lin(Z(B),[(B.mul(x,y),2),(x,2),(y,.5)])]
# ---------------- 10 flows (Euler, dt = 2^-k) ----------------
def euler(B,s,d,dt): return [B.lin(a,[(b,dt)]) for a,b in zip(s,d)]
def lorenz(B,x,y,z):
    dt=2**-7; return [B.lin(x,[(B.sub(y,x),10*dt)]),
        B.lin(y,[(B.mul(x,B.sub(B.K(28.),z)),dt),(y,-dt)]),
        B.lin(z,[(B.mul(x,y),dt),(z,-8/3*dt)])]
def rossler(B,x,y,z):
    dt=2**-8; return [B.lin(x,[(y,-dt),(z,-dt)]), B.lin(y,[(x,dt),(y,.2*dt)]),
        B.lin(z,[(B.mul(z,B.sub(x,B.K(5.7))),dt)],.2*dt)]
def chua(B,x,y,z):
    dt=2**-7; a=15.6; m0,m1=-8/7,-5/7
    return [B.lin(x,[(x,-dt*a*(1+m1)),(y,dt*a),(B.sat(x),-dt*a*(m0-m1))]),
            B.lin(y,[(x,dt),(y,-dt),(z,dt)]), B.lin(z,[(y,-28*dt)])]
def chen(B,x,y,z):
    dt=2**-9; return [B.lin(x,[(B.sub(y,x),35*dt)]),
        B.lin(y,[(x,-7*dt),(B.mul(x,z),-dt),(y,28*dt)]),
        B.lin(z,[(B.mul(x,y),dt),(z,-3*dt)])]
def lu(B,x,y,z):
    dt=2**-9; return [B.lin(x,[(B.sub(y,x),36*dt)]),
        B.lin(y,[(B.mul(x,z),-dt),(y,20*dt)]),
        B.lin(z,[(B.mul(x,y),dt),(z,-3*dt)])]
def halvorsen(B,x,y,z):
    dt=2**-9; a=1.4
    return [B.lin(x,[(x,-a*dt),(y,-4*dt),(z,-4*dt),(B.mul(y,y),-dt)]),
            B.lin(y,[(y,-a*dt),(z,-4*dt),(x,-4*dt),(B.mul(z,z),-dt)]),
            B.lin(z,[(z,-a*dt),(x,-4*dt),(y,-4*dt),(B.mul(x,x),-dt)])]
def rikitake(B,x,y,z):
    dt=2**-8; return [B.lin(x,[(x,-2*dt),(B.mul(y,z),dt)]),
        B.lin(y,[(y,-2*dt),(B.mul(B.sub(z,B.K(5.)),x),dt)]),
        B.lin(z,[(B.mul(x,y),-dt)],dt)]
def arneodo(B,x,y,z):
    dt=2**-8; return [B.lin(x,[(y,dt)]), B.lin(y,[(z,dt)]),
        B.lin(z,[(x,5.5*dt),(y,-3.5*dt),(z,-dt),(B.mul(B.mul(x,x),x),-dt)])]
def shimizu(B,x,y,z):
    dt=2**-7; return [B.lin(x,[(y,dt)]),
        B.lin(y,[(B.mul(B.sub(B.K(1.),z),x),dt),(y,-.75*dt)]),
        B.lin(z,[(z,-.45*dt),(B.mul(x,x),dt)])]
def sprott_jerk(B,x,y,z):
    dt=2**-6; return [B.lin(x,[(y,dt)]), B.lin(y,[(z,dt)]),
        B.lin(z,[(z,-.6*dt),(y,-dt),(B.abs(x),dt)],-dt)]

# name, fn, integer bits, initial state, kind
SYSTEMS=[
 ("Logistic (r=3.9375)",logistic,2,(0.3,),"map"),
 ("Tent (mu=1.99)",tent,2,(0.3,),"map"),
 ("Bernoulli / dyadic",bernoulli,2,(0.3,),"map"),
 ("Henon",henon,3,(0.1,0.1),"map"),
 ("Lozi (a=1.75)",lozi,3,(0.1,0.1),"map"),
 ("Arnold's cat",cat,2,(0.3,0.7),"map"),
 ("Baker's",baker,2,(0.3,0.7),"map"),
 ("Gingerbreadman",gingerbread,5,(-0.1,0.0),"map"),
 ("Duffing map",duffing_map,5,(0.1,0.1),"map"),
 ("Tinkerbell",tinkerbell,3,(-0.72,-0.64),"map"),
 ("Lorenz",lorenz,12,(1,1,1),"flow"),
 ("Rossler",rossler,10,(1,1,0),"flow"),
 ("Chua",chua,4,(0.7,0,0),"flow"),
 ("Chen",chen,13,(-10,0,37),"flow"),
 ("Lu",lu,12,(1,1,1),"flow"),
 ("Halvorsen",halvorsen,10,(-1.48,-1.51,2.04),"flow"),
 ("Rikitake",rikitake,8,(1,0,0.5),"flow"),
 ("Arneodo",arneodo,8,(0.2,0.2,-0.75),"flow"),
 ("Shimizu-Morioka",shimizu,4,(0.1,0,0),"flow"),
 ("Sprott jerk circuit",sprott_jerk,4,(0.1,0,0),"flow"),
]

def build(fn,W,I,nv,digits=None):
    B=BitB(W,I,digits); st=[[(chr(97+v),i) for i in range(W)] for v in range(nv)]
    outs=fn(B,*st); return B,outs

def compile_net(B,outs,nv):
    """Turn the netlist into one Python function on bit lists (fast simulation)."""
    def r(a):
        if a in (0,1): return str(a)
        return f"v{a[1]}" if a[0]=='n' else f"{a[0]}[{a[1]}]"
    L=[f"def step({','.join(chr(97+v) for v in range(nv))}):"]
    for i,(op,a,b) in enumerate(B.g.ops):
        e = f"1-{r(a)}" if op=='NOT' else f"{r(a)}{ {'AND':'&','OR':'|','XOR':'^'}[op] }{r(b)}"
        L.append(f" v{i}={e}")
    L.append(" return ["+",".join("["+",".join(r(b) for b in o)+"]" for o in outs)+"]")
    ns={}; exec("\n".join(L),ns); return ns['step']
