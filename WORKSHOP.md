# LogLab: end-to-end exercise

Use two agents to build independent features, then bring them together in one
working app. Work at your own pace.

## 1. Create two worktrees

Use Worktrunk to create filter and summary worktrees from the same current
starter commit. Keep the original checkout for merging and final verification.

## 2. Run both agents

Start one agent in each worktree and give it the matching task:

- **Filter:** [log selection](tasks/filter.md).
- **Summary:** [ranked component reports](tasks/summary.md).

Each agent runs focused tests and commits its task. Review both results and
confirm both commits exist before merging. Tests intentionally start red; the
full suite passes after both features are implemented and merged.

## 3. Merge both features

Merge both task branches into the original checkout. The CLI wiring is already
provided; no additional implementation is needed.

## 4. Test and clean up

Run the full suite and a combined example:

```sh
python3 -m unittest discover -s tests -v
python3 -m loglab data/sample.jsonl --severity ERROR --severity WARNING --summary --top 2
```

Once verification passes, remove the finished task worktrees.

## Done when

- Both features work together.
- All tests pass.
- Changes are committed and the original checkout is clean.
- Task worktrees are removed.
