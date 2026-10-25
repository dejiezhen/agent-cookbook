# Red, green, refactor

Start from the acceptance criteria, applicable standards, actual runner, and baseline.
For new executable behavior and regression fixes:

1. Select one observable behavior. Write the smallest test that exposes its absence
   through a meaningful assertion at the real owning boundary. Prefer public behavior
   over private structure; reproduce the reported symptom for a regression.
2. Run it. Inspect the failure and establish why it concerns the missing behavior.
   Import errors, broken fixtures, and unavailable services do not establish that red.
3. Implement the minimum coherent behavior. Keep required validation, authorization,
   and integrity. Do not mock away the behavior under test to reach green.
4. Run focused and relevant nearby tests. Once green, refactor when it improves a
   concrete responsibility, duplication, or readability problem. Rerun affected checks.
5. Repeat for the next criterion. Before handoff, read the diff and run required
   project checks appropriate to the final change.

Use controlled clocks/promises and isolated state rather than arbitrary sleeps.
Mock external boundaries only when their behavior is outside the test's claim.
Vue tests should establish rendering/events and a real browser where needed.
Database semantics need disposable PostgreSQL, rather than SQLite or a mocked commit.
Read [test design examples](../references/test-design.md) for difficult assertions,
generated cases, or meaningful invariants.

If code already exists, preserve it and add characterization or regression coverage.
Report a missed test-first step honestly. For a regression, confirm the assertion
distinguishes pre-fix behavior in an isolated copy when practical; do not reset user
work or delete implementation to manufacture red. Pure refactors can use existing
coverage and characterization tests; prose/formatting edits need no invented tests.

Keep deterministic adapters and orchestration under TDD for AI features. Use
task-specific evaluations for model output, tool selection, outcomes, and effects;
one exact model reply or a mocked tool call cannot establish agent reliability.

Record actual commands, results, relevant red/green evidence, and checks not run.
Proceed to [review and verification](review-and-verify.md); implementation self-review
does not replace an independent reviewer when the selected execution mode requires one.
