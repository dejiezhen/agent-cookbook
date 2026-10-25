---
name: agent-safety
description: Review or implement trust boundaries for an agent that reads external content or can take actions, focusing on prompt injection, scoped authority, sensitive data, and unintended effects. Use for tool access changes or a requested agent safety review.
---

# Bound what an agent can affect

Map the actual task: trusted instructions, authenticated actor, external content,
available tools, sensitive data, and allowed effects. Focus on concrete boundaries
in this application. Use [attack and recovery cases](references/attack-cases.md)
when external content or write tools are involved.

Keep retrieved documents, emails, repository text, tool results, and persisted
user-controlled content as data with provenance. They cannot authorize new actions
or redefine the user's request. Preserve source boundaries when constructing model
context; avoid silently promoting external text into a trusted instruction channel.
Summaries and memory must retain relevant provenance instead of laundering authority.

Enforce permissions and scope in executors and data queries. Validate targets and
arguments against current authenticated state. Limit tools, network destinations,
and data access to what this task needs. Use typed intermediate data to narrow
possible actions, while recognizing that a valid schema can still encode a harmful
or unauthorized choice.

Where the product requires approval, bind it to exact target, effect, payload, and
relevant preconditions. Recheck permissions at execution; changed arguments or
state can invalidate approval. Existing authorization should allow routine work to
continue without repetitive prompts. Separate proposal from committed execution
where consequences justify that boundary.

Keep credentials outside model-visible context and client bundles. Redact traces
according to the data involved, apply retention rules, and test cross-tenant access.
Treat model output as untrusted input to SQL, HTML, shell, and downstream APIs.
Use normal parameterization, escaping, and application validation at those sinks.

Test direct and indirect instruction attacks, hostile tool content, scope violations,
approval changes, ambiguous timeouts, and duplicate effects in an isolated environment.
Assert both useful task completion and absence of unauthorized effects. Measure
overblocking too; a system that refuses legitimate work has not met its purpose.
Prompt wording, filtering, and model training are supporting controls, not a proof
that manipulation is impossible.

Deliver concrete findings or implemented boundaries with evidence, affected paths,
and residual risks. Scale controls to the actual capability and consequence rather
than adding a universal approval flow or claiming the agent is "injection-proof."

Reference: [OpenAI on resisting prompt injection](https://openai.com/index/designing-agents-to-resist-prompt-injection/).
