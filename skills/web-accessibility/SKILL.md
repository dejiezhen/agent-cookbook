---
name: web-accessibility
description: Implement or review accessible behavior in a specific web interface, including Vue forms, dialogs, keyboard navigation, and status messages. Use for UI interaction changes or a requested accessibility review.
---

# Accessible interactions

Identify the user journey, interactive controls, and existing component library.
Reuse its accessible primitives when they fit. Scope work to the requested interface
and affected interactions; a form edit does not require a whole-site redesign.

Start with semantic HTML and meaningful accessible names. Associate instructions
and errors with fields. Keep keyboard access and visible focus. Preserve native
button, link, and input behavior rather than recreating it with clickable containers.
For dialogs or menus, inspect focus entry, navigation, dismissal, and restoration.

Represent loading, validation, and completion clearly. Use status announcements
when users need updates without a focus change; avoid repetitive announcements.
Preserve entered values on recoverable failures. Respect reduced-motion preferences
when motion is part of the change. Do not communicate essential meaning only by color.

Translate the journey into observable acceptance criteria before implementing new
behavior. Add focused failing tests for names, errors, and state changes. Then check
the real browser with keyboard navigation and relevant viewport/zoom conditions.
Use available automated accessibility tooling as supporting evidence; it does not
prove usability or conformance by itself. State when assistive technology checks
were not performed.

Report concrete barriers with reproduction and affected controls. When fixing one,
prefer the smallest semantic or interaction change that resolves it. Avoid adding an
accessibility abstraction layer where existing native controls suffice.
