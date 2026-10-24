---
name: test-driven-development
description: Implement specified behavior or a regression fix through observed red-green-refactor cycles. Use for new executable behavior and bug fixes; do not force tests onto prose, formatting, or a disposable investigation.
---

# Test-driven implementation

Start with a concise behavioral spec or existing acceptance criteria. If the user
already supplied clear criteria, use them directly. Inspect the project's runner,
test conventions, and baseline before changing production behavior.

1. Select one observable behavior. Write the smallest test that would expose its
   absence through a meaningful assertion. Prefer public interfaces over private
   structure. For a regression, reproduce the reported symptom.
2. Run it and inspect the failure. Confirm the failure concerns the missing behavior.
   Import errors, a broken fixture, or unavailable infrastructure do not demonstrate
   the intended red. Fix the harness and rerun before calling it red.
3. Implement only what makes that behavior correct. Keep the real boundary intact;
   do not make a test pass by mocking away the behavior being specified.
4. Run the focused test and relevant nearby tests. Once green, improve structure
   when there is a concrete benefit. Rerun after refactoring.
5. Repeat for the next criterion, then run the project's required checks appropriate
   to the final diff. Report actual evidence and remaining gaps.

Use Vue component tests for visible states/events and a real browser when browser
behavior matters. Use parametrized Python tests for meaningful input partitions.
Use a disposable Postgres instance for SQL, constraints, or transaction semantics;
SQLite and mocks do not establish Postgres correctness.

Keep tests deterministic: control clocks and random seeds when relevant, await
observable async conditions, and isolate mutable state. Mock external boundaries
when their behavior is outside the test's claim.

If implementation already exists, preserve it and add characterization or regression
coverage. Report that test-first order was missed; never delete user code or claim
an unobserved red. If execution is blocked, state that limit without inventing results.

Reference: [Martin Fowler on TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html).
