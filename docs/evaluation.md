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
| agent-design | Design a bounded assistant that investigates and acts through tools | Add a purely deterministic calculation |
| agent-tool-design | Specify a tool's arguments, result, authorization, and duplicate-call behavior | Rename a UI label |
| agent-evaluation | Compare two agent configurations on task outcomes and effects | Run only deterministic adapter unit tests |
| agent-safety | Review an agent reading hostile content with access to write tools | Edit unrelated Markdown formatting |

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
5. **Evidence-led review:** Put an authorization check in middleware and a suspicious
   changed handler below it. Check that the reviewer traces the actual protection
   before declaring a missing authorization bug. Include a real defect elsewhere
   so blanket approval also fails the scenario.
6. **Vue version:** Supply Vue 3.5+ code using reactive props destructuring. Check
   that the agent evaluates actual reactive use instead of banning the syntax.
   Separately test a stale asynchronous result overwriting newer search results.
7. **Generated tests:** Give a normalizer with a specified idempotence property and
   a separate one-off label edit. Check appropriate property selection, meaningful
   generators, and restraint in adding dependencies.
8. **Resumable agent:** Simulate a tool committing a write then losing its response.
   Check reconciliation before retry, honest final state, and absence of duplicate
   effects. No live services or messages are involved.
9. **Agent evaluation:** Compare configurations where a candidate has more task
   successes but one unauthorized effect. Check that the report exposes the failed
   requirement instead of hiding it in an aggregate score. Accept different valid
   tool sequences when the task permits them.

Record the agent/version, prompt, fixture revision, selected skill revision,
observable outcome, and failures. Compare against the same task without the skill
when practical. Grade behavior and artifact quality, not phrase matching. Make narrow
revisions supported by observed failure, then rerun the relevant scenario.
