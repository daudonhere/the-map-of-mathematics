from __future__ import annotations

import typer

from themath.cli.utils import console, print_graph
from themath.core.repository import Repository
from themath.core.service import MapService


def explore_cmd(
    node_id: str = typer.Argument(..., help="Concept ID to explore"),
) -> None:
    """Explore a mathematical concept and its relationships."""
    repo = Repository()
    service = MapService(repo)
    graph = service.explore(node_id)
    if not graph.nodes:
        console.print(f"[yellow]Concept '{node_id}' not found.[/]")
        raise typer.Exit(code=1)
    print_graph(graph)
