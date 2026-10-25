# Working preferences and tailoring

## Chosen defaults

- Full-stack development with Vue, TypeScript, Python, and PostgreSQL.
- Portable instructions for Codex, Claude Code, and Cursor.
- AI development focus: tool-using agents and automation.
- Spec → red → green → refactor, followed by verification of acceptance criteria.
- One `development-sdlc` skill owns requirements, spec/plan, TDD, review, and verification.
  New or ambiguous products can use a thorough adaptive discovery interview, with
  small rounds of questions and an implementation-ready handoff rather than a fixed
  questionnaire. Existing documented decisions are reused, not asked again.
  It loads stage and stack modules as needed. Small work stays inline; significant
  risk can add independent review without delegated implementation. For substantial
  work with useful task separation, its
  subagent execution stage coordinates fresh implementers, independent
  task review, and integrated review. Both workers and reviewers receive the standards.
- Apply YAGNI, KISS, DRY, modular design, high cohesion/low coupling, explicit contracts,
  and testable composition according to concrete requirements and failure costs.
- Intentional changes: solve the concrete requirement, preserve existing conventions,
  and justify new abstractions, dependencies, configuration, and files.
- Prefer focused tests that expose meaningful failures over test count or broad
  checklists. Keep security, accessibility, and data integrity where they belong.

## Decisions to make from actual projects

| Question | Why it changes a future skill |
| --- | --- |
| Vue 3 or Vue 2? SPA or Nuxt/SSR? | Component APIs, browser/server boundaries, test setup |
| FastAPI, Django, Flask, or another Python framework? | Routing, validation, transaction ownership, integration tests |
| SQLAlchemy/Alembic, Django ORM, or direct SQL? | Migration commands and query conventions |
| Which package managers and quality tools are already established? | Exact verification commands and lockfile handling |
| Where do applications run? | CI, deployment, rollback, observability workflows |
| Which failures recur: flaky tests, auth bugs, SQL performance, or UI state? | The most valuable next narrow skill |

Do not add framework-specific defaults until a real project resolves these choices.
Next useful candidates are a project-specific test runner skill, a CI diagnosis
skill, a focused authorization review, or an end-to-end user journey workflow.
Agent design, tool contracts, evaluation, and safety workflows are included. Tailor
their concrete tools, budgets, and acceptance cases from the first real project.
