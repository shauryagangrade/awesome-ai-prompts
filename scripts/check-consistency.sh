#!/usr/bin/env bash
# Consistency lint for awesome-ai-prompts.
# Verifies that:
#   1. every *-prompt.md in a category folder is linked from README.md
#   2. prompt files added on this branch have a CHANGELOG.md [Unreleased] entry
#      (needs git history; set BASE_REF, defaults to origin/main)
#   3. category folders and README sections stay in sync (both directions)
#   4. README Contents counts and per-section prompt links match the files
set -uo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo" || exit 1

BASE_REF="${BASE_REF:-origin/main}"
fail=0

CATEGORIES="career-learning code-review core-coding data-ai devops-deploy docs-delivery frontend-ui git-github security-performance system-design testing-quality"

# Folder -> "README heading|Contents anchor".
meta_for() {
  case "$1" in
    career-learning)      echo "Career & learning|career--learning" ;;
    code-review)          echo "Code review & quality|code-review--quality" ;;
    core-coding)          echo "Core coding|core-coding" ;;
    data-ai)              echo "Data & AI|data--ai" ;;
    devops-deploy)        echo "DevOps & deploy|devops--deploy" ;;
    docs-delivery)        echo "Docs & delivery|docs--delivery" ;;
    frontend-ui)          echo "Frontend & UI|frontend--ui" ;;
    git-github)           echo "Git & GitHub|git--github" ;;
    security-performance) echo "Security & performance|security--performance" ;;
    system-design)        echo "System design|system-design" ;;
    testing-quality)      echo "Testing & quality|testing--quality" ;;
    *)                    return 1 ;;
  esac
}

heading_of() { printf '%s' "${1%%|*}"; }
anchor_of() { printf '%s' "${1##*|}"; }

file_count() { find "$1" -maxdepth 1 -name '*-prompt.md' | wc -l | tr -d ' '; }

total_count() { find . -mindepth 2 -name '*-prompt.md' -not -path './.git/*' | wc -l | tr -d ' '; }

# 1. Every prompt file in a category folder is linked from README.
while IFS= read -r f; do
  rel="${f#./}"
  if ! grep -qF "($rel)" README.md; then
    echo "FAIL unlisted prompt (not linked in README): $rel"
    fail=1
  fi
done < <(find . -mindepth 2 -name '*-prompt.md' -not -path './.git/*' | sort)

# 2. Prompt files added on this branch appear in CHANGELOG [Unreleased].
if git rev-parse --verify --quiet "$BASE_REF" >/dev/null; then
  unreleased="$(awk '/^## \[Unreleased\]/{flag=1; next} /^## \[/{flag=0} flag' CHANGELOG.md)"
  while IFS= read -r rel; do
    [[ -n "$rel" ]] || continue
    if ! grep -qF "$(basename "$rel")" <<<"$unreleased"; then
      echo "FAIL newly added prompt missing from CHANGELOG [Unreleased]: $rel"
      fail=1
    fi
  done < <(git diff --name-only --diff-filter=A "${BASE_REF}...HEAD" -- '*-prompt.md')
else
  echo "SKIP changelog check: $BASE_REF not found (full clone required)"
fi

# 3. Category folders and README sections exist in both directions.
for d in */; do
  d="${d%/}"
  case "$d" in scripts | docs) continue ;; esac
  if git check-ignore -q -- "$d/"; then
    # Skip local-only, gitignored directories (e.g. design assets).
    continue
  fi
  if ! meta_for "$d" >/dev/null; then
    echo "FAIL category folder without README section: $d/"
    fail=1
  fi
done
for d in $CATEGORIES; do
  meta="$(meta_for "$d")"
  if [[ -z "$meta" ]]; then
    echo "FAIL unknown category in CATEGORIES list: $d"
    fail=1
    continue
  fi
  if [[ ! -d "$d" ]]; then
    echo "FAIL README section '$(heading_of "$meta")' has no matching folder: $d/"
    fail=1
    continue
  fi
  if ! grep -qF "## $(heading_of "$meta")" README.md; then
    echo "FAIL missing README section for folder $d/: ## $(heading_of "$meta")"
    fail=1
  fi
done

# 4. Contents counts and section link counts match the files on disk.
for d in $CATEGORIES; do
  meta="$(meta_for "$d")"
  [[ -n "$meta" ]] || continue
  [[ -d "$d" ]] || continue
  heading="$(heading_of "$meta")"
  anchor="$(anchor_of "$meta")"
  count="$(file_count "$d")"

  expected="- [$heading](#$anchor) ($count)"
  if ! grep -qxF -- "$expected" README.md; then
    echo "FAIL stale Contents entry for $d/ - expected line: $expected"
    fail=1
  fi

  section_text="$(awk -v h="## $heading" '$0 == h {flag = 1; next} /^## /{flag = 0} flag' README.md)"
  links="$(grep -oE "\]\($d/[a-z0-9-]+-prompt\.md\)" <<<"$section_text" | wc -l | tr -d ' ')"
  if [[ "$links" != "$count" ]]; then
    echo "FAIL section '$heading' lists $links prompt(s) but $d/ contains $count"
    fail=1
  fi
done

if [[ "$fail" -ne 0 ]]; then
  echo "check-consistency.sh: FAILED"
  exit 1
fi
echo "check-consistency.sh: OK ($(total_count) prompts, all listed, counted, and changelogged)"
