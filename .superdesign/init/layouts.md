# Layouts - The Map of Mathematics

This is a terminal TUI and desktop GUI application. Layouts describe screen-level rendering structures.

## Terminal Layouts

### TUI Launcher Layout
- File: `src/themath/tui/launcher.py`
- Structure:
  1. Clear screen
  2. Print 5-line ASCII banner "THE MATH" (bold cyan, centered)
  3. Print blank line
  4. Print menu items (3 items: Terminal Mode, Desktop Mode, Select Language) with `> ` prefix on selected item and reverse style
  5. Print blank line
  6. Print keybind hints (dim, centered): "Up/Down Navigate | Enter Select | Esc Exit | Tab Back"
- Sub-layout: Language submenu (same banner) with title "Select Language" and 2 items (English, Indonesia), keybind hint: "Up/Down Navigate | Enter Select | Esc Back"

### CLI Menu Layout
- File: `src/themath/cli/main.py`
- Structure:
  1. Print greeting: "[bold magenta]Hello, Professor![/]"
  2. Loop:
     - Print Rich Panel with title "The Map of Mathematics" (bold yellow) and subtitle "Select a topic to explore"
     - Inside Panel: Table with numbered rows (bold cyan number + concept name)
     - Last row: "0. Exit" (bold red 0, red text)
     - Prompt: "[?] Enter number: "
     - On valid selection: print blank line, call print_concept(), print blank line

### CLI Explore View
- File: `src/themath/cli/utils.py` (print_graph)
- Structure:
  - Rich Tree titled "[bold]Graph[/]"
  - For each node: branch with concept name (cyan), category (dim), description
  - For each edge: "[green]source -> target[/]"
  
### CLI Search View
- File: `src/themath/cli/utils.py` (print_concept_table)
- Structure:
  - Rich Table titled "Concepts"
  - Columns: ID (dim), Name (cyan), Category (magenta), Description
  - One row per concept

## GUI Layouts

### Main Window (TheMapApp)
- QStackedWidget with 3 screens:
  1. HomeScreen (index 0)
  2. ExploreScreen (index 1)
  3. VisualizeScreen (index 2)
- 1000x700 default size
- Window title from locale: "Peta Matematika" (id) or "The Map of Mathematics" (en)

### HomeScreen Layout (QVBoxLayout, margins 40,24,40,24)
1. Title label (28px bold, centered)
2. Subtitle label (14px, #666, centered, select_topic text)
3. QListWidget with concept list items formatted as "name | category"
4. QHBoxLayout at bottom: stretch + Visualize button

### ExploreScreen Layout (QVBoxLayout, margins 40,24,40,24)
1. Back button (left-aligned, "|<- Back")
2. Name label (24px bold, top padding 16px)
3. Category label (13px, #888, bottom padding 8px)
4. QTextBrowser for description (14px, max height 120px)
5. Related concepts title (16px bold, top padding 16px)
6. QListWidget for related concepts

### VisualizeScreen Layout (QVBoxLayout, margins 40,24,40,24)
1. Back button (left-aligned)
2. Title label (24px bold, centered, "Concept Connections")
3. QTextBrowser with HTML-rendered connections (14px)
4. QHBoxLayout: stretch + Refresh button
