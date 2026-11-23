import glob,re,html,sys,csv
SMALL=set('a an the and but or nor for so yet as at by in of on to up via vs vs. with from into per than off out over'.split())
WORD=re.compile(r"(?<![A-Za-z0-9&;'’.])([A-Za-z][A-Za-z0-9'’.]*)")
def fix_heading(inner):
    parts=re.split(r'(<[^>]+>)',inner)
    # collect words across text parts to know first/last
    words=[]
    skip=False
    for i,p in enumerate(parts):
        if p.startswith('<'):
            if p.lower().startswith('<small'): skip=True
            if p.lower().startswith('</small'): skip=False
            continue
        if skip: continue
        for m in WORD.finditer(p): words.append((i,m))
    if not words: return inner
    out=list(parts); edits={}
    for k,(i,m) in enumerate(words):
        w=m.group(1); first=k==0; last=k==len(words)-1
        prev=parts[i][:m.start()]
        after_colon=False
        # look back through text for colon/dash start of a phrase
        j=k-1
        if j>=0:
            pi,pm=words[j]
            between=parts[pi][pm.end():] if pi!=i else parts[i][pm.end():m.start()]
            if re.search(r'[:?!.]|&mdash;|—',between): after_colon=True
        if any(c.isupper() for c in w[1:]) or any(c.isdigit() for c in w) or ('.' in w[:-1]): continue
        lw=w.lower().rstrip('.')
        if lw in SMALL and not (first or last or after_colon):
            new=w if w[0].islower() else w  # leave small words as written
            new=w[0].lower()+w[1:] if w[0].isupper() and False else w
        else:
            new=w[0].upper()+w[1:]
        if '-' in w: pass
        edits.setdefault(i,[]).append((m.start(),m.end(),new))
    for i,es in edits.items():
        p=parts[i]
        for s,e,new in sorted(es,reverse=True): p=p[:s]+new+p[e:]
        out[i]=p
    # hyphenated parts: capitalize letter after hyphen inside words (Go-live -> Go-Live) unless small
    res=''.join(out)
    return res
def hyph(inner):
    def f(m):
        nxt=m.group(2)
        return m.group(1)+'-'+(nxt[0].upper()+nxt[1:])
    parts=re.split(r'(<[^>]+>)',inner)
    return ''.join(p if p.startswith('<') else re.sub(r'([A-Za-z])-([a-z][a-z]*)',f,p) for p in parts)
rows=[]
H=re.compile(r'(<h([1-3])\b[^>]*>)(.*?)(</h\2>)',re.S)
apply='--apply' in sys.argv
for fpath in sorted(glob.glob('site/**/*.html',recursive=True)):
    s=open(fpath).read(); a=s.find('<main'); b=s.find('</main>')
    if a<0: continue
    main=s[a:b]
    def r(m):
        new=hyph(fix_heading(m.group(3)))
        if new!=m.group(3):
            t=lambda x: html.unescape(re.sub(r'<[^>]+>','',x)).replace('­','').strip()
            rows.append((fpath,t(m.group(3)),t(new)))
        return m.group(1)+new+m.group(4)
    main2=H.sub(r,main)
    if apply and main2!=main: open(fpath,'w').write(s[:a]+main2+s[b:])
out=next((a.split('=',1)[1] for a in sys.argv if a.startswith('--out=')),None)
if out:  # only with --out, so a later run can never blank the saved list
    w=csv.writer(open(out,'w',newline=''))
    w.writerow(['page','before','after']); w.writerows(rows)
print(len(rows),'headings changed on',len({r[0] for r in rows}),'pages')
