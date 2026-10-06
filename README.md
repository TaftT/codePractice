# Code Grinder: Coding Interview Practice

A personal practice repo for technical interviews: LeetCode / HackerRank / CodeSignal style problems plus practical engineering exercises, generated, graded, and coached by Claude Code.

Covers JavaScript/TypeScript, React/Next.js/Vue, Node.js backend, Python, SQL, and CS fundamentals. Difficulty ranges from Warmup to Hard and adapts to my results.

## How It Works

Open this repo in Claude Code (it reads [CLAUDE.md](CLAUDE.md) for the rules) and talk naturally:

| Say | Result |
|---|---|
| "Give me a problem" | Next recommended problem based on my history |
| "Give me a SQL / medium TypeScript / frontend problem" | Targeted problem |
| "Give me a hint" | Progressive hint (4 levels, no solution code) |
| "Teach me this" | Coaching mode with unrelated examples |
| "Verify my code" | Runs tests, grades, gives feedback, updates this README, commits |
| "Start an interview" | Timed interviewer mode |
| "What should I practice?" | Weakness analysis from history |
| "Show my progress" | Summary of performance and improvement |
| "Show me the solution" | Approach + reference implementation |

## Workflow

1. Ask for a problem. It appears in `problems/NNN-title/` with a README, starter code, and tests.
2. Write your solution in the provided solution file. Don't ask for hints right away.
3. Ask Claude to verify. You get a rating, feedback, and interview-style follow-up questions.
4. This README updates with the new result.

## Repository Layout

```
CLAUDE.md          Instructions and rules for Claude
README.md          This file: progress history and statistics
problems/
  NNN-title/
    README.md      Problem statement, metadata, results
    solution.*     My solution (starter scaffold at first)
    tests.*        Public tests (grading tests may be kept separately)
```

## Scoring Rubric

| Category | Points |
|---|---|
| Correctness | 40 |
| Code quality / readability | 20 |
| Efficiency | 15 |
| Edge cases / error handling | 10 |
| Language / framework best practices | 10 |
| Interview reasoning / readiness | 5 |

Weights shift for problem types such as frontend or architecture, and hints used are factored in.

---

## Practice History

| # | Problem | Category | Difficulty | Date | Rating |
|---|---------|----------|------------|------|--------|
| 001 | [Log Level Counter](problems/001-log-level-counter/README.md) | Data Processing / Hash Maps | Warmup | 2026-10-06 | Developing (3 revisions) |

Ratings: Needs Work, Developing, Proficient, Strong. Numeric scores are kept privately.

## Statistics

_Calculated from completed problems only. Updated each time a solution is graded._

- **Problems completed:** 1

### Completed by Technology

| Technology | Completed |
|------------|-----------|
| Python | 1 |

### Problems by Difficulty

| Difficulty | Completed |
|------------|-----------|
| Warmup | 1 |
| Easy | 0 |
| Medium | 0 |
| Hard | 0 |

### Strongest Areas
_Not enough data yet._

### Areas Needing Practice
- Exact field matching (set membership) instead of substring checks
- Whitespace-robust parsing (`split()` vs `split(" ")`)
- Python naming conventions (snake_case)

### Concepts Recently Practiced
- Python dict counting, string normalization, `str.split()` parsing (001)
