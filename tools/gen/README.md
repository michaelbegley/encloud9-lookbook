# Page generators and helpers (moved from the session scratchpad at handoff, 10 Nov 2026)

- gen_*.py write concept pages into pages/ (gen_support, gen_faq, gen_legal, gen_acc, gen_story...). After any generator, run
  `python3 tools/gen/finish.py <page>:<section>` (sections per page in allsec.txt) to re-apply the shared header and footer
  from tools/n9kit/chrome.py, then `python3 tools/build_site.py`.
- n9base.py: shared helpers the generators import. finish.py: re-applies chrome and relinks.
- sitewide.py: the site-wide copy fixes of 9 Nov (pass page and generator paths).
- ldedit.py: add an Offer or missing FAQ questions to a page's JSON-LD.
- STANDARD.txt: plain-text copy of the Page Quality Standard for reviewer agents (the live standard is the Claude Doc).
- *.js: one-off Playwright helpers (screenshots, axe detail, list check).
Paths assume the repo is cloned at /home/claude/lb.

- STALE GENERATORS (10 Nov 2026): since the 9 Nov site-wide fixes and the Draft 2 reviews, pages are edited directly in pages/. gen_pp.py, gen_ppprod.py and most other generators no longer reproduce the approved pages (tested 10 Nov: rerunning gen_ppprod.py changed 5 pages, including old wording that failed review). Do not rerun a page generator on a reviewed page. gen_faq.py is the exception: rerun it after any page FAQ change.
- con.js was renamed console-check.js (10 Nov): CON is a reserved file name on Windows and broke a clone there.
