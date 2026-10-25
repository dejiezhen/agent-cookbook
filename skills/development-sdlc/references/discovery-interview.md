# Interview an idea into a buildable plan

Use for a new product, substantial unresolved direction, or an explicit request to
be challenged before building. Explore deeply where answers change the outcome;
do not measure thoroughness by question count. Small understood changes use the
short spec flow instead. This mode produces decisions and a plan, not a second
workflow coordinator.

## Start from what is known

Inspect available product docs, specs, code, tests, and tooling first. Identify the
current product, intended next milestone, and existing decisions. Distinguish a new
product from a feature or next milestone of an existing one. Do not ask the user to
repeat documented rules or replace an established stack with personal defaults.
Confirm only facts that conflict, appear obsolete, or materially affect the request.

Ask a small batch, usually one to three connected questions, then adapt to the
answers. Start with the problem and user outcome before choosing technology.
If the user does not know, explain a reasonable recommendation and its tradeoffs.
Keep confirmed decisions, proposals, assumptions, and unanswered questions distinct.

## Probe the decisions that affect this build

Use the relevant topics below as prompts, not a questionnaire to dump all at once:

| Topic | Useful questions |
| --- | --- |
| Problem and audience | Who experiences the problem, in what situation, and how often? What do they do today, and what fails about it? |
| Outcome and evidence | What would become easier or better? What observable behavior or feedback would show the first version worked? |
| First useful scope | What is the smallest complete user journey? Which requested capabilities are essential now, and what can wait? |
| Behavior and edge cases | Walk through a concrete successful example. What should happen for invalid input, missing data, cancellation, or repeated actions where relevant? |
| Data and authority | What data is stored, where does it originate, and who can read/change it? Are identity, tenant isolation, sensitive data, retention, or deletion requirements actually involved? |
| Technology and integrations | What already exists and must remain compatible? Which stack choices are requirements versus preferences? What capabilities justify external services, AI, or background work? |
| Style and interaction | Which existing visual/code conventions apply? For a new UI, what character, reference examples, interaction needs, or accessibility constraints could change the design? |
| Operating constraints | What are the delivery budget/timeline, hosting constraints, expected workload, and relevant reliability, accessibility, latency, cost, or recovery needs? |
| Delivery and validation | Who will try the first slice, on which devices, and how will feedback be collected? What testing, publishing, migration, or operational work is necessary for this milestone? |

For an AI feature, also establish which choices need a model, allowed tool effects,
authoritative success/failure evidence, trust boundaries, and evaluation/cost limits.
For a game, clarify the core loop, players, session length, fairness/content policy,
replay/progression, and intended playtesting where those are unsettled. Preserve
existing rules and scoring unless changing them is explicitly part of the request.
Skip conditional topics that do not affect the product. Do not request credentials
or real sensitive records to write a plan.

## Challenge with concrete tradeoffs

Ask why a proposed feature is needed and what happens without it. Use a realistic
example to expose conflicting rules, hidden users, and ambiguous words such as
"easy," "secure," or "real-time." Explain a contradiction and offer viable choices;
do not silently pick a business rule. Prefer a simple existing capability when it
satisfies the outcome. Do not turn speculative scale into queues, caches, accounts,
or provider abstractions without a requirement.

Research current official documentation when a recommendation depends on changing
API behavior, limits, or compatibility. Mark unverified facts. When a material
unknown needs experimentation, propose a bounded investigation with a question,
completion check, and effect on the plan. A planning request does not authorize
executing external calls or building that experiment.

## Finish with an actionable handoff

Summarize decisions after useful rounds, invite correction, and ask the next questions
that could change the plan. Do not treat silence as an answer. Continue independent
inspection or planning while waiting; do not implement work dependent on an unresolved
material decision.

Use the [spec and plan template](../assets/spec-and-plan.md) in the project's existing
document convention. Capture the problem/audience, success evidence, first milestone,
scope/non-goals, behavior and acceptance/test map, stack decisions with reasons,
the [style guide](style-guide.md), important data/interfaces, risks/open questions,
and ordered cohesive tasks. Each
task needs criterion IDs, dependencies, context, and a completion check. Distinguish
verified commands/paths from proposed ones. Identify the first end-to-end slice and
which tasks can start versus require an answer; another agent should need no chat
history to understand the plan.

Finish interviewing when the first milestone is testable, material choices are
resolved or visibly block specific work, and the user outcome remains coherent.
Keep future optional decisions deferred. If only a plan was requested, deliver it
without coding. If the user already authorized planning and building, proceed with
ready work under that authorization once dependent decisions are answered; do not
introduce a ritual approval gate.
