---
name: subagent-driven-development
description: Execute a multi-task implementation plan with a fresh implementer per task, independent specification and quality review, and a final integrated review. Use when tasks have clear boundaries and subagents are available; keep small or tightly coupled changes inline.
license: MIT
---

# Subagent-driven development

Adapted from Superpowers; see [provenance and changes](UPSTREAM.md) and the bundled
[MIT license](LICENSE). This folder includes all required prompts and templates;
it does not require other Superpowers skills or scripts.

## One coordinator

Own the plan, task dispatch, review loops, progress, and final result here. Use
engineering, language, TDD, and review skills as task-specific standards when
available; do not start a second coordination or review pipeline for each skill.

Read the specification, plan, project instructions, and current Git state. If the
user requested implementation without a plan, write a short acceptance-criteria
map and task list first. For substantial planning, use the
[plan template](assets/implementation-plan.md). Resolve routine reversible choices
from evidence; ask only for material missing decisions or required authorization.

Use a suitable isolated checkout or branch, preserving existing work. Create a
worktree when needed rather than resetting a shared checkout. Set a realistic task
and review budget. Honor the host's configured model and selection policy.

## Durable progress

Create a plan-specific working directory in the project's scratch area. Use the
[ledger template](assets/progress-ledger.md). Record plan identity, checkout, base
revision, task state, agent IDs, commits or patch identities, checks, and findings.
On resumption, reconcile the ledger with Git and artifacts before dispatching;
completed work must not be repeated because conversational context was lost.

## Execute each task

1. Save a brief containing the task's exact requirements, relevant spec constraints,
   interfaces, permitted files, and completion checks. Require **spec → red → green
   → refactor** for executable behavior changes. Preserve existing code; prose edits
   do not need invented tests.
2. Record the task's base revision. Dispatch a fresh implementer using the
   [implementer prompt](prompts/implementer.md), with only the needed context and
   artifact paths. Never run overlapping implementation workers concurrently.
3. Read its report. Supply missing context or resume it for a concrete gap. Verify
   actual changes and check evidence; a success message alone is insufficient.
4. Package the exact change and dispatch a fresh read-only reviewer using the
   [task-review prompt](prompts/task-reviewer.md). Require separate specification
   and quality verdicts. Implementer self-review does not replace this review.
5. Resolve supported findings with the implementer, then review the fix. Use
   [review and recovery rules](references/review-and-recovery.md) for evidence,
   review scope, fix budgets, and interruptions. Mark complete only when required
   criteria are met. Record unresolved gaps honestly and continue independent work
   when useful; never turn an unmet requirement into success by relabeling it.

## Finish once

After the tasks, dispatch one [integrated reviewer](prompts/final-reviewer.md)
against the overall spec and full change. Address integration gaps and run required
checks on the final state when earlier evidence does not cover it. Report behavior,
verification, significant decisions, and remaining gaps. Preserve useful recovery
records. Publishing, merging, and cleanup follow existing user authorization.

If subagents are unavailable or the user chose inline execution, follow the same
spec, TDD, and verification standards directly and disclose the execution mode.
Do not simulate independent review or install a delegation framework as a fallback.
