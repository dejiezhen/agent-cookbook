---
name: spec-driven-development
description: Turn a feature request or behavior change into a concise, testable specification before implementation. Use for spec-first work, acceptance criteria, and reducing ambiguity; continue into implementation when the user requested it.
---

# Spec → red → green

Read relevant code and existing tests before drafting. Capture the user's goal,
current behavior, intended behavior, and constraints. Resolve questions from the
repository first. Ask only about missing decisions that materially change behavior.

Write the shortest spec that makes the change testable. Keep it in the existing
project convention; use chat for tiny work. For a substantial feature, use the
[spec template](assets/spec-template.md). Define scope and non-goals, stable
acceptance IDs, realistic examples, important failure cases, and compatibility.
Mark unresolved decisions; do not quietly invent business rules.

Map each acceptance criterion to the lowest useful test level. Use a unit test for
a pure rule, an integration test for a database or API boundary, and a browser test
for a critical user journey. A criterion may require multiple levels when their
failure modes differ. Avoid a long task plan that repeats the spec.

If asked to implement, carry the spec into small vertical slices. For each slice,
write a test, observe its relevant failure, implement the minimum coherent behavior,
then refactor with passing tests. Record criterion-to-test evidence at completion.
When only a spec was requested, stop after producing the spec and test map.

Keep spec detail proportional to uncertainty. Do not turn every edit into a design
ceremony or add an approval checkpoint when implementation is already authorized.
If requirements change, update the spec and tests together. Preserve the user's
work even if it predates the spec.

Reference: [GitHub Spec Kit](https://github.com/github/spec-kit), a larger toolkit
to consider when a project needs persistent specifications and planning artifacts.
