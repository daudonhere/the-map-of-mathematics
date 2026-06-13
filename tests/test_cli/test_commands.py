from __future__ import annotations

from unittest.mock import patch

import typer
from typer.testing import CliRunner

from mathverse.cli.commands.explore import explore_cmd
from mathverse.cli.commands.search import search_cmd
from mathverse.cli.commands.visualize import visualize_cmd
from mathverse.core.models import GraphData, MathConcept

app = typer.Typer()
app.command("explore")(explore_cmd)
app.command("search")(search_cmd)
app.command("visualize")(visualize_cmd)

runner = CliRunner()


class TestExploreCmd:
    def test_explore_found(self) -> None:
        mock_concept = MathConcept(
            id="algebra",
            name="Algebra",
            description="Study of symbols",
            category="Pure",
            related_concepts=["geometry"],
        )
        mock_graph = GraphData(nodes=[mock_concept], edges=[])
        with patch(
            "mathverse.cli.commands.explore.MapService"
        ) as mock_service_cls:
            instance = mock_service_cls.return_value
            instance.explore.return_value = mock_graph
            result = runner.invoke(app, ["explore", "algebra"])
            assert result.exit_code == 0
            assert "Algebra" in result.stdout

    def test_explore_not_found(self) -> None:
        mock_graph = GraphData(nodes=[], edges=[])
        with patch(
            "mathverse.cli.commands.explore.MapService"
        ) as mock_service_cls:
            instance = mock_service_cls.return_value
            instance.explore.return_value = mock_graph
            result = runner.invoke(app, ["explore", "unknown"])
            assert result.exit_code == 1
            assert "not found" in result.stdout.lower()


class TestSearchCmd:
    def test_search_found(self) -> None:
        mock_concept = MathConcept(
            id="algebra",
            name="Algebra",
            description="Study of symbols",
            category="Pure",
            related_concepts=[],
        )
        with patch(
            "mathverse.cli.commands.search.MapService"
        ) as mock_service_cls:
            instance = mock_service_cls.return_value
            instance.search.return_value = [mock_concept]
            result = runner.invoke(app, ["search", "algebra"])
            assert result.exit_code == 0
            assert "Algebra" in result.stdout

    def test_search_no_results(self) -> None:
        with patch(
            "mathverse.cli.commands.search.MapService"
        ) as mock_service_cls:
            instance = mock_service_cls.return_value
            instance.search.return_value = []
            result = runner.invoke(app, ["search", "zzzz"])
            assert result.exit_code == 1
            assert "no results" in result.stdout.lower()


class TestVisualizeCmd:
    def test_visualize_found(self) -> None:
        mock_concept = MathConcept(
            id="algebra",
            name="Algebra",
            description="Study of symbols",
            category="Pure",
            related_concepts=["geometry"],
        )
        mock_graph = GraphData(nodes=[mock_concept], edges=[("algebra", "geometry")])
        with patch(
            "mathverse.cli.commands.visualize.MapService"
        ) as mock_service_cls:
            instance = mock_service_cls.return_value
            instance.visualize.return_value = mock_graph
            result = runner.invoke(app, ["visualize", "algebra", "geometry"])
            assert result.exit_code == 0
            assert "Algebra" in result.stdout

    def test_visualize_not_found(self) -> None:
        mock_graph = GraphData(nodes=[], edges=[])
        with patch(
            "mathverse.cli.commands.visualize.MapService"
        ) as mock_service_cls:
            instance = mock_service_cls.return_value
            instance.visualize.return_value = mock_graph
            result = runner.invoke(app, ["visualize", "unknown"])
            assert result.exit_code == 1
            assert "no concepts found" in result.stdout.lower()
