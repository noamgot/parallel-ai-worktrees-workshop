# CLI integration

After merging both features, connect them in `loglab/__main__.py`.
You may extend `tests/test_combined.py`.

**Scope:** Modify only the two files named above. Both feature implementations
must already be merged; do not implement or repair them here. If they are missing
or changes outside this scope seem necessary, stop and ask first. Do not search
other branches or Git history for solutions.

Run the full suite below. Stop when it passes and report your changes.

- Pass repeatable `--severity` and `--component` values and `--message` to selection.
- Without `--summary`, print selected records as JSON lines, preserving input order.
- With `--summary`, report on **selected records only**, respecting `--top N`.
  `--top` requires `--summary`; N must be nonnegative.
- Print one line per ranked component, with severity names sorted alphabetically:
  `api: total=3 ERROR=2 INFO=1`. Empty results print nothing.

Demonstrate combined selection and ranking, not just each feature separately:

```sh
python3 -m loglab data/sample.jsonl --severity ERROR --severity WARNING --summary --top 2
python3 -m unittest discover -s tests -v
```
