import zoo2, ext, zoo, tune, mdcs, math, json, os, time, signal, numpy as np
out=json.load(open('res2.json')) if os.path.exists('res2.json') else {}
class TO(Exception): pass
def _h(*a): raise TO()
signal.signal(signal.SIGALRM,_h)
def auto_I(fn,ic,kind,dt,uses):
    F=ext.FloatX(); s=list(ic)
    for k in range(20000 if kind=="map" else int(min(200000,300/dt))): s=fn(F,*s)
    I=max(2,math.ceil(math.log2(F.mx+1e-9))+2)
    return max(I,3) if uses else I
def build(fn,n,I,nv):
    B=ext.BitX(n,I); st=[[(chr(97+v),i) for i in range(n)] for v in range(nv)]
    return B,fn(B,*st)
for name,fn,ic,kind,dt,uses in zoo2.all_systems():
    if name in out and not out[name].get('timeout'): continue
    signal.alarm(400); t0=time.time(); nv=len(ic); r={}
    try:
        r['lam']=tune.lyap(fn,ic,20000 if kind=="map" else int(min(200000,400/dt)),dt,tr=200 if kind=="map" else int(20/dt))
        I=auto_I(fn,ic,kind,dt,uses); r.update(kind=kind,I=I,dt=dt,uses=uses)
        L={}
        for n in [16,24,32,40,48,56,64]:
            if n>I+2: Bn,on=build(fn,n,I,nv); L[n]=mdcs.live(Bn.g,on)
        heavy=bool(uses); xs=sorted(L); ys=[L[n] for n in xs]
        pf=np.polyfit(xs,ys,3 if heavy else 2)
        for n in (128,256):
            if heavy: L[n]=int(round(np.polyval(pf,n)))
            else: Bn,on=build(fn,n,I,nv); L[n]=mdcs.live(Bn.g,on)
        r.update(L=L,fit=list(pf),resid=float(max(abs(np.polyval(pf,xs)-ys))),heavy=heavy)
        # gate-level check at 32 bits
        W=max(32,I+20); B,o=build(fn,W,I,nv); step=zoo.compile_net(B,o,nv)
        tof=lambda A:(sum(b<<i for i,b in enumerate(A))-((1<<W) if A[-1] else 0))/(1<<B.F)
        F=ext.FloatX(); s=[B.K(v) for v in ic]; p=list(ic); t=[list(v) for v in s]; t[0][B.F-12]^=1
        steps=2000 if kind=="map" else 15000; early=0; div=None; sc=1
        for k in range(steps):
            s=step(*s); t=step(*t); p=fn(F,*p); xs_=[tof(v) for v in s]; sc=max(sc,max(map(abs,xs_)))
            if k<(5 if kind=="map" else 200): early=max(early,max(abs(a-b) for a,b in zip(xs_,p)))
            if max(abs(tof(a)-tof(b)) for a,b in zip(s,t))>0.1*sc: div=k; break
        r.update(early=early,div=div)
    except TO: r['timeout']=True
    signal.alarm(0); out[name]=r; json.dump(out,open('res2.json','w'))
    print(name, 'TIMEOUT' if r.get('timeout') else f"I={r['I']} lam={r['lam']} L32={r['L'].get(32)} L64={r['L'].get(64)} div={r.get('div')} ({time.time()-t0:.0f}s)",flush=True)
print("ALLDONE",flush=True)
