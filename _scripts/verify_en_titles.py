"""Verify official 5e English chapter titles across every title surface.

Checks (exit 0 iff all pass):
1. html/ch01-26.html    -- subtitle EN span == official title.
2. html_v2/ch01-26.html -- subtitle EN span AND <div class="cent"> content.
3. _agent_spec.md       -- EN text after the last '|' on each table row.
4. HEAD byte-suffix     -- bytes after the EN span on each subtitle line are
                          identical to `git show HEAD:<path>` (nothing after
                          the title may change).

The EN span is the text between the tag's '>' and the first delimiter
'(' / U+FF08 / '|' / U+FF5C. All comparisons are byte/UTF-8 exact after
strip; line endings are never rewritten (bytes in, bytes out).
"""
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

with io.open(os.path.join(HERE, "five_e_titles.json"), encoding="utf-8") as f:
    OFFICIAL = {int(k): v for k, v in json.load(f).items()}

SUBTITLE_ATTR = b'class="subtitle"'
CENT_RE = re.compile(rb'<div class="cent">([^<]*)</div>')
DELIMS = [b"(", "\uff08".encode("utf-8"), b"|", "\uff5c".encode("utf-8")]
SPEC_ROW = re.compile(r"^\s*(\d+)\.\s*第\d+章.*\|.*\|")

failures = []
checks = 0


def report(ok, label, detail=""):
    global checks
    checks += 1
    if ok:
        print("OK       %s" % label)
    else:
        print("MISMATCH %s%s" % (label, (": " + detail) if detail else ""))
        failures.append(label)


def read_bytes(rel):
    with io.open(os.path.join(ROOT, rel), "rb") as f:
        return f.read()


def strip_eol(line):
    return line.rstrip(b"\r\n")


def subtitle_span(line):
    """Return (span_bytes, suffix_bytes) for a subtitle line, else None."""
    line = strip_eol(line)
    attr = line.find(SUBTITLE_ATTR)
    if attr < 0:
        return None
    start = line.find(b">", attr)
    if start < 0:
        return None
    start += 1
    ends = [line.find(d, start) for d in DELIMS]
    ends = [e for e in ends if e >= 0]
    end = min(ends) if ends else len(line)
    return line[start:end], line[end:]


def git_show_bytes(rel):
    r = subprocess.run(["git", "-C", ROOT, "show", "HEAD:" + rel],
                       stdout=subprocess.PIPE)
    if r.returncode != 0:
        return None
    return r.stdout


def head_subtitle_line(data):
    for line in data.split(b"\n"):
        if SUBTITLE_ATTR in line:
            return line
    return None


def check_span(label, span, ch):
    got = span.decode("utf-8").strip()
    report(got == OFFICIAL[ch], label,
           "" if got == OFFICIAL[ch] else "got %r want %r" % (got, OFFICIAL[ch]))


def check_head_suffix(rel):
    cur = head_subtitle_line(read_bytes(rel))
    head = head_subtitle_line(git_show_bytes(rel))
    if cur is None or head is None:
        report(cur is not None and head is not None, rel + " [HEAD-suffix]",
               "subtitle line missing (cur=%s head=%s)" % (cur is not None,
                                                           head is not None))
        return
    cur_span = subtitle_span(cur)
    head_span = subtitle_span(head)
    ok = cur_span is not None and head_span is not None and \
        cur_span[1] == head_span[1]
    report(ok, rel + " [HEAD-suffix]",
           "" if ok else "cur=%r head=%r" % (cur_span and cur_span[1],
                                             head_span and head_span[1]))


def check_subtitle_file(rel, ch):
    lines = read_bytes(rel).split(b"\n")
    subs = [l for l in lines if SUBTITLE_ATTR in l]
    if len(subs) != 1:
        report(False, rel + " [subtitle]", "%d subtitle lines" % len(subs))
        return
    span = subtitle_span(subs[0])
    if span is None:
        report(False, rel + " [subtitle]", "no EN span found")
        return
    check_span(rel + " [subtitle]", span[0], ch)


def main():
    for ch in range(1, 27):
        check_subtitle_file("html/ch%02d.html" % ch, ch)

    for ch in range(1, 27):
        rel = "html_v2/ch%02d.html" % ch
        data = read_bytes(rel)
        check_subtitle_file(rel, ch)
        cents = CENT_RE.findall(data)
        if len(cents) != 1:
            report(False, rel + " [cent]", "%d cent divs" % len(cents))
        else:
            check_span(rel + " [cent]", cents[0], ch)

    spec = io.open(os.path.join(ROOT, "_agent_spec.md"), encoding="utf-8",
                   newline="").read().split("\n")
    seen = set()
    for line in spec:
        m = SPEC_ROW.match(line)
        if not m:
            continue
        ch = int(m.group(1))
        seen.add(ch)
        got = line.rsplit("|", 1)[1].strip()
        report(got == OFFICIAL[ch], "_agent_spec.md row %d" % ch,
               "" if got == OFFICIAL[ch] else
               "got %r want %r" % (got, OFFICIAL[ch]))
    if seen != set(range(1, 27)):
        report(False, "_agent_spec.md [coverage]",
               "rows found: %s" % sorted(seen))

    for ch in range(1, 27):
        check_head_suffix("html/ch%02d.html" % ch)
        check_head_suffix("html_v2/ch%02d.html" % ch)
    check_head_suffix("pdf_demo/ch01_demo.html")

    bad_chs = sorted({int(s) for lab in failures for s in
                      re.findall(r"ch(\d{2})|row (\d+)", lab) for s in [s[0] or s[1]]})
    print("\n%d/%d checks passed" % (checks - len(failures), checks))
    if failures:
        print("failing chapters: %s" % ",".join(str(c) for c in bad_chs))
        sys.exit(1)
    print("ALL TITLE CHECKS PASS")


if __name__ == "__main__":
    main()
