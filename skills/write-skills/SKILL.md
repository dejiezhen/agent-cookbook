---
name: write-skills
description: Create or refine a focused portable developer skill from a repeated workflow or demonstrated failure. Use when adding a new skill to this library or tailoring one to an actual project.
---

# Write a skill that changes decisions

Identify a realistic task the skill should handle and a nearby task it should not
attract. Ask for missing domain constraints only when they materially affect the
workflow. Inspect existing skills before adding another overlapping entry.

Use one folder per capability with a `SKILL.md` containing YAML `name` and
`description`, followed by concise Markdown instructions. Match the name to the
folder using lowercase letters, digits, and hyphens. The description should explain
the work and its trigger without claiming every coding task.

Include only guidance that improves decisions: relevant inputs, meaningful steps,
actual invariants, completion evidence, and stopping conditions where needed.
Preserve user intent and authorization. A skill does not grant permission to publish,
message people, deploy, or mutate a live database. Do not create an approval ceremony
for ordinary authorized work or require subagents as a default.

Keep common guidance in the entrypoint. Add references, scripts, or templates only
when they serve a concrete recurring need, and link them where relevant. Make each
skill usable when installed on its own; do not require a hidden sibling skill or a
tool that the target environment lacks. Use ordinary Markdown rather than agent
specific command interpolation in portable instructions.

Validate frontmatter, links, and any scripts. Try realistic positive and negative
trigger prompts and inspect outputs on an isolated permitted task when useful.
Record structural validation separately from demonstrated behavioral effectiveness.
Revise from actual failures rather than growing a universal checklist.

Reference: [Agent Skills specification](https://agentskills.io/specification).
