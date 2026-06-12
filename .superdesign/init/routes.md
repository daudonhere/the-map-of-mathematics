# Routes / Navigation Flow - The Map of Mathematics

This is a Python application with no web routing. Navigation is imperative (function calls and widget stacking).

## Entry Point
- File: `src/themath/__main__.py`
- `python -m themath` entry

### Flow:
```
python -m themath
  |-- parses --lang en|id (default: id)
  |-- if --gui: -> GUI main() directly
  |-- else: -> TUI Launcher (run_launcher)
       |-- returns "terminal" -> CLI main() (numbered menu loop)
       |-- returns "gui" -> GUI main()
       |-- returns None -> exit
```

## Launcher Menu
- Screens: Main Menu (3 items), Language Submenu (2 items)
- Navigation: Up/Down arrows to select, Enter to confirm, Esc/Tab/Q to go back or exit

## CLI Menu Loop
- Display numbered list of available concepts
- User enters number to view concept details
- 0 to exit
- Concept detail displayed via print_concept()
- Loop repeats until exit

## CLI Commands (standalone, not wired to main entry)
- `explore <node_id>` -> Graph display via print_graph()
- `search <query>` -> Table display via print_concept_table()
- `visualize <node_ids...>` -> Graph display via print_graph()

## GUI Navigation
- HomeScreen: concept list (double-click -> ExploreScreen), Visualize button -> VisualizeScreen
- ExploreScreen: back button -> HomeScreen
- VisualizeScreen: back button -> HomeScreen, refresh button -> refresh data
