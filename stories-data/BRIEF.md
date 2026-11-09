# Story data brief (for research agents)

Goal: for each assigned enCloud9 client story, read the LIVE published story page and write ONE JSON file with the facts the new story template needs. Every fact must come from the page you opened. Never invent or embellish. If something is not on the page, leave the field null or empty.

Live URL: https://www.encloud9.com/blog/success_stories/<slug>/
Use WebFetch; ask it for exact wording (it summarizes, so ask for short exact quotes sentence by sentence). If WebFetch is refused, write "could not determine" in notes and stop for that story.

Write: /home/claude/lb/stories-data/<key>.json  (UTF-8, valid JSON, no comments)

Schema (all strings plain text, US spelling, NO em or en dashes anywhere, no "Business Central"):
{
 "key": "<key you were given>",
 "slug": "<slug you were given>",
 "client": "Client name as the story writes it",
 "work_type": one of "New build", "Rescue or fix", "Upgrade", "Integration", "Add-on", "Support" (use the hub label you were given unless the page clearly says otherwise; say why in notes),
 "title": "<Client>: <short what> | enCloud9"  (60 characters or fewer, count them),
 "meta": 120 to 160 characters, factual, starts "How enCloud9 ...",
 "h1": ["<Client>:", "<short result line, 2 to 7 words>"],
 "answer": 40 to 60 words (count them). Who the client is and where, what was wrong or needed, what we did, the result. We voice ("We ..."). Only facts on the page.,
 "facts": [["Client", "..."], ["Location", "City, ST"], ["Industry", "..."], ["Starting point", "..."], ["Products", "A; B; C (exact product list from the page)"], ["Services", "exact services list from the page, joined with commas"]]  (drop a row if the page lacks it, except Client),
 "timeline": "Within three months" style text if the page states a timeline, else null,
 "tiles": up to 3 pairs [["Big short value", "small caption"]], ONLY real numbers or plain facts stated on the page (for example a stated timeline, a stated count). If none, [],
 "outcomes": 2 to 5 short sentences, each a result the page states,
 "chapters": [["What was wrong with <Client short>'s CRM?" or a fitting question for new builds such as "What did <Client short> need?", ["paragraph", ...]], ["What did we change?" or "What did we build?", ["paragraph", ...]], ["What changed day to day?", ["paragraph"]]],
 "next_steps": ["What comes next for <Client short>?", "one paragraph"] only if the page states next steps, else null,
 "quote": {"text": "...", "name": "...", "title": "..."} ONLY if the page has a quote attributed to a NAMED client person, else null,
 "author": "author as shown", "published": "YYYY-MM-DD", "published_h": "Month D, YYYY",
 "sources": [{"claim": "short label", "quote": "exact short quote from the page"}, ...]  one entry per fact you used (at least one per outcome, per key fact, timeline, tile, quote),
 "notes": "anything odd: product names that do not match, missing fields, wording you could not confirm, any mention of Business Central or other off-limits items"
}

Writing rules:
- Paraphrase in plain words but never go further than the page: no "again", "back to", "finally" unless the page says it, no causes the page does not state, no numbers not on the page.
- Do not quote the page as "the story" (the page IS the story). Short direct quotes of the page's own words are fine.
- If the page mentions Business Central, do not use it in any field; flag it in notes.
- Client details: only what the page says.
- Questions as H2s.
When done, reply with: the files written, and per story one line of anything doubtful. End with the four stand-down answers: what you saw and did not write down; what looked odd; what you left out of scope; what you did not look at.
