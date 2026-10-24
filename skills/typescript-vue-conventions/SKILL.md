---
name: typescript-vue-conventions
description: Write or review intentional TypeScript and Vue code using the project's established conventions. Use for Vue components, composables, frontend state, and TypeScript boundaries; avoid unrelated framework migrations or style rewrites.
---

# TypeScript and Vue conventions

Inspect Vue/TypeScript versions, nearby components, package scripts, tsconfig,
linting, formatting, and state management. Preserve established choices. For a new
Vue 3 component without an existing convention, prefer a typed single-file component
using Composition API and `<script setup lang="ts">`.

## TypeScript

- Preserve strict checking. For a new project, propose strict mode; fix existing
  repositories within the requested scope rather than triggering a global migration.
- Use inference for obvious local values and explicit types at public or external
  boundaries where they clarify a contract. Treat untrusted data as `unknown`, then
  validate and narrow it. A type assertion does not validate network data.
- Prefer a small concrete type over a generic framework. Model mutually exclusive
  states with discriminated unions when it removes impossible combinations. Follow
  the repository's type/interface convention; do not churn equivalent declarations.
- Avoid `any`, non-null assertions, and suppressions used to hide uncertainty.
  A necessary escape hatch should be local with a concrete justification.

## Vue

- Type props and emitted events. Keep inputs flowing down and changes explicit
  through events or the existing model convention. Avoid mutating props or silently
  sharing mutable state between component instances.
- Use computed values for derived state. Use watchers for effects that actually
  depend on reactive changes; handle invalidation and stale async responses when
  they can overwrite newer state. Clean up subscriptions and timers.
- Keep state local until multiple owners need it. Reuse the current store when
  appropriate; do not introduce a store for a single form or component.
- Extract a composable for reusable stateful behavior or a meaningful independent
  responsibility. Keep a one-use pure calculation as a simple function when clearer.
- Include loading, empty, failure, and success states when reachable. Use semantic
  controls, labels, stable list keys, and keyboard behavior.

Test observable rendering and events with the existing runner; for new Vue tooling,
consider Vitest and Vue Test Utils. Use existing type-check, lint, and build scripts;
template checking may require `vue-tsc`. Avoid installing tools already provided.

References: [Vue typed Composition API](https://vuejs.org/guide/typescript/composition-api.html),
[Vue testing](https://vuejs.org/guide/scaling-up/testing),
[TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html),
[strict mode](https://www.typescriptlang.org/tsconfig/strict.html).
