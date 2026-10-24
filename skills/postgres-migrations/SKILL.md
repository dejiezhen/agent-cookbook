---
name: postgres-migrations
description: Prepare and test PostgreSQL schema or data migrations with attention to integrity, locks, compatibility, and recovery. Use for migration authoring and review; executing against a live database requires authorization for that environment.
---

# Postgres changes with explicit consequences

Inspect the supported server version, actual schema, migration framework, table
size estimates, deployment order, and transaction conventions. Separate authoring
and disposable-environment verification from executing a live migration.

Define the invariant and expected application behavior first. Use database
constraints for durable uniqueness, relationships, and valid values. Check null
semantics and existing data before adding restrictions. A pre-insert application
check alone cannot guarantee uniqueness under concurrent requests.

For a rolling deployment, consider an expand → transition → contract sequence when
old and new code must coexist. Do not impose multiple phases on a small isolated
table when no compatibility or lock risk requires them. For substantial backfills,
define bounded batches, restart behavior, transaction size, and progress evidence.

Evaluate locks and rewrites for the server version and exact operation. A concurrent
index build can reduce write blocking but has limitations, can leave an invalid
index after failure, and cannot run inside a transaction block. Verify the migration
framework can express the required transaction behavior. Use lock/statement timeout
settings appropriate to the authorized environment and operation.

Test on disposable Postgres with representative valid and invalid data. Exercise
upgrade behavior, affected application queries, and meaningful concurrency or
constraint cases. Rehearse recovery where practical. Distinguish a reversible schema
change from restoring destroyed data; a down migration is not automatically recovery.

Deliver the migration, verification, deployment compatibility, and recovery approach.
Flag destructive operations explicitly. Do not run against production or staging
merely because a connection string is present.

References: [ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html),
[CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html),
[constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).
Consult the documentation matching the project's server version.
