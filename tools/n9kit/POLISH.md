# Polish round brief (4 Nov 2026, 22:15): make every page as good as the home page

Michael: "make it consistent with the home page ... make things look cool and nice. Go crazy. Figure out what isn't working and fix it, plus other ideas you have."

## First, study the home page (the standard)
Open /home/claude/lb/pages/nine-home.html and the end of /home/claude/lb/pages/nine.css (sections "home polish round" and "Michael's notes, 4 Nov 22:10"). Screenshot it yourself at 1440 and 390 with Playwright and look. What Michael approved there:
1. Cube grids: hovering a cube makes it grow toward you (scale about 1.1, lift, deep shadow, slight tilt with the mouse) while the other cubes step back (scale .97, a little dimmer); clicking goes somewhere. NO spinning or sweeping ring animations, NO loops. Michael explicitly removed the auto "ring sweep" from the home hero; do not add sweeps anywhere. One-time reveal on scroll is fine.
2. Proof row with BIG numbers (class "proof big" with <b class="num">). Numbers stay plain text, no count-up.
3. Package and option lists as coloured cube tiles (.ptiles / .ptile) rather than plain table-like rows where it makes sense.
4. Story cards lead with a big outcome (span.big) taken only from facts already on the page.
5. Rows (a.row): hover highlight bleeds past the text and the arrow (already global in nine.css).
6. FAQ: answer slides and fades open (already global in nine.css). FAQ uses the split layout (.faqsplit with a sticky .faqside: heading, one line, Book a call, phone) instead of a half-empty full width list.
7. Vary the rhythm: avoid two neighbouring sections with the same text-left/graphic-right layout (home flipped one with .vsplit.flip). Avoid blank, decorative-only grids: every cube carries a real label or fact.
8. Stage strips use the filling bar (.stages.flowbar).

## Rules (unchanged from KIT.md, read /home/claude/dec/n9kit/KIT.md fully)
- Edit ONLY your own pages. Do NOT edit nine.css, nine.js, nine-home.html or chrome.py. Page-specific CSS goes in the page's own <style> block scoped by the body class; page JS in the page's own <script>. You may USE the shared classes above (they are global).
- If a hover-grow effect is needed for a cube grid that is not .grid9, write it in your page style using the same values as the home rule (see "hero cubes: hovered cube comes toward you" in nine.css), wrapped in @media (hover:hover) and (prefers-reduced-motion:no-preference).
- Never invent facts, numbers, clients, quotes, prices or URLs. Keep every bracket. No package prices. No "Business Central". No em or en dashes (also not as CSS content). "Free checkups, no obligation". "23 client stories" (never "written up"). Click is "Click (formerly ClickDimensions)" the first time on a page.
- Keep the shared header and footer exactly (if you touch them by accident, re-run chrome.py with your page's SECTION).
- Keep all motion gated by prefers-reduced-motion; keep keyboard access (buttons for interactive cubes, focus styles).

## Checks before you report
- Playwright at 1440, 390 and 360: scrollWidth equals width, 0 page errors, 0 console errors. Test every interactive element by clicking. Test hover on cube grids. Screenshots to /home/claude/dec/shots/polish-PAGE-WIDTH.png; LOOK at them in parts and fix what looks off (overflowing text, awkward wraps, cramped cells, empty halves, misaligned rows, low contrast, tiny tap targets under 24px).
- grep each page: "Business Central", "written up", U+2014, U+2013, "free check" not followed by "up", "$[" (should be 0).
- Every href="#x" resolves; relative links point to existing files.
- Do not git commit or push.

## Report (short)
Per page: what you changed, what was broken and how you fixed it, check numbers. Any shared-CSS change you think would help every page (describe it; do not make it). Then the four stand-down answers: (1) seen but not written down, (2) odd, did not fit, (3) out of scope, (4) not looked at and should be named.
