import math, json, os, time, signal, numpy as np, ext, zoo2, mdcs, tune
import energy_fn as EA
M=lambda B,a,b: B.mul(a,b)
OLD={ # derivative forms of the original 10 flows: (deriv, ic, Euler dt, uses)
 "Lorenz":(lambda B,x,y,z:[([(B.sub(y,x),10.)],0),([(M(B,x,B.sub(B.K(28.),z)),1),(y,-1)],0),([(M(B,x,y),1),(z,-8/3)],0)],(1,1,1),2**-7,""),
 "Rossler":(lambda B,x,y,z:[([(y,-1),(z,-1)],0),([(x,1),(y,.2)],0),([(M(B,z,B.sub(x,B.K(5.7))),1)],.2)],(1,1,0),2**-8,""),
 "Chua":(lambda B,x,y,z:[([(x,-15.6*(2/7)),(y,15.6),(B.sat(x),15.6*3/7)],0),([(x,1),(y,-1),(z,1)],0),([(y,-28)],0)],(0.7,0,0),2**-7,""),
 "Chen":(lambda B,x,y,z:[([(B.sub(y,x),35.)],0),([(x,-7),(M(B,x,z),-1),(y,28)],0),([(M(B,x,y),1),(z,-3)],0)],(-10,0,37),2**-9,""),
 "Lu":(lambda B,x,y,z:[([(B.sub(y,x),36.)],0),([(M(B,x,z),-1),(y,20)],0),([(M(B,x,y),1),(z,-3)],0)],(1,1,1),2**-9,""),
 "Halvorsen":(lambda B,x,y,z:[([(x,-1.4),(y,-4),(z,-4),(M(B,y,y),-1)],0),([(y,-1.4),(z,-4),(x,-4),(M(B,z,z),-1)],0),([(z,-1.4),(x,-4),(y,-4),(M(B,x,x),-1)],0)],(-1.48,-1.51,2.04),2**-9,""),
 "Rikitake":(lambda B,x,y,z:[([(x,-2),(M(B,y,z),1)],0),([(y,-2),(M(B,B.sub(z,B.K(5.)),x),1)],0),([(M(B,x,y),-1)],1.)],(1,0,0.5),2**-8,""),
 "Arneodo":(lambda B,x,y,z:[([(y,1)],0),([(z,1)],0),([(x,5.5),(y,-3.5),(z,-1),(M(B,M(B,x,x),x),-1)],0)],(0.2,0.2,-0.75),2**-8,""),
 "Shimizu-Morioka":(lambda B,x,y,z:[([(y,1)],0),([(M(B,B.sub(B.K(1.),z),x),1),(y,-.75)],0),([(z,-.45),(M(B,x,x),1)],0)],(0.1,0,0),2**-7,""),
 "Sprott jerk circuit":(lambda B,x,y,z:[([(y,1)],0),([(z,1)],0),([(z,-.6),(y,-1),(B.abs(x),1)],-1.)],(0.1,0,0),2**-6,""),
}
class FX(ext.FloatX):
    def sat(s,a): return max(-1.,min(1.,a))
def flows():
    for k,(d,ic,dt,u) in OLD.items(): yield k,d,ic,dt,u
    for k,(d,ic,dt,u) in zoo2.FLOWS.items():
        if k in zoo2.EXCLUDED or k.startswith("Sprott-Linz Q"): continue
        yield k,d,ic,dt,u
def rk4(der,dt):
    def ev(B,s):
        out=[]
        for v,di in zip(s,der(B,*s)):
            if isinstance(di,str): out.append(B.K(float(di.split(':')[1])))
            else: t,c=di; out.append(B.lin(B.K(0.),t,c))
        return out
    def step(B,*s):
        k1=ev(B,s); s2=[B.lin(v,[(k,dt/2)]) for v,k in zip(s,k1)]
        k2=ev(B,s2); s3=[B.lin(v,[(k,dt/2)]) for v,k in zip(s,k2)]
        k3=ev(B,s3); s4=[B.lin(v,[(k,dt)]) for v,k in zip(s,k3)]
        k4=ev(B,s4); new=[B.lin(v,[(a,dt/6),(b,dt/3),(c,dt/3),(d,dt/6)]) for v,a,b,c,d in zip(s,k1,k2,k3,k4)]
        ph=[isinstance(di,str) for di in der(FX(),*[0.1]*len(s))]
        return [B.frac(w) if p else w for w,p in zip(new,ph)]
    return step
out=json.load(open('rk4_all.json')) if os.path.exists('rk4_all.json') else {}
class TO(Exception): pass
signal.signal(signal.SIGALRM,lambda *a:(_ for _ in ()).throw(TO()))
for name,der,ic,dte,u in flows():
    if name in out: continue
    signal.alarm(500); t0=time.time(); r={}
    try:
        for mult in (4,2,1):
            dt=dte*mult; step=rk4(der,dt); lam=tune.lyap(step,ic,int(min(100000,300/dt)),dt,tr=int(20/dt))
            if isinstance(lam,float) and lam>0.003: break
        F=FX(); s=list(ic)
        for k in range(int(min(100000,200/dt))): s=step(F,*s)
        I=max(3,math.ceil(math.log2(F.mx+1e-9))+2); nv=len(ic)
        L={}
        for n in [16,24,32,40,48,56,64]:
            if n<=I+2: continue
            B=ext.BitX(n,I); o=step(B,*[[(chr(97+v),i) for i in range(n)] for v in range(nv)]); L[n]=mdcs.live(B.g,o)
            if n==32: B32,o32=B,o
        xs=sorted(L); deg=3 if u and ('sin' in u or 'exp' in u) else 2
        pf=np.polyfit(xs,[L[n] for n in xs],deg); resid=float(max(abs(np.polyval(pf,xs)-[L[n] for n in xs])))
        for n in (128,256): L[n]=int(round(np.polyval(pf,n)))
        EA.n=32; F2=FX(); s=list(ic)
        for k in range(int(30/dt)): s=step(F2,*s)
        Fb=32-I; bits=np.array([((round(x*(1<<Fb))&((1<<32)-1))>>i)&1 for x in s for i in range(32)],dtype=np.uint8)
        e=EA.energy(B32.g,o32,nv,bits)
        r=dict(dt_euler=dte,dt=dt,lam=lam,I=I,L=L,fit=list(pf),resid=resid,pj=e['pj_bit'],alpha=e['alpha'],deg=deg)
    except TO: r=dict(timeout=True)
    signal.alarm(0); out[name]=r; json.dump(out,open('rk4_all.json','w'))
    print(name,{k:v for k,v in r.items() if k not in('fit',)},f"{time.time()-t0:.0f}s",flush=True)
print("DONE",flush=True)
