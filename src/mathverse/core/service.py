from __future__ import annotations

from mathverse.core.graph import GraphBuilder
from mathverse.core.i18n import t
from mathverse.core.models import GraphData, MathConcept
from mathverse.core.repository import Repository


class MapService:
    def __init__(self, repo: Repository, locale: str = "id") -> None:
        self._repo = repo
        self._locale = locale

    @property
    def locale(self) -> str:
        return self._locale

    def set_locale(self, locale: str) -> None:
        self._locale = locale

    def _(self, key: str) -> str:
        return t(key, self._locale)

    def search(self, query: str) -> list[MathConcept]:
        results = self._repo.search(query)
        return [c for c in results if c.locale == self._locale]

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

    def list_concepts(self) -> list[MathConcept]:
        return [c for c in self._repo.get_all() if c.locale == self._locale]

    def get_all_locales(self) -> dict[str, list[MathConcept]]:
        result: dict[str, list[MathConcept]] = {}
        for c in self._repo.get_all():
            result.setdefault(c.locale, []).append(c)
        return result
