# Reusable prompt: secrets scanning response

Copy-paste the block below into any AI coding agent when a secret (API key,
token, password) has been committed to a repository. It runs the response in
the right order: revoke first, assess exposure, clean history safely, then
prevent a repeat.

Keywords: leaked secret, committed api key, secret rotation, git history cleanup, filter-repo, credential exposure, incident response

---

A secret was committed to this repository. The goal: stop the damage first,
find out whether it was used, remove it from history safely, and make sure it
cannot happen again - without writing the secret into any new place.

## Steps

1. **Identify without copying** - Find what leaked and where: the file, the
   commit, the branches and tags that contain it, and whether it reached a
   remote, a fork, a pull request, a CI log, or a published package. Search with
   `git log -S` or `git grep` using a short fragment, not the whole value. Refer
   to the secret by type and its last four characters only; never paste the full
   value into chat, an issue, a commit message, or a log.
2. **Contain first: revoke and rotate** - Revoke or rotate the credential at its
   provider before touching git. Rewriting history does not un-leak it. Create
   the replacement in the secret store, update every place that uses it, and
   confirm the old one is now rejected. If you cannot reach the provider, say so
   and make that the first open item.
3. **Assess exposure** - Note whether the repository is public or private and
   how long the secret was exposed (first commit time to revoke time). List who
   could have cloned or forked it. Check the provider's audit logs for use of
   that credential in that window: unfamiliar IPs, unusual calls, new
   resources, spend spikes. Record "no evidence of use" separately from
   "evidence of use", and treat the secret as compromised either way.
4. **Plan the history cleanup** - Back up first with a mirror clone. Use
   `git filter-repo` (or BFG) on a fresh clone with an explicit replace-text or
   path rule, and list every branch and tag it will change. Show the plan and
   wait for approval before any force-push. Tell collaborators to re-clone, and
   ask the host to purge cached views and pull-request refs that still hold the
   old commits.
5. **Prevent a repeat** - Add a secret scanner as a pre-commit hook and in CI
   (gitleaks, trufflehog, or the host's push protection). Ignore the file
   pattern that leaked, load secrets from the environment or a secret manager,
   and commit an example file with placeholder values only.
6. **Write the incident record** - Keep a short record with no secret in it:
   what leaked (type and last four characters), the exposure window, the
   evidence of use found or not found, each action with its time, and the
   follow-ups with owners.

## Verification

- [ ] The old credential was tested after rotation and is rejected, with the
      output shown and redacted.
- [ ] The new credential works in every place that uses it.
- [ ] The audit-log review is written down with its time window and result,
      even when it found nothing.
- [ ] After the rewrite, a scan of the full history finds no match for the old
      value, and `git log -S` on the fragment returns nothing in a fresh clone.
- [ ] A scanner runs in pre-commit or CI and was shown to block a fake test
      secret.
- [ ] The incident record contains no secret value.

## Rules

- Never treat deleting the file or adding a new commit as removing the secret;
  it stays in history and in every existing clone.
- Never rewrite history, force-push, or delete a branch without a backup and
  explicit approval.
- Never skip revocation because the repository is private or the exposure was
  short; rotate anyway.
- Never paste the full secret into chat, an issue, a commit message, or the
  incident record.
- If you cannot revoke the credential yourself, stop and report that before
  doing anything else.
