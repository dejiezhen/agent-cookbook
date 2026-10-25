# Vue decisions and failure cases

Read when changing reactivity, asynchronous effects, or version-sensitive macros.
Preserve local conventions and the supported framework version.

## Version matters

| Choice | Decision |
| --- | --- |
| Destructuring `defineProps` | Vue 3.5+ supports compiler-assisted reactive destructuring in the same script-setup block; older versions require a different pattern |
| Passing a prop into a watcher/composable | Preserve the reactive source with a getter or suitable ref; passing its current primitive value can lose updates |
| `onWatcherCleanup` | Vue 3.5+; register synchronously before awaiting |
| `defineModel` | Vue 3.4+; use the project's existing model convention when appropriate |
| `shallowRef` | Useful when nested values need not be reactive and updates replace the value; deep mutations will not trigger updates through it |

Do not mechanically replace every `ref` with `shallowRef`, or ban a supported feature
because another author's skill prefers a different style.

## Async search: latest request owns the UI

A user searches for A and then B. B completes first; A completes later. The UI must
retain B. Scope cleanup to the watcher and prevent an invalidated response or its
error/loading handler from overwriting current state. Cancellation can reduce work;
ownership of the active result still matters. Reuse the existing request abstraction
when it handles these semantics.

Test reversed completion order, failure, and unmount/cancellation when relevant.
Use controlled promises or the existing network test layer; arbitrary sleeps make
the test harder to trust.

## State location

A form draft used by one component can stay local. A shared authenticated workspace
selection can belong in the existing application store. A composable earns its role
through reusable behavior or a coherent responsibility, not a fixed line-count rule.

References: [Vue script setup](https://vuejs.org/api/sfc-script-setup.html),
[watcher cleanup](https://vuejs.org/guide/essentials/watchers.html).
