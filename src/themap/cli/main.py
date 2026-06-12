from __future__ import annotations

import sys

from rich import print as rprint
from rich.panel import Panel
from rich.table import Table

from themap.cli.utils import console, print_concept
from themap.core.repository import Repository
from themap.core.seed import seed_repo
from themap.core.service import MapService


def _build_menu_table(repo: Repository) -> tuple[Table, dict[int, str]]:
    concepts = repo.get_all()
    table = Table(show_header=False, box=None, padding=(0, 2))
    mapping: dict[int, str] = {}
    for i, c in enumerate(concepts, 1):
        table.add_row(f"[bold cyan]{i}[/]", c.name)
        mapping[i] = c.id
    table.add_row("[bold red]0[/]", "[red]Exit[/]")
    return table, mapping


def _show_menu(repo: Repository, service: MapService) -> None:
    while True:
        table, mapping = _build_menu_table(repo)
        console.print()
        console.print(
            Panel(
                table,
                title="[bold yellow]Map of Mathematics[/]",
                subtitle="Select a topic to explore",
            )
        )
        try:
            choice = input("[?] Enter number: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[red]See you later, Professor![/]")
            sys.exit(0)

        if choice == "0":
            console.print("[red]See you later, Professor![/]")
            break

        try:
            num = int(choice)
        except ValueError:
            console.print("[red]Enter a valid number.[/]")
            continue

        concept_id = mapping.get(num)
        if concept_id is None:
            console.print("[red]Choice not available.[/]")
            continue

        concept = service.get_concept(concept_id)
        if concept:
            console.print()
            print_concept(concept)
            console.print()


def main() -> None:
    repo = Repository()
    seed_repo(repo)
    service = MapService(repo)
    rprint("[bold magenta]Hello, Professor![/]")
    _show_menu(repo, service)


if __name__ == "__main__":
    main()
