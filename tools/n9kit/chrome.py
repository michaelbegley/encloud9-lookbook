"""Shared header and footer for look 9 concept pages. Usage: python3 chrome.py page.html SECTION
SECTION is one of: home d365 marketing copilot packages stories about (marks the current nav item).
Replaces everything from <header class="top"> to </header>, and from <footer class="foot"> to </footer>."""
import sys,re
NAV=[('d365','nine-dynamics-365.html','Dynamics 365'),('marketing','nine-marketing.html','Marketing'),('copilot','nine-copilot.html','Copilot and AI'),
     ('packages','nine-packages.html','Packages'),('stories','nine-stories.html','Stories'),('blog','nine-blog.html','Blog'),('about','nine-about.html','About')]
GROUPS={
 'd365':[('Apps',[('All Dynamics 365 apps','nine-dynamics-365.html'),('Dynamics 365 Sales','nine-dynamics-365-sales.html'),('Customer Service','nine-customer-service.html'),('Field Service','nine-field-service.html'),('Contact Center','nine-contact-center.html'),('Customer Insights','nine-customer-insights.html'),('Project Operations','nine-project-operations.html')]),
         ('Plan and buy',[('Dynamics 365 pricing','nine-d365-pricing.html'),('Dynamics 365 licensing','nine-d365-licensing.html'),('Compare with Salesforce and HubSpot','nine-vs-crm.html'),('Document Core Pack','nine-document-core-pack.html'),('Email Verifier','nine-email-verifier.html')]),
         ('Industries',[('Healthcare','nine-healthcare.html'),('Distribution','nine-distribution.html'),('Professional services','nine-professional-services.html'),('Manufacturing','nine-manufacturing.html'),('Omaha and Nebraska','nine-omaha.html')])],
 'copilot':[('Copilot and AI',[('Copilot and agents','nine-copilot.html'),('Generative pages','nine-copilot.html#genpages'),('Copilot Studio','nine-copilot-studio.html')]),
            ('Power Platform',[('Power Platform family','nine-power-platform.html'),('Power Apps','nine-power-apps.html'),('Power BI','nine-power-bi.html')])],
 'packages':[('Packages',[('All packages','nine-packages.html'),('Full implementation','nine-full-implementation.html'),('Rescue and Repair','nine-rescue-repair.html'),('Accelerators','nine-accelerators.html'),('Sales Accelerator','nine-sales-accelerator.html'),('Service Accelerator','nine-service-accelerator.html')]),
             ('Move to Dynamics 365',[('From Salesforce','nine-move-salesforce.html'),('From HubSpot','nine-move-hubspot.html'),('From Zoho','nine-move-zoho.html'),('From monday.com','nine-move-monday.html')]),
             ('After go-live',[('Support plans','nine-support.html'),('Free guides and checks','nine-guides.html'),('CRM Health Check','nine-health-check.html'),('License check','nine-license-check.html')])],
 'about':[('Company',[('About enCloud9','nine-about.html'),('How we work','nine-how-we-work.html'),('Team','nine-team.html'),('Contact us','nine-contact.html'),('All questions','nine-faq.html')])],
}
CHEV='<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true" focusable="false"><path d="M1.5 3.5 5 7l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
def header(cur):
    items=''
    for k,h,t in NAV:
        a=f'<a href="{h}"'+(' class="cur"' if k==cur else '')+f'>{t}'+('<span class="sr-only"> (current section)</span>' if k==cur else '')+'</a>'
        if k in GROUPS:
            cols=''.join(f'<div class="pcol"><b>{g}</b>'+''.join(f'<a href="{hh}">{tt}</a>' for tt,hh in links)+'</div>' for g,links in GROUPS[k])
            items+=(f'<div class="nav-i">{a}<button class="nav-x" type="button" aria-expanded="false" aria-controls="p-{k}"><span class="sr-only">{t} pages</span>{CHEV}</button>'
                    f'<div class="panel" id="p-{k}" hidden><div class="wrap pgrid">{cols}</div></div></div>')
        else: items+=f'<div class="nav-i">{a}</div>'
    m=''
    for k,h,t in NAV:
        if k in GROUPS:
            m+=f'<details><summary>{t}</summary>'+''.join(f'<b>{g}</b>'+''.join(f'<a href="{hh}">{tt}</a>' for tt,hh in links) for g,links in GROUPS[k])+'</details>'
        else: m+=f'<a href="{h}">{t}</a>'
    return f'''<header class="top">
  <a class="skip" href="#main">Skip to main content</a>
  <div class="wrap">
    <a class="logo" href="nine-home.html" aria-label="enCloud9 home"><img src="../assets/brand/enCloud9-wordmark-blue.svg" alt="enCloud9" width="104" height="34"></a>
    <nav class="nav" aria-label="Main">{items}</nav>
    <a class="tel" href="tel:+18442640729">1-844-264-0729</a>
    <a class="btn btn-p" href="nine-book.html">Book a call</a>
    <a class="btn btn-p call-m" href="tel:+18442640729">Call</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav">Menu</button>
  </div>
  <nav class="mnav" id="mnav" aria-label="Mobile">{m}<a href="tel:+18442640729">Call 1-844-264-0729</a>
    <a class="btn btn-p" href="nine-book.html">Book a call</a>
  </nav>
</header>'''
FOOT='''<footer class="foot">
      <div class="fcols">
        <div><img src="../assets/brand/enCloud9-wordmark-white.svg" alt="enCloud9" width="84" height="28"><p>Microsoft Partner since 2008, specializing in Dynamics 365.</p><p><a href="tel:+18442640729">1-844-264-0729</a><br>8:00am to 5:00pm Central</p></div>
        <nav aria-label="Dynamics 365"><b>Dynamics 365</b><a href="nine-dynamics-365.html">All Dynamics 365 apps</a><a href="nine-dynamics-365-sales.html">Dynamics 365 Sales</a><a href="nine-customer-service.html">Customer Service</a><a href="nine-marketing.html">Marketing automation</a><a href="nine-d365-pricing.html">Dynamics 365 pricing</a><a href="nine-vs-crm.html">Compare with Salesforce and HubSpot</a></nav>
        <nav aria-label="Copilot and Power Platform"><b>Copilot and AI</b><a href="nine-copilot.html">Copilot and agents</a><a href="nine-copilot.html#genpages">Generative pages</a><a href="nine-power-platform.html">Power Platform</a><a href="nine-copilot-studio.html">Copilot Studio</a><a href="nine-power-apps.html">Power Apps</a><a href="nine-power-bi.html">Power BI</a></nav>
        <nav aria-label="Packages and support"><b>Packages and support</b><a href="nine-packages.html">All packages</a><a href="nine-full-implementation.html">Full implementation</a><a href="nine-sales-accelerator.html">Sales Accelerator</a><a href="nine-service-accelerator.html">Service Accelerator</a><a href="nine-rescue-repair.html">Rescue and Repair</a><a href="nine-support.html#plans">Support plans</a></nav>
        <nav aria-label="Industries"><b>Industries</b><a href="nine-healthcare.html">Healthcare</a><a href="nine-distribution.html">Distribution</a><a href="nine-professional-services.html">Professional services</a><a href="nine-manufacturing.html">Manufacturing</a><a href="nine-omaha.html">Omaha and Nebraska</a></nav>
        <nav aria-label="Company"><b>Company</b><a href="nine-about.html">About enCloud9</a><a href="nine-how-we-work.html">How we work</a><a href="nine-team.html">Team</a><a href="nine-stories.html">Client stories</a><a href="nine-blog.html">Blog</a><a href="nine-contact.html">Contact us</a><a href="nine-faq.html">All questions</a><a href="nine-guides.html">Free guides and checks</a></nav>
      </div>
      <div class="tm">enCloud9 LLC, 2915 Lynnwood Dr., Bellevue, NE 68123. Serving clients across the US. Microsoft, Dynamics 365 and Copilot are trademarks of the Microsoft group of companies. Prices are subject to change; Microsoft sets its own prices. <a href="nine-terms.html">Terms of use</a> &middot; <a href="nine-privacy.html">Privacy policy</a> &middot; <a href="nine-accessibility.html">Accessibility statement</a></div>
    </footer>'''
f,cur=sys.argv[1],sys.argv[2]
s=open(f).read()
s,n1=re.subn(r'<header class="top">.*?</header>',lambda m:header(cur),s,count=1,flags=re.S)
s,n2=re.subn(r'<footer class="foot">.*?</footer>',lambda m:FOOT,s,count=1,flags=re.S)
assert n1==1 and n2==1,(n1,n2)
open(f,'w').write(s);print(f,'ok')
