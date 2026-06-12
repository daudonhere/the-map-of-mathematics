from __future__ import annotations

from themath.core.graph import GraphBuilder
from themath.core.models import MathConcept


class TestGraphBuilder:
    def test_build_empty(self) -> None:
        builder = GraphBuilder()
        graph = builder.build()
        assert graph.nodes == []
        assert graph.edges == []

    def test_add_concept(self) -> None:
        builder = GraphBuilder()
        c = MathConcept(id="a", name="A", description="...", category="Test")
        builder.add_concept(c)
        graph = builder.build()
        assert len(graph.nodes) == 1

    def test_duplicate_concept(self) -> None:
        builder = GraphBuilder()
        c = MathConcept(id="a", name="A", description="...", category="Test")
        builder.add_concept(c)
        builder.add_concept(c)
        graph = builder.build()
        assert len(graph.nodes) == 1

    def test_add_edge(self) -> None:
        builder = GraphBuilder()
        builder.add_edge("a", "b")
        graph = builder.build()
        assert graph.edges == [("a", "b")]

    def test_duplicate_edge_reversed(self) -> None:
        builder = GraphBuilder()
        builder.add_edge("a", "b")
        builder.add_edge("b", "a")
        graph = builder.build()
        assert len(graph.edges) == 1
