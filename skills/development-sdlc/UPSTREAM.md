# Source and modifications

The subagent execution stage, role prompts, and review/recovery resources in this
skill are adapted from
[obra/superpowers: subagent-driven-development](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/subagent-driven-development),
revision `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`, reviewed 2026-10-24.

Upstream copyright: Copyright (c) 2025 Jesse Vincent. Distributed under the
[bundled MIT license](LICENSE). Local modifications: Copyright (c) 2026 dejiezhen.

## Intentional changes

- Retain fresh task implementers, independent spec/quality verdicts, an integrated
  final review, a progress ledger, scoped fix loops, and minimal dispatch context.
- Make the folder self-contained with bundled role prompts and plan/ledger templates.
  Replace upstream helper scripts and cross-skill requirements with direct Git and
  ordinary file operations; no executable upstream scripts are included.
- Require the user's spec → red → green preference for behavior changes, while
  preserving existing code and avoiding manufactured tests for prose.
- Apply local engineering and stack standards without duplicating orchestration.
- Consolidate requirements, TDD, review, verification, and stack standards under
  `development-sdlc`. Supporting modules are loaded by stage and affected stack;
  the coordinator explicitly passes their paths to implementers and reviewers.
- Honor host model configuration, available delegation tools, existing authorization,
  and project policies. Provide an honest inline mode when delegation is unavailable.
- Keep evidence useful through handoff; do not automatically delete recovery records.
- Bound fix loops while keeping unmet requirements visible. A review cap does not
  convert a known material defect into a completed task.

This is a maintained adaptation, not an unmodified upstream release. Consult the
pinned source before incorporating future upstream changes, retain its license,
and evaluate changes against this library's constraints.
