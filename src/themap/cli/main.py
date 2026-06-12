from __future__ import annotations

import typer
from rich import print as rprint

from themap.cli.commands.explore import explore_cmd
from themap.cli.commands.search import search_cmd
from themap.cli.commands.visualize import visualize_cmd


def _print_greeting() -> None:
    rprint("[bold magenta]Hello, Professor![/]")


app = typer.Typer(
    name="themap",
    help="The Map of Mathematics - explore, search, and visualize mathematical concepts",
    callback=_print_greeting,
)
app.command(name="explore")(explore_cmd)
app.command(name="search")(search_cmd)
app.command(name="visualize")(visualize_cmd)


def main() -> None:
    app()
