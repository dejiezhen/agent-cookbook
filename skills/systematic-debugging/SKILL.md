---
name: systematic-debugging
description: Diagnose a reproducible bug, failing test, or unexpected runtime behavior by tracing evidence and testing hypotheses before applying a focused fix.
---

# Evidence-led debugging

Capture expected behavior, actual behavior, reproduction steps, and environment.
Read the full error and relevant recent changes. Establish whether the issue is
deterministic, intermittent, or environment-specific. Preserve the original symptom.

Trace data and control flow from the failing boundary to its source. Compare a
working case with a failing one. Distinguish observed facts from hypotheses.
Choose a small discriminating experiment: name the hypothesis, predicted result,
and how each possible result changes the next step. Change one meaningful variable
at a time. Prefer temporary instrumentation over speculative production rewrites.

Once evidence supports a cause, capture it in a focused regression test or a
repeatable reproduction check. Observe failure, implement the smallest cause-level
fix, and observe success. Check nearby failure paths. Do not fix the symptom with
blanket retries, broad exception handling, disabled validation, or arbitrary delays.

For a Vue race, compare request ordering and state ownership. For a Python failure,
inspect exception causes and resource lifetime. For Postgres, inspect actual schema,
transaction boundaries, and relevant locks or query plans in an appropriate test
environment. Use production access only when already authorized and necessary.

After two experiments that provide no useful distinction, revisit the hypothesis
set and missing evidence before another code change. If blocked by unavailable
data or infrastructure, report what was learned and the specific evidence needed.

Finish with cause, fix, regression evidence, and any remaining uncertainty. Remove
temporary instrumentation introduced for diagnosis unless its operational value is
part of the requested fix.
