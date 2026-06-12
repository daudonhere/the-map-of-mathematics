from __future__ import annotations

from rich.console import Console
from rich.table import Table
from rich.tree import Tree

from themap.core.models import GraphData, MathConcept

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
        tree.add(f"[green]{edge[0]} → {edge[1]}[/]")
    console.print(tree)
