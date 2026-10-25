# Development ledger

## Identity

- Plan and specification paths:
- Checkout / branch:
- Overall base revision:
- Execution mode, reason for delegation if any, and task/review budget:
- Baseline state and pre-existing changes:
- Selected engineering/stack modules per task and integrated review:

## Tasks

| Task | State | Worker / reviewer | Base → head or patch | Report / review | Checks and remaining gaps |
| --- | --- | --- | --- | --- | --- |
| Record the task ID | Pending, implementing, reviewing, fixing, complete, or incomplete | Record actual identities | Use exact revisions or artifacts | Record paths | State observed evidence |

## Decisions and findings

Record a material decision, its evidence, and consequences. Keep unresolved required
criteria distinct from optional suggestions. Preserve significant rulings for final
handoff rather than hiding them in scratch files.

## Integration and handoff

Record the final review, final revision, checks that cover it, unresolved gaps,
and the next action if interrupted. Never infer completion solely from a status label.
For each required final-review finding, record the fix identity, affected checks,
and independent re-review verdict/identity. Retain superseded verdicts as history.

## Verification inputs

For reused results, record command/outcome, tested revision plus dirty patch if any,
and relevant dependency/configuration/runtime/schema/fixture identities. Note which
changes invalidate which checks and the refreshed evidence. Keep this proportional.
