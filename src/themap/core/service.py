from __future__ import annotations

from themap.core.graph import GraphBuilder
from themap.core.models import GraphData, MathConcept
from themap.core.repository import Repository


class MapService:
    """Business logic untuk The Map of Mathematics."""

    def __init__(self, repo: Repository) -> None:
        self._repo = repo

    def search(self, query: str) -> list[MathConcept]:
        return self._repo.search(query)

    def explore(self, node_id: str) -> GraphData:
        concept = self._repo.get_by_id(node_id)
        if not concept:
            return GraphData(nodes=[], edges=[])
        related = self._repo.get_related(node_id)
        builder = GraphBuilder()
        builder.add_concept(concept)
        for r in related:
            builder.add_concept(r)
            builder.add_edge(node_id, r.id)
        return builder.build()

    def visualize(self, node_ids: list[str]) -> GraphData:
        builder = GraphBuilder()
        for nid in node_ids:
            concept = self._repo.get_by_id(nid)
            if concept:
                builder.add_concept(concept)
                for rid in concept.related_concepts:
                    related = self._repo.get_by_id(rid)
                    if related:
                        builder.add_concept(related)
                        builder.add_edge(nid, rid)
        return builder.build()

    def get_concept(self, concept_id: str) -> MathConcept | None:
        return self._repo.get_by_id(concept_id)
