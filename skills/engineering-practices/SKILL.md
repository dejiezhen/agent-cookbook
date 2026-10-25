---
name: engineering-practices
description: Apply intentional software engineering practices when designing or implementing a feature, assessing maintainability, or explicitly reviewing engineering quality. Favor the smallest coherent change that meets the requirement.
---

# Intentional engineering

Optimize for understandable, correct code with a clear reason to exist. Choose
practices according to the actual change, repository conventions, and failure cost.

## Before changing code

Read applicable project instructions, nearby implementations, and test/build
configuration. State the desired behavior and the existing boundary that owns it.
Turn new behavior into a short spec with observable acceptance criteria, then work
through red → green → refactor. For a small change, a few sentences are enough.

Identify the invariant and effects: what must remain true, who owns the state,
and what can be committed or observed externally. For meaningful failure behavior,
consider denied access, partial failure, and repeated execution. Use cases relevant
to this operation. Read [decision examples](references/decision-examples.md) when
an abstraction, dependency, retry, or wider refactor seems necessary.

## Design decisions

- Keep business rules near their owner and I/O at explicit boundaries. Use a plain
  function or existing module when sufficient. Add a service, interface, factory,
  composable, or repository layer only for a demonstrated boundary or variation.
- Prefer a little understandable duplication over coupling unrelated concepts.
  Extract when shared semantics are stable; line count alone is not evidence.
- Keep one clear source of truth. Model valid states explicitly and avoid duplicated
  derived state. Validate external input where it enters the system.
- Handle expected failures explicitly. Preserve useful causes and provide actionable
  user errors. Add retries only for transient failures, with bounded attempts and
  safe semantics. Use transactions for invariants spanning database writes.
- Enforce authorization on the server and relational integrity in Postgres. Keep
  secrets out of clients and logs. Parameterize queries.
- Add logs, metrics, or traces where they answer a concrete operational question.
  Measure a suspected bottleneck before introducing caching or concurrency.
- Follow existing formatting, names, type checking, and dependency choices. Explain
  the concrete benefit and maintenance cost before adding a new dependency.

## Check the final diff

Can each changed file be tied to an acceptance criterion, a required integration,
or meaningful verification? Remove speculative configuration, unused helpers,
pass-through wrappers, and unrelated cleanup introduced by this change. Keep
required validation, security, and compatibility behavior even when it adds code.

Report behavior delivered, checks actually run, and material tradeoffs. Explain an
architectural decision only when its reason would otherwise be lost.

Reference: [Google engineering review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html).
