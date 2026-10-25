# Skill evaluation prompts

The scenarios below are evaluation prompts; completed executions are recorded
separately at the end. Structural validation and utility tests are automated
separately. Use an isolated disposable project and permitted resources; avoid live
data and services.

## Trigger checks

| Skill | Should match | Should not be selected solely for |
| --- | --- | --- |
| development-sdlc | Specify/implement a feature, fix a regression with TDD, or perform requested code review/verification | Translate a paragraph, run a model benchmark, or research a topic without a code change |
| systematic-debugging | Reproduce an intermittent stale response | Draft an unimplemented feature spec |
| safe-refactoring | Consolidate a duplicated domain rule without behavior changes | Add a new user capability |
| api-contracts | Change a Python endpoint consumed by TypeScript | Rename a CSS class |
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
10. **Subagent coordination:** Execute two independent utility tasks in an isolated
    Git repository. Check distinct task workers, independent task reviews, an integrated
    review, observed TDD evidence, a durable ledger, and preservation of user-owned
    files. Resume a recorded stage rather than repeating completed work. Verify the
    skill can be installed with its required prompts, templates, and license intact.
11. **Stage and stack routing:** Request only a full-stack plan and then only a Vue
    review. Check that planning loads affected Vue/TypeScript/Python/PostgreSQL
    standards, stops before implementation, and review keeps product files unchanged.
    In Python-only work, an unrelated Vue dependency must not force loading Vue.
    Check that actual task workers and reviewers receive and read selected modules.

Record the agent/version, prompt, fixture revision, selected skill revision,
observable outcome, and failures. Compare against the same task without the skill
when practical. Grade behavior and artifact quality, not phrase matching. Make narrow
revisions supported by observed failure, then rerun the relevant scenario.

## Recorded trial: combined subagent workflow

Historical trial before consolidation into Development SDLC; it does not by itself
validate the new entrypoint or its stage/stack routing.

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

## Recorded trial: Development SDLC scope and stack routing

Date: 2026-10-24. A context-free evaluator received a standalone installation of
`development-sdlc` and a disposable repository, then two sequential user requests:
a full-stack archive plan only, followed by a Vue diff review only. Host model
defaults were inherited; the resolved model version was not captured.

Tested bundle SHA-256: `122cf0eedbb019bd8c232670cbf6a73bb73fd6310ffc1348d992477b46ecb8f7`.
Computed from sorted relative file paths followed by NUL, file bytes, and NUL for
every distributed file, independent of its installation location.

The fixture contained Vue 3.5.13/TypeScript configuration, a Python service boundary,
a PostgreSQL schema, a user note, and an existing uncommitted search-component change.
Its local baseline was `4078a8f`. No networking, installation, implementation,
external service, publication, or delegation was permitted.

| Observation | Actual result |
| --- | --- |
| Planning scope | One spec, acceptance/test map, and five cohesive tasks; no implementation |
| Full-stack routing | Engineering, TypeScript, Vue, Python, and PostgreSQL modules read |
| Review scope | Complete existing Vue diff reviewed; only engineering/TypeScript/Vue applied |
| Version awareness | Supported Vue 3.5 reactive props destructuring was not flagged |
| Findings | Stale async results/loading ownership and missing local failure state reported |
| Discriminating check | Controlled promises in the extracted watcher callback reproduced the defects |
| Preservation | All eight product-file hashes and recorded Git state unchanged; only ignored reports created |
| Standalone packaging | All 23 installed bundle files matched the candidate byte-for-byte, including license |

The parent inspected the reports and findings and independently checked the original
dirty-file set, unchanged fixtures, and installed-bundle equality. The callback probe
did not mount Vue, run compiler macros, or test browser behavior. Planned archive
tests and PostgreSQL operations were not executed. This establishes one scoped use
of the new routing; it is not evidence of general effectiveness or host portability.
Raw reports remain in local scratch, outside the distributed repository.

## Recorded trial: Development SDLC implementation

Date: 2026-10-24. A separate context-free controller received the same standalone
23-file bundle/fingerprint recorded above, an isolated repository with two Python
stubs, and behavioral requirements without a prewritten plan. Baseline `b5fdbb4`;
local task commits `1b855cc` and `100e321`. Host model defaults were inherited;
resolved model versions were not captured. Standard library only; local task-owned
commits permitted; networking, installation, and publication prohibited.

The request required a defaulted ASCII-decimal page size bounded to 1–200 and stable
exact-string ID deduplication supporting one-shot iterators without input mutation.
The fixture also had an unrelated Vue dependency and a pre-existing uncommitted note.

| Observation | Actual result |
| --- | --- |
| Spec and plan | Controller derived one authoritative spec, acceptance/test map, and two task briefs |
| Implementers | Two fresh context-free workers, sequential execution |
| Task reviews | Two separate fresh reviewers; specification compliant, quality approved |
| Integrated review | Fresh reviewer approved the entire four-file base-to-final change |
| Module routing | Both implementers and all reviewers read supplied engineering/Python modules and relevant stage/role instructions |
| Unrelated stack | Vue/TypeScript/PostgreSQL modules stayed unloaded for Python-only work |
| TDD evidence | Page-size slices observed relevant RED then GREEN; 8 focused tests passed. Deduplication observed stub RED then GREEN; 5 focused tests passed |
| Final checks | Required full suite passed all 14 tests on Python 3.13.4; unchanged evidence reused during review |
| Scope/preservation | Only two modules and two test files committed; original note bytes and dirty status preserved; no dependencies added |
| Recovery artifacts | Spec, briefs, exact diffs, reports, logs, and ledger retained in ignored scratch |

One overlapping dispatch hit the shared agent limit; fresh dispatch succeeded after
the current review finished. No implementation workers overlapped, identities were
not reused, and no inline fallback was needed. No review findings required fixes.
The parent inspected the reports, integrated review, and test log and independently
verified exact changed paths, final commit, and original note/status preservation.

This exercised requirements through final verification, including explicit standards
handoff. It did not exercise interrupted recovery, fix-budget exhaustion, unavailable
delegation fallback, live services, or full-stack implementation. No baseline speed,
cost, or effectiveness comparison was performed. These small fixtures establish
working paths, not a reason to use subagents for every small change. Raw artifacts
remain in local scratch and are not distributed.
