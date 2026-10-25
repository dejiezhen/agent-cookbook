# Feature or fix

## Goal, scope, constraints

State the user outcome, current behavior, intended behavior, and relevant non-goals.
Record compatibility, authorized effects, and unresolved material decisions.

## Acceptance criteria and test map

| ID | Given / when / then, including relevant failures | Planned test level/case |
| --- | --- | --- |
| AC-1 | Observable result | Unit, integration, or browser |

## Implementation tasks

For each cohesive task record:

- Goal and acceptance IDs; exact behavior and failure cases.
- Dependencies and interfaces; relevant global constraints.
- Likely/permitted files and selected engineering/stack module paths.
- Spec → red → green → refactor for changed executable behavior.
- Focused checks and required integration evidence.

Keep this proportional; a single task need not repeat the spec. Group tiny edits of
the same shape when dispatching each separately would add no useful isolation.

## Execution and completion

Record baseline state/revision, inline or delegated execution, task/review budget,
and restrictions on commits or external effects when relevant. Define integrated
checks. During execution, map criteria to actual evidence and record remaining gaps.
The plan does not grant new authorization.
