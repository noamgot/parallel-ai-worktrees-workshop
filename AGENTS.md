# Loglab task contract

Python 3.9+; standard library only; use unittest, not pytest. All data is synthetic.
Run commands from your worktree root. Check `pwd`, `git branch --show-current`,
and `git status --short` before editing. Never operate in another task's checkout.

Records are lists of dictionaries. Input validation already guarantees nonempty
string `severity`, `component`, `message`; extra fields are retained. Blank lines
are ignored. Severity is exactly one of DEBUG, INFO, WARNING, ERROR, CRITICAL.
There is no normalization or threshold ordering. Components are case-sensitive,
nonempty strings, without trimming. Task functions receive valid records only;
invalid arguments are outside the contract, and need no new validation.

`filter_records(records, severity=None)` returns a **new list**, retaining input
order and exact severity matches. None includes everything. Empty input or no
matches returns []. Do not mutate the list or dictionaries; shallow reuse is fine.
`summarize_records(records)` returns a fresh dict mapping component to integer
count. Empty input gives {}. Do not mutate input. Mapping insertion order is not
part of the contract; CLI sorts component names lexicographically.

CLI owns parsing, reading, errors, deterministic JSON output, and **filter then
summary** composition. Summary output is `component: count`, one line per key;
empty output prints nothing. Input/unfinished errors exit 2 without a traceback.

Task A owns only `loglab/filtering.py` and `tests/test_filter_task.py`.
Task B owns only `loglab/summary.py` and `tests/test_summary_task.py`.
Do not edit acceptance `checks/`, CLI, shared input, fixture, docs, metadata, or
the other task. Ask for review if changes outside ownership seem necessary.
No dependencies, global configuration, hooks, network operations, agent launching,
merges, worktree removal, or commits unless the human explicitly requests them.
Report files changed and exact test commands/results; human reviews and commits.

Baseline: `python3 -m unittest discover -s tests -v`.
Acceptance: `python3 -m unittest discover -s checks -v` (red at starter by design).
