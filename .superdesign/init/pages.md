# Pages / Screen Dependency Trees - The Map of Mathematics

## 1. TUI Launcher Screen
Entry: src/themath/tui/launcher.py
Dependencies:
- src/themath/tui/launcher.py (contains banner, _read_key, _draw_menu, _draw_lang_menu, run_launcher)
  - src/themath/core/i18n.py (t helper for bilingual labels)

## 2. CLI Menu Screen
Entry: src/themath/cli/main.py
Dependencies:
- src/themath/cli/main.py (_build_menu_table, _show_menu, main)
  - src/themath/cli/utils.py (console, print_concept)
  - src/themath/core/repository.py (Repository)
  - src/themath/core/seed.py (seed_repo)
  - src/themath/core/service.py (MapService)
    - src/themath/core/i18n.py (t)
    - src/themath/core/models.py (MathConcept, GraphData)
    - src/themath/core/graph.py (GraphBuilder)
  - src/themath/core/models.py (MathConcept, GraphData)

## 3. CLI Explore Screen
Entry: src/themath/cli/commands/explore.py
Dependencies:
- src/themath/cli/commands/explore.py
  - src/themath/cli/utils.py (console, print_graph)
  - src/themath/core/repository.py
  - src/themath/core/service.py
    - (same chain as above)

## 4. CLI Search Screen
Entry: src/themath/cli/commands/search.py
Dependencies:
- src/themath/cli/commands/search.py
  - src/themath/cli/utils.py (console, print_concept_table)
  - src/themath/core/repository.py
  - src/themath/core/service.py

## 5. CLI Visualize Screen
Entry: src/themath/cli/commands/visualize.py
Dependencies:
- src/themath/cli/commands/visualize.py
  - src/themath/cli/utils.py (console, print_graph)
  - src/themath/core/repository.py
  - src/themath/core/service.py

## 6. GUI Home Screen
Entry: src/themath/gui/screens/home.py
Dependencies:
- src/themath/gui/screens/home.py (HomeScreen)
  - src/themath/core/service.py (MapService)
  - src/themath/gui/main.py (TheMapApp - has show_concept, go_home, go_visualize)
- src/themath/gui/main.py (TheMapApp)
  - src/themath/core/repository.py
  - src/themath/core/seed.py
  - src/themath/core/service.py
  - src/themath/gui/fonts/__init__.py (load_fonts)
  - src/themath/gui/screens/explore.py (ExploreScreen)
  - src/themath/gui/screens/home.py (HomeScreen)
  - src/themath/gui/screens/visualize.py (VisualizeScreen)

## 7. GUI Explore Screen
Entry: src/themath/gui/screens/explore.py
Dependencies:
- src/themath/gui/screens/explore.py (ExploreScreen)
  - src/themath/core/service.py (MapService)
  - src/themath/gui/main.py (TheMapApp)

## 8. GUI Visualize Screen
Entry: src/themath/gui/screens/visualize.py
Dependencies:
- src/themath/gui/screens/visualize.py (VisualizeScreen)
  - src/themath/core/service.py (MapService)
  - src/themath/gui/main.py (TheMapApp)
