# Components - The Map of Mathematics

This project is a Python terminal TUI (Text User Interface) and desktop GUI application, not a web frontend. "Components" here refer to the Rich terminal rendering patterns and PyQt6 GUI widgets used to build the UI.

## Terminal (Rich) Components

### TUI Launcher (ASCII Banner + Menu)
- Source: `src/themath/tui/launcher.py` (131 lines)
- Description: Full-screen launcher with ASCII art banner, Rich console menu, and raw terminal key handling via termios/tty.

Full source:
```python
from __future__ import annotations

import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from themath.core.i18n import t

BANNER = [
    "TTTTTTT H   H EEEEEE   M   M  AAAA  TTTTTTT H   H",
    "   T    H   H E        MM MM A   A    T    H   H",
    "   T    HHHHH EEEEE    M M M AAAAA    T    HHHHH",
    "   T    H   H E        M   M A   A    T    H   H",
    "   T    H   H EEEEEE   M   M A   A    T    H   H",
]


def _read_key() -> str:
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            seq = sys.stdin.read(2)
            return {"[A": "up", "[B": "down", "[D": "left", "[C": "right"}.get(
                seq, "esc"
            )
        elif ch in ("\n", "\r"):
            return "enter"
        elif ch == "\t":
            return "tab"
        elif ch in ("q", "Q"):
            return "q"
        else:
            return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _draw_menu(
    console: Console,
    current: int,
    items: list[str],
) -> None:
    console.clear()
    for line in BANNER:
        console.print(line, style="bold cyan", justify="center")
    console.print()

    for i, item in enumerate(items):
        prefix = "> " if i == current else "  "
        style = "reverse" if i == current else ""
        console.print(Text(f"{prefix}{item}", style=style), justify="center")

    console.print()
    console.print(
        "Up/Down Navigate | Enter Select | Esc Exit | Tab Back",
        style="dim",
        justify="center",
    )


def _draw_lang_menu(console: Console, locale: str, current: int) -> None:
    langs = [("English", "en"), ("Indonesia", "id")]

    console.clear()
    for line in BANNER:
        console.print(line, style="bold cyan", justify="center")
    console.print()
    console.print(f"  [bold]{t('select_language', locale)}[/]", justify="center")
    console.print()

    for i, (label, _) in enumerate(langs):
        prefix = "> " if i == current else "  "
        style = "reverse" if i == current else ""
        console.print(Text(f"{prefix}{label}", style=style), justify="center")

    console.print()
    console.print("Up/Down Navigate | Enter Select | Esc Back", style="dim", justify="center")


def run_launcher(locale: str = "id") -> str | None:
    if not sys.stdin.isatty():
        return "terminal"

    console = Console()
    items = [t("terminal_mode", locale), t("desktop_mode", locale), t("select_language", locale)]
    current = 0
    in_lang_menu = False
    lang_current = 0

    try:
        while True:
            if in_lang_menu:
                _draw_lang_menu(console, locale, lang_current)
                key = _read_key()
                if key == "up":
                    lang_current = (lang_current - 1) % 2
                elif key == "down":
                    lang_current = (lang_current + 1) % 2
                elif key == "enter":
                    locale = "en" if lang_current == 0 else "id"
                    items = [t("terminal_mode", locale), t("desktop_mode", locale), t("select_language", locale)]
                    in_lang_menu = False
                elif key in ("esc", "tab", "q"):
                    in_lang_menu = False
            else:
                _draw_menu(console, current, items)
                key = _read_key()
                if key == "up":
                    current = (current - 1) % len(items)
                elif key == "down":
                    current = (current + 1) % len(items)
                elif key == "enter":
                    if current == 0:
                        return "terminal"
                    elif current == 1:
                        return "gui"
                    elif current == 2:
                        in_lang_menu = True
                        lang_current = 0
                elif key in ("esc", "tab", "q"):
                    return None
    except (EOFError, KeyboardInterrupt):
        return None
    except Exception:
        return "terminal"
```

### CLI Menu (Rich Panel + Table)
- Source: `src/themath/cli/main.py` (83 lines)
- Description: Numbered list of concepts displayed in a Rich Panel with Table, with input-based navigation.

Full source:
```python
from __future__ import annotations

import sys

from rich import print as rprint
from rich.panel import Panel
from rich.table import Table

from themath.cli.utils import console, print_concept
from themath.core.repository import Repository
from themath.core.seed import seed_repo
from themath.core.service import MapService


def _build_menu_table(service: MapService) -> tuple[Table, dict[int, str]]:
    concepts = service.list_concepts()
    table = Table(show_header=False, box=None, padding=(0, 2))
    mapping: dict[int, str] = {}
    for i, c in enumerate(concepts, 1):
        table.add_row(f"[bold cyan]{i}[/]", c.name)
        mapping[i] = c.id
    table.add_row("[bold red]0[/]", f"[red]{service._('exit')}[/]")
    return table, mapping


def _show_menu(service: MapService) -> None:
    while True:
        table, mapping = _build_menu_table(service)
        console.print()
        console.print(
            Panel(
                table,
                title=f"[bold yellow]{service._('app_title')}[/]",
                subtitle=service._("select_topic"),
            )
        )
        try:
            choice = input(f"[?] {service._('enter_number')}: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print(f"\n[red]{service._('goodbye')}[/]")
            sys.exit(0)

        if choice == "0":
            console.print(f"[red]{service._('goodbye')}[/]")
            break

        try:
            num = int(choice)
        except ValueError:
            console.print(f"[red]{service._('enter_valid_number')}[/]")
            continue

        concept_id = mapping.get(num)
        if concept_id is None:
            console.print(f"[red]{service._('choice_not_available')}[/]")
            continue

        concept = service.get_concept(concept_id)
        if concept:
            console.print()
            print_concept(concept)
            console.print()


def main(locale: str = "id") -> None:
    repo = Repository()
    seed_repo(repo)
    service = MapService(repo, locale)
    rprint(f"[bold magenta]{service._('hello')}[/]")
    _show_menu(service)


if __name__ == "__main__":
    locale_arg = "id"
    if "--lang" in sys.argv:
        idx = sys.argv.index("--lang")
        try:
            locale_arg = sys.argv[idx + 1]
        except IndexError:
            locale_arg = "id"
        if locale_arg not in ("en", "id"):
            locale_arg = "id"
    main(locale_arg)
```

### CLI Utility Functions (print_concept, print_graph, print_concept_table)
- Source: `src/themath/cli/utils.py` (42 lines)
- Description: Shared Rich rendering functions for concept display, tables, and graph trees.

Full source:
```python
from __future__ import annotations

from rich.console import Console
from rich.table import Table
from rich.tree import Tree

from themath.core.models import GraphData, MathConcept

console = Console()


def print_concept(concept: MathConcept) -> None:
    console.print(f"[bold cyan]{concept.name}[/]")
    console.print(f"  [dim]{concept.category}[/]")
    console.print(f"  {concept.description}")
    if concept.related_concepts:
        console.print("  [yellow]Related:[/]", ", ".join(concept.related_concepts))


def print_concept_table(concepts: list[MathConcept]) -> None:
    table = Table(title="Concepts")
    table.add_column("ID", style="dim")
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="magenta")
    table.add_column("Description")
    for c in concepts:
        table.add_row(c.id, c.name, c.category, c.description)
    console.print(table)


def print_graph(graph: GraphData) -> None:
    if not graph.nodes:
        console.print("[yellow]No concepts found.[/]")
        return
    tree = Tree("[bold]Graph[/]")
    for node in graph.nodes:
        branch = tree.add(f"[cyan]{node.name}[/]")
        branch.add(f"[dim]{node.category}[/]")
        branch.add(node.description)
    for edge in graph.edges:
        tree.add(f"[green]{edge[0]} \u2192 {edge[1]}[/]")
    console.print(tree)
```

### CLI Commands (Explore, Search, Visualize)
- Source: `src/themath/cli/commands/explore.py` (20 lines)
- Source: `src/themath/cli/commands/search.py` (20 lines)
- Source: `src/themath/cli/commands/visualize.py` (22 lines)
- Description: Standalone Typer commands for explore, search, and visualize. Not wired to the main entry point.

## GUI (PyQt6) Components

### TheMapApp (Main Window)
- Source: `src/themath/gui/main.py` (62 lines)
- Description: QMainWindow with QStackedWidget managing HomeScreen, ExploreScreen, VisualizeScreen.

### HomeScreen
- Source: `src/themath/gui/screens/home.py` (66 lines)
- Description: Concept list with QListWidget, title/subtitle labels, and visualize button.

### ExploreScreen
- Source: `src/themath/gui/screens/explore.py` (85 lines)
- Description: Concept detail view with back button, name/category labels, QTextBrowser for description, related concepts list.

### VisualizeScreen
- Source: `src/themath/gui/screens/visualize.py` (74 lines)
- Description: All connections view with HTML-rendered concept relationships, refresh button.

### Font Loader
- Source: `src/themath/gui/fonts/__init__.py` (16 lines)
- Description: Loads STIX Two Text OTF fonts from bundled `fonts/` directory via QFontDatabase.
