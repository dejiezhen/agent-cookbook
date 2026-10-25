---
name: development-sdlc
description: Carry a software feature or fix from requirements and acceptance criteria through a concise spec, task plan, red-green-refactor implementation, review, and verification. Also supports explicitly requested planning, code review, or verification alone. Use relevant engineering and Vue, TypeScript, Python, or PostgreSQL standards within the requested scope.
license: MIT
---

# Development SDLC

Own the development workflow here. Use **requirements → acceptance criteria and
spec → task plan → red → green → refactor → review → verify**. Requirements and
acceptance criteria form the spec; avoid writing competing versions of them.

Read project instructions, relevant code/tests, configuration, and current Git state.
Preserve existing work and authorization. A request for a plan, review, or verification
alone ends at that deliverable. Authorized implementation continues through completion
without an invented approval gate. Keep tiny work proportional: a short spec in chat,
one cohesive change, and useful checks can suffice.

## Load the current stage

Read the applicable stage before doing its work, rather than loading every file:

| Work | Instructions |
| --- | --- |
| Clarify requirements, define behavior, plan slices | [Specify and plan](phases/spec-and-plan.md) |
| Investigate an unclear bug or intermittent failure | [Diagnose the cause](references/debugging.md), then TDD |
| Implement specified behavior or a regression | [Red, green, refactor](phases/implement-tdd.md) |
| Review a task/diff or verify the result | [Review and verify](phases/review-and-verify.md) |
| Coordinate suitable multi-task implementation | [Subagent execution](phases/subagent-execution.md) |

## Choose proportionate execution

Default to inline work. Choose by uncertainty, impact, and useful task isolation;
several requested items or changed files alone do not justify delegation.

| Change | Default execution |
| --- | --- |
| Small, understood feature or fix | Inline implementation, focused tests, self-review; a short spec in chat |
| Cohesive change with significant correctness, security, or data risk | Inline implementation plus independent review |
| Substantial work with separable task context and interfaces | Fresh task implementers, task reviews, integrated review, and ledger |

Before delegating, state the concrete benefit. Group tiny related work instead of
creating a worker for each helper. Independent review does not require delegating
implementation: for the middle mode, use the [review stage](phases/review-and-verify.md)
and [final-review prompt](prompts/final-reviewer.md) on the one coherent change, without
manufacturing a task pipeline or ledger. One coordinator owns any dispatch and fixes.

When delegation is unavailable or not permitted, work inline and disclose missing
independent review when relevant. Do not simulate it or add a delegation framework.

## Route engineering standards

Read [engineering standards](standards/engineering.md) before design, implementation,
or quality review. Then select stack modules from the task, affected interfaces,
actual files, dependency manifests, and supported versions. Reassess after discoveries;
a package in the repository does not make its standards relevant to every task.

| Affected behavior | Additional modules |
| --- | --- |
| TypeScript code or contracts | [TypeScript](standards/typescript.md) |
| Vue component, composable, or frontend state | [Vue](standards/vue.md), plus TypeScript when used |
| Python code, service, or library | [Python](standards/python.md) |
| SQL, schema, migration, query, or transaction | [PostgreSQL](standards/postgres.md), plus the application language |
| Mixed-stack change | Each relevant module; check contracts across boundaries |

For each delegated task, explicitly pass the selected module paths and require
both implementer and reviewer to read them. They do not inherit the coordinator's
loaded context. Resolve paths relative to this skill, then supply usable absolute
paths or the necessary content if the worker cannot access the files.

Other installed specialist skills can contribute relevant API, accessibility,
debugging, performance, or AI-agent guidance. This bundle has no required sibling
skills, provider SDK, or upstream plugin. An AI feature also needs model-behavior
evaluations where deterministic tests cannot establish the outcome.

## Completion

Map the final behavior and execution evidence to acceptance criteria. Review the
whole change for unnecessary scope and integration gaps. Report actual checks,
material decisions, and remaining limits; a green build or a worker's success message
alone does not establish completion. Publishing and deployment follow existing
authorization.
