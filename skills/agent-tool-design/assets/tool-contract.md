# Tool contract

## Task and boundary

State the user task this operation supports, when to call it, and any prerequisite
lookup. Describe read effects and write effects separately when both exist.

## Inputs and trusted context

| Field | Type / units | Validation | Source of value |
| --- | --- | --- | --- |
| target_id | Stable resource identifier | Exists and is in the actor's scope | Prior lookup or trusted application state |
| operation_id | Request identity, if needed | Consistent with the operation's payload | Application-generated |

Actor identity, permissions, and tenant scope come from authenticated application
context. Adapt the table to the actual operation; do not add fields with no use.

## Results and errors

Define success evidence, no-op/partial outcomes, bounded output, and pagination.
Distinguish invalid input, denied access, conflict, transient dependency failure,
and unknown effect status after a timeout where they matter.

## Effects and recovery

Document the transaction/commit boundary, idempotency, duplicate requests, uncertain
outcomes, cancellation, and reconciliation. Bind any required approval to the
action's exact target and payload. Omit mechanisms the operation does not need.

## Verification

Record adapter tests and agent-use scenarios separately, with actual results.
Check final state and unintended effects, rather than only a success-shaped reply.
