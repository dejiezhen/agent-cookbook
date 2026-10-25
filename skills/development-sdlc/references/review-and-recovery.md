# Review, fixes, and recovery

Read when assembling review evidence, handling findings, or resuming interrupted work.

## Package the exact change

Record the base before implementation and the actual head afterward. Snapshot any
pre-existing edits in affected files, including untracked contents, so the later
patch can distinguish user work from task work. A commit alone does not identify a
dirty working tree. For committed
work, provide the complete base-to-head diff, relevant commit list, and new files.
Do not substitute `HEAD~1` when a task made several commits. One way to capture a
plain diff without configured external diff programs is:

```sh
git diff --no-ext-diff --no-textconv --no-color BASE..HEAD > REVIEW_FILE
```

Replace BASE, HEAD, and REVIEW_FILE with recorded revisions and the review artifact
path using proper quoting for the shell. Read enough surrounding code to answer a
concrete risk. If commits are disallowed, capture the scoped working-tree patch and
new file contents against the recorded baseline. Do not assume HEAD includes edits,
and keep existing user changes distinguishable from the task's work.

Keep briefs, reports, and packages in one plan-specific scratch directory. Pass paths
and essential context to subagents rather than the accumulated conversation. When the
host supports context-free workers, use them. Honor its model-selection rules and
tool capabilities; do not prescribe model names unavailable in that environment.

## Findings and fix budget

Resolve required specification gaps and supported material defects. Clarify disputed
findings against actual requirements and evidence. A design preference or hypothetical
future need does not justify broadening the task. Record accepted tradeoffs and why.

Use a default budget of three focused fix/re-review rounds per task or final integrated
review unless the task's
risk or user constraints justify another budget. Resume the implementer to retain
task context, and use scoped review for each fix. If the same issue recurs, reassess
the cause instead of accumulating patches. At the budget, record the remaining gaps
and a focused next action; do not silently waive a required invariant or claim full
completion. Continue unrelated plan work only when the unresolved task is not needed.
Record findings against the reviewed revision/patch. After a fix, run affected checks
and obtain scoped independent re-review; this also applies to the integrated review.
Reuse the original reviewer when available, or give a fresh reviewer the findings,
intervening changes, and evidence. Approval covers the reviewed state, not later edits.

## Evidence and final state

Each success claim needs corresponding evidence. A compile is not an interaction
test; a mock call is not a committed write; a tool result is not proof of the intended
external outcome. Check meaningful red/green assertions and actual final state.

Keep a compact evidence record in the report or ledger, not a new tracking system:

- Exact command, outcome, and relevant assertions/counts or log path.
- Tested commit plus working-tree patch identity when dirty, including new files.
- Relevant dependency/lockfile and test configuration, runtime/service versions,
  schema/fixture setup, or evaluation dataset/model configuration where applicable.

Record only inputs that can affect the claim; no exhaustive environment inventory or
universal hashing scheme is required. Reuse a result when those inputs still apply.
Code, dependency, test configuration, schema/data setup, environment, or contract
changes invalidate affected evidence even if a particular source file is unchanged.
Rerun the affected check, not automatically every check. An unknown material input is
a gap to resolve or disclose. Honor mandatory project checks regardless of reuse.

Before final handoff, resolve any integration gaps, inspect the whole diff, and run
required project checks whose evidence does not cover the final revision. Report
pre-existing failures and unavailable checks separately. Preserve unresolved findings
as visible limits. Do not claim independent review when no separate reviewer ran.

## Resume safely

Verify the ledger belongs to the current plan and checkout. Inspect its recorded
revisions, reports, and the current Git state. Reuse completed work and resume the
pending task or review. Reconcile a worker that finished without reporting before
redispatching it. A lost conversation is not evidence that code was never written.
Establish whether an earlier writer is active, stopped, or finished before another
writer starts. If its state is unknown, resolve that uncertainty first. Reuse valid
completed implementation/review records and continue from the pending transition;
do not redispatch completed work merely because its conversational context is gone.

Keep working on useful local coordination while children run. When genuinely idle,
use bounded waits appropriate to the host and keep the user informed of meaningful
progress. Do not create duplicate reviewers to fill time. Never reset or clean a
checkout as a recovery shortcut. Retain the ledger and useful evidence through
handoff; remove only task-owned disposable artifacts when safe and authorized.
