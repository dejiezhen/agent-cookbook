# Repository specification

Create a portable, curated library for full-stack development with Vue, TypeScript,
Python, and PostgreSQL. The preferred implementation workflow is **spec → red →
green → refactor → verify**. Support local Codex, Claude Code, and Cursor projects.

## Acceptance criteria

- Each original skill has a focused trigger, an actionable workflow, and a concrete
  outcome. Each skill folder contains valid `SKILL.md` frontmatter and Codex UI metadata.
- Specs identify observable acceptance criteria before implementation. New behavior
  is implemented through small failing-test/passing-test cycles. Existing user work
  is preserved; a missed test-first step is reported honestly without deleting work.
- A curated source catalog links to primary upstream projects, explains their use,
  and distinguishes references from vendored content. No upstream skill is copied.
- A selected skill can be copied into the chosen agent's project directory. Preview
  is the default; writes require `--apply`. Existing destinations, unknown names,
  traversal, and overlapping source/destination paths are rejected before copying.
- Validation rejects invalid manifests, folder/name mismatches, missing local Markdown
  references, invalid UI metadata, and symlinks inside distributed skills.
- Tests exercise installer behavior in temporary directories, including preservation
  of existing content and references. Validation and tests run in CI.
- The local Git repo is prepared for public publication without local absolute paths,
  credentials, environment files, or third-party source copied into the repository.

## Scope

Instructions and small management utilities; no framework bootstrap, database
execution, global agent configuration changes, or automatic upstream installation.
Public GitHub publication is requested. GitHub account: `dejiezhen`; repository name:
`agent-cookbook`.

## Validation limits

Structural checks and scenario prompts do not establish agent effectiveness.
Real tasks should be compared with and without a skill before calling it proven.
