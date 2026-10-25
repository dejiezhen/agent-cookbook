---
name: verify-changes
description: Verify a completed code change against acceptance criteria and report execution evidence before claiming success. Use for final implementation checks, regression confirmation, and validating a proposed fix.
---

# Verify the delivered behavior

This skill defines evidence requirements. Within subagent-driven development, the
coordinator owns the verification schedule and final handoff. Reuse valid evidence
for the exact unchanged code; resolve concrete gaps and rerun affected checks after
changes. Do not start another completion pipeline or repeat every task's full suite.
For standalone work, perform the relevant verification directly.

Read the final diff and acceptance criteria. Find the project's actual commands in
its configuration and instructions; do not invent a standard command sequence.
Choose checks according to changed behavior and required project checks.

Map each acceptance criterion to evidence. Run the focused regression or behavior
test, then relevant integration checks and required lint/type/build checks. Use a
real browser for claims involving keyboard behavior, navigation, or rendering that
unit tests cannot establish. Use the supported Postgres version for claims about
database semantics. A successful build alone does not establish behavior.

Keep claims narrow:

| Claim | Evidence that addresses it |
| --- | --- |
| A regression is fixed | Assertion distinguishes pre-fix behavior and passes with the fix |
| A Vue feature works | Relevant interaction checks plus configured template/type checks |
| A write succeeded | Authoritative committed state, not only a mocked adapter call |
| An agent completed a task | Required final state and no forbidden effects, not just its final message |

Inspect results, test counts, exit codes, warnings, skipped cases, and the actual
environment. Distinguish a failing assertion from a missing service. A passing test
with its essential dependency mocked out supports only the narrower claim.

Review for unintended file changes, generated clutter, ignored error paths, and
new dependencies without a reason. Recheck a previously verified area only when a
later change, failure, or unresolved risk invalidates its evidence.

Finish with behavior delivered, checks actually run and results, and material gaps.
State when a check could not run and why. Do not claim clean CI, a successful
migration, a deployment, or a test-first red without observing it. Preserve known
pre-existing failures as separate evidence instead of quietly fixing unrelated work.
