from __future__ import annotations

import typer

from themap.cli.utils import console, print_concept_table
from themap.core.repository import Repository
from themap.core.service import MapService


def search_cmd(
    query: str = typer.Argument(..., help="Search query"),
) -> None:
    """Search for mathematical concepts."""
    repo = Repository()
    service = MapService(repo)
    results = service.search(query)
    if not results:
        console.print(f"[yellow]No results for '{query}'.[/]")
        raise typer.Exit(code=1)
    print_concept_table(results)
