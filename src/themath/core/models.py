from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MathConcept:
    id: str
    name: str
    description: str
    category: str
    locale: str = "id"
    related_concepts: list[str] = field(default_factory=list)


@dataclass
class GraphData:
    nodes: list[MathConcept]
    edges: list[tuple[str, str]]
