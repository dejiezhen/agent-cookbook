# Feature or fix

Keep a style-guide section in every plan; scale other sections to the work.
A tiny change can be a short spec in chat; a new
product or substantial milestone needs enough context to survive a new agent/chat.

## Problem and first useful outcome

Who is affected, what do they do now, and what should improve? Describe the first
complete user journey and the evidence that would show it helps. Reuse existing
product decisions instead of inventing a new vision for an established project.

## Goal, scope, constraints

State the user outcome, current behavior, intended behavior, and relevant non-goals.
Record compatibility, authorized effects, and unresolved material decisions.

## Decisions, boundaries, and open questions

Record stack/runtime choices and their reasons, relevant data ownership/interfaces,
deployment constraints, and material risks. Distinguish confirmed decisions,
recommendations, assumptions to verify, and open questions. Map unanswered material
decisions to the tasks they block. Skip sections that add no useful information.

## Acceptance criteria and test map

| ID | Given / when / then, including relevant failures | Planned test level/case |
| --- | --- | --- |
| AC-1 | Observable result | Unit, integration, or browser |

## Style guide

Reference the project's authoritative design/code sources and record affected
choices. For a UI, cover relevant typography, semantic colors, layout/spacing,
components/states, accessibility/input, motion/media, and writing conventions.
Distinguish established choices from proposals and identify checks. For non-UI work,
mark visual styling not applicable and capture code/interface/output conventions.
Do not introduce a redesign or global style migration as a side effect.

## Implementation tasks

Give each cohesive task a stable ID, then record:

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
State the first buildable end-to-end slice, ready versus blocked work, context paths,
and the next implementation action. Mark proposed files/commands as proposals until
verified. The plan must be understandable without the interview transcript.
