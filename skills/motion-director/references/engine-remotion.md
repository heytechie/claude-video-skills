# Engine: Remotion

React components rendered per frame. The `remotion-best-practices` skill owns API correctness; read it first. Licence: free for individuals and small companies; larger companies need a Remotion company licence. Check before commercial client work.

Install (once):
```bash
npx skills add remotion-dev/skills          # official skills
npx create-video@latest                      # new project (offers to add the skills)
```

## Mapping this skill onto Remotion
- Everything derives from `useCurrentFrame()` and `useVideoConfig()`. No `useEffect` timers, no CSS transitions/animations, no `Math.random()` (use `random(seed)` from `remotion`).
- One `<Sequence from durationInFrames>` per scene inside one `<Composition width=1920 height=1080 fps=60 durationInFrames=1800>`. Shared `theme.ts` (colors, fonts, easing tokens via `Easing.bezier(...)`, durations in frames) and `content.ts` (all copy and numbers).
- Shared components: `<Camera>` (scale/translate wrapper), `<Cursor>` (bezier arc path), `<Counter>` (`interpolate` + `Math.round`, tabular nums), `<Press>` (1→0.96→1 over 8 f).
- Entrances: `spring({ frame: frame - start, fps, config: { damping: 14 } })` for slight overshoot; `damping: 200` for none. Map with `interpolate(progress, [0,1], [from,to])`. Exits: `interpolate(frame, [a,b], [1,0], { easing: Easing.bezier(0.7,0,0.84,0), extrapolateLeft:'clamp', extrapolateRight:'clamp' })`.
- Always clamp `interpolate` extrapolation.
- Fonts: `@remotion/google-fonts/<Font>` `loadFont()`, or local `@font-face` with `delayRender()` until `document.fonts.ready` then `continueRender()`.
- Images/SVG: `staticFile()` + `<Img>`; Figma 1440-wide frames scaled by one uniform factor and centered on 1920.
- Audio: `<Audio src={staticFile('music.mp3')} />`; SFX as `<Sequence from={f}><Audio .../></Sequence>`.
- Variants: register extra `<Composition>`s for 1080×1920 and 1080×1080 that reuse scenes with center-based layout.
- Stills gate: `npx remotion still <CompId> out/s3.png --frame=900`.
- Render: `npx remotion render <CompId> out/video.mp4 --codec=h264 --crf=16 --pixel-format=yuv420p`.
- Studio (`npx remotion studio`) gives prop controls for fine tweaks; expose key timings as props via a zod schema.
