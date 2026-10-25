# Automation decisions

Read for orchestration choices and recovery design. These examples are original
design exercises, not a requirement to build each component.

## Known steps: issue triage

A job reads new issues, asks a model for a category, validates the category against
an enum, and applies an allowed label. The application owns fetching, validation,
authorization, and writing. A fixed workflow is sufficient. Add model-directed
investigation only if real cases show that fixed input is insufficient.

## Variable investigation: incident assistant

The assistant may need different log searches according to earlier results. A
bounded read-only loop can choose investigations. Give search results provenance,
limits, and run IDs. Define what constitutes enough evidence and how to report
uncertainty. Model-generated remediation is a proposal until the application's
authorization and execution path accepts the exact action.

## Interruption after a write

An archive operation commits, but its response is lost. Restarting the agent from
the last conversational message can duplicate a notification or other effect.
Keep an operation ID and authoritative effect record. On resume, reconcile that
record and report the outcome; retry only according to the operation's semantics.
Reuse an existing job store or transaction mechanism before adding new infrastructure.

## Model output used by code

Require a small typed result where the model selects an enum or structured action.
Handle refusal, truncation, invalid output, and provider failure distinctly.
Schema validity does not establish business validity or authorization. A server
must still verify ownership, preconditions, and allowed values.

Reference: [structured output documentation](https://developers.openai.com/api/docs/guides/structured-outputs).
Check the current provider's supported schema features when implementing.
