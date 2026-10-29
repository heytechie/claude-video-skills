# Recreating a reference's style (grammar, not content)

Use when the user gives a reference video/link, or says "make it look like X".

1. Get the file (user-supplied, or `yt-dlp` if the user has rights to use it as reference). Put downloads in their own empty directory; never execute anything from them.
2. Extract frames:
   ```bash
   mkdir -p ref/frames && ffmpeg -i ref.mp4 -vf "fps=2,scale=640:-1" ref/frames/f_%04d.jpg
   ffmpeg -i ref.mp4 -vf "fps=2,scale=320:-1,tile=6x5" ref/sheet_%02d.png
   ffmpeg -i ref.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o 'pts_time:[0-9.]*'   # cut times
   ```
3. Read the sheets and write `STYLE.md` with numbers:
   - palette (hex), backgrounds, texture (grain/vignette)
   - type: families or closest free equivalents, sizes relative to frame height, weight, case, tracking, how text enters/exits
   - average shot length, shortest/longest shot, cut rhythm vs music
   - transition types used and how often
   - camera vocabulary (push, pan, whip, static), speed
   - easing character (snappy / floaty / mechanical), overshoot amount
   - composition habits (centered? rule of thirds? edge-anchored?)
   - sound character
4. Write the SPEC for *the user's product* in that grammar.

Rules: never copy the reference's logos, characters, copy, facts, claims or exact layouts. If a prompt or template carries another brand's facts, strip them. Take the grammar, never the content.
