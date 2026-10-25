# Migrate to Development SDLC

The library now has one development-cycle entrypoint, `development-sdlc`, with
supporting stage, engineering, and stack modules. These modules are ordinary
resources inside that folder, not separately discovered skills.

| Previous skill | Location within Development SDLC |
| --- | --- |
| spec-driven-development | [Spec and plan](../skills/development-sdlc/phases/spec-and-plan.md) |
| test-driven-development | [TDD](../skills/development-sdlc/phases/implement-tdd.md) |
| subagent-driven-development | [Subagent execution](../skills/development-sdlc/phases/subagent-execution.md), role prompts and recovery resources |
| code-review | [Review and verify](../skills/development-sdlc/phases/review-and-verify.md), review-only scope supported |
| verify-changes | [Review and verify](../skills/development-sdlc/phases/review-and-verify.md), verification-only scope supported |
| engineering-practices | [Engineering](../skills/development-sdlc/standards/engineering.md) and decision examples |
| typescript-vue-conventions | Separate [TypeScript](../skills/development-sdlc/standards/typescript.md) and [Vue](../skills/development-sdlc/standards/vue.md) modules |
| python-conventions | [Python](../skills/development-sdlc/standards/python.md) and boundary examples |
| postgres-migrations | [PostgreSQL](../skills/development-sdlc/standards/postgres.md), including query and transaction conventions |
| systematic-debugging | [Diagnosis](../skills/development-sdlc/references/debugging.md) and the preserved [boundary-tracing example](../skills/development-sdlc/references/boundary-tracing.md) |
| safe-refactoring | [Refactoring](../skills/development-sdlc/references/refactoring.md), linked from implementation |

## Existing installations

Updating this repository does not update copied skills in another project.

1. Preview, then install `development-sdlc` with the existing copy helper into your
   agent's chosen project skill directory. The installer will not overwrite a copy.
2. Compare any local changes in the retired folders listed above with the corresponding
   new modules. Preserve useful project-specific changes and source notices.
3. Once reconciled, move the old installed folders outside all agent discovery paths
   or remove their tracked copies through your normal review process. Keeping both
   versions active leaves competing workflows discoverable.
4. Replace explicit old skill invocations in project guidance with
   `$development-sdlc` or `/development-sdlc`, specifying plan-only or review-only
   scope when appropriate. Inspect changes before committing them.

No automatic deletion, global configuration update, or compatibility shim is
performed. Previous repository revisions retain the historical skill versions.
The Superpowers license and provenance now travel inside the new bundle.
