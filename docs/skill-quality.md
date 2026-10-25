# Depth and quality

A short skill can be useful or vague; a long skill can be precise or distracting.
Length alone does not establish quality. The useful question is whether the skill
changes an agent's decisions on an actual task in a way that improves the result.

## What belongs where

- `SKILL.md`: trigger, task-specific decisions, real constraints, essential workflow,
  and the evidence needed to finish.
- `references/`: conditional detail and worked failure cases. Link each reference
  at the point where the agent needs it, rather than loading every file by default.
- `assets/`: templates that become part of the task's output.
- `scripts/`: repeated mechanics that benefit from deterministic execution. Add
  these for real recurring work, not to make a skill look substantial.

The engineering entrypoint stays compact while its references demonstrate
abstraction choices, ownership, and ambiguous writes. Vue references cover specific
version and async-state traps. Python examples clarify validation and error boundaries.
Agent skills carry tool contracts, evaluation plans, and attack/recovery cases.

## When to add detail

Add a concrete example when the short rule permits a recurring wrong interpretation.
Add an invariant when a mistake can corrupt state or cross an authorization boundary.
Add exact commands when the target project's tooling is known and the sequence matters.
Preserve room for judgment where several approaches meet the requirement.

Avoid encyclopedic syntax tutorials, repeated slogans, invented edge cases, and
mandatory ceremony for unrelated tasks. External skills can contain useful guidance
and author-specific preferences in the same file; evaluate both separately.

## Current evidence and limits

The library has structural validation and tests of its management utilities. These
checks do not demonstrate that the skills improve agent behavior. Manual behavioral
scenarios are documented but have not yet been executed as independent trials.

The next meaningful validation is a real permitted project task: record a baseline,
run the same task with a selected skill under comparable conditions, inspect artifacts
and execution, and revise only from observed failures. Project-specific examples,
commands, schemas, and incidents will add more value than padding every entrypoint.

Reference: [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices).
