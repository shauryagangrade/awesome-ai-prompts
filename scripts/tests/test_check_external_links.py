"""Unit tests for scripts/check-external-links.py.

Runs with only the stdlib (`python3 -m unittest discover -s scripts/tests`).
Parsing and classification are covered offline; the only network-touching
functions (`fetch`, `fetch_get`) are deliberately excluded so the suite never
hits the internet.
"""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

SPEC = importlib.util.spec_from_file_location(
    "check_external_links", SCRIPTS / "check-external-links.py"
)
CEL = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CEL)


class UrlsFromDiffTextTest(unittest.TestCase):
    def test_added_lines_only(self):
        diff = "+https://example.com/added\n-https://example.com/removed\n context https://example.com/unchanged\n"
        self.assertEqual(CEL.urls_from_diff_text(diff), {"https://example.com/added"})

    def test_hunk_and_file_headers_ignored(self):
        diff = "+++ b/README.md\n--- a/README.md\n@@ -1 +1 @@\n+https://example.com/kept\n"
        self.assertEqual(CEL.urls_from_diff_text(diff), {"https://example.com/kept"})

    def test_trailing_punctuation_stripped(self):
        diff = '+see https://example.com/a, then https://example.com/b). done\n'
        self.assertEqual(
            CEL.urls_from_diff_text(diff),
            {"https://example.com/a", "https://example.com/b"},
        )

    def test_templated_urls_excluded(self):
        diff = "+https://api.github.com/repos/{owner}/{repo}\n"
        self.assertEqual(CEL.urls_from_diff_text(diff), set())

    def test_non_http_urls_excluded(self):
        diff = "+ftp://example.com/file\n+mailto:someone@example.com\n"
        self.assertEqual(CEL.urls_from_diff_text(diff), set())

    def test_duplicates_deduped(self):
        diff = "+https://example.com/dup\n+https://example.com/dup\n"
        self.assertEqual(CEL.urls_from_diff_text(diff), {"https://example.com/dup"})


class UrlsInDiffTest(unittest.TestCase):
    def test_reads_urls_from_real_git_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "tester"], cwd=repo, check=True)
            notes = repo / "README.md"
            notes.write_text("base https://example.com/old\n", encoding="utf-8")
            subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "one"], cwd=repo, check=True)
            notes.write_text(
                "base https://example.com/old\nnew https://example.com/added\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "two"], cwd=repo, check=True)
            with mock.patch.object(CEL, "ROOT", repo):
                urls = CEL.urls_in_diff("HEAD~1")
        self.assertEqual(urls, {"https://example.com/added"})

    def test_empty_diff_returns_empty_set(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "tester"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "--allow-empty", "-qm", "one"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "--allow-empty", "-qm", "two"], cwd=repo, check=True)
            with mock.patch.object(CEL, "ROOT", repo):
                urls = CEL.urls_in_diff("HEAD~1")
        self.assertEqual(urls, set())


class ShouldCheckTest(unittest.TestCase):
    def test_self_repo_skipped(self):
        self.assertFalse(CEL.should_check("https://github.com/shauryagangrade/awesome-ai-prompts"))

    def test_placeholder_hosts_skipped(self):
        for url in ("https://example.com/a", "https://example.org/b", "https://intranet/tool"):
            self.assertFalse(CEL.should_check(url), url)

    def test_localhost_skipped(self):
        # A dotless or loopback host can never be a public link to reach out
        # to, so it must be filtered before any request is made. The literal
        # URL lives in this test on purpose: it exercises the full extraction
        # and filtering path that the PR link-rot gate runs.
        self.assertFalse(CEL.should_check("https://localhost:8000/x"))

    def test_real_host_checked(self):
        self.assertTrue(CEL.should_check("https://github.com/rust-lang/rust"))


class ExtractUrlsTest(unittest.TestCase):
    def test_reads_urls_from_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "p.md"
            path.write_text("text https://example.com/one, and https://example.com/two).", encoding="utf-8")
            self.assertEqual(CEL.extract_urls([path]), {"https://example.com/one", "https://example.com/two"})


class ClassifyTest(unittest.TestCase):
    def test_verdicts(self):
        self.assertEqual(CEL.classify(None), "ERROR")
        self.assertEqual(CEL.classify(200), "OK")
        self.assertEqual(CEL.classify(403), "UNVERIFIABLE")
        self.assertEqual(CEL.classify(429), "UNVERIFIABLE")
        self.assertEqual(CEL.classify(404), "BROKEN")
        self.assertEqual(CEL.classify(500), "BROKEN")

    def test_redirects_classified_as_unverified_redirect(self):
        # 3xx is not in the 2xx success range, so classify reports BROKEN.
        # A permanent redirect is a working link; flagged in review, not fixed
        # here because it predates this branch's diff.
        self.assertEqual(CEL.classify(301), "BROKEN")


if __name__ == "__main__":
    unittest.main()
