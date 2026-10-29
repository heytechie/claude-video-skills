# Review loop

You cannot watch video. You review through **stills and contact sheets**, plus measurements. Never claim a video is good without having looked at frames.

## 1. Stills gate (before the first full render)
For each scene render: first frame, key frame (the readable hold), last frame, and the frames 2 before and 2 after each seam. Inspect for: overlapping text, clipped/overflowing elements, fallback fonts, wrong colors, empty frames, elements outside safe zones.

## 2. Draft render + QA script
```bash
bash <skill-dir>/scripts/qa.sh out/draft.mp4 qa/
```
It writes contact sheets (2 fps, 6×5 tiles, timestamped), a per-second strip, hard-change timestamps, freeze ranges, black frames, the stream spec (resolution/fps/pix_fmt/codec), and integrated loudness. Read the sheets with your image-reading tool.

Interpretation:
- **Hard changes** not at planned cuts → a single-frame pop / element appearing without an entrance.
- **Freeze ranges** longer than a planned hold → dead air (nothing performing).
- **Black frames** not planned → missing clip, wrong `data-start`, or a white/black flash at a seam.
- Spec mismatch vs SPEC → fix render settings.
- Loudness outside target ±1 LU → re-normalize.

## 3. Determinism check
Render frame 60 after frame 30, then frame 60 after frame 120 (or render the same frame twice in separate processes). The images must be identical. Any difference = time-dependent state, randomness or async loading.

## 4. Score (1–10 each; ship only when all ≥ 8)
| Category | 8+ means |
|---|---|
| Story | Hook in 2 s, one idea per scene, clear problem→turn→proof→payoff, ends on CTA |
| Pacing | Contrast of calm and peak, cuts on beats, stillness before climax, no dead air, no rush |
| Readability | Every line holds per the table; ≤ 6 words; phone-legible sizes |
| Motion craft | Signature ease, stagger/overlap, causal chains, arcs, seams matched, no idle wobble |
| Composition & type | Clear focal point per frame, hierarchy, safe zones, bold scale contrast |
| Brand fidelity | Exact hex, fonts, logo; real UI sharp at zoom; product's own language |
| Sound | Beat-aligned, sparse real SFX, clean mix, target loudness |
| Originality | Doesn't look like a template or the default AI look |

Write scores and the top 3 fixes into `REVIEW.md`, fix, re-render, re-score. For big jobs, run the critic as a separate subagent given only the SPEC + contact sheets (an un-anchored reviewer catches more), but only send flagged frames to expensive vision review to save tokens.

## 5. Pre-delivery checklist
- [ ] Canvas and fps match SPEC; H.264 yuv420p (CRF ~16–18); audio AAC 48 kHz.
- [ ] Fonts correct in every scene's frame 0.
- [ ] No overlapping text at any seam; nothing leaves the canvas unless exiting on purpose.
- [ ] Every counter ~1 s, lands ≥ 1.5 s before exit.
- [ ] Repeated elements stagger; nothing pops in on one frame.
- [ ] Every camera move eased and readable.
- [ ] Seams: matched axis/direction/speed; no white/black flash.
- [ ] Copy proof-read; numbers only from the brief.
- [ ] Poster frame chosen and baked as frame 0 (if delivering for social).
- [ ] Cutdowns (9:16, 1:1) re-rendered from the same timeline with key elements inside the center square, not cropped from 16:9.
- [ ] Loudness: −14 LUFS (social) / −16 LUFS (web), true peak ≤ −1 dBTP.
- [ ] Deliverables named: `product_launch_16x9_v3.mp4`, etc. Keep project source + `content` config for revisions.
