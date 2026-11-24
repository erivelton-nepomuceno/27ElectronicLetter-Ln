import numpy as np, json, math, os, time, signal, zoo, zoo2, ext, mdcs_gate, tune
import energy_fn as EA
from rk4_all import OLD, FX, rk4, flows
EA.n=64; EA.ITERS=100; n=64
res=json.load(open('res2.json')); R4=json.load(open('rk4_all.json'))
out=json.load(open('e64.json')) if os.path.exists('e64.json') else {}
class TO(Exception): pass
signal.signal(signal.SIGALRM,lambda *a:(_ for _ in ()).throw(TO()))
def bits_of(s,I): F=n-I; return np.array([((round(x*(1<<F))&((1<<n)-1))>>i)&1 for x in s for i in range(n)],dtype=np.uint8)
def run(key,build,ic,I,stepF,warm):
    if key in out: return
    signal.alarm(600); t0=time.time()
    try:
        s=list(ic); F=FX()
        for k in range(warm): s=stepF(F,*s)
        B,o,nv=build()
        e=EA.energy(B.g,o,nv,bits_of(s,I)); out[key]=e['pj_bit']
    except TO: out[key]=None
    signal.alarm(0); json.dump(out,open('e64.json','w')); print(key,out[key],f"{time.time()-t0:.0f}s",flush=True)
# maps and Euler flows from zoo
for name,fn,I,ic,kind in zoo.SYSTEMS:
    run("E|"+name,lambda fn=fn,I=I,ic=ic:(lambda B:(B,fn(B,*[[(chr(97+v),i) for i in range(n)] for v in range(len(ic))]),len(ic)))(ext.BitX(n,I)),ic,I,fn,2000 if kind=="map" else 20000)
for name,fn,ic,kind,dt,u in zoo2.all_systems():
    I=res[name]['I']
    run("E|"+name,lambda fn=fn,I=I,ic=ic:(lambda B:(B,fn(B,*[[(chr(97+v),i) for i in range(n)] for v in range(len(ic))]),len(ic)))(ext.BitX(n,I)),ic,I,fn,2000 if kind=="map" else 20000)
# MDCS
if "E|MDCS" not in out:
    g,o=mdcs_gate.build(n,2,5); x=0.3
    for k in range(2000): x=4*x*(1-2**-32-x)
    out["E|MDCS"]=EA.energy(g,o,1,np.array([(int(x*2**n)>>i)&1 for i in range(n)],dtype=np.uint8))['pj_bit']; json.dump(out,open('e64.json','w'))
# RK4
for name,der,ic,dte,u in flows():
    r=R4.get(name)
    if not r or r.get('timeout'): continue
    st=rk4(der,r['dt']); I=r['I']
    run("R|"+name,lambda st=st,I=I,ic=ic:(lambda B:(B,st(B,*[[(chr(97+v),i) for i in range(n)] for v in range(len(ic))]),len(ic)))(ext.BitX(n,I)),ic,I,st,int(30/r['dt']))
print("DONE",flush=True)
