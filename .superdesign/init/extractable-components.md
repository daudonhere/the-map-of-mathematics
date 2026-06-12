# Extractable Components - The Map of Mathematics

This project has no React/Vue components. However, the following visual patterns could be extracted as reusable units for design purposes:

#### Layout Patterns
- **TUI Launcher** — the full-screen ASCII banner + menu loop is the core "landing" experience
- **CLI Menu** — the Rich Panel + Table + input prompt pattern is the main interactive loop
- **GUI App Shell** — QMainWindow + QStackedWidget + navigation between screens

#### Visual Patterns
- **ASCII Banner** — the 5-line "THE MATH" block letter banner
- **Rich Panel + Table** — the menu panel with numbered concept list
- **Concept Detail Card** — the structured display of name, category, description, related
- **Graph Tree** — Rich Tree rendering of concept relationships
- **GUI Home List** — QListWidget with concept names and categories
- **GUI Concept Detail** — QLabel + QTextBrowser + QListWidget for concept exploration

No traditional component extraction is applicable since this is not a web frontend project.
