# Skill evaluation prompts

The scenarios below are evaluation prompts; completed executions are recorded
separately at the end. Structural validation and utility tests are automated
separately. Use an isolated disposable project and permitted resources; avoid live
data and services.

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
| subagent-driven-development | Execute a multi-task implementation plan with fresh workers and independent review | Write only a spec, change one label, or build a runtime agent product |

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
10. **Subagent coordination:** Execute two independent utility tasks in an isolated
    Git repository. Check distinct task workers, independent task reviews, an integrated
    review, observed TDD evidence, a durable ledger, and preservation of user-owned
    files. Resume a recorded stage rather than repeating completed work. Verify the
    skill can be installed with its required prompts, templates, and license intact.

Record the agent/version, prompt, fixture revision, selected skill revision,
observable outcome, and failures. Compare against the same task without the skill
when practical. Grade behavior and artifact quality, not phrase matching. Make narrow
revisions supported by observed failure, then rerun the relevant scenario.

## Recorded trial: combined subagent workflow

Date: 2026-10-24. An independent controller was given the adapted skill and a small
isolated Git repository, without this conversation's history. It was asked to execute
a supplied two-task plan using the skill as written. Exact model versions were not
captured; workers inherited the host's configured models without overrides.

The fixture contained a tag-normalization stub, a page-limit parser stub, one baseline
test, project instructions, and a user-owned note. The plan specified whitespace and
ASCII handling for normalization; the parser required a default, ASCII decimal syntax,
and the inclusive range 1–100. Standard library only; local commits allowed; external
services and publication prohibited. These were local fixture revisions, not commits
in this cookbook: baseline `e13a725`, task 1 `68b8bb5`, final `1eafba4`.

| Observation | Actual result |
| --- | --- |
| Task implementation | Two separate context-free implementers, run sequentially |
| Task review | Two fresh read-only reviewers; separate spec and quality verdicts approved |
| Integrated review | One fresh reviewer approved the complete base-to-final change |
| Task 1 TDD | Relevant stub RED; 7 focused tests GREEN; 8 total tests passed |
| Task 2 TDD | Relevant stub RED; 10 focused tests GREEN; final 18-test suite passed |
| Scope | Only the two utility modules and their new test files changed |
| Preservation | Existing note unchanged byte-for-byte; working tree clean |
| Recovery records | Briefs, reports, exact diffs, test logs, and a durable ledger retained |
| Standalone packaging | All 10 skill files copied unchanged; references valid and license retained |

The parent checked the controller's report, integrated-review record, actual Git
diff/status, and preserved-note hash. There were no review findings, so fix-loop and
budget behavior were not exercised. Interrupted recovery and unavailable-subagent
fallback remain untested. There was no comparison against inline execution or an
unmodified upstream workflow; this is evidence of one functioning execution, not
proof of general effectiveness or a speed/cost improvement. Raw trial artifacts are
kept in the local workspace's ignored scratch area and are not distributed here.
