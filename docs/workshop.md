# Participant runbook — ordinary terminal tabs

## Preflight

Clone the workshop repository:
```sh
git clone https://github.com/noamgot/parallel-ai-worktrees-workshop.git loglab-workshop
cd loglab-workshop
```
Avoid shallow or single-branch clones for fallbacks.

Check `python3 --version` (3.9+), `git --version`, `wt --version`. These commands
target Worktrunk v0.81.0; inspect help if yours differs. Your CLI agent must
already be authenticated: open it and perform its normal status/login check
before class, never paste credentials into a prompt. Verify Git author identity
with `git var GIT_AUTHOR_IDENT`; configure your real identity if needed.

Shell integration permits `wt switch` to change the parent shell directory.
Optional prework: `wt config shell install`, review the shell-file edits, then
restart the shell. This runbook does **not** require it: creation uses `--no-cd`
and every new terminal explicitly changes directory. No hooks or auto-agents.
Herdr TUI/community plugin and uv are not required; no plugin setup in class.

Fetch prepared refs from your clone's origin (local source works too):
```sh
git fetch origin 'refs/heads/solution/*:refs/remotes/origin/solution/*'
git fetch origin tag workshop-start
git show-ref --verify refs/remotes/origin/solution/filter
git show-ref --verify refs/remotes/origin/solution/summary
git show-ref --verify refs/remotes/origin/solution/combined
```

## Timing targets (not yet rehearsed)

0–6 intro; 6–12 worktree model; 12–15 tools; checkpoint 1 15–22;
checkpoint 2 22–37; checkpoint 3 37–43; checkpoint 4 43–49;
49–55 reflection; 55–60 Q&A. These are presentation targets, not measured results.

## 1. Create workspaces (15–22, 7 minutes)

From the original clone, keep this terminal for integration. Commands assume
fresh `learn/*` branch names; if they exist, inspect rather than overwriting.
Paths stay inside the repository's ignored `.worktrees/` directory.
```sh
git switch -c learn/integration workshop-start
python3 -m unittest discover -s tests -v
mkdir -p .worktrees
wt switch --create learn/filter --base workshop-start --path .worktrees/filter --no-cd --no-hooks
wt switch --create learn/summary --base workshop-start --path .worktrees/summary --no-cd --no-hooks
wt list
pwd
```
Open two terminal tabs, `cd` to the printed original path plus
`/.worktrees/filter` in one and `/.worktrees/summary` in the other. In **each**:
```sh
pwd
git branch --show-current
python3 -m unittest discover -s tests -v
```
Done: different directories, branches learn/filter and learn/summary, green
baseline in both. Both branch bases are workshop-start, not each other's work.

## 2. Launch independent tasks (22–37, 15 minutes)

Start your already-authenticated agent in each task terminal. Copy the complete
`tasks/filter.md` prompt into the filter agent; copy `tasks/summary.md` into the
summary agent. Keep permission/review prompts enabled. Verify each agent's
printed branch/path. Don't ask it to integrate or operate on another checkout.
Done: both agents work concurrently in their respective ownership boundaries.
Early finishers inspect the diff or add an owned edge-case test, not new scope.

## 3. Review before integrating (37–43, 6 minutes)

Stop/wait for each agent before review. In filter terminal:
```sh
git status --short
git diff -- loglab/filtering.py
git diff --no-index /dev/null tests/test_filter_task.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s checks -p test_filter.py -v
git add loglab/filtering.py tests/test_filter_task.py
git diff --cached --stat
git diff --cached
git commit -m "Implement exact severity filtering"
```
`git diff --no-index` returns 1 when differences exist; this is expected.
In summary terminal use equivalent review, then:
```sh
git status --short
git diff -- loglab/summary.py
git diff --no-index /dev/null tests/test_summary_task.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s checks -p test_summary.py -v
git add loglab/summary.py tests/test_summary_task.py
git diff --cached --stat
git diff --cached
git commit -m "Implement component counts"
```
Only two owned files per task may change. Read the tests as well as production
code. Reject changes to checks or shared files. Combined checks need both tasks;
don't spend time fixing the other branch. Done: reviewed commits, focused checks
and baseline green, clean task statuses.

## 4. Integrate, validate, clean up (43–49, 6 minutes)

Return to original integration terminal; stop agents/exit their task shells.
We use explicit native Git merges rather than `wt merge` (which may automate
commit/squash/rebase/removal). Worktrunk owns creation/list/removal lifecycle.
```sh
git branch --show-current
git status --short
git merge --no-ff learn/filter -m "Integrate filtering"
git merge --no-ff learn/summary -m "Integrate summary"
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s checks -v
python3 -m loglab data/sample.jsonl --severity ERROR --summary
git merge-base --is-ancestor learn/filter HEAD
git merge-base --is-ancestor learn/summary HEAD
git status --short
git -C .worktrees/filter status --short
git -C .worktrees/summary status --short
```
Require learn/integration, empty statuses, successful ancestor checks and all
tests green. Output must be `api: 1` then `worker: 2`. If anything is dirty or
unintegrated, stop and preserve it. Only then:
```sh
wt remove learn/filter --foreground --no-delete-branch --no-hooks
wt remove learn/summary --foreground --no-delete-branch --no-hooks
wt list
git worktree list
```
Removal blocks until complete and **keeps branches** explicitly. Without
`--no-delete-branch`, Worktrunk may delete integrated branches. No force flags.
Optional later branch cleanup is a separate human decision (`git branch -d`).
Done: green composed behavior, clean integration, only intended worktrees remain.

Trouble? [Preserve-first recovery](presenter.md). If paths already exist, inspect
`git worktree list` and choose unused paths/names, never use clobber or force.
