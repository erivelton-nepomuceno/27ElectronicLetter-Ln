import zoo2, ext, math, sys
def lyap(fn,ic,n,dt,tr=2000):
    F=ext.FloatX(); s=list(ic)
    try:
        for k in range(tr): s=fn(F,*s)
        t=[s[0]+1e-8]+list(s[1:]); L=0
        for k in range(n):
            s=fn(F,*s); t=fn(F,*t)
            if max(abs(v) for v in s)>1e5: return "div"
            d=math.sqrt(sum((a-b)**2 for a,b in zip(s,t)))
            if d==0: return "col"
            L+=math.log(d/1e-8); t=[a+(b-a)*1e-8/d for a,b in zip(s,t)]
    except Exception as e: return "err"
    return round(L/(n*dt),3)
