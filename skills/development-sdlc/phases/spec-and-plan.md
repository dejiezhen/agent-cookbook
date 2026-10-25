# Specify and plan

For a new or ambiguous product, or a request for a thorough planning interview,
use [discovery](../references/discovery-interview.md) first. A bounded change with
clear criteria can use the concise flow below. In an existing project, inspect
current behavior, nearby implementations, tests, specs, and configuration before
asking questions. In an empty project, distinguish proposed choices from facts.

Capture the user's goal, intended behavior, constraints, and
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

Make a substantial plan usable by an agent without the interview transcript: include
confirmed decisions, material assumptions/open questions, criteria, ordered task IDs,
interfaces/dependencies, relevant context paths, and the first buildable slice.
Identify tasks blocked by unanswered decisions. Never label a plan implementation-ready
while concealing a missing decision that changes its behavior or architecture.

If implementation is authorized, proceed to [TDD](implement-tdd.md) inline or
[subagent execution](subagent-execution.md) for suitable multi-task work. Keep one
authoritative spec through implementation; update it and the tests when requirements
change. When only discovery or planning is requested, deliver the interview state
or spec/plan and stop. A later implementation request consumes that saved artifact;
recheck its assumptions against the current repository instead of restarting the
whole interview or depending on lost chat context.
