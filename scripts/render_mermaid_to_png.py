#!/usr/bin/env python3
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "book"
OUTPUT_DIR = ROOT / "assets" / "diagrams"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MERMAID_BLOCKS = [
    re.compile(r"```\{mermaid\}([\s\S]*?)```", re.MULTILINE),
    re.compile(r"```mermaid\s*\n([\s\S]*?)\n```", re.MULTILINE),
    re.compile(r":::\{mermaid\}\s*\n([\s\S]*?)\n:::", re.MULTILINE),
]


def render_mermaid(code: str, out_path: Path):
    temp = out_path.with_suffix(".mmd")
    temp.write_text(code.strip() + "\n")
    cmd = ["mmdc", "-i", str(temp), "-o", str(out_path)]
    subprocess.run(cmd, check=True)
    temp.unlink()


for md_path in sorted(BOOK_DIR.rglob("*.md")):
    text = md_path.read_text(encoding="utf-8")
    matches = []
    for blk in MERMAID_BLOCKS:
        matches.extend(list(blk.finditer(text)))
    if not matches:
        continue
    matches.sort(key=lambda m: m.start())

    rel_md = md_path.relative_to(ROOT)
    base_name = "_".join(rel_md.with_suffix("").parts)
    out_rel_dir = Path("assets") / "diagrams"
    rel_prefix = Path("..").joinpath(
        *([".."] * (len(md_path.parents) - len(ROOT.parents) - 1))
    )
    # Actually, simpler: compute relative path from md file to OUTPUT_DIR
    rel_prefix = Path(os.path.relpath(OUTPUT_DIR, md_path.parent))

    new_text = []
    last_end = 0
    counter = 0

    for m in matches:
        counter += 1
        start, end = m.span()
        code = m.group(1)
        out_file = OUTPUT_DIR / f"{base_name}_mermaid_{counter}.png"
        render_mermaid(code, out_file)

        img_rel = rel_prefix / out_file.name
        replacement = f"![Diagrama Mermaid]({img_rel.as_posix()})\n"

        new_text.append(text[last_end:start])
        new_text.append(replacement)
        last_end = end

    new_text.append(text[last_end:])
    md_path.write_text("".join(new_text), encoding="utf-8")
    print(f"Rendered {len(matches)} diagram(s) for {md_path} -> {out_file}")
