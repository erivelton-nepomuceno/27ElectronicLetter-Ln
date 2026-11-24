import numpy as np, json, math, zoo, zoo2, ext, mdcs_gate, vhdl_power as V, time
n=32; E_T=0.040; E_FF=0.010; ITERS=200
res=json.load(open('res2.json'))
def systems():
    for name,fn,I,ic,kind in zoo.SYSTEMS:
        yield name,fn,I,ic,kind,zoo.FloatB(),"zoo"
    for name,fn,ic,kind,dt,u in zoo2.all_systems():
        yield name,fn,res[name]['I'],ic,kind,ext.FloatX(),"zoo2"
def levelize(g,keep,NI,base,ref):
    lvl={}
    for k in keep:
        op,a,b=g.ops[k]; L=0
        for x in (a,b):
            if isinstance(x,tuple) and x[0]=='n': L=max(L,lvl[x[1]]+1)
        lvl[k]=L
    return lvl
def energy(g,outs,nv,bits0):
    keep=V.live_ops(g,outs); idx={k:i for i,k in enumerate(keep)}; NI=nv*n; base=NI+2
    def ref(a):
        if a==0: return NI
        if a==1: return NI+1
        if a[0]=='n': return base+idx[a[1]]
        return (ord(a[0])-97)*n+a[1]
    lv=levelize(g,keep,NI,base,ref); D=max(lv.values())+1 if lv else 0
    groups=[[] for _ in range(D)]
    for k in keep: groups[lv[k]].append(k)
    G=[]
    for grp in groups:
        o=np.array([{'AND':0,'OR':1,'XOR':2,'NOT':3}[g.ops[k][0]] for k in grp]); a=np.array([ref(g.ops[k][1]) for k in grp])
        b=np.array([ref(g.ops[k][2]) if g.ops[k][2] is not None else NI for k in grp]); d=np.array([base+idx[k] for k in grp])
        G.append((o,a,b,d))
    outidx=np.array([ref(x) for o in outs for x in o])
    v=np.zeros(base+len(keep),dtype=np.uint8); v[NI+1]=1; v[:NI]=bits0
    def ev():
        for o,a,b,d in G:
            x,y=v[a],v[b]; v[d]=np.where(o==0,x&y,np.where(o==1,x|y,np.where(o==2,x^y,1-x)))
    ev(); tog=np.zeros(len(keep))
    for it in range(ITERS):
        prev=v[base:].copy(); v[:NI]=v[outidx]; ev(); tog+=(v[base:]!=prev)
    roots=V.tech_map(g,outs,keep); rm=np.array([k in roots for k in keep]) if keep else np.array([],bool)
    lt=tog[rm].sum()/ITERS if keep else 0
    return dict(gates=len(keep),luts=int(rm.sum()),depth=D,alpha=float(tog.sum()/ITERS/max(1,len(keep))),lut_tog=float(lt),
                pj_bit=(lt*E_T+NI*E_FF)/NI,bits=NI)
out={}
for name,fn,I,ic,kind,FB,src in systems():
    t=time.time(); nv=len(ic); F=n-I
    s=list(ic)
    for k in range(2000 if kind=="map" else 20000):
        s=fn(FB,*s)
    if src=="zoo": B,o=zoo.build(fn,n,I,nv)
    else:
        B=ext.BitX(n,I); o=fn(B,*[[(chr(97+v),i) for i in range(n)] for v in range(nv)])
    bits=np.array([((round(x*(1<<F))&((1<<n)-1))>>i)&1 for x in s for i in range(n)],dtype=np.uint8)
    e=energy(B.g,o,nv,bits); out[name]=e
    print(f"{name:38s} gates={e['gates']} luts={e['luts']} alpha={e['alpha']:.2f} pJ/bit={e['pj_bit']:.3f} ({time.time()-t:.0f}s)",flush=True)
    json.dump(out,open('energy_all.json','w'))
# MDCS
g,o=mdcs_gate.build(n,2,5); x=0.3
for k in range(2000): x=4*x*(1-2**-32-x)
bits=np.array([(int(x*2**n)>>i)&1 for i in range(n)],dtype=np.uint8)
out["MDCS"]=energy(g,o,1,bits); json.dump(out,open('energy_all.json','w')); print("MDCS",out["MDCS"],flush=True)
print("ALLDONE",flush=True)
