---
name: spec-driven-development
description: Turn a feature request into a concise specification, acceptance criteria, and a scoped implementation plan. Use for spec-first planning and reducing ambiguity; hand authorized implementation to the selected execution workflow.
---

# Specify and plan

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

For a multi-task change, produce cohesive implementation slices with explicit
dependencies, interfaces, constraints, and completion checks. Map each task to its
acceptance criteria. Include spec → red → green → refactor for changed executable
behavior and relevant engineering or language standards in the task's brief.

When implementation is requested, hand the plan to subagent-driven development if
that skill and delegation tools are available and the tasks suit it. That workflow
owns dispatch, progress, reviews, fixes, and final verification. For a small or tightly
coupled change, execute inline with the same TDD and evidence standards. Preserve
existing authorization; planning does not require another approval checkpoint.
When only a spec or plan was requested, stop at that deliverable.

Keep spec detail proportional to uncertainty. Do not turn every edit into a design
ceremony or add an approval checkpoint when implementation is already authorized.
If requirements change, update the spec and tests together. Preserve the user's
work even if it predates the spec.

Reference: [GitHub Spec Kit](https://github.com/github/spec-kit), a larger toolkit
to consider when a project needs persistent specifications and planning artifacts.
