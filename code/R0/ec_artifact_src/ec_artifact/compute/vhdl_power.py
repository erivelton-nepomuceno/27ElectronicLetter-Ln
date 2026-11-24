# Netlist -> structural VHDL, plus a simulation-based energy estimate.
import numpy as np, zoo, zoo2, ext, mdcs, mdcs_gate, os

def get(name, n=32):
    if name=="MDCS":
        g,o=mdcs_gate.build(n,2,5); return g,o,1
    if name=="Sine map":
        f=zoo2.MAPS["Sine map (mu=0.99)"][0]; B=ext.BitX(n,3)
        o=f(B,[('a',i) for i in range(n)]); return B.g,o,1
    tbl={s[0]:s for s in zoo.SYSTEMS}
    key={"Gingerbreadman":"Gingerbreadman","Lozi":"Lozi (a=1.75)","Lorenz":"Lorenz"}[name]
    _,fn,I,ic,_=tbl[key]; B,o=zoo.build(fn,n,I,len(ic)); return B.g,o,len(ic)

def live_ops(g,outs):
    keep=set(); st=[b for o in outs for b in o]
    while st:
        a=st.pop()
        if isinstance(a,tuple) and a[0]=='n' and a[1] not in keep:
            keep.add(a[1]); op,x,y=g.ops[a[1]]; st+=[x]+([y] if y is not None else [])
    return sorted(keep)

def to_vhdl(name,g,outs,nv,n):
    ent=name.lower().replace(' ','_')+f"_{n}"
    keep=live_ops(g,outs)
    def r(a):
        if a in (0,1): return f"'{a}'"
        return f"g{a[1]}" if a[0]=='n' else f"s_{a[0]}({a[1]})"
    L=["library ieee; use ieee.std_logic_1164.all;","",
       f"-- {name}: {len(keep)} two-input gates (AND/OR/XOR/NOT), {nv}x{n} state bits",
       f"entity {ent} is port(",
       "  clk, rst, load : in std_logic;"]
    L+= [f"  init_{chr(97+v)} : in std_logic_vector({n-1} downto 0);" for v in range(nv)]
    L+= [f"  q_{chr(97+v)}    : out std_logic_vector({n-1} downto 0){';' if v<nv-1 else ''}" for v in range(nv)]
    L+= [");",f"end entity;","",f"architecture gates of {ent} is"]
    L+= [f"  signal s_{chr(97+v)}, d_{chr(97+v)} : std_logic_vector({n-1} downto 0);" for v in range(nv)]
    for i in range(0,len(keep),16):
        L.append("  signal "+", ".join(f"g{k}" for k in keep[i:i+16])+" : std_logic;")
    L+=["begin"]
    for k in keep:
        op,a,b=g.ops[k]
        e=f"not {r(a)}" if op=='NOT' else f"{r(a)} {op.lower()} {r(b)}"
        L.append(f"  g{k} <= {e};")
    for v,o in enumerate(outs):
        c=chr(97+v)
        for i,bit in enumerate(o): L.append(f"  d_{c}({i}) <= {r(bit)};")
    L+=["  process(clk) begin","    if rising_edge(clk) then"]
    for v in range(nv):
        c=chr(97+v); L.append(f"      if load='1' then s_{c} <= init_{c}; else s_{c} <= d_{c}; end if;")
    L+=["    end if;","  end process;"]
    L+=[f"  q_{chr(97+v)} <= s_{chr(97+v)};" for v in range(nv)]
    L+=["end architecture;"]
    return ent,"\n".join(L)+"\n"

def tech_map(g,outs,keep,K=6):
    """Greedy K-LUT cone packing: returns set of gate ids that are LUT outputs."""
    fan={k:0 for k in keep}; outset=set()
    for k in keep:
        op,a,b=g.ops[k]
        for x in (a,b):
            if isinstance(x,tuple) and x[0]=='n': fan[x[1]]+=1
    for o in outs:
        for b in o:
            if isinstance(b,tuple) and b[0]=='n': outset.add(b[1])
    roots=set(); leaves={}
    for k in keep:
        op,a,b=g.ops[k]; fins=[x for x in (a,b) if isinstance(x,tuple)]
        def lv(x):
            if x[0]!='n' or x[1] in roots: return {x}
            return leaves[x[1]]
        S=set().union(*[lv(x) for x in fins]) if fins else set()
        while len(S)>K:
            cand=[x for x in fins if x[0]=='n' and x[1] not in roots]
            big=max(cand,key=lambda x:len(leaves[x[1]])); roots.add(big[1])
            S=set().union(*[lv(x) for x in fins])
        leaves[k]=S
        if fan[k]>1 or k in outset: roots.add(k)
    return roots

def activity(g,outs,nv,n,ic_bits,iters):
    keep=live_ops(g,outs); idx={k:i for i,k in enumerate(keep)}
    NI=nv*n; base=NI+2                                   # 0..NI-1 inputs, NI=const0, NI+1=const1
    def ref(a):
        if a==0: return NI
        if a==1: return NI+1
        if a[0]=='n': return base+idx[a[1]]
        return (ord(a[0])-97)*n+a[1]
    opc=np.array([{'AND':0,'OR':1,'XOR':2,'NOT':3}[g.ops[k][0]] for k in keep])
    A=np.array([ref(g.ops[k][1]) for k in keep]); Bv=np.array([ref(g.ops[k][2]) if g.ops[k][2] is not None else NI for k in keep])
    outidx=[[ref(b) for b in o] for o in outs]
    v=np.zeros(base+len(keep),dtype=np.uint8); v[NI+1]=1
    def evalall(v):
        a,b=v[A],v[B_]; r=np.where(opc==0,a&b,np.where(opc==1,a|b,np.where(opc==2,a^b,1-a)))
        return r.astype(np.uint8)
    global B_; B_=Bv
    v[:NI]=ic_bits
    for _ in range(4000):                                # settle
        nw=evalall(v)
        if np.array_equal(nw,v[base:]): break
        v[base:]=nw
    tog_ud=np.zeros(len(keep)); tog_zd=np.zeros(len(keep)); depth=0
    for it in range(iters):
        nxt=np.array([v[i] for o in outidx for i in o],dtype=np.uint8)
        prev_final=v[base:].copy(); v[:NI]=nxt; steps=0
        while True:                                       # unit-delay propagation
            nw=evalall(v); ch=nw!=v[base:]
            if not ch.any(): break
            tog_ud+=ch; v[base:]=nw; steps+=1
        depth=max(depth,steps); tog_zd+=(v[base:]!=prev_final)
    roots=tech_map(g,outs,keep); rmask=np.array([k in roots for k in keep])
    return dict(gates=len(keep),luts=int(rmask.sum()),depth=depth,
        alpha_gate_zd=tog_zd.sum()/iters/len(keep),
        lut_tog_zd=tog_zd[rmask].sum()/iters, lut_tog_ud=tog_ud[rmask].sum()/iters,
        gate_tog_ud=tog_ud.sum()/iters)
