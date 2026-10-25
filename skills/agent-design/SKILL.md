---
name: agent-design
description: Design a tool-using AI agent or automation around a concrete task, with explicit state, bounded execution, and measurable outcomes. Use when choosing orchestration or implementing an agent loop; preserve the existing provider and framework unless changing them is requested.
---

# Build the smallest useful agent

Inspect the product requirement, existing automation, provider integration, tools,
and authorization model. Specify the user-visible outcome, allowed effects, required
inputs, failure behavior, and time/cost limits before selecting an architecture.

## Choose control deliberately

Use ordinary code for rules that can be stated reliably. Use a fixed workflow when
the stages are known. Give the model control over the next action only when tasks
need that flexibility. Start with the existing SDK and one coherent tool set; add
routing, delegation, retrieval, or long-term memory only for a measured need.
Read [automation patterns](references/automation-patterns.md) when choosing between
a workflow and a loop, or designing resumable actions.

Make run state explicit: input, current stage, tool observations, pending effects,
outcome, and stop reason. Define completion, missing information, cancellation,
failed dependency, and exhausted budgets. Bound iterations, tool calls, elapsed
time, and model output as appropriate; budget exhaustion is not successful completion.
Never assume the model's final message establishes that an external action happened.

Keep authoritative business state in the existing application/database. Persist
checkpoints when interruption would lose important work; do not add a distributed
queue for a short synchronous task without a reason. A resumed run must reconcile
previous effects before repeating writes. Cancellation stops future work; already
committed effects may need explicit recovery.

In a Vue/Python app, keep credentials and execution on the backend. Expose real
progress and outcomes to the client, including partial completion. Bind any required
user approval to the exact action and current state, rather than treating a vague
"continue" as permission for changed effects.

## Establish evidence

Use spec → red → green for deterministic orchestration and adapters. Define agent
evaluation cases before tuning prompts, then compare against the simplest baseline.
Measure task success, unauthorized/duplicate effects, recovery, latency, and cost.
Log useful run/tool identifiers and outcomes with appropriate redaction and retention.
Use versioned prompts and configuration; verify current SDK semantics from official
documentation when implementation depends on them.

Deliver the chosen control flow, justified complexity, state/stop behavior, and
actual verification. Do not add a framework, provider abstraction, or multi-agent
layer solely because the feature uses a model.

Reference: [Anthropic's architecture patterns](https://www.anthropic.com/research/building-effective-agents).
