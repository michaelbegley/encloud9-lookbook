#!/usr/bin/env python3
"""Site-wide consistency check (G2 by machine). Usage: python3 tools/consistency.py [pages/*.html]

One canonical list of facts, each with the wrong variants that have turned up on the site.
Every page's visible text and JSON-LD is searched; any wrong variant is reported with the page and a snippet.
Exit code 1 if anything is found. Add a fact here the day it is decided (source and date in the note).
"""
import glob, html, os, re, sys

FACTS = [
    ("Fort Myers spelling", "Fort Myers, FL", [r"Fort Meyers"], "bgland.json facts; REVIEW-G7B issue 6"),
    ("Competitor price read date", "read 10 Nov 2026", [r"each vendor's own pricing page, checked 4 Nov 2026"], "Salesforce and HubSpot only (Microsoft-only pages keep their own check date); FACTCHECK-G6 read all vendor prices 10 Nov; REVIEW-G7B issue 6"),
    # (fact, canonical, [regex of wrong variants], note)
    ("Partnership price", "from $2,000 a month", [r"\$2,000\+", r"\bat \$2,000\b", r"Partnership is \$2,000", r"data-l=\"Price\">\$2,000 a month"], "Brian call 23 '$2,000+'; site wording 9 Nov"),
    ("Full implementation price", "from $20,000", [r"\$24,000", r"from \$2[1-9],000"], "Brian call 27 and Teams '20', 9 Nov"),
    ("Rescue and Repair price", "$500 to $10,000", [r"Rescue[^.]{0,60}\$(?!500\b)\d[\d,]* to"], "Brian call 27"),
    ("Accelerator price", "$7,500 per accelerator (Sales, Service); Marketing $5,000 until Brian says otherwise", [r"(?<!Sales and Service )(?<!Service )Accelerators are \$7,500"], "Brian call 27; answer 1, 11 Nov 2026: per accelerator"),
    ("On-Demand rate", "$200 an hour", [r"\$2(10|25|75) an hour"], "Brian call 27"),
    ("Support plans start", "$500 a month", [r"support plans? (start|from) (at )?\$(?!500)\d"], "Brian 4 Nov"),
    ("Phone", "1-844-264-0729", [r"\(844\) ?264", r"844\.264", r"844 264 0729"], "live contact page"),
    ("Open hours", "not displayed (support response window 7:00am to 5:00pm stays)", [r"8:00 ?am to 5:00 ?pm", r"(open|office|phone) hours"], "Brian's answer 23, 11 Nov 2026: business hours not displayed"),
    ("Partner year", "2008", [r"partner since (2006|2009)", r"since (2006|2009)", r"\b20 years\b"], "Brian's answer 18, 11 Nov 2026: 2008"),
    ("CRL name", "Clinical Reference Lab (CRL)", [r"Clinical Reference Laboratories", r"Clinical Reference Labs\b"], "site standard, 10 Nov"),
    ("Compana name", "Compana Pet Brands", [r"Compana Pet Products", r">Compana<"], "Brian call 27"),
    ("Compana Copilot Studio", "built and deployed to production", [r"Compana[^.]{0,40}is testing Copilot"], "Brian's answer 15, 11 Nov 2026"),
    ("monday.com", "monday.com", [r"(?-i:Monday CRM)", r"(?-i:Monday\.com)"], "vendor spelling"),
    ("Brand blue", "#355DA6", [r"#255DA6"], "Michael 2 Nov"),
    ("Fit wording", "consider another option if", [r"not a fit", r"none of our packages"], "Brian call 23"),
    ("Microsoft Partner", "Microsoft Partner", [r"(became|are|is) a Microsoft partner", r"Microsoft Solutions Partner"], "Brian call 23: capital P; Solutions designation lapsed"),
    ("No featured Hogan", "not featured", [r'class="(story|cell)[^"]*"[^>]*href="nine-story-hogan'], "Brian 4 Nov; card in the stories list is fine"),
    ("No MSA proof", "not used as proof", [r'href="nine-story-msa"[^>]*class="cell', r"health compliance compan"], "Brian call 27"),
    ("Accent never orange", "no orange", [r"#F[0-9A-F]{1}8[0-9A-F]{3}\b(?=[^\n]{0,40}orange)"], "Brian 4 Nov"),
]

def text_of(path):
    s = open(path, encoding="utf-8").read()
    ld = " ".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S))
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S)
    vis = html.unescape(re.sub(r"<[^>]+>", " ", body))
    # raw markup is searched too, for href and class based rules
    return re.sub(r"\s+", " ", vis + " " + ld), s

def main(paths):
    found = 0
    for fact, canon, bad, note in FACTS:
        hits = []
        for p in paths:
            vis, raw = text_of(p)
            for rx in bad:
                hay = raw if ("href" in rx or "class" in rx) else vis
                for m in re.finditer(rx, hay, 0 if fact in ("Microsoft Partner",) else re.I):
                    a = max(0, m.start() - 50)
                    hits.append(f"  {p.split('/')[-1]}: ...{hay[a:m.end()+40].strip()}...")
        if hits:
            found += len(hits)
            print(f"[{fact}] should be: {canon}   ({note})")
            for h in sorted(set(hits))[:40]:
                print(h)
    # No monospace font anywhere on the new site (Michael, 10 Nov 2026: it reads as AI-made).
    mono = re.compile(r"monospace|['\"][A-Za-z ]*Mono['\"]|var\(--mono\)")
    for p in list(paths) + [x for x in ("pages/nine.css", "pages/nine-scale.css") if os.path.exists(x)]:
        for m in mono.finditer(open(p, encoding="utf-8").read()):
            found += 1
            print(f"[monospace font] {p.split('/')[-1]}: {m.group(0)}")
    print(f"\n{found} inconsistencies across {len(paths)} pages" if found else f"\nclean: {len(paths)} pages")
    return 1 if found else 0

if __name__ == "__main__":
    args = sys.argv[1:] or sorted(glob.glob("pages/nine-*.html"))
    sys.exit(main(args))
