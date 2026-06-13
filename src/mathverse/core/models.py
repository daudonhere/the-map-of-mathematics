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


@dataclass
class SubTopic:
    title: dict[str, str]
    description: dict[str, str]
    explanation: dict[str, str]
    examples: dict[str, list[str]] = field(default_factory=dict)
    playground: str | None = None


@dataclass
class TopicContent:
    concept_id: str
    subtopics: list[SubTopic] = field(default_factory=list)
