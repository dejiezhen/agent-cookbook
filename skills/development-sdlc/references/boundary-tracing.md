# Trace across component boundaries

Use for a failure spanning Vue, a Python service, a tool adapter, or Postgres.
Record enough redacted metadata to compare the same request across boundaries.
Avoid dumping credentials, complete environment variables, or sensitive payloads.

## Example: the UI claims archive succeeded, but the project is active

| Boundary | Evidence | Question |
| --- | --- | --- |
| Vue → API | Target ID, request/run ID, response status, state transition | Was the intended target sent, and was success shown before confirmation? |
| API → service | Authenticated scope, validated ID, returned outcome | Did the correct operation run and propagate its result? |
| Service → Postgres | Transaction outcome, row count, relevant constraint error | Did the write commit, affect zero rows, or roll back? |
| API → Vue | Serialized result and client interpretation | Was a failure translated into success or stale state? |

Suppose the transaction rolls back, but a broad catch returns an empty success-shaped
object. That evidence supports fixing error propagation and its regression test.
An extra frontend refresh or arbitrary retry would hide the failed write.

Compare a working request using the same path. Form one hypothesis and predict
which boundary evidence would confirm or refute it. Remove temporary diagnostics
after the focused regression check unless they have an agreed operational purpose.
