# Sound

Sound sells motion. A silent film reads as unfinished; a badly scored one reads as AI.

## Beat grid first
1. Pick or receive the track (default 100–120 BPM for launch films). Royalty-free sources: user-supplied, Pixabay Music, Uppbeat, Artlist/Epidemic (user's licence). Never use copyrighted commercial songs without a licence.
2. Analyse it into `beats.json` (beats, downbeats, the drop) using python (librosa / aubio / numpy onset energy). **Verify the drop by bass energy** (20–150 Hz RMS jump) because auto beat detectors often pick the kick entry instead of the real drop.
   - In UI films the clicks follow the cursor, not a beat, so a drum groove clashes with them (WhatsApp film). Use a drumless bed (pad or ambient) placed so its section changes land on scene changes, and offer 2 options instead of forcing a beat grid.
3. Retime the SPEC to the grid: scene cuts and hard cuts on downbeats, hero hits on the strongest accent, the payoff on (or right after) the drop.
4. Lock audio as the clock. If music or VO changes, re-time and re-check seams.

## SFX
- Only on visible actions: click, card land, checkmark, message pop, logo hit.
- **No whooshes, sparkles or impacts by default** (ReferRush user found them irritating, 2026-10-26). UI sounds only: clicks, typing, pops, ticks, a soft success chord, one end chime.
- Sparse. Over-SFX is the #1 amateur tell. If two events are < 0.25 s apart, keep one sound.
- Real recorded SFX (Mixkit, Pixabay SFX, Zapsplat, user libraries) over synthesized beeps.
- Place each SFX at the action frame (±10 ms); align the transient peak, not the file start.
- Mix SFX 6–12 dB under music peaks; duck music −4 to −6 dB under VO.

## Structure
- A short silence or filter-drop (0.3–0.75 s) right before the payoff makes it land.
- Fade music out over the end card, or end on a hard stop on the last beat with the logo hit.
- 30 ms audio fades at every audio cut (no clicks).

## VO (only if asked)
- Script written for the ear: short sentences, complements visuals, never reads on-screen text verbatim.
- Generate (ElevenLabs / Fish Audio / Kokoro), get word timestamps (Whisper/WhisperX/Parakeet), re-time scenes to real word times; never squeeze a read to fit a slot.
- What worked (ReferRush Exports, 2026-10-28, user: "must sound like a human, not an AI"):
  - HeyGen Starfish via media-use `heygen-tts.mjs` (word timestamps included). Let the user pick from 4–5 voice samples reading the opening section.
  - Record **one continuous take per section**, never line by line (per-line takes reset the intonation and sound robotic). loudnorm I=−17, then cut into lines at the midpoints of the word gaps.
  - The voice is the clock. Keep a `VO` list of (line id, visual gap before, text): starts are cumulative (previous end + gap), durations are measured, and every animation time is anchored to a line start or a spoken word (`W(line, word)`), e.g. the click lands on "Export".
  - Gaps: 0.3–0.4 s inside a thought, ≤ 1.0 s where an action must play out. Never review a voiced film silently; it feels slow.
  - Mix: VO bus via adelay; duck SFX under it with sidechaincompress; alimiter; always bound with `-t TOTAL`.
  - Plain, literal, conversational English, like showing another store owner. Read big amounts on screen, not aloud.
- Burn-in captions on social; captions on their own track inside title-safe.

## Loudness (ffmpeg)
```bash
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -c:v copy -c:a aac -b:a 192k out.mp4   # social
# web: I=-16
```
