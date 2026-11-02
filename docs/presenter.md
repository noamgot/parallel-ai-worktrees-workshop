# Presenter guide

## Timing and preflight

Targets, not yet rehearsed: 0–6 intro; 6–12 worktree model (shared objects vs
isolated working trees, interfaces and scope); 12–15 tools; 15–22 checkpoint 1
(7 min); 22–37 checkpoint 2 (15 min, agent latency buffer); 37–43 checkpoint 3
(6 min); 43–49 checkpoint 4 (6 min); 49–55 reflection; 55–60 Q&A.
Cut agent waiting short and use prepared refs if needed; never skip review.
Rehearse timing with actual agents before claiming the hour is validated.

Before class: confirm Python/Git/Worktrunk, agent authentication and real Git
identity; validate final clone access and fetched refs. Commands were checked
against wt 0.81.0. Shell integration is optional with explicit cd; if installed
in prework, restart terminals before class. No required global config or hooks.
Herdr **TUI** and community plugin are optional only: compatibility, picker
dependencies and actual create/open action are **not validated** here; omit from
the live path unless separately rehearsed. The native Herdr app is different.

Starter main equals workshop-start. Each independent solution changes only its
module and task-test file. Combined merges both independent branches. Never
advance shared starter main during a demo: use learn/integration or recovery/*.

## Preserve-first fallback (original integration terminal)

Stop agents; do not overwrite or remove unfinished worktrees. Inspect `wt list`
and `git status --short`. If dirty, leave files there (or deliberately commit
reviewed WIP in that task); no reset, force checkout, clobber or force removal.
Prepared refs in a clone are remote-tracking refs, not automatically local names:
```sh
git fetch origin 'refs/heads/solution/*:refs/remotes/origin/solution/*'
git show-ref --verify refs/remotes/origin/solution/filter
git show-ref --verify refs/remotes/origin/solution/summary
git show-ref --verify refs/remotes/origin/solution/combined
wt switch --create recovery/integration --base workshop-start --path .worktrees/recovery --no-cd --no-hooks
cd .worktrees/recovery
git merge --no-ff origin/solution/filter -m "Recover filtering"
git merge --no-ff origin/solution/summary -m "Recover summary"
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s checks -v
python3 -m loglab data/sample.jsonl --severity ERROR --summary
```
For a ready-combined checkout instead, from the original root:
```sh
wt switch --create recovery/combined --base origin/solution/combined --path .worktrees/combined --no-cd --no-hooks
```
Open it in another tab; run all tests and canonical CLI there. In the unpublished
source repo itself, there is no origin: use solution/filter, solution/summary,
solution/combined instead. Don't invent a remote to paper over that distinction.
Recovery leaves learner work untouched. Use fresh names if recovery names exist.

## Troubleshooting / native Git reference

- Unfinished workshop error or red acceptance on starter: intentional. Baseline
  should pass. After only A, summary remains unfinished; after only B, filtering
  with a severity remains unfinished.
- Out-of-scope edits: review and ask agent to narrow its work; preserve rejected
  edits before undoing anything. Never change acceptance to conceal failures.
- Unexpected merge conflict: `git status`, preserve work; `git merge --abort`
  only for a newly started merge from a clean tree. Use separate recovery above.
- CLI result api: 2/cache: 1/worker: 3 with ERROR requested: filter/composition
  bug; combined checks catch this. Correct filtered result is api: 1/worker: 2.
- Missing refs: fetch explicit solution refspec above; no upstream write access
  needed. A remote branch isn't a local solution branch.
- Native equivalents for explanation/recovery: `git worktree list`,
  `git worktree add -b recovery/native .worktrees/native workshop-start`,
  and (only after clean/integrated checks) `git worktree remove PATH`.
  Git worktree removal retains branches. Never remove dirty work forcibly.
- Re-run rehearsal in a fresh clone rather than resetting an active learner's
  branch. Cleanup finished recovery worktrees only after preserving commits.

## Final demonstration

Show branch/path isolation and two reviewed two-file diffs; merge sequentially;
run baseline and all acceptance; show canonical ERROR summary and contrast
unfiltered summary; verify ancestors and clean status; remove only integrated
clean task worktrees with explicit branch retention. Discuss semantic contracts
versus textual conflicts and why isolated files alone are insufficient.

## Validation still owned by workshop owner

Owner verified on macOS with Python 3.12 and Worktrunk 0.81.0: fresh local-clone
baseline 6 passed, combined 12+4 passed, Worktrunk creation and fallback recovery
merges worked while preserving a dirty learner file. Owner then integrated both
tasks, verified ancestry/clean summary status, and exercised foreground removal
with branch retention: summary directory absent, branch retained, dirty filter
worktree/learner-wip.txt preserved. Cleanup safety is verified on that platform.
Full timed workshop rehearsal, actual two-agent prompt trial, Python 3.9 runtime and
Linux/SSH execution remain pending. Remote clone/ref verification after push is
also pending. See IMPLEMENTATION.md and publication.md for current evidence.
