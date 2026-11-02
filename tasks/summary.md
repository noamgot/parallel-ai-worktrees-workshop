# Task B — ready-to-copy agent prompt

Implement component counts in this isolated workshop checkout.
First print `pwd`, `git branch --show-current`, `git status --short`; stop if this
is not the intended `learn/summary` checkout or if unexpected edits exist.
Read AGENTS.md and loglab/summary.py and inspect checks/test_summary.py.
Own ONLY loglab/summary.py and tests/test_summary_task.py (create the latter).
Implement summarize_records(records) per AGENTS.md: fresh dict mapping each
case-sensitive component string to its integer count; empty input gives {}.
Do not mutate input list/dicts. Insertion order is not a contract; CLI sorts.
Inputs are already validated; don't add normalization or schema changes.
Add unittest tests for repeated components, distinct/case-sensitive names, empty
input and immutability. Do not edit shared acceptance checks or any other file.
Run `python3 -m unittest discover -s tests -v` and
`python3 -m unittest discover -s checks -p test_summary.py -v`.
Task A and combined checks are expected to remain red; don't fix them.
Report scope/diff and commands/results. Do not commit, merge, remove worktrees,
install packages, change global config, or launch other agents. Human reviews.
