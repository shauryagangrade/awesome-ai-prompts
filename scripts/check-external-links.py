#!/usr/bin/env python3
"""Check external URLs referenced in the repo for rot.

Reads README.md and every *-prompt.md, extracts http(s) URLs, and reports any
that no longer resolve or return an error status. Runs on a weekly schedule
(see .github/workflows/url-rot-check.yml) so a dead badge or a referenced tool
surfaces without slowing every PR. Internal relative links are out of scope
(check-links.sh owns those) and self-repo URLs are skipped so unauthenticated
GitHub requests can not flake the job.

Exit code is 1 if any URL is broken, so the scheduled workflow fails loudly.

Usage:
  python3 scripts/check-external-links.py            # full check
  python3 scripts/check-external-links.py --max 20   # cap requests (debug)
  python3 scripts/check-external-links.py --diff HEAD~1  # only URLS on added (+) lines of the diff
"""

import argparse
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF_REPO = "github.com/shauryagangrade/awesome-ai-prompts"
URL_RE = re.compile(r"https?://[^\s)<>'\"]+")
USER_AGENT = "Mozilla/5.0 (compatible; awesome-ai-prompts-url-rot/1.0)"
TIMEOUT = 15
PLACEHOLDER_HOSTS = {
    "example.com",
    "example.org",
    "example.net",
    "example.test",
}

CA_BUNDLES = (
    "/etc/ssl/cert.pem",
    "/etc/ssl/certs/ca-certificates.crt",
    "/etc/pki/tls/certs/ca-bundle.crt",
)


def ssl_context():
    context = ssl.create_default_context()
    for bundle in CA_BUNDLES:
        if os.path.exists(bundle):
            context.load_verify_locations(cafile=bundle)
            break
    return context


def collect_files():
    files = [ROOT / "README.md"]
    files.extend(sorted(ROOT.glob("**/*-prompt.md")))
    return files


def urls_from_text(text):
    """Return the normalized URLs found in a text blob.

    Trailing punctuation is stripped and URLs containing template braces (e.g.
    {owner}/{repo}) are skipped, so both prompt files and diff lines can feed
    this without pre-cleaning.
    """
    urls = set()
    for raw in URL_RE.findall(text):
        url = raw.rstrip(".,;:)]}'\"").strip()
        if url.startswith(("http://", "https://")) and "{" not in url:
            urls.add(url)
    return urls


def extract_urls(files):
    urls = set()
    for path in files:
        urls |= urls_from_text(path.read_text(encoding="utf-8"))
    return urls


def urls_in_diff_text(diff_text):
    """Return URLs found on added (+) lines of a unified diff.

    Only URLs a PR actually introduces are considered: context, removed, and
    hunk-header lines are ignored.
    """
    urls = set()
    for raw_line in diff_text.splitlines():
        if not raw_line.startswith("+") or raw_line.startswith("+++"):
            continue
        urls |= urls_from_text(raw_line[1:])
    return urls


def urls_in_git_diff(diff_range):
    """Return URLs found only on added (+) lines of `git diff diff_range`.

    Used for PR-time checking (see ci.yml ext-links job):  only URLs a PR
    actually introduces are contacted, so a rot check runs on every PR
    without re-hitting the whole repo's link set the way the weekly full
    check does.
    """
    proc = subprocess.run(
        ["git", "diff", "-U0", diff_range],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    return urls_in_diff_text(proc.stdout)


def should_check(url):
    if SELF_REPO in url:
        return False
    match = re.search(r"https?://([^/:]+)", url)
    if not match:
        return False
    host = match.group(1)
    has_domain = "." in host
    return has_domain and host != "localhost" and host not in PLACEHOLDER_HOSTS


def fetch(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl_context()) as resp:
            return resp.getcode()
    except urllib.error.HTTPError as error:
        code = error.code
        if code in (405, 501):
            return fetch_get(url)
        return code
    except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError):
        return None


def fetch_get(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl_context()) as resp:
            return resp.getcode()
    except urllib.error.HTTPError as error:
        return error.code
    except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError):
        return None


def classify(code):
    if code is None:
        return "ERROR"
    if 200 <= code < 300:
        return "OK"
    if code in (403, 429):
        return "UNVERIFIABLE"
    return "BROKEN"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max", type=int, default=0, help="stop after N requests")
    parser.add_argument(
        "--diff",
        metavar="RANGE",
        default=None,
        help="check only URLs on added lines of `git diff RANGE` (e.g. main...HEAD)",
    )
    args = parser.parse_args()

    if args.diff:
        new_urls = sorted(u for u in urls_in_git_diff(args.diff) if should_check(u))
        if not new_urls:
            print(f"No external URLs added in `git diff {args.diff}`")
            return 0
        print(f"Checking {len(new_urls)} URL(s) added in `git diff {args.diff}`")
        urls = new_urls
    else:
        files = collect_files()
        urls = sorted(u for u in extract_urls(files) if should_check(u))
        if args.max:
            urls = urls[: args.max]

    all_count = len(urls)
    broken = []

    for index, url in enumerate(urls, 1):
        code = fetch(url)
        if code is None:
            time.sleep(3)
            code = fetch(url)
        verdict = classify(code)
        mark = {"OK": ".", "BROKEN": "X", "ERROR": "E", "UNVERIFIABLE": "?"}[verdict]
        print(f"[{mark}] {url} ({'status ' + str(code) if isinstance(code, int) else 'network error'})", flush=True)
        if verdict in ("BROKEN", "ERROR"):
            broken.append(url)
        if index % 25 == 0:
            print(f"... {index}/{all_count}", file=sys.stderr)

    print(f"\n{all_count - len(broken)} of {all_count} links healthy")
    if broken:
        print("Broken or unreachable links:")
        for url in broken:
            print(f"  - {url}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
