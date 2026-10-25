# Python boundary examples

Read when deciding where logic belongs and how failures should propagate. These
are original examples; adapt input contracts to the actual project.

## A query parameter needs a bounded integer

The HTTP boundary parses a string and validates the allowed range. The domain
function receives the validated integer. A small parsing function is enough; a
generic validation hierarchy is unnecessary for one parameter. If a schema library
already owns request validation, express the rule there instead of duplicating it.

Example spec: an omitted limit uses 20; explicit limits must be decimal integers
from 1 through 100. Define whether empty and whitespace-only strings are invalid.
Test omission, both valid bounds, 0, 101, and malformed text. Avoid collapsing an
explicitly invalid value into the default through a truthiness check.

## An external service fails

Translate a known timeout at the boundary that can provide useful recovery. Keep
unexpected programming errors visible, preserve causes where translated, and avoid
returning an empty successful result after a failed dependency. Separate "no matching
records" from "could not query records." They drive different behavior.

## State earns a class

A pure calculation can remain a function. A client with a connection lifecycle or
meaningful session state can justify a class. An interface becomes useful when
there is an actual replaceable boundary, not merely because a test could mock it.
Prefer exercising pure rules directly and adapters at their real boundaries.

## Database ownership

Keep transaction ownership explicit. Test expected rows and rollback of partial
changes. A mocked `commit()` assertion does not establish database behavior. Let
Postgres enforce durable invariants while application errors translate known
constraint failures into the intended user-visible outcome.
