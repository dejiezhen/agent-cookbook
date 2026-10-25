# Vue conventions

Inspect Vue/TypeScript versions, component conventions, routing, stores, and test
tooling. For new Vue 3 code without an existing convention, prefer Composition API
in an SFC with `<script setup lang="ts">` when TypeScript is used. Preserve existing
APIs and avoid unrelated Options/Composition API rewrites.

- Type props and emitted events in TypeScript. Keep ownership explicit: inputs flow
  down; changes use events or the project's model convention. Avoid mutating props
  or unintentionally sharing mutable state across component instances.
- Use computed values for derived state and watchers for necessary effects. Clean
  up subscriptions/timers. In async effects, an obsolete request's result, error,
  or loading update must not overwrite the active request's state.
- Keep state local until multiple owners need it. Reuse the existing store where
  appropriate. Extract a composable for reusable stateful behavior or a coherent
  independent responsibility; a one-use pure calculation can remain a function.
- Provide reachable loading, empty, error, and success states. Use stable list keys,
  semantic controls, labels, and appropriate focus/keyboard behavior. UI visibility
  does not enforce server authorization.
- For SSR/Nuxt, check server/browser ownership, request-scoped state, and hydration
  before using browser globals or module-level mutable state.

Check versions before adopting or rejecting an API:

| Choice | Constraint |
| --- | --- |
| Reactive `defineProps` destructuring | Supported by Vue 3.5+ within the same script-setup block; preserve reactive sources when passing elsewhere |
| `onWatcherCleanup` | Vue 3.5+; register synchronously before awaiting |
| `defineModel` | Vue 3.4+; use the established model contract |
| `shallowRef` | Nested mutations do not trigger updates through it; useful when updates replace the value |

Read [Vue failure examples](../references/vue-decisions.md) for async ownership,
reactivity depth, or prop sources. Do not mechanically prefer shallow reactivity or
ban supported syntax because an upstream author's skill has another preference.

Test rendering and events through observable interactions. Use the existing runner;
Vitest and Vue Test Utils are candidates when establishing new tooling. Use real
browser checks for behavior component tests cannot establish, and configured
template/type/lint/build commands. Avoid snapshots that miss the required behavior.

References: [typed Composition API](https://vuejs.org/guide/typescript/composition-api.html),
[script setup](https://vuejs.org/api/sfc-script-setup.html),
[watcher cleanup](https://vuejs.org/guide/essentials/watchers.html),
[testing](https://vuejs.org/guide/scaling-up/testing).
