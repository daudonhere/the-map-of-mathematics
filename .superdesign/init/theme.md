# Theme / Design Tokens - The Map of Mathematics

This is a terminal application with optional PyQt6 desktop GUI. Theme tokens reflect the terminal aesthetic.

## Terminal Theme

### Color Palette
- Background: terminal default (typically dark in modern terminals)
- Accent (cyan): `bold cyan` — used for banner text, concept names, menu numbers
- Accent (yellow): `bold yellow` — used for panel titles, "Related:" labels
- Accent (magenta): `bold magenta` — used for greeting text
- Accent (red): `bold red` / `red` — used for exit option, errors
- Accent (green): `green` — used for graph edges
- Dim: `dim` — used for keybind hints, category display
- Reverse: `reverse` — used for selected menu item background

### Typography
- Font: Monospace (terminal default, typically 9-12pt)
- Style: Rich's built-in markup tags for bold, dim, color
- Banner: 5 lines of ASCII block letters (no Unicode, no box drawing)
- Line length: ~70 chars (banner width)

### Spacing
- Blank line after banner: 1 newline
- Menu items: one per line, no extra spacing
- Keybind hints: 1 blank line above, centered

### Visual Conventions
- Selected menu item: `> ` prefix + `reverse` style (inverted foreground/background)
- Unselected menu item: `  ` prefix (2 spaces)
- Panel title: `[bold yellow]`
- Table: no borders (box=None), padding (0, 2)
- Concept detail: name in cyan, category in dim, description plain, related in yellow
- Error messages: yellow text
- Graph tree: cyan nodes, dim categories, green edges

## GUI Theme (PyQt6)

### Window
- Size: 1000x700
- Font: STIX Two Text at 13pt (loaded from bundled OTF files)
- Window title: locale-dependent

### Colors
- Subtitle text: `#666` (gray)
- Category text: `#888` (lighter gray)
- Link/connection highlight: `#0066cc` (blue)
- Back/action buttons: default Qt style

### Typography (GUI)
- Title: 28px bold
- Section title: 24px bold
- Sub-section title: 16px bold
- Body: 14px
- Category: 13px, lighter color

### Spacing (GUI)
- Content margins: 40px horizontal, 24px vertical
- Title bottom padding: 4px
- Subtitle bottom padding: 16px
- Section top padding: 16px
- Category bottom padding: 8px

### Bundle Fonts
- Location: `src/themath/gui/fonts/`
- Format: OTF (OpenType)
- Family: STIX Two Text (scientific typesetting)
- Load method: QFontDatabase.addApplicationFont()
