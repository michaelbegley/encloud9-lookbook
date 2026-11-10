"""2026 Dynamics 365 pricing guide as a blog post, Draft 1. Content and every figure from refresh/dynamics-365-pricing-2026-guide.md
(Agent 7, Microsoft pages read 4 Nov 2026, each with its source). URL stays the 2025 slug. Unverified 'most common waste we see' reworded."""
import re, json, html as H
L = '/home/claude/lb/pages/'
s = open(L + 'nine-blog-post.html', encoding='utf-8').read()
URL = 'https://www.encloud9.com/blog/dynamics-365-pricing-licensing-2025-guide/'
TITLE = 'Dynamics 365 Pricing 2026: Licenses, Copilot and Costs'
META = 'Dynamics 365 prices for 2026: Sales, Customer Service, Field Service and more, plus Copilot costs, licensing rules and what drives your total cost.'
H1 = 'Dynamics 365 Pricing and Licensing: The 2026 Guide'
ANS = ('In 2026, Dynamics 365 Sales costs $65 to $150 per user per month, Customer Service costs $50 to $195, Field Service costs $105 and Project Operations costs $135. '
       'These are Microsoft list prices, paid yearly. Paying monthly on an annual plan costs 5% more. Copilot agents run on Copilot Credits, which most plans buy separately.')
FAQ = [
 ("How much does Dynamics 365 cost per user?","At Microsoft list price, paid yearly, Dynamics 365 Sales runs $65 to $150 per user per month, Customer Service $50 to $195, Field Service $105 and Project Operations $135. Customer Insights is priced per company, starting at $1,000 per month with attach pricing."),
 ("Is Copilot included in Dynamics 365?","Partly. Sales Enterprise and Premium include Copilot in Dynamics 365 Sales, Outlook and Teams. Running agents uses Copilot Credits. Sales Premium includes 1,000 credits per user per month; other plans buy credits from $200 per 25,000-credit pack per month or pay as they go."),
 ("What is the cheapest Dynamics 365 license?","For full users, Customer Service Professional and Field Service Contractor are the lowest listed prices at $50 per user per month. For light users, the Team Members license costs less; ask your partner for the current price."),
 ("What is a Dynamics 365 attach license?","An attach license adds a second app to a user who already has a base license, at a lower price than a full license. The base must be the highest-priced app that user needs."),
 ("Can I pay for Dynamics 365 monthly?","Yes. Microsoft's listed prices are for paying yearly. Paying monthly on an annual subscription costs 5% more, a rule Microsoft has applied since 1 April 2025."),
 ("Is there a minimum number of users for Dynamics 365?","Most apps have no minimum on Microsoft's pricing pages. Microsoft Relationship Sales needs 10 seats, and Customer Insights Attach needs 10 or more users of a qualifying Dynamics 365 app."),
 ("Did Dynamics 365 prices go up in 2026?","Microsoft's Dynamics 365 pricing pages show no dated 2026 list price change for these apps. The bigger changes are about AI and storage: Premium plans include Copilot Credits, agents are part of the Sales plans, and storage overage rules are stricter. Microsoft 365 suite prices rose on 1 July 2026."),
]
def tbl(cap, cols, rows):
    th = ''.join(f'<th scope="col">{c}</th>' for c in cols)
    tr = ''.join('<tr><th scope="row">' + H.escape(r[0]) + '</th>' + ''.join(f'<td data-l="{cols[i+1]}">{H.escape(v)}</td>' for i, v in enumerate(r[1:])) + '</tr>' for r in rows)
    return f'<div class="tbl-wrap" tabindex="0" role="region" aria-label="Table, scrolls sideways on small screens"><table class="tbl gtbl"><caption class="mono">{cap}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>\n'
P = lambda t: f'        <p>{t}</p>\n'
body = f'''        <p class="answer"><span class="mono">The short answer</span><strong>{H.escape(ANS)}</strong></p>
        <p class="fine">Prices checked 4 November 2026. All prices are Microsoft US list prices in US dollars, per user per month, paid yearly, unless a row says otherwise. Microsoft changes prices, and your price can differ by country, currency and agreement. Confirm current pricing before you buy.</p>

        <h2 id="prices">How much does each Dynamics 365 app cost in 2026?</h2>
        <h3>Dynamics 365 Sales</h3>
''' + tbl('Dynamics 365 Sales plans', ('Plan','Price','Best for'), [
 ('Sales Professional','$65','Small sales teams that need core pipeline tracking'),('Sales Enterprise','$105','Most B2B sales teams; includes Copilot in Sales, Outlook and Teams'),
 ('Sales Premium','$150','Teams that want 1,000 Copilot Credits per user per month for agents'),('Microsoft Relationship Sales','Not listed; ask Microsoft or a partner','Sales Enterprise plus LinkedIn Sales Navigator; 10-seat minimum')]) + '''        <h3>Customer Service and Contact Center</h3>
''' + tbl('Customer Service and Contact Center plans', ('Plan','Price','Best for'), [
 ('Customer Service Professional','$50','Basic case management'),('Customer Service Enterprise','$105','Full case management, queues, knowledge and service levels'),
 ('Customer Service Premium','$195','Case work and contact center in one plan, with Copilot Credits included'),('Contact Center','$110','Voice and digital channels together'),
 ('Contact Center Digital','$95','Chat and messaging only'),('Contact Center Voice','$95','Phone only')]) + P('Microsoft notes that Contact Center has discount pricing when bought with Customer Service Enterprise. Voice calling runs on Azure Communication Services, which is billed separately.') + '''        <h3>Field Service and Project Operations</h3>
''' + tbl('Field Service and Project Operations plans', ('Plan','Price','Billing basis'), [
 ('Field Service','$105','Per user per month, paid yearly'),('Field Service Contractor','$50','Per user per month, paid yearly'),
 ('Resource Scheduling Optimization add-in','$30','Per resource per month, paid yearly'),('Project Operations','$135','Per user per month, paid yearly')]) + '''        <h3>Customer Insights</h3>
''' + P('Customer Insights is priced per company (tenant), not per user. Users are unlimited.') + tbl('Customer Insights plans', ('Plan','Price per company per month','Includes'), [
 ('Customer Insights','$1,700','100,000 unified people and 10,000 interacted people'),('Customer Insights Attach','$1,000','Same entitlements; needs 10 or more users of a qualifying Dynamics 365 app')]) + '''        <h3>Team Members</h3>
''' + P('Team Members is a low-cost license for people who mostly read data and do light tasks, like entering time or updating a record they own. Microsoft does not show its price on its public Dynamics 365 pricing pages. Ask your partner or check the Microsoft 365 admin center for the current figure.') + f'''
        <h2 id="licensing">How does Dynamics 365 licensing work?</h2>
        <ul>
          <li><strong>One base license per user.</strong> Each full user gets one base license, for the highest-priced app that user needs.</li>
          <li><strong>Attach licenses for more apps.</strong> If the same person needs a second app, you add an attach license at a lower price instead of a second full license. A sales manager on Sales Enterprise who also works service cases gets Sales Enterprise as the base and a Customer Service attach license.</li>
          <li><strong>Team Members for light users.</strong> Staff who only view records, enter time or update a few items can use Team Members. It is limited to set apps and up to 15 tables in a custom app. If a Team Members user starts doing full work, Microsoft expects a full license.</li>
          <li><strong>Minimums.</strong> Most apps have no minimum user count. Microsoft Relationship Sales needs 10 seats, and Customer Insights Attach needs 10 or more users of a qualifying app.</li>
          <li><strong>Yearly or monthly.</strong> Since 1 April 2025, monthly billing on an annual subscription costs 5% more than paying up front.</li>
          <li><strong>Where to buy.</strong> From Microsoft directly, through the Microsoft 365 admin center, or through a Microsoft partner.</li>
        </ul>
        <p>More on base, attach and Team Members on our <a class="lnk" href="nine-d365-licensing.html">Dynamics 365 licensing page</a>.</p>

        <h2 id="copilot">What do Copilot and agents cost in 2026?</h2>
        <p>There are three different AI costs to budget for.</p>
        <p><strong>1. Copilot built into Dynamics 365.</strong> Sales Enterprise and Sales Premium include Copilot in Dynamics 365 Sales, Outlook and Teams at no extra cost. Sales Professional does not. Contact Center plans include Copilot in the service rep desktop, such as case summaries, email help and knowledge answers.</p>
        <p><strong>2. Agents and Copilot Credits.</strong> Agents do work on their own, such as qualifying leads or researching accounts. Running agents uses Copilot Credits. Sales Premium includes 1,000 Copilot Credits per user per month, pooled across your company, and Customer Service Premium also includes credit capacity. Other plans buy credits:</p>
''' + tbl('Copilot Credit options', ('Option','Price','How it bills'), [
 ('Copilot Credit pack','$200 per pack per month','25,000 credits per pack, company-wide, paid up front'),('Pay-as-you-go','Rate per credit not shown on Microsoft\'s pricing page','Billed monthly through an Azure subscription'),
 ('Pre-purchase plan','Up to 20% savings, per Microsoft','One-year commitment, then pay-as-you-go when used up')]) + P('How many credits you use depends on the agent. Microsoft\'s rates include 2 credits for a generative answer, 5 credits for an agent action and 10 credits for tenant graph grounding. One question can use several of these at once.') + P('<strong>3. Microsoft 365 Copilot.</strong> A separate add-on for Word, Excel, Outlook and Teams: $30 per user per month paid yearly, or $31.50 paid monthly with an annual commitment. For businesses up to 300 users, Microsoft 365 Copilot Business is $21 per user per month paid yearly, with a promotion at $18 for the first year for eligible existing customers from 1 July to 31 December 2026. Agents published to Microsoft 365 Copilot carry no extra credit charge for users who have that license. More on our <a class="lnk" href="nine-copilot.html">Copilot and AI page</a>.') + f'''
        <h2 id="total">What drives your total cost?</h2>
        <p>Licenses are only part of the bill.</p>
        <ul>
          <li><strong>Licenses.</strong> Users times price, paid yearly. 10 Sales Enterprise users cost 10 x $105 = $1,050 per month, or $12,600 per year at list price. Paid monthly, the same seats cost about 5% more.</li>
          <li><strong>Storage.</strong> Every company gets a default amount of Dataverse storage, and full user licenses add more. Extra database storage is $40 per GB per month, paid yearly. Once a company passes 100% of its storage, creating, copying and restoring environments is blocked; after 30 days sandboxes go to admin-only mode, and after 90 days sign-in to them is blocked. See <a class="lnk" href="nine-storage.html">Dataverse storage</a>.</li>
          <li><strong>Copilot Credits</strong> if you plan to run agents, unless you are on a Premium plan with credits included.</li>
          <li><strong>Implementation and support.</strong> Setup, data moves, integrations and training depend on your scope. After go-live, you need someone to keep the system healthy.</li>
        </ul>
''' + tbl('enCloud9 support plans, 12-month agreement', ('Plan','Price','Hours included'), [
 ('On-Demand','$200 per hour','Pay as you go'),('Stability','$500 per month','4 hours per month'),('Optimization','$1,500 per month','20 hours per month'),('Partnership','$2,000 per month','35 hours per month')]) + P('Stability is the minimum plan for new clients. So a 10-user Sales Enterprise team with the Stability plan starts at about $1,550 per month before any implementation project or Copilot Credits. See <a class="lnk" href="nine-support.html">support plans</a>.') + '''
        <h2 id="pick">How do you pick the right Dynamics 365 license?</h2>
        <ul>
          <li><strong>Sales team:</strong> start with Sales Enterprise. Choose Professional only if you do not need Copilot or advanced forecasting. Choose Premium if you plan to run agents at volume, since the included credits may cover what you would buy anyway.</li>
          <li><strong>Service team:</strong> start with Customer Service Enterprise. Add Contact Center if you take calls or chats in Dynamics 365. Look at Customer Service Premium if you need both.</li>
          <li><strong>Field team:</strong> Field Service for technicians and dispatchers, Field Service Contractor for outside contractors.</li>
          <li><strong>Project business:</strong> Project Operations for project managers; Team Members for staff who only enter time and expenses.</li>
        </ul>
        <p>Two common ways to overpay: full licenses for people who only need Team Members, and two full licenses where one base plus an attach would do.</p>

        <h2 id="faq">Frequently asked questions</h2>
        <div class="faq">
''' + ''.join(f'          <details><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>\n' for q, a in FAQ) + '''        </div>

        <section class="abox" aria-labelledby="ab-h">
          <span class="pic" aria-hidden="true"><i style="--c:var(--b9)"></i><i style="--c:var(--b8)"></i><i style="--c:var(--b7)"></i><i style="--c:var(--b6)"></i><i style="--c:var(--b5)"></i><i style="--c:var(--b4)"></i><i style="--c:var(--b3)"></i><i style="--c:var(--b2)"></i><i style="--c:var(--b1)"></i></span>
          <div><h2 class="nm" id="ab-h">About the author: Brian Begley</h2><p>Brian is the founder of enCloud9. [One line on his Dynamics 365 work, Brian confirms.] enCloud9 checks every Microsoft price in this guide on Microsoft's own pages before it goes live.</p></div>
        </section>

        <div class="ctabox">
          <h2 id="see">Are you paying for the right licenses?</h2>
          <p>Book a call and we go through your users, apps and storage with you, and show you where you can save or what you are missing.</p>
          <a class="btn btn-w" href="nine-book.html">Book a call with enCloud9</a>
        </div>
'''
art0 = s.index('      <div class="art" id="art">'); art1 = s.index('        <section class="abox"')
end1 = s.index('      </div>\n    </div>\n  </article>')
s = s[:art0] + '      <div class="art" id="art">\n' + body + s[end1:]
# header
s = re.sub(r'<h1 class="h1 rise" id="h1" style="--d:2">.*?</h1>', f'<h1 class="h1 rise" id="h1" style="--d:2">{H1}</h1>', s, 1, re.S)
s = re.sub(r'<span class="draft rise".*?</span>\n', '<span class="draft rise" style="--d:0"><i aria-hidden="true"></i>Refresh of the 2025 guide</span>\n', s, 1, re.S)
s = re.sub(r'<span class="mono cat rise" style="--d:1">.*?</span>', '<span class="mono cat rise" style="--d:1">Pricing and licensing &middot; Dynamics 365</span>', s, 1, re.S)
words = len(re.sub('<[^>]+>', ' ', body).split()); mins = round(words / 230)
s = re.sub(r'<p class="byline rise".*?</p>', f'<p class="byline rise" style="--d:3"><span class="av" aria-hidden="true"></span><span>By <b>Brian Begley</b></span><span>Updated <b>[Publish date]</b></span><span>{mins} min read</span><span>Prices checked on Microsoft\'s pages, 4 Nov 2026</span></p>', s, 1, re.S)
gl = [('b9','Sales','$65 to $150'),('b8','Customer Service','$50 to $195'),('b6','Monthly billing','5% more than yearly'),('b4','Copilot Credit pack','$200 for 25,000')]
s = re.sub(r'<ul class="gl">.*?</ul>', '<ul class="gl">\n' + ''.join(f'          <li{" class=\"lt\"" if i<3 else ""} style="--c:var(--{c});--k:{i}"><span class="k">{k}</span><b>{v}</b></li>\n' for i,(c,k,v) in enumerate(gl)) + '        </ul>', s, 1, re.S)
toc = [('prices','How much does each Dynamics 365 app cost in 2026?'),('licensing','How does Dynamics 365 licensing work?'),('copilot','What do Copilot and agents cost in 2026?'),
       ('total','What drives your total cost?'),('pick','How do you pick the right Dynamics 365 license?'),('faq','Frequently asked questions'),('see','Are you paying for the right licenses?')]
s = re.sub(r'(<summary>On this page</summary>\s*<ol>).*?(</ol>)', lambda m: m.group(1) + '\n' + ''.join(f'            <li><a href="#{a}">{t}</a></li>\n' for a,t in toc) + '          ' + m.group(2), s, 1, re.S)
s = re.sub(r'<span aria-current="page">.*?</span></nav>', '<span aria-current="page">Dynamics 365 pricing 2026</span></nav>', s, 1)
# next step and related
s = re.sub(r'(<h2 class="h2" id="nx-h">Next step</h2>\s*<p class="lead">).*?(</p>)', r'\1See our pricing and licensing pages, start with a free checkup, or talk to us.\2', s, 1, re.S)
s = s.replace('href="nine-copilot.html#genpages"><span class="pt-top"><span class="mono">Copilot and AI</span>', 'href="nine-d365-pricing.html"><span class="pt-top"><span class="mono">Dynamics 365</span>', 1)
s = s.replace('<span class="nm">Generative pages</span><span class="ds">How generative pages fit with Copilot and agents in Dynamics 365.</span><span class="pt-foot"><span class="go">See generative pages &rarr;</span>',
              '<span class="nm">Dynamics 365 pricing</span><span class="ds">Every plan, and what else goes into the bill.</span><span class="pt-foot"><span class="go">See pricing &rarr;</span>', 1)
s = s.replace('<span class="ds">Tell us about the screen your team wishes it had.</span>', '<span class="ds">Ask us which licenses fit your team.</span>', 1)
s = s.replace('<p class="lead">More on Copilot and Dynamics 365.', '<p class="lead">More on Dynamics 365 costs and Copilot.', 1)
s = s.replace('href="https://www.encloud9.com/blog/dynamics-365-sales-qualification-agent/"><span class="mono">Copilot and AI &middot; August 18, 2025</span><span class="t">Smarter Selling with the Dynamics 365 Sales Qualification Agent</span><span class="d">About one of the agents in Dynamics 365 Sales.</span>',
              'href="nine-blog-post.html"><span class="mono">Copilot and AI &middot; Draft</span><span class="t">Generative pages in Dynamics 365: what they are and 12 ways to use them</span><span class="d">Build a Dynamics 365 screen from a plain-language prompt.</span>', 1)
# head
s = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', s, 1)
s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(META)}">', s, 1)
s = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', s, flags=re.S)
ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.encloud9.com/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://www.encloud9.com/blog/"},{"@type":"ListItem","position":3,"name":"Dynamics 365 pricing 2026","item":URL}]},
      {"@context":"https://schema.org","@type":"BlogPosting","headline":H1,"description":META,"url":URL,"author":{"@type":"Person","name":"Brian Begley"},"publisher":{"@type":"Organization","name":"enCloud9","url":"https://www.encloud9.com/"}},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}]
css = ('<style>.art .tbl-wrap{margin:22px 0}.art .gtbl{min-width:0}.art .gtbl caption{text-align:left;padding-bottom:8px}.art h3{margin:28px 0 0}'
       '@media(max-width:640px){.art .gtbl thead{position:absolute;left:-9999px}.art .gtbl tr{display:grid;grid-template-columns:1fr;padding:12px 0;border-bottom:1px solid var(--line)}'
       '.art .gtbl tbody th,.art .gtbl td{display:block;border:0;padding:2px 0}.art .gtbl td::before{content:attr(data-l) ": ";font-family:var(--label);font-size:13px;color:var(--muted)}}</style>\n')
s = s.replace('<style>', ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + css + '<style>', 1)
open(L + 'nine-blog-pricing-2026.html', 'w', encoding='utf-8').write(s)
print('ok words', words, 'min', mins, len(ANS.split()), len(TITLE), len(META))
