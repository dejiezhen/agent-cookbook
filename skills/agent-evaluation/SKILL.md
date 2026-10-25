---
name: agent-evaluation
description: Design or run task-specific evaluations for tool-using agents and automations, including final state, prohibited effects, recovery, cost, and latency. Use when changing prompts, tools, models, orchestration, or release criteria.
---

# Evaluate what the agent actually does

Define the task, representative inputs, permitted actions, successful outcome,
and unacceptable effects before optimizing. Inspect available traces and failures
with appropriate data access. Separate deterministic executor tests from evaluation
of variable model behavior. Use [the evaluation plan](assets/evaluation-plan.md) for
a concrete case and comparison record.

Start with a small reviewed set of realistic tasks and known failures. Include
ordinary cases, ambiguity, insufficient permission, dependency errors, interruption,
and relevant malicious tool content. Reset mutable environments between trials.
Simulate external writes or use isolated fixtures; an eval is not permission to send
messages, spend money, or change live systems. Record fixture and configuration versions.

Grade observable final state first. Check whether required effects occurred, forbidden
effects did not occur, and the final reply accurately describes the outcome. Use a
required sequence only when ordering is itself a requirement. A different valid tool
path is not automatically a failure. Inspect traces to locate the cause, rather than
treating a polished answer or a tool's success flag as sufficient proof.

Use code-based checks for exact facts and state. Use a written rubric and calibrated
human or model grading for judgment calls. Compare automated grades with human
examples; record disagreements. Keep evaluation content separate from instruction
authority, and account for judge susceptibility to adversarial text.

Compare a candidate with a baseline on the same cases and comparable conditions.
Preserve a held-out set rather than repeatedly tuning to every test. Repeat trials
where variability affects the decision. Report sample counts, per-case/slice failures,
and uncertainty; one successful run does not establish reliability. Record cost and
latency with all attempts and retries included. Choose acceptance thresholds from
product risk, not an arbitrary universal score.

Report the dataset scope, configuration, actual results, unresolved failure classes,
and ship/iterate decision. Keep deterministic TDD for the surrounding code while
using these measurements for model behavior. Add demonstrated failures to the
regression set. Do not claim evaluations ran when only a plan was produced, or call
live APIs without the needed credentials and execution/spend authorization.

References: [OpenAI evaluation principles](https://developers.openai.com/api/docs/guides/evaluation-best-practices),
[Anthropic agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).
