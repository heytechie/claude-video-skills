# Engine: HyperFrames (default)

HTML + CSS + GSAP compositions rendered by seeking a paused timeline frame by frame, giving deterministic MP4. Apache-2.0. The `hyperframes` skill owns the render contract and CLI; read it first and obey its contract over anything here.

Install (once):
```bash
claude plugin marketplace add heygen-com/hyperframes && claude plugin install hyperframes@hyperframes
# or: npx hyperframes skills update
```
Optional companions: `npx skills add https://github.com/greensock/gsap-skills` (GSAP API).

## Mapping this skill onto HyperFrames
- New project: `npx hyperframes init <dir>`; website as the subject: `npx hyperframes capture <url> --json`.
- `index.html` root holds scene hosts, media and audio only; one scene per sub-composition in `compositions/`.
- Each timed element: `class="clip"`, `data-start`, `data-duration` (seconds). Each composition builds one paused GSAP timeline registered on `window.__timelines["<id>"]`.
- Put the easing tokens and durations from `motion-rules.md` in a shared JS/CSS theme; put copy and numbers in variables (`data-var-text`, CSS vars) so revisions are one-liners.
- Animate transforms, never `left/top/width/height`; never tween `display/visibility` on a `.clip` (animate a child).
- Cold-seek safe: render workers and `snapshot --at` jump straight to a time. Move elements only with property tweens (`fromTo` with `immediateRender:false` after a `tl.set` baseline); never position via `onUpdate` + `gsap.set` (curved cursor paths = x and y tweens on different eases). Verify with a single-time `snapshot --at T` at every click/landing.
- Custom fonts via `@font-face` to files in `assets/fonts/`.
- HyperFrames defaults to 30 fps. Set 60 fps if the brief asks (Sanji format) or keep 30 for social; state it in SPEC.
- Before hand-writing a named effect/transition/caption style, search the registry (`/hyperframes-registry`).
- Gates: `npx hyperframes check --json` (fix every error) → `npx hyperframes snapshot --review` for stills → preview → render only after approval.
- Render flags (verified v0.8.201): iterate with `npx hyperframes render -q draft -f 30`; deliver with `-q delivery` (or default `looks`, CRF 16) at the SPEC fps. `-w <n>` sets parallel Chrome workers (~256 MB RAM each, default auto); lower it if RAM is tight. `--gpu` uses GPU encoding. `-c compositions/<scene>.html` renders one scene. `--strict` fails on lint errors. `--variables '{"key":"val"}'` swaps copy/numbers for client revisions without editing files. `--format mov|png-sequence` gives alpha output for AE/Premiere/Resolve overlays.
- Note: HyperFrames reports HeyGen plan usage; avatars/TTS via HeyGen cost money. Rendering HTML is free.

## No-framework fallback (zero dependencies)
Single `index.html` exposing `window.seek(t)` that sets every style as a pure function of `t` (closed-form springs/eases; no CSS transitions/animations). Capture with Playwright: for each frame `await page.evaluate(t => seek(t), i/fps)`, `await document.fonts.ready` before frame 0, screenshot to `frames/%05d.png`, then:
```bash
ffmpeg -framerate 60 -i frames/%05d.png -i audio.wav -c:v libx264 -pix_fmt yuv420p -crf 16 -c:a aac -shortest out.mp4
```
Optional motion blur: render N=8 subframes per frame and blend (`tmix=frames=8`); 4 subframes ghost.
