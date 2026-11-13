"""Score a WordPress build against the mock. usage: python3 -I score.py <outDir> [wp-path-for-editability]
Prints parity (pixel difference, height), status, broken images, script errors, page weight,
and, with a WordPress path, how much page content is editable blocks rather than Custom HTML."""
import json,sys,os,subprocess,re,statistics
from PIL import Image, ImageChops
out=sys.argv[1]; d=json.load(open(os.path.join(out,'shots.json')))
by={}
for r in d: by.setdefault((r['old'],r['w']),{})[r['tag']]=r
rows=[]
for (old,w),v in by.items():
    m,p=v['mock'],v['wp']; n=(old.replace('/','_') or '_')+f'-{w}'
    a=Image.open(f'{out}/{n}-mock.png').convert('RGB'); b=Image.open(f'{out}/{n}-wp.png').convert('RGB')
    h=min(a.height,b.height); W=min(a.width,b.width)
    dd=ImageChops.difference(a.crop((0,0,W,h)),b.crop((0,0,W,h))).convert('L').point(lambda x:255 if x>24 else 0)
    rows.append(dict(old=old,w=w,diff=dd.histogram()[255]/(W*h)*100,dh=p['h']-m['h'],status=p['status'],broken=len(p['broken']),errs=len(p['errs']),kb=p['bytes']/1024))
diffs=[r['diff'] for r in rows]
s=dict(pages=len(rows)//2,median_diff_pct=round(statistics.median(diffs),3),max_diff_pct=round(max(diffs),2),
  over_1pct_count=sum(1 for r in rows if r['diff']>1),worst10=[(r['old'],r['w'],round(r['diff'],2)) for r in sorted(rows,key=lambda r:-r['diff'])[:10]],
  height_mismatch_over_20px=[(r['old'],r['w'],r['dh']) for r in rows if abs(r['dh'])>20],
  non_200=[(r['old'],r['status']) for r in rows if r['status']!=200 and r['old']!='/404/'],
  broken_images=sum(r['broken'] for r in rows),script_errors=sum(r['errs'] for r in rows),
  median_page_kb_1440=round(statistics.median([r['kb'] for r in rows if r['w']==1440]),1))
if len(sys.argv)>2:
    php=f"""foreach(get_posts(['post_type'=>['page','post','story'],'numberposts'=>-1,'post_status'=>'any']) as $p){{$b=parse_blocks($p->post_content);$t=0;$h=0;foreach($b as $x){{if(!$x['blockName'])continue;$t++;if($x['blockName']==='core/html')$h++;}}echo $t.' '.$h.PHP_EOL;}}"""
    o=subprocess.run(['php',os.path.join(os.path.dirname(sys.argv[2]),'wp-cli.phar'),'--allow-root','--path='+sys.argv[2],'eval',php],capture_output=True,text=True).stdout
    t=h=0
    for l in o.split():
        pass
    nums=[tuple(map(int,l.split())) for l in o.strip().splitlines() if l.strip()]
    t=sum(a for a,_ in nums); h=sum(b for _,b in nums)
    s['top_level_blocks']=t; s['custom_html_blocks']=h; s['editable_pct']=round(100*(t-h)/t,1) if t else None
print(json.dumps(s,indent=1))
