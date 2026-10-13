def trim(path, ops):
    """ops: (start, end, replacement). If end is '' the start string itself is replaced."""
    s=open(path).read(); n0=len(s.split())
    for a,b,rep in ops:
        i=s.find(a)
        if i<0: print('MISSING START:',a[:50]); continue
        if b=='':
            s=s[:i]+rep+s[i+len(a):]; continue
        j=s.find(b,i)
        if j<0: print('MISSING END:',b[:50]); continue
        if j-i>3500: print('REFUSED (span too long):',a[:50]); continue
        s=s[:i]+rep+s[j+len(b):]
    open(path,'w').write(s)
    print(path,n0,'->',len(s.split()))
