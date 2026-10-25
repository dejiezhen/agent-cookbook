# Repository specification

Create a portable, curated library for full-stack development with Vue, TypeScript,
Python, and PostgreSQL. One `development-sdlc` entrypoint owns **requirements →
acceptance criteria and spec → task plan → red → green → refactor → review → verify**.
Support local Codex, Claude Code, and Cursor projects.

## Acceptance criteria

- Each original skill has a focused trigger, an actionable workflow, and a concrete
  outcome. Each skill folder contains valid `SKILL.md` frontmatter and Codex UI metadata.
- Specs identify observable acceptance criteria before implementation. New behavior
  is implemented through small failing-test/passing-test cycles. Existing user work
  is preserved; a missed test-first step is reported honestly without deleting work.
- A curated source catalog links to primary upstream projects, explains their use,
  and distinguishes references from adapted content. The requested Superpowers
  adaptation retains its source revision, license, and modification record.
- The integrated workflow loads supporting stage modules and engineering standards
  selectively. Vue, TypeScript, Python, and PostgreSQL routing follows affected
  behavior and supported versions. Both implementers and reviewers receive the
  applicable modules explicitly. No overlapping workflow entrypoints remain.
- Small understood work defaults to inline execution; significant risk can add
  independent review without delegated implementation. Substantial separable work
  uses one subagent coordinator for dispatch, progress, task review, fixes, and
  integrated verification. Task count alone does not justify delegation. Plan-only,
  review-only, and verification-only requests preserve their requested scope.
- Both task and final integrated findings require fixes, affected checks, and
  independent re-review against the delivered revision/patch. Resume preserves
  completed work and reconciles stopped/active writers before another writer starts.
- Unclear bugs use evidence-led diagnosis before a cause-level regression fix.
  Verification reuse accounts for relevant dependencies, configuration, schema/data,
  and environment inputs as well as source changes.
- Development SDLC is installable by itself with all required prompts, templates,
  and standards, honest inline fallback, and no hidden upstream plugin dependency.
- Engineering guidance applies YAGNI, KISS, DRY, modular design, explicit contracts,
  and relevant reliability practices without speculative layers or tooling.
- A selected skill can be copied into the chosen agent's project directory. Preview
  is the default; writes require `--apply`. Existing destinations, unknown names,
  traversal, and overlapping source/destination paths are rejected before copying.
- Validation rejects invalid manifests, folder/name mismatches, missing local Markdown
  references, invalid UI metadata, and symlinks inside distributed skills.
- Tests exercise installer behavior in temporary directories, including preservation
  of existing content and references. Validation and tests run in CI.
- The local Git repo is prepared for public publication without local absolute paths,
  credentials, or environment files. Third-party adapted material is recorded.

## Scope

Instructions and small management utilities; no framework bootstrap, database
execution, global agent configuration changes, or automatic upstream installation.
Public GitHub publication is requested. GitHub account: `dejiezhen`; repository name:
`agent-cookbook`.

## Validation limits

Structural checks and scenario prompts do not establish agent effectiveness.
Real tasks should be compared with and without a skill before calling it proven.
