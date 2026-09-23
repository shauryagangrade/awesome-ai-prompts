"""Structural tests for scripts/build-all.py's generated page.

CI's `build-all.py --check` only guarantees the committed ALL_PROMPTS.html is
deterministic and in sync with the builder; it cannot see a template change
that produces valid-looking but broken HTML. These tests run the real builder
and assert the structural invariants the page relies on: one collapsed
<details> per prompt, working copy-button ids, lucide icons on every category,
and header links that resolve to the repo.
"""

import importlib.util
import re
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

SPEC = importlib.util.spec_from_file_location("build_all", SCRIPTS / "build-all.py")
BUILD_ALL = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BUILD_ALL)


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

    def test_every_prompt_body_collapsed_by_default(self):
        bodies = re.findall(r'<details class="body">', self.html)
        self.assertEqual(len(bodies), len(re.findall(r'<article class="prompt">', self.html)))
        self.assertNotIn('<details class="body" open>', self.html)

    def test_copy_buttons_target_existing_body_ids(self):
        anchors = re.findall(r'<button class="copy" data-copy="([^"]+)">', self.html)
        self.assertGreater(len(anchors), 0)
        missing = [a for a in anchors if f'id="body-{a}"' not in self.html]
        self.assertEqual(missing, [])

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
        self.assertIn('data-lucide="git-fork"', self.html)

    def test_expand_collapse_controls_present(self):
        self.assertIn('id="expandAll"', self.html)
        self.assertIn('id="collapseAll"', self.html)

    def test_every_category_has_a_known_lucide_icon(self):
        for cat in BUILD_ALL.category_order():
            self.assertIn(f'data-lucide="{BUILD_ALL.category_icon(cat)}"', self.html)
        self.assertNotIn('data-lucide="sparkles"', self.html)

    def test_prompt_cards_are_linked_from_github(self):
        self.assertIn('href="https://github.com/shauryagangrade/awesome-ai-prompts/blob/main/', self.html)


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
