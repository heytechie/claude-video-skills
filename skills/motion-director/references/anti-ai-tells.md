# Anti-AI tells

These are the specific things professional motion designers and editors mock in Claude- and AI-made videos (r/MotionDesign, r/AfterEffects, r/ClaudeAI, X). Check every draft against this list.

| Tell (what pros say) | Why it happens | Fix |
|---|---|---|
| "Pacing is awful"; constant easing, no tension/relief, no sharp cuts | Every move gets the same smooth curve | Mix hard cuts on the beat with eased moves; build to a stillness-before-climax; vary scene energy (calm → build → peak → resolve) |
| "Looks like PowerPoint / a website moving" | Scenes authored as separate slides; fades between them | Seams with carriers and match cuts; outgoing scene creates the next; one camera world |
| Text disappears before you can read it; crams info, 1–2 s per item | No hold budget | Readability holds table; ≤ 6 words on screen; one idea per scene; cut content, not hold time |
| Typography is "square", timid | Default sizes, no hierarchy | Hero type ≥ 3× body; bold weight contrast; let one word fill the frame |
| Bounce expression on everything | Overshoot as default | Overshoot ≤ 5 % and only on heroes; most moves no overshoot |
| Fades "straight from 2000" | Long opacity transitions | Short (≤ 0.3 s) or none; use masks, moves, morphs |
| Synth "ding" SFX on everything | Python-synthesized blips | Real recorded SFX library, sparse, only on visible actions; mix under music |
| Same dark glassy 3D glow look | Model default aesthetic | Ban it in SPEC; follow the brand; consider warm light 2D / editorial looks |
| Generic copy pasted from the website | Copywriting skipped | Write for video: short, concrete, verb-led; banned SaaS words list |
| Everything moves at once | No choreography | ≤ 1/3 of elements moving; lead with hero; stagger 2–4 f |
| Floating text drifts off its anchor; layout "like a broken physics sim" | Absolute positions from a different canvas size; transforms fighting | Lock canvas, layout from center, parent groups, scale Figma frames uniformly |
| Elements idly breathing/floating | "Nothing should stop" taken literally | Sustained motion must perform (story routes), not wobble |
| Fallback font (Times New Roman) in frames | Font not loaded before capture | Load fonts before frame 0; QA stills at frame 0 of each scene |
| Counter jumps to final value | No interpolation | ~1 s ease-out count |
| Wrong CTA hierarchy | No end-card design | End card: logo > one line > CTA/URL, hold ≥ 2 s |
| Invented facts or numbers ("1M users") | Copied prompt/reference carried someone else's facts | Only numbers from the brief; never transfer reference content |

## Remember
- "Smooth doesn't mean good." Focus points and rhythm matter more than buttery easing.
- Planning > generation: what is shown, in what order, for how long, with what emphasis.
- Showing Claude one excellent reference beats ten rounds of vague feedback.
