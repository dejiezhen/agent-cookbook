# TypeScript conventions

Inspect the supported version, runtime, `tsconfig`, package scripts, lint/format
settings, and nearby code. Follow established choices rather than triggering a
global migration for one feature.

- Preserve strict checking; prefer strict mode for a new project. Do not hide a
  contract problem with `any`, a non-null assertion, or a suppression. Keep necessary
  escape hatches local with a concrete reason. Indexed access can still be absent:
  respect actual runtime behavior and configured `noUncheckedIndexedAccess`.
- Infer obvious locals. Type public contracts and non-obvious values where that
  clarifies ownership. Treat untrusted data as `unknown`, validate at the boundary,
  and narrow before use; assertions and generated client types do not validate JSON.
- Model genuinely exclusive states with discriminated unions rather than unrelated
  flags. Handle relevant variants explicitly. Distinguish absent, empty, and invalid
  values according to the contract instead of using truthiness for all three.
- Prefer concrete types/functions over speculative generics, inheritance, or utility
  type frameworks. Follow local `type`/`interface` conventions without equivalent
  declaration churn. Share types for shared semantics, not coincidental shape.
- Make async outcomes and ownership explicit. Await work whose completion matters;
  handle intentional background failures and stale responses. Preserve cancellation
  and existing error conventions. A rejected promise is not an empty successful result.
- Keep module effects explicit and use supported module/import conventions. Do not
  add a runtime dependency when a type-only need or existing tool suffices.

Test observable behavior, valid/invalid input partitions, and meaningful async races
with the existing runner. Use configured lint/type/build checks; Vue templates may
need `vue-tsc` in addition to TypeScript checking. Do not install duplicate tooling.

References: [narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html),
[strict](https://www.typescriptlang.org/tsconfig/strict.html),
[indexed access checks](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html).
