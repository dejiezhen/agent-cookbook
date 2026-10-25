# Agent cookbook

Portable skills for **intentional Vue, TypeScript, Python, PostgreSQL, and AI agent
development**. Use **requirements → acceptance criteria and spec → task plan →
red → green → refactor → review → verify**.

Keep changes small enough to explain and complete enough to satisfy the requirement.
This library contains 11 skills: one integrated development workflow with an attributed
Superpowers adaptation, and ten complementary specialist skills. The
[source catalog](docs/sources.md) records useful upstream projects and official guidance.

## Start with Development SDLC

[development-sdlc](skills/development-sdlc/SKILL.md) owns the whole development cycle.
Invoke one skill; it loads the stage and stack guidance relevant to the task:

```text
development-sdlc/
  SKILL.md                 Entry point and routing
  phases/                  Spec/plan, TDD, subagent execution, review/verification
  standards/               Engineering, TypeScript, Vue, Python, PostgreSQL
  references/              Concrete decisions, test design, failure/recovery cases
  prompts/                 Implementer, task reviewer, integrated reviewer
  assets/                  Spec/plan and progress templates
  agents/openai.yaml       Optional Codex UI metadata
  LICENSE + UPSTREAM.md    Superpowers attribution and modifications
```

The engineering module applies **YAGNI, KISS, DRY, modular design, high cohesion and
low coupling, explicit contracts, and testable composition** to concrete decisions.
Shared business knowledge needs one owner; similar code with different purposes
can stay separate. New abstractions, dependencies, modules, and configuration need
a current reason. Correctness, security, accessibility, and data integrity remain
part of the behavior where relevant.

Stack routing uses the affected behavior, interfaces, files, configurations, and
supported versions. Vue with TypeScript loads engineering + Vue + TypeScript;
Python database work loads engineering + Python + PostgreSQL. Each delegated task
explicitly passes the applicable modules to its implementer **and reviewer**.
Unrelated modules stay unloaded.

For suitable multi-task work, one coordinator dispatches fresh sequential task
implementers, independent spec/quality review, and integrated final review. Small
or tightly coupled work stays inline. The bundle has all required prompts, templates,
and standards; it needs no sibling skill or upstream plugin. Actual subagent execution
depends on the host's available tools and permission to delegate. Planning-only,
review-only, and verification-only requests stay within their requested scope.

The previous nine workflow/convention skills have been consolidated. See the
[migration guide](docs/migration-development-sdlc.md) for old names and existing
installations. The [source record](skills/development-sdlc/UPSTREAM.md) and
[third-party notices](THIRD_PARTY_NOTICES.md) preserve the Superpowers attribution.

## Complementary specialists

These add relevant domain guidance when needed; they do not start another SDLC
coordinator. No specialist is required to install Development SDLC on its own.

| Skill | When useful |
| --- | --- |
| [Systematic debugging](skills/systematic-debugging/SKILL.md) | Reproduce and locate a failure before changing code |
| [Safe refactoring](skills/safe-refactoring/SKILL.md) | Simplify a concrete structure while preserving behavior |
| [API contracts](skills/api-contracts/SKILL.md) | Align clients, services, validation, and compatibility |
| [Web accessibility](skills/web-accessibility/SKILL.md) | Keyboard, focus, forms, dialogs, and status updates |
| [Performance investigation](skills/performance-investigation/SKILL.md) | Measure a bottleneck and validate a targeted improvement |
| [Write skills](skills/write-skills/SKILL.md) | Capture a recurring workflow without growing a catchall |
| [Agent design](skills/agent-design/SKILL.md) | Simple control flow, bounded runs, interruption and recovery |
| [Agent tool design](skills/agent-tool-design/SKILL.md) | Tool schemas, outcomes, authorization, duplicate-call semantics |
| [Agent evaluation](skills/agent-evaluation/SKILL.md) | Task outcomes, unintended effects, recovery, cost, and latency |
| [Agent safety](skills/agent-safety/SKILL.md) | Trust boundaries around external content and actions |

For AI features, use TDD for deterministic code and task-specific evaluations for
model behavior. A passing adapter test does not establish reliable tool choice or
a correct external outcome. The agent guides are provider-neutral instructions;
they do not execute API calls themselves.

## Install into a project

Requires Python 3.10+ for the copy helper. Preview an installation:

```sh
git clone https://github.com/dejiezhen/agent-cookbook.git
cd agent-cookbook
python3 scripts/install_skills.py --dest ../your-project/.agents/skills --skills development-sdlc
```

Add `--apply` to copy after reviewing the preview. Existing skill folders are never
overwritten. Copies are independent snapshots; compare and merge updates deliberately.
Include other skill names in `--skills` only when useful. No global configuration
is changed.

| Agent | Project destination | Explicit invocation |
| --- | --- | --- |
| Codex | `.agents/skills` | `$development-sdlc` |
| Claude Code | `.claude/skills` | `/development-sdlc` |
| Cursor | `.agents/skills` or `.cursor/skills` | `/` and select the skill |

Keep one installed copy per agent's discovery path to avoid duplicate names.
Instructions follow the [Agent Skills format](https://agentskills.io/specification).
Discovery and execution differ across hosts; see the
[official references](docs/sources.md#agent-format-and-discovery).

## Example task

```text
Use $development-sdlc to add project archiving. Define acceptance criteria,
implement with observed red → green → refactor, then review and verify.
Apply the relevant Vue, TypeScript, Python, and PostgreSQL standards.
Use subagents when the task boundaries justify them. Keep changes intentional.
```

## Maintain and validate

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests -v
```

Validation checks manifests, names, UI metadata, local Markdown links, and file
structure. Utility tests cover copying and preservation. See
[evaluation prompts and recorded trials](docs/evaluation.md) for behavioral evidence
and its limits. Structural checks alone do not establish agent effectiveness.

Keep the entrypoint focused and disclose detail progressively. Useful depth comes
from decisions, failure cases, and tested outcomes rather than a word target. See
[skill quality](docs/skill-quality.md), [upstream review](docs/upstream-review.md),
[preferences](docs/preferences.md), and [contributing](CONTRIBUTING.md).
Original content is MIT licensed; adapted material retains its attribution.
