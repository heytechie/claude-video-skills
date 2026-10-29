# SPEC.md template

The SPEC is the contract. No code before the user approves it. Every adjective becomes a number.

```
# [Product] — [video type] — SPEC
Total: 30.0 s · 1920×1080 · 60 fps · 1800 frames · formats: 16:9 (+ 9:16, 1:1)
Angle: [the chosen story angle in one sentence]
Signature ease: expo.out / cubic-bezier(0.16,1,0.3,1)   Exit ease: expo.in
Durations: quick 0.25 s · standard 0.5 s · slow 0.9 s
Current (dominant seam direction): LEFT
Accent: #XXXXXX = [what it means, e.g. "done / success"]
Music: [track / BPM / drop at s]   Beat grid: beats.json
Banned this film: [defaults you're avoiding, by name]
```

## Scene block (repeat per scene)

```
### S1 · [Name] · [beat: hook | problem | turn | proof | payoff]
Frames 0–240 (0.00–4.00 s)
On screen:   [exact copy in quotes; real UI elements by name]
Motion:      [element: property from→to, duration, ease, delay/stagger]
             e.g. task cards: y +80→0, scale 0.9→1, 0.5 s back.out(1.4), stagger 3 f
Camera:      [push 100→106 % over 4 s, ease in-out] / [pan follow cursor] / [static]
Sustained:   [route between entry and exit: staged reveal | camera intent | UI life | acted sequence | cursor-led]
Holds:       [what must be readable and for how long: "headline ≥1.5 s settled"]
Seam out:    [axis + direction + speed + carrier], e.g. "x LEFT, power4.in 0.35 s, carrier: pile card"
Sound:       [beat/frame: SFX or music event]
```

Rules:
- Scene frame ranges are contiguous and sum to the total; state the check: `240+420+480+360+300 = 1800 ✓`.
- Seam out of scene N must equal seam in of scene N+1 (same axis, same direction, matched speed). Mismatch → fix the plan, not the easing.
- Max 6 words on screen per moment outside the end card.
- Mark the poster frame (best settled frame; bake it as frame 0 for thumbnails).

## Worked example (30 s B2B agent product)

```
S1 · Pile-up · hook · 0–240
  On screen: task cards ("Update CRM", "Export leads", "Weekly report"…) drop and stack; counter "Open tasks 0→200"; headline "200 tasks. Before lunch."
  Motion: cards y −120→0, 0.45 s back.out(1.3), stagger 3 f; counter 1.0 s expo.out; headline word-by-word 4 f stagger
  Camera: push 100→106 % over 4 s, sine.inOut   Sustained: staged reveal (cards keep landing)
  Seam out: x LEFT, carrier = top card, power4.in 0.3 s
S2 · Copy-paste grind · problem · 240–660
  On screen: CRM, sheet, inbox windows; cursor copies a row, arcs, pastes, hesitates 0.4 s, moves on. Text "Copy. Paste. Repeat."
  Camera: eased pan following the cursor   Sound: soft click on each press
S3 · Agents kick in · turn · 660–1140
  Cursor types the prompt, presses Run (press 8 f) → on that frame the camera punches 100→130 % into the button, then eases back; four agent cards stagger in, tasks fly from pile into cards
  Stillness before climax: 0.4 s hold after Run press before the cards erupt
S4 · Payoff · proof · 1140–1500
  Checkmarks cascade (3 f stagger); counter 200→0 in 1.0 s; "Zero busywork." holds ≥1.5 s settled; camera pull-back = arrival
S5 · Logo + CTA · payoff · 1500–1800
  Board docks into logo (shape handoff); tagline + CTA; hold ≥2 s; poster frame = 1700
Sum: 240+420+480+360+300 = 1800 ✓
```
