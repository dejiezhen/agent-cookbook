---
name: api-contracts
description: Design or change an API contract shared by a TypeScript frontend and Python backend. Use for request/response schemas, validation, compatibility, and contract tests without introducing a new API framework by default.
---

# Define the API boundary

Inspect existing endpoints, schema generation, authentication, error formats, and
client code. Identify the consumer and the required behavior. Keep the current
framework and transport unless changing them is explicitly part of the task.

Specify requests, responses, errors, authorization, and important limits before
implementation. Make omitted fields, explicit null, empty values, timestamp
format/timezone, and numeric precision unambiguous. Include pagination and
idempotency only when the operation needs them. Check compatibility with existing
clients before removing fields or changing meaning.

Use an existing authoritative schema when available. Reuse generation tools already
in the repository rather than manually maintaining multiple independent contracts.
Runtime validation at the Python boundary and appropriate client boundary is still
needed; TypeScript annotations do not validate JSON. Keep internal database models
separate from public representations when their ownership or exposure differs.

Write failing tests for a successful request and important invalid or unauthorized
requests. Exercise serialization and the actual routing/validation boundary. Verify
the Vue caller handles loading and returned failures. Avoid turning every endpoint
into a generic client framework or adding a new abstraction for one call.

Report the contract, compatibility decisions, and tests. Include a migration note
only if existing consumers must change. Do not publish, version, or deploy an API
unless the user's task includes that action.
