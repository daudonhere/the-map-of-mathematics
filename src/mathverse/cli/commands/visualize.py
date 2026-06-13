from __future__ import annotations

import typer

from mathverse.cli.utils import console, print_graph
from mathverse.core.repository import Repository
from mathverse.core.service import MapService


def visualize_cmd(
    node_ids: list[str] = typer.Argument(
        ..., help="Concept IDs to visualize (space-separated)"
    ),
) -> None:
    """Visualize connections between multiple mathematical concepts."""
    repo = Repository()
    service = MapService(repo)
    graph = service.visualize(node_ids)
    if not graph.nodes:
        console.print("[yellow]No concepts found for given IDs.[/]")
        raise typer.Exit(code=1)
    print_graph(graph)
