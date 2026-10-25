# Put a style guide in the plan

Every plan includes a style-guide section, including a short plan in chat. Scale it
to the work: reference authoritative existing guides, tokens, components, and tooling,
then state the decisions that affect this change. Do not create a new design system
or duplicate a project's entire guide for a small feature.

## Start with the existing product

Inspect product/design docs, styles, shared components, language configuration, and
nearby code. Record which sources govern the change. Distinguish established choices
from proposed changes and unresolved preferences. Reuse existing visual identity
unless redesign is part of the request. For a new UI, establish a small coherent
direction before implementing screens; ask about a material preference or offer a
clear proposed default rather than silently choosing a new brand.

## UI and content

Include the relevant decisions below, with real token/component names or concrete
proposed values where needed. A mood adjective alone cannot guide implementation.

| Area | Decisions to capture |
| --- | --- |
| Visual direction | Product character, reference screens if supplied, existing identity to preserve, and the intended hierarchy |
| Typography | Existing fonts, heading/body/label roles, sizes, weights, line heights, and legibility at supported sizes |
| Color | Semantic surface/text/accent/status roles, light/dark variants where supported, and contrast checks; never make color the only state cue |
| Layout and spacing | Content width, spacing conventions, alignment, grouping, responsive behavior, and long-content/zoom handling |
| Components and states | Reusable buttons, fields, dialogs, navigation, and affected default/focus/disabled/error/empty/loading/success states; omit irrelevant states |
| Accessibility and input | Keyboard/focus behavior, labels/status feedback, touch targets, alternatives to color, and device/browser checks |
| Motion and media | Purpose and duration of relevant effects, reduced-motion behavior, audio controls, and asset/license constraints where affected |
| Writing | Voice, terminology, labels, error/recovery wording, and content formatting; use concrete examples for ambiguous copy |

Name how the affected style decisions will be checked: actual browser interaction,
supported widths/themes, keyboard navigation, or focused visual review as relevant.
Do not claim that chosen colors, markup, or a green build establish accessibility.
Introduce reusable tokens only for an actual recurring role; avoid a token framework
or component catalog for every possible future screen.

## Code and non-visual interfaces

Record the project's applicable naming, file organization, type/error conventions,
format/lint tools, and selected stack modules. Reference existing settings rather
than inventing another rulebook or initiating a style migration.

For backend, CLI, data, or documentation work without a UI, say visual styling is
not applicable and capture relevant API/output/error/naming or prose conventions.
A content-only change can carry forward the existing visual guide in a sentence.
This section constrains authorized work; it does not add a redesign or cleanup task.

References: [GOV.UK style categories](https://design-system.service.gov.uk/styles/)
and [W3C accessible interface design](https://www.w3.org/WAI/tips/designing/).
