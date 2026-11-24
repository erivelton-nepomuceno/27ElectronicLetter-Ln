# Minimal Digital Chaotic System (Nepomuceno, Lima, Arias-Garcia, Perc, Repnik,
# Chaos, Solitons & Fractals 120 (2019) 62-66):
#   x_{n+1} = 4 * x_n * xdc_n,  xdc = digit (one's) complement of x = 1 - ulp - x
# Gate-level trick: x_i*~x_j + x_j*~x_i = x_i XOR x_j and x_i*~x_i = 0, so the
# product needs only n(n-1)/2 XOR partial products; r = 4 is a 2-bit shift (wires).
from chua_min import Net

def build(n):
    g=Net(); X=[('a',i) for i in range(n)]          # unsigned fraction, LSB first
    cols=[[] for _ in range(2*n+1)]
    for i in range(n):
        for j in range(i+1,n): cols[i+j].append(g.XOR(X[i],X[j]))
    P=[]
    for c in range(2*n):                             # column compression, exact
        col=cols[c]
        while len(col)>1:
            if len(col)>=3:
                a,b,d=col.pop(),col.pop(),col.pop(); s=g.XOR(a,b)
                col.append(g.XOR(s,d)); cols[c+1].append(g.OR(g.AND(a,b),g.AND(s,d)))
            else:
                a,b=col.pop(),col.pop(); col.append(g.XOR(a,b)); cols[c+1].append(g.AND(a,b))
        P.append(col[0] if col else 0)
    return g,[P[n-2:2*n-2]]                          # x' = 4P >> n  (pure wiring)

def live(g,outs):
    """Gates that actually drive an output (dead-code elimination)."""
    seen=set(); st=[b for o in outs for b in o]
    while st:
        a=st.pop()
        if isinstance(a,tuple) and a[0]=='n' and a[1] not in seen:
            seen.add(a[1]); op,x,y=g.ops[a[1]]; st+= [x] + ([y] if y is not None else [])
    return len(seen)
