#!/usr/bin/env python3
"""Build the static catalog site: every prompt on one printable page, plus
per-category and per-prompt pages for search engines.

Category folders come from the tracked `*-prompt.md` files; each file is split
at its `---` divider (the copy-paste prompt block) and rendered as a
self-contained HTML page with a linked mini-TOC, lucide category/prompt icons,
per-prompt copy buttons, prompt bodies collapsed in <details> by default
(expand/collapse all controls included), header links to the repo README,
quick-start, examples and best practices, and print styles.

Every page (main, per-category, per-prompt) additionally carries SEO metadata:
a unique title and meta description, a canonical URL, Open Graph and Twitter
card tags, and a JSON-LD graph. The whole site lives in one folder:
website/index.html (the main catalog), website/category/<cat>.html (one page
per category), website/prompt/<cat>/<slug>.html (one page per prompt),
website/sitemap.xml, website/robots.txt, and website/llms.txt (a Markdown
index of the catalog for LLM readers, per llmstxt.org). vercel.json rewrites
keep the public URLs short: / serves the catalog, /category/<cat>,
/prompt/<cat>/<slug>, /sitemap.xml, /robots.txt, and /llms.txt map onto the
files under website/. Nothing generated lives at the repo root.

Output is deliberately deterministic: category and file order are sorted and no
timestamps or build metadata are embedded, so two runs are byte-identical.
Translated prompts under i18n/ are excluded; they are indexed by their own
per-language README instead.

The generated site is committed to the repo root for static hosting (see
README "Printable one-page catalog"); CI verifies the committed files are in
sync with a deterministic build via `--check`.

Usage:
  python3 scripts/build-all.py             # regenerate the whole site
  python3 scripts/build-all.py --output X  # also write the main page to X
  python3 scripts/build-all.py --check     # verify determinism + committed files up to date
"""

import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Everything the site serves lives in one folder: website/index.html (the main
# catalog), website/category/<cat>.html, website/prompt/<cat>/<slug>.html,
# website/sitemap.xml, and website/robots.txt. vercel.json rewrites keep the
# public URLs short (/category/<cat>, /prompt/<cat>/<slug>, /sitemap.xml).
SITE_DIRNAME = "website"
MAIN_PAGE_NAME = "index.html"
SITE_DIR = ROOT / SITE_DIRNAME
DEFAULT_OUTPUT = SITE_DIR / MAIN_PAGE_NAME
SELF_REPO = "github.com/shauryagangrade/awesome-ai-prompts"
SITE_URL = "https://awesome-ai-prompts.vercel.app"
SITE_OG_IMAGE = f"{SITE_URL}/assets/social-preview.png"
# Page directories inside website/, served as clean URLs by Vercel.
CATEGORY_PAGES = "category"
PROMPT_PAGES = "prompt"
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
    "system-and-exploration": "laptop",
    "system-design": "layers",
    "testing-quality": "flask-conical",
}
FALLBACK_ICON = "sparkles"


def category_icon(cat):
    return CATEGORY_ICONS.get(cat, FALLBACK_ICON)


def clip(text, limit=155):
    """Single-line snippet for meta descriptions, cut at a word boundary."""
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",.;:") + "..."


def meta_block(title, description, canonical, og_type, jsonld):
    """SEO head tags shared by every generated page.

    Each page carries a unique title, meta description, canonical URL,
    Open Graph and Twitter card tags for link previews, and a JSON-LD graph
    for search engines. The JSON-LD is dumped with sorted keys and compact
    separators so output stays byte-deterministic.
    """
    esc = html.escape
    return f"""<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(canonical)}">
<meta property="og:type" content="{esc(og_type)}">
<meta property="og:site_name" content="awesome-ai-prompts">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{SITE_OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{SITE_OG_IMAGE}">
<script type="application/ld+json">{json.dumps(jsonld, sort_keys=True, separators=(",", ":"))}</script>"""


def site_jsonld():
    """JSON-LD for the home page: a WebSite holding a CollectionPage."""
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "name": "awesome-ai-prompts",
                "url": f"{SITE_URL}/",
                "license": "https://spdx.org/licenses/MIT.html",
            },
            {
                "@type": "CollectionPage",
                "name": "awesome-ai-prompts - all AI coding-agent prompts",
                "url": f"{SITE_URL}/",
                "isPartOf": {"@type": "WebSite", "url": f"{SITE_URL}/"},
            },
        ],
    }


COPY_PROMPT_JS = """\
function copyText(el) {
  var text = el.textContent;
  function done() { el.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
  function fallback() {
    var ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } finally { document.body.removeChild(ta); }
    done();
  }
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(done, fallback);
  } else {
    fallback();
  }
}"""

# Compact stylesheet for the per-category and per-prompt pages; same visual
# language as CSS below, scoped down to what a single page needs.
PAGE_CSS = """\
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:#1a1a1a;margin:0;background:#f7f7f5}
.wrap{max-width:760px;margin:0 auto;padding:2rem 1.5rem 4rem}
header.site{border-bottom:2px solid #1a1a1a;padding-bottom:1rem;margin-bottom:1.5rem}
header.site h1{margin:0 0 .25rem;font-size:1.6rem}
header.site p.sub{margin:.25rem 0;color:#555;font-size:.95rem}
header.site nav.links{display:flex;flex-wrap:wrap;gap:.6rem 1.5rem;margin-top:.9rem;font-size:.9rem}
header.site nav.links a{color:#1a1a1a;text-decoration:none;border-bottom:1px dotted #999}
header.site nav.links a:hover{border-bottom-style:solid;color:#2f4f7f}
nav.crumb{font-size:.85rem;color:#777;margin-bottom:1.25rem}
nav.crumb a{color:#777;text-decoration:none;border-bottom:1px dotted #bbb}
nav.crumb a:hover{color:#2f4f7f;border-bottom-style:solid}
h2.page{border-bottom:2px solid #333;padding-bottom:.35rem;font-size:1.35rem;display:flex;align-items:center;gap:.5rem;margin:0 0 1rem}
h2.page svg{width:1.2rem;height:1.2rem;flex:none;color:#2f4f7f}
span.spec{display:inline-block;font-size:.7rem;vertical-align:middle;background:#7fb3df;color:#fff;border-radius:4px;padding:.05rem .45rem;margin-left:.15rem}
article.prompt{background:#fff;border:1px solid #ddd;border-radius:8px;padding:1.25rem 1.5rem;margin-bottom:1.75rem}
article.prompt .head{display:flex;align-items:baseline;justify-content:space-between;gap:1rem}
article.prompt .meta{font-size:.82rem;color:#777;margin:0 0 .75rem}
article.prompt .meta a{color:#777}
.intro p{margin:.4rem 0 .9rem;color:#333}
button.copy{border:1px solid #ddd;background:#fff;padding:.25rem .6rem;border-radius:6px;color:#666;cursor:pointer;font-size:.78rem;flex:none}
button.copy:hover{background:rgba(0,0,0,.05);color:#111}
pre.prompt{white-space:pre-wrap;background:#1e1e1e;color:#e6e6e6;border-radius:6px;padding:1rem;margin:0;overflow-x:auto}
ul.cards{list-style:none;padding:0;margin:0 0 1.5rem}
ul.cards li{margin:.4rem 0}
ul.cards a{display:block;background:#fff;border:1px solid #ddd;border-radius:8px;padding:.7rem 1rem;text-decoration:none;color:#1a1a1a}
ul.cards a:hover{border-color:#2f4f7f}
ul.cards strong{display:block}
ul.cards span{font-size:.85rem;color:#555}
section.siblings{margin-top:2rem}
section.siblings h3{font-size:1rem;text-transform:uppercase;letter-spacing:.04em;color:#555}
section.siblings ul{margin:.25rem 0;padding-left:1.25rem}
section.siblings a{color:#1a1a1a;text-decoration:none;border-bottom:1px dotted #999}
section.siblings a:hover{border-bottom-style:solid}
a.cta{display:inline-block;font-size:.9rem;color:#2f4f7f;text-decoration:none;border-bottom:1px dotted #999}
a.cta:hover{border-bottom-style:solid}
footer.site{margin-top:3rem;padding-top:1rem;border-top:1px solid #ddd;color:#888;font-size:.85rem}
@media print{button.copy{display:none}.wrap{max-width:none;padding:0}pre.prompt{color:#000;background:#fff;border:1px solid #ccc}}
"""


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
a.pagenav{color:#777;text-decoration:none;border-bottom:1px dotted #bbb;font-weight:400}
a.pagenav:hover{color:#2f4f7f;border-bottom-style:solid}
h2 a.pagenav{margin-left:auto;font-size:.75rem}
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

    i18n/ is excluded explicitly. A translated file lives at
    i18n/<lang>/<category>/<slug>-prompt.md, so its first path segment is
    `i18n`, not a category name; taking that segment would invent a fourteenth
    category called "i18n" holding nothing. Skipping it by name keeps the
    catalog an English-language catalog, which is what its title claims.
    """
    out = subprocess.check_output(
        ["git", "ls-files", "--", f"*{PROMPT_SUFFIX}"],
        cwd=ROOT,
        text=True,
    ).split()
    return sorted({rel.split("/", 1)[0] for rel in out if not rel.startswith("i18n/")})


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


def meta_title(title):
    """Title as it should read in search results and meta descriptions.

    The H1 convention prefixes every prompt with "Reusable prompt: ", which
    wastes the front of a result title and a meta description.
    """
    return re.sub(r"^Reusable prompt: ", "", title)


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
<p class="meta"><a href="{src_link}">{html.escape(cat + '/' + path.name)}</a> &middot; <a class="pagenav" href="/{PROMPT_PAGES}/{cat}/{slug_for(path)}">view page</a></p>
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
            f'<span class="count">({len(loaded)})</span>'
            f'<a class="pagenav" href="/{CATEGORY_PAGES}/{cat}">category page</a></h2>\n'
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
        '<a href="https://github.com/shauryagangrade/awesome-ai-prompts"><i data-lucide="star" aria-hidden="true"></i>Star on GitHub</a>',
    ])
    meta_description = (
        f"{total} copy-paste AI coding-agent prompts across {len(cats)} categories "
        "for developers: debugging, code review, testing, security, DevOps, "
        "system design, and more. Verify, don't guess."
    )
    meta = meta_block(
        title="awesome-ai-prompts - all prompts on one page",
        description=meta_description,
        canonical=f"{SITE_URL}/",
        og_type="website",
        jsonld=site_jsonld(),
    )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{meta}
<style>{CSS}</style>
<script>
  window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
</script>
<script defer src="/_vercel/insights/script.js"></script>
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


def page_shell(meta, sub, breadcrumb, content, extra_js=""):
    """Common HTML shell for the per-category and per-prompt pages.

    Same visual language as the main catalog but scoped to one page: a
    breadcrumb instead of the mini-TOC, and no expand/collapse controls.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{meta}
<style>{PAGE_CSS}</style>
<script>
  window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
</script>
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<div class="wrap">
<header class="site">
<h1>awesome-ai-prompts</h1>
<p class="sub">{sub}</p>
<nav class="links">
<a href="{GITHUB_BLOB}README.md">README &amp; docs</a>
<a href="https://{SELF_REPO}">Star on GitHub</a>
</nav>
</header>
<nav class="crumb">{breadcrumb}</nav>
<main>
{content}
</main>
<footer class="site">
<p>Generated by scripts/build-all.py from the prompt files in this repo. Do not edit by hand. Regenerate with: python3 scripts/build-all.py</p>
</footer>
</div>
<script src="{LUCIDE_SRC}"></script>
<script>
{extra_js}
if (window.lucide) {{ lucide.createIcons(); }}
</script>
</body>
</html>
"""


def render_category_page(cat, entries):
    """One page per category: its prompt set as a linked card list.

    entries is the loaded, ordered list of (path, title, intro, body, is_spec)
    tuples for the category.
    """
    specs = [meta_title(clean_title(title, spec)) for _, title, _, _, spec in entries]
    titles = ", ".join(specs[:4]) + ("..." if len(specs) > 4 else "")
    description = clip(
        f"{len(entries)} copy-paste AI coding-agent prompts in the {cat} "
        f"category for developers: {titles}"
    )
    url = f"{SITE_URL}/{CATEGORY_PAGES}/{cat}"
    meta = meta_block(
        title=f"{cat} - {len(entries)} AI coding-agent prompts | awesome-ai-prompts",
        description=description,
        canonical=url,
        og_type="website",
        jsonld={
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "CollectionPage",
                    "name": f"{cat} - AI coding-agent prompts",
                    "url": url,
                    "description": description,
                    "isPartOf": {"@type": "WebSite", "url": f"{SITE_URL}/"},
                    "mainEntity": {
                        "@type": "ItemList",
                        "numberOfItems": len(entries),
                        "itemListElement": [
                            {
                                "@type": "ListItem",
                                "position": position,
                                "url": f"{SITE_URL}/{PROMPT_PAGES}/{cat}/{slug_for(path)}",
                            }
                            for position, (path, _, _, _, _) in enumerate(entries, start=1)
                        ],
                    },
                }
            ],
        },
    )
    cards = "".join(
        f'<li><a href="/{PROMPT_PAGES}/{cat}/{slug_for(path)}">'
        f'<strong><i data-lucide="{category_icon(cat)}" aria-hidden="true"></i> '
        f"{html.escape(clean_title(title, spec))}</strong>"
        f"<span>{html.escape(clip(intro, 90))}</span></a></li>"
        for path, title, intro, _, spec in entries
    )
    content = f"""<h2 class="page"><i data-lucide="{category_icon(cat)}" aria-hidden="true"></i><span>{html.escape(cat)}</span></h2>
<ul class="cards">
{cards}
</ul>
<a class="cta" href="{GITHUB_BLOB}{cat}/">View {html.escape(cat)} on GitHub</a>"""
    return page_shell(
        meta=meta,
        sub=f"{len(entries)} prompts in {cat}. Each page has the full prompt block ready to paste.",
        breadcrumb=f'<a href="/">All prompts</a> &rsaquo; {html.escape(cat)}',
        content=content,
    )


def render_prompt_page(cat, path, title, intro, body, is_spec, entries):
    """One page per prompt: title, intro, and the full copy-paste block.

    entries is the category's loaded list, used for the sibling links that
    keep the subpages interlinked for readers and crawlers alike.
    """
    rel = f"{cat}/{path.name}"
    slug = slug_for(path)
    title = clean_title(title, is_spec)
    search_title = meta_title(title)
    url = f"{SITE_URL}/{PROMPT_PAGES}/{cat}/{slug}"
    description = clip(intro or search_title)
    meta = meta_block(
        title=f"{search_title} | awesome-ai-prompts",
        description=description,
        canonical=url,
        og_type="article",
        jsonld={
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "name": search_title,
                    "url": url,
                    "description": description,
                    "isPartOf": {"@type": "WebSite", "url": f"{SITE_URL}/"},
                    "mainEntity": {
                        "@type": "CreativeWork",
                        "name": search_title,
                        "url": url,
                        "license": "https://spdx.org/licenses/MIT.html",
                    },
                }
            ],
        },
    )
    spec_html = '<span class="spec">spec</span>' if is_spec else ""
    intro_html = ""
    if intro:
        paras = [html.escape(p.strip()) for p in intro.split("\n\n") if p.strip()]
        intro_html = f'<div class="intro">{"".join(f"<p>{p}</p>" for p in paras)}</div>'
    siblings = "".join(
        f'<li><a href="/{PROMPT_PAGES}/{cat}/{slug_for(sibling)}">{html.escape(clean_title(sib_title, spec))}</a></li>'
        for sibling, sib_title, _, _, spec in entries
        if sibling != path
    )
    content = f"""<h2 class="page"><i data-lucide="{category_icon(cat)}" aria-hidden="true"></i><span>{html.escape(title)}</span>{spec_html}</h2>
<article class="prompt">
<div class="head">
<p class="meta"><a href="{GITHUB_BLOB}{rel}">{html.escape(rel)}</a></p>
<button class="copy" type="button">Copy prompt</button>
</div>
{intro_html}
<pre class="prompt" id="prompt-body">{html.escape(body)}</pre>
</article>
<section class="siblings">
<h3>More {html.escape(cat)} prompts</h3>
<ul>{siblings}</ul>
</section>"""
    return page_shell(
        meta=meta,
        sub="One prompt from the awesome-ai-prompts catalog, ready to paste into your AI coding agent.",
        breadcrumb=(
            f'<a href="/">All prompts</a> &rsaquo; '
            f'<a href="/{CATEGORY_PAGES}/{cat}">{html.escape(cat)}</a> &rsaquo; {html.escape(title)}'
        ),
        content=content,
        extra_js=(
            f"document.querySelector('button.copy').addEventListener('click', "
            f"function () {{ copyText(document.getElementById('prompt-body')); }});\n"
            f"{COPY_PROMPT_JS}"
        ),
    )


def sitemap_urls():
    """Every published URL: home, one per category, one per prompt."""
    urls = [f"{SITE_URL}/"]
    for cat in [c for c in category_order() if prompt_files(c)]:
        urls.append(f"{SITE_URL}/{CATEGORY_PAGES}/{cat}")
        urls.extend(
            f"{SITE_URL}/{PROMPT_PAGES}/{cat}/{slug_for(path)}" for path in prompt_files(cat)
        )
    return urls


def render_sitemap(dest_root):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    lines.extend(f"<url><loc>{url}</loc></url>" for url in sitemap_urls())
    lines.append("</urlset>")
    (dest_root / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_robots(dest_root):
    (dest_root / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )


def render_llms_txt(dest_root, spec_rels):
    """llms.txt: a Markdown index of the site for LLM readers.

    Follows the llmstxt.org convention - project name, a blockquote summary,
    then sections of bullet links - so an agent can discover the prompt pages
    and fetch the one it needs instead of wading through the full catalog.
    Categories first, then every prompt with its usage note as the link
    description.
    """
    cats = [c for c in category_order() if prompt_files(c)]
    total = sum(len(prompt_files(cat)) for cat in cats)
    lines = [
        "# awesome-ai-prompts",
        "",
        (
            "> A curated list of copy-paste AI coding-agent prompts for developers: "
            "disciplined workflows that verify, don't guess."
        ),
        "",
        (
            f"{total} prompts across {len(cats)} categories, generated from the prompt files "
            f"in github.com/shauryagangrade/awesome-ai-prompts (MIT licensed). Each prompt "
            "page carries the full prompt block ready to paste into an AI coding agent."
        ),
        "",
        "## Site",
        "",
        (
            f"- [All prompts on one page]({SITE_URL}/): the full catalog with a mini-TOC "
            "and one-click copy buttons"
        ),
        (
            f"- [GitHub repository](https://{SELF_REPO}): source of truth for every prompt, "
            "contributions welcome"
        ),
        "",
        "## Categories",
        "",
    ]
    for cat in cats:
        count = len(prompt_files(cat))
        noun = "prompt" if count == 1 else "prompts"
        lines.append(f"- [{cat}]({SITE_URL}/{CATEGORY_PAGES}/{cat}): {count} {noun}")
    lines += ["", "## Prompts", ""]
    for cat in cats:
        lines.append(f"### {cat}")
        lines.append("")
        for path in prompt_files(cat):
            title, intro, _ = split_prompt(path)
            is_spec = f"{cat}/{path.name}" in spec_rels
            title = meta_title(clean_title(title, is_spec))
            url = f"{SITE_URL}/{PROMPT_PAGES}/{cat}/{slug_for(path)}"
            lines.append(f"- [{title}]({url}): {clip(intro) or 'copy-paste prompt'}")
        lines.append("")
    (dest_root / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_site(dest_root):
    """Write the whole generated site: main catalog, per-category and
    per-prompt pages, sitemap.xml, robots.txt, and llms.txt.

    Subpage paths mirror the clean URLs Vercel serves them under (see the
    rewrites in vercel.json). Returns the number of prompts rendered.
    """
    dest_root = Path(dest_root)
    dest_root.mkdir(parents=True, exist_ok=True)
    total = render_page(dest_root / MAIN_PAGE_NAME)
    spec_rels = spec_prompt_rels()
    for cat in [c for c in category_order() if prompt_files(c)]:
        entries = []
        for path in prompt_files(cat):
            title, intro, body = split_prompt(path)
            entries.append((path, title, intro, body, f"{cat}/{path.name}" in spec_rels))
        page_dir = dest_root / CATEGORY_PAGES
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / f"{cat}.html").write_text(render_category_page(cat, entries), encoding="utf-8")
        prompt_dir = dest_root / PROMPT_PAGES / cat
        prompt_dir.mkdir(parents=True, exist_ok=True)
        for path, title, intro, body, is_spec in entries:
            page = render_prompt_page(cat, path, title, intro, body, is_spec, entries)
            (prompt_dir / f"{slug_for(path)}.html").write_text(page, encoding="utf-8")
    render_sitemap(dest_root)
    render_robots(dest_root)
    render_llms_txt(dest_root, spec_rels)
    return total


def check():
    """Verify the whole generated site is deterministic and in sync.

    Renders the full site twice into temp dirs and requires byte-identical
    output, then compares every generated file against its committed copy and
    flags committed files the build no longer produces (a prompt or category
    that was deleted but whose page was left behind).
    """
    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "one"
        second = Path(tmp) / "two"
        first.mkdir()
        second.mkdir()
        render_site(first)
        render_site(second)
        first_files = {p.relative_to(first) for p in first.rglob("*") if p.is_file()}
        second_files = {p.relative_to(second) for p in second.rglob("*") if p.is_file()}
        if first_files != second_files:
            print("FAIL generated file set differs across runs")
            return 1
        for rel in sorted(first_files):
            if (first / rel).read_bytes() != (second / rel).read_bytes():
                print(f"FAIL build output is not byte-identical across runs: {rel}")
                return 1
        main_page = (first / DEFAULT_OUTPUT.name).read_bytes()
        if main_page.count(b"<article") == 0:
            print("FAIL no prompts found")
            return 1

        problems = []
        fresh = {str(rel) for rel in first_files}
        for rel in sorted(fresh):
            committed = SITE_DIR / rel
            if not committed.exists():
                problems.append(f"missing committed file: {SITE_DIRNAME}/{rel}")
            elif committed.read_bytes() != (first / rel).read_bytes():
                problems.append(f"stale: {SITE_DIRNAME}/{rel}")
        # Committed pages under the generated dirs that the build no longer
        # produces (a prompt or category was deleted or renamed).
        for pattern in (f"{CATEGORY_PAGES}/*.html", f"{PROMPT_PAGES}/*/*.html"):
            for committed in sorted(SITE_DIR.glob(pattern)):
                rel = str(committed.relative_to(SITE_DIR))
                if rel not in fresh:
                    problems.append(f"no longer generated, delete or regenerate: {SITE_DIRNAME}/{rel}")
        if problems:
            for problem in problems:
                print(f"FAIL {problem}")
            print("run: python3 scripts/build-all.py to regenerate, or delete removed pages")
            return 1
    print(
        f"OK ({main_page.count(b'<article')} prompts, "
        f"{len(first_files)} files deterministic and in sync)"
    )
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="extra path for a copy of the main catalog page (default: the site is written at the repo root)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="build the full site twice in a temp dir and verify byte-identical, in-sync output",
    )
    args = parser.parse_args()

    if args.check:
        return check()

    total = render_site(SITE_DIR)
    print(f"Wrote {SITE_DIRNAME}/ ({MAIN_PAGE_NAME}, {CATEGORY_PAGES}/*.html, {PROMPT_PAGES}/*/*.html, sitemap.xml, robots.txt, llms.txt; {total} prompts)")
    if args.output != DEFAULT_OUTPUT:
        render_page(args.output)
        print(f"Wrote an extra copy of the catalog to {args.output} ({total} prompts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
