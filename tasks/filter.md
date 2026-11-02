# Log selection

Let callers select logs by multiple severities, multiple components, and a message
substring. Work in `loglab/filtering.py` and optionally `tests/test_filter.py`.
**Scope:** Implement only this task; modify only the files named above.
Reporting is intentionally unfinished; do not implement it or fix its failing
tests. CLI wiring is already provided; do not modify it. Do not search other branches or Git history
for solutions. If changes outside this scope seem necessary, ask first.

Run the task-specific tests below. Once they pass, review your changes and
commit only this task’s changes in the current worktree. Stage only the files
named above. Report changed files, test results, and the commit hash.
Do not merge branches or remove worktrees.

`filter_records(records, severities=None, components=None, message=None)` returns
a new list in input order without modifying records:

- Values within one filter use OR; different filters use AND.
- Severity and component matches are exact and case-sensitive. Message matching
  is a case-sensitive substring search.
- `None` disables a filter; an empty severity/component collection matches nothing.
  An empty message substring matches everything.

For example, severities `ERROR, WARNING`, components `api, worker`, and message
`timeout` select only timeout messages from either component at either severity.

```sh
python3 -m unittest discover -s tests -p 'test_filter*.py' -v
```
