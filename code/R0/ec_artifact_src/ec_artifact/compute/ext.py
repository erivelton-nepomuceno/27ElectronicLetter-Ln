# Extended backends: sin, cos, exp, division, sqrt, sign, signed frac - float and gate level.
import math, zoo
from zoo import FloatB, BitB

class FloatX(FloatB):
    def __init__(s): s.mx=0.0
    def _r(s,v):
        if abs(v)>s.mx: s.mx=abs(v)
        return v
    def add(s,a,b): return s._r(a+b)
    def sub(s,a,b): return s._r(a-b)
    def mul(s,a,b): return s._r(a*b)
    def lin(s,acc,terms,const=0.0): return s._r(acc+const+sum(c*v for v,c in terms))
    def sin(s,a): return math.sin(a)
    def cos(s,a): return math.cos(a)
    def sin_turn(s,t): return math.sin(2*math.pi*t)
    def cos_turn(s,t): return math.cos(2*math.pi*t)
    def exp(s,a): return s._r(math.exp(a))
    def div(s,a,b): return s._r(a/b)
    def sqrt(s,a): return math.sqrt(a)
    def sign(s,a): return 1.0 if a>=0 else -1.0
    def frac(s,a): return a%1.0

class BitX(BitB):
    def mux(s,c,A,B):            # c ? B : A
        g=s.g; nc=g.NOT(c); return [g.OR(g.AND(nc,a),g.AND(c,b)) for a,b in zip(A,B)]
    def _sub_w(s,A,B):           # A-B and "no borrow" flag (A>=B), unsigned equal widths
        g=s.g;o=[];c=1
        for a,b in zip(A,B):
            nb=g.NOT(b); x=g.XOR(a,nb); o.append(g.XOR(x,c)); c=g.OR(g.AND(a,nb),g.AND(x,c))
        return o,c
    def sign(s,A): return [0]*s.F+[1]+[A[-1]]*(s.I-1)        # +1 / -1: pure wiring
    def _poly(s,x,coefs):        # Horner: coefs[0]+x*(coefs[1]+...)
        r=s.K(coefs[-1])
        for c in reversed(coefs[:-1]): r=s.add(s.mul(r,x),s.K(c))
        return r
    def sin_turn(s,T):           # sin(2*pi*t), t in turns
        g=s.g; F=s.F
        t=T[:F]+[T[F-1]]*s.I                                  # signed frac in [-0.5,0.5)
        a=s.abs(t); cond=a[F-2]
        v=s.mux(cond,a,s.sub(s.K(.5),a))                      # fold to [0,0.25]
        u=s.shl(v,2); w=s.mul(u,u)                            # u in [0,1]
        K=0
        while (math.pi/2)**(2*K+3)/math.factorial(2*K+3) >= 2.0**-(F+1): K+=1
        co=[(-1)**m*(math.pi/2)**(2*m+1)/math.factorial(2*m+1) for m in range(K+1)]
        r=s.mul(s._poly(w,co),u)
        return [g.XOR(b,t[-1]) for b in r]
    def cos_turn(s,T): return s.sin_turn(s.add(T,s.K(.25)))
    def sin(s,A): return s.sin_turn(s.lin(s.K(0.),[(A,1/(2*math.pi))]))
    def cos(s,A): return s.cos_turn(s.lin(s.K(0.),[(A,1/(2*math.pi))]))
    def exp(s,A):
        g=s.g; F,W,I=s.F,s.W,s.I
        y=s.lin(s.K(0.),[(A,1/math.log(2))])
        f=y[:F]+[0]*I; k=y[F:]                                 # y = k + f
        K=0
        while math.log(2)**(K+1)/math.factorial(K+1) >= 2.0**-(F+1): K+=1
        p=s._poly(f,[math.log(2)**j/math.factorial(j) for j in range(K+1)])   # 2^f
        R=F; m=max(2*R,1).bit_length()+1
        kk=k+[k[-1]]*(m-len(k)); Rb=[(R>>i)&1 for i in range(m)]
        sh=s._add(kk,Rb)                                       # s = k + R >= 0
        wide=p+[p[-1]]*(2*R)
        for j in range(m-1):
            moved=[0]*(1<<j)+wide[:len(wide)-(1<<j)]
            wide=s.mux(sh[j],wide,moved)
        return wide[R:R+W]
    def div(s,A,B):
        g=s.g; W,F=s.W,s.F; sg=g.XOR(A[-1],B[-1])
        a=s.abs(A); b=s.abs(B); WR=W+2; D=b+[0]*(WR-W)
        N2=lambda i: (a[i-F] if 0<=i-F<W else 0)
        R=[N2(W+j) for j in range(F)]; R=(R+[0]*WR)[:WR]
        q=[0]*W
        for i in range(W-1,-1,-1):
            R=[N2(i)]+R[:-1]
            T,ok=s._sub_w(R,D); q[i]=ok; R=s.mux(ok,R,T)
        return [g.XOR(x,sg) for x in q]
    def sqrt(s,A):
        g=s.g; W,F=s.W,s.F; a=A
        bits=[0]*F+a; L=len(bits)+(len(bits)&1); bits+= [0]*(L-len(bits))
        h=L//2; WR=h+3; rem=[0]*WR; root=[0]*h
        for i in range(h-1,-1,-1):
            rem=[bits[2*i],bits[2*i+1]]+rem[:-2]
            trial=([1,0]+root+[0]*WR)[:WR]
            T,ok=s._sub_w(rem,trial); rem=s.mux(ok,rem,T); root=[ok]+root[:-1]
        return (root+[0]*W)[:W]
