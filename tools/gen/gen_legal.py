"""Accessibility statement and privacy policy DRAFTS, Draft 1 (not legal advice; the privacy policy goes to a lawyer before launch).
Measured: live /privacy-policy/ has 6 sections, no date, no named tools, no privacy contact (read 9 Nov 2026); forms are ClickDimensions forms feeding Dynamics 365
(PLATFORM-OPTIONS-9-NOV.md); GA4 via Google Tag Manager (live page source, QA reports); booking through Microsoft Bookings (outlook.office.com bookwithme links).
Everything else bracketed. WCAG level per Brian (W24); never 'ADA compliant'."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from n9base import *
CSS = ('.legal{max-width:760px}.legal h2{margin:48px 0 12px}.legal p,.legal li{font-size:17px;line-height:1.65;color:var(--ink)}.legal ul{padding-left:20px;display:grid;gap:8px}'
       '.draftbar{background:var(--tint,#EAF0F8);border-left:4px solid var(--b5);padding:14px 18px;font-size:15px;margin:0 0 28px}')
def page(fn, url, title, meta, crumb, h1, lead, banner, sections):
    def blk(blocks):
        if blocks and blocks[0] == 'x': return '    <ul>\n' + ''.join(f'      <li>{x}</li>\n' for x in blocks[1:]) + '    </ul>\n'
        return ''.join(f'    <p>{b}</p>\n' for b in blocks)
    body = ''.join(f'    <h2 class="h3" id="s{i}">{e(h)}</h2>\n' + blk(blocks) for i, (h, blocks) in enumerate(sections))
    main = crumbnav([('Home','nine-home.html'),(crumb,None)]) + f'''  <section class="sec" aria-labelledby="h1" style="padding-top:24px">
    <div class="legal">
    <h1 class="h1" id="h1" style="font-size:clamp(36px,4.6vw,60px)">{e(h1)}</h1>
    <p class="draftbar" style="margin-top:20px">{banner}</p>
    <p class="lead" style="margin-top:18px">{lead}</p>
{body}    </div>
  </section>
'''
    hd = mkhead(title, meta, [('Home','https://www.encloud9.com/'),(crumb,url)], css=CSS)
    hd = hd.replace('</head>', '<meta name="robots" content="noindex">\n</head>', 1)  # drafts stay out of search until approved
    write(fn, hd, main)
L = ['x']  # list marker: a list block is ['x', item, item...]
page('nine-accessibility.html','https://www.encloud9.com/accessibility/','Accessibility Statement | enCloud9',
  'How enCloud9 builds encloud9.com to be usable by everyone, the standard we work to, known gaps, and how to tell us about a problem.',
  'Accessibility statement','Accessibility statement',
  'We want everyone to be able to use encloud9.com, including people who use a screen reader, a keyboard, zoom or other assistive technology.',
  'Draft for Brian to approve. [Date published.]',
  [('What standard do we work to?',['We build this site to meet the Web Content Accessibility Guidelines (WCAG) [2.1 level AA, or 2.2 level AA if Brian chooses it].','We test new pages before they go live and again when they change.']),
   ('What do we check?',[L+['Automated accessibility tests on every page at phone and desktop widths.','Keyboard use: every link, button and menu can be reached and used without a mouse, and focus is visible.','Reduced motion: if your device asks for less motion, our animations stop.','Text and color contrast, headings in order, and labels on every form field.','Pages that work at 200% zoom without sideways scrolling.']][0]),
   ('Where might you still have trouble?',[L+['Some parts of the site come from other companies, such as our forms, the booking page and [the chat assistant]. We choose them with accessibility in mind, but we do not control all of their code.','Older blog posts and PDF guides may not meet the standard yet. We fix them as we update them.','[Known gaps found in testing, listed here with a date.]']][0]),
   ('How do I tell you about a problem?',['Call us at <a class="lnk" href="tel:+18442640729">1-844-264-0729</a> (8:00am to 5:00pm Central) or email <a class="lnk" href="mailto:sales@encloud9.com">sales@encloud9.com</a>. Tell us the page and what got in the way. [Response time, Brian confirms.]']),
   ('When was this statement last reviewed?',['[Date of last review.] We review it at least once a year and whenever the site changes in a big way.'])])
page('nine-privacy.html','https://www.encloud9.com/privacy-policy/','Privacy Policy | enCloud9',
  'What information enCloud9 collects on encloud9.com, why, who we share it with, the cookies we use, and how to ask us to see, correct or delete it.',
  'Privacy policy','Privacy policy',
  'This policy explains what information enCloud9 LLC collects when you use encloud9.com, why we collect it, who we share it with, and the choices you have.',
  'DRAFT for legal review. Not legal advice and not in force. A lawyer reviews this before launch; every [bracket] needs an answer. It replaces the current policy, which has no date, names no tools and gives no privacy contact.',
  [('Who we are',['enCloud9 LLC, 2915 Lynnwood Dr., Bellevue, NE 68123. Phone <a class="lnk" href="tel:+18442640729">1-844-264-0729</a>. [Privacy contact email, Brian confirms.]']),
   ('What information do we collect?',[L+['<strong>What you give us:</strong> your name, company, work email, phone and message when you fill in a form, book a call or download a guide.','<strong>How you use the site:</strong> pages visited, links clicked and form activity, collected with cookies and similar tools (see Cookies).','<strong>Chats:</strong> [if the chat assistant goes live: what you type, and how long we keep it].','We do not ask for payment details, health information or government ID numbers on this site.']][0]),
   ('How do we use it?',[L+['To answer you, book calls and send what you asked for, such as a guide.','To follow up about what you asked for, and to send our newsletter if you agree. You can unsubscribe in any email.','To understand how the site is used and improve it.','[Advertising or remarketing: only if Brian decides to run it; describe it here.]']][0]),
   ('Where does it go?',[L+['Our forms send what you enter to our CRM, Microsoft Dynamics 365, through ClickDimensions.','We book calls with Microsoft Bookings.','We measure site use with Google Analytics, loaded through Google Tag Manager. [Microsoft Clarity, if installed.]','[Website host, email and chat providers, listed by name.]','We do not sell your personal information. [Confirm with the lawyer how this fits Nebraska and other state laws.]']][0]),
   ('Cookies',['We use cookies to keep the site working, to measure how it is used, and to connect form fills with earlier visits (ClickDimensions tracking). [Once the cookie banner is built: you can decline non-essential cookies and change your choice at any time.] [Cookie list, after the cookie audit.]']),
   ('Your choices and rights',[L+['Ask to see, correct or delete the information we hold about you.','Opt out of marketing emails at any time.','[State privacy rights that apply, including the Nebraska Data Privacy Act, and how to use them; lawyer.]']][0]),
   ('How long do we keep it?',['[Retention periods for leads, form data, analytics and chat transcripts, Brian and the lawyer decide.]']),
   ('Changes to this policy',['We post any change here with a new date. [Effective date.]'])])
page('nine-terms.html','https://www.encloud9.com/terms-of-use/','Website Terms of Use | enCloud9',
  'The terms for using encloud9.com, including how prices on the site work: Microsoft sets and can change its own prices at any time.',
  'Terms of use','Website terms of use',
  'By using encloud9.com you accept these terms. If you do not accept them, please do not use the site.',
  'DRAFT for legal review. Not legal advice and not in force. Brian asked for the pricing disclaimer (9 Nov 2026); a lawyer reviews the whole page before launch, and every [bracket] needs an answer.',
  [('Who we are',['enCloud9 LLC, 2915 Lynnwood Dr., Bellevue, NE 68123. Phone <a class="lnk" href="tel:+18442640729">1-844-264-0729</a>.']),
   ('Prices on this site',[L+['<strong>Microsoft prices are set by Microsoft.</strong> Prices shown for Microsoft products, licenses and Copilot Credits are Microsoft list prices, given for reference with the date we checked them. Microsoft can change them at any time without notice, and the price you pay is the one in effect when you buy.',
       '<strong>All prices on this site are subject to change.</strong> enCloud9 package and support plan prices are starting prices or ranges. Your price is the one in the written quote or agreement you sign, and that document governs.',
       'Prices on this site are in US dollars and do not include taxes.',
       'Nothing on this site is an offer that you can accept by using the site. Work starts only under a signed agreement.']]),
   ('Information on this site',['We work to keep the site accurate, but it is general information, not advice for your business. Product features, plans and availability are Microsoft\'s to change, and they change often. Check with us before you rely on anything here for a decision.']),
   ('Trademarks',['Microsoft, Dynamics 365, Copilot, Power Platform and related names and logos are trademarks of the Microsoft group of companies. Other product and company names belong to their owners. enCloud9 and its logo belong to enCloud9 LLC.']),
   ('Links to other sites',['We link to other sites, such as Microsoft Learn, for your convenience. We do not control them and are not responsible for their content.']),
   ('No warranty, and limits on liability',['The site is provided as is. [Warranty disclaimer and limitation of liability wording: the lawyer writes this.]']),
   ('Governing law',['[State law that governs these terms, and where disputes are heard: the lawyer and Brian decide.]']),
   ('Changes to these terms',['We may update these terms and will post the new version here with its date. [Effective date.]']),
   ('Contact',['Questions about these terms: call <a class="lnk" href="tel:+18442640729">1-844-264-0729</a> (8:00am to 5:00pm Central). [Legal contact email, Brian confirms.]'])])
print('ok')
