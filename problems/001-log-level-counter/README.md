# 001 - Log Level Counter

**Problem #:** 001
**Category:** Data Processing / Hash Maps
**Technology:** Python
**Difficulty:** Warmup
**Suggested Time:** 15 minutes
**Status:** Completed
**Date Started:** 2026-10-06
**Date Completed:** 2026-10-06
**Rating:** Developing (3 revisions; first attempt: Needs Work)

## Scenario
Your team's service writes plain-text logs. Before building a dashboard, you've been asked to write a small helper that summarizes how many log lines exist at each severity level. Logs are messy: some lines are blank or malformed, and level casing isn't always consistent.

## Problem
Implement `count_log_levels(lines)` which takes a list of log line strings and returns a dictionary mapping each log level to the number of lines with that level.

Each valid line looks like:

```
2026-10-06 12:00:01 ERROR Database connection failed
```

That is: `<date> <time> <LEVEL> <message...>`, separated by single spaces. The message may contain spaces and may even be absent.

## Requirements
1. Valid levels are `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
2. Level matching is case-insensitive (`error`, `Error`, `ERROR` all count as `ERROR`). Keys in the result are always uppercase.
3. Only levels that actually appear are included in the result (no zero-count keys).
4. Lines that are blank, have fewer than 3 whitespace-separated parts, or have an unrecognized level are ignored.
5. Surrounding whitespace on a line should not affect parsing.
6. Do not modify the input list.

## Examples
```python
count_log_levels([
    "2026-10-06 12:00:01 INFO Server started",
    "2026-10-06 12:00:05 error Database connection failed",
    "2026-10-06 12:01:00 INFO Request received",
])
# {"INFO": 2, "ERROR": 1}

count_log_levels(["", "garbage", "2026-10-06 12:00:00 VERBOSE hi"])
# {}

count_log_levels([])
# {}
```

## Constraints
- `0 <= len(lines) <= 10^6`
- Each line is a string of at most 1000 characters
- Use only the Python standard library
- Python 3.10+

## Starter Code
See [solution.py](solution.py).

## What Is Being Evaluated
- Correctness
- Handling of messy input and edge cases
- Readability and idiomatic Python
- Choice of data structures
- Efficiency at scale

## Hints
_Unused. Ask for one if you need it._

**Hints used:** 0

## My Results

## Revision 3 (second refactor): Developing

Hints used: 0. Rated after seeing feedback on earlier attempts, so not a clean first attempt; the root README uses this latest rating.

**What changed:** replaced the per-line loop over all levels with an exact check of the level field (`upperStatus not in statuses`). `INFORMATION` and `ERRORS` are no longer miscounted, and each line is checked once instead of up to 5 times. All 6 public tests pass.

**Still open**
- `split(" ")` instead of `split()`: `"  2026-10-06 12:00:00 info x  "` and `"2026-10-06  12:00:00  ERROR x"` still return `{}` (requirement 5).
- `statuses` is a list; a `set` (or frozenset) gives O(1) membership and signals intent.
- The counting block can be `counts[level] = counts.get(level, 0) + 1` (or `defaultdict(int)` / `Counter`).
- Both earlier versions are now kept as commented-out code at the top of the file; delete them (git keeps history), since this repo is a public showcase.
- snake_case naming (`split_log`, `level`), trailing whitespace at end of file.
- No sample-run block, so `python solution.py` prints nothing.

**Progress noted:** each revision fixed a real class of bug (substring matching, then crashes on short lines, then substring-in-field matching).

---

## Revision 2 (refactor after feedback): Developing

Hints used: 0.

**What changed:** replaced the whole-line substring search with `split(" ")`, a length guard, and a check on the third field. This fixed double-counting and the `VERBOSE ... information` false positive, and malformed lines like `"garbage ERROR"` are now ignored. All 6 public tests pass. Along the way the refactor briefly introduced an `IndexError` (no length guard) and then a `NameError` (typo `slitLog`), both caught by running the tests and fixed.

**Still open**
- `split(" ")` instead of `split()`: lines with leading/trailing/double spaces (e.g. `"  2026-10-06 12:00:00 info x  "`, `"2026-10-06  12:00:00  ERROR x"`) are dropped, violating requirement 5.
- `status in upperStatus` is still a substring check on the field: `INFORMATION` counts as `INFO`, `ERRORS` as `ERROR`. Compare the whole field to the valid levels instead (set membership).
- Style: `splitLog` / `upperStatus` should be snake_case; commented-out old code at the top should be deleted (git keeps history); trailing whitespace; the `if status not in counts` block can use `counts.get` / `defaultdict`.
- No sample-run block (rule added after this problem was created).

**Progress noted:** you went from unguarded substring matching to field-based parsing and used the tests to find your own regressions.

---

## Revision 1 (first attempt): Needs Work

Hints used: 0.

**What I did well**
- Passed all 6 public tests; basic counting, case-insensitivity, empty input and not mutating the input all work.
- Uppercase keys and omitting zero-count levels were handled correctly.
- Used a dict to accumulate counts, which is the right data structure.

**What could be improved**
- The solution searches for the level *anywhere in the line* (`status in upperLog`) instead of parsing the line and checking the level field.
  - `"2026-10-06 12:00:00 INFO error in module"` returns `{INFO: 1, ERROR: 1}` (one line counted twice).
  - `"2026-10-06 12:00:00 VERBOSE information only"` returns `{INFO: 1}` (invalid level accepted via substring).
  - `"garbage ERROR"` is counted, although it has fewer than 3 parts.
- Requirement 4 (ignore malformed lines / unrecognized levels) is effectively not implemented.
- Scans each line up to 5 times; a single parse per line is cleaner and faster.
- Style: `upperLog` should be `upper_log` (PEP 8); `counts` has no type annotation; trailing whitespace at end of file; nested `if status not in counts` can be `counts.get(...)` or `defaultdict(int)`.
- No sample run block at the bottom (this requirement was added after the problem was created).

**Gap classification**
- Misunderstood concept / major reasoning problem: parsing structured text by field vs. substring search.
- Minor: naming convention, redundant membership checks.
- Clearly understand: dicts for counting, case normalization, not mutating input.

**Concepts to review**: `str.split()` and field positions, `maxsplit`, set membership for valid values, `dict.get` / `defaultdict` / `collections.Counter`, writing tests for requirements that your own code might violate.

**Recommended follow-up**: another Python text-parsing problem where messages contain words that look like keywords (forces field-based parsing), e.g. a request-log or CSV-ish line summarizer.

## How to Run Tests
```
pip install pytest
pytest problems/001-log-level-counter
```
