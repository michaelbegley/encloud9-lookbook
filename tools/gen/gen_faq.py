"""Grand FAQ, Draft 1. Every FAQ answer on the built Look 9 pages, pulled from the pages themselves (Michael's idea, Brian agreed, 9 Nov call).
Re-run after any page FAQ changes. Blog posts left out (their FAQs belong to the post)."""
import sys, re; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
URL = 'https://www.encloud9.com/faq/'
GROUPS = [
 ('start', 'Getting started', [('nine-home.html','Home'),('nine-contact.html','Contact us'),('nine-omaha.html','Omaha and Nebraska'),('nine-how-we-work.html','How we work'),('nine-team.html','Team'),('nine-healthcare.html','Healthcare'),('nine-professional-services.html','Professional services'),('nine-manufacturing.html','Manufacturing'),('nine-distribution.html','Distribution'),]),
 ('d365', 'Dynamics 365', [('nine-dynamics-365.html','Dynamics 365'),('nine-dynamics-365-sales.html','Dynamics 365 Sales'),('nine-customer-service.html','Customer Service'),('nine-d365-pricing.html','Dynamics 365 pricing'),('nine-d365-licensing.html','Dynamics 365 licensing'),('nine-vs-crm.html','Dynamics 365 vs Salesforce vs HubSpot'),('nine-contact-center.html','Contact Center'),('nine-field-service.html','Field Service'),('nine-project-operations.html','Project Operations'),('nine-customer-insights.html','Customer Insights')]),
 ('ai', 'Copilot, AI and Power Platform', [('nine-copilot.html','Copilot and AI'),('nine-copilot-studio.html','Copilot Studio'),('nine-power-platform.html','Power Platform'),('nine-document-core-pack.html','Document Core Pack'),('nine-business-central.html','Business Central integration'),('nine-power-apps.html','Power Apps'),('nine-power-bi.html','Power BI')]),
 ('mkt', 'Marketing and email', [('nine-marketing.html','Marketing'),('nine-email-verifier.html','Email Verifier')]),
 ('pkg', 'Packages', [('nine-packages.html','Packages'),('nine-full-implementation.html','Full implementation'),('nine-rescue-repair.html','Rescue and Repair'),
    ('nine-accelerators.html','Accelerators'),('nine-sales-accelerator.html','Sales Accelerator'),('nine-service-accelerator.html','Service Accelerator')]),
 ('move', 'Moving to Dynamics 365', [('nine-move-salesforce.html','Move from Salesforce'),('nine-move-hubspot.html','Move from HubSpot'),('nine-move-zoho.html','Move from Zoho'),('nine-move-monday.html','Move from monday.com')]),
 ('sup', 'Support and storage', [('nine-support.html','Support plans'),('nine-storage.html','Dataverse storage'),('nine-guides.html','Free guides and checks'),('nine-health-check.html','CRM Health Check'),('nine-license-check.html','License check')]),
]
seen, groups, total, dup = set(), [], 0, 0
for gid, gname, pages in GROUPS:
    items = []
    for fn, label in pages:
        s = open(P + fn, encoding='utf-8').read()
        for q, a in re.findall(r'<details><summary>((?:(?!</?details|</summary>).)*?)</summary><p>((?:(?!</?details).)*?)</p></details>', s, re.S):  # tempered: never spans the menu's details (10 Nov 2026 fix, G4/G7)
            key = re.sub(r'\W+', ' ', H.unescape(q).lower()).strip()
            if key in seen: dup += 1; continue
            seen.add(key); items.append((H.unescape(q), a, fn, label))
    total += len(items); groups.append((gid, gname, items))
ANSWER = (f'This page holds every question answered across our site, {total} in all, grouped by topic. Each answer links back to the page it comes from. '
          'Search the list, or jump to a topic: Dynamics 365, Copilot and AI, marketing, packages, moving from another CRM, and support.')
TITLE = 'Dynamics 365 Questions, Answered | enCloud9 FAQ'
META = 'Every question we answer about Dynamics 365, Copilot, Power Platform, packages, moving from another CRM and support plans, in one place.'
css = ('.fqtools{display:grid;gap:14px;margin:8px 0 32px}.fqtools input{font:inherit;font-size:17px;padding:14px 16px;border:1px solid var(--line);background:#fff;color:var(--ink);width:100%;max-width:640px}'
       '.chips{display:flex;flex-wrap:wrap;gap:8px}.chips a{font-family:var(--mono);font-size:12px;padding:8px 12px;border:1px solid var(--line);color:var(--ink);text-decoration:none;background:#fff}'
       '.chips a:hover{border-color:var(--b5)}.fqfrom{display:block;margin-top:10px;font-family:var(--mono);font-size:12px}.fqcount{font-family:var(--mono);font-size:12px;color:var(--muted)}'
       '.fqg{scroll-margin-top:96px}.fqg .faq{max-width:none}')
allqa = [(q, a) for _, _, it in groups for q, a, _, _ in it]
hd = mkhead(TITLE, META, [('Home','https://www.encloud9.com/'),('Questions',URL)], faq=allqa, css=css)
chips = ''.join(f'<a href="#{gid}">{e(gn)} ({len(it)})</a>' for gid, gn, it in groups)
secs = ''
for gid, gn, it in groups:
    li = ''.join(f'      <details><summary>{e(q)}</summary><p>{a}<a class="lnk fqfrom" href="{fn}">From {e(lb)} &rarr;</a></p></details>\n' for q, a, fn, lb in it)
    secs += f'''  <section class="sec fqg" id="{gid}" aria-labelledby="{gid}-h">
    <div class="faqsplit">
    <div class="faqside rev"><h2 class="h2" id="{gid}-h">{e(gn)}</h2><p class="fqcount">{len(it)} questions</p></div>
    <div><div class="faq rev">
{li}    </div></div>
    </div>
  </section>
'''
main = crumbnav([('Home','nine-home.html'),('Questions',None)]) + f'''  <section class="hero" aria-labelledby="h1" style="grid-template-columns:1fr">
    <div class="copy" style="max-width:820px">
      <span class="mono rise" style="--d:0">Questions &middot; All topics</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Questions,</span></span> <span class="ln"><span style="--d:2">answered</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="fqtools rise" style="--d:4">
        <label class="sr-only" for="fqs">Search the questions</label>
        <input id="fqs" type="search" placeholder="Search the questions, for example licenses" autocomplete="off">
        <p class="fqcount" id="fqn" role="status">{total} questions</p>
        <nav class="chips" aria-label="Topics">{chips}</nav>
      </div>
    </div>
  </section>

{secs}
  <section class="sec" aria-labelledby="ask-h">
    <div class="sec-head rev"><h2 class="h2" id="ask-h">Did not find your question?</h2>
    <p class="lead">Ask us on a call. You get a straight answer, whether or not you work with us.</p></div>
    <div class="acts rev"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="nine-contact.html">Contact us <span>&rarr;</span></a></div>
  </section>
<script>
(function(){{var i=document.getElementById('fqs'),n=document.getElementById('fqn');if(!i)return;
var ds=[].slice.call(document.querySelectorAll('.fqg details')),gs=[].slice.call(document.querySelectorAll('.fqg'));
i.addEventListener('input',function(){{var t=i.value.trim().toLowerCase(),c=0;
ds.forEach(function(d){{var hit=!t||d.textContent.toLowerCase().indexOf(t)>-1;d.hidden=!hit;if(hit)c++;d.open=!!t&&hit&&c<=3;}});
gs.forEach(function(g){{g.hidden=!g.querySelector('details:not([hidden])');}});
n.textContent=t?(c+' of {total} questions match'):'{total} questions';}});}})();
</script>
'''
write('nine-faq.html', hd, main)
print('ok', total, 'dups skipped', dup, len(ANSWER.split()), len(TITLE), len(META), [(g, len(i)) for g, _, i in groups])
