# Motion rules: full tables

## Easing tokens (define once in `theme`, never inline ad-hoc curves)

| Token | GSAP | CSS / Remotion `Easing.bezier` | Use |
|---|---|---|---|
| `enter` (signature) | `expo.out` | `(0.16, 1, 0.3, 1)` | most entrances, camera arrivals |
| `enterSoft` | `power3.out` | `(0.33, 1, 0.68, 1)` | text, calm/premium films |
| `enterPop` | `back.out(1.4)` | `(0.34, 1.4, 0.64, 1)` ≈ 4–5 % overshoot | hero elements, cards landing |
| `exit` | `expo.in` / `power3.in` | `(0.7, 0, 0.84, 0)` | exits (shorter than entrances) |
| `move` | `power2.inOut` | `(0.65, 0, 0.35, 1)` | on-screen repositioning, camera pans |
| `cut` | `power4.in` → `power4.out` | mirrored pair | seam handoffs (exit side / entry side) |
| `linear` | `none` | linear | ONLY progress bars, spinners, constant scroll, typing cadence |

Remotion springs: entrance `spring({ frame, fps, config: { damping: 14, stiffness: 120, mass: 1 } })` (slight overshoot); no-overshoot settle `damping: 200`.
Banned: `bounce.*`, `elastic.*`, overshoot > ~8 %, and a unique ease per element.

## Durations (UI-in-video, 60 fps)

| Element | Duration | Frames |
|---|---|---|
| Click press (1→0.96→1) | 0.13 s | 8 |
| Checkmark draw | 0.25–0.35 s | 15–21 |
| Small element / badge / icon entrance | 0.25–0.35 s | 15–21 |
| Card / panel / window entrance | 0.4–0.6 s | 24–36 |
| Headline entrance (per word stagger 3–5 f) | 0.4–0.6 s | 24–36 |
| Camera punch-in on a click | 0.35–0.5 s | 21–30 |
| Camera pan full-width | ≥ 0.8 s (usually 1–1.5 s) | ≥ 48 |
| Count-up | ~1.0 s | 60 |
| Dramatic reveal / logo build | 0.6–1.2 s | 36–72 |
| Exit | 60–75 % of its entrance | |

Distance scales duration: 100 px = base, 200 px ≈ 1.3×, 400 px ≈ 1.6×. No single move travels more than ~1/3 of the frame without a keyframe/direction change, unless it's a deliberate seam whip.

## Readability holds

| Content | Minimum settled hold |
|---|---|
| 1–3 word label | 0.8 s |
| Sentence | 0.3 s/word + 0.5 s |
| Key headline / big number / key UI state | 1.5 s |
| End card (logo + CTA) | 2.0 s |

## Stagger and overlap

- Siblings: 2–4 frames apart (micro cascade 1–2 f for list rows; dramatic 6–10 f for 3–4 hero items).
- Total stagger ≤ 0.5 s. With 8+ items, stagger the first 4–5 and bring the rest as a group.
- No more than ~1/3 of elements in active motion at once. Lead with the hero.
- Overlap: next move begins during the last ~20 % of the current one, so nothing freezes or snaps.
- All siblings enter from the same direction.

## Cursor

- Size 1.5–2× OS default, crisp SVG, subtle shadow.
- Path: a gentle curve from A to B (~15 % bow; alternate sides for consecutive moves). In HyperFrames build it from x and y tweens on different eases, not onUpdate (see engine-hyperframes.md). Duration 0.5–0.9 s by distance, `power2.inOut`, tiny overshoot (2–4 px) on arrival.
- Before a click: 2–4 f micro-slowdown. Click: cursor scale 1→0.9→1 + target press 1→0.96→1 (8 f), effect ignites on the same frame (ripple, state change, camera punch).
- Typing: 18–28 chars/s with ±15 % deterministic jitter (seeded), caret blink only while idle.
- Human hesitation: 0.3–0.5 s pause where a person would think (choosing a tab, before "Run").

## Camera

- One camera container per scene wrapping the stage; animate scale + translate on it, not on every child.
- Establish wide → travel → arrive on subject. Push-in = attention/deeper; pull-back = arrival/reveal.
- One camera move at a time; never pan and zoom on unrelated axes simultaneously.
- Punch-in on clicks (100→120–135 %) ignites on the click frame; ease back over 0.5–0.8 s.
- Micro-push during long holds: ≤ 3 % over the hold, `sine.inOut`.
- Parallax: background moves 20–40 % of foreground camera travel.

## Seams (vector law)

1. Same axis across the cut (x→x, y→y, z→z).
2. Same direction; on z the sign of scale change must match (growing exit → growing entry). A shrinking exit answered by grow-from-small entry is the most common error.
3. Matched speed: exit `power4.in` + entry `power4.out`, same distance/duration; the incoming side starts ≥ 50 % along its path (mid-flight, never from rest).
4. Cut mid-motion on both sides. No dissolves between busy layouts (they make mud); if a crossfade is unavoidable, stagger it so layouts don't overlap at 50 %.
5. One dominant direction per film. Reserve others: up = conclusion; push-in = deeper; pull-back = arrival; burst = leaving a world. Never ping-pong consecutive seams. A direction change needs a visible cause.
6. Best seams use a carrier (cursor mid-path, card that docks into the next layout, a dot that grows into the next card, a word that becomes the next scene).
7. Use 2–3 seam types per film, repeated. Hard cuts on the beat are a seam type: use them.

## Sustained-motion routes (pick one per hold, name it in SPEC)

staged reveals · camera with intent · UI life (progress, counters, highlights stepping) · acted sequences (card files into stack, result assembles) · cursor-led action. Pause test: freeze any second; something meaningful must be mid-flight.

## Counters

~1 s ease-out; integer rounding with tabular numerals (`font-variant-numeric: tabular-nums`) so width doesn't jitter; optional soft glow in the accent that grows with the value; land on the final value ≥ 1.5 s before scene exit.

## Typography in motion

- Word-by-word or line-by-line reveals (3–5 f stagger), mask/clip reveals over raw fades.
- Never opacity-only for important changes: pair with 12–40 px translate or 0.9→1 scale.
- Kinetic type sized for phones: headline ≥ 72 px at 1080p, nothing important < 32 px.
