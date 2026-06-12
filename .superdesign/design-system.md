# Design System - The Map of Mathematics

## Product Context
A bilingual (EN/ID) terminal TUI + desktop GUI application for exploring, searching, and visualizing mathematical concepts. Users navigate a connected graph of 14 math concepts per locale.

## Platform
- **Primary**: Terminal/CLI (Rich text rendering)
- **Secondary**: Desktop GUI (PyQt6)

## Brand Typography
- **Terminal**: Monospace font (terminal default, ~9-12pt)
- **GUI**: STIX Two Text at 13pt (scientific typesetting font, bundled as OTF)

## Color Palette

### Terminal Colors
- Background: terminal default (typically dark bg, light text)
- Cyan: `bold cyan` — banner, concept names, menu numbers
- Yellow: `bold yellow` — panel titles, "Related" labels
- Magenta: `bold magenta` — greeting text
- Red: `bold red` / `red` — exit option, errors
- Green: `green` — graph edges (relationships)
- Dim: `dim` — keybind hints, category labels, secondary info
- Reverse: `reverse` — selected menu item (inverted fg/bg)

### GUI Colors
- Background: default Qt light theme
- Text: default black
- Subtitle: `#666666`
- Category: `#888888`
- Link/connection: `#0066cc`
- Buttons: default Qt style

## ASCII Banner
5 lines of fixed-width block letters spelling "THE MATH":
```
TTTTTTT H   H EEEEEE   M   M  AAAA  TTTTTTT H   H
   T    H   H E        MM MM A   A    T    H   H
   T    HHHHH EEEEE    M M M AAAAA    T    HHHHH
   T    H   H E        M   M A   A    T    H   H
   T    H   H EEEEEE   M   M A   A    T    H   H
```
Rendered in bold cyan, centered.

## Layout Conventions

### TUI Launcher
- Full screen clear before render
- Banner + blank line + menu items + blank line + keybind hints
- Selected item: `> ` prefix + reverse style
- Unselected item: `  ` prefix (2 spaces)
- Keybind hints: dim style, centered

### CLI Menu
- Rich Panel with border
- Panel title: app name (bold yellow)
- Panel subtitle: instruction text
- Numbered table (no borders, minimal padding)
- 0 = exit (bold red)

### GUI Screens
- Content margins: 40px horizontal, 24px vertical
- Title: 28px bold
- Section header: 24px bold
- Body: 14px
- Secondary: 13px colored

## Iconography
No icons in terminal mode. GUI uses no custom icons (standard Qt widget text only).

## Spacing
- Terminal blank lines: 1 newline between sections
- Panel padding: (0, 2) for tables
- GUI margins: 40px horizontal, 24px vertical (all screens)

## Language Support
- Two locales: English (en) and Indonesian (id)
- Labels defined in `src/themath/core/i18n.py`
- Default locale: Indonesian (id)
- Override via: `--lang en` flag or language menu in launcher
