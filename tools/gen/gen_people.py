"""Team page, Meet Brian page, CRM Health Check and license check pages: layouts with placeholders, Draft 1.
Known facts only: Brian Begley is enCloud9's founder (project panel); post authors from the blog index. Roles, bios, photos, session lengths in brackets."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
CSS = ('.ppl{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}'
       '.ppl a,.ppl div.p{display:flex;flex-direction:column;gap:10px;background:var(--bg,#fff);padding:22px;text-decoration:none;color:var(--ink)}'
       '.ppl a:hover{background:var(--tint,#EAF0F8)}.ph{aspect-ratio:4/5;background:var(--b8);display:flex;align-items:center;justify-content:center;font-family:var(--label);font-size:12px;color:var(--b3);text-align:center;padding:12px}'
       '.ppl .n{font-family:var(--head);font-size:21px;font-weight:600}.ppl .r{color:var(--muted);font-size:15px}'
       '.bio{display:grid;grid-template-columns:minmax(0,320px) minmax(0,1fr);gap:clamp(28px,4vw,56px);align-items:start}'
       '.cform{display:grid;gap:14px;max-width:640px}.cform label{display:grid;gap:6px;font-size:15px;color:var(--ink)}.cform input,.cform textarea{font:inherit;padding:12px 14px;border:1px solid var(--line);background:#fff;color:var(--ink)}'
       '.cform .msg{font-size:15px;color:var(--ink);padding:12px 14px;background:var(--tint,#EAF0F8)}'
       '@media(max-width:900px){.ppl{grid-template-columns:1fr 1fr}.bio{grid-template-columns:1fr}}@media(max-width:480px){.ppl{grid-template-columns:1fr}}')
TEAM = [('Brian Begley','Founder','nine-team-brian.html'),('Kristin Caniglia','[Role, Kristin confirms]',None),('Deb Burgesser','[Role, Deb confirms]',None),('Jodie [last name]','[Role, Jodie confirms]',None),('Michael Begley','[Title, matches LinkedIn; Brian and Michael set it]',None)]
def card(n, r, h):
    inner = f'<span class="ph" aria-hidden="true">[Photo: real, not AI]</span><span class="n">{e(n)}</span><span class="r">{e(r)}</span>'
    return f'      <a href="{h}">{inner}<span class="mono">Read more &rarr;</span></a>\n' if h else f'      <div class="p">{inner}</div>\n'
def simplehero(kick, h1, ans, acts):
    return f'''  <section class="hero" aria-labelledby="h1" style="grid-template-columns:1fr">
    <div class="copy" style="max-width:820px">
      <span class="mono rise" style="--d:0">{kick}</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">{h1}</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ans)}</p>
      <div class="acts rise" style="--d:4">{acts}</div>
    </div>
  </section>
'''
# Team
FAQ_T = [("Who will work on our project?","[Brian confirms: who leads a project and who does the build work.]"),("Where is the team?","Our office is in Bellevue, Nebraska, in the Omaha metro. We work with clients across the US, mostly remotely.")]
ANS_T = 'enCloud9 is a Dynamics 365 team in Bellevue, Nebraska, founded by Brian Begley. [One line, Brian confirms: what the team does and how it works with clients.]'
main = crumbnav([('Home','nine-home.html'),('About','nine-about.html'),('Team',None)]) + simplehero('About &middot; Team','Meet the team', ANS_T, f'<a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="nine-how-we-work.html">How we work <span>&rarr;</span></a>') + '''
  <section class="sec" id="people" aria-labelledby="pp-h">
    <div class="sec-head rev"><h2 class="h2" id="pp-h">Who is on the team?</h2><p class="lead">The people who plan, build and support your Dynamics 365 system. [Brian confirms who is listed.]</p></div>
    <div class="ppl rev">
''' + ''.join(card(*t) for t in TEAM) + '''    </div>
  </section>

''' + faqsec('Questions about the team', FAQ_T) + '\n' + lnav('Related', [('nine-about.html','Company','About enCloud9'),('nine-how-we-work.html','Company','How we work'),('nine-stories.html','Proof','Client stories'),('nine-contact.html','Company','Contact us')])
write('nine-team.html', mkhead('The enCloud9 Team | Dynamics 365 Partner', 'Meet the enCloud9 team in Bellevue, Nebraska, who plan, build and support Dynamics 365 for growing businesses across the US. Founded by Brian Begley.',
      [('Home','https://www.encloud9.com/'),('About','https://www.encloud9.com/about-encloud9/'),('Team','https://www.encloud9.com/about-encloud9/team/')], faq=FAQ_T, css=CSS), main)
# Brian
POSTS = [('nine-post-storage-warning.html','The Microsoft Dataverse Storage Warning You Shouldn\'t Ignore'),('nine-post-crm-skills.html','Microsoft Introduces 30 New Dynamics 365 CRM Skills for Copilot'),
         ('nine-post-customizations.html','Which Dynamics 365 Customizations Are Worth It'),('nine-post-partner-list-2026.html','enCloud9 Recognized on CRM Software Blog\'s Best Dynamics 365 Partner List 2026'),
         ('nine-post-activate-salesforce.html','How Dynamics 365 Activate Makes Leaving Salesforce Easier'),('nine-post-leads-cracks.html','How to Stop Leads From Falling Through the Cracks in Dynamics 365')]
ANS_B = 'Brian Begley founded enCloud9 and leads its Dynamics 365 work. [Two lines, Brian confirms: his background, what he works on today, and why he started enCloud9.]'
posts = ''.join(f'        <li><a class="lnk" href="{h}">{e(t)}</a></li>\n' for h, t in POSTS)
main = crumbnav([('Home','nine-home.html'),('About','nine-about.html'),('Team','nine-team.html'),('Brian Begley',None)]) + simplehero('Team &middot; Founder','Brian Begley', ANS_B, f'<a class="btn btn-p" href="{BOOK}">Book a call with Brian\'s team</a><a class="lnk" href="#posts">Brian\'s posts <span>&rarr;</span></a>') + f'''
  <section class="sec" id="about" aria-labelledby="ab-h">
    <div class="bio rev">
      <div class="ph" aria-hidden="true">[Photo of Brian: real, not AI]</div>
      <div>
        <h2 class="h2" id="ab-h">Who is Brian Begley?</h2>
        <p class="lead">[Bio, Brian writes or approves: background, how enCloud9 started, the kind of clients he works with.]</p>
        <ul class="fit" style="list-style:none;padding:0;margin-top:18px">
          <li>Founder, enCloud9</li>
          <li>[LinkedIn profile link, Brian confirms]</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="sec" id="posts" aria-labelledby="po-h">
    <div class="sec-head rev"><h2 class="h2" id="po-h">What has Brian written?</h2><p class="lead">Recent posts by Brian on the enCloud9 blog.</p></div>
    <ul class="rev" style="display:grid;gap:12px;padding-left:18px">
{posts}    </ul>
  </section>

''' + lnav('Related', [('nine-team.html','Company','The team'),('nine-about.html','Company','About enCloud9'),('nine-blog.html','Read','Blog'),('nine-contact.html','Company','Contact us')])
ld = [{"@context":"https://schema.org","@type":"Person","name":"Brian Begley","jobTitle":"Founder","worksFor":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"}}]
write('nine-team-brian.html', mkhead('Brian Begley, Founder of enCloud9', 'Brian Begley founded enCloud9, a Dynamics 365 partner in Bellevue, Nebraska. His background, how he works with clients, and his posts on Dynamics 365.',
      [('Home','https://www.encloud9.com/'),('About','https://www.encloud9.com/about-encloud9/'),('Team','https://www.encloud9.com/about-encloud9/team/'),('Brian Begley','https://www.encloud9.com/about-encloud9/team/brian-begley/')], extra_ld=ld, css=CSS), main)
# Free check pages
def checkpage(fn, url, title, meta, kick, h1, ans, gets, fit_h, fit, faq, asset):
    gl = ''.join(f'        <li>{x}</li>\n' for x in gets)
    fl = ''.join(f'        <li>{x}</li>\n' for x in fit)
    main = crumbnav([('Home','nine-home.html'),('Free guides and checks','nine-guides.html'),(h1,None)]) + simplehero(kick, h1, ans, '<a class="btn btn-p" href="#book">Book the free check</a><a class="lnk" href="#get">What you get <span>&rarr;</span></a>') + f'''
  <section class="sec" id="get" aria-labelledby="gt-h">
    <div class="fitsplit">
    <div class="side rev"><h2 class="h2" id="gt-h">What do you get from the {e(h1)}?</h2><p class="lead">Written findings you can share with your team, and a next step. Free checkups, no obligation.</p></div>
    <div class="fit rev"><div class="yes"><h3 class="h3">You get</h3><ul>
{gl}    </ul></div></div>
    </div>
  </section>

  <section class="sec" id="fit" aria-labelledby="ft-h">
    <div class="fitsplit">
    <div class="side rev"><h2 class="h2" id="ft-h">{e(fit_h)}</h2></div>
    <div class="fit rev"><div class="yes"><h3 class="h3">Book it if</h3><ul>
{fl}    </ul></div></div>
    </div>
  </section>

  <section class="sec" id="book" aria-labelledby="bk-h">
    <div class="bio">
    <div class="rev"><h2 class="h2" id="bk-h">How do I book it?</h2><p class="lead">Fill in the form and we set up a time. [Session length and access needed, Brian confirms.]</p>
      <div class="ph" aria-hidden="true" style="aspect-ratio:16/10;margin-top:18px">[Sample of the written findings: real screenshot, client details removed]</div></div>
    <form class="cform rev" id="cform" novalidate>
      <input type="hidden" name="asset" value="{asset}">
      <label>Your name<input name="name" autocomplete="name" required></label>
      <label>Company name<input name="company" autocomplete="organization" required></label>
      <label>Work email<input name="email" type="email" autocomplete="email" required></label>
      <div><button class="btn btn-p" type="submit">Book the free check</button></div>
      <p class="msg" id="cmsg" role="status" hidden></p>
    </form>
    </div>
  </section>

''' + faqsec(f'Questions about the {h1}', faq) + '\n' + lnav('Related', [('nine-guides.html','Free','All free guides and checks'),('nine-storage.html','Free check','Dataverse storage'),('nine-rescue-repair.html','Package','Rescue and Repair'),('nine-contact.html','Company','Contact us')]) + '''<script>
(function(){var f=document.getElementById('cform'),m=document.getElementById('cmsg');if(!f)return;f.addEventListener('submit',function(ev){ev.preventDefault();m.hidden=false;
m.textContent=f.checkValidity()?'Concept form: not connected yet. On the live site this goes to our CRM with the check named.':'Please fill in every field.';});})();
</script>
'''
    write(fn, mkhead(title, meta, [('Home','https://www.encloud9.com/'),('Free guides and checks','https://www.encloud9.com/free-guides-and-checks/'),(h1,url)], faq=faq, css=CSS), main)
checkpage('nine-health-check.html','https://www.encloud9.com/crm-health-check/','Free Dynamics 365 CRM Health Check | enCloud9',
  'A free review of your Dynamics 365 setup, with findings ranked by what each fix is worth. Free checkups, no obligation, from enCloud9.',
  'Free check &middot; CRM Health Check','CRM Health Check',
  'A free review of your Dynamics 365 setup, with findings ranked by what each fix is worth. [Session length, Brian confirms.] Free checkups, no obligation: you get a straight answer, whether or not you work with us.',
  ['Findings on your Dynamics 365 setup, ranked by what each fix is worth.','[What we look at, Brian confirms: for example customizations, security roles, data quality, automation.]','A next step, written down.'],
  'Who should book a CRM Health Check?',
  ['Your team works around the CRM instead of in it.','Years of fields, workflows and customizations nobody fully understands. See <a class="lnk" href="nine-post-customizations.html">which customizations are worth it</a>.','Leads or cases slip through and nobody is sure why.','You are not sure whether to fix your system or start again.'],
  [("Is the CRM Health Check free?","Yes. Free checkups, no obligation."),("What happens after the check?",'You keep the written findings. If you want help with the fixes, <a class="lnk" href="nine-rescue-repair.html">Rescue and Repair</a> is built for that.'),("How long does it take?","[Brian confirms.]")],'crm-health-check')
checkpage('nine-license-check.html','https://www.encloud9.com/dynamics-365-license-check/','Free Dynamics 365 License Check | enCloud9',
  'A free check of your Dynamics 365 licenses, apps and storage, before Microsoft enforces Power Apps licensing more strictly in February 2027.',
  'Free check &middot; License check','License check',
  'A free check of your Dynamics 365 licenses: who has which license, where one base license plus an attach would do, who only needs Team Members, and what Microsoft\'s stricter Power Apps checks from February 2027 mean for you. [Session length, Brian confirms.]',
  ['A list of users whose license may be more than they need, or less.','Where a base plus an attach license would replace two full licenses.','What Microsoft\'s February 2027 Power Apps licensing checks mean for your apps.','Your storage against your limit. See <a class="lnk" href="nine-storage.html">Dataverse storage</a>.'],
  'Who should book a license check?',
  ['Some users only view records or enter time, but have full licenses.','One person holds two full licenses for two apps.','You run custom apps, and are not sure they are covered from February 2027.','Your Microsoft bill has grown and nobody has looked at why.'],
  [("Is the license check free?","Yes. Free checkups, no obligation."),("What changes in February 2027?","Microsoft starts enforcing Power Apps licensing more strictly. Users of model-driven apps, apps in managed environments and apps used outside a Dynamics 365 environment need a qualifying license, or they cannot open the app."),("Do you sell the licenses?","[Brian confirms.]")],'license-check')
print('ok')
