#!/usr/bin/env bash
# QA report for a rendered video: contact sheets, hard changes, freezes, black frames, specs, loudness.
# Usage: qa.sh <video.mp4> [out_dir] [scene_threshold=0.30]
set -euo pipefail

in="${1:?usage: qa.sh <video.mp4> [out_dir] [scene_threshold]}"
out="${2:-qa}"
thr="${3:-0.30}"
mkdir -p "$out"
report="$out/report.txt"

dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$in")

{
  echo "# QA report: $in"
  echo "duration_s: $dur"
  echo
  echo "## Video stream"
  ffprobe -v error -select_streams v:0 \
    -show_entries stream=codec_name,width,height,pix_fmt,r_frame_rate,avg_frame_rate,nb_frames \
    -of default=nw=1 "$in"
  echo
  echo "## Audio stream"
  ffprobe -v error -select_streams a:0 \
    -show_entries stream=codec_name,sample_rate,channels \
    -of default=nw=1 "$in" || true
  if [ -z "$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$in")" ]; then echo "(no audio stream)"; fi
} > "$report"

# Contact sheets: 2 fps, 6x5 tiles (15 s per sheet), timestamp burned in.
ffmpeg -v error -y -i "$in" -vf \
  "fps=2,scale=320:-2,drawtext=text='%{pts\:hms}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6,tile=6x5:padding=4:margin=4" \
  -fps_mode vfr "$out/sheet_%02d.png"

# Per-second strip for quick skim (1 fps, 10 per row).
ffmpeg -v error -y -i "$in" -vf \
  "fps=1,scale=192:-2,drawtext=text='%{pts\:hms}':x=4:y=4:fontsize=12:fontcolor=white:box=1:boxcolor=black@0.6,tile=10x6:padding=2" \
  -fps_mode vfr "$out/strip_%02d.png"

{
  echo
  echo "## Hard changes (scene score > $thr): compare with planned cuts; unplanned = pop/flash"
  ffmpeg -hide_banner -i "$in" -an -filter:v "select='gt(scene,$thr)',showinfo" -f null - 2>&1 \
    | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 | awk '{printf "  %.3f s\n", $1}' || true

  echo
  echo "## Freezes (>= 1.0 s with no visible change): compare with planned holds; long = dead air"
  ffmpeg -hide_banner -i "$in" -an -vf "freezedetect=n=0.003:d=1.0" -f null - 2>&1 \
    | grep -o 'freeze_\(start\|end\|duration\): [0-9.]*' | sed 's/^/  /' || true

  echo
  echo "## Black frames (>= 0.05 s)"
  ffmpeg -hide_banner -i "$in" -an -vf "blackdetect=d=0.05:pix_th=0.10" -f null - 2>&1 \
    | grep -o 'black_start:[0-9.]* black_end:[0-9.]* black_duration:[0-9.]*' | sed 's/^/  /' || true

  echo
  echo "## Loudness (target: -14 LUFS social / -16 web, true peak <= -1 dBTP)"
  if ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$in" | grep -q .; then
    ffmpeg -hide_banner -i "$in" -vn -af ebur128=peak=true -f null - 2>&1 \
      | sed -n '/Summary:/,$p' | grep -E 'I:|LRA:|Peak:' | sed 's/^ */  /'
  else
    echo "  (no audio)"
  fi

  echo
  echo "## Files"
  ls -1 "$out" | grep -E '^(sheet|strip)_' | sed 's/^/  /'
} >> "$report"

cat "$report"
