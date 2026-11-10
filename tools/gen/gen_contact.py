"""Contact page, Draft 1. Address and email measured on the live /contact-us/ page, 9 Nov 2026. Hours from the shared footer (W11 open)."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
URL = 'https://www.encloud9.com/contact-us/'
TITLE = 'Contact enCloud9 | Dynamics 365 Partner'
META = 'Book a call, phone 1-844-264-0729 or email sales@encloud9.com. enCloud9 is a Dynamics 365 partner in Bellevue, Nebraska, serving clients across the US.'
ANSWER = ('The fastest way to reach us is to book a call, or phone 1-844-264-0729 from 8:00am to 5:00pm Central. You can also email '
          'sales@encloud9.com or use the form below. We are a Dynamics 365 partner in Bellevue, Nebraska, and we work with clients across the US.')
FAQ = [
 ("What happens on the first call?", "You tell us where your system is today and what is not working. You get a straight answer on what fits, whether or not you work with us."),
 ("Is the first call free?", "Yes. Free checkups, no obligation."),
 ("Where is enCloud9 located?", "Our office is at 2915 Lynnwood Dr., Bellevue, NE 68123. We work with clients across the US."),
 ("What are your phone hours?", "Call 1-844-264-0729 from 8:00am to 5:00pm Central, Monday to Friday."),
 ("I am already a client. How do I get help?", 'Call 1-844-264-0729 or see our <a class="lnk" href="nine-support.html">support plans</a>.'),
]
css = ('.cform{display:grid;gap:14px;max-width:640px}.cform label{display:grid;gap:6px;font-size:15px;color:var(--ink)}'
       '.cform input,.cform textarea{font:inherit;padding:12px 14px;border:1px solid var(--line);background:#fff;color:var(--ink)}'
       '.cform textarea{min-height:140px}.cform .ck{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:var(--muted)}'
       '.cform .ck input{margin-top:4px}.cform .msg{font-size:15px;color:var(--ink);padding:12px 14px;background:var(--tint,#EAF0F8)}'
       '.csplit{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(32px,5vw,72px);align-items:start}'
       '@media(max-width:860px){.csplit{grid-template-columns:1fr}}')
hd = mkhead(TITLE, META, [('Home','https://www.encloud9.com/'),('Contact us',URL)], faq=FAQ, css=css,
  extra_ld=[{"@context":"https://schema.org","@type":"ContactPage","url":URL,"about":{"@type":"Organization","name":"enCloud9","telephone":"+1-844-264-0729","email":"sales@encloud9.com",
   "address":{"@type":"PostalAddress","streetAddress":"2915 Lynnwood Dr.","addressLocality":"Bellevue","addressRegion":"NE","postalCode":"68123","addressCountry":"US"}}}])
cells = [
 ('b1', BOOK, 'Fastest', 'Book a call', 'Pick a time that suits you', '&#8599;', ''),
 ('b2', 'tel:+18442640729', 'Phone', 'Call us', '1-844-264-0729, 8:00am to 5:00pm Central', '&#8599;', ''),
 ('b3', 'mailto:sales@encloud9.com', 'Email', 'Email us', 'sales@encloud9.com', '&#8599;', ''),
 ('b4', '#form', 'Form', 'Send a note', 'Tell us what you need', '&#8600;', ''),
 ('b5', '#visit', 'enCloud9', 'Bellevue, NE', 'Serving clients across the US', '', 'core'),
 ('b6', 'nine-packages.html', 'Packages', 'What we sell', 'Fixed scope, quoted in writing', '&#8599;', 'lt'),
 ('b7', 'nine-stories.html', 'Proof', '23 client stories', 'What we built for others', '&#8599;', 'lt'),
 ('b8', 'nine-support.html', 'Clients', 'Support', 'Already a client? Start here', '&#8599;', 'lt'),
 ('b9', 'nine-faq.html', 'Questions', 'All questions', 'Every answer on one page', '&#8599;', 'lt'),
]
main = crumbnav([('Home','nine-home.html'),('Contact us',None)]) + f'''  <section class="hero" aria-labelledby="h1">
    <div class="copy">
      <span class="mono rise" style="--d:0">Contact &middot; enCloud9</span>
      <h1 class="h1" id="h1" style="font-size:clamp(40px,5.4vw,72px)"><span class="ln"><span style="--d:1">Talk to</span></span> <span class="ln"><span style="--d:2">enCloud9</span></span></h1>
      <p class="lead rise" style="--d:3">{e(ANSWER)}</p>
      <div class="acts rise" style="--d:4"><a class="btn btn-p" href="{BOOK}">Book a call</a><a class="lnk" href="#form">Send a note <span>&rarr;</span></a></div>
      <p class="phone-note rise" style="--d:5">Prefer the phone? Call <a href="tel:+18442640729">1-844-264-0729</a>.</p>
    </div>
    <div>
{grid('Ways to reach enCloud9', cells)}    </div>
  </section>

  <section class="sec" id="form" aria-labelledby="fm-h">
    <div class="csplit">
    <div class="rev">
      <h2 class="h2" id="fm-h">How do I send enCloud9 a note?</h2>
      <p class="lead">Fill in the form and we get back to you. If it is urgent, call 1-844-264-0729.</p>
      <div id="visit" style="margin-top:32px">
        <h3 class="h3">Where are you?</h3>
        <p>enCloud9 LLC<br>2915 Lynnwood Dr.<br>Bellevue, NE 68123</p>
        <p class="fine">We work with clients across the US.</p>
      </div>
    </div>
    <form class="cform rev" id="cform" novalidate>
      <label>Your name<input name="name" autocomplete="name" required></label>
      <label>Company name<input name="company" autocomplete="organization" required></label>
      <label>Work email<input name="email" type="email" autocomplete="email" required></label>
      <label>What do you need?<textarea name="msg" required></textarea></label>
      <label class="ck"><input type="checkbox" name="ok" required> <span>I agree to the <a class="lnk" href="https://www.encloud9.com/privacy-policy/">privacy policy</a>.</span></label>
      <div><button class="btn btn-p" type="submit">Send</button></div>
      <p class="msg" id="cmsg" role="status" hidden></p>
    </form>
    </div>
  </section>

''' + faqsec('Contact questions we get asked', FAQ) + '\n' + lnav('Next steps', [
  ('nine-packages.html','Packages','All packages'),('nine-stories.html','Proof','Client stories'),('nine-support.html','Clients','Support plans'),('nine-about.html','Company','About enCloud9')])
main += '''<script>
(function(){var f=document.getElementById('cform'),m=document.getElementById('cmsg');if(!f)return;
f.addEventListener('submit',function(ev){ev.preventDefault();if(!f.checkValidity()){m.hidden=false;m.textContent='Please fill in every field and tick the privacy box.';f.reportValidity();return;}
m.hidden=false;m.textContent='Concept form: not connected yet. On the live site this goes to our CRM. For now, email sales@encloud9.com or book a call.';});})();
</script>
'''
write('nine-contact.html', hd, main)
print('ok', len(ANSWER.split()), len(TITLE), len(META))
