"""Omaha page, Draft 1. Live page read 9 Nov 2026: address 2915 Lynnwood Dr., Bellevue, NE 68123; remote with on-site visits for Omaha-area clients.
Brian confirmed on call 27: partner since 2008, CRL a client 15+ years (added). Still dropped: ( 'only', 'trusted across the Midwest', 1 to 7 days). Local proof: REI (Omaha, NE), Aureon (Des Moines, IA) from stories-data."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import gen_ppprod as G
d = dict(url='https://www.encloud9.com/microsoft-dynamics-365-partner-omaha/', name='Omaha and Nebraska', h1=('Dynamics 365 partner','in Omaha'),
  parent=('About enCloud9','https://www.encloud9.com/about-encloud9/','nine-about.html'), seelink='See what we do',
  title='Dynamics 365 Partner in Omaha, Nebraska | enCloud9', kicker='Omaha &middot; Nebraska',
  meta='enCloud9 is a Microsoft Dynamics 365 partner in Bellevue, in the Omaha metro. We build, fix and support Dynamics 365 for Nebraska businesses and beyond.',
  answer=('enCloud9 is a Microsoft Dynamics 365 partner based in Bellevue, in the Omaha metro. We build, fix and support Dynamics 365 Sales and Customer Service for businesses in Nebraska, Iowa and across the US. '
          'A Microsoft Partner since 2008. Most work runs remotely, with on-site visits for Omaha-area clients when needed.'),
  caption='What we do for Omaha businesses', cols=('Service','What it covers','Price'),
  plans=[('Full implementation','A new Dynamics 365 system, with data moves and integrations','From $20,000, quoted in writing'),
         ('Rescue and Repair','An existing Dynamics 365 system that is stalled or over-customized','$500 to $10,000, quoted in writing'),
         ('Sales Accelerator','A first Dynamics 365 Sales system, fixed scope','$7,500'),
         ('Service Accelerator','A first Customer Service system, fixed scope','$7,500'),
         ('Support plans','Help after go-live, on a 12-month agreement','From $500 a month')],
  note='Microsoft licenses are a separate cost from our work. <a class="lnk" href="nine-packages.html">See all packages</a>',
  plan_h='What does enCloud9 do for Omaha businesses?', plan_lead='The same packages we run for clients across the US: a new system, a rescue of one that is not working, a fixed-scope accelerator, and support after go-live.',
  cells=[('b1','#fit','Based in','Bellevue, NE','The Omaha metro','&#8600;',''),('b2','#plans','Builds','Dynamics 365','Sales and Customer Service','&#8600;',''),('b3','nine-story-rei.html','Omaha client','REI','Five divisions on one CRM','&#8599;',''),
         ('b4','nine-story-aureon.html','Iowa client','Aureon','Des Moines, IA','&#8599;',''),('b5','#plans','enCloud9','Local partner','Clients across the US','','core'),
         ('b6','nine-packages.html','Packages','Fixed scope','Quoted in writing','&#8599;','lt'),('b7','nine-support.html','After go-live','Support','From $500 a month','&#8599;','lt'),
         ('b8','nine-stories.html','Proof','23 client stories','What we built','&#8599;','lt'),('b9','nine-contact.html','Visit','Contact us','Phone, email, address','&#8599;','lt')],
  fit_h='Who do we work with in the Omaha area?', fit_lead='Growing businesses that sell or serve customers and run, or want to run, Dynamics 365. One of them is right here in Omaha.',
  fit_title='Local proof', fit=['<a class="lnk" href="nine-story-rei.html">Radio Engineering Industries (REI)</a>, Omaha: we moved REI to Dynamics 365 Online and built sales processes for its five divisions.',
       '<a class="lnk" href="nine-story-aureon.html">Aureon</a>, Des Moines, Iowa: we audited a CRM staff did not trust and built the plan to fix it.',
       'Our office: 2915 Lynnwood Dr., Bellevue, NE 68123. Call <a class="lnk" href="tel:+18442640729">1-844-264-0729</a>.',
       'Clients across the US. See all <a class="lnk" href="nine-stories.html">client stories</a>.'],
  faq=[("Is enCloud9 based in Omaha?","Yes. Our office is at 2915 Lynnwood Dr., Bellevue, NE 68123, in the Omaha metro. We work with clients in Nebraska, Iowa and across the US."),
       ("Do you work on site or remotely?","Mostly remotely, through Teams and screen sharing. For Omaha-area clients, we visit on site when the work needs it."),
       ("What Dynamics 365 work do you do?","We build new Dynamics 365 systems, rescue ones that are not working, run fixed-scope accelerators for Sales and Customer Service, and support systems after go-live."),
       ("How long does a Dynamics 365 project take?","Each package has a written scope and timeline, set before we start. A fixed-scope accelerator is shorter than a full implementation with data moves and integrations."),
       ("How long have you worked with your clients?",'enCloud9 has been a Microsoft Partner since 2008. <a class="lnk" href="nine-story-crl.html">Clinical Reference Laboratories</a> has been a client for more than 15 years.'),
       ("Do you have Omaha clients?",'Yes. One is <a class="lnk" href="nine-story-rei.html">Radio Engineering Industries</a> in Omaha, which runs its five divisions on Dynamics 365.')],
  related=[('nine-about.html','Company','About enCloud9'),('nine-story-rei.html','Client story','REI, Omaha'),('nine-packages.html','Packages','All packages'),('nine-contact.html','Company','Contact us')])
G.render('nine-omaha.html', d)
