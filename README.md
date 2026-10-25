# Agent cookbook

Portable skills for **intentional Vue, TypeScript, Python, Postgres, and AI agent development**.
The default implementation workflow is **spec → red → green → refactor → verify**.

Keep changes small enough to explain and complete enough to satisfy the requirement.
Reuse existing conventions. Add abstractions, dependencies, and configuration for a
demonstrated need. Treat correctness, accessibility, security, and data integrity as
part of the behavior where relevant.

This library contains 18 original skills and a [curated source catalog](docs/sources.md).
It is a focused starting point, not an exhaustive index of every agent skill.

## Start with these

| Skill | What it contributes |
| --- | --- |
| [Engineering practices](skills/engineering-practices/SKILL.md) | Design decisions, explicit boundaries, intentional scope |
| [Spec-driven development](skills/spec-driven-development/SKILL.md) | Observable acceptance criteria before implementation |
| [Test-driven development](skills/test-driven-development/SKILL.md) | Small, observed red → green → refactor cycles |
| [TypeScript / Vue conventions](skills/typescript-vue-conventions/SKILL.md) | Types, component ownership, reactivity, focused tests |
| [Python conventions](skills/python-conventions/SKILL.md) | Readability, errors, types, resources, focused modules |

## Tool-using agents and automation

| Skill | What it contributes |
| --- | --- |
| [Agent design](skills/agent-design/SKILL.md) | Choose simple control flow, bound runs, and handle interruption |
| [Agent tool design](skills/agent-tool-design/SKILL.md) | Explicit tool schemas, outcomes, authorization, and retry semantics |
| [Agent evaluation](skills/agent-evaluation/SKILL.md) | Measure task outcomes, unintended effects, recovery, cost, and latency |
| [Agent safety](skills/agent-safety/SKILL.md) | Preserve trust boundaries around external content and actions |

For AI features, apply TDD to deterministic code and use task-specific evaluations
for model behavior. A passing adapter test does not establish reliable tool choice
or a correct external outcome. Evaluation and tool-contract templates are included
inside their respective skills. No live model calls are needed to use this library.

## Add when useful

| Skill | When to use it |
| --- | --- |
| [Systematic debugging](skills/systematic-debugging/SKILL.md) | Diagnose a failure before changing code |
| [Code review](skills/code-review/SKILL.md) | Find supported defects and unnecessary complexity |
| [Safe refactoring](skills/safe-refactoring/SKILL.md) | Simplify a concrete structure while preserving behavior |
| [Verify changes](skills/verify-changes/SKILL.md) | Match completion claims to actual execution evidence |
| [API contracts](skills/api-contracts/SKILL.md) | Align TypeScript clients and Python service boundaries |
| [Postgres migrations](skills/postgres-migrations/SKILL.md) | Constraints, compatibility, locks, backfills, recovery |
| [Web accessibility](skills/web-accessibility/SKILL.md) | Forms, dialogs, status updates, keyboard interaction |
| [Performance investigation](skills/performance-investigation/SKILL.md) | Measure a bottleneck and validate a targeted improvement |
| [Write skills](skills/write-skills/SKILL.md) | Capture a repeated workflow without growing a catchall |

## Install selected skills into a project

Requires Python 3.10+ for the copy helper; running the skills themselves depends on
the target project's tools. Clone this repo, then preview a selected installation:

```sh
git clone https://github.com/dejiezhen/agent-cookbook.git
cd agent-cookbook
python3 scripts/install_skills.py --dest ../your-project/.agents/skills --skills engineering-practices spec-driven-development test-driven-development typescript-vue-conventions python-conventions
```

Add `--apply` to copy after reviewing the preview. Existing skill folders are never
overwritten. To update an installation, compare the tracked files and merge the
changes deliberately. Copying creates an independent snapshot; it does not auto-sync.

| Agent | Project destination | Explicit invocation |
| --- | --- | --- |
| Codex | `.agents/skills` | `$skill-name` in CLI / IDE |
| Claude Code | `.claude/skills` | `/skill-name` |
| Cursor | `.agents/skills` or `.cursor/skills` | `/` and select the skill |

For Claude Code, use the same helper with `--dest ../your-project/.claude/skills`.
Codex and Cursor can share one `.agents/skills` installation. Keep one installed
copy per agent's discovery path to avoid duplicate names. Instructions use the
[Agent Skills format](https://agentskills.io/specification); `agents/openai.yaml`
provides optional Codex UI metadata. Individual agents' discovery and execution
behavior can differ; see the [official installation references](docs/sources.md#agent-format-and-discovery).

No global configuration is changed by this repository. Install just the workflows
you expect to use; each skill is self-contained.

## Example task

In Codex, after installing the relevant skills:

```text
Use $engineering-practices, $spec-driven-development, and
$test-driven-development to add project archiving.
Write a short spec, then implement one behavior at a time with red → green.
Use $typescript-vue-conventions for UI changes and $python-conventions
for backend changes. Keep the diff tied to the acceptance criteria.
```

Use `/skill-name` when invoking the equivalent skills in Claude Code. This is a
portable instruction library, not a guarantee that every host will follow it.

## Maintain and validate

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests -v
```

The validator checks manifests, folder names, UI metadata, local Markdown links,
and distributable file structure. Tooling tests cover copying and preservation.
[Behavioral evaluation prompts](docs/evaluation.md) are provided for future trials;
passing structural checks does not prove that a skill improves agent performance.

## How much detail belongs in a skill?

Keep the entrypoint focused. Load examples and fragile, task-specific details from
references when relevant. Depth comes from concrete decisions, failure cases, and
tested outcomes, rather than a target word count. See [skill quality](docs/skill-quality.md)
and the [upstream review](docs/upstream-review.md) for the rationale and specific
ideas incorporated from open-source skill repositories.

See [preferences and next decisions](docs/preferences.md) for tailoring and
[contribution guidance](CONTRIBUTING.md) for adding skills. Original content is MIT
licensed; linked upstream projects retain their own licenses. No upstream skills
are vendored here.
