# Diagnose before patching

Use for an unclear cause, intermittent failure, or symptom crossing component
boundaries. Keep a clear localized regression proportional; it does not need an
investigation ceremony.

Capture expected versus observed behavior, a repeatable reproduction or failure
trace, relevant environment, and recent changes. Preserve the original symptom.
Distinguish an assertion failure from a missing service or broken harness.

Trace inputs and effects to the first boundary that violates its contract. Compare
a working case with a failing case. Name a plausible cause, the observation that
would distinguish it, and a small experiment. Prefer controlled timing, a focused
test, or temporary instrumentation over speculative production edits. If experiments
stop distinguishing hypotheses, revisit the evidence instead of accumulating patches.

Once evidence supports the cause, capture it with a regression assertion at the
owning boundary, observe red, make the smallest cause-level fix, and observe green.
Confirm that the original reproduction is resolved. Avoid hiding the symptom with
blanket retries, swallowed exceptions, disabled validation, or arbitrary delays.
For races, control completion order; for database failures, inspect real constraints
and transaction boundaries in an appropriate disposable environment.

Record cause, fix, regression evidence, and remaining uncertainty. Remove temporary
diagnostic code unless its ongoing operational value belongs to the request. If
execution is blocked, state the missing evidence and continue independent work;
do not invent a diagnosis or claim the bug is fixed.
