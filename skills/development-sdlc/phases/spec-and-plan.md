# Specify and plan

Read the current behavior, nearby implementations, tests, and configuration before
designing a change. Capture the user's goal, intended behavior, constraints, and
important compatibility needs. Resolve questions from available evidence first;
ask about missing business decisions that materially affect the outcome. Mark
unresolved decisions rather than quietly inventing a rule.

Write the shortest useful spec. Use existing project conventions; chat is enough
for tiny work. For substantial work, adapt the [spec and plan template](../assets/spec-and-plan.md).
Give acceptance criteria stable IDs and observable outcomes, with realistic examples
and failure cases relevant to the operation. State scope and non-goals only when they
help prevent ambiguity. Do not expand the assignment to improve unrelated architecture.

Map criteria to the lowest useful test level: pure rule → unit; API/database boundary
→ integration; browser-specific behavior or a critical user journey → browser.
Use multiple levels when they expose different failure modes. An authorization
criterion includes absence of the forbidden write, not just an error message.

Choose cohesive slices with explicit dependencies, interfaces, likely files, and
completion checks. Each task names its criteria and selected engineering/stack
modules. A plan should make execution clearer without repeating the whole spec.
Inspect existing tests before planning new infrastructure. Identify required project
checks and any unavailable dependency early.

If implementation is authorized, proceed to [TDD](implement-tdd.md) inline or
[subagent execution](subagent-execution.md) for suitable multi-task work. Keep one
authoritative spec through implementation; update it and the tests when requirements
change. When only planning is requested, deliver the spec/plan and stop.
