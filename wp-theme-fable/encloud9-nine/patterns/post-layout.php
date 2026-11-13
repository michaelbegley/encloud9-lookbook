<?php
/**
 * Title: Blog post layout
 * Slug: encloud9/post-layout
 * Categories: encloud9
 * Post Types: post
 * Block Types: core/post-content
 * Description: The full designed layout, filled with the words of an existing page. Replace the words.
 */
?>
<!-- wp:encloud9/box {"tag":"div","attrs":{"class":"wrap"},"lock":{"move":true,"remove":true}} -->
<div class="wrap"><!-- wp:encloud9/section -->
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep" aria-hidden="true">/</span><a href="/blog/">Blog</a><span class="sep" aria-hidden="true">/</span><span aria-current="page">Generative pages</span></nav>
<!-- /wp:encloud9/section -->

<!-- wp:encloud9/box {"tag":"article","attrs":{"aria-labelledby":"h1"}} -->
<article aria-labelledby="h1"><!-- wp:encloud9/section -->
<header class="phead">
      <div class="pmain">
        <h1 class="h1 rise" id="h1" style="--d:2">Generative pages in Dynamics 365: what they are and 12 ways to use them</h1>
        <span class="draft rise" style="--d:0"><i aria-hidden="true"></i>Draft for the December theme</span>
        <span class="mono cat rise" style="--d:1">Copilot and AI &middot; Generative pages</span>
        <p class="byline rise" style="--d:3"><span class="av" aria-hidden="true"></span><span>By <b>[Author]</b></span><span><b>[Publish date]</b></span><span>5 min read</span><span>Facts checked on Microsoft Learn, 5 Nov 2026</span></p>
      <div class="acts" style="margin-top:16px"><a class="btn btn-p" href="/lp/schedule-a-meeting/">Book a call</a></div>
      </div>
      <aside class="glance" aria-labelledby="gl-h">
        <p class="mono" id="gl-h">At a glance</p>
        <ul class="gl">
          <li class="lt" style="--c:var(--b9);--k:0"><span class="k">Status, November 2026</span><b>Generally available</b></li>
          <li class="lt" style="--c:var(--b8);--k:1"><span class="k">Data per page</span><b>Up to six Dataverse tables</b></li>
          <li class="lt" style="--c:var(--b6);--k:2"><span class="k">Cost to build</span><b>No extra AI or message credits</b></li>
          <li style="--c:var(--b4);--k:3"><span class="k">Ways to build</span><b>In the browser or with an AI coding tool</b></li>
        </ul>
      </aside>
    </header>
<!-- /wp:encloud9/section -->

<!-- wp:encloud9/box {"tag":"div","attrs":{"class":"pgrid"}} -->
<div class="pgrid"><!-- wp:encloud9/section -->
<nav class="toc" aria-label="On this page">
        <details open id="tocd">
          <summary>On this page</summary>
          <ol>
            <li><a href="#what">What is a generative page?</a></li>
            <li><a href="#build">How do you build one?</a></li>
            <li><a href="#where">Where do generative pages show up?</a></li>
            <li><a href="#uses">What are 12 ways to use generative pages?</a></li>
            <li><a href="#not">When should you not use a generative page?</a></li>
            <li><a href="#start">What do you need to get started?</a></li>
            <li><a href="#status">What is the status and licensing (November 2026)?</a></li>
            <li><a href="#faq">Frequently asked questions</a></li>
            <li><a href="#see">Want to see what one could do for your team?</a></li>
          </ol>
        </details>
      </nav>
<!-- /wp:encloud9/section -->

<!-- wp:encloud9/box {"tag":"div","attrs":{"class":"art","id":"art"},"prose":true} -->
<div class="art" id="art"><!-- wp:paragraph {"className":"answer"} -->
<p class="answer"><span class="mono">The short answer</span><strong>Generative pages let you describe a screen in plain English and get a working page inside a Dynamics 365 app. Microsoft's app agent writes the code and connects it to your Dataverse tables, and you refine it by chatting. They are generally available and fit best when a team needs one focused screen that standard views lack.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="what">What is a generative page?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Dynamics 365 Sales, Customer Service, Field Service and Project Operations run as model-driven apps in Power Apps. A generative page is a new kind of page you can add to those apps.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You describe the page you want. You pick the tables it should use. You can even attach a sketch of the layout. Microsoft's app agent then plans the page, writes React code, and shows you a live preview. If something is off, you tell it what to change, or you edit the code yourself.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The AI does its work while the page is being built. The finished page is an ordinary screen that reads and updates your Dynamics 365 records, and we test it with your users' real security roles before anyone relies on it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="build">How do you build one?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There are two ways.</p>
<!-- /wp:paragraph -->

<!-- wp:encloud9/section -->
<div class="ways">
          <div style="--c:var(--b6)"><span class="mono">Way 1</span><p><strong>In the browser.</strong> In Power Apps, open your model-driven app in the app designer. Choose Add page, then Generative page, then Describe a page. Type what you want, add up to six Dataverse tables, and select Generate page. You watch the agent outline its plan, write the code and render the result. Then you save and publish.</p></div>
          <div style="--c:var(--b3)"><span class="mono">Way 2</span><p><strong>With an AI coding tool.</strong> Microsoft now recommends building generative pages with AI code generation tools such as GitHub Copilot CLI or Claude Code. A planner agent proposes the pages, tables and solution first. You approve the plan, and it builds and deploys. This route can create several pages and their supporting tables in one run.</p></div>
        </div>
<!-- /wp:encloud9/section -->

<!-- wp:paragraph -->
<p>Either way, a person still checks the result. Microsoft is clear that the maker is responsible for validating the code before users rely on it.</p>
<!-- /wp:paragraph -->

<!-- wp:encloud9/section -->
<figure class="shot">
          <div class="frame"><div class="bar" aria-hidden="true"><i></i><i></i><i></i></div><div class="ph">[Screenshot: Power Apps app designer, Add page, Generative page, Describe a page, with a prompt typed in. Take it in the demo environment.]</div></div>
          <figcaption>Where the screenshots go. Real screenshots only, taken in the demo environment on made-up data, with user names and the environment address blurred.</figcaption>
        </figure>
<!-- /wp:encloud9/section -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="where">Where do generative pages show up?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A generative page can live in three places:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>In the app navigation</strong>, as its own page.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Inside a form</strong>, in a section or tab. Once the page is set up to accept a record ID, the form passes in the current record automatically. So you can keep the standard form for data entry and add a richer view beside it.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Opened from another page or from script</strong>, with the record or other inputs passed in.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>To see three of these built, with the limits stated plainly, read <a href="#" data-todo="Examples post URL: goes live with this post (slug generative-pages-dynamics-365-examples)">three screens we built on demo data</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="uses">What are 12 ways to use generative pages?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Here are twelve uses for small and mid-sized teams on Dynamics 365. Some come from Microsoft's own examples, three are the screens in our demo, and the rest are common requests.</p>
<!-- /wp:paragraph -->

<!-- wp:encloud9/section -->
<ol class="uses rev" id="usegrid">
          <li class="use lt" style="--c:var(--b9);--k:0"><span class="hd"><span class="n">1</span><span class="grp">Sales</span></span><b>Top accounts board.</b><span class="x">A ranked gallery of key accounts with revenue and last activity. Microsoft's own examples include an account card gallery and a top accounts dashboard.</span></li>
          <li class="use lt" style="--c:var(--b9);--k:1"><span class="hd"><span class="n">2</span><span class="grp">Sales</span></span><b>Pipeline board.</b><span class="x">Opportunities as cards by stage, so reps see the whole pipeline on one screen.</span></li>
          <li class="use lt" style="--c:var(--b8);--k:2"><span class="hd"><span class="n">3</span><span class="grp">Sales</span></span><b>Account 360 on the account form.</b><span class="x">Relationship health with its reason, win rate, open pipeline by month, contacts and open cases, on one tab before a call.</span></li>
          <li class="use lt" style="--c:var(--b8);--k:3"><span class="hd"><span class="n">4</span><span class="grp">Sales</span></span><b>Opportunity command center.</b><span class="x">The first tab on a deal: revenue, probability, stage, products, overdue follow-ups in red, and the quote.</span></li>
          <li class="use lt" style="--c:var(--b7);--k:4"><span class="hd"><span class="n">5</span><span class="grp">Sales</span></span><b>Quote approvals.</b><span class="x">A list of pending quotes. Tick the ones you are happy with and approve them together. Microsoft shows the same pattern with an order review page that calls a custom API, which is still in preview.</span></li>
          <li class="use lt" style="--c:var(--b6);--k:5"><span class="hd"><span class="n">6</span><span class="grp">Service</span></span><b>Active cases command center.</b><span class="x">Case list, status and trend charts, filters and SLA flags on one page.</span></li>
          <li class="use" style="--c:var(--b5);--k:6"><span class="hd"><span class="n">7</span><span class="grp">Service</span></span><b>Customer history on the case.</b><span class="x">Past cases and recent activity for the same customer, shown inside the case form.</span></li>
          <li class="use" style="--c:var(--b4);--k:7"><span class="hd"><span class="n">8</span><span class="grp">Service</span></span><b>Documents beside the case.</b><span class="x">Files from a SharePoint list shown next to the record. Connector support is still in preview.</span></li>
          <li class="use" style="--c:var(--b3);--k:8"><span class="hd"><span class="n">9</span><span class="grp">Operations and field</span></span><b>Jobs on a map.</b><span class="x">Open work orders or incidents on a map for dispatchers. Microsoft lists "incident reports on a map" as an example prompt.</span></li>
          <li class="use" style="--c:var(--b3);--k:9"><span class="hd"><span class="n">10</span><span class="grp">Operations and field</span></span><b>Equipment gallery with photos.</b><span class="x">Customer assets or products as picture cards, so people find the right one by sight, not by ID.</span></li>
          <li class="use" style="--c:var(--b2);--k:10"><span class="hd"><span class="n">11</span><span class="grp">Leadership and finance</span></span><b>Role-based home pages.</b><span class="x">One start page per role, showing that person's open work.</span></li>
          <li class="use" style="--c:var(--b1);--k:11"><span class="hd"><span class="n">12</span><span class="grp">Leadership and finance</span></span><b>Unbilled time review.</b><span class="x">Time entries waiting for approval or billing, by project.</span></li>
        </ol>
<!-- /wp:encloud9/section -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="not">When should you not use a generative page?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Generative pages are not the answer to everything. Pick something else when:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"not"} -->
<ul class="wp-block-list not"><!-- wp:list-item -->
<li><strong>The job is simple data entry.</strong> A standard form is more consistent and easier to support.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>You need heavy reporting over a lot of data.</strong> Use Power BI. A community tester has noted that generated pages can load data into the browser, which does not suit large volumes.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>People need to ask questions, not open a screen.</strong> Copilot in Dynamics 365 answers questions about your data in a side pane.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>The need is a conversation or an automated process.</strong> Build an agent or workflow in Copilot Studio.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>You need one control reused across many forms.</strong> A PCF code component fits better.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Several makers must edit the same page at once.</strong> Generative pages do not support co-authoring.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Also expect to iterate. A new prompt can change parts of the page you were happy with, so test after each change.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="start">What do you need to get started?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>You need a Dynamics 365 or Power Apps environment with a model-driven app. Microsoft says the maker experience does not need any extra AI or message credits.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For in-browser building, the environment must be in the United States, Great Britain, Australia or Singapore, and prompts are in US English. The AI coding tool route works worldwide on public clouds.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="status">What is the status and licensing (November 2026)?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As of November 2026, generative pages in model-driven apps are generally available. Using Power Platform connectors, Dataverse custom APIs and Application Insights telemetry with generative pages is still in preview. Microsoft does not list a separate end-user license for generative pages. Check your own licensing and admin settings with your partner before you build. Features change often, so confirm details on <a href="https://learn.microsoft.com/power-apps/maker/model-driven-apps/generative-pages">Microsoft Learn</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading" id="faq">Frequently asked questions</h2>
<!-- /wp:heading -->

<!-- wp:encloud9/section -->
<div class="faq">
          <details><summary>What are generative pages in Dynamics 365?</summary><p>They are pages in model-driven apps that Microsoft's app agent builds from a plain-language description. The agent writes React code that reads and updates your Dataverse data.</p></details>
          <details><summary>Are generative pages generally available?</summary><p>Yes. Generative pages in model-driven apps are generally available. Using Power Platform connectors and Dataverse custom APIs with them is still in preview.</p></details>
          <details><summary>Does building generative pages cost extra?</summary><p>Microsoft says the maker experience doesn't require any additional AI or message credits. Users still need a license for the app the page sits in.</p></details>
          <details><summary>What data can a generative page use?</summary><p>Up to six Dataverse tables per page. Power Platform connectors and Dataverse custom APIs are available in preview.</p></details>
          <details><summary>Can I edit the code?</summary><p>Yes. You can keep chatting with the agent or edit the code directly. Each save becomes a new iteration, and you can compare iterations within the same editing session.</p></details>
          <details><summary>Do generative pages replace Power BI or Copilot?</summary><p>No. Use Power BI for heavy analytics, Copilot for questions about your data, and generative pages for focused working screens.</p></details>
        </div>
<!-- /wp:encloud9/section -->

<!-- wp:encloud9/section -->
<section class="abox" aria-labelledby="ab-h">
          <span class="pic" aria-hidden="true"><i style="--c:var(--b9)"></i><i style="--c:var(--b8)"></i><i style="--c:var(--b7)"></i><i style="--c:var(--b6)"></i><i style="--c:var(--b5)"></i><i style="--c:var(--b4)"></i><i style="--c:var(--b3)"></i><i style="--c:var(--b2)"></i><i style="--c:var(--b1)"></i></span>
          <div><h2 class="nm" id="ab-h">About the author: [Author]</h2><p>[Author's role at enCloud9, and one line on the Dynamics 365 work they do.] enCloud9 checks every Microsoft fact in this post on Microsoft Learn before it goes live.</p></div>
        </section>
<!-- /wp:encloud9/section -->

<!-- wp:encloud9/section -->
<div class="ctabox">
          <h2 id="see">Want to see what one could do for your team?</h2>
          <p>Tell us about the screen your team wishes it had. We will show you whether a generative page is the right fit, and what it would take to build it.</p>
          <a class="btn btn-w" href="/lp/schedule-a-meeting/">Book a call with enCloud9</a>
        </div>
<!-- /wp:encloud9/section --></div>
<!-- /wp:encloud9/box --></div>
<!-- /wp:encloud9/box --></article>
<!-- /wp:encloud9/box -->

<!-- wp:encloud9/section -->
<section class="sec" aria-labelledby="nx-h">
    <div class="sec-head rev">
      <h2 class="h2" id="nx-h">Next step</h2>
      <p class="lead">See generative pages on the Copilot page, start with a free checkup, or talk to us.</p>
    </div>
    <div class="nx rev">
      <a class="ptile lt" style="--c:var(--b8)" href="/microsoft-copilot-for-business/#genpages"><span class="pt-top"><span class="mono">Copilot and AI</span><span class="g big" aria-hidden="true"><i></i><i></i><i></i><i></i><i class="on"></i><i></i><i></i><i></i><i></i></span></span><span class="nm">Generative pages</span><span class="ds">How generative pages fit with Copilot and agents in Dynamics 365.</span><span class="pt-foot"><span class="go">See generative pages &rarr;</span></span></a>
      <a class="ptile" style="--c:var(--b4)" href="/free-guides-and-checks/"><span class="pt-top"><span class="mono">Free</span><span class="g big" aria-hidden="true"><i class="on"></i><i class="on"></i><i class="on"></i><i class="m"></i><i class="m"></i><i></i><i></i><i></i><i></i></span></span><span class="nm">Free checkups, no obligation</span><span class="ds">Find out where your system stands before you spend anything.</span><span class="pt-foot"><span class="go">See the checkups &rarr;</span></span></a>
      <a class="ptile" style="--c:var(--b2)" href="/lp/schedule-a-meeting/"><span class="pt-top"><span class="mono">Talk to us</span><span class="g big" aria-hidden="true"><i class="on"></i><i></i><i class="on"></i><i></i><i class="on"></i><i></i><i class="on"></i><i></i><i class="on"></i></span></span><span class="nm">Book a call</span><span class="ds">Tell us about the screen your team wishes it had.</span><span class="pt-foot"><span class="go">Book a call &rarr;</span></span></a>
    </div>
  </section>
<!-- /wp:encloud9/section -->

<!-- wp:encloud9/section -->
<section class="sec" aria-labelledby="rl-h">
    <div class="sec-head rev">
      <h2 class="h2" id="rl-h">Related posts</h2>
      <p class="lead">More on Copilot and Dynamics 365. <a class="lnk" href="/blog/">All posts <span>&rarr;</span></a></p>
    </div>
    <div class="rel rev">
      <a class="pc" style="--c:var(--b7)" href="/blog/microsoft-dynamics-365-crm-skills-copilot/"><span class="mono">Copilot and AI &middot; October 14, 2026</span><span class="t">Microsoft Introduces 30 New Dynamics 365 CRM Skills for Copilot</span><span class="d">Microsoft added 30 CRM skills for Copilot, built on more than 180 Dynamics 365 tools. What they do for sales, service and marketing teams.</span><span class="go">Read the post &#8599;&#xFE0E;</span></a>
      <a class="pc" style="--c:var(--b5)" href="/blog/dynamics-365-sales-qualification-agent/"><span class="mono">Copilot and AI &middot; August 18, 2025</span><span class="t">Smarter Selling with the Dynamics 365 Sales Qualification Agent</span><span class="d">How the Dynamics 365 Sales Qualification Agent researches, scores and follows up with leads against your ideal customer profile, with a worked example.</span><span class="go">Read the post &#8599;&#xFE0E;</span></a>
      <a class="pc" style="--c:var(--b3)" href="/blog/dynamics-365-pricing-licensing-2025-guide/"><span class="mono">Licensing and pricing &middot; Updated November 10, 2026</span><span class="t">Dynamics 365 Pricing and Licensing: The 2026 Guide</span><span class="d">Dynamics 365 prices for 2026: Sales, Customer Service, Field Service and more, plus Copilot costs, licensing rules and what drives your total cost.</span><span class="go">Read the post &#8599;&#xFE0E;</span></a>
    </div>
  </section>
<!-- /wp:encloud9/section --></div>
<!-- /wp:encloud9/box -->

<!-- wp:encloud9/section {"lock":{"move":true,"remove":true}} -->
<section class="final" aria-labelledby="fc-h">
  <div class="wrap">
    <div class="inner">
      <div class="rev">
        <h2 class="h2" id="fc-h">Start with a call or a free checkup</h2>
        <p class="lead">Tell us where your system is today. You get a plan, a package and a price, whether or not you work with us.</p>
      </div>
      <div class="side rev">
        <a class="btn btn-w" href="/lp/schedule-a-meeting/">Book a call</a>
        <a class="lnk" href="/free-guides-and-checks/">Free checkups, no obligation <span>&rarr;</span></a>
        <span class="mono">or call <a href="tel:+18442640729"><span style="white-space:nowrap">1-844-264-0729</span></a></span>
      </div>
    </div>
    
  </div>
  
</section>
<!-- /wp:encloud9/section -->
