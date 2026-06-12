from __future__ import annotations

from themap.core.models import MathConcept


class Repository:
    """Data access layer untuk matematika concepts."""

    def __init__(self) -> None:
        self._concepts: dict[str, MathConcept] = {}

    def get_by_id(self, concept_id: str) -> MathConcept | None:
        return self._concepts.get(concept_id)

    def search(self, query: str) -> list[MathConcept]:
        q = query.lower()
        return [
            c
            for c in self._concepts.values()
            if q in c.name.lower() or q in c.description.lower()
        ]

    def get_all(self) -> list[MathConcept]:
        return list(self._concepts.values())

    def add(self, concept: MathConcept) -> None:
        self._concepts[concept.id] = concept

    def get_related(self, concept_id: str) -> list[MathConcept]:
        concept = self._concepts.get(concept_id)
        if not concept:
            return []
        return [
            self._concepts[rid]
            for rid in concept.related_concepts
            if rid in self._concepts
        ]
