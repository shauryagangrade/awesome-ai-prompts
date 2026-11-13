"""Structural tests for scripts/build-all.py's generated pages.

CI's `build-all.py --check` only guarantees the committed site under website/ is
deterministic and in sync with the builder; it cannot see a template change
that produces valid-looking but broken HTML. These tests run the real builder
and assert the structural invariants the pages rely on: the catalog links to
every prompt page instead of inlining the bodies, every prompt page carries its
own prompt as the h1, lucide icons on every category, and header links that
resolve to the repo.
"""

import re
import tempfile
import unittest
from pathlib import Path

from _helpers import SCRIPTS, load_module

BUILD_ALL = load_module(SCRIPTS / "build-all.py", "build_all")


def build_html():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "out.html"
        BUILD_ALL.render_page(out)
        return out.read_text(encoding="utf-8")


URL_RE = re.compile(r'href="#([^"]+)"')


class PageStructureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = build_html()

    def test_prompts_rendered(self):
        articles = re.findall(r'<article class="prompt">', self.html)
        self.assertGreater(len(articles), 0)

    def test_prompt_bodies_are_not_inlined(self):
        # The catalog carries titles, intros and links. Inlining every body
        # made index.html a 642 KB duplicate of all 144 prompt pages, which
        # left search engines choosing between the catalog and the page it
        # duplicated. The full block belongs on the prompt page only.
        self.assertEqual(re.findall(r'<pre class="prompt"', self.html), [])
        self.assertEqual(re.findall(r'<details', self.html), [])

    def test_every_prompt_links_to_its_own_page(self):
        linked = re.findall(r'href="(/prompt/[a-z0-9-]+/[a-z0-9-]+)"', self.html)
        expected = {
            f"/prompt/{cat}/{BUILD_ALL.slug_for(path)}"
            for cat in BUILD_ALL.category_order()
            for path in BUILD_ALL.prompt_files(cat)
        }
        self.assertEqual(set(linked), expected)
        self.assertGreater(len(linked), 0)

    def test_toc_anchors_resolve(self):
        hrefs = URL_RE.findall(self.html)
        self.assertGreater(len(hrefs), 0)
        dangling = [h for h in hrefs if f'id="{h}"' not in self.html]
        self.assertEqual(dangling, [])

    def test_header_links_present(self):
        for expected in (
            "github.com/shauryagangrade/awesome-ai-prompts",
            "blob/main/README.md",
            "README.md#quick-start",
            "README.md#usage-in-the-wild",
            "CONTRIBUTING.md#pr-guidelines",
        ):
            self.assertIn(expected, self.html)
        # The repo header link is a star CTA, not a fork action.
        self.assertIn('data-lucide="star"', self.html)
        self.assertIn("Star on GitHub", self.html)
        self.assertNotIn('data-lucide="git-fork"', self.html)

    def test_catalog_has_no_copy_or_expand_controls(self):
        # The bodies live on their own pages now, so the copy buttons and the
        # expand/collapse controls went with them.
        self.assertNotIn('id="expandAll"', self.html)
        self.assertNotIn('id="collapseAll"', self.html)
        self.assertNotIn('class="copy"', self.html)

    def test_every_category_has_a_known_lucide_icon(self):
        for cat in BUILD_ALL.category_order():
            self.assertIn(f'data-lucide="{BUILD_ALL.category_icon(cat)}"', self.html)
        self.assertNotIn('data-lucide="sparkles"', self.html)

    def test_prompt_cards_are_linked_from_github(self):
        self.assertIn('href="https://github.com/shauryagangrade/awesome-ai-prompts/blob/main/', self.html)


class InternalLinkTest(unittest.TestCase):
    """Every internal page-to-page link must be root-relative and extensionless.

    The site is served by vercel.json rewrites (/, /category/:cat,
    /prompt/:cat/:slug) onto the files under website/. A relative href like
    "prompt/x/y.html" resolves against the current page's directory, so on a
    category page it becomes "/category/prompt/x/y.html", which matches no
    rewrite and 404s. This pins every internal link to the exact clean URL shape
    the rewrites serve, independent of how deep the current page sits.
    """

    HREF_RE = re.compile(r'href="([^"]+)"')

    @classmethod
    def setUpClass(cls):
        cls.spec_rels = BUILD_ALL.spec_prompt_rels()
        cls.cat = next(c for c in BUILD_ALL.category_order() if BUILD_ALL.prompt_files(c))
        cls.entries = []
        for path in BUILD_ALL.prompt_files(cls.cat):
            title, intro, body = BUILD_ALL.split_prompt(path)
            spec = f"{cls.cat}/{path.name}" in cls.spec_rels
            cls.entries.append((path, title, intro, body, spec))
        cls.category_html = BUILD_ALL.render_category_page(cls.cat, cls.entries)
        cls.first = cls.entries[0]
        path, title, intro, body, spec = cls.first
        cls.prompt_html = BUILD_ALL.render_prompt_page(
            cls.cat, path, title, intro, body, spec, cls.entries
        )

    @staticmethod
    def _h1(page_html):
        match = re.search(r"<h1>(.*?)</h1>", page_html, re.DOTALL)
        assert match, "page has no h1"
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", match.group(1))).strip()

    def test_prompt_page_h1_is_the_prompt_not_the_site_name(self):
        # Every subpage used to open with <h1>awesome-ai-prompts</h1>, which
        # told a search engine nothing about the page. The h1 is the topic.
        _, title, _, _, spec = self.first
        expected = BUILD_ALL.meta_title(BUILD_ALL.clean_title(title, spec))
        self.assertEqual(self._h1(self.prompt_html), expected)
        self.assertNotEqual(self._h1(self.prompt_html), "awesome-ai-prompts")
        self.assertFalse(self._h1(self.prompt_html).startswith("Reusable prompt:"))

    def test_category_page_h1_names_the_category(self):
        self.assertIn(self.cat, self._h1(self.category_html))
        self.assertNotEqual(self._h1(self.category_html), "awesome-ai-prompts")

    def test_subpages_link_back_to_the_catalog(self):
        for page_html in (self.category_html, self.prompt_html):
            self.assertIn('<a class="brand" href="/">awesome-ai-prompts</a>', page_html)

    def _internal_hrefs(self, page_html):
        # Root-relative ("/...") only; drop in-page anchors and absolute URLs
        # (GitHub, canonical, og:url), which are off-site and resolve on their own.
        return [
            h
            for h in self.HREF_RE.findall(page_html)
            if not h.startswith(("http://", "https://", "#", "mailto:"))
        ]

    def test_category_page_links_are_root_relative_and_extensionless(self):
        hrefs = self._internal_hrefs(self.category_html)
        self.assertGreater(len(hrefs), 0)
        for h in hrefs:
            self.assertTrue(h.startswith("/"), f"relative internal link: {h}")
            self.assertFalse(h.endswith(".html"), f"non-clean internal link: {h}")

    def test_prompt_page_links_are_root_relative_and_extensionless(self):
        hrefs = self._internal_hrefs(self.prompt_html)
        self.assertGreater(len(hrefs), 0)
        for h in hrefs:
            self.assertTrue(h.startswith("/"), f"relative internal link: {h}")
            self.assertFalse(h.endswith(".html"), f"non-clean internal link: {h}")

    def test_links_match_urls_the_rewrites_serve(self):
        # Only /, /category/<cat>, and /prompt/<cat>/<slug> are routed; anything
        # else would 404 even though it looks root-relative.
        served = re.compile(r"^/$|^/category/[a-z0-9-]+$|^/prompt/[a-z0-9-]+/[a-z0-9-]+$")
        for page_html in (self.category_html, self.prompt_html):
            for h in self._internal_hrefs(page_html):
                self.assertRegex(h, served)


class LlmsTxtTest(unittest.TestCase):
    """llms.txt is the LLM-facing index; it must cover the whole catalog."""

    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as tmp:
            BUILD_ALL.render_llms_txt(Path(tmp), BUILD_ALL.spec_prompt_rels())
            cls.text = (Path(tmp) / "llms.txt").read_text(encoding="utf-8")

    def test_header_follows_llmstxt_convention(self):
        self.assertTrue(self.text.startswith("# awesome-ai-prompts\n"))
        self.assertIn("> A curated list", self.text)
        self.assertIn("## Categories", self.text)
        self.assertIn("## Prompts", self.text)

    def test_every_tracked_prompt_linked(self):
        tracked = {
            f"{cat}/{BUILD_ALL.slug_for(path)}"
            for cat in BUILD_ALL.category_order()
            for path in BUILD_ALL.prompt_files(cat)
        }
        self.assertGreater(len(tracked), 0)
        linked = re.findall(
            re.escape(BUILD_ALL.SITE_URL) + r"/prompt/([a-z0-9-]+)/([a-z0-9-]+)\)",
            self.text,
        )
        self.assertEqual({f"{cat}/{slug}" for cat, slug in linked}, tracked)

    def test_every_category_linked(self):
        for cat in BUILD_ALL.category_order():
            self.assertIn(f"]({BUILD_ALL.SITE_URL}/category/{cat}):", self.text)


class SplitPromptTest(unittest.TestCase):
    def test_title_intro_and_body(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x-prompt.md"
            path.write_text(
                "# Reusable prompt: x\n\nSome intro.\n\n---\n\nthe body\nsecond line\n",
                encoding="utf-8",
            )
            title, intro, body = BUILD_ALL.split_prompt(path)
            self.assertEqual(title, "Reusable prompt: x")
            self.assertEqual(intro, "Some intro.")
            self.assertEqual(body, "the body\nsecond line")

    def test_no_divider_means_all_intro(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "y-prompt.md"
            path.write_text("# Reusable prompt: y\n\njust body\n", encoding="utf-8")
            title, intro, body = BUILD_ALL.split_prompt(path)
            self.assertEqual(title, "Reusable prompt: y")
            self.assertEqual(intro, "just body")
            self.assertEqual(body, "")


class CleanTitleTest(unittest.TestCase):
    def test_spec_suffix_stripped_only_when_badged(self):
        self.assertEqual(BUILD_ALL.clean_title("Reusable prompt: x [spec]", True), "Reusable prompt: x")
        self.assertEqual(BUILD_ALL.clean_title("Reusable prompt: x [spec]", False), "Reusable prompt: x [spec]")

    def test_not_badged_title_unchanged(self):
        self.assertEqual(BUILD_ALL.clean_title("Reusable prompt: y", True), "Reusable prompt: y")


class CategoryIconTest(unittest.TestCase):
    def test_known_categories_mapped(self):
        self.assertTrue(BUILD_ALL.category_icon("core-coding"))
        self.assertTrue(BUILD_ALL.category_icon("testing-quality"))

    def test_unknown_category_falls_back(self):
        self.assertEqual(BUILD_ALL.category_icon("brand-new-folder"), BUILD_ALL.FALLBACK_ICON)

    def test_every_tracked_category_is_mapped(self):
        unmapped = [cat for cat in BUILD_ALL.category_order() if BUILD_ALL.category_icon(cat) == BUILD_ALL.FALLBACK_ICON]
        self.assertEqual(unmapped, [])


if __name__ == "__main__":
    unittest.main()
