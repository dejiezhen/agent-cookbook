---
name: code-review
description: Review a diff or pull request for actionable defects, regressions, missing behavior, and unnecessary complexity. Use for requested reviews; report evidence and keep stylistic preferences separate from correctness findings.
---

# Review a change

Read the requested diff, relevant specification, nearby callers, and project
instructions. Establish the base revision and changed behavior. Trace important
inputs through outputs and durable effects; do not judge a changed line in isolation.

Prioritize incorrect behavior, data loss, authorization errors, concurrency hazards,
contract incompatibility, and missing tests that would expose a concrete defect.
Check whether new abstractions, dependencies, configuration, and wrappers solve a
current problem. Do not demand speculative infrastructure as a quality improvement.

For each finding, identify the trigger, affected behavior, and reason supported by
code or a reproduction. Use a narrow verified file/line location. Rank severity by
actual impact and likelihood. Explain a practical correction without rewriting the
whole design. Mark uncertain hypotheses as questions or limitations, not confirmed
bugs. Avoid restating issues already fixed in the reviewed revision.

Before reporting a missing check, trace callers, middleware, constraints, and tests
that may already enforce it. For changed data access, inspect query count, result
bounds, and transaction behavior where relevant. Read omitted/truncated diff sections
before claiming full coverage; state the reviewed subset when the task is bounded.

Run focused tests when they can discriminate a suspected issue and execution is
available. Reading tests is not equivalent to running them. Check both whether a
test covers the requirement and whether it would fail if the implementation broke.

Return actionable findings first, followed by verification and material review
limits. If none are supported, say so; do not invent findings to fill a quota.
Keep optional maintainability suggestions brief and separate. Respect read-only
review scope unless the user also asked for fixes.

Reference: [Google review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html).
