import sys,html,base64,pathlib
R='/home/claude/encloud9-lookbook'
font=base64.b64encode(open(R+'/wp-theme-fable/encloud9-nine/assets/fonts/hanken-grotesk-latin-600-normal.woff2','rb').read()).decode()
font4=base64.b64encode(open(R+'/wp-theme-fable/encloud9-nine/assets/fonts/hanken-grotesk-latin-500-normal.woff2','rb').read()).decode()
wm=open(R+'/assets/brand/enCloud9-wordmark-white.svg').read()
wm=wm[wm.find('<svg'):]
# which square lights up per topic
LIT={'Admin and how-to':4,'Copilot and AI':2,'Marketing automation':6,'Switching to Dynamics 365':8,'News':0,'Licensing and pricing':5}
SH=['#1F3A80','#2A4B94','#355DA6','#2A4B94','#355DA6','#1F3A80','#355DA6','#1F3A80','#2A4B94']
PHOTO={'clickdimensions-dashboards-2025-update':'472720714','creating-and-managing-sequences-in-dynamics-365-sales-insights':'471776879','dynamics-365-adoption':'278612687','dynamics-365-pricing-licensing-2025-guide':'393026206','dynamics-365-sales-qualification-agent':'485903695','encloud9-recognized-on-crm-software-blogs-best-dynamics-365-partner-list-2026':'145073469','generative-pages-dynamics-365':'394721662','how-dynamics-365-activate-makes-leaving-salesforce-easier':'356565250','how-to-improve-dynamics-365-data-quality-garbage-in-garbage-out':'96097567','how-to-stop-leads-from-falling-through-the-cracks-in-dynamics-365':'329210123','how-to-track-the-last-activity-date-in-microsoft-dynamics-365-sales':'563913420','mastering-lead-management-in-dynamics-365-igniting-your-sales-pipeline':'714059085','microsoft-dataverse-storage-notifications':'162150298','microsoft-dynamics-365-crm-skills-copilot':'1225697039','optimizing-sales-strategies-with-dynamics-365-enabling-and-utilizing-sales-usage-reports':'828885386','what-a-healthy-dynamics-365-system-actually-looks-like':'227086625','whats-new-in-dynamics-365-november-2026':'296716261','which-dynamics-365-customizations-are-worth-it-and-which-ones-we-usually-advise-against':'342229375'}
def page(topic,title,slug=''):
    ph=base64.b64encode(open(f'/home/claude/thumbs/photos/AdobeStock_{PHOTO[slug]}.jpeg','rb').read()).decode() if slug in PHOTO else ''
    lit=LIT.get(topic,4)
    sq=''.join(f'<i style="background:{"#9DB3DC" if i==lit else SH[i]}"></i>' for i in range(9))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:H;src:url(data:font/woff2;base64,{font}) format('woff2');font-weight:600}}
@font-face{{font-family:H;src:url(data:font/woff2;base64,{font4}) format('woff2');font-weight:500}}
*{{margin:0;box-sizing:border-box}}body{{width:1200px;height:630px;background:#172A5E;font-family:H,Arial,sans-serif;position:relative;overflow:hidden}}
.ph{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{ph}) center/cover;filter:grayscale(1) contrast(1.05);opacity:.26;mix-blend-mode:luminosity}}.fade{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(23,42,94,.92) 0%,rgba(23,42,94,.55) 62%,rgba(23,42,94,.35) 100%)}}.t{{position:absolute;left:80px;top:78px;color:#9DB3DC;font-weight:500;font-size:22px;letter-spacing:.14em;text-transform:uppercase}}
h1{{position:absolute;left:80px;top:128px;width:740px;color:#fff;font-weight:600;font-size:64px;line-height:1.08;letter-spacing:-.01em}}
.w{{position:absolute;left:66px;bottom:52px;width:200px}}.w svg{{width:100%;height:auto;display:block}}
.u{{position:absolute;left:290px;bottom:66px;color:#9DB3DC;font-weight:500;font-size:22px}}
.g{{position:absolute;right:80px;top:50%;transform:translateY(-50%);display:grid;grid-template-columns:repeat(3,72px);gap:12px}}
.g i{{width:72px;height:72px;border-radius:10px;display:block}}
</style></head><body><div class="ph"></div><div class="fade"></div><div class="t">{html.escape(topic)}</div><h1 id="h">{html.escape(title)}</h1><div class="g">{sq}</div>
<div class="w">{wm}</div><div class="u">encloud9.com/blog</div>
<script>const h=document.getElementById('h');let s=64;while(h.scrollHeight>330&&s>40){{s-=2;h.style.fontSize=s+'px'}}</script></body></html>'''
if __name__=='__main__':
    import csv
    from playwright.sync_api import sync_playwright
    rows=[l.rstrip('\n').split('|') for l in open('/tmp/posts.tsv')]
    want=sys.argv[1:]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1200,'height':630})
        for slug,topic,title in rows:
            if want and slug not in want: continue
            if topic=='?': topic={'dynamics-365-pricing-licensing-2025-guide':'Licensing and pricing','generative-pages-dynamics-365':'Copilot and AI','optimizing-sales-strategies-with-dynamics-365-enabling-and-utilizing-sales-usage-reports':'Admin and how-to'}[slug]
            pathlib.Path(f'{slug}.html').write_text(page(topic,title,slug))
            pg.goto('file://'+str(pathlib.Path(f'{slug}.html').resolve())); pg.wait_for_timeout(300)
            pg.screenshot(path=f'{slug}.png'); print('ok',slug)
        b.close()
