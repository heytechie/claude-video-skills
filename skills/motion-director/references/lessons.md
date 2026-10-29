# Lessons log

Read at the start of every job. Append after every job: `- [date] [symptom] → [cause] → [rule now]`.
Promote a lesson into SKILL.md / motion-rules.md once it recurs twice.

## Seeded from research (2026-10)
- Layout exploded off-canvas → Figma frames 1440 wide placed on 1920 canvas by edge coordinates → lock canvas, scale frames uniformly, position from center.
- Times New Roman in early frames → font not loaded before frame 0 → block render until fonts ready; QA frame 0 of every scene.
- Counter jumped to final value in one frame → no interpolation → ~1 s ease-out count.
- Agent cards popped in all at once, stacked → no stagger → 2–4 f stagger, each lands before its checkmark.
- Camera pan too fast/jerky → linear, short → ≥ 0.8 s, eased both ends.
- Every scene visible the whole time → a single CSS rule overrode clip visibility → QA contact sheet of the full film, not just per-scene stills.
- Beat detector chose the kick entry, not the drop → trusted auto-detection → verify drop by bass-energy jump.
- Count-up never reached the final number → animation ended before the value tween → land value ≥ 1.5 s before exit.
- Brand accent failed contrast on its background → no check → verify text contrast ≥ 4.5:1 for small text, 3:1 for large.
- Reference prompt invented "1M visitors" → copied someone else's facts → numbers only from the brief.
- Token blow-up on max effort → many critic subagents reviewing every frame → measure with scripts first, send only flagged frames to vision review, one reviewer.
- Agent fixes one scene and breaks another in long sessions → context degradation → one fresh session per act; SPEC.md + lessons.md as memory; smallest-change revisions.

## ReferRush WhatsApp film (2026-10-26, HyperFrames)
- Cursor sat ~100 px off its button in some frames, fine in others → bezier path applied via `onUpdate` + `gsap.set`, which renders wrong on a cold seek (render workers and `snapshot --at` jump straight to a time) → move things with plain property tweens only (`fromTo` x and y on different eases, e.g. lead `power1.inOut` / lag `power3.inOut`, gives the arc); test a single cold `snapshot --at T` at every click.
- Table visible on screen during the wrong scene, depending on seek order → `fromTo` with default `immediateRender` fought a `tl.set` baseline, and its "off-screen" x wasn't off-screen → explicit `tl.set` start state at 0 + `immediateRender:false` on later fromTos; off-screen offsets must clear the frame edge.
- Typed text appeared mid-field → placeholder faded to opacity 0 but still took flex space → placeholders `position:absolute`.
- WhatsApp bubbles overlapped when one wrapped → bubbles placed at fixed `top` steps → flow layout (flex column, 3 px gap), only the first bubble of a group gets the tail corner.
- `text_occluded` under the caption band → `data-layout-allow-occlusion` on the band does nothing → put it (plus allow-overlap) on the covered text.
- Zoomed UI cropped at the frame edges → zoom chosen without checking page width × scale against 1920 → keep ≥ 60 px margin: scale ≤ (1920 − 120) / content width.
- Toast landed on top of the button just clicked → screen-space toast vs camera-space button → check toast rect against the last click target per camera state.
- QA "freeze" for 3–4 s while only the cursor moved → static camera during form filling → slow eased push-in during holds (`sine.inOut`, ~4 % scale), cursor targets computed from the camera state at press time.
- CTA looked disabled → neutral grey button on a near-black end card → brand-colour fill + soft glow + hover nudge before the press; clear the label before any shape morph.
- Cursor missed every click in one scene → targets computed in page coords but w2s() expects window coords (page sits at x = sidebar 248 + padding 28) → define one `PX` page-origin constant per scene and use it for every target; cold-snapshot each click.
- Elements vanished during camera moves and transitions smeared (looked "not smooth") → HyperFrames `data-motion-blur="on"` drops elements in some frames (only in render/snapshot, never in the live preview) → leave motion blur off for UI films; 60 fps carries the smoothness. Debug render-only bugs by toggling root options and cold-snapshotting, since the preview player hides them.
- User: "UI broken in a lot of places" → screens were approximated from labels, not from the component markup → before building any product UI, read the actual components + UI kit + theme tokens and copy layout, sizes, icons and states (disabled, loading, empty) exactly; never invent fields/variables.
- User: "sudden increase in pace" → second half crammed (~1 s per action, 0.18 s whip) to fit an approved duration → keep one rhythm (~1.5–2 s per UI action) for the whole film; extend the runtime rather than compress late beats.
- iPhone Dynamic Island touching the bezel → island positioned in device coords instead of screen coords → island 11 px below the screen top, centred; status-bar time/icons vertically centred on it.

## ReferRush Analytics film (2026-10-27, HyperFrames)
- ₹ and → were not in the bundled Geist-Variable.woff2 (a 225-glyph Latin subset), so the WhatsApp film drew them in a fallback font → fonts copied from a CDN subset, glyphs never checked → before building, check every font's cmap (fontTools `getBestCmap()`) against every on-screen string (currency, arrows, dashes, emoji); use the full family release (Geist v1.8.2 from vercel/geist-font has ₹ →). A display font without the needed glyphs (Instrument Serif has no ₹) is out, however nice it looks.
- Script beats with real multi-click flows (date picker needs preset + Apply; upgrade dialog needs 5 clicks) were timed as if one click → script timings came from copy holds, not UI actions → when converting SCRIPT → SPEC, count real clicks per beat from the component code (~1–1.5 s each) and propose a runtime change before building.
- White smears in render frames while the whole dashboard receded → `filter: blur()` animated on a huge transformed layer → never blur the whole world; recede with scale + opacity, blur only small elements.
- Date popover ran off the window → positioned with world coordinates inside a page-local container → keep one coordinate system per container; compute world targets as page origin + local.
- GSAP "target not found" and wrong elements animating → duplicate ids across partials (reply bubbles reused leaderboard-row ids) and ids missing their prefix hyphen → prefix every id by component (`rp1`, not `r1`) and grep the built HTML for duplicate ids before snapshotting.
- `content_overlap` from an intended popover/dialog clears with `data-layout-allow-overlap` on an ancestor (`.win`); `text_occluded` from the caption band needs the attributes on the covered text itself.
- QA "black frames" at page swaps → fade-out finished before the next page's blocks became visible → start the incoming blocks at the outgoing fade's start (overlap ≥ 0.2 s).
- User: "the WhatsApp UI text was flickering" → slow scale drifts (phone 0.96→0.995 over 6 s, camera micro-pushes ≤ 3 % on held UI shots) make Chrome re-rasterize small text at a new scale every frame; glyphs snap between hinting states (measured 70–230 luma jumps per frame on a "still" chat) → no slow scale/translate drift on any shot with readable UI text; the camera is still during reading holds and moves only when it travels (≥ 0.8 s, purposeful). Verify with a frame-diff of 6 consecutive frames on each hold (static text should differ by ≤ 2 luma). This overrides the "micro-push allowed" rule for UI films.

## ReferRush Exports film (2026-10-28, HyperFrames, 3D MacBook)
- Readable UI inside a CSS-3D laptop → rasterization risk → keep every reading shot on a flat 2D copy of the screen, use the 3D model only for the move/lid action, and hand off on one frame with the identical camera at the START of a camera move (measured ≈1 luma diff, invisible). Diff the frame before/after each handoff against neighbouring frames.
- Lid rotated the wrong way, and I "fixed" a correct version → misread a closed laptop seen from above (a plain grey slab) as a bug → snapshot 50 % and 100 % of any 3D rotation and describe what each sign should look like before changing it. In this rig (deck rotateX(90deg) on its top edge, world tilt −16° to look down), closing the lid = rotateX(−89.6°) on its bottom edge.
- A "floor shadow" plane placed at hinge height showed as a dark blotch through the closed lid → coplanar/near-coplanar 3D planes z-fight; drop decorative planes or keep them well below the deck.
- Ghost double text for 3–6 frames on 0.1 s cross-fades between text-heavy UI pages → the app navigates instantly, so hard-cut page swaps (tl.set on the frame), including the sidebar state.
- A HUD chip under the captions' dark gradient band rendered dim → anything that must stay bright goes in its own composition above captions.
- Hide-then-show `tl.set()` pairs at time 0 on the same element left it hidden in renders → never stack contradictory sets at one time; guard the baseline instead (skip it for elements visible at frame 0).
- A sheet scaled from a right-centre origin landed off-screen → compute the unscaled box from the desired FINAL rect and the transform-origin, not the other way round.
- The phone rose over the laptop while the requested lid-close was still playing, hiding the hero action → let a hero action finish fully on screen before the next element enters.
- hyperframes check reported ~100 text_occluded / clipped_text / contrast errors on rebuilt product UI layered under a phone and caption band → false positives; tag product-UI layers `data-layout-ignore data-layout-allow-occlusion data-layout-allow-overflow` and verify with stills instead.
- Emails/notifications that must look "exactly the same" → execute the backend's own template function on the film's values (read-only) and embed the HTML; swap only the remote logo URL for a local copy and stand in fonts that can't be bundled (SF → Inter), and say so.
- A code-reading agent said the calendar uses "arrows, not chevrons"; the actual HugeIcons paths (ArrowLeft01Icon) are curved chevrons → always extract icon paths from the installed package instead of trusting a description.
- User: "the back lid has dashboard UI, why?" → with the camera above the laptop, the screen side stays visible until the lid is ~(90° − tilt) closed, so a lit screen on a closing lid reads as UI on the lid → dim the screen to black in the first half of a close, raise the camera (tilt ≥ 20°), and put the brand mark on the lid back (it's the hero of the closed shot).
- Zero-thickness 3D lid vanished for a frame when edge-on to the camera → give thin 3D objects real thickness (offset the back face with translateZ and add an edge strip) so no angle shows nothing; check every frame around the edge-on angle, not one snapshot.
- User: "export your other lists too: the delivery of the thought is not clear" → a montage of four 0.8 s screens with small rings names nothing and shows no result → in a breadth beat, NAME each item big (a second caption line in the accent colour), and SHOW the outcome per item (here a labelled file card flying into a row), ending on all items together.
- User: "at some point the video rushes, not according to the whole video's pace" → beats had been fitted to script times, so several motions overlapped (5–7 events inside 2 s around transitions) → before rendering, run a pacing audit on the timing table (events per 2 s window) and re-time so one main motion happens at a time, each settled and held before the next. Keep ALL times in one table (no hard-coded times in motion code) so re-pacing is a one-place change. Extend the runtime rather than compress.
- User: "the ending's text, meaning and promotion don't end well" → a stat-equation recap plus a generic tagline and a small lockup → end in three steps: close the story ("…Done."), give the brand meaning tied to the story (a claim the film just proved), then the CTA held ≥ 3 s. A product prop carrying the logo (the laptop lid) makes a strong carrier into the lockup: crane into it, dim everything around the mark, and match the end-card mark to its measured on-screen bbox.
- User screenshot: the step chain "1 · Click Export → 2 · Choose Last 90 days → 3 · Click Export" ran under the HUD counter chip → copy got longer in a rewrite and the line was laid out across the full 1920 width → whenever copy changes, re-snapshot every caption at its fullest state; centre long lines inside the free width (here 1600 px left of the chip), never the full frame, when a HUD element shares the band.

## 2026-10-28 · Exports film v7: "the R logo animation is too laggy"
- Cause: two tweens animated the same property (x, and scale) on the same cards with overlapping windows (a 0.9 s "gather" and a "shrink" that started 0.4 s before it ended). GSAP doesn't overwrite by default, so the later tween took over mid-flight: the cards crept, then jumped and collapsed. The logo also faded in on top of half-collapsed cards, which looked muddy.
- Fix: one gesture per property, back to back, never overlapping: arrows fade (0.25 s) → cards slide into a stack (x + scale to 0.82, 0.6 s power3.inOut) → the stack squeezes (scale 0.82 → 0.3 + opacity, 0.28 s power2.in, starts when the slide ends) → the mark springs out of the stack (scale 0.5 → 1, back.out(1.6), 0.6 s) with a soft radial flash → it glides into the lockup (0.75 s), and the wordmark slides in only after the mark has arrived.
- Rule: before a render, list every tween per element and property; if two windows overlap on one property, chain them (fromTo from the previous end) instead.
- Pacing: a voiced film reviewed silently (VO not recorded yet) feels slow because the voice gaps play as dead air. Keep the visual-only gaps between lines at 0.3–0.4 s for continuous thoughts and ≤ 1.0 s where an action needs to play out.
- Follow-up (same film, v8 → v9): even the clean "slide into a stack, squeeze, R springs out" was rejected ("I hate this part"). Stacking UI cards always reads as a pile-up: mismatched cards overlap, and a white card behind dark ones turns grey. What worked: a focus pull. The summary row holds, then softens out of focus outside-in (opacity, scale 0.95, blur 0 → 10 px, 0.55 s power2.inOut, 0.08 s stagger), and the logo comes into focus on the same spot (blur 14 → 0, scale 0.92 → 1, expo.out) with a soft radial glow. Default to that for "cards become the logo" handoffs; never stack cards.

## Cross-film rules from the ReferRush films (WhatsApp, Analytics, Exports, 2026-10)
- No device mockups (laptops, lid closes). Founder: "a bit cheap". Show the product as a plain floating app window; a phone frame is fine only where the real surface is a phone (WhatsApp, mail).
- The UI must be rebuilt from the real code (read-only), with labels checked against upstream. A wrong label or spacing is noticed immediately.
- The user doesn't keep a film's code once it's done (only the final mp4s), so every lesson has to land here or in the skills at the end of each film, not in the project's PROGRESS.md.

## ReferRush Referral Popup film (2026-10-29)
- HeyGen's OAuth free TTS allowance (10 min/month) ran out mid-recording → the Exports film's samples and re-takes had used most of it → before recording, estimate the read (~3 words/s) and check what's left; record samples sparingly. The fallback was local Kokoro (`hyperframes tts`, venv with `kokoro-onnx soundfile` on PATH): one clip per line, silence-trimmed, a single loudnorm pass over the joined read, word times estimated by character weight. Keep the voice consistent across the whole film; never mix two voices.
- Cursor targets for flow-laid-out UI → measure, don't guess: build a static measure page from the same markup functions, load it in headless Chromium (puppeteer-core from the hyperframes npx cache + /usr/bin/chromium), wait for `document.fonts.ready`, record every id's rect to `src/measure.json`, and run it twice when later positions depend on earlier measurements.
- A long settings page doesn't fit a 900 px window → scroll the page layers (header + body) with y transforms while the top bar and sidebar stay put, rather than zooming the camera out.
- Captions over busy UI during zoomed shots → use the solid caption band (opaque to ~64 % of its height) for those spans.
- A breadth line read in one breath gave each L2 result card ~1 s → split the VO into short lines with a ~0.5 s pause each, so each result holds ≥ 2 s.

### Voice fallback (Popup film re-voice, 2026-10-29)
- Kokoro male voices (am_michael) were rejected as unusable. Don't ship Kokoro VO for ReferRush.
- Gemini TTS (gemini-3.8-flash-tts, voice Achird) is the working fallback when HeyGen is out. The free tier allows 3 req/min and 10 req/day per key, so spend at most 1–2 requests on samples.
- Record a whole section per request ("clear pause of about one second between paragraphs") and cut at the pauses. Choose the cut set whose pieces best match each line's text share. Then check every piece's RMS: a short line ("then save.") can be mis-cut as pure silence while its words ride on the previous line.
