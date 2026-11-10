"""How we work page, Draft 1. Stages, change-order line and support section reused word for word from the Sales Accelerator page (Draft 2)
with the same generic edits as the Accelerators hub; remote and on-site line from the live Omaha page (read 9 Nov). Team and cadence bracketed for Brian."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
st = base[base.index('    <div class="stages flowbar">'):]; st = st[:st.index('  </section>')].rstrip('\n')
st = (st.replace('Build Dynamics 365 Sales to the plan', 'Build to the plan').replace('We build Dynamics 365 Sales to the plan', 'We build Dynamics 365 to the plan')
        .replace('We learn how you sell, using', 'We learn how your team works, using').replace('users, sales stages, data to move', 'users, stages or queues, data to move'))
sup = base[base.index('  <section class="sec" id="support"'):]; sup = sup[:sup.index('  </section>') + len('  </section>')]
URL = 'https://www.encloud9.com/about-encloud9/how-we-work/'
TITLE = 'How We Work on Dynamics 365 Projects | enCloud9'
META = 'How an enCloud9 Dynamics 365 project runs: a written plan and price first, four stages from plan to support, and every change approved in writing.'
ANSWER = ('Every project runs through the same four stages: Plan, Build, Go live and Run. You see the scope, timeline and price in writing before we start, '
          'and every change after that is a written change order you approve. After go-live, a support plan keeps the system healthy, from $500 a month.')
FAQ = [("What do we get in writing before you start?","A written plan with the scope, the timeline and a fixed price for our build work. Microsoft licenses are a separate cost."),
       ("What if we need something the plan does not cover?","Anything outside the plan is a written change order you approve before work starts."),
       ("Do you work on site or remotely?","Mostly remotely, through Teams and screen sharing. For Omaha-area clients, we visit on site when the work needs it."),
       ("Who will we work with?","[Brian confirms: who leads a project and who does the build work.]"),
       ("How often will we hear from you during a project?","[Brian confirms: the regular check-in during a project.]"),
       ("What happens after go-live?","Your support plan starts. Health checks and updates are logged, so you always know what changed. Plans start at $500 a month for 4 hours.")]
cells = [('b1','#stages','Stage A','Plan','Written plan and price first','&#8600;',''),('b2','#stages','Stage B','Build','Standard features first','&#8600;',''),
         ('b3','#stages','Stage C','Go live','Training and cut-over day','&#8600;',''),('b4','#stages','Stage D','Run','Support plan starts','&#8600;',''),
         ('b5','#writing','enCloud9','In writing','Scope, price, changes','','core'),('b6','#support','After go-live','Support','From $500 a month','&#8600;','lt'),
         ('b7','nine-packages.html','Packages','Fixed scope','Quoted in writing','&#8599;','lt'),('b8','nine-stories.html','Proof','23 client stories','What we built','&#8599;','lt'),
         ('b9','nine-guides.html','Start free','Free checks','No obligation','&#8599;','lt')]
main = crumbnav([('Home','nine-home.html'),('About','nine-about.html'),('How we work',None)]) + f'''  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">About &middot; How we work</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">How we work</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="#stages">See the four stages <span>&rarr;</span></a></div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
{grid('How an enCloud9 project runs', cells)}    </div>
  </section>

  <section class="sec" id="stages" aria-labelledby="st-h">
    <div class="sec-head rev">
      <h2 class="h2" id="st-h">What are the four stages of a project?</h2>
      <p class="lead">Plan, Build, Go live and Run. You see the written plan before we build, and every change after that is written down and approved.</p>
    </div>
{st}
  </section>

  <section class="sec" id="writing" aria-labelledby="wr-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="wr-h">What do you put in writing?</h2>
      <p class="lead">Everything that affects your budget or your timeline. You never find out about a change from an invoice.</p>
      <div class="acts" style="margin-top:0"><a class="btn btn-p" href="nine-packages.html">See the packages</a></div>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">In writing, before work starts</h3><ul>
        <li>The scope: what is included and what is not.</li>
        <li>The timeline, stage by stage.</li>
        <li>A fixed price for our build work. Microsoft licenses are a separate cost.</li>
        <li>Any change: anything outside the plan is a written change order you approve before work starts.</li>
      </ul></div>
    </div>
    </div>
  </section>

  <section class="sec" id="team" aria-labelledby="tm-h">
    <div class="fitsplit">
    <div class="side rev">
      <h2 class="h2" id="tm-h">Who does the work, and how do we stay in touch?</h2>
      <p class="lead">Mostly remote, through Teams and screen sharing, with on-site visits for Omaha-area clients when the work needs it.</p>
    </div>
    <div class="fit rev">
      <div class="yes"><h3 class="h3">During a project</h3><ul>
        <li>[Brian confirms: who leads your project and who builds it.]</li>
        <li>[Brian confirms: how often you get a check-in, and in what form.]</li>
        <li>You check your imported records against your old system before sign-off.</li>
        <li>Health checks and updates are logged after go-live, so you always know what changed.</li>
      </ul></div>
    </div>
    </div>
  </section>

{sup}

''' + faqsec('Questions about working with us', FAQ) + '\n' + lnav('Related', [
  ('nine-about.html','Company','About enCloud9'),('nine-packages.html','Packages','All packages'),('nine-support.html','After go-live','Support plans'),('nine-contact.html','Company','Contact us')])
hd = mkhead(TITLE, META, [('Home','https://www.encloud9.com/'),('About','https://www.encloud9.com/about-encloud9/'),('How we work',URL)], faq=FAQ)
write('nine-how-we-work.html', hd, main)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
