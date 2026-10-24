# Repository guidance

This repository distributes portable developer skills. Keep each skill focused,
self-contained, and useful when copied on its own. Add resources only for a concrete
need. Favor deliberate changes over expanding the catalog to cover every topic.

For executable behavior changes, write a concise spec, then use observed
red → green → refactor cycles. Preserve existing work and report test execution
honestly. Prose edits do not need manufactured tests.

Use the configured Python environment to run:

```sh
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

Update the README and relevant evaluation prompts when changing skill scope.
Keep upstream code out of the repository unless vendoring is explicitly requested
with source revision and license notices. Do not change global agent configuration
as a side effect of maintaining this library.
