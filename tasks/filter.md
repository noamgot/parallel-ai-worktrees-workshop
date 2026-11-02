# Log selection

Let callers select logs by multiple severities, multiple components, and a message
substring. Work in `loglab/filtering.py` and optionally `tests/test_filter.py`.
**Scope:** Implement only this task; modify only the files named above.
Reporting and CLI integration are intentionally unfinished; do not implement
them or fix their failing tests. Do not search other branches or Git history
for solutions. If changes outside this scope seem necessary, ask first.

Run the task-specific tests below. Stop when they pass and report your changes.

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
