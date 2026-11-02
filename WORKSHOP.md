# LogLab: end-to-end exercise

Use two agents to build independent features, then bring them together in one
working app. Work at your own pace.

## 1. Create two worktrees

Use Worktrunk to create filter and summary worktrees from the same current
starter commit. Keep the original checkout for integration.

## 2. Run both agents

Start one agent in each worktree and give it the matching task:

- **Filter:** [log selection](tasks/filter.md).
- **Summary:** [ranked component reports](tasks/summary.md).

Review each result, run its focused tests, and commit it. Tests intentionally
start red; the full suite passes only after both features and integration.

## 3. Merge and connect

Merge both task branches into the original checkout. Then complete
[CLI integration](tasks/integrate.md), yourself or with an agent.

## 4. Test and clean up

Run the full suite and a combined example:

```sh
python3 -m unittest discover -s tests -v
python3 -m loglab data/sample.jsonl --severity ERROR --severity WARNING --summary --top 2
```

Review and commit the integration, then remove the finished task worktrees.

## Done when

- Both features work together.
- All tests pass.
- Changes are committed and the original checkout is clean.
- Task worktrees are removed.
