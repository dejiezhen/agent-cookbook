# Python conventions

Inspect the supported Python version, framework, `pyproject.toml`, package manager,
formatter/linter/type checker, and nearby tests. Use that stack; avoid adding a
second package manager or formatter for a local change.

- Use descriptive `snake_case` functions/variables, `PascalCase` classes, grouped
  imports, and the configured formatter. Prefer readable loops, comprehensions,
  and early returns over clever compression.
- Start with functions and cohesive modules. Dataclasses suit actual data objects;
  classes suit meaningful state/lifecycle or behavior. Add protocols, inheritance,
  factories, or DI machinery for a real seam or variation rather than a test mock.
- Annotate public boundaries and non-obvious values with supported syntax. Preserve
  local inference. Runtime input still needs validation; reuse the existing schema
  boundary rather than adding validation at every layer.
- Avoid mutable defaults and unintended shared state. Use context managers for
  resources; keep significant I/O and setup out of import-time execution.
- Catch specific exceptions where recovery or translation belongs; preserve causes
  when translating. Keep unexpected programming failures visible. Separate no
  matching records from a failed query. Log where actionable, without duplicate
  reports or sensitive payloads.
- Choose sync/async for the surrounding stack and workload. Do not block an event
  loop with known blocking I/O or introduce async for a pure computation. Preserve
  cancellation and resource cleanup when handling background tasks.
- Parameterize SQL and make transaction ownership explicit. Use database constraints
  instead of check-then-insert for durable uniqueness. Read the
  [PostgreSQL module](postgres.md) when queries, transactions, or schema are affected.

Read [boundary examples](../references/python-boundaries.md) for parsing, error
translation, state ownership, and functions versus classes. Test behavior through
the TDD stage, using existing unittest/pytest conventions. With pytest, prefer small
fixtures and parametrization for meaningful partitions. Patch at the consumed
external boundary without mocking the behavior being specified.

Run configured checks for changed paths. Reuse Ruff, Black, mypy, Pyright, or the
actual existing tools; this list is not a required installation. Explain only
conventions that affect the change and avoid redundant docstrings/style cleanup.

References: [PEP 8](https://peps.python.org/pep-0008/),
[PEP 20](https://peps.python.org/pep-0020/),
[pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html).
