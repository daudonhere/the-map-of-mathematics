from __future__ import annotations

from themap.core.models import MathConcept
from themap.core.repository import Repository


def seed_repo(repo: Repository) -> None:
    topics = [
        MathConcept(
            id="aritmatika",
            name="Aritmatika",
            description="Cabang matematika yang mempelajari operasi dasar bilangan seperti penjumlahan, pengurangan, perkalian, dan pembagian.",
            category="Dasar",
            related_concepts=["aljabar", "teori-bilangan"],
        ),
        MathConcept(
            id="aljabar",
            name="Aljabar",
            description="Cabang matematika yang menggunakan simbol dan aturan untuk memanipulasi persamaan dan struktur matematika.",
            category="Aljabar",
            related_concepts=["aritmatika", "aljabar-linear", "aljabar-abstrak"],
        ),
        MathConcept(
            id="geometri-euclid",
            name="Geometri Euclid",
            description="Sistem geometri klasik berdasarkan postulat Euclid, mempelajari titik, garis, bidang, dan ruang.",
            category="Geometri",
            related_concepts=["trigonometri", "geometri-diferensial", "topologi"],
        ),
        MathConcept(
            id="trigonometri",
            name="Trigonometri",
            description="Cabang matematika yang mempelajari hubungan antara sudut dan sisi segitiga serta fungsi trigonometri.",
            category="Trigonometri",
            related_concepts=["geometri-euclid", "kalkulus", "analisis-kompleks"],
        ),
        MathConcept(
            id="kalkulus",
            name="Kalkulus",
            description="Cabang matematika yang mempelajari perubahan melalui turunan dan integral, serta limit dan deret tak hingga.",
            category="Analisis",
            related_concepts=["trigonometri", "analisis-real", "aljabar-linear"],
        ),
        MathConcept(
            id="aljabar-linear",
            name="Aljabar Linear",
            description="Cabang matematika yang mempelajari vektor, ruang vektor, matriks, dan transformasi linear.",
            category="Aljabar",
            related_concepts=["aljabar", "geometri-diferensial", "kalkulus"],
        ),
        MathConcept(
            id="matematika-diskrit",
            name="Matematika Diskrit",
            description="Cabang matematika yang mempelajari struktur diskrit seperti graf, himpunan, kombinatorika, dan logika.",
            category="Matematika Diskrit",
            related_concepts=["aljabar", "teori-bilangan", "probabilitas-statistika"],
        ),
        MathConcept(
            id="probabilitas-statistika",
            name="Probabilitas & Statistika",
            description="Cabang matematika yang mempelajari peluang, pengumpulan data, analisis, dan inferensi statistik.",
            category="Probabilitas",
            related_concepts=["matematika-diskrit", "kalkulus", "analisis-real"],
        ),
        MathConcept(
            id="analisis-real",
            name="Analisis Real",
            description="Cabang matematika yang mempelajari bilangan real, barisan, fungsi kontinu, turunan, dan integral secara rigorous.",
            category="Analisis",
            related_concepts=["kalkulus", "analisis-kompleks", "topologi"],
        ),
        MathConcept(
            id="aljabar-abstrak",
            name="Aljabar Abstrak",
            description="Cabang matematika yang mempelajari struktur aljabar seperti grup, ring, field, dan modul.",
            category="Aljabar",
            related_concepts=["aljabar", "teori-bilangan", "topologi"],
        ),
        MathConcept(
            id="topologi",
            name="Topologi",
            description="Cabang matematika yang mempelajari sifat-sifat ruang yang invariant di bawah transformasi kontinu.",
            category="Geometri",
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
            related_concepts=["aritmatika", "aljabar-abstrak", "matematika-diskrit"],
        ),
        MathConcept(
            id="geometri-diferensial",
            name="Geometri Diferensial",
            description="Cabang matematika yang menggunakan kalkulus dan aljabar linear untuk mempelajari kurva, permukaan, dan manifold.",
            category="Geometri",
            related_concepts=["kalkulus", "aljabar-linear", "topologi"],
        ),
        MathConcept(
            id="analisis-kompleks",
            name="Analisis Kompleks",
            description="Cabang matematika yang mempelajari fungsi bernilai kompleks yang terdiferensiasi (fungsi analitik).",
            category="Analisis",
            related_concepts=["analisis-real", "trigonometri", "topologi"],
        ),
    ]
    for topic in topics:
        repo.add(topic)
