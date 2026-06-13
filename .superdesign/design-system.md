# Design System — The Map of Mathematics (GUI)

## Product Context
Desktop application for exploring mathematics concepts. Dark-themed educational tool with bilingual support (English/Indonesian).

## Color Palette
- Background: #1a1a2e (dark navy)
- Surface/Card: #16213e (slightly lighter navy)
- Accent/Primary: #FFD700 (gold) — used for borders, selection highlights, button outlines, titles
- Accent Hover: #e6c200 (darker gold) — button hover state
- Text Primary: #f0f0f0 (near white)
- Text Secondary: #aaa (gray)
- Text Muted: #888 (dimmer gray)
- Border: #333 (dark gray)
- Button Surface: #FFD700 text on transparent bg, gold border
- Button Hover: filled #FFD700 with #1a1a2e text
- Success: #00ff88 (green)
- Error: #ff4444 (red)

## Typography
- Primary Font: STIX Two Text (scientific typesetting) at 13pt body
- Monospace: used for ASCII banner elements
- Title (h1): 64px bold, gold, centered — splash screen
- Title (h2): 28px bold, gold, centered — screen headings
- Subtitle: 16px italic, #888 (#666), centered — tagline
- Body: 14-15px, #ccc/#f0f0f0
- Muted: 13px, #888

## Spacing
- Content margins: 40px horizontal, 16-24px vertical
- Between sections: 12-16px
- Between items in list: 8px padding
- Button padding: 12px 24px (large), 8px 16px (default)

## Components

### Button Styles
- **Primary (gold outline)**: transparent bg, 2px #FFD700 border, gold text, 8px border-radius, bold
  - Hover: filled #FFD700 bg, #1a1a2e text
- **Secondary (subtle back)**: transparent bg, 1px #555 border, #888 text, 8px border-radius
  - Hover: border and text turn #FFD700
- **Default dark**: #FFD700 bg, #1a1a2e text, no border, 6px border-radius
  - Hover: #e6c200

### List Items (QListWidget)
- Dark bg (#16213e), gold border (#FFD700)
- Items: 10px 14px padding, 4px border-radius
- Selected: #FFD700 bg, #1a1a2e text
- Hover: #2a2a4e bg

### Text/Body Area (QTextBrowser)
- Transparent bg, #ccc text
- Border: none or 1px #333 with 8px padding

### Separators (QFrame HLine)
- Color: #333 or #444

### Dialog (Playground)
- Dark bg (#1a1a2e)
- Header title: 22px bold gold
- Input: dark bg (#16213e), gold border on focus
- Buttons: gold filled for primary actions

## Layout Patterns
- **Splash Screen**: centered vertical layout with stretch
  - Large "THE MATH" title
  - Math symbols row
  - Italic slogan
  - Horizontal separator
  - Start button (large, gold outline)
  - Change Language button (subtle)
- **Topic List Screen**: back button top-left, title centered, scrollable list, bottom bar with Back (left) and Visualize (right) buttons
- **Explore Screen**: back button top-left, concept name centered, category center, description, "Explore Topics" button (if available), Related Concepts list
- **Topic Screen**: back button, concept name, stacked list/detail views
  - List: clickable subtopic list, separator, description preview
  - Detail: back-to-list button, subtopic title, examples (dim) + explanations (italic), playground button
