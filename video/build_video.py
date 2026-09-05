#!/usr/bin/env python3
"""Build the Track 2 pitch video (mp4 + vtt) from the script in track2/video_script.md.

Re-runnable. Reads OPENAI_API_KEY from ~/.env.digging at runtime; nothing secret
is stored in this file. Intermediates go to video/out/, which is gitignored.

Usage:
    python3 video/build_video.py            # full build (TTS is cached)
    python3 video/build_video.py --slides   # slides only, no audio, no assembly
"""

import json
import os
import pathlib
import re
import subprocess
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

REPO = pathlib.Path(__file__).resolve().parent.parent
VIDEO = REPO / "video"
OUT = VIDEO / "out"
OUT.mkdir(parents=True, exist_ok=True)

FINAL_MP4 = VIDEO / "mva_track2_pitch.mp4"
FINAL_VTT = VIDEO / "mva_track2_pitch.vtt"

W, H = 1920, 1080
BG = "#F6F4EE"
FG = "#1C1A17"
ACCENT = "#B8431F"
MUTED = "#6B655C"
MARGIN = 140
FOOTER = "MVA Hackathon 2026, Track 2, henkvaness. Hypothesis for follow-up."
TAIL = 0.35          # seconds of silence-tail padding per beat
CLOSING_SECONDS = 4.5  # silent final card

F_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
F_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
F_MONO = "/System/Library/Fonts/Menlo.ttc"

_font_cache = {}


def font(kind, size):
    key = (kind, size)
    if key not in _font_cache:
        path = {"reg": F_REG, "bold": F_BOLD, "mono": F_MONO}[kind]
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


# ---------------------------------------------------------------- slide engine

def wrap(text, width):
    return textwrap.wrap(text, width=width) or [""]


class Slide:
    def __init__(self):
        self.img = Image.new("RGB", (W, H), BG)
        self.d = ImageDraw.Draw(self.img)
        self.y = MARGIN

    def gap(self, px):
        self.y += px

    def line(self, text, kind="reg", size=44, color=FG, x=MARGIN, strike=False):
        f = font(kind, size)
        self.d.text((x, self.y), text, font=f, fill=color)
        w = self.d.textlength(text, font=f)
        if strike:
            ty = self.y + size * 0.62
            self.d.line([(x - 4, ty), (x + w + 4, ty)], fill=ACCENT, width=4)
        self.y += int(size * 1.42)
        return w

    def para(self, text, kind="reg", size=40, color=FG, chars=45, lead=1.38, x=MARGIN):
        f = font(kind, size)
        for ln in wrap(text, chars):
            self.d.text((x, self.y), ln, font=f, fill=color)
            self.y += int(size * lead)

    def rule(self, color="#D8D3C7"):
        self.gap(14)
        self.d.line([(MARGIN, self.y), (W - MARGIN, self.y)], fill=color, width=2)
        self.gap(24)

    def footer(self):
        f = font("reg", 22)
        self.d.text((MARGIN, H - 62), FOOTER, font=f, fill=MUTED)

    def save(self, path):
        self.footer()
        self.img.save(path)
        return path


def cols(slide, columns, size=24, header_size=30, top=None, caption=None):
    """columns: list of (header, subhead, [lines]) rendered as monospaced listings."""
    n = len(columns)
    avail = W - 2 * MARGIN
    colw = avail // n
    y0 = top if top is not None else slide.y
    fm = font("mono", size)
    for i, (header, sub, lines) in enumerate(columns):
        x = MARGIN + i * colw
        y = y0
        slide.d.text((x, y), header, font=font("bold", header_size), fill=FG)
        y += int(header_size * 1.35)
        if sub:
            slide.d.text((x, y), sub, font=font("reg", 24), fill=ACCENT)
            y += 36
        slide.d.line([(x, y), (x + colw - 50, y)], fill="#D8D3C7", width=2)
        y += 16
        for ln in lines:
            slide.d.text((x, y), ln, font=fm, fill=FG)
            y += int(size * 1.32)
        slide.y = max(slide.y, y)
    if caption:
        slide.gap(26)
        slide.line(caption, kind="bold", size=32, color=ACCENT)


def listing(path, limit=None):
    names = sorted(p.name for p in (REPO / path).iterdir() if p.is_file())
    if limit:
        extra = len(names) - limit
        names = names[:limit]
        if extra > 0:
            names.append(f"... +{extra} more")
    return names


# ---------------------------------------------------------------- the 12 beats

NARRATION = [
    "One child. Two changes in one gene, BUB1B. It makes the protein that checks "
    "chromosomes are shared out correctly when a cell divides.",

    "No approved medicine acts on that protein. So every candidate acts on a "
    "consequence instead. And no repurposed drug has ever been given to anyone with "
    "this syndrome, for the syndrome. Nothing in this work is expected to reduce this "
    "child's cancer risk. That is on the first page of the report, and it is said here.",

    "So the question changed. How do you search honestly when the answer is probably "
    "no? Two expert panels worked on the same five dossiers, blind to each other. "
    "Thirteen seats.",

    "Then ten divergent files, written without access to either panel. Then "
    "verification: every claim the arguments actually turned on, checked against the "
    "primary source. Then three independent referees. No seat could defer to the other "
    "panel, because no seat knew what it had written. This was built to find its own errors.",

    "It found them. The two candidates that looked best did not survive.",

    "Metformin fails on exposure. The concentration that did something in a dish is "
    "thirty two to a hundred and thirty fold above what a child reaches. Dose cannot "
    "close that gap. The ceiling is lactic acidosis.",

    "Senolytic therapy fails on three independent grounds. Any one of them is enough. "
    "There is no paediatric senolytic dose in any condition.",

    "Verification caught a survival figure that was wrong, sitting inside the clause "
    "written to stop cancer treatment being withheld. And a supporting allele turned "
    "out to be a splice variant, not a nonsense variant. It could not support the "
    "readthrough argument at all. Both corrections are printed in the report.",

    "What survives is smaller. First, a list of ordinary medicines to avoid, with a "
    "carve-out that protects cancer treatment. It is written by intent, not as a closed "
    "list, so it cannot be read as a reason to change a chemotherapy plan.",

    "Second, four additions to surveillance at no cost. One of them reads UGT1A1, the "
    "irinotecan safety marker, out of data that has already been sequenced.",

    "Third, a kidney work-up before any kidney drug, because two causes are possible "
    "and they need opposite treatments. Fourth, a measurement gate. Its first item "
    "returns a number that exists for no patient with this syndrome.",

    "The method transfers. Change the gene and the tool runs again: it queried a "
    "hundred and ten targets and returned twenty nine approved drugs in under six "
    "minutes. The gate is the part worth copying. What is not known: whether the two "
    "changes sit on separate copies, how much protein this child makes, whether the "
    "target is there at all. The report says so.",
]

SCRIPT_SECONDS = [12, 20, 12, 20, 6, 14, 10, 20, 16, 10, 14, 26]


def slide_1(s):
    s.gap(190)
    s.line("One child.", "bold", 96)
    s.gap(20)
    s.line("Two changes in one gene.", "bold", 96)
    s.gap(20)
    s.line("BUB1B", "bold", 96, color=ACCENT)
    s.gap(50)
    s.line("The protein that checks chromosomes are shared", "reg", 36, color=MUTED)
    s.line("out correctly when a cell divides.", "reg", 36, color=MUTED)


def slide_2(s):
    s.gap(90)
    s.para("No approved medicine acts on BubR1.", "reg", 52, chars=44)
    s.gap(34)
    s.para("No repurposed drug has ever been given to a "
           "person with this syndrome, for the syndrome.", "reg", 52, chars=44)
    s.gap(34)
    s.para("Nothing here is expected to reduce this "
           "child's cancer risk.", "bold", 58, color=ACCENT, chars=42)
    s.gap(30)
    s.line("REPORT_track2.md, section 1.", "reg", 26, color=MUTED)


def slide_3(s):
    s.gap(0)
    s.line("Two panels, same five dossiers.", "bold", 46)
    s.gap(2)
    s.line("Thirteen seats. Blind to each other.", "bold", 36, color=ACCENT)
    s.gap(26)
    cols(s, [
        ("track2/panel/", "Team 1, five seats", listing("track2/panel", 19)),
        ("track2/panel2/", "Team 2, eight seats", listing("track2/panel2", 19)),
    ], size=22)


def slide_4(s):
    s.gap(0)
    s.line("Divergence, then verification, then refereeing.", "bold", 46)
    s.gap(2)
    s.line("Three referees, all returned major revision.", "bold", 36, color=ACCENT)
    s.gap(26)
    cols(s, [
        ("track2/creative/", "ten divergent files", listing("track2/creative")),
        ("track2/verify/", "verification passes", listing("track2/verify")),
        ("track2/referees/", "three referee reports", listing("track2/referees")),
    ], size=22)


def slide_5(s):
    s.gap(360)
    s.para("Verification and refereeing removed the two "
           "strongest candidates.", "bold", 72, chars=36)


def slide_6(s):
    s.gap(30)
    s.line("Metformin, as a prescription.", "bold", 54)
    s.gap(26)
    s.para("The supporting experiment worked at 0.5 to 1.0 "
           "millimolar in mouse cells.", "reg", 40, chars=48)
    s.gap(20)
    s.para("Paediatric plasma metformin is 7.7 to 15.5 micromolar:",
           "reg", 40, chars=52)
    s.line("a gap of 32 to 130 fold.", "bold", 52, color=ACCENT)
    s.gap(16)
    s.para("Dose cannot close it. The ceiling is toxicological: "
           "above about 39 micromolar is the lactic acidosis range.",
           "reg", 40, chars=52)
    s.gap(16)
    s.line("Residual gap at the toxic ceiling: still 12.9 to 25.8 fold.",
           "bold", 36, color=ACCENT)
    s.gap(14)
    s.line("REPORT_track2.md, section 7.", "reg", 26, color=MUTED)


def slide_7(s):
    s.gap(30)
    s.line("Dasatinib is not a candidate at any rank.", "bold", 54)
    s.gap(30)
    items = [
        "Tumour direction unresolved.",
        "Growth deceleration acts through cartilage,\n     not avoided by intermittent dosing.",
        "Immune clearance suppressed within hours,\n     the same arm that may restrain aneuploidy.",
    ]
    for i, it in enumerate(items, 1):
        parts = it.split("\n")
        s.line(f"{i}.  {parts[0]}", "reg", 42)
        for extra in parts[1:]:
            s.line(extra, "reg", 42)
        s.gap(12)
    s.gap(14)
    s.line("Each objection fails the candidate on its own.", "bold", 36, color=ACCENT)
    s.gap(10)
    s.line("There is no paediatric senolytic dose in any condition.", "reg", 34)
    s.gap(10)
    s.line("REPORT_track2.md, section 7.", "reg", 26, color=MUTED)


def slide_8(s):
    s.gap(20)
    s.line("Two corrections, printed in the report.", "bold", 46)
    s.rule()
    s.line("A.  Survival figure, inside the safety carve-out", "bold", 32, color=MUTED)
    s.gap(8)
    x = MARGIN
    f = font("bold", 46)
    s.d.text((x, s.y), "85.0 against 72.4 percent", font=f, fill=MUTED)
    w = s.d.textlength("85.0 against 72.4 percent", font=f)
    s.d.line([(x - 4, s.y + 30), (x + w + 4, s.y + 30)], fill=ACCENT, width=5)
    s.d.text((x + w + 60, s.y), "86.5 against 73.7 percent", font=f, fill=ACCENT)
    s.y += 66
    s.line("Primary endpoint, disease-free survival, p=0.061, not significant.",
           "reg", 30)
    s.line("Found by the referees. Inside the safety carve-out.", "reg", 28, color=MUTED)
    s.rule()
    s.line("B.  Supporting allele, section 2", "bold", 32, color=MUTED)
    s.gap(8)
    s.d.text((x, s.y), "731X = nonsense allele", font=f, fill=MUTED)
    w = s.d.textlength("731X = nonsense allele", font=f)
    s.d.line([(x - 4, s.y + 30), (x + w + 4, s.y + 30)], fill=ACCENT, width=5)
    s.d.text((x + w + 60, s.y), "IVS16-2A>G, splice acceptor", font=f, fill=ACCENT)
    s.y += 60
    s.line("p.Ser714fsTer731", "bold", 36, color=ACCENT, x=x + w + 60)
    s.y -= 6
    s.line("Found by neither panel nor any referee.", "reg", 30)
    s.line("The readthrough argument built on it is withdrawn.", "reg", 28, color=MUTED)


def slide_9(s):
    s.gap(30)
    s.line("The avoidance rule carries its own carve-out.", "bold", 46)
    s.gap(28)
    s.d.line([(MARGIN, s.y), (MARGIN, s.y + 400)], fill=ACCENT, width=6)
    s.para("DOES NOT APPLY TO any antineoplastic agent given with "
           "curative, maintenance, relapse, disease-control or palliative "
           "intent, nor to radiotherapy given as local therapy with any of "
           "those intents.", "bold", 40, chars=52, x=MARGIN + 40)
    s.gap(14)
    s.para("Do not reduce, omit, delay or substitute any agent in a "
           "rhabdomyosarcoma protocol, or in any other cancer treatment "
           "plan, on the basis of this page.", "reg", 38, chars=54, x=MARGIN + 40)
    s.gap(24)
    s.line("Written by intent, not as a closed list.", "bold", 34, color=ACCENT)
    s.gap(6)
    s.line("REPORT_track2.md, section 5, repeated verbatim in section 7.",
           "reg", 26, color=MUTED)


def slide_10(s):
    s.gap(40)
    s.line("Four surveillance additions.", "bold", 54)
    s.gap(34)
    rows = [
        ("1.  UGT1A1 *28 and *6 before any irinotecan", "no cost"),
        ("2.  Bladder and, in girls, vagina added to the existing scan", "no cost"),
        ("3.  No assumed end date at age 7", "no cost"),
        ("4.  Full blood count on a draw already scheduled", "no cost"),
    ]
    for left, right in rows:
        f = font("reg", 40)
        s.d.text((MARGIN, s.y), left, font=f, fill=FG)
        s.d.text((W - MARGIN - 200, s.y), right, font=font("bold", 40), fill=ACCENT)
        s.y += 82
    s.gap(20)
    s.para("The UGT1A1 star 28 repeat is a promoter TA-repeat, and "
           "short-read sequencing calls it unreliably.", "reg", 30,
           color=MUTED, chars=70)
    s.gap(10)
    s.line("REPORT_track2.md, section 6, item 2.", "reg", 26, color=MUTED)


def slide_11(s):
    s.gap(24)
    s.line("The measurement gate, ordered by yield per cost.", "bold", 46)
    s.gap(30)
    s.line("Item 1.  Tubular panel, one visit.", "bold", 42)
    s.gap(4)
    s.para("Two causes are possible and they need opposite treatments. "
           "It decides which one operates, and sets every renal threshold "
           "from cystatin C.", "reg", 36, chars=62)
    s.gap(28)
    s.line("Item 4.  BubR1 immunoblot, against both parents and three controls.",
           "bold", 42)
    s.gap(10)
    s.d.line([(MARGIN, s.y), (MARGIN, s.y + 70)], fill=ACCENT, width=6)
    s.para("a figure that exists for no MVA patient", "bold", 46,
           color=ACCENT, chars=50, x=MARGIN + 34)
    s.gap(26)
    s.line("REPORT_track2.md, section 4.", "reg", 26, color=MUTED)


def slide_12(s):
    s.gap(24)
    s.line("The method transfers. Change the gene, run it again.", "bold", 44)
    s.gap(24)
    s.line("$ python pipeline/track2_drugmap/drugmap.py \\", "mono", 26)
    s.line("      --config pipeline/track2_drugmap/targets_bub1b.json \\", "mono", 26)
    s.line("      --out track2/creative/E_drugmap_output", "mono", 26)
    s.gap(16)
    rows = [
        ("rank", "drug", "harm flags"),
        ("1", "TRILACICLIB", "0"),
        ("2", "ABEMACICLIB", "1  myelosuppression"),
        ("3", "NIACIN", "1  nephrotoxicity"),
        ("4", "NIACINAMIDE", "1  nephrotoxicity"),
        ("5", "RIBOCICLIB", "1  myelosuppression"),
    ]
    for i, (a, b, c) in enumerate(rows):
        k = "bold" if i == 0 else "mono"
        col = MUTED if i == 0 else FG
        s.d.text((MARGIN, s.y), a, font=font(k, 28), fill=col)
        s.d.text((MARGIN + 120, s.y), b, font=font(k, 28), fill=col)
        s.d.text((MARGIN + 560, s.y), c, font=font(k, 28), fill=col)
        s.y += 42
    s.gap(20)
    s.line("110 targets, 148 molecules, 29 approved, 350 seconds.", "bold", 38, color=ACCENT)
    s.gap(10)
    s.para("Its top hit is its own limitation. It is a shortlist for a human.",
           "reg", 32, color=MUTED, chars=70)


def slide_close(s):
    s.gap(300)
    s.line("Track 2.", "bold", 80)
    s.gap(26)
    s.line("A hypothesis for follow-up.", "bold", 64, color=FG)
    s.gap(16)
    s.line("Not evidence that a medicine works.", "bold", 64, color=ACCENT)
    s.gap(46)
    s.para("What is not known: whether the two changes sit on separate "
           "copies, how much protein this child makes, whether the target "
           "is there at all. The report says so.", "reg", 32,
           color=MUTED, chars=72)


BUILDERS = [slide_1, slide_2, slide_3, slide_4, slide_5, slide_6,
            slide_7, slide_8, slide_9, slide_10, slide_11, slide_12]


def build_slides():
    paths = []
    for i, fn in enumerate(BUILDERS, 1):
        s = Slide()
        fn(s)
        p = OUT / f"slide_{i:02d}.png"
        s.save(p)
        paths.append(p)
    s = Slide()
    slide_close(s)
    p = OUT / "slide_13_close.png"
    s.save(p)
    paths.append(p)
    return paths


# ---------------------------------------------------------------------- audio

def api_key():
    env = pathlib.Path.home() / ".env.digging"
    for line in env.read_text().splitlines():
        m = re.match(r'\s*(?:export\s+)?OPENAI_API_KEY\s*=\s*["\']?([^"\'\s]+)', line)
        if m:
            return m.group(1)
    raise SystemExit("OPENAI_API_KEY not found in ~/.env.digging")


def tts(text, path, key):
    import requests
    if path.exists() and path.stat().st_size > 1000:
        return path
    instructions = ("Flat, level delivery. No lift at the end of lines. "
                    "Unhurried. Nothing here is read as good news.")
    for model, extra in (("gpt-4o-mini-tts", {"instructions": instructions}),
                         ("tts-1", {})):
        body = {"model": model, "voice": "ash", "input": text,
                "response_format": "mp3"}
        body.update(extra)
        r = requests.post("https://api.openai.com/v1/audio/speech",
                          headers={"Authorization": f"Bearer {key}"},
                          json=body, timeout=180)
        if r.ok:
            path.write_bytes(r.content)
            return path
        print(f"  {model} failed: {r.status_code} {r.text[:200]}", file=sys.stderr)
    raise SystemExit(f"TTS failed for {path.name}")


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def build_audio():
    key = api_key()
    paths = []
    for i, text in enumerate(NARRATION, 1):
        p = OUT / f"beat_{i:02d}.mp3"
        print(f"TTS beat {i:02d} ...")
        tts(text, p, key)
        paths.append(p)
    return paths


# ------------------------------------------------------------------- assembly

def build_segments(slides, audios):
    segs = []
    durations = []
    for i, (png, mp3) in enumerate(zip(slides, audios), 1):
        d = duration(mp3) + TAIL
        durations.append(d)
        seg = OUT / f"seg_{i:02d}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-i", str(png),
            "-i", str(mp3),
            "-f", "lavfi", "-t", str(d), "-i", "anullsrc=r=48000:cl=stereo",
            "-filter_complex", "[1:a]apad[a1];[a1]atrim=0:%.3f[aout]" % d,
            "-map", "0:v", "-map", "[aout]",
            "-c:v", "libx264", "-tune", "stillimage", "-r", "30",
            "-s", "1920x1080", "-pix_fmt", "yuv420p", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-t", "%.3f" % d, str(seg)
        ], check=True, capture_output=True)
        segs.append(seg)
    # closing silent card
    seg = OUT / "seg_13.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(slides[12]),
        "-f", "lavfi", "-t", str(CLOSING_SECONDS), "-i", "anullsrc=r=48000:cl=stereo",
        "-c:v", "libx264", "-tune", "stillimage", "-r", "30",
        "-s", "1920x1080", "-pix_fmt", "yuv420p", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", str(CLOSING_SECONDS), str(seg)
    ], check=True, capture_output=True)
    segs.append(seg)
    durations.append(CLOSING_SECONDS)
    return segs, durations


def concat(segs):
    lst = OUT / "concat.txt"
    lst.write_text("".join(f"file '{s}'\n" for s in segs))
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", "-movflags", "+faststart",
                    str(FINAL_MP4)], check=True, capture_output=True)
    return FINAL_MP4


def ts(sec):
    h = int(sec // 3600)
    m = int(sec % 3600 // 60)
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"


def write_vtt(durations):
    lines = ["WEBVTT", ""]
    t = 0.0
    for i, (d, text) in enumerate(zip(durations, NARRATION), 1):
        end = t + d - TAIL / 2
        lines += [str(i), f"{ts(t)} --> {ts(end)}"]
        lines += wrap(text, 62)
        lines.append("")
        t += d
    lines += ["13", f"{ts(t)} --> {ts(t + CLOSING_SECONDS)}",
              "Track 2. A hypothesis for follow-up.",
              "Not evidence that a medicine works.", ""]
    FINAL_VTT.write_text("\n".join(lines))
    return FINAL_VTT


def main():
    slides = build_slides()
    print(f"{len(slides)} slides rendered")
    if "--slides" in sys.argv:
        return
    audios = build_audio()
    segs, durations = build_segments(slides, audios)
    concat(segs)
    write_vtt(durations)
    total = sum(durations)
    print("\nbeat  audio+tail  script  delta")
    for i, d in enumerate(durations[:12], 1):
        sc = SCRIPT_SECONDS[i - 1]
        print(f"{i:>4}  {d:9.2f}s {sc:6}s {d - sc:+6.2f}s")
    print(f"closing card {durations[-1]:.2f}s")
    print(f"TOTAL {total:.2f}s = {int(total // 60)}:{total % 60:04.1f}")
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate",
                            "-of", "default=nw=1", str(FINAL_MP4)],
                           capture_output=True, text=True)
    print(probe.stdout)
    print(f"wrote {FINAL_MP4}\nwrote {FINAL_VTT}")


if __name__ == "__main__":
    main()
