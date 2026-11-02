# Task A — ready-to-copy agent prompt

Implement exact severity filtering in this isolated workshop checkout.
First print `pwd`, `git branch --show-current`, `git status --short`; stop if this
is not the intended `learn/filter` checkout or if unexpected edits exist.
Read AGENTS.md and loglab/filtering.py and inspect checks/test_filter.py.
Own ONLY loglab/filtering.py and tests/test_filter_task.py (create the latter).
Implement filter_records(records, severity=None) per AGENTS.md: new list,
same order, exact supported severity equality (not a threshold), None includes
all, empty/no-match gives [], input list/dicts unchanged. Shallow reuse is fine.
Inputs are already validated; don't add normalization or schema changes.
Add unittest tests covering exact matching, empty/no-match, order, new-list
identity and immutability. Do not edit shared acceptance checks or any other file.
Run `python3 -m unittest discover -s tests -v` and
`python3 -m unittest discover -s checks -p test_filter.py -v`.
Task B and combined checks are expected to remain red; don't fix them.
Report scope/diff and commands/results. Do not commit, merge, remove worktrees,
install packages, change global config, or launch other agents. Human reviews.
