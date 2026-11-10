"""Edit JSON-LD blocks in a page: add an offer to the Service block, and add FAQ questions that are visible but missing."""
import re,json,html,sys
def blocks(s):return list(re.finditer(r'(<script type="application/ld\+json">)(.*?)(</script>)',s,re.S))
def visible_faq(s,q):
    m=re.search(r'<summary>'+re.escape(q)+r'</summary>(.*?)</details>',s,re.S)
    if not m: return None
    t=re.sub(r'<[^>]+>',' ',m.group(1));t=html.unescape(re.sub(r'\s+',' ',t)).strip();return t
def edit(path,offers=None,add_q=()):
    s=open(path,encoding='utf-8').read()
    for m in reversed(blocks(s)):
        j=json.loads(m.group(2));ch=False
        def svc(o):
            nonlocal ch
            if isinstance(o,dict) and o.get('@type')=='Service' and offers is not None:o['offers']=offers;ch=True
            if isinstance(o,dict) and o.get('@type')=='FAQPage':
                have={x['name'] for x in o['mainEntity']}
                for q in add_q:
                    if q in have:continue
                    a=visible_faq(s,q)
                    if a:o['mainEntity'].append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}});ch=True
                    else:print('NOT FOUND visible',q)
        if isinstance(j,dict) and '@graph' in j:[svc(x) for x in j['@graph']]
        else:svc(j)
        if ch:s=s[:m.start(2)]+json.dumps(j,ensure_ascii=False)+s[m.end(2):]
    open(path,'w',encoding='utf-8').write(s)
if __name__=='__main__':
    path=sys.argv[1];spec=json.loads(sys.argv[2]);edit(path,spec.get('offers'),spec.get('add_q',[]))
