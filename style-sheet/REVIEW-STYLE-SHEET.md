# Review: enCloud9 style sheet, Draft 1 to Draft 2 (9 Nov 2026)

Frozen Draft 1: style-sheet/draft1/encloud9-style-sheet-D1.html, sha256 0991b49b...1a71 (unchanged before and after review).
Reader: Brian (approve the look) and Kristin (make blog graphics, social posts, emails).

## Scores
- Draft 1: 21/32, independent reviewer (agent that did not build it). Failed.
- Draft 2: 29/32, Claude's re-score against the same rubric (not independent). Areas moved: answer first 3 to 4, fit 2 to 3, accuracy 2 to 4, completeness 2 to 3, finish 2 to 4, house rules 3 to 4.

## Changed in Draft 2 (from the review and fact check)
1. Ask added at the top: Brian approves or marks changes; Kristin uses it.
2. Logo section added: wordmark only, blue on light, white on dark. Cloud mark retired (Brian, 9 Nov call).
3. Facts fixed to match the built site (pages/nine.css): page background #F7F9FC (was white); labels on dark step 8 (was 7); weights 600 SemiBold (was 550, which Canva and Office do not have); headline ranges 44 to 96 and 32 to 54 (were unsourced 84 to 92 and 48 to 56); body 17 px.
4. Hanken credited as Michael's choice replacing the kit's Bricolage Grotesque; Google Fonts links added; Word, PowerPoint and graphics guidance added.
5. Sample buttons are no longer dead links (labelled "Samples, not links"); outline button and hover darkening added; email spec now includes line height 2 (measured); price placeholder removed; contrast pairs added; step 5 shows a BRAND tag instead of a focus-like outline.

## Not changed, and why
- Date for Brian's approval: no date given; Michael adds one if he wants.
- ink2 #24304F and the 3x3 grid markers: minor for these readers.
- Canva: whether Hanken Grotesk is in Canva's font list could not determine. Michael checks.

## Still open
- Logo blue: the 2024 wordmark SVGs use #255DA6; all other brand blue is #355DA6 (measured). Brian's call.
- Font: Hanken replaces Bricolage (Michael's decision 9 Nov). Brian to approve.
- Local site font files cover Hanken 300 to 600 only; fine while the sheet says SemiBold (600).
- Out of scope but seen by the reviewer: some concept pages hold real-looking prices ($500 a month, $1,500, $2,000). Check against the no-prices rule before go-live.

## Checks run on Draft 2
- No sideways scroll at 320, 390, 768, 1440 (scrollWidth equals width).
- Both logo images load (300 px wide). Links: 2, both Google Fonts specimen pages.
- Em and en dashes: 0.
- Regression: every line dropped from Draft 1 was an intended rewrite; nothing lost by accident.
