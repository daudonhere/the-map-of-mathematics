from __future__ import annotations

from mathverse.core.models import SubTopic, TopicContent
from mathverse.core.topics.abstract_algebra import (
    subtopics as _abstract_algebra_subtopics,
)
from mathverse.core.topics.algebra import algebra_subtopics as _algebra_subtopics
from mathverse.core.topics.analysis import subtopics as _analysis_subtopics
from mathverse.core.topics.arithmetic import subtopics as _arithmetic_subtopics
from mathverse.core.topics.boolean_algebra import (
    subtopics as _boolean_algebra_subtopics,
)
from mathverse.core.topics.calculus import subtopics as _calculus_subtopics
from mathverse.core.topics.computer_algebra import (
    subtopics as _computer_algebra_subtopics,
)
from mathverse.core.topics.discrete import subtopics as _discrete_subtopics
from mathverse.core.topics.geometry import subtopics as _geometry_subtopics
from mathverse.core.topics.linear_algebra import (
    subtopics as _linear_algebra_subtopics,
)
from mathverse.core.topics.number_theory import subtopics as _number_theory_subtopics
from mathverse.core.topics.probability import subtopics as _probability_subtopics
from mathverse.core.topics.topology import subtopics as _topology_subtopics
from mathverse.core.topics.trigonometry import subtopics as _trigonometry_subtopics

_SUBTOPICS: dict[str, TopicContent] = {}


def _reg(concept_id: str, subtopics: list[SubTopic]) -> None:
    _SUBTOPICS[concept_id] = TopicContent(concept_id=concept_id, subtopics=subtopics)


def get_content(concept_id: str) -> TopicContent | None:
    return _SUBTOPICS.get(concept_id)


_reg("arithmetic", _arithmetic_subtopics)
_reg("aritmatika", _arithmetic_subtopics)
_reg("algebra", _algebra_subtopics)
_reg("aljabar", _algebra_subtopics)
_reg("euclidean-geometry", _geometry_subtopics)
_reg("geometri-euclid", _geometry_subtopics)
_reg("differential-geometry", _geometry_subtopics)
_reg("geometri-diferensial", _geometry_subtopics)
_reg("trigonometry", _trigonometry_subtopics)
_reg("trigonometri", _trigonometry_subtopics)
_reg("calculus", _calculus_subtopics)
_reg("kalkulus", _calculus_subtopics)
_reg("discrete-mathematics", _discrete_subtopics)
_reg("matematika-diskrit", _discrete_subtopics)
_reg("probability-statistics", _probability_subtopics)
_reg("probabilitas-statistika", _probability_subtopics)
_reg("real-analysis", _analysis_subtopics)
_reg("analisis-real", _analysis_subtopics)
_reg("complex-analysis", _analysis_subtopics)
_reg("analisis-kompleks", _analysis_subtopics)
_reg("topology", _topology_subtopics)
_reg("topologi", _topology_subtopics)
_reg("number-theory", _number_theory_subtopics)
_reg("teori-bilangan", _number_theory_subtopics)
_reg("linear-algebra", _linear_algebra_subtopics)
_reg("aljabar-linear", _linear_algebra_subtopics)
_reg("abstract-algebra", _abstract_algebra_subtopics)
_reg("aljabar-abstrak", _abstract_algebra_subtopics)
_reg("boolean-algebra", _boolean_algebra_subtopics)
_reg("aljabar-boolean", _boolean_algebra_subtopics)
_reg("computer-algebra", _computer_algebra_subtopics)
_reg("aljabar-komputer", _computer_algebra_subtopics)
