# SCRIPT.md: format (the handoff contract with motion-director)

Keep the headings and the beat-table columns exactly as below: `lint_script.py` and motion-director parse them.

````markdown
# SCRIPT: [Product] [Feature] [type]
Status: DRAFT            <!-- DRAFT | APPROVED -->
Total: 18.0 s
FPS: 60
Formats: 16:9 master; 1:1, 9:16 cutdowns
Audio: music + sfx       <!-- music + sfx | vo + music | silent -->
Music: ~110 BPM, minimal electronic, drop at 13.0 s
Archetype: F2 Before → after
First product shot: 2.0 s

## Brief
Product: …
Feature: …
Audience: …
Platform: …
Goal / CTA: …
The one thing: You can now …
Takeaway (viewer's words): …
Spine: [one viewer] does [one real task] with [concrete data]
Tone: …
Brand: colors #…, #…; fonts …; logo path …
UI source: …

## Claims ledger
| ID | Claim | Source |
|---|---|---|
| C1 | … | product page /features/x |

## Hooks
- **Chosen:** [pattern] Visual: … / Text: "…" / VO: …
- Variant B: [pattern] …
- Variant C: [pattern] …
- Rejected: … (why)

## Beats
| # | Beat | Start | End | On-screen | VO | Visual | Sound |
|---|---|---|---|---|---|---|---|
| 1 | hook | 0.0 | 2.0 | "…" | | … | … |

## Assets needed
- [ ] Screen: … (per beat)

## Cutdowns
- 15 s: beats …
- 9:16: …

## Checks
- [x] lint_script.py: 0 errors
- [x] Muted test · [x] Pictures test · [x] Hook test · [x] Spine test · [x] Buildable test
````

Present to the user as a compact table (their review format), not the full beat table:

| Time | On-screen copy | What happens |
|---|---|---|
| **0–4s** | **11:48 PM. Your accountant needs 1,126 payouts.** | Payouts page with **1,126** visible. Vikram's message arrives: "Last 90 days of payouts? Need it by tomorrow 🙏" |

Column rules:
- **Beat** ∈ `hook | problem | turn | proof | payoff | cta`.
- **Start/End** in seconds, contiguous; the last End equals `Total`.
- **On-screen**: exact text in quotes; several cards in one beat separated by ` / `. Empty if the UI carries it. UI text the camera reads goes in Visual as `[UI: "…"]` (not counted as card text).
- **VO**: exact line or empty.
- **Visual**: what the real product does; reference ledger IDs for claims (`C2`).
- **Sound**: music event or SFX on a visible action.

---

## Filled example (illustrative product "Ledgerly", feature "Auto-reconcile")

```markdown
# SCRIPT: Ledgerly Auto-reconcile feature video
Status: DRAFT
Total: 18.0 s
FPS: 60
Formats: 16:9 master; 1:1, 9:16 cutdowns
Audio: music + sfx
Music: ~110 BPM minimal electronic, drop at 13.0 s
Archetype: F2 Before → after
First product shot: 2.0 s

## Hooks
- **Chosen:** [Relatable moment] Visual: clock 23:47 over a wall of bank-statement rows / Text: "Month-end. 412 unmatched rows."
- Variant B: [Old vs new] Text: "Reconciling: 2 days → 1 click"
- Variant C: [Self-check] Text: "Still matching rows by hand?"

## Beats
| # | Beat | Start | End | On-screen | VO | Visual | Sound |
|---|---|---|---|---|---|---|---|
| 1 | hook | 0.0 | 2.5 | "Month-end. 412 unmatched rows." | | clock 23:47, rows scroll endlessly (C1 count) | low pulse, clock tick |
| 2 | problem | 2.5 | 5.5 | "Copy. Search. Match. Repeat." | | cursor ping-pongs between statement and ledger, hesitates | soft clicks on each match |
| 3 | turn | 5.5 | 7.5 | "Now: Auto-reconcile" | | cursor clicks [UI: "Auto-reconcile"]; press, camera punch-in 125 % | click on press |
| 4 | proof | 7.5 | 13.0 | "Matched as you watch" | | rows pair up and turn green in a cascade; counter 412 → 0 (C1) | rising riser into drop |
| 5 | payoff | 13.0 | 15.5 | "0 left" | | clean ledger, camera pulls back to full app | drop hits on "0" |
| 6 | cta | 15.5 | 18.0 | "Live on all plans" | | logo carried in by the last matched row; ledgerly.com/reconcile | final hit, music tail |
```

Lint arithmetic for this example: card 1 = 4 words → min hold 1.7 s ≤ 2.5 ✓; card 2 = 4 words → 1.7 ≤ 3.0 ✓; CTA 4 words, holds 2.5 s ✓; total 18.0 ✓; first product shot 2.0 s ≤ 5 ✓.

---

## Filled example 2 (gold standard): ReferRush Exports, hook chain, 40 s (written by the user, 2026-10-28)

This is the bar for feature videos. Every line is a stake, a promise, a numbered step, the mechanic, a proof, a bonus, a loop-closer, breadth, a callback or the tagline/CTA.

| Time | On-screen copy | What happens |
|---|---|---|
| 0–4s | 11:48 PM. Your accountant needs 1,126 payouts. | Payouts page with 1,126 visible. Vikram's message arrives: "Last 90 days of payouts? Need it by tomorrow 🙏" |
| 4–6s | Here's the file. In 3 clicks. | Message moves aside. Cursor heads toward Export. |
| 6–11s | 1 · Open export → 2 · Last 90 days → 3 · Export | Show each real action. Counter increments only when the click happens. Match labels to the actual UI. |
| 11–15s | Over 30 days? We email it when it's ready. | Hold on the real confirmation toast. Brief laptop-close transition. |
| 15–19s | Ready in your inbox. | Open "Your payouts export is ready." Highlight Rows: 1,126. |
| 19–23s | All 1,126 payouts. One CSV. | Download and open the file. Show its column headers and populated rows. |
| 23–27s | Total included: ₹2,48,600 | Jump to the final row, with enough surrounding context to show it belongs to the file. |
| 27–30s | Sent. Before tomorrow. | File sent to Vikram. Reply: "Perfect, thank you! 🙌" |
| 30–34s | Export your other lists, too. | Four quick, clearly labelled shots: Referrers · Affiliates · Orders · Free products. Show the export control in each. |
| 34–37s | 1,126 payouts → 3 clicks. | Return to the opening payout count beside the completed counter. |
| 37–40s | Less admin. More referrals. | ReferRush logo. "Referral & affiliate programs for Shopify." Get started at referrush.com |

In SCRIPT.md, each line becomes its own beat or card, so lint can check the holds. Two-part lines ("11:48 PM." + the stake; "Over 30 days?" + the answer) build as two cards. Steps 1–3 become three beats of ~1.6 s. The full version is `outputs/export-video/SCRIPT.md` (rev 5).

What the earlier drafts got wrong, and this fixes: tutorial captions ("Click Export, pick the payouts"), a UI-mechanic stake ("57 pages"), a puzzle instead of a promise ("Count the clicks"), a caption about a state the viewer never saw ("Already set: last 90 days"), a feature-list ending, and 53 s of runtime.
