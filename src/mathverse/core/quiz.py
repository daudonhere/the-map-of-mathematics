from __future__ import annotations

from mathverse.core.topics.algebra.core import gen_question as _gen_algebra_core
from mathverse.core.topics.algebra.exponents_logs import (
    gen_question as _gen_algebra_exponents,
)
from mathverse.core.topics.algebra.functions import (
    gen_question as _gen_algebra_functions,
)
from mathverse.core.topics.algebra.identities import (
    gen_question as _gen_algebra_identities,
)
from mathverse.core.topics.algebra.linear import gen_question as _gen_algebra_linear
from mathverse.core.topics.algebra.quadratic import (
    gen_question as _gen_algebra_quadratic,
)
from mathverse.core.topics.arithmetic import gen_question as _gen_arithmetic

_PLAYGROUND_MAP: dict[str, object] = {}

for _pid in (
    "basic_ops",
    "powers",
    "mental_math",
    "properties",
    "number_types",
    "factors",
    "ratios",
    "percentages",
    "number_theory",
):
    _PLAYGROUND_MAP[_pid] = _gen_arithmetic

for _pid in (
    "variables",
    "algebraic_forms",
    "algebraic_ops",
    "factoring",
    "expressions",
    "equations",
    "systems",
    "polynomials",
    "inequalities",
):
    _PLAYGROUND_MAP[_pid] = _gen_algebra_core

for _pid in ("perfect_square", "diff_squares"):
    _PLAYGROUND_MAP[_pid] = _gen_algebra_identities

for _pid in ("linear_equations", "systems_of_equations"):
    _PLAYGROUND_MAP[_pid] = _gen_algebra_linear

for _pid in ("quadratic", "quadratics"):
    _PLAYGROUND_MAP[_pid] = _gen_algebra_quadratic

_PLAYGROUND_MAP["functions"] = _gen_algebra_functions
_PLAYGROUND_MAP["exponents_logs"] = _gen_algebra_exponents


def gen_question(playground: str, locale: str) -> tuple[str, str, float]:
    handler = _PLAYGROUND_MAP.get(playground)
    if handler is not None:
        result = handler(playground, locale)
        if result is not None:
            return result
    return ("?", "0", 0.0)


__all__ = ["gen_question"]
