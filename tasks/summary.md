# Ranked component reports

Build a report of log volume and severity breakdown by component. Work in
`loglab/summary.py` and optionally `tests/test_summary.py`. Leave CLI integration
for later.

**Scope:** Implement only this task; modify only the files named above.
Selection and CLI integration are intentionally unfinished; do not implement
them or fix their failing tests. Do not search other branches or Git history
for solutions. If changes outside this scope seem necessary, ask first.

Run the task-specific tests below. Stop when they pass and report your changes.

`summarize_records(records, top_n=None)` returns a list of reports:

```python
{"component": "api", "total": 3, "severities": {"ERROR": 2, "INFO": 1}}
```

- Include only observed components and severities; do not modify input records.
- Rank by total descending, breaking ties by component name ascending
  (case-sensitive).
- `top_n=None` returns all components; a nonnegative integer limits the results.
  Zero or empty input returns `[]`.

For example, equal-volume `api` and `worker` components put `api` first;
`top_n=1` returns only its report.

```sh
python3 -m unittest discover -s tests -p 'test_summary*.py' -v
```
