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

The Development SDLC entrypoint routes to substantial stage and stack modules.
Engineering references demonstrate abstraction choices, ownership, and ambiguous
writes. Vue references cover version and async-state traps. Python examples clarify
validation and error boundaries. These resources belong to one installable skill;
they are not separate workflow owners. Agent skills carry tool contracts, evaluation
plans, and attack/recovery cases.

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
checks alone do not demonstrate that the skills improve agent behavior. A
[historical subagent workflow trial](evaluation.md#recorded-trial-combined-subagent-workflow)
executed two tasks with fresh implementers, independent task review, integrated review,
and passing tests. It exercised the successful path, not recovery or a fix loop.
A [Development SDLC routing trial](evaluation.md#recorded-trial-development-sdlc-scope-and-stack-routing)
then exercised full-stack planning-only and Vue review-only scope on the new bundle,
preserving existing files and Git state. A separate
[implementation trial](evaluation.md#recorded-trial-development-sdlc-implementation)
executed the new entrypoint from requirements through TDD, explicit Python standards
handoff, independent reviews, and a passing 14-test suite. These did not execute a
full Vue application/database, interruption recovery, or a review fix loop. Other
scenarios remain planned; comparative effectiveness and behavior across agent hosts
have not been established.

Further validation should use a real permitted project task: record a baseline,
run the same task with a selected skill under comparable conditions, inspect artifacts
and execution, and revise only from observed failures. Project-specific examples,
commands, schemas, and incidents will add more value than padding every entrypoint.

Reference: [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices).
