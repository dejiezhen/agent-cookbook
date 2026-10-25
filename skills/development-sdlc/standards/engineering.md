# Intentional engineering

Use these principles to decide a concrete design, rather than as a checklist that
creates work. Respect explicit user requirements and supported project conventions;
identify an actual defect when a convention must change. Optimize for understandable,
correct behavior and manageable future change.

## Principles and their limits

| Principle | Apply it | Avoid the common misuse |
| --- | --- | --- |
| YAGNI | Build capabilities and extension points for demonstrated requirements | Omitting required security, failure handling, compatibility, or reliability |
| KISS | Prefer the simplest design that satisfies the real constraints | Dense clever code, or removing necessary controls merely to reduce lines |
| DRY | Give a shared business rule or invariant one authoritative owner | Coupling unrelated rules just because their syntax looks similar |
| Modular design | Group behavior that changes for the same reason; expose a small purposeful interface | A file, service, or interface for every function |
| High cohesion, low coupling | Keep related policy/state together and dependencies explicit | Splitting one responsibility across many pass-through layers |
| Separation of concerns | Separate domain policy from transport, persistence, or UI effects where it clarifies ownership | Mandatory architecture layers around a straightforward operation |
| Explicit contracts | Define valid inputs, outputs, state transitions, and failures at boundaries | Revalidating the same trusted value in every internal function |
| Composition | Assemble small functions/components for actual responsibilities | Banning useful inheritance, or creating a generic framework preemptively |
| Testable design | Exercise observable rules and real integration boundaries | Adding interfaces or DI machinery solely to mock implementation details |

Use SOLID as a diagnostic where applicable: a coherent responsibility, substitutable
implementations, small client-facing interfaces, and stable dependency boundaries.
These do not require classes, a DI container, or extension hooks in every project.
Prefer an existing module or a plain function until another boundary earns its cost.

## Correctness at boundaries

Identify who owns each state and invariant, what can fail, and what effects can
already have happened. Keep one source of truth; derive state instead of maintaining
copies. Validate untrusted input at its entry point. Preserve transaction ownership
and use database constraints for durable relational invariants.

Handle expected failures where recovery or translation belongs. Preserve useful
causes; avoid swallowing errors or returning success-shaped defaults after failure.
Bound retries and resource use. A timeout after a write leaves the outcome uncertain:
reconcile before repeating an effect that could be duplicated. Clean up resources,
subscriptions, and background work when their owner ends.

Enforce authorization on the server, parameterize queries, and keep secrets out of
clients/logs. Account for meaningful concurrency, partial failure, accessibility,
and backward compatibility when this change affects them. Keep old/new deployment
versions compatible when they must coexist; do not impose a rollout ceremony without
that requirement.

Measure a suspected bottleneck before adding caching or concurrency. Add logs,
metrics, or traces to answer a concrete operational question. Document a non-obvious
decision or contract, rather than narrating straightforward code.

## The complexity test

For each new abstraction, dependency, module, or configuration change, name the
current requirement or concrete risk it addresses. Compare the existing stack and
maintenance cost. Libraries can reduce risk for difficult problems; a second tool
or a wrapper around a simple operation can add cost. No numeric size rule decides.

At review, tie changed files to behavior, required integration, meaningful tests,
or necessary docs. Remove speculative helpers, unused options, pass-through wrappers,
and unrelated cleanup introduced by this change. Preserve useful existing work.
Read [decision examples](../references/engineering-decisions.md) when evaluating a
proposed extraction, retry, dependency, or wider refactor.

References: [Google design and complexity review](https://google.github.io/eng-practices/review/reviewer/looking-for.html),
[YAGNI](https://martinfowler.com/bliki/Yagni.html).
