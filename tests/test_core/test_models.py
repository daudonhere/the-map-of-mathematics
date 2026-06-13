from __future__ import annotations

from mathverse.core.models import GraphData, MathConcept


class TestMathConcept:
    def test_create_concept(self) -> None:
        c = MathConcept(
            id="calc",
            name="Calculus",
            description="Study of change",
            category="Analysis",
            related_concepts=["limits"],
        )
        assert c.id == "calc"
        assert c.name == "Calculus"

    def test_concept_default_related(self) -> None:
        c = MathConcept(id="test", name="Test", description="...", category="Test")
        assert c.related_concepts == []


class TestGraphData:
    def test_create_graph(self) -> None:
        c = MathConcept(id="a", name="A", description="...", category="Test")
        g = GraphData(nodes=[c], edges=[("a", "b")])
        assert len(g.nodes) == 1
        assert len(g.edges) == 1
