#!/usr/bin/env python3
"""Build ALL_PROMPTS.html: every prompt on one printable, copyable page.

Category folders come from the tracked `*-prompt.md` files; each file is split
at its `---` divider (the copy-paste prompt block) and rendered as a
self-contained HTML page with a linked mini-TOC, lucide category/prompt icons,
per-prompt copy buttons, prompt bodies collapsed in <details> by default
(expand/collapse all controls included), header links to the repo README,
quick-start, examples and best practices, and print styles. Output is
deliberately deterministic: category and file order are sorted and no
timestamps or build metadata are embedded, so two runs are byte-identical.

The generated page is committed to the repo root for static hosting (see
README "Printable one-page catalog"); CI verifies the committed file is in
sync with a deterministic build via `--check`.

Usage:
  python3 scripts/build-all.py             # regenerate ALL_PROMPTS.html
  python3 scripts/build-all.py --output X  # write to a custom path
  python3 scripts/build-all.py --check     # verify determinism + committed file up to date
"""

import argparse
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "ALL_PROMPTS.html"
SELF_REPO = "github.com/shauryagangrade/awesome-ai-prompts"
DIVIDER = "---"

LUCIDE_SRC = "https://unpkg.com/lucide@latest"
CATEGORY_ICONS = {
    "a-a-p-contributing": "users",
    "career-learning": "graduation-cap",
    "code-review": "eye",
    "core-coding": "code-2",
    "data-ai": "database",
    "devops-deploy": "server",
    "docs-delivery": "file-text",
    "frontend-ui": "palette",
    "git-github": "git-branch",
    "mobile-dev": "smartphone",
    "security-performance": "shield",
    "system-design": "layers",
    "testing-quality": "flask-conical",
}
FALLBACK_ICON = "sparkles"


def category_icon(cat):
    return CATEGORY_ICONS.get(cat, FALLBACK_ICON)


CSS = """\
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:#1a1a1a;margin:0;background:#f7f7f5}
.wrap{max-width:960px;margin:0 auto;padding:2rem 1.5rem 4rem}
header.site{border-bottom:2px solid #1a1a1a;padding-bottom:1rem;margin-bottom:2rem}
header.site h1{margin:0 0 .25rem;font-size:1.9rem}
header.site p.sub{margin:.25rem 0;color:#555}
header.site .links{display:flex;flex-wrap:wrap;gap:.6rem 1.5rem;margin-top:.9rem;font-size:.9rem}
header.site .links a{display:inline-flex;align-items:center;gap:.35rem;color:#1a1a1a;text-decoration:none;border-bottom:1px dotted #999}
header.site .links a:hover{border-bottom-style:solid;color:#2f4f7f}
header.site .links svg{width:1.05em;height:1.05em;flex:none}
nav.toc{background:#fff;border:1px solid #ddd;border-radius:8px;padding:1rem 1.5rem;margin-bottom:2.5rem}
nav.toc h2{margin:0 0 .5rem;font-size:1.05rem;text-transform:uppercase;letter-spacing:.04em;color:#555}
nav.toc .controls{display:flex;gap:.5rem;margin:0 0 .9rem}
nav.toc .controls button{border:1px solid #ddd;background:#fff;border-radius:6px;padding:.3rem .65rem;font-size:.8rem;color:#555;cursor:pointer}
nav.toc .controls button:hover{background:rgba(0,0,0,.05);color:#111}
nav.toc ol,.toc ul{margin:.25rem 0}.toc ul{margin-left:1.25rem}
nav.toc li{margin:.15rem 0}
nav.toc a{color:#1a1a1a;text-decoration:none;border-bottom:1px dotted #999}
nav.toc a:hover{border-bottom-style:solid}
nav.toc .count{color:#888;font-size:.85em}
nav.toc li>a{display:inline-flex;align-items:center;gap:.35rem}
nav.toc li>a svg{width:.95em;height:.95em;flex:none;color:#4a6fa5}
section.cat{margin-bottom:3rem}
section.cat h2{border-bottom:2px solid #333;padding-bottom:.35rem;font-size:1.35rem;display:flex;align-items:center;gap:.5rem}
section.cat h2 svg{width:1.2rem;height:1.2rem;flex:none;color:#2f4f7f}
section.cat h2 .count{font-size:.8rem;color:#888;font-weight:400;margin-left:.15rem}
article.prompt{background:#fff;border:1px solid #ddd;border-radius:8px;padding:1.25rem 1.5rem;margin-bottom:1.75rem}
article.prompt h3{margin:0 0 .5rem;font-size:1.15rem;display:flex;align-items:center;gap:.45rem}
article.prompt h3 svg{width:1.05em;height:1.05em;flex:none;color:#4a6fa5}
article.prompt .head{display:flex;align-items:baseline;justify-content:space-between;gap:1rem}
button.copy{border:1px solid #ddd;background:#fff;padding:.25rem .6rem;border-radius:6px;color:#666;cursor:pointer;font-size:.78rem;flex:none}
button.copy:hover{background:rgba(0,0,0,.05);color:#111}
article.prompt .meta{font-size:.82rem;color:#777;margin-bottom:.75rem}
article.prompt .meta a{color:#777}
article.prompt .intro p{margin:.4rem 0 .9rem;color:#333}
details.body{margin-top:.25rem}
details.body summary{cursor:pointer;user-select:none;color:#666;font-size:.82rem;margin:.1rem 0}
details.body summary:hover{color:#111}
details.body[open] summary{margin-bottom:.6rem}
details.body summary::after{content:"▸";color:#999;margin-left:.4rem}
details.body[open] summary::after{content:"▾"}
pre.prompt{white-space:pre-wrap;background:#1e1e1e;color:#e6e6e6;border-radius:6px;padding:1rem;margin:0;overflow-x:auto}
span.spec{display:inline-block;font-size:.7rem;vertical-align:middle;background:#7fb3df;color:#fff;border-radius:4px;padding:.05rem .45rem;margin-left:.15rem}
footer.site{margin-top:3rem;padding-top:1rem;border-top:1px solid #ddd;color:#888;font-size:.85rem}
@media print{button.copy,.controls,nav.toc,header.site p.sub,header.site .links{display:none}.wrap{max-width:none;padding:0}article.prompt{border:none;padding:.5rem 0}section.cat{page-break-before:always}pre.prompt{color:#000;background:#fff;border:1px solid #ccc}}
"""

PROMPT_SUFFIX = "-prompt.md"
GITHUB_BLOB = f"https://{SELF_REPO}/blob/main/"
SPEC_BADGE = 'src="docs/media/spec-badge.svg"'
PROMPT_LINK = re.compile(r"\(([a-z0-9-]+/[a-z0-9-]+-prompt\.md)\)")


def category_order():
    """Category folders, sorted by name, from the tracked prompt files.

    Deriving from `git ls-files` means a local-only, gitignored folder can
    never change the build, so every machine reproduces the committed output.
    Sorting matches the README Contents order, and adding or renaming a
    category only touches the folder and the README.
    """
    out = subprocess.check_output(
        ["git", "ls-files", "--", f"*{PROMPT_SUFFIX}"],
        cwd=ROOT,
        text=True,
    ).split()
    return sorted({rel.split("/", 1)[0] for rel in out})


def spec_prompt_rels():
    """Which prompt files carry the [spec] badge, read from README.md.

    The README listing line for a spec prompt contains the badge image next to
    its link. Deriving the set from README keeps it in sync with the
    authoritative SPEC_PROMPTS list instead of duplicating it here.
    """
    rels = set()
    for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines():
        if SPEC_BADGE in line:
            match = PROMPT_LINK.search(line)
            if match:
                rels.add(match.group(1))
    return rels


def prompt_files(category):
    return sorted(ROOT.glob(f"{category}/*{PROMPT_SUFFIX}"))


def split_prompt(path):
    """Return (title, intro, body) from a prompt file.

    Title is the H1, intro the prose between the title and the first `---`
    divider, body everything after it. Files without a divider are treated as
    all intro (gates reject them, but the builder should not crash either way).
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    title = lines[0][2:].strip() if lines and lines[0].startswith("# ") else path.stem
    rest = lines[1:]
    body_lines = []
    intro_lines = []
    in_body = False
    for line in rest:
        if line == DIVIDER:
            in_body = True
            continue
        (body_lines if in_body else intro_lines).append(line)
    intro = "\n".join(intro_lines).strip()
    body = "\n".join(body_lines).strip()
    return title, intro, body


def slug_for(path):
    return path.name[: -len(PROMPT_SUFFIX)]


def clean_title(title, is_spec):
    """Strip a trailing [spec] marker when the prompt actually carries the badge."""
    if is_spec and title.endswith("[spec]"):
        return title[: -len("[spec]")].rstrip()
    return title


def render_prompt(path, title, intro, body, spec_rels, icon):
    cat = path.parent.name
    rel = f"{cat}/{path.name}"
    anchor = f"{cat}-{slug_for(path)}"
    is_spec = rel in spec_rels
    title = clean_title(title, is_spec)
    src_link = f'{GITHUB_BLOB}{cat}/{path.name}'
    intro_html = ""
    if intro:
        paras = [html.escape(p.strip()) for p in intro.split("\n\n") if p.strip()]
        intro_html = f'<div class="intro">{"".join(f"<p>{p}</p>" for p in paras)}</div>'
    spec_html = '<span class="spec">spec</span>' if is_spec else ""
    icon_html = f'<i data-lucide="{icon}" aria-hidden="true"></i>'
    return f"""<article class="prompt">
<div class="head">
<h3 id="{anchor}">{icon_html}<span>{html.escape(title)}</span>{spec_html}</h3>
<button class="copy" data-copy="{anchor}">Copy prompt</button>
</div>
<p class="meta"><a href="{src_link}">{html.escape(cat + '/' + path.name)}</a></p>
{intro_html}
<details class="body"><summary>Show prompt</summary>
<pre class="prompt" id="body-{anchor}">{html.escape(body)}</pre>
</details>
</article>"""


def render_page(output_path):
    cats = [cat for cat in category_order() if prompt_files(cat)]
    total = sum(len(prompt_files(cat)) for cat in cats)
    spec_rels = spec_prompt_rels()

    toc_lists = []
    sections = []
    for cat in cats:
        loaded = []
        for path in prompt_files(cat):
            title, intro, body = split_prompt(path)
            spec = f"{cat}/{path.name}" in spec_rels
            loaded.append((path, title, intro, body, spec))
        toc_inner = "".join(
            f'<li><a href="#{cat}-{slug_for(path)}">{html.escape(clean_title(title, spec))}</a></li>'
            for path, title, _, _, spec in loaded
        )
        toc_lists.append(
            f'<li><a href="#{cat}"><i data-lucide="{category_icon(cat)}" aria-hidden="true"></i>'
            f'{html.escape(cat)}</a> <span class="count">({len(loaded)})</span>'
            f"<ul>{toc_inner}</ul></li>"
        )
        cat_html = [
            render_prompt(path, title, intro, body, spec_rels, category_icon(cat))
            for path, title, intro, body, _ in loaded
        ]
        sections.append(
            f'<section class="cat">\n<h2 id="{cat}"><i data-lucide="{category_icon(cat)}" '
            f'aria-hidden="true"></i><span>{html.escape(cat)}</span>'
            f'<span class="count">({len(loaded)})</span></h2>\n'
            + "\n".join(cat_html)
            + "\n</section>"
        )

    toc_html = '<ul>' + "".join(toc_lists) + "</ul>"
    sections_html = "\n".join(sections)
    category_note = f"{total} prompts across {len(cats)} categories"
    header_links = "\n".join([
        f'<a href="{GITHUB_BLOB}README.md"><i data-lucide="book-open" aria-hidden="true"></i>README &amp; docs</a>',
        f'<a href="{GITHUB_BLOB}README.md#quick-start"><i data-lucide="terminal" aria-hidden="true"></i>How to use</a>',
        f'<a href="{GITHUB_BLOB}README.md#usage-in-the-wild"><i data-lucide="globe" aria-hidden="true"></i>Examples in the wild</a>',
        f'<a href="{GITHUB_BLOB}CONTRIBUTING.md#pr-guidelines"><i data-lucide="circle-check" aria-hidden="true"></i>Best practices</a>',
        '<a href="https://github.com/shauryagangrade/awesome-ai-prompts"><i data-lucide="git-fork" aria-hidden="true"></i>GitHub</a>',
    ])

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>awesome-ai-prompts - all prompts on one page</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="site">
<h1>awesome-ai-prompts</h1>
<p class="sub">{category_note}. Prompt bodies are collapsed by default: expand a card to read it, or Copy to grab the whole block.</p>
<nav class="links">
{header_links}
</nav>
</header>
<nav class="toc">
<h2>Jump to</h2>
<div class="controls">
<button id="expandAll" type="button">Expand all</button>
<button id="collapseAll" type="button">Collapse all</button>
</div>
{toc_html}
</nav>
{sections_html}
<footer class="site">
<p>Generated by scripts/build-all.py from the prompt files in this repo. Do not edit by hand. Regenerate with: python3 scripts/build-all.py</p>
</footer>
</div>
<script src="{LUCIDE_SRC}"></script>
<script>
function copyPrompt(id) {{
  var el = document.getElementById('body-' + id);
  var text = el.textContent;
  function done() {{ el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }}); }}
  function fallback() {{
    var ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try {{ document.execCommand('copy'); }} finally {{ document.body.removeChild(ta); }}
    done();
  }}
  if (navigator.clipboard && window.isSecureContext) {{
    navigator.clipboard.writeText(text).then(done, fallback);
  }} else {{
    fallback();
  }}
}}
function toggleAll(open) {{
  document.querySelectorAll('details.body').forEach(function (d) {{ d.open = open; }});
}}
document.querySelectorAll('button.copy').forEach(function (b) {{
  b.addEventListener('click', function () {{ copyPrompt(b.getAttribute('data-copy')); }});
}});
document.getElementById('expandAll').addEventListener('click', function () {{ toggleAll(true); }});
document.getElementById('collapseAll').addEventListener('click', function () {{ toggleAll(false); }});
window.addEventListener('beforeprint', function () {{ toggleAll(true); }});
if (window.lucide) {{ lucide.createIcons(); }}
</script>
</body>
</html>
"""
    output_path.write_text(page, encoding="utf-8")
    return total


def check():
    generated = None
    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "one.html"
        second = Path(tmp) / "two.html"
        render_page(first)
        render_page(second)
        if first.read_bytes() != second.read_bytes():
            print("FAIL build output is not byte-identical across runs")
            return 1
        generated = first.read_bytes()

    if generated.count(b"<article") == 0:
        print("FAIL no prompts found")
        return 1
    if DEFAULT_OUTPUT.exists() and DEFAULT_OUTPUT.read_bytes() != generated:
        print(
            "FAIL committed ALL_PROMPTS.html is stale; "
            "run: python3 scripts/build-all.py"
        )
        return 1
    print(f"OK ({generated.count(b'<article')} prompts, deterministic and in sync)")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="output HTML path (default: ALL_PROMPTS.html at the repo root)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="build twice in a temp dir and verify byte-identical output",
    )
    args = parser.parse_args()

    if args.check:
        return check()

    total = render_page(args.output)
    print(f"Wrote {args.output} ({total} prompts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
