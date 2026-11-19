# Reusable prompt: dataset discovery and analysis [spec]

Paste this entire prompt into your agent when you need real datasets, not a
list of suggestions: it searches the literature, downloads the files, and
writes a plain-spoken analysis of each one.

Keywords: datasets, research papers, find data, download, analysis, licensing

---

## Define the scope first

Before searching, confirm:

1. **Requirements** - The task the dataset must support, the modality (text,
   image, tabular, audio, and so on), required fields or labels, minimum size,
   and language or domain constraints.
2. **Search space** - Which venues, fields, and years of research papers to
   mine, and how many papers to scan (the large-corpus target).
3. **Output location** - Where dataset files will be written and how much disk
   space is available. Confirm writes are allowed there.
4. **License limits** - Any license, privacy, or use restriction that would
   disqualify a dataset, and whether credentialed or gated datasets are in
   scope.
5. **Analysis depth** - What each per-dataset analysis must cover, and the
   requested format: a `.md` file per dataset.
6. **Out of scope** - State what will not be done, so "done" is bounded.

Do not begin until the scope is confirmed.

## What to produce

1. **Candidate list** - Every dataset found in the scanned papers, with the
   paper (title, authors, year, link) that mentioned it and a stable dataset
   identifier or URL.
2. **Downloaded files** - The actual dataset files for every candidate that is
   accessible under the license limits, saved under the output location, with
   checksums and a manifest of source URL, version, size, and retrieval date.
3. **Gap report** - For each candidate that could not be downloaded, the exact
   reason (gated, dead link, credentials, license, size) and what is needed to
   get it. No silent omissions.
4. **Per-dataset analysis** - One `.md` file per downloaded dataset, written in
   plain, specific prose following the analysis contract below.
5. **Summary** - A short index linking each analysis file and the dataset
   files, with a one-line verdict per dataset on fitness for the requirements.

## Analysis contract (for each .md file)

- Start with the concrete facts: source paper, version, size, row or record
  count, fields, label distribution, and license.
- Report what you verified by inspecting the files, not what the paper claims.
  Separate "the paper says" from "I checked".
- Give one honest strength and one honest limitation, each tied to a specific
  observation. Name the task it is and is not suited to.
- Include the exact commands used to inspect the data, so a reader can repeat
  the check.
- Ban filler: no throat-clearing, no "it is important to note", no generic
  praise, no restating the prompt, no lists of obvious benefits. Every sentence
  must carry a fact, a number, a verdict, or a limitation.

## Method

1. Scan the papers in the agreed corpus, following citations and references to
   datasets. Record the paper that surfaced each dataset.
2. Deduplicate candidates by dataset identifier and version; do not count the
   same dataset twice under two names.
3. Check each candidate against the requirements and license limits before
   downloading. Skip disqualified ones with a recorded reason.
4. Download the files into the output location, verify checksums, and write the
   manifest. Never claim a file was saved unless it exists on disk.
5. Inspect each downloaded dataset and write its `.md` analysis from what you
   observed, keeping the paper's claims clearly separate from your checks.
6. Assemble the summary index and verify every link and file path resolves.

## Verification

- [ ] Scope, requirements, search space, output location, and license limits
      were confirmed before work began.
- [ ] Every dataset in the candidate list cites the paper that surfaced it.
- [ ] Duplicates were merged by identifier and version.
- [ ] Every download claimed exists on disk, with a valid checksum and a
      manifest entry (source, version, size, retrieval date).
- [ ] Every inaccessible dataset has a recorded reason in the gap report.
- [ ] Each `.md` analysis follows the analysis contract: facts, verified
      observations, one strength, one limitation, inspection commands, no
      filler.
- [ ] Paper claims and your own checks are clearly separated in every analysis.
- [ ] The summary index links only to files that exist.

## Rules

- Never claim a dataset was downloaded when it was not; the file must exist.
- Never analyze a dataset from its paper description alone; inspect the files.
- Never write fluffy, generic analysis; if you have no concrete fact to state,
  say so plainly and move on.
- Never download or use a dataset that violates the stated license or privacy
  limits; record it as disqualified instead.
- Never invent a dataset, URL, checksum, or statistic; cite or omit it.
