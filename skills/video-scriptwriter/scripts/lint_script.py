#!/usr/bin/env python3
"""Lint a SCRIPT.md produced by the video-scriptwriter skill.

Usage: python3 lint_script.py SCRIPT.md
Exit code 1 if any ERROR.
"""
import re
import sys

BEATS = {"hook", "problem", "turn", "proof", "payoff", "cta"}
BANNED_WORDS = [
    "seamless", "seamlessly", "powerful", "intuitive", "robust", "cutting-edge", "next-level",
    "revolutionary", "revolutionize", "revolutionise", "game-changer", "game-changing",
    "supercharge", "unlock", "effortless", "effortlessly", "elevate", "empower", "leverage",
    "streamline", "reimagine", "reimagined",
]
BANNED_PHRASES = [
    "in seconds", "save hours", "say goodbye to", "the future of", "is here",
    "we're excited", "we are excited", "all-in-one", "we added ai", "next generation",
]
BANNED_OPENERS = ("introducing", "meet ", "we're excited", "we are excited")
# Lessons from review (2026-10-28): walkthrough captions, UI-mechanic stakes and
# invisible-state captions made a feature script read "vague" and like any other promo.
TUTORIAL_START = re.compile(r"^(click|tap|pick|select|choose|go to|open|then|press|scroll|hit)\b", re.I)
STEP_LABEL = re.compile(r"^\d+\s*[·.):]")
UI_MECHANICS = re.compile(r"\b(pages?|pagination|tabs?|dropdowns?|toggles?|rows per page)\b", re.I)
INVISIBLE_STATE = re.compile(r"^already (set|selected|filled|picked)\b", re.I)

errors, warns = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def header(text, key):
    m = re.search(rf"^{key}:\s*(.+)$", text, re.M | re.I)
    return m.group(1).strip() if m else None


def num(s):
    m = re.search(r"[-+]?\d+(?:\.\d+)?", s or "")
    return float(m.group()) if m else None


def words(s):
    toks = [t for t in re.split(r"\s+", s.strip()) if t and not re.fullmatch(r"[→\-–—/|·•.,!?:;]+", t)]
    return len(toks)


def cards(cell):
    cell = cell.strip()
    if not cell:
        return []
    parts = [p.strip() for p in cell.split(" / ")]
    return [p.strip('"“”\'') for p in parts if p.strip('"“”\' ')]


def lint_card_style(label, text):
    t = text.strip()
    if TUTORIAL_START.search(t) and not STEP_LABEL.search(t):
        warn(f"{label}: walkthrough caption {t!r}: show the step, or number it on a counter ('1 · Open export')")
    if UI_MECHANICS.search(t):
        warn(f"{label}: UI-mechanic word in {t!r}: use units the viewer thinks in (₹, orders, payouts, days, clicks)")
    if INVISIBLE_STATE.search(t):
        warn(f"{label}: {t!r} depends on a state the viewer may not have seen; caption only what happens on screen")


def lint_copy(label, text):
    low = " " + text.lower() + " "
    for w in BANNED_WORDS:
        if re.search(rf"(?<![a-z]){re.escape(w)}(?![a-z])", low):
            err(f"{label}: banned word '{w}' in: {text!r}")
    for p in BANNED_PHRASES:
        if p in low:
            err(f"{label}: banned phrase '{p}' in: {text!r}")
    if re.search(r"\bnot\s+[^.]{1,40}\.\s+[a-z]", text, re.I):
        warn(f"{label}: possible 'Not X. Y.' structure: {text!r}")


def section(text, name):
    m = re.search(rf"^##\s+{name}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S | re.I)
    return m.group(1) if m else None


def main(path):
    text = open(path, encoding="utf-8").read()

    total = num(header(text, "Total"))
    if total is None:
        err("Header 'Total: <seconds>' missing")
    fps = num(header(text, "FPS"))
    audio = (header(text, "Audio") or "").lower()
    status = (header(text, "Status") or "").upper()
    fps_ = num(header(text, "First product shot"))
    if fps_ is None:
        err("Header 'First product shot: <seconds>' missing")
    elif fps_ > 5:
        err(f"First product shot at {fps_}s (> 5s; platforms want product/brand by 5s)")
    elif fps_ > 2.5:
        warn(f"First product shot at {fps_}s (top-brand median is 2.5s)")
    if not header(text, "Archetype"):
        warn("Header 'Archetype' missing")

    hooks = section(text, "Hooks")
    if hooks is None:
        err("Section '## Hooks' missing")
    else:
        n = len(re.findall(r"^\s*-\s", hooks, re.M))
        if n < 3:
            warn(f"Only {n} hook entries; keep chosen + ≥2 variants (write ≥5 in drafting)")
        for line in hooks.splitlines():
            for q in re.findall(r'"([^"]+)"', line):
                lint_copy("Hooks", q)

    ledger = section(text, "Claims ledger")
    if ledger is None or len([l for l in ledger.splitlines() if l.strip().startswith("|")]) < 3:
        warn("Claims ledger missing or empty: every claim/number needs a source row")

    beats_sec = section(text, "Beats")
    if beats_sec is None:
        err("Section '## Beats' missing")
        return report()
    rows = [l for l in beats_sec.splitlines() if l.strip().startswith("|")]
    if len(rows) < 3:
        err("Beat table has no rows")
        return report()
    head = [c.strip().lower() for c in rows[0].strip().strip("|").split("|")]
    need = ["#", "beat", "start", "end", "on-screen", "vo", "visual", "sound"]
    if head[: len(need)] != need:
        err(f"Beat table columns must be {need}, got {head}")
        return report()

    prev_end = 0.0
    first_text_checked = False
    early_text = []
    parsed = []
    for raw in rows[2:]:
        c = [x.strip() for x in raw.strip().strip("|").split("|")]
        if len(c) < 8:
            err(f"Malformed row: {raw}")
            continue
        idx, beat, start, end, onscreen, vo, visual, sound = c[:8]
        beat = beat.lower()
        s, e = num(start), num(end)
        tag = f"Beat {idx} ({beat})"
        if beat not in BEATS:
            err(f"{tag}: beat must be one of {sorted(BEATS)}")
        if s is None or e is None or e <= s:
            err(f"{tag}: bad Start/End")
            continue
        if abs(s - prev_end) > 1e-6:
            err(f"{tag}: starts at {s}s but previous beat ended at {prev_end}s (must be contiguous)")
        prev_end = e
        dur = e - s
        parsed.append((beat, s, e))

        cs = cards(onscreen)
        if cs and not first_text_checked:
            first_text_checked = True
            if cs[0].lower().startswith(BANNED_OPENERS):
                err(f"{tag}: first on-screen line opens with a banned opener: {cs[0]!r}")
        per_card = dur / len(cs) if cs else dur
        if s < 4.0:
            early_text.extend(cs)
        for card in cs:
            w = words(card)
            lint_copy(tag, card)
            lint_card_style(tag, card)
            if w > 6:
                err(f"{tag}: {w} words on one card (max 6): {card!r}")
            if len(card) > 42:
                warn(f"{tag}: {len(card)} characters on one card (aim ≤ 42): {card!r}")
            need_hold = 0.3 * w + 0.5
            if beat == "cta":
                need_hold = max(need_hold, 2.0)
            if per_card + 1e-6 < need_hold:
                err(f"{tag}: card {card!r} gets ~{per_card:.2f}s, needs ≥ {need_hold:.2f}s to read")
        if vo:
            lint_copy(tag + " VO", vo)
            wps = words(vo.strip('"“”')) / dur
            if wps > 2.8:
                err(f"{tag}: VO {wps:.2f} words/s (max 2.5; cut words)")
            elif wps > 2.5:
                warn(f"{tag}: VO {wps:.2f} words/s (target ≤ 2.5)")
        if not visual:
            err(f"{tag}: Visual is empty")
        if not sound and "silent" not in audio:
            warn(f"{tag}: no Sound cue")
        if total and total <= 30 and dur > 6 and beat != "proof":
            warn(f"{tag}: {dur:.1f}s is long for a short film; change something every 1.5–3s")

    if early_text and not any(re.search(r"\d", t) for t in early_text):
        warn("No number in the first 4 s of on-screen copy: a stake lands harder with a concrete number or time ('11:48 PM.', '1,126 payouts')")
    if parsed:
        if parsed[0][0] != "hook":
            err("First beat must be 'hook'")
        elif parsed[0][2] > 3.0:
            warn(f"Hook runs to {parsed[0][2]}s; the point must land within ~2–3s")
        if parsed[-1][0] != "cta":
            warn("Last beat is not 'cta'")
        if total is not None and abs(prev_end - total) > 1e-6:
            err(f"Beats end at {prev_end}s but Total is {total}s")
    if fps is None:
        warn("Header 'FPS' missing (motion-director defaults to 60)")
    if status not in ("DRAFT", "APPROVED"):
        warn("Header 'Status' should be DRAFT or APPROVED")
    return report()


def report():
    for e in errors:
        print(f"ERROR  {e}")
    for w in warns:
        print(f"WARN   {w}")
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
