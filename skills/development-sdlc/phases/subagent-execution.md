# Coordinate subagent execution

Read after a task plan exists, when delegation is available,
permitted, and useful. Keep small or tightly coupled work inline. One coordinator
owns the spec, dispatch, reviews, fix loops, ledger, and final result. Stage and
standard modules supply instructions within roles rather than another workflow.

Use a suitable checkout/branch, preserving existing work. Create a worktree when
needed rather than resetting a shared checkout. Honor the host's model configuration,
capabilities, and permissions. Choose a realistic task/review budget.

Keep one plan-specific scratch directory with the spec, task briefs, reports, review
packages, and a [progress ledger](../assets/progress-ledger.md). Record the overall
base, pre-existing changes, agent IDs, exact task revisions/patches, checks, and
findings. Reconcile artifacts and Git before dispatching on resumption.

## Each task

1. Save a brief with exact requirements and acceptance IDs, interfaces/dependencies,
   relevant global constraints, likely/permitted files, test commands if known,
   completion checks, and the selected engineering/stack module paths. Pass the
   [TDD stage](implement-tdd.md) and require it for changed executable behavior.
2. Record the task's actual base. Dispatch a fresh implementer using the
   [implementer prompt](../prompts/implementer.md). Supply only needed context and
   usable artifact paths. Use a context-free worker when supported. Run implementation
   workers sequentially; never allow overlapping writes or shared Git mutations.
3. Read the report, inspect actual changes and evidence, and address concrete gaps.
   Package the complete exact change using [review/recovery guidance](../references/review-and-recovery.md).
4. Dispatch a fresh read-only reviewer with the [task-review prompt](../prompts/task-reviewer.md),
   brief, report, full change, selected standards, and [review stage](review-and-verify.md).
   Require separate spec and quality verdicts. Implementer self-review is insufficient.
5. Resume the implementer for supported fixes, then obtain scoped re-review. Record
   findings and evidence in the ledger. Mark complete only when required criteria
   are met; a review budget cannot turn a material defect into success.

After all tasks, dispatch one fresh [integrated reviewer](../prompts/final-reviewer.md)
with the overall spec, ledger, complete base-to-final change, all applicable standards,
and verification evidence. Address integration gaps and verify the final state under
the [review stage](review-and-verify.md). Finish once with the combined outcome and
remaining limits. Preserve useful recovery records through handoff.

Workers and reviewers do not spawn their own coordination pipelines. If delegation
becomes unavailable, reconcile finished work and continue inline when permitted,
disclosing the change in execution mode and any missing independent review.
