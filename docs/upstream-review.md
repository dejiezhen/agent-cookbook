# Review of upstream engineering skills

Reviewed 2026-10-24 by reading the skill files themselves. The rows below record
design influences and original additions. The subsequently requested subagent
workflow is a modified adaptation recorded separately below. Repository license
labels describe the inspected root license, not every file in every collection.

| Source at inspected revision | Useful addition here | Boundary retained here |
| --- | --- | --- |
| [Superpowers TDD](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/test-driven-development/SKILL.md) and [verification](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/verification-before-completion/SKILL.md) | Ensure a regression assertion distinguishes the bug, and align each completion claim with relevant evidence | Preserve existing user code; avoid automatic deletion or rerunning unchanged checks simply to satisfy a ritual |
| [Superpowers debugging](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging/SKILL.md) | Trace the first failing component boundary and compare observations across layers | Redact diagnostics; investigate with judgment instead of a universal fixed number of attempts |
| [Sentry review](https://github.com/getsentry/skills/blob/d12f250460ffd961f549dbebf7eeb0cf4afd4c2e/skills/code-review/SKILL.md) and [find bugs](https://github.com/getsentry/skills/blob/d12f250460ffd961f549dbebf7eeb0cf4afd4c2e/skills/find-bugs/SKILL.md) | Trace existing protections, inspect query behavior, and disclose truncated or partial review coverage | Apply relevant risk checks; avoid a mandatory full security checklist for every file or Sentry-specific escalation rules |
| [Anthony Fu Vue](https://github.com/antfu/skills/blob/8886fe2d385d3644cbb47e46ae9cb1cf09307d3b/skills/vue/SKILL.md) and [reactivity reference](https://github.com/antfu/skills/blob/8886fe2d385d3644cbb47e46ae9cb1cf09307d3b/skills/vue/references/core-new-apis.md) | Focused conditional references for watcher cleanup, reactivity depth, and typed component boundaries | Respect supported Vue versions and project conventions; author preferences are not universal framework restrictions |
| [Trail of Bits property-based testing](https://github.com/trailofbits/skills/blob/196a9073ab10d35bacf111f945e02c00b2c6883a/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | Consider generated cases for real invariants and check for weak assertions or vacuous input filtering | Integrate test-design guidance into TDD rather than adding another always-relevant skill or dependency |

## License records

- Superpowers: [MIT at the inspected revision](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/LICENSE).
- Sentry: [Apache-2.0 at the inspected revision](https://github.com/getsentry/skills/blob/d12f250460ffd961f549dbebf7eeb0cf4afd4c2e/LICENSE).
- Anthony Fu: [MIT root license at the inspected revision](https://github.com/antfu/skills/blob/8886fe2d385d3644cbb47e46ae9cb1cf09307d3b/LICENSE.md);
  the collection includes generated and upstream-sourced material.
- Trail of Bits: [CC BY-SA 4.0 root license at the inspected revision](https://github.com/trailofbits/skills/blob/196a9073ab10d35bacf111f945e02c00b2c6883a/LICENSE).

The original additions incorporate general methods in independently written
instructions and examples. Any adapted files need their own source/notice record;
the library's MIT license does not replace third-party terms.

## Combined subagent workflow

The user selected Superpowers' subagent-driven development as the implementation
coordinator. The [adapted skill](../skills/subagent-driven-development/SKILL.md)
bundles role prompts, plan/ledger templates, and review/recovery guidance. Its
[source record](../skills/subagent-driven-development/UPSTREAM.md) and
[license](../skills/subagent-driven-development/LICENSE) travel with an installation.

Spec-driven development now supplies requirements and task plans. Code review and
verification remain usable independently and provide standards within the assigned
roles; they do not dispatch another pipeline. TDD and language conventions stay
focused on how to implement. The product-facing agent skills retain their separate
purpose. This combines coordination while preserving useful standalone workflows.

## What the comparison says about length

Upstream skills vary widely: some are concise routers to supporting references;
others use repeated rules and long example lists. Our selection criterion is whether
an addition helps a plausible decision or prevents a concrete failure. The substantive
gap in the starter library was examples and behavioral evidence, not a uniform lack
of words. See [skill quality](skill-quality.md) for the resulting structure and limits.
