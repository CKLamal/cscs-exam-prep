# -*- coding: utf-8 -*-
"""Diff html_v2/ against the pre-proofread backup; report per-chapter hunk
counts and structural element counts (svg/table/qa/style) to catch damage.

Run from repo root:  python -X utf8 _scripts/diff_proofread.py [ch03 ch07 ...]
"""
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = ROOT / "html_v2"
OLD = ROOT / "html_v2_backup_pre_proofread"


def counts(text: str) -> dict:
    return {
        "svg": len(re.findall(r"<svg[\s>]", text)),
        "table": len(re.findall(r"<table[\s>]", text)),
        "qa": text.count('class="qa"'),
        "style": len(re.findall(r"<style[\s>]", text)),
        "html_end": text.rstrip().endswith("</html>"),
    }


def main() -> int:
    wanted = set(sys.argv[1:]) or {p.stem for p in NEW.glob("ch*.html")}
    bad = 0
    for ch in sorted(wanted):
        old_p, new_p = OLD / f"{ch}.html", NEW / f"{ch}.html"
        if not old_p.exists() or not new_p.exists():
            print(f"{ch}: MISSING file (old={old_p.exists()} new={new_p.exists()})")
            bad += 1
            continue
        a = old_p.read_text(encoding="utf-8").splitlines()
        b = new_p.read_text(encoding="utf-8").splitlines()
        hunks = sum(
            1 for l in difflib.unified_diff(a, b, n=0) if l.startswith("@@")
        )
        ca, cb = counts("\n".join(a)), counts("\n".join(b))
        drift = [k for k in ("svg", "table", "qa", "style") if ca[k] != cb[k]]
        if not cb["html_end"]:
            drift.append("html_end")
        # style block must be byte-identical
        style_a = re.findall(r"<style.*?</style>", "\n".join(a), re.S)
        style_b = re.findall(r"<style.*?</style>", "\n".join(b), re.S)
        if style_a != style_b:
            drift.append("style_changed")
        flag = "OK " if not drift else "!! "
        if drift:
            bad += 1
        print(f"{flag}{ch}: hunks={hunks} {'+'.join(drift) if drift else ''} "
              f"(svg {ca['svg']}->{cb['svg']}, table {ca['table']}->{cb['table']}, "
              f"qa {ca['qa']}->{cb['qa']})")
    print(f"chapters with issues: {bad}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
