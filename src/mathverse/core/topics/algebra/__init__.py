from __future__ import annotations

from mathverse.core.topics.algebra.core import algebra_core_subtopics
from mathverse.core.topics.algebra.exponents_logs import algebra_exponents_subtopics
from mathverse.core.topics.algebra.functions import algebra_functions_subtopics
from mathverse.core.topics.algebra.identities import algebra_identity_subtopics
from mathverse.core.topics.algebra.linear import algebra_linear_subtopics
from mathverse.core.topics.algebra.quadratic import algebra_quadratic_subtopics

algebra_subtopics: list = (
    algebra_core_subtopics
    + algebra_identity_subtopics
    + algebra_linear_subtopics
    + algebra_quadratic_subtopics
    + algebra_functions_subtopics
    + algebra_exponents_subtopics
)

__all__ = ["algebra_subtopics"]
