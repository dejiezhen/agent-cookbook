---
name: performance-investigation
description: Investigate a measured performance problem in a Vue, Python, or Postgres application and validate a focused improvement. Use for slow interactions, endpoints, queries, or resource pressure; avoid speculative optimization.
---

# Measure before adding complexity

Define the affected operation, representative workload, metric, and target. Capture
a reproducible baseline with environment details and realistic data volume. Separate
client, network, application, and database time before choosing a fix.

Use evidence appropriate to the suspected boundary: browser traces and render
timing, Python profiling, request tracing, or Postgres query plans and statistics.
`EXPLAIN ANALYZE` executes the statement; use a disposable environment or an
explicitly authorized safe workload, especially for writes and expensive queries.

Form a hypothesis and change the narrowest cause supported by measurements. Check
for repeated queries, unnecessary work, overfetching, missing indexes, excessive
rendering, or blocking I/O before adding caches, workers, or concurrency. Consider
index write/storage cost and cache invalidation, memory, and consistency cost.

Protect behavior with a regression test where useful. Rerun the same workload after
the change and compare distributions or repeated measurements rather than a single
favorable run. Check correctness, resource tradeoffs, and performance elsewhere in
the affected path. Avoid flaky wall-clock thresholds in ordinary unit tests.

Report baseline, revised measurements, reproduction method, and limitations. If the
data does not show an improvement, say so and do not retain complexity merely because
it looked promising. Keep benchmark artifacts only when they make future comparison
repeatable.
