# Agent guidelines

- Python 3.10+; standard library only. Use `unittest`.
- Follow the assigned task in `tasks/`; keep changes within its scope.
- Inputs are already validated. Do not add normalization or input validation.
- You may extend existing tests. Do not remove or weaken existing assertions.
- Leave commits, merges, and worktree management to the user unless requested.
- Report changed files and test results.

Run feature tests with the command in the assigned task. Run the full suite with
`python3 -m unittest discover -s tests -v`; it intentionally fails until both
features and CLI integration are implemented. Additional tests are optional.
