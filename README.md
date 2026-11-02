# Loglab

A small CLI for analyzing synthetic JSON-line logs. Requires Python **3.10+**;
no external dependencies.

```sh
python3 -m loglab data/sample.jsonl
python3 -m unittest discover -s tests -v
```

Develop [log selection](tasks/filter.md) and [ranked reports](tasks/summary.md)
in parallel. The CLI wiring is provided: review and merge both features, then
verify they work together.

## Workshop exercise

Follow the [end-to-end exercise guide](WORKSHOP.md) at your own pace:

1. Create two worktrees from the same starter.
2. Run one coding agent per task, then review, test, and commit each result.
3. Merge both features into the original checkout; no CLI wiring task is needed.
4. Run the full tests and combined example, then remove the finished worktrees.

You are done when both features work together, all tests pass, your changes are
committed, and the original checkout is clean with the task worktrees removed.

After merging both features:

```sh
python3 -m loglab data/sample.jsonl --severity ERROR --severity WARNING --summary --top 2
python3 -m unittest discover -s tests -v
```

All tests live in `tests/`. Baseline tests pass from the start; feature and
combined tests start red. The full suite should pass after both features are
implemented and merged. Additional tests are optional.
