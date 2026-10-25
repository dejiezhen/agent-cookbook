# Choose assertions that expose a mistake

Read for difficult test design or generated input domains.

## Behavior examples

For "archive a project," assert the intended project's stored state, unrelated state,
and relevant response. Asserting that a mock's `archive()` method was called proves
less. For a denied request, verify no write occurred rather than only checking text.

Identify a specific pre-fix outcome that should fail the regression assertion.
A test passing against both versions may cover another behavior. Compare in an
isolated copy if needed; do not reset or discard uncommitted user work.

## Generated cases

Use property-based testing when a domain has an independently meaningful rule:

- A serializer/parser pair preserves supported values across a round trip.
- Normalizing an already normalized value leaves it unchanged.
- A state transition preserves a defined invariant for valid initial states.

Confirm the property is actually specified; not every normalization is lossless.
Generate valid constrained inputs directly, and test invalid inputs separately.
An assertion that duplicates the implementation or filters out almost every case
can provide little evidence. Keep a minimized counterexample as a regression case.

Reuse an existing library. If none exists, weigh adding Hypothesis (Python) or
fast-check (TypeScript) against a few explicit boundary examples. A new dependency
is worthwhile for a demonstrated testing need, not for every small function.

References: [Hypothesis quickstart](https://hypothesis.readthedocs.io/en/latest/quickstart.html),
[fast-check rationale](https://fast-check.dev/docs/introduction/why-property-based/).
Related upstream skill: [Trail of Bits property-based testing](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md).
