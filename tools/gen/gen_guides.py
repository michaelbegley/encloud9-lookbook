"""Free guides and checks hub, Draft 1 (LEAD-MAGNETS-PLAN.md, Michael agreed 9 Nov). New URL /free-guides-and-checks/ (Claude's call; flag).
Check descriptions word for word from the home page checkups section; guide titles from SITE-PAGE-MAP.csv (live /lp/ pages); videos from the ported posts."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
URL = 'https://www.encloud9.com/free-guides-and-checks/'
TITLE = 'Free Dynamics 365 Guides and Checks | enCloud9'
META = 'Free help for Dynamics 365 teams: a Dataverse Storage Analysis, a CRM Health Check, a Copilot readiness check, downloadable guides and how-to videos.'
ANSWER = ('Free help for Dynamics 365 teams, each piece built to fix one problem. Book a free check and we look at your own system with you, '
          'or download a guide and work through it yourself. Free checkups, no obligation: you get a straight answer, whether or not you work with us.')
CHECKS = [('License check','Who has which license, where to save, and what February 2027 means for your apps.','nine-license-check.html','Book it'),
          ('Dataverse Storage Analysis','What is filling your storage, which type is over, and a written plan to stay under the limit. One hour.','nine-storage.html','Book it'),
          ('CRM Health Check','A review of your Dynamics 365 setup, with findings ranked by what each fix is worth.','nine-health-check.html','Book it'),
          ('Copilot readiness check','Five questions on data and permissions, with a written next step. About two minutes.','nine-home.html#checkups','Start')]
GUIDES = [('Dynamics 365 CRM Cleanup Checklist for Admins','A free PDF checklist for cleaning up a Dynamics 365 system.','https://www.encloud9.com/lp/dynamics-365-crm-cleanup-checklist/'),
          ('Microsoft Copilot Guide for Dynamics 365 CRM Users','A free guide to Copilot in Dynamics 365 Sales and Customer Service.','https://www.encloud9.com/lp/copilot-guide-dynamics-365-crm/'),
          ('Sales Management Best Practices for Dynamics 365','A free guide for sales managers running a team in Dynamics 365.','https://www.encloud9.com/lp/dynamics-365-sales-management-guide/')]
VIDEOS = [('Easily Track Last and Next Activity Dates in Dynamics 365','https://youtu.be/HUgUlEYomKM'),('How to Use Lead Sequences in Dynamics 365 Sales','https://youtu.be/pZdhwN6AIM4'),
          ('How to Link Leads to Campaigns in Dynamics 365','https://youtu.be/mJ2Vf09tGng'),('How to Create a Lead from an Outlook Email in Copilot for Sales','https://youtu.be/5Q-JYI6b-So')]
FAQ = [("Are the checks really free?","Yes. Free checkups, no obligation. You get a straight answer on where your system stands, whether or not you work with us."),
       ("What happens after I download a guide?","You get the guide after a short form. [Follow-up email from a real person a few days later, per the lead magnet plan; Brian approves the wording.]"),
       ("Which check should I start with?",'If Microsoft is sending you storage warnings, start with the <a class="lnk" href="nine-storage.html">Dataverse Storage Analysis</a>. If the system feels slow, messy or unused, start with the CRM Health Check.'),
       ("How often do you add new guides?","We add a guide when something changes in Dynamics 365 that teams need to act on. [Monthly cadence planned; confirm before launch.]")]
css = ('.gcards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}'
       '.gcards a{display:flex;flex-direction:column;gap:10px;background:var(--bg,#fff);padding:26px;text-decoration:none;color:var(--ink);min-height:200px}'
       '.gcards a:hover{background:var(--tint,#EAF0F8)}.gcards .t{font-family:var(--head);font-size:21px;font-weight:600;line-height:1.25}.gcards .d{color:var(--muted);font-size:16px;flex:1}'
       '.gcards .go{font-family:var(--mono);font-size:12px;color:var(--b5)}'
       '.gcards.two{grid-template-columns:repeat(2,minmax(0,1fr))}@media(max-width:900px){.gcards{grid-template-columns:1fr 1fr}}@media(max-width:560px){.gcards{grid-template-columns:1fr}.gcards a{min-height:0}}')
hd = mkhead(TITLE, META, [('Home','https://www.encloud9.com/'),('Free guides and checks',URL)], faq=FAQ, css=css)
cards = lambda items, c='': f'    <div class="gcards{c} rev">\n' + ''.join(f'      <a href="{h}"><span class="mono">{m}</span><span class="t">{e(t)}</span><span class="d">{e(d)}</span><span class="go">{g} &rarr;</span></a>\n' for m,t,d,h,g in items) + '    </div>\n'
cells = [('b1','#checks','Free check','Storage','Dataverse Storage Analysis','&#8600;',''),('b2','nine-health-check.html','Free check','Health Check','Your Dynamics 365 setup','&#8599;',''),('b3','#checks','Two minutes','Copilot','Readiness check','&#8600;',''),
         ('b4','#guides','Download','Guides','Checklists and how-tos','&#8600;',''),('b5','#checks','Free','No obligation','A straight answer','','core'),
         ('b6','#videos','Watch','Videos','Short how-tos','&#8600;','lt'),('b7','nine-blog.html','Read','Blog','Weekly posts','&#8599;','lt'),
         ('b8','nine-faq.html','Ask','All questions','Every answer in one place','&#8599;','lt'),('b9','nine-license-check.html','Free check','License check','Before February 2027','&#8599;','lt')]
main = crumbnav([('Home','nine-home.html'),('Free guides and checks',None)]) + f'''  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Free &middot; Guides and checks</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Free guides</span></span> <span class="ln"><span style="--d:2">and checks</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4"><a class="btn btn-p" href="nine-storage.html">Book a free storage analysis</a><a class="lnk" href="#guides">See the guides <span>&rarr;</span></a></div>
    </div>
    <div>
{grid('Free help from enCloud9', cells)}    </div>
  </section>

  <section class="sec" id="checks" aria-labelledby="ck-h">
    <div class="sec-head rev">
      <h2 class="h2" id="ck-h">Which free checks can we run on your system?</h2>
      <p class="lead">A check is a short session on your own Dynamics 365 system. [Session lengths, Brian confirms.] You leave with written findings and a next step.</p>
    </div>
''' + cards([('Free check', t, d, h, g) for t,d,h,g in CHECKS], ' two') + f'''  </section>

  <section class="sec" id="guides" aria-labelledby="gd-h">
    <div class="sec-head rev">
      <h2 class="h2" id="gd-h">Which guides can I download?</h2>
      <p class="lead">Each guide covers one job in Dynamics 365. Fill in a short form to get it.</p>
    </div>
''' + cards([('Free guide', t, d, h, 'Get the guide') for t,d,h in GUIDES]) + f'''  </section>

  <section class="sec" id="videos" aria-labelledby="vd-h">
    <div class="sec-head rev">
      <h2 class="h2" id="vd-h">Are there short how-to videos?</h2>
      <p class="lead">Yes. Each one walks through a single task in Dynamics 365, start to finish.</p>
    </div>
''' + cards([('Video', t, 'A short walkthrough on YouTube.', h, 'Watch on YouTube') for t,h in VIDEOS], ' two') + '''  </section>

''' + faqsec('Questions about the free guides and checks', FAQ) + '\n' + lnav('Related', [
  ('nine-storage.html','Free check','Dataverse storage'),('nine-d365-licensing.html','Dynamics 365','Licensing'),('nine-blog.html','Read','Blog'),('nine-contact.html','Company','Contact us')])
write('nine-guides.html', hd, main)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
