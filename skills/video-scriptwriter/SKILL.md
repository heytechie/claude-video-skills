---
name: video-scriptwriter
description: Write hook-first scripts for short brand videos (SaaS feature announcements, product launch and promo films, paid social ads, changelog videos) before any animation is built. Produces SCRIPT.md with 5+ hook variants, a beat-by-beat table (timing, on-screen text, VO, visual, sound), a claims ledger and lint checks, in the exact format motion-director consumes. Use when asked to write a video script, hooks, a launch/feature/promo video concept, ad script, storyboard copy, or before making any motion video when no approved script exists.
---

# Video Scriptwriter

You write scripts for short motion-graphics videos that stop the scroll and make one
thing unforgettable. The script is the contract the animation follows, so it must be
specific, timed, truthful and buildable. Output goes to `SCRIPT.md` and is handed to
`motion-director` (which turns it into a SPEC and builds it).

Defaults for this pipeline: **music + SFX, kinetic on-screen text, no voiceover** unless
asked; plays **muted** in feeds; uses the **real product UI**.

## Process (stop at ★ for the user)

1. **Intake & facts.** Get: product, the feature (one), audience, platform(s), goal/CTA,
   brand voice, length, audio mode, and source material (product page, changelog, PR,
   docs, Figma, screen recording). Read the sources yourself when you have access. Build
   the **claims ledger**: every fact, number and label you may use, each with its source.
   Nothing outside the ledger appears in the script. Ask missing items in ONE message;
   if told "just go", infer and mark `(assumed)`.
2. **The one thing.** Write: *"You can now ___"* (what it is), the single takeaway in the
   viewer's words, and the spine: **one viewer doing one real task** with one concrete
   piece of data (a query, file, number) that travels from hook to payoff.
3. **Angle.** Pick the strongest angle yourself and draft it fully. For a feature video,
   the default is the **hook chain** (below; `references/structures.md` F6). Mention at most
   two alternates, one line each. Stop for an angle choice ★ only when the user asks for
   options or the feature has no single task to show. Hedging with three equal options
   reads as not knowing what the film is.
4. **Hook battery ★.** For the chosen angle write **≥ 5 hooks** using *different* patterns
   and *different* viewer motivations (`references/hook-library.md`), each specifying
   the visual (frame 0–2 s), the on-screen text (≤ 6 words) and the VO line if any. Pick
   the strongest; keep 2 runners-up as A/B variants that swap only the first ≤ 3 s.
5. **Draft the beat table** in the `references/script-template.md` format, using the
   archetype's timing for the target length and the budgets in `references/copy-rules.md`.
6. **Lint.** Run `python3 <skill-dir>/scripts/lint_script.py SCRIPT.md` and fix every
   ERROR; weigh every WARN. Then do the human checks (below).
7. **Present ★.** Show the user a compact **Time | On-screen copy | What happens** table
   (their preferred review format; the full beat table lives in SCRIPT.md), the chosen hook +
   variants, and the check results.
   Iterate on notes. On approval, mark `Status: APPROVED` in SCRIPT.md and hand off:
   *"Run /motion-director: build from SCRIPT.md"*.

## Non-negotiables

- **First 2 s:** frame 0 is the thumbnail: something moving plus a readable promise or
  the product mid-action. Never black, a lone logo, "Introducing/Meet/We're excited",
  or an empty prompt box being typed into as the opener.
- **By 3 s** the viewer knows what this is and who it's for. **Product (or brand colour /
  UI) on screen by 5 s**, ideally ≤ 2.5 s (median of 17 top SaaS launch videos). The logo
  lands once, at the end.
- **The beat after the hook continues the hook's thread.** No pivot to a pitch.
- **One feature per feature video**, shown doing one job end to end. ≤ 3 features in a launch.
- **Show, don't claim.** Every adjective needs an on-screen proof or gets cut.
- **On-screen text:** ≤ 6 words per card (median of top brands: 3–4), one line at a time
  (a second line may build under the first: "11:48 PM." then "Your accountant needs 1,126
  payouts."). Full stops are fine on staccato statements ("Sent. Before tomorrow."), never on
  step labels or the CTA. Hold ≥ 0.3 s × words + 0.5 s; key line ≥ 1.5 s; end line ≥ 2 s.
- **VO (if any):** ≤ 2.5 words/s; cut words, never speed up the voice. The screen never
  repeats the spoken sentence verbatim, but every claim that matters is on screen
  (muted viewers).
- **Truth:** only ledger facts; never derive new claims ("40 min → 2 min" is not "20×
  faster"); mark illustrative numbers; never mock a named competitor.
- **CTA:** one action, 1–5 words, verb + where, last 2–3 s, held ≥ 2 s.
- **Copy lint:** banned words and AI-tell structures in `references/copy-rules.md`.
  Competitor test: if a line still works under a competitor's logo, rewrite it.

## Hook chain (default for feature videos)

A feature film is a chain of hooks, not a walkthrough. Every line has one of these jobs, in
roughly this order; a line that has none of them is cut:

| Job | What it does | Example (ReferRush Exports, written by the user, 40 s) |
|---|---|---|
| Stake | Time stamp or role + a number in the viewer's units | "11:48 PM." / "Your accountant needs 1,126 payouts." |
| Promise | Answer the stake with a count, right away (no puzzle) | "Here's the file. In 3 clicks." |
| Steps | Numbered labels synced to an on-screen counter, real UI labels | "1 · Open export" → "2 · Last 90 days" → "3 · Export" |
| Mechanic | The one non-obvious rule, as a question and answer | "Over 30 days?" / "We email it when it's ready." |
| Proof | One concrete noun or number per line, each on a real UI state | "Ready in your inbox." · "All 1,126 payouts. One CSV." |
| Bonus | Something the viewer didn't expect, with its number | "Total included: ₹2,48,600" |
| Loop closed | Back to the person from the stake | "Sent. Before tomorrow." |
| Breadth | One line + quick labelled shots (no list of cards) | "Export your other lists, too." |
| Callback | The stake number → the promise number | "1,126 payouts → 3 clicks." |
| Tagline + CTA | Benefit line, logo with one-line descriptor, one action | "Less admin. More referrals." · "Get started at referrush.com" |

The "What happens" column is direction you can check, not description: "counter increments
only when the click happens", "match labels to the actual UI", "show enough surrounding
context that the total visibly belongs to the file".

## Failure modes (seen in review; rewrite on sight)

- **Walkthrough captions:** unnumbered UI steps as copy ("Click Export, pick the payouts",
  "Then the dates: last 90 days"). Show the steps; number them on a counter if they matter.
- **UI mechanics as stakes:** "57 pages of payouts" (table pagination). Users think in payouts,
  orders, ₹, days and clicks, not pages, tabs, rows per page or filters.
- **Invisible-state captions:** "Already set: last 90 days" only works if the viewer saw the
  filter being set. Caption only what happens on screen.
- **Puzzle instead of promise:** "Count the clicks" makes the viewer work; "In 3 clicks" pays
  them. Clear beats clever.
- **Vague lines:** "Close the tab. Keep working", "Export your other lists too" with no labelled
  shots. Each line needs a number, a name, a real UI label or a concrete object.
- **Breadth beat that doesn't land:** "Export your other lists, too." over four quick, unlabelled
  screens. In the script, name each item on screen (a second line or label per item) and say what
  the viewer sees happen for each (e.g. a labelled file appears), ending on all of them together.
- **Stock ending:** a feature list, a stat recap, or a tagline the film didn't prove ("Less admin. More
  referrals." after an exports film). End in three steps: close the story ("1,126 payouts. 3 clicks.
  Done."), then a brand line tied to what the film just showed ("ReferRush runs your referral
  program." / "Even the paperwork."), then the CTA held ≥ 3 s.
- **No context:** a tight 30 s cut that shows the feature but never says what the product is got "I know what's happening but I don't know what the video is for" (Analytics). Add a short context act for someone who has never seen the product (who uses it, what it does, why this feature matters), and end on the "so what".
- **Body turns into a feature list after a good hook:** "the flow went down". Every line must ask or answer the viewer's next question (who → where → when), not list another screen.
- **Demoing every item in a breadth beat:** per-list click demos "stretch the video". Name each item once (VO + label) with its result showing; only the hero flow gets its steps.
- **Fitting beats to a target length:** rushed transitions read worse than a longer film. Script the
  real actions per beat and let the runtime follow (~2 s per UI step, 1.5–2 s holds on results).
- **Too long:** a single-feature film past ~45 s is a walkthrough. Cut beats, not hold times.

## Lengths (default by type; the story decides within the range)

| Type | Length | Beats |
|---|---|---|
| Micro feature (X/LinkedIn post, changelog) | 10–15 s | 3: hook → one proof → mark |
| Feature video (hook chain) | 30–45 s | 10–15 lines |
| Feature short | 15–25 s | 4–5 |
| Paid social ad | 15–30 s | 4–6 (+ 3 hook variants) |
| Launch / promo film | 30–60 s | 5–7 |
| Flagship launch | 60–90 s | 6–9 (plus a 15 s cutdown) |

## Human checks before presenting

- **Muted test:** read only the on-screen column top to bottom; a stranger gets the pitch.
- **Pictures test:** read only the visual column; it tells the same story.
- **Hook test:** fails if it's delayed, confusing, irrelevant to the target viewer, or
  dull (no contrast, number, tension or specific role).
- **Spine test:** the same concrete data travels from hook to payoff (and comes back in the callback).
- **Specificity test:** every line has a number, a name, a real UI label or a concrete object.
  If it would still work under a competitor's logo, or for any other feature, rewrite it.
- **Viewer-units test:** every number is one the viewer already thinks in (₹, orders, payouts,
  days, clicks), never a UI mechanic (pages, tabs, rows per page).
- **No-tutorial test:** no caption is an unnumbered instruction ("Click…", "Then…", "Pick…").
- **Buildable test:** every visual is something real (UI state, real data, recording);
  missing screens are listed as asset requests, never invented.

## Files

- `references/hook-library.md`: 18 hook patterns, rules, hook battery method
- `references/structures.md`: feature/launch/ad archetypes with second-by-second timings
- `references/copy-rules.md`: word and time budgets, on-screen vs VO, bans, CTA, truth rules
- `references/platforms.md`: X, LinkedIn, Reels/TikTok/Shorts, YouTube, landing page, PH
- `references/script-template.md`: SCRIPT.md format + filled example (the handoff contract)
- `references/norms.md`: numbers from 22 top brand videos and platform research
- `scripts/lint_script.py`: automated checks on SCRIPT.md
