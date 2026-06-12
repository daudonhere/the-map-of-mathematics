from __future__ import annotations

from themap.core.models import MathConcept
from themap.core.repository import Repository


def seed_repo(repo: Repository) -> None:
    topics = [
        MathConcept(
            id="arithmetic",
            name="Arithmetic",
            description="The branch of mathematics dealing with basic operations on numbers: addition, subtraction, multiplication, and division.",
            category="Foundations",
            related_concepts=["algebra", "number-theory"],
        ),
        MathConcept(
            id="algebra",
            name="Algebra",
            description="The branch of mathematics that uses symbols and rules to manipulate equations and mathematical structures.",
            category="Algebra",
            related_concepts=["arithmetic", "linear-algebra", "abstract-algebra"],
        ),
        MathConcept(
            id="euclidean-geometry",
            name="Euclidean Geometry",
            description="The classical system of geometry based on Euclid's postulates, studying points, lines, planes, and space.",
            category="Geometry",
            related_concepts=["trigonometry", "differential-geometry", "topology"],
        ),
        MathConcept(
            id="trigonometry",
            name="Trigonometry",
            description="The branch of mathematics that studies relationships between angles and sides of triangles, and trigonometric functions.",
            category="Trigonometry",
            related_concepts=["euclidean-geometry", "calculus", "complex-analysis"],
        ),
        MathConcept(
            id="calculus",
            name="Calculus",
            description="The branch of mathematics studying change through derivatives and integrals, limits, and infinite series.",
            category="Analysis",
            related_concepts=["trigonometry", "real-analysis", "linear-algebra"],
        ),
        MathConcept(
            id="linear-algebra",
            name="Linear Algebra",
            description="The branch of mathematics studying vectors, vector spaces, matrices, and linear transformations.",
            category="Algebra",
            related_concepts=["algebra", "differential-geometry", "calculus"],
        ),
        MathConcept(
            id="discrete-mathematics",
            name="Discrete Mathematics",
            description="The branch of mathematics studying discrete structures such as graphs, sets, combinatorics, and logic.",
            category="Discrete Mathematics",
            related_concepts=["algebra", "number-theory", "probability-statistics"],
        ),
        MathConcept(
            id="probability-statistics",
            name="Probability & Statistics",
            description="The branch of mathematics studying chance, data collection, analysis, and statistical inference.",
            category="Probability",
            related_concepts=["discrete-mathematics", "calculus", "real-analysis"],
        ),
        MathConcept(
            id="real-analysis",
            name="Real Analysis",
            description="The rigorous study of real numbers, sequences, continuous functions, derivatives, and integrals.",
            category="Analysis",
            related_concepts=["calculus", "complex-analysis", "topology"],
        ),
        MathConcept(
            id="abstract-algebra",
            name="Abstract Algebra",
            description="The branch of mathematics studying algebraic structures such as groups, rings, fields, and modules.",
            category="Algebra",
            related_concepts=["algebra", "number-theory", "topology"],
        ),
        MathConcept(
            id="topology",
            name="Topology",
            description="The branch of mathematics studying properties of space that are invariant under continuous transformations.",
            category="Geometry",
            related_concepts=[
                "real-analysis",
                "differential-geometry",
                "abstract-algebra",
            ],
        ),
        MathConcept(
            id="number-theory",
            name="Number Theory",
            description="The branch of mathematics studying properties of integers and integer-valued functions.",
            category="Number Theory",
            related_concepts=["arithmetic", "abstract-algebra", "discrete-mathematics"],
        ),
        MathConcept(
            id="differential-geometry",
            name="Differential Geometry",
            description="The branch of mathematics using calculus and linear algebra to study curves, surfaces, and manifolds.",
            category="Geometry",
            related_concepts=["calculus", "linear-algebra", "topology"],
        ),
        MathConcept(
            id="complex-analysis",
            name="Complex Analysis",
            description="The branch of mathematics studying complex-valued functions that are differentiable (analytic functions).",
            category="Analysis",
            related_concepts=["real-analysis", "trigonometry", "topology"],
        ),
    ]
    for topic in topics:
        repo.add(topic)
