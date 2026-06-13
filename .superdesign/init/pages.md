# Pages / Screen Dependency Trees - The Map of Mathematics

## 1. TUI Launcher Screen
Entry: src/mathverse/tui/launcher.py
Dependencies:
- src/mathverse/tui/launcher.py (contains banner, _read_key, _draw_menu, _draw_lang_menu, run_launcher)
  - src/mathverse/core/i18n.py (t helper for bilingual labels)

## 2. CLI Menu Screen
Entry: src/mathverse/cli/main.py
Dependencies:
- src/mathverse/cli/main.py (_build_menu_table, _show_menu, main)
  - src/mathverse/cli/utils.py (console, print_concept)
  - src/mathverse/core/repository.py (Repository)
  - src/mathverse/core/seed.py (seed_repo)
  - src/mathverse/core/service.py (MapService)
    - src/mathverse/core/i18n.py (t)
    - src/mathverse/core/models.py (MathConcept, GraphData)
    - src/mathverse/core/graph.py (GraphBuilder)
  - src/mathverse/core/models.py (MathConcept, GraphData)

## 3. CLI Explore Screen
Entry: src/mathverse/cli/commands/explore.py
Dependencies:
- src/mathverse/cli/commands/explore.py
  - src/mathverse/cli/utils.py (console, print_graph)
  - src/mathverse/core/repository.py
  - src/mathverse/core/service.py
    - (same chain as above)

## 4. CLI Search Screen
Entry: src/mathverse/cli/commands/search.py
Dependencies:
- src/mathverse/cli/commands/search.py
  - src/mathverse/cli/utils.py (console, print_concept_table)
  - src/mathverse/core/repository.py
  - src/mathverse/core/service.py

## 5. CLI Visualize Screen
Entry: src/mathverse/cli/commands/visualize.py
Dependencies:
- src/mathverse/cli/commands/visualize.py
  - src/mathverse/cli/utils.py (console, print_graph)
  - src/mathverse/core/repository.py
  - src/mathverse/core/service.py

## 6. GUI Home Screen
Entry: src/mathverse/gui/screens/home.py
Dependencies:
- src/mathverse/gui/screens/home.py (HomeScreen)
  - src/mathverse/core/service.py (MapService)
  - src/mathverse/gui/main.py (TheMapApp - has show_concept, go_home, go_visualize)
- src/mathverse/gui/main.py (TheMapApp)
  - src/mathverse/core/repository.py
  - src/mathverse/core/seed.py
  - src/mathverse/core/service.py
  - src/mathverse/gui/fonts/__init__.py (load_fonts)
  - src/mathverse/gui/screens/explore.py (ExploreScreen)
  - src/mathverse/gui/screens/home.py (HomeScreen)
  - src/mathverse/gui/screens/visualize.py (VisualizeScreen)

## 7. GUI Explore Screen
Entry: src/mathverse/gui/screens/explore.py
Dependencies:
- src/mathverse/gui/screens/explore.py (ExploreScreen)
  - src/mathverse/core/service.py (MapService)
  - src/mathverse/gui/main.py (TheMapApp)

## 8. GUI Visualize Screen
Entry: src/mathverse/gui/screens/visualize.py
Dependencies:
- src/mathverse/gui/screens/visualize.py (VisualizeScreen)
  - src/mathverse/core/service.py (MapService)
  - src/mathverse/gui/main.py (TheMapApp)
