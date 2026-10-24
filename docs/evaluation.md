# Skill evaluation prompts

These are **planned manual scenarios**, not completed agent evaluations. Structural
validation and utility tests are automated separately. Use an isolated disposable
project and permitted resources; avoid live data and services.

## Trigger checks

| Skill | Should match | Should not be selected solely for |
| --- | --- | --- |
| engineering-practices | Implement a small feature with intentional boundaries | Translate a paragraph |
| spec-driven-development | Clarify and implement new archival behavior | Fix Markdown spacing |
| test-driven-development | Add a specified validation rule with tests first | Edit a project description |
| typescript-vue-conventions | Add typed props and loading states to a Vue form | Modify a Python-only script |
| python-conventions | Simplify a Python module and its error handling | Modify a Vue-only component |
| systematic-debugging | Reproduce an intermittent stale response | Draft an unimplemented feature spec |
| code-review | Review a diff for defects and unnecessary complexity | Translate source comments |
| safe-refactoring | Consolidate a duplicated domain rule without behavior changes | Add a new user capability |
| verify-changes | Check that a proposed fix satisfies its acceptance criteria | Summarize a research article |
| api-contracts | Change a Python endpoint consumed by TypeScript | Rename a CSS class |
| postgres-migrations | Add a constraint while keeping existing data valid | Change a component label |
| web-accessibility | Fix keyboard and focus behavior in a dialog | Tune a database query |
| performance-investigation | Diagnose a measured slow endpoint | Preemptively add a cache |
| write-skills | Capture a recurring test setup workflow | Complete a one-time test run |

Multiple skills can legitimately apply. Evaluate whether selection adds useful
guidance; do not require all plausible skills to be invoked.

## Behavioral trials

1. **Small feature:** In a minimal Vue/Python fixture, request an archive toggle.
   Check concise acceptance criteria, a relevant observed red, green implementation,
   useful failure handling, and no speculative framework or state store.
2. **Preserve work:** Provide partially implemented behavior and ask for TDD coverage.
   Check that the agent preserves existing changes, reports the missed test-first
   order, and does not delete implementation to manufacture a red.
3. **Database integrity:** In disposable Postgres, ask for unique identifiers with
   dirty seed data. Check that the agent accounts for data cleanup, real constraints,
   actual migration semantics, and live-environment authorization boundaries.
4. **Intentional refactor:** Give two similar functions with different domain rules.
   Check that the agent reasons about ownership instead of creating a generic
   abstraction merely to remove similar lines.

Record the agent/version, prompt, fixture revision, selected skill revision,
observable outcome, and failures. Compare against the same task without the skill
when practical. Grade behavior and artifact quality, not phrase matching. Make narrow
revisions supported by observed failure, then rerun the relevant scenario.
