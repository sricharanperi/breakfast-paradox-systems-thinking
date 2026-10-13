import sys,re
def load(f):
    return open(f).read().split('\n')
def paras(f,minw=70):
    L=load(f); out=[]
    for i,l in enumerate(L):
        if not l.strip() or l[0] in '|#!>' or l.startswith('Decision:') or l.startswith('Table:'): continue
        w=len(l.split())
        if w>=minw: out.append((i,w,l))
    return out
def sentences(l):
    return re.split(r'(?<=[.;:?])\s+(?=[A-Z"(\[*])',l)
if __name__=='__main__':
    f=sys.argv[1]; mn=int(sys.argv[2]) if len(sys.argv)>2 else 70
    for i,w,l in paras(f,mn):
        s=sentences(l)
        print(f"{i:4} {w:4} s{len(s):2} | {l[:95]}")

def apply(f, keep=None, drop=None):
    L=load(f); n0=sum(len(x.split()) for x in L)
    for i,n in (keep or {}).items():
        s=sentences(L[i]); 
        if len(s)>n:
            k=n
            while k<len(s) and s[k-1].rstrip()[-1:] in ';:': k+=1
            L[i]=' '.join(s[:k])
    for i in (drop or []): L[i]=None
    L=[x for x in L if x is not None]
    # collapse triple blank lines
    t='\n'.join(L); t=re.sub(r'\n{3,}','\n\n',t)
    open(f,'w').write(t)
    print(f,n0,'->',len(t.split()))
