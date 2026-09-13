# Reusable prompt: release automation

Copy-paste the block below into any AI coding agent to automate versioning,
tagging, changelog generation, and publishing - a reliable release pipeline,
not a manual checklist.

---

Automate the release process for this repository. The goal: a CI-driven
pipeline that versions, tags, changelogs, and publishes releases
consistently, with no manual steps that can be forgotten.

## Steps

1. **Understand the current process** - Read the existing release-related
   files: CHANGELOG.md, package.json version fields, any existing CI
   workflows, Makefile targets, and publish scripts. Understand how releases
   happen today (manual, semi-automated, or not at all).
2. **Choose a versioning strategy** - Based on the project type, pick the
   right approach:
   - **Semantic Versioning (SemVer)** - for libraries and packages with a
     public API (MAJOR.MINOR.PATCH)
   - **CalVer** - for applications with date-based releases
   - **Keep a Changelog** format for the CHANGELOG
     Document the chosen strategy in the README or CONTRIBUTING.
3. **Set up version bumping** - Configure a tool to automate version bumps:
   `semantic-release`, `release-please`, `changesets`, `bump2version`, or
   a custom script. The tool should: read conventional commits to determine
   the version bump type, update version fields in all relevant files, and
   generate or update the CHANGELOG.
4. **Automate tagging and GitHub releases** - When a version is bumped:
   create a git tag, push it, and create a GitHub release with release notes
   auto-generated from commits since the last tag. Use the repo's CI
   platform (GitHub Actions).
5. **Automate publishing** - If the project publishes to a registry (npm,
   PyPI, crates.io, etc.), add a publish step to the release workflow that
   triggers after tagging. Use secrets for credentials, never hardcode them.
6. **Verify** - Create a test release (on a fork or pre-release tag) to
   confirm the full pipeline: version bump, changelog, tag, GitHub release,
   and publish all work end-to-end.

## Rules

- Never hardcode version numbers in the release workflow - the tool must
  calculate them from commits or config.
- Never skip the changelog step - users and contributors rely on it.
- Never publish to a public registry without a tag and release notes.
- If the project has multiple publish targets (e.g. npm + Docker), all must
  be part of the same release workflow.
