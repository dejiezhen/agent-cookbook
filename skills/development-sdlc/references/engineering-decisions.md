# Intentional change examples

Read when choosing boundaries or checking whether a diff has grown beyond its goal.
These are original examples for this library.

## A project gains an archive action

The existing endpoint and service already own project state. Add authorization,
the state transition, and focused tests there. A new repository interface and generic
command bus need a reason beyond having an additional endpoint.

Acceptance criteria describe the allowed transition, denied access, and returned
result. If archive already exists as a state, clarify repeated calls. If the action
sends a notification, check how duplicate requests affect that separate effect.
A small implementation still needs correct ownership and failure handling.

## Two calculations look similar

A display estimate and a billing rule both multiply values, but have different
rounding and change owners. Keep them separate until a genuinely shared rule exists.
If two endpoints implement the same eligibility policy, a named policy function can
give the rule one owner. Avoid making unrelated behavior fit a configurable helper
just to reduce repeated syntax.

## A network timeout follows a write

A timeout says the caller did not receive a result. It does not prove the write
failed. Reconcile the operation using existing state or an operation identity before
retrying a potentially duplicate effect. A retry helper is useful only after defining
which failures are transient and which operations are safe to repeat.

## A change needs another dependency

Name the missing capability and compare the existing stack with the proposed package.
Consider maintenance, compatibility, and failure modes. A library can reduce code
and risk for a hard problem; a wrapper around a straightforward standard-library
operation can increase both. Decide for this requirement rather than establishing
a speculative platform.

## Completion review

Trace each changed file to behavior, integration, verification, or necessary docs.
Ask what would become harder to maintain if the new abstraction were removed. If
there is no concrete answer, prefer the simpler structure. Keep correctness and
security controls even when they add lines.
