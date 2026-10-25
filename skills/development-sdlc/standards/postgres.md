# PostgreSQL conventions and migrations

Inspect the server version, actual schema, database access/migration tools,
transaction conventions, expected data size, and deployment order. Consult docs for
that version. Authoring a migration and testing disposable data do not authorize
running it against staging/production merely because credentials exist.

## Queries and integrity

Define the invariant and owner first. Parameterize values; use the driver's safe
identifier composition for dynamic identifiers. Enforce durable uniqueness, foreign
keys, and valid values with appropriate database constraints. Check null semantics
and existing data. An application pre-check alone cannot guarantee uniqueness under
concurrent writes.

Own multi-write transactions explicitly; define rollback and partial-failure behavior.
Inspect affected query count, result bounds, ordering/pagination, and concurrency
where relevant. Add indexes for demonstrated access patterns and verify significant
performance claims with plans/measurement on representative data. Avoid speculative
indexes, unbounded result sets, and caches that conceal a query problem.

## Schema and data changes

For rolling deployments, use expand → transition → contract when old/new code must
coexist. Do not require multiple phases for an isolated change without compatibility
or lock risk. Substantial backfills need bounded batches, restart behavior, transaction
size, and progress evidence.

Evaluate locks and rewrites for the exact operation/version. A concurrent index build
can reduce write blocking but has restrictions, may leave an invalid index on failure,
and cannot run inside a transaction block. Verify the migration framework supports
the required transaction mode. Set operation timeouts appropriate to the authorized
environment.

Test upgrades, constraints, affected application queries, rollback, and meaningful
concurrency cases on disposable PostgreSQL with representative valid/invalid data.
Mocks and SQLite do not establish PostgreSQL semantics. Rehearse recovery where
practical; a down migration does not automatically recover destroyed data. Deliver
verification, compatibility, recovery, and explicit destructive consequences with
the migration. State unavailable checks honestly.

References: [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html),
[ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html),
[CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html).
