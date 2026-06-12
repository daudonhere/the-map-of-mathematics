# ruff: noqa: RUF001
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SubTopic:
    title: str
    explanation: str
    examples: list[str] = field(default_factory=list)
    playground: str | None = None


@dataclass
class TopicContent:
    concept_id: str
    subtopics: list[SubTopic] = field(default_factory=list)


_SUBTOPICS: dict[str, TopicContent] = {}


def _reg(concept_id: str, subtopics: list[SubTopic]) -> None:
    _SUBTOPICS[concept_id] = TopicContent(concept_id=concept_id, subtopics=subtopics)


def get_content(concept_id: str) -> TopicContent | None:
    return _SUBTOPICS.get(concept_id)


_reg("arithmetic", [
    SubTopic(
        title="Operasi Dasar",
        explanation=(
            "Empat operasi fundamental yang menjadi dasar semua perhitungan matematika. "
            "Penjumlahan menggabungkan dua bilangan, pengurangan mencari selisih, "
            "perkalian adalah penjumlahan berulang, dan pembagian adalah kebalikan perkalian."
        ),
        examples=[
            "Penjumlahan (+): 12 + 7 = 19",
            "Pengurangan (−): 24 − 9 = 15",
            "Perkalian (×): 6 × 8 = 48",
            "Pembagian (÷): 56 ÷ 7 = 8",
        ],
        playground="basic_ops",
    ),
    SubTopic(
        title="Jenis Bilangan",
        explanation=(
            "Bilangan diklasifikasikan ke dalam beberapa jenis berdasarkan sifat-sifatnya. "
            "Memahami jenis bilangan membantu dalam mempelajari topik matematika lebih lanjut."
        ),
        examples=[
            "Bilangan asli: 1, 2, 3, 4, 5, ...",
            "Bilangan cacah: 0, 1, 2, 3, 4, ...",
            "Bilangan bulat: ..., −3, −2, −1, 0, 1, 2, 3, ...",
            "Bilangan genap: ..., −4, −2, 0, 2, 4, ...",
            "Bilangan ganjil: ..., −3, −1, 1, 3, 5, ...",
            "Bilangan prima: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...",
            "Bilangan komposit: 4, 6, 8, 9, 10, 12, ...",
            "Pecahan: 1/2, 3/4, 7/8, ...",
            "Desimal: 0.5, 3.14, 2.718, ...",
            "Persen: 50%, 25%, 100%, ...",
        ],
    ),
    SubTopic(
        title="Sifat-Sifat Operasi",
        explanation=(
            "Sifat-sifat ini berlaku untuk operasi penjumlahan dan perkalian, "
            "memudahkan kita menghitung dengan lebih fleksibel."
        ),
        examples=[
            "Komutatif (Pertukaran): a + b = b + a",
            "  Contoh: 8 + 5 = 5 + 8 = 13",
            "  Contoh: 4 × 7 = 7 × 4 = 28",
            "",
            "Asosiatif (Pengelompokan): (a + b) + c = a + (b + c)",
            "  Contoh: (3 + 4) + 6 = 3 + (4 + 6) = 13",
            "  Contoh: (2 × 5) × 3 = 2 × (5 × 3) = 30",
            "",
            "Distributif: a × (b + c) = a × b + a × c",
            "  Contoh: 3 × (4 + 5) = 3 × 4 + 3 × 5 = 27",
        ],
        playground="properties",
    ),
    SubTopic(
        title="Pangkat dan Akar",
        explanation=(
            "Pangkat adalah perkalian berulang suatu bilangan, sedangkan akar "
            "adalah kebalikan dari pangkat. Misalnya, 3 pangkat 2 (3²) = 9, "
            "dan akar kuadrat dari 9 adalah 3."
        ),
        examples=[
            "Pangkat: 5² = 5 × 5 = 25",
            "Pangkat: 2³ = 2 × 2 × 2 = 8",
            "Pangkat: 10⁴ = 10 × 10 × 10 × 10 = 10.000",
            "Akar: √25 = 5 (karena 5² = 25)",
            "Akar: √144 = 12 (karena 12² = 144)",
            "Akar: ∛27 = 3 (karena 3³ = 27)",
        ],
        playground="powers",
    ),
    SubTopic(
        title="Kelipatan dan Faktor",
        explanation=(
            "Faktor adalah bilangan yang membagi habis bilangan lain. "
            "Kelipatan adalah hasil perkalian suatu bilangan dengan bilangan bulat. "
            "FPB adalah faktor terbesar yang sama, KPK adalah kelipatan terkecil yang sama."
        ),
        examples=[
            "Faktor dari 12: 1, 2, 3, 4, 6, 12",
            "Kelipatan dari 5: 5, 10, 15, 20, 25, ...",
            "FPB dari 12 dan 18: 6",
            "KPK dari 4 dan 6: 12",
        ],
    ),
    SubTopic(
        title="Rasio dan Proporsi",
        explanation=(
            "Rasio membandingkan dua bilangan, proporsi menyatakan "
            "kesamaan dua rasio. Konsep ini penting dalam skala peta, "
            "resep masakan, dan perbandingan senilai/berbalik nilai."
        ),
        examples=[
            "Perbandingan: 3 : 5 (dibaca 3 banding 5)",
            "Skala peta 1 : 100.000 berarti 1 cm = 1 km",
            "Perbandingan senilai: 2 kg = Rp10.000, 4 kg = Rp20.000",
            "Perbandingan berbalik nilai: 3 pekerja = 6 hari, 6 pekerja = 3 hari",
        ],
    ),
    SubTopic(
        title="Persentase",
        explanation=(
            "Persen berarti 'per seratus' (%). Digunakan dalam banyak "
            "aplikasi sehari-hari seperti diskon, pajak, keuntungan, "
            "dan bunga."
        ),
        examples=[
            "Diskon 25% dari Rp80.000 = Rp20.000, bayar Rp60.000",
            "Pajak 10% dari Rp5.000.000 = Rp500.000",
            "Keuntungan 15% dari modal Rp200.000 = Rp30.000",
            "Bunga sederhana: 5% per tahun dari Rp1.000.000 selama 2 tahun = Rp100.000",
        ],
    ),
    SubTopic(
        title="Metode Hitung Cepat (Mental Math)",
        explanation=(
            "Teknik menghitung cepat tanpa kalkulator. Metode ini "
            "menghemat waktu dan melatih otak untuk berpikir secara "
            "fleksibel dengan angka."
        ),
        examples=[
            "Kompensasi: 98 + 37 = 100 + 35 = 135",
            "Doubling & Halving: 25 × 16 = 50 × 8 = 400",
            "Perkalian 11: 23 × 11 = 253 (2, 2+3, 3)",
            "Bilangan dekat 100: 96 × 97 = (96−3)×100 + (4×3) = 9300 + 12 = 9312",
        ],
        playground="mental_math",
    ),
    SubTopic(
        title="Teori Bilangan Dasar",
        explanation=(
            "Landasan teoritis dari aritmatika yang membahas sifat-sifat "
            "bilangan bulat. Sering dianggap sebagai jembatan menuju "
            "matematika yang lebih abstrak."
        ),
        examples=[
            "Faktorisasi prima: 84 = 2² × 3 × 7",
            "Sisa pembagian (modulo): 17 mod 5 = 2",
            "Bilangan sempurna: 6 = 1 + 2 + 3 (faktor kecuali 6)",
            "Bilangan Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...",
        ],
    ),
])
