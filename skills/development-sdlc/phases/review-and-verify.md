# Review and verify

Review and verification have different outputs: supported findings and execution
evidence. Apply the requested scope. A review-only assignment stays read-only and
does not start implementation, delegate more reviews, or publish changes.

## Review the actual change

Read the spec/task brief, project instructions, selected standards, complete diff,
new files, and relevant callers. Establish the real base and reviewed state. For
multi-commit or uncommitted changes, use [exact change packaging](../references/review-and-recovery.md).
Treat implementer reports as claims to check.

Check separately:

- **Specification:** each criterion is implemented correctly; no omitted behavior,
  misinterpreted rule, or unrequested feature.
- **Quality:** correctness, state ownership, errors, authorization, concurrency,
  data integrity, compatibility, meaningful assertions, and justified complexity
  where affected by this change. Apply [engineering](../standards/engineering.md)
  and the relevant stack modules, rather than personal style preferences.

Trace callers, middleware, database constraints, and tests before declaring a missing
check. Inspect query count, result bounds, and transaction ownership for affected
data access. Resolve concrete risks beyond the diff without expanding into an
unrequested whole-project audit. Read omitted/truncated sections or disclose partial
coverage. Run focused checks when they can resolve a concrete uncertainty.

For each finding, provide severity, trigger, impact, verified location, and supporting
reason or reproduction. Keep uncertain hypotheses and optional suggestions separate
from defects. Do not invent findings or demand speculative infrastructure. A material
unmet criterion cannot be waived by calling it optional. In coordinated execution,
the coordinator owns fixes and scoped re-review using the
[review/recovery rules](../references/review-and-recovery.md).
This includes findings from the final integrated review and inline implementation
with independent review: record the reviewed state, fix, run affected checks, and
obtain scoped independent re-review before treating those findings as resolved.

## Verify the final behavior

Map acceptance criteria to evidence covering the actual final code. Use configured
commands and required project checks. Reuse evidence only while its relevant code,
dependencies, configuration, schema/data setup, and environment inputs remain valid;
use the [evidence rules](../references/review-and-recovery.md#evidence-and-final-state).
Rerun affected checks after changes and close specific integration gaps. Avoid ritual full
suite repetitions, while honoring mandatory project/CI checks.

| Claim | Evidence that addresses it |
| --- | --- |
| Regression fixed | Relevant assertion fails before the fix and passes after it |
| Vue interaction works | Observable interaction plus configured template/type checks; browser where required |
| PostgreSQL invariant holds | Real database constraint/transaction cases on the supported version |
| Write succeeded | Authoritative committed state, beyond an adapter call |
| Agent completed a task | Required final state and absence of forbidden effects |

Inspect exit codes, assertions, counts, warnings, skips, and environment. A successful
build alone does not prove behavior. Distinguish assertion failures from unavailable
infrastructure and pre-existing failures. Do not quietly fix unrelated failures.

Inspect the full final diff for missing wiring, incompatible contracts, clutter,
unused helpers, and unexplained dependencies. Hand off delivered behavior, checks
actually run/results, significant tradeoffs, and material gaps. Claim clean CI,
deployment, independent review, or observed red only when actually established.
