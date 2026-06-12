from __future__ import annotations

from themap.core.models import GraphData, MathConcept


class GraphBuilder:
    """Membangun graph data dari konsep matematika."""

    def __init__(self) -> None:
        self._nodes: dict[str, MathConcept] = {}
        self._edges: list[tuple[str, str]] = []

    def add_concept(self, concept: MathConcept) -> None:
        if concept.id not in self._nodes:
            self._nodes[concept.id] = concept

    def add_edge(self, from_id: str, to_id: str) -> None:
        if (from_id, to_id) not in self._edges and (to_id, from_id) not in self._edges:
            self._edges.append((from_id, to_id))

    def build(self) -> GraphData:
        return GraphData(nodes=list(self._nodes.values()), edges=list(self._edges))
