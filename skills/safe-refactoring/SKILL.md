---
name: safe-refactoring
description: Improve a concrete code structure while preserving observable behavior. Use for a requested refactor, duplication removal, or simplifying an existing implementation; separate intentional behavior changes from structural changes.
---

# Refactor with a reason

Identify the specific maintenance problem and a practical success criterion: a
duplicated rule has one owner, a function has fewer responsibilities, or a concrete
dependency is isolated. Read callers, tests, and compatibility requirements before
choosing a boundary. Shorter code is useful only when it is easier to understand.

Establish a passing baseline. Add characterization tests where important existing
behavior lacks coverage, including externally visible errors and side effects.
If you discover a bug, distinguish the bug fix from behavior-preserving work.
Do not silently bless an unintended behavior as a permanent contract.

Make small structural moves and run focused tests between them. Preserve public
interfaces unless changing them is in scope; update all known callers when it is.
Avoid combining dependency upgrades, reformatting, and architecture changes in a
single refactor. Prefer a named function or existing module over a new hierarchy.

Before extracting shared code, verify the callers share a rule and a reason to
change. Similar-looking code with different ownership can remain separate. Remove
dead code introduced or made obsolete by this refactor after checking actual use.
Keep explicit edge handling and domain boundaries even if they cost a few lines.

Check the final diff against the stated goal. Report what became simpler, what
behavior stayed covered, and any compatibility risk. If a new abstraction creates
more indirection than it removes, simplify it before finishing.
