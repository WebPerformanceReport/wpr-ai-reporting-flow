"""Build the distributed One Pager templates from one_pager/.

Each template in one_pager/ marks where the shared base goes:
  /*@@BASE_CSS@@*/  is replaced by one_pager/base.css
  <!--@@MOTIF@@-->  is replaced by one_pager/motif.svg

The result is one self-contained HTML file per template at the repository root,
which is what users upload to their Project.

Usage:
  python3 tools/build_one_pagers.py          write the templates
  python3 tools/build_one_pagers.py --check  fail if a template is out of date
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "one_pager"
TEMPLATES = {
    "executive.html": "WPR_Executive_One_Pager.html",
    "benchmark.html": "WPR_Benchmark_One_Pager.html",
}


def strip_comments(css):
    """Remove /* comments */ while leaving quoted strings untouched."""
    out, i, quote = [], 0, None
    while i < len(css):
        ch = css[i]
        if quote:
            out.append(ch)
            if ch == "\\" and i + 1 < len(css):
                out.append(css[i + 1])
                i += 1
            elif ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif css.startswith("/*", i):
            end = css.find("*/", i + 2)
            if end == -1:
                raise SystemExit("base.css: unclosed comment")
            i = end + 1
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def compact_css(css):
    """Drop comments and indentation so the distributed file stays small."""
    lines = (line.strip() for line in strip_comments(css).splitlines())
    return "\n".join(line for line in lines if line)


def build(source):
    base = compact_css((SRC / "base.css").read_text(encoding="utf-8"))
    motif = (SRC / "motif.svg").read_text(encoding="utf-8").strip()
    html = (SRC / source).read_text(encoding="utf-8")
    for marker in ("/*@@BASE_CSS@@*/", "<!--@@MOTIF@@-->"):
        if marker not in html:
            raise SystemExit(f"{source}: marker {marker} not found")
    return html.replace("/*@@BASE_CSS@@*/", base).replace("<!--@@MOTIF@@-->", motif)


def main():
    check = "--check" in sys.argv[1:]
    stale = []
    for source, target in TEMPLATES.items():
        html = build(source)
        path = ROOT / target
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != html:
                stale.append(target)
            continue
        path.write_text(html, encoding="utf-8")
        print(f"{target}: {len(html):,} characters")
    if stale:
        raise SystemExit("Out of date, run python3 tools/build_one_pagers.py: " + ", ".join(stale))
    if check:
        print("All One Pager templates are up to date.")


if __name__ == "__main__":
    main()
