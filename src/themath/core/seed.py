from __future__ import annotations

from themath.core.models import MathConcept
from themath.core.repository import Repository


def seed_repo_en(repo: Repository) -> None:
    topics = [
        MathConcept(
            id="arithmetic",
            name="Arithmetic",
            description="The branch of mathematics dealing with basic operations on numbers: addition, subtraction, multiplication, and division.",
            category="Foundations",
            locale="en",
            related_concepts=["algebra", "number-theory"],
        ),
        MathConcept(
            id="algebra",
            name="Algebra",
            description="The branch of mathematics that uses symbols and rules to manipulate equations and mathematical structures.",
            category="Algebra",
            locale="en",
            related_concepts=["arithmetic", "linear-algebra", "abstract-algebra"],
        ),
        MathConcept(
            id="euclidean-geometry",
            name="Euclidean Geometry",
            description="The classical system of geometry based on Euclid's postulates, studying points, lines, planes, and space.",
            category="Geometry",
            locale="en",
            related_concepts=["trigonometry", "differential-geometry", "topology"],
        ),
        MathConcept(
            id="trigonometry",
            name="Trigonometry",
            description="The branch of mathematics that studies relationships between angles and sides of triangles, and trigonometric functions.",
            category="Trigonometry",
            locale="en",
            related_concepts=["euclidean-geometry", "calculus", "complex-analysis"],
        ),
        MathConcept(
            id="calculus",
            name="Calculus",
            description="The branch of mathematics studying change through derivatives and integrals, limits, and infinite series.",
            category="Analysis",
            locale="en",
            related_concepts=["trigonometry", "real-analysis", "linear-algebra"],
        ),
        MathConcept(
            id="linear-algebra",
            name="Linear Algebra",
            description="The branch of mathematics studying vectors, vector spaces, matrices, and linear transformations.",
            category="Algebra",
            locale="en",
            related_concepts=["algebra", "differential-geometry", "calculus"],
        ),
        MathConcept(
            id="discrete-mathematics",
            name="Discrete Mathematics",
            description="The branch of mathematics studying discrete structures such as graphs, sets, combinatorics, and logic.",
            category="Discrete Mathematics",
            locale="en",
            related_concepts=["algebra", "number-theory", "probability-statistics"],
        ),
        MathConcept(
            id="probability-statistics",
            name="Probability & Statistics",
            description="The branch of mathematics studying chance, data collection, analysis, and statistical inference.",
            category="Probability",
            locale="en",
            related_concepts=["discrete-mathematics", "calculus", "real-analysis"],
        ),
        MathConcept(
            id="real-analysis",
            name="Real Analysis",
            description="The rigorous study of real numbers, sequences, continuous functions, derivatives, and integrals.",
            category="Analysis",
            locale="en",
            related_concepts=["calculus", "complex-analysis", "topology"],
        ),
        MathConcept(
            id="abstract-algebra",
            name="Abstract Algebra",
            description="The branch of mathematics studying algebraic structures such as groups, rings, fields, and modules.",
            category="Algebra",
            locale="en",
            related_concepts=["algebra", "number-theory", "topology"],
        ),
        MathConcept(
            id="topology",
            name="Topology",
            description="The branch of mathematics studying properties of space that are invariant under continuous transformations.",
            category="Geometry",
            locale="en",
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
            locale="en",
            related_concepts=["arithmetic", "abstract-algebra", "discrete-mathematics"],
        ),
        MathConcept(
            id="differential-geometry",
            name="Differential Geometry",
            description="The branch of mathematics using calculus and linear algebra to study curves, surfaces, and manifolds.",
            category="Geometry",
            locale="en",
            related_concepts=["calculus", "linear-algebra", "topology"],
        ),
        MathConcept(
            id="complex-analysis",
            name="Complex Analysis",
            description="The branch of mathematics studying complex-valued functions that are differentiable (analytic functions).",
            category="Analysis",
            locale="en",
            related_concepts=["real-analysis", "trigonometry", "topology"],
        ),
    ]
    for topic in topics:
        repo.add(topic)


def seed_repo_id(repo: Repository) -> None:
    topics = [
        MathConcept(
            id="aritmatika",
            name="Aritmatika",
            description="Cabang matematika yang mempelajari operasi dasar bilangan: penjumlahan, pengurangan, perkalian, dan pembagian.",
            category="Dasar",
            locale="id",
            related_concepts=["aljabar", "teori-bilangan"],
        ),
        MathConcept(
            id="aljabar",
            name="Aljabar",
            description="Cabang matematika yang menggunakan simbol dan aturan untuk memanipulasi persamaan dan struktur matematika.",
            category="Aljabar",
            locale="id",
            related_concepts=["aritmatika", "aljabar-linear", "aljabar-abstrak"],
        ),
        MathConcept(
            id="geometri-euclid",
            name="Geometri Euclid",
            description="Sistem geometri klasik berdasarkan postulat Euclid, mempelajari titik, garis, bidang, dan ruang.",
            category="Geometri",
            locale="id",
            related_concepts=["trigonometri", "geometri-diferensial", "topologi"],
        ),
        MathConcept(
            id="trigonometri",
            name="Trigonometri",
            description="Cabang matematika yang mempelajari hubungan sudut dan sisi segitiga serta fungsi trigonometri.",
            category="Trigonometri",
            locale="id",
            related_concepts=["geometri-euclid", "kalkulus", "analisis-kompleks"],
        ),
        MathConcept(
            id="kalkulus",
            name="Kalkulus",
            description="Cabang matematika yang mempelajari perubahan melalui turunan dan integral, limit, serta deret tak hingga.",
            category="Analisis",
            locale="id",
            related_concepts=["trigonometri", "analisis-real", "aljabar-linear"],
        ),
        MathConcept(
            id="aljabar-linear",
            name="Aljabar Linear",
            description="Cabang matematika yang mempelajari vektor, ruang vektor, matriks, dan transformasi linear.",
            category="Aljabar",
            locale="id",
            related_concepts=["aljabar", "geometri-diferensial", "kalkulus"],
        ),
        MathConcept(
            id="matematika-diskrit",
            name="Matematika Diskrit",
            description="Cabang matematika yang mempelajari struktur diskrit seperti graf, himpunan, kombinatorika, dan logika.",
            category="Matematika Diskrit",
            locale="id",
            related_concepts=["aljabar", "teori-bilangan", "probabilitas-statistika"],
        ),
        MathConcept(
            id="probabilitas-statistika",
            name="Probabilitas & Statistika",
            description="Cabang matematika yang mempelajari peluang, pengumpulan data, analisis, dan inferensi statistik.",
            category="Probabilitas",
            locale="id",
            related_concepts=["matematika-diskrit", "kalkulus", "analisis-real"],
        ),
        MathConcept(
            id="analisis-real",
            name="Analisis Real",
            description="Cabang matematika yang mempelajari bilangan real, barisan, fungsi kontinu, turunan, dan integral secara rigor.",
            category="Analisis",
            locale="id",
            related_concepts=["kalkulus", "analisis-kompleks", "topologi"],
        ),
        MathConcept(
            id="aljabar-abstrak",
            name="Aljabar Abstrak",
            description="Cabang matematika yang mempelajari struktur aljabar seperti grup, ring, field, dan modul.",
            category="Aljabar",
            locale="id",
            related_concepts=["aljabar", "teori-bilangan", "topologi"],
        ),
        MathConcept(
            id="topologi",
            name="Topologi",
            description="Cabang matematika yang mempelajari sifat-sifat ruang yang invariant di bawah transformasi kontinu.",
            category="Geometri",
            locale="id",
            related_concepts=[
                "analisis-real",
                "geometri-diferensial",
                "aljabar-abstrak",
            ],
        ),
        MathConcept(
            id="teori-bilangan",
            name="Teori Bilangan",
            description="Cabang matematika yang mempelajari sifat-sifat bilangan bulat dan fungsi bernilai bulat.",
            category="Teori Bilangan",
            locale="id",
            related_concepts=["aritmatika", "aljabar-abstrak", "matematika-diskrit"],
        ),
        MathConcept(
            id="geometri-diferensial",
            name="Geometri Diferensial",
            description="Cabang matematika yang menggunakan kalkulus dan aljabar linear untuk mempelajari kurva, permukaan, dan manifold.",
            category="Geometri",
            locale="id",
            related_concepts=["kalkulus", "aljabar-linear", "topologi"],
        ),
        MathConcept(
            id="analisis-kompleks",
            name="Analisis Kompleks",
            description="Cabang matematika yang mempelajari fungsi bernilai kompleks yang terdiferensiasi (fungsi analitik).",
            category="Analisis",
            locale="id",
            related_concepts=["analisis-real", "trigonometri", "topologi"],
        ),
    ]
    for topic in topics:
        repo.add(topic)


def seed_repo(repo: Repository) -> None:
    seed_repo_en(repo)
    seed_repo_id(repo)
