#!/usr/bin/env bash
# Prettier lint for awesome-ai-prompts.
# Verifies tracked+untracked files (markdown, JSON/JSONC, YAML, CSS) match
# Prettier formatting, using the repo-wide .prettierrc.json and .prettierignore.
set -uo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo" || exit 1

PRETTIER="npx --yes prettier@3.5.3"

files=""
count=0
while IFS= read -r f; do
  case "$f" in
    *.md | *.markdown | *.json | *.jsonc | *.yaml | *.yml | *.css)
      files="$files $f"
      count=$((count + 1))
      ;;
  esac
done < <(git ls-files --cached --others --exclude-standard)

if [ "$count" -eq 0 ]; then
  echo "No Prettier-managed files found"
  exit 1
fi

# shellcheck disable=SC2086
if ! $PRETTIER --check $files; then
  echo ""
  echo "check-prettier.sh: FAILED"
  echo "Formatting differs from Prettier. Run: npx --yes prettier@3.5.3 --write <files>"
  exit 1
fi

echo "check-prettier.sh: OK ($count files match Prettier style)"
