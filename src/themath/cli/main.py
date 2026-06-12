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
