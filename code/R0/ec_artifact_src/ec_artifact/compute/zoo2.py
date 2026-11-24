# Additional systems from Wikipedia's "List of chaotic maps" with standard equations.
# Maps return the next state; flows return per-variable (terms, const) derivatives,
# integrated with Euler at dt = 2^-k (dt folded into the constants).
import math
TWO_PI=2*math.pi
def Z(B): return B.K(0.)
def M(B,a,b): return B.mul(a,b)

MAPS = {}
def mp(name,ic,uses=""):
    def d(f): MAPS[name]=(f,ic,uses); return f
    return d

@mp("2D Lorenz map (a=1.25,b=0.75)",(0.1,0.1))
def _(B,x,y): a,b=1.25,.75; return [B.lin(Z(B),[(x,1+a*b),(M(B,x,y),-b)]), B.lin(Z(B),[(y,1-b),(M(B,x,x),b)])]
@mp("Bogdanov (k=1.2)",(0.1,0.01))
def _(B,x,y):
    yn=B.lin(y,[(M(B,x,B.sub(x,B.K(1.))),1.2)]); return [B.add(x,yn),yn]
@mp("Chialvo neuron",(0.5,0.5),"exp")
def _(B,x,y): return [B.add(M(B,M(B,x,x),B.exp(B.sub(y,x))),B.K(.03)), B.lin(Z(B),[(y,.89),(x,-.6)],.28)]
@mp("Circle map (K=3, Omega=0.1)",(0.3,),"sin")
def _(B,t): return [B.frac(B.lin(t,[(B.sin_turn(t),-3/TWO_PI)],.1))]
@mp("Complex quadratic (c=-2)",(0.3,0.0))
def _(B,x,y): return [B.lin(Z(B),[(M(B,x,x),1),(M(B,y,y),-1)],-2.), B.lin(Z(B),[(M(B,x,y),2)])]
@mp("Complex squaring (on unit circle)",(math.cos(1),math.sin(1)))
def _(B,x,y): return [B.lin(Z(B),[(M(B,x,x),1),(M(B,y,y),-1)]), B.lin(Z(B),[(M(B,x,y),2)])]
@mp("Clifford",(0.1,0.1),"sin")
def _(B,x,y): a,b,c,d=-1.4,1.6,1.0,0.7; return [B.lin(B.sin(B.lin(Z(B),[(y,a)])),[(B.cos(B.lin(Z(B),[(x,a)])),c)]), B.lin(B.sin(B.lin(Z(B),[(x,b)])),[(B.cos(B.lin(Z(B),[(y,b)])),d)])]
@mp("De Jong",(0.1,0.1),"sin")
def _(B,x,y): a,b,c,d=1.641,1.902,0.316,1.525; return [B.sub(B.sin(B.lin(Z(B),[(y,a)])),B.cos(B.lin(Z(B),[(x,b)]))), B.sub(B.sin(B.lin(Z(B),[(x,c)])),B.cos(B.lin(Z(B),[(y,d)])))]
@mp("Delayed logistic (a=2.27)",(0.5,0.4))
def _(B,x,y): return [B.lin(Z(B),[(M(B,x,B.sub(B.K(1.),y)),2.27)]), x]
@mp("Fractal-Dream",(0.1,0.1),"sin")
def _(B,x,y): a,b,c,d=-0.966918,2.879879,0.765145,0.744728; return [B.lin(B.sin(B.lin(Z(B),[(y,b)])),[(B.sin(B.lin(Z(B),[(x,b)])),c)]), B.lin(B.sin(B.lin(Z(B),[(x,a)])),[(B.sin(B.lin(Z(B),[(y,a)])),d)])]
@mp("Gauss (alpha=4.9, beta=-0.5)",(0.1,),"exp")
def _(B,x): return [B.add(B.exp(B.lin(Z(B),[(M(B,x,x),-4.9)])),B.K(-.5))]
@mp("Gumowski-Mira (mu=-0.7)",(0.1,0.1),"div")
def _(B,x,y):
    mu,a=-0.7,0.008
    f=lambda u: B.lin(Z(B),[(u,mu),(B.div(M(B,u,u),B.add(B.K(1.),M(B,u,u))),2*(1-mu))])
    xn=B.add(B.lin(y,[(B.lin(y,[(M(B,M(B,y,y),y),-.05)]),a)]),f(x))
    return [xn, B.sub(f(xn),x)]
@mp("Hopalong (a=7.17,b=8.44,c=2.56)",(0.1,0.1),"sqrt")
def _(B,x,y): return [B.sub(y,M(B,B.sign(x),B.sqrt(B.abs(B.lin(Z(B),[(x,8.44)],-2.56))))), B.sub(B.K(7.17),x)]
@mp("Ikeda (u=0.9)",(0.1,0.1),"sin,div")
def _(B,x,y):
    t=B.sub(B.K(.4),B.div(B.K(6.),B.add(B.K(1.),B.add(M(B,x,x),M(B,y,y)))))
    c,s=B.cos(t),B.sin(t)
    return [B.lin(Z(B),[(B.sub(M(B,x,c),M(B,y,s)),.9)],1.), B.lin(Z(B),[(B.add(M(B,x,s),M(B,y,c)),.9)])]
@mp("Kaplan-Yorke (alpha=0.2)",(0.3,0.1),"sin")
def _(B,x,y): return [B.frac(B.shl(x,1)), B.lin(B.cos_turn(B.shl(x,1)),[(y,.2)])]
@mp("Pomeau-Manneville type I (x+x^2 mod 1)",(0.3,))
def _(B,x): return [B.frac(B.add(x,M(B,x,x)))]
@mp("Standard map (K=5)",(0.1,0.2),"sin")
def _(B,th,p):                     # both in turns (angle/2pi), on the torus
    pn=B.frac(B.lin(p,[(B.sin_turn(th),5/TWO_PI)])); return [B.frac(B.add(th,pn)),pn]
@mp("Zaslavskii (r=3, nu=400/3, eps=0.3)",(0.3,0.1),"sin,exp")
def _(B,x,y):
    r,nu,eps=3.,400/3,.3; mu=(1-math.exp(-r))/r; c=B.cos_turn(x)
    return [B.frac(B.lin(x,[(y,nu*mu),(c,eps*nu*mu)],nu)), B.lin(Z(B),[(y,math.exp(-r)),(c,eps*math.exp(-r))])]
@mp("Zeraoulia-Sprott (a=3.3,b=0.3)",(0.1,0.1),"div")
def _(B,x,y): return [B.lin(Z(B),[(B.div(x,B.add(B.K(1.),M(B,y,y))),-3.3)]), B.lin(x,[(y,.3)])]

FLOWS = {}
def fl(name,ic,dt,uses=""):
    def d(f): FLOWS[name]=(f,ic,dt,uses); return f
    return d
@fl("Aizawa",(0.1,0,0),2**-7)
def _(B,x,y,z):
    a,b,c,d,e,f=.95,.7,.6,3.5,.25,.1; zb=B.sub(z,B.K(b)); r2=B.add(M(B,x,x),M(B,y,y))
    return [([(M(B,zb,x),1),(y,-d)],0),([(x,d),(M(B,zb,y),1)],0),
            ([(z,a),(M(B,M(B,z,z),z),-1/3),(r2,-1),(M(B,r2,z),-e),(M(B,z,M(B,x,M(B,x,x))),f)],c)]
@fl("Burke-Shaw",(0.6,0,0),2**-9)
def _(B,x,y,z): s,v=10.,4.272; return [([(x,-s),(y,-s)],0),([(y,-1),(M(B,x,z),-s)],0),([(M(B,x,y),s)],v)]
@fl("Chen-Lee",(1,1,1),2**-10)
def _(B,x,y,z): return [([(x,5.),(M(B,y,z),-1)],0),([(y,-10.),(M(B,x,z),1)],0),([(z,-.38),(M(B,x,y),1/3)],0)]
@fl("Duffing oscillator (forced)",(0.1,0,0),2**-7,"sin")
def _(B,x,v,ph):    # x''+0.3x'-x+x^3 = 0.5 cos(1.2 t); ph = phase in turns
    return [([(v,1)],0),([(v,-.3),(x,1),(M(B,M(B,x,x),x),-1),(B.cos_turn(ph),.5)],0),"PHASE:%r"%(1.2/TWO_PI)]
@fl("Finance (a=0.001,b=0.2,c=1.1)",(0.1,4,0.5),2**-7)
def _(B,x,y,z): return [([(z,1),(M(B,B.sub(y,B.K(.001)),x),1)],0),([(y,-.2),(M(B,x,x),-1)],1.),([(x,-1),(z,-1.1)],0)]
@fl("Genesio-Tesi",(0.1,0.1,0.1),2**-7)
def _(B,x,y,z): return [([(y,1)],0),([(z,1)],0),([(x,-1),(y,-1.1),(z,-.44),(M(B,x,x),1)],0)]
@fl("Hadley circulation",(0,0,1.3),2**-9)
def _(B,x,y,z): a,b,F,G=.25,4.,8.,1.; return [([(M(B,y,y),-1),(M(B,z,z),-1),(x,-a)],a*F),([(M(B,x,y),1),(M(B,x,z),-b),(y,-1)],G),([(M(B,x,y),b),(M(B,x,z),1),(z,-1)],0)]
@fl("Hindmarsh-Rose",(-1.3,-7.3,3.1),2**-7)
def _(B,x,y,z): return [([(y,1),(M(B,M(B,x,x),x),-1),(M(B,x,x),3),(z,-1)],3.25),([(M(B,x,x),-5),(y,-1)],1.),([(x,.024),(z,-.006)],.0384)]
@fl("Hyper-Rossler (4D)",(-10,-6,0,10),2**-8)
def _(B,x,y,z,w): return [([(y,-1),(z,-1)],0),([(x,1),(y,.25),(w,1)],0),([(M(B,x,z),1)],3.),([(z,-.5),(w,.05)],0)]
@fl("Hyper-Lorenz (4D)",(1,1,1,1),2**-9)
def _(B,x,y,z,w): return [([(y,10),(x,-10),(w,1)],0),([(x,28),(y,-1),(M(B,x,z),-1)],0),([(M(B,x,y),1),(z,-8/3)],0),([(M(B,y,z),-1),(w,-1)],0)]
@fl("Hyper-Lu (4D)",(1,1,1,1),2**-9)
def _(B,x,y,z,w): return [([(y,36),(x,-36),(w,1)],0),([(M(B,x,z),-1),(y,20)],0),([(M(B,x,y),1),(z,-3)],0),([(M(B,x,z),1),(w,1.3)],0)]
@fl("Hyperchaotic Chen (4D)",(1,1,1,1),2**-10)
def _(B,x,y,z,w): return [([(y,35),(x,-35),(w,1)],0),([(x,7),(M(B,x,z),-1),(y,12)],0),([(M(B,x,y),1),(z,-3)],0),([(M(B,y,z),1),(w,.5)],0)]
@fl("Lorenz 96 (N=5, F=8)",(8.01,8,8,8,8),2**-8)
def _(B,*x):
    N=len(x); return [([(M(B,B.sub(x[(i+1)%N],x[i-2]),x[i-1]),1),(x[i],-1)],8.) for i in range(N)]
@fl("Moore-Spiegel (T=6,R=20)",(0.1,0,0),2**-9)
def _(B,x,y,z): return [([(y,1)],0),([(z,1)],0),([(z,-1),(y,14.),(M(B,M(B,x,x),y),-20),(x,-6)],0)]
@fl("Newton-Leipnik",(0.349,0,-0.16),2**-8)
def _(B,x,y,z): return [([(x,-.4),(y,1),(M(B,y,z),10)],0),([(x,-1),(y,-.4),(M(B,x,z),5)],0),([(z,.175),(M(B,x,y),-5)],0)]
@fl("Rayleigh-Benard",(0.1,0,0),2**-8)
def _(B,x,y,z): return [([(x,-9),(y,9)],0),([(x,12),(y,-1),(M(B,x,z),-1)],0),([(M(B,x,y),1),(z,-5)],0)]
@fl("Rucklidge",(1,0,4.5),2**-7)
def _(B,x,y,z): return [([(x,-2),(y,6.7),(M(B,y,z),-1)],0),([(x,1)],0),([(z,-1),(M(B,y,y),1)],0)]
@fl("Sakarya",(1,-1,1),2**-8)
def _(B,x,y,z): return [([(x,-1),(y,1),(M(B,y,z),1)],0),([(x,-1),(y,-1),(M(B,x,z),.4)],0),([(z,1),(M(B,x,y),-.3)],0)]
SL={ # Sprott (1994) cases A-S
 "A":lambda B,x,y,z:[([(y,1)],0),([(x,-1),(M(B,y,z),1)],0),([(M(B,y,y),-1)],1.)],
 "B":lambda B,x,y,z:[([(M(B,y,z),1)],0),([(x,1),(y,-1)],0),([(M(B,x,y),-1)],1.)],
 "C":lambda B,x,y,z:[([(M(B,y,z),1)],0),([(x,1),(y,-1)],0),([(M(B,x,x),-1)],1.)],
 "D":lambda B,x,y,z:[([(y,-1)],0),([(x,1),(z,1)],0),([(M(B,x,z),1),(M(B,y,y),3)],0)],
 "E":lambda B,x,y,z:[([(M(B,y,z),1)],0),([(M(B,x,x),1),(y,-1)],0),([(x,-4)],1.)],
 "F":lambda B,x,y,z:[([(y,1),(z,1)],0),([(x,-1),(y,.5)],0),([(M(B,x,x),1),(z,-1)],0)],
 "G":lambda B,x,y,z:[([(x,.4),(z,1)],0),([(M(B,x,z),1),(y,-1)],0),([(x,-1),(y,1)],0)],
 "H":lambda B,x,y,z:[([(y,-1),(M(B,z,z),1)],0),([(x,1),(y,.5)],0),([(x,1),(z,-1)],0)],
 "I":lambda B,x,y,z:[([(y,-.2)],0),([(x,1),(z,1)],0),([(x,1),(M(B,y,y),1),(z,-1)],0)],
 "J":lambda B,x,y,z:[([(z,2)],0),([(y,-2),(z,1)],0),([(x,-1),(y,1),(M(B,y,y),1)],0)],
 "K":lambda B,x,y,z:[([(M(B,x,y),1),(z,-1)],0),([(x,1),(y,-1)],0),([(x,1),(z,.3)],0)],
 "L":lambda B,x,y,z:[([(y,1),(z,3.9)],0),([(M(B,x,x),.9),(y,-1)],0),([(x,-1)],1.)],
 "M":lambda B,x,y,z:[([(z,-1)],0),([(M(B,x,x),-1),(y,-1)],0),([(x,1.7),(y,1)],1.7)],
 "N":lambda B,x,y,z:[([(y,-2)],0),([(x,1),(M(B,z,z),1)],0),([(y,1),(z,-2)],1.)],
 "O":lambda B,x,y,z:[([(y,1)],0),([(x,1),(z,-1)],0),([(x,1),(M(B,x,z),1),(y,2.7)],0)],
 "P":lambda B,x,y,z:[([(y,2.7),(z,1)],0),([(x,-1),(M(B,y,y),1)],0),([(x,1),(y,1)],0)],
 "Q":lambda B,x,y,z:[([(z,-1)],0),([(x,1),(y,-1)],0),([(x,3.1),(M(B,y,y),1),(z,.5)],0)],
 "R":lambda B,x,y,z:[([(y,-1)],.9),([(z,1)],.4),([(M(B,x,y),1),(z,-1)],0)],
 "S":lambda B,x,y,z:[([(x,-1),(y,-4)],0),([(x,1),(M(B,z,z),1)],0),([(x,1)],1.)],
}
SL_IC={"A":(0,5,0),"B":(.05,.05,.05),"C":(.05,.05,.05),"D":(0,.8,0),"E":(1,0,0),"F":(.05,.05,.05),"G":(.05,.05,.05),
 "H":(.05,.05,.05),"I":(.05,.05,.05),"J":(2,2,0),"K":(.05,.05,.05),"L":(.05,.05,.05),"M":(.05,.05,.05),
 "N":(.05,.05,.05),"O":(.05,.05,.05),"P":(.05,.05,.05),"Q":(.05,.05,.05),"R":(.05,.05,.05),"S":(.05,.05,.05)}
SL_IC.update({"M":(0,0,0),"Q":(0,0,0)})
SL_DT={"A":2**-9,"M":2**-9,"Q":2**-9,"S":2**-9}
for k,f in SL.items(): FLOWS["Sprott-Linz "+k+(" (Nose-Hoover)" if k=="A" else "")]=(f,SL_IC[k],SL_DT.get(k,2**-7),"")
@fl("Thomas (b=0.208186)",(0.1,0,-0.1),2**-6,"sin")
def _(B,x,y,z): b=.208186; return [([(B.sin(y),1),(x,-b)],0),([(B.sin(z),1),(y,-b)],0),([(B.sin(x),1),(z,-b)],0)]
@fl("Ueda oscillator",(2.5,0,0),2**-8,"sin")
def _(B,x,v,ph): return [([(v,1)],0),([(v,-.05),(M(B,M(B,x,x),x),-1),(B.cos_turn(ph),7.5)],0),"PHASE:%r"%(1/TWO_PI)]
@fl("Van der Pol (forced, mu=8.53)",(0.1,0,0),2**-9,"sin")
def _(B,x,v,ph): return [([(v,1)],0),([(v,8.53),(M(B,M(B,x,x),v),-8.53),(x,-1),(B.cos_turn(ph),1.2)],0),"PHASE:%r"%(0.1)]
@fl("WINDMI (a=0.7,b=2.5)",(0,0.8,0),2**-9,"exp")
def _(B,x,y,z): return [([(y,1)],0),([(z,1)],0),([(z,-.7),(y,-1),(B.exp(x),-1)],2.5)]

def flow_step(name):
    f,ic,dt,uses=FLOWS[name]
    def step(B,*s):
        d=f(B,*s); out=[]
        for i,v in enumerate(s):
            di=d[i]
            if isinstance(di,str):                        # phase variable for forcing
                out.append(B.frac(B.add(v,B.K(float(di.split(':')[1])*dt))))
            else:
                terms,c=di; out.append(B.lin(v,[(t,cf*dt) for t,cf in terms],c*dt))
        return out
    return step
def all_systems():
    S=[(n,f,ic,"map",1,u) for n,(f,ic,u) in MAPS.items()]
    S+=[(n,flow_step(n),ic,"flow",dt,u) for n,(f,ic,dt,u) in FLOWS.items()]
    return S

# Listed on Wikipedia but NOT chaotic (or unstable) with the standard parameters tried here:
EXCLUDED=["Bogdanov (k=1.2)","Chialvo neuron","Zeraoulia-Sprott (a=3.3,b=0.3)","Complex squaring (on unit circle)",
 "Duffing oscillator (forced)","Rayleigh-Benard","Van der Pol (forced, mu=8.53)","Hindmarsh-Rose","Sprott-Linz D"]
_all=all_systems
def all_systems(): return [s for s in _all() if s[0] not in EXCLUDED]

@mp("Sine map (mu=0.99)",(0.3,),"sin")
def _(B,x): return [B.lin(Z(B),[(B.sin_turn(B.asr(x,1)),.99)])]
