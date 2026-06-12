from __future__ import annotations

import pytest

from themath.core.models import MathConcept
from themath.core.repository import Repository


@pytest.fixture
def sample_repo() -> Repository:
    repo = Repository()
    repo.add(
        MathConcept(
            id="algebra",
            name="Algebra",
            description="Study of symbols and rules for manipulating them",
            category="Pure Mathematics",
            related_concepts=["geometry", "number-theory"],
        )
    )
    repo.add(
        MathConcept(
            id="geometry",
            name="Geometry",
            description="Study of shapes, sizes, and properties of space",
            category="Pure Mathematics",
            related_concepts=["algebra", "trigonometry"],
        )
    )
    repo.add(
        MathConcept(
            id="number-theory",
            name="Number Theory",
            description="Study of integers and integer-valued functions",
            category="Pure Mathematics",
            related_concepts=["algebra"],
        )
    )
    repo.add(
        MathConcept(
            id="trigonometry",
            name="Trigonometry",
            description="Study of relationships between angles and sides of triangles",
            category="Pure Mathematics",
            related_concepts=["geometry"],
        )
    )
    return repo
