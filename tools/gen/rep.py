import sys,json
def run(path,pairs):
    s=open(path,encoding='utf-8').read()
    for a,b in pairs:
        n=s.count(a)
        if n!=1: sys.exit(f"MISS ({n}) in {path}: {a[:90]!r}")
        s=s.replace(a,b)
    open(path,'w',encoding='utf-8').write(s);print('ok',path,len(pairs))
