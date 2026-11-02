# Loglab: parallel agents with Git worktrees

Small synthetic-log CLI for a 60-minute workshop. Python **3.9+**, Git,
Worktrunk (commands checked against **v0.81.0**), and an already-authenticated
CLI agent. No runtime dependencies, services, real company data, or upstream
write access required. Python runtime verification locally used 3.12.12;
3.9 runtime and Linux/SSH rehearsal remain pending.

Clone the workshop repository:
```sh
git clone https://github.com/noamgot/parallel-ai-worktrees-workshop.git loglab-workshop
cd loglab-workshop
```

```sh
git switch -c learn/integration workshop-start
python3 -m loglab --help
python3 -m loglab data/sample.jsonl
python3 -m unittest discover -s tests -v
```

Starter `main` and tag `workshop-start` deliberately leave two extension points
unfinished. Filtering without a severity works; requesting a severity or summary
exits 2 with a clear workshop message until implemented. Baseline passes;
acceptance is intentionally red, not skipped or mixed into baseline discovery:

```sh
python3 -m unittest discover -s checks -p test_filter.py -v
python3 -m unittest discover -s checks -p test_summary.py -v
python3 -m unittest discover -s checks -p test_combined.py -v
python3 -m unittest discover -s checks -v
```

Finished demo:
```sh
python3 -m loglab data/sample.jsonl --severity ERROR --summary
```
```text
api: 1
worker: 2
```
Unfiltered summary is api: 2, cache: 1, worker: 3, proving filtering matters.

Four checkpoints: **create workspaces → launch bounded tasks → review/commit →
integrate/validate/clean up**. Follow [participant runbook](docs/workshop.md).
[Presenter guide and recovery](docs/presenter.md) includes prepared independent
`solution/filter`, `solution/summary`, and merged `solution/combined` refs.
Contracts: [AGENTS.md](AGENTS.md). Prompts: [A](tasks/filter.md), [B](tasks/summary.md).
