# Sources and useful upstream projects

Reviewed on **2026-10-23**. These are primary project repositories and official
documentation. Links are research references, not automatic installations or
claims that every upstream workflow has been audited or evaluated here.

## Developer collections

| Project | Why it is useful | How it fits this library |
| --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | Composable development workflows including TDD, debugging, planning, review, and verification | Closest match to spec and TDD interests; inspect its stronger process requirements before adopting the whole framework |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | A toolkit for carrying specifications through plans, tasks, implementation, and convergence | Consider for larger projects needing persistent artifacts; the short local spec skill keeps small changes light |
| [OpenAI skills](https://github.com/openai/skills) | Official Codex skill catalog and examples | Browse for tool-specific workflows beyond this library |
| [Anthropic skills](https://github.com/anthropics/skills) | Examples spanning development, testing, MCP, design, and documents | Study selected workflows; inspect each license because document skills have different terms |
| [Trail of Bits skills](https://github.com/trailofbits/skills) | Security auditing, differential review, static analysis, and testing workflows | Add selected security workflows when the project's risks call for them |
| [Vercel agent skills](https://github.com/vercel-labs/agent-skills) | Web interface guidance and framework-specific patterns | Web review ideas can help; React-specific rules should not be applied blindly to Vue |

The original skills in this repository express independently written, project-neutral
workflows. Upstream content has not been copied into skill folders. Before vendoring
anything later, record the exact source revision, applicable license, retained
notices, modifications, and the need that justifies maintaining a copy.

## Agent format and discovery

- [Agent Skills specification](https://agentskills.io/specification): folder layout,
  required frontmatter, naming, and progressive disclosure.
- [OpenAI local skill documentation](https://learn.chatgpt.com/docs/build-skills):
  Codex discovery in `.agents/skills`, invocation, and UI metadata.
- [Claude Code skills](https://code.claude.com/docs/en/skills): project discovery
  in `.claude/skills` and slash invocation. Cloud behavior can differ from local use.
- [Cursor skills](https://cursor.com/docs/skills): project `.agents/skills` and
  `.cursor/skills`, plus explicit invocation.

## Engineering and stack references

- [Google engineering practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html):
  design, functionality, useful tests, and avoiding unnecessary complexity.
- [Martin Fowler on TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html):
  test cases and the red → green → refactor process.
- [Vue and TypeScript](https://vuejs.org/guide/typescript/composition-api.html):
  typed component boundaries in Composition API.
- [Vue testing guide](https://vuejs.org/guide/scaling-up/testing) and
  [Vue Test Utils](https://test-utils.vuejs.org/guide/): choosing meaningful test levels.
- [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
  and [strict mode](https://www.typescriptlang.org/tsconfig/strict.html): narrowing
  uncertain inputs and retaining type checks.
- [PEP 8](https://peps.python.org/pep-0008/) and [PEP 20](https://peps.python.org/pep-0020/):
  readable Python and practical simplicity.
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html): resource
  ownership and test setup.
- PostgreSQL [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html),
  [ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html), and
  [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html):
  integrity and migration semantics. Use the project's server-version documentation.

Prefer maintained version-specific documentation over freezing framework API
snippets into a long-lived skill. Refresh links when updating a related workflow.
