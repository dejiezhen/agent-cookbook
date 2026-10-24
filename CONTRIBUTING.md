# Contributing

Add a skill when a repeated workflow needs guidance that changes the agent's
decisions. Prefer improving an existing skill when its scope already fits.

1. Describe a realistic matching task and a nearby non-matching task.
2. Create `skills/<name>/SKILL.md` with matching lowercase hyphenated name and a
   focused description. Include only necessary workflow guidance.
3. Keep resources inside the skill so it works when installed individually. Add
   `agents/openai.yaml` with display name, a 25–64 character short description, and
   a default prompt mentioning `$<name>`. Automatic discovery remains the default.
4. Run the validation and tests documented in the README. Execute new scripts in
   a disposable workspace. Use behavior-based tests for meaningful invariants.
5. Add a README catalog entry and evaluation scenarios when relevant. Record primary
   sources and retain licenses/notices for any explicitly vendored content.

Keep changes tied to the requested capability. Avoid generic advice, duplicate
checklists, unused templates, speculative helpers, and required multi-agent flows.
A skill is guidance, not authorization for external actions.
