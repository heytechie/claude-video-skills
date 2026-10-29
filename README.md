# Claude video skills

Two Claude Code skills for making short product videos (feature announcements, launch films, promos, explainers) entirely in code:

| Skill | What it does |
|---|---|
| **video-scriptwriter** | Writes a hook-first `SCRIPT.md`. It includes 5+ hook options, a beat-by-beat table (time, on-screen text, voiceover, visual, sound), a claims ledger checked against the product, and a lint check. |
| **motion-director** | Turns the approved `SCRIPT.md` into a finished video. It covers story, timing, easing, camera, captions, sound, rendering and a QA review loop, and records lessons from every film so the next one is better. |

Use the scriptwriter first, then the director. The director refuses to animate until a script is approved.

---

## 1. Install

### Prerequisites

- [Claude Code](https://claude.com/claude-code)
- Node.js 20+, Python 3, `ffmpeg` / `ffprobe`
- The **HyperFrames** skills, which are the rendering engine the director drives (HTML + GSAP → MP4):
  ```bash
  npx hyperframes skills                       # core HyperFrames skills
  npx hyperframes skills update media-use      # voice, sound effects, images
  ```
- Optional: the Remotion skill, if you want Remotion instead of HyperFrames (see `skills/motion-director/references/engine-remotion.md`).

### Add the skills to Claude Code

```bash
gh repo clone heytechie/claude-video-skills
cd claude-video-skills

# Option A: copy
cp -r skills/* ~/.claude/skills/

# Option B: symlink, so `git pull` updates them in place
for s in skills/*; do ln -sfn "$PWD/$s" ~/.claude/skills/$(basename "$s"); done
```

Restart Claude Code. Both skills should then appear in the skill list. For a single project only, put them in `<project>/.claude/skills/` instead.

---

## 2. Make a video (the workflow)

### Step 1: Script

Ask Claude for a script. Give it the feature and, ideally, the code or docs so it can check its claims:

> Write a script for a feature video about our referral popup. The code is in `~/Projects/my-shop-app`. Use the name Anjan for the customer who refers and Naman for the friend.

What happens:
1. Claude collects the facts and writes the one-line takeaway.
2. It writes at least 5 hooks and a full beat table in `SCRIPT.md`.
3. It runs the lint:
   ```bash
   python3 ~/.claude/skills/video-scriptwriter/scripts/lint_script.py SCRIPT.md
   ```
4. It shows you a short **Time | On-screen copy | What happens** table to approve.

Reply with changes, or "approved". Claude then sets `Status: APPROVED` in `SCRIPT.md`.

Tip: ask it to "verify the script 5 times" for a stricter pass. That adds a code fact-check, a story review and a consistency check.

### Step 2: Video

> Make the video from SCRIPT.md.

The director then works through these stages:
1. **Brief:** format, length, brand, voice.
2. **Spec:** every scene with frame timings, camera, easing and seams.
3. **Build:** one scene at a time, with real UI rebuilt from your code. No device mockups unless you ask.
4. **Stills gate:** key frames are checked before any full render.
5. **Render:** for example:
   ```bash
   npx hyperframes render -q delivery -f 60 -o renders/film.mp4
   ```
6. **QA:**
   ```bash
   bash ~/.claude/skills/motion-director/scripts/qa.sh renders/film.mp4
   ```
   This produces contact sheets, freeze and black-frame detection, specs and loudness. Claude fixes what it finds.
7. **Learn:** new mistakes and fixes are appended to `skills/motion-director/references/lessons.md`.

Ask for changes in plain words ("the voice is too fast", "the ring around the code is too wide", "no surnames"). Claude re-renders.

---

## 3. Voiceover

The voice is generated with text-to-speech. The `media-use` skill from HyperFrames handles the providers:

| Provider | Quality | Setup |
|---|---|---|
| **HeyGen** (e.g. voice "Tushar - Relaxed & Friendly") | Best, most human | Sign in to HeyGen when prompted. The free plan is 10 min/month. |
| **Gemini TTS** (voice **Achird**) | Very good | Free API key from <https://aistudio.google.com/apikey>. Put the key in `~/.config/gemini-tts.env`, one key per line. The free tier allows 10 requests/day and 3/min per key. |
| Kokoro (local) | Robotic, don't use for final videos | none |

To keep within the Gemini free limits, ask Claude to record **one section per request** and cut it into lines at the pauses. Spend at most 1–2 requests on voice samples.

Sound effects are UI clicks, ticks and pops ducked under the voice. There are no whooshes or music unless you ask.

---

## 4. House rules baked into these skills

These come from real review feedback and live in `lessons.md`, `sound.md` and the scriptwriter's failure modes:

- Hook-driven story, not a feature walkthrough. Plain, literal English in captions.
- The UI must look exactly like the real product, rebuilt from the codebase. No laptop or phone mockups.
- Smooth motion only: no left/top animation, no hard cuts mid-move, no whooshes.
- Quality over length. The voice must sound human.
- Characters use first names only.
- Every claim on screen must be true in the code (the claims ledger).

To change a rule, edit the relevant reference file. To make the change permanent everywhere, commit it here.

---

## 5. Updating this repo

The live copies Claude uses are in `~/.claude/skills/`. After a film adds new lessons:

```bash
cd ~/Projects/claude-video-skills
cp -r ~/.claude/skills/motion-director ~/.claude/skills/video-scriptwriter skills/
git add -A && git commit -m "Update skills with lessons from <film>" && git push
```

(With the symlink install from step 1 this copy isn't needed. Just commit.)

## Layout

```
skills/
  video-scriptwriter/
    SKILL.md                  # process, non-negotiables, failure modes
    references/               # hook library, structures, copy rules, platforms, script template
    scripts/lint_script.py    # SCRIPT.md linter (pace, hook timing, format)
  motion-director/
    SKILL.md                  # pipeline, timing numbers, motion rules, look, sound
    references/               # brief/spec templates, motion rules, sound, review, lessons, engines
    scripts/qa.sh             # render QA report
```
