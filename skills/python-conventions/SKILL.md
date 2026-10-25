---
name: python-conventions
description: Write or review readable, idiomatic Python with focused types, explicit errors, small modules, and useful tests. Use for Python application or library changes while preserving existing framework and tooling conventions.
---

# Python conventions

Inspect the supported Python version, `pyproject.toml`, dependency manager,
format/lint/type-check settings, and nearby tests. Work within these choices. Avoid
introducing a second package manager or formatter for a local change.

For validation boundaries, error translation, or choosing a function versus a class,
read [boundary examples](references/boundary-examples.md).

- Use descriptive `snake_case` functions/variables and `PascalCase` classes, grouped
  imports, and the configured formatter. Prefer straightforward loops, comprehensions,
  and early returns that a maintainer can read quickly.
- Start with functions and small modules. Use a dataclass for a genuine data object;
  use a class for meaningful state or behavior. Add protocols, inheritance, factories,
  or dependency injection machinery only for a concrete seam or variation.
- Annotate public boundaries and non-obvious values using syntax supported by the
  target version. Keep local inference. Validate untrusted runtime data explicitly;
  annotations alone do not enforce a contract. Reuse existing validation tools.
- Avoid mutable defaults and unintended shared state. Use context managers for
  resources. Keep significant I/O and setup out of import-time execution.
- Catch specific exceptions where recovery or translation belongs. Preserve causes
  when translating errors. Do not swallow unexpected failures or return a success
  shaped default after a failed operation. Log where an error becomes actionable,
  avoiding duplicate reports and sensitive payloads.
- Choose sync or async to fit the surrounding stack and workload. Do not introduce
  async for a pure function, or block an event loop with known blocking I/O.
- Keep SQL parameterized and transaction ownership explicit. Let database constraints
  enforce durable invariants; avoid check-then-insert races.
- Test new behavior through spec → red → green. With pytest, use small fixtures,
  parameterization for meaningful cases, and isolated external resources. Patch at
  the consumed boundary; avoid mocking the function whose behavior is under test.

Run configured checks appropriate to the changed paths. Reuse Ruff, Black, mypy,
Pyright, or another existing tool rather than imposing a universal tool list. Explain
only conventions that affect this change; skip unrelated cleanup and docstrings
that merely repeat a function name.

References: [PEP 8](https://peps.python.org/pep-0008/),
[PEP 20](https://peps.python.org/pep-0020/),
[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html).
