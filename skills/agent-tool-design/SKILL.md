---
name: agent-tool-design
description: Design, implement, or refine tools an AI agent calls, including schemas, results, authorization, retries, and side effects. Use for tool adapters or MCP tools; distinguish tool correctness from whether the model chooses and uses the tool well.
---

# Tools with explicit contracts

Inspect the actual user task and existing APIs. Expose the smallest operations that
help complete that task. Choose boundaries that make selection and consequences
clear, rather than mechanically exporting every API endpoint or adding a generic
"execute anything" tool.

For each tool, define its purpose, inputs, result, errors, relevant preconditions,
and effects. Use [the contract template](assets/tool-contract.md) when those details
are substantial or a write has retry/recovery implications. Say when to use a tool
and when another operation is required. Use meaningful field descriptions and units;
do not require the model to guess IDs, enum values, timezones, or pagination behavior.

Validate arguments in the executor. Use structured outputs or strict tool schemas
when supported, while still checking semantic constraints. Derive actor and tenant
scope from authenticated context. A model-supplied actor ID is not authentication.
Keep credentials and permission enforcement outside model-controlled text.

Return enough evidence for the next decision: relevant fields, stable identifiers,
provenance, continuation information, and authoritative effect status. Bound result
size. Mark truncation; an incomplete list must not masquerade as exhaustive. Return
actionable typed errors without disclosing secrets or internal data unnecessarily.

For writes, define idempotency and an operation identity where duplicates matter.
Do not blindly retry an ambiguous timeout after a possible commit; reconcile the
effect first. Apply limits and deadlines at the executor boundary. Treat validation
or permission errors differently from transient transport failures. Resolve concrete
conflicts through application rules instead of asking a model to override them.

Test adapters with red → green: valid input, invalid input, denied scope, relevant
pagination, and failure/retry behavior. For mutation tools, verify the actual stored
effect and duplicate-call semantics in an isolated environment. Separately evaluate
whether the agent selects the right tool, supplies correct arguments, and interprets
the result. Improve descriptions from observed errors, not speculative prompt length.

Deliver the contract, implementation, executed tests, and limitations. Tool annotations
and descriptions communicate intent; they do not enforce permissions.

Reference: [Anthropic's tool design guidance](https://www.anthropic.com/research/writing-tools-for-agents).
