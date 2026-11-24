# Gate-minimal MDCS: XOR-pair partial products, column compression,
# optional truncation (k guard columns) with a constant bias compensation.
from chua_min import Net
def build(n,k=None,comp=0):
    g=Net(); X=[('a',i) for i in range(n)]
    lo = 0 if k is None else max(0,n-2-k)
    cols=[[] for _ in range(2*n+2)]
    for i in range(n):
        for j in range(i+1,n):
            if i+j>=lo: cols[i+j].append(g.XOR(X[i],X[j]))
    for b in range(lo, 2*n):                 # add constant 'comp' at column lo
        if (comp>>(b-lo))&1: cols[b].append(1)
    P=[]; fa=ha=0
    for c in range(2*n):
        col=cols[c]
        while len(col)>1:
            if len(col)>=3:
                a,b,d=col.pop(),col.pop(),col.pop(); s=g.XOR(a,b)
                col.append(g.XOR(s,d)); cols[c+1].append(g.OR(g.AND(a,b),g.AND(s,d))); fa+=1
            else:
                a,b=col.pop(),col.pop(); col.append(g.XOR(a,b)); cols[c+1].append(g.AND(a,b)); ha+=1
        P.append(col[0] if col else 0)
    g.fa,g.ha=fa,ha
    return g,[P[n-2:2*n-2]]
