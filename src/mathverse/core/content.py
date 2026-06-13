# ruff: noqa: RUF001
from __future__ import annotations

from dataclasses import dataclass, field


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


_SUBTOPICS: dict[str, TopicContent] = {}


def _reg(concept_id: str, subtopics: list[SubTopic]) -> None:
    _SUBTOPICS[concept_id] = TopicContent(concept_id=concept_id, subtopics=subtopics)


def get_content(concept_id: str) -> TopicContent | None:
    return _SUBTOPICS.get(concept_id)


_arithmetic_subtopics = [
    SubTopic(
        title={"id": "Operasi Dasar", "en": "Basic Operations"},
        description={
            "id": (
                "Empat operasi fundamental yang menjadi dasar semua perhitungan matematika."
            ),
            "en": (
                "Four fundamental operations that form the basis of all mathematical calculations."
            ),
        },
        explanation={
            "id": (
                "Penjumlahan menggabungkan dua bilangan atau lebih menjadi satu jumlah total.\n"
                "Pengurangan mencari selisih atau jarak antara dua bilangan.\n"
                "Perkalian adalah cara cepat menjumlahkan bilangan yang sama secara berulang.\n"
                "Pembagian memisahkan suatu bilangan menjadi beberapa kelompok sama besar."
            ),
            "en": (
                "Addition combines two or more numbers into a single total sum.\n"
                "Subtraction finds the difference or distance between two numbers.\n"
                "Multiplication is a fast way to repeatedly add the same number.\n"
                "Division splits a number into several equal-sized groups."
            ),
        },
        examples={
            "id": [
                "Penjumlahan (+): 12 + 7 = 19",
                "Pengurangan (−): 24 − 9 = 15",
                "Perkalian (×): 6 × 8 = 48",
                "Pembagian (÷): 56 ÷ 7 = 8",
            ],
            "en": [
                "Addition (+): 12 + 7 = 19",
                "Subtraction (−): 24 − 9 = 15",
                "Multiplication (×): 6 × 8 = 48",
                "Division (÷): 56 ÷ 7 = 8",
            ],
        },
        playground="basic_ops",
    ),
    SubTopic(
        title={"id": "Jenis Bilangan", "en": "Types of Numbers"},
        description={
            "id": (
                "Bilangan diklasifikasikan ke dalam beberapa jenis berdasarkan sifat-sifatnya."
            ),
            "en": (
                "Numbers are classified into several types based on their properties."
            ),
        },
        explanation={
            "id": (
                "Bilangan asli dimulai dari 1: 1, 2, 3, 4, 5, ...\n"
                "Bilangan cacah mencakup juga nol: 0, 1, 2, 3, 4, ...\n"
                "Bilangan bulat mencakup bilangan negatif: ..., −3, −2, −1, 0, 1, 2, 3, ...\n"
                "Bilangan genap habis dibagi 2: ..., −4, −2, 0, 2, 4, ...\n"
                "Bilangan ganjil tidak habis dibagi 2: ..., −3, −1, 1, 3, 5, ...\n"
                "Bilangan prima hanya memiliki 2 faktor: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...\n"
                "Bilangan komposit memiliki lebih dari 2 faktor: 4, 6, 8, 9, 10, 12, ...\n"
                "Pecahan: 1/2, 3/4, 7/8, ... — terdiri dari pembilang dan penyebut.\n"
                "Desimal: 0.5, 3.14, 2.718, ... — bilangan dengan tanda koma, bentuk lain dari pecahan.\n"
                "Persen: 50%, 25%, 100%, ... — per seratus, sering digunakan dalam kehidupan sehari-hari."
            ),
            "en": (
                "Natural numbers start from 1: 1, 2, 3, 4, 5, ...\n"
                "Whole numbers include zero: 0, 1, 2, 3, 4, ...\n"
                "Integers include negatives: ..., −3, −2, −1, 0, 1, 2, 3, ...\n"
                "Even numbers are divisible by 2: ..., −4, −2, 0, 2, 4, ...\n"
                "Odd numbers are not divisible by 2: ..., −3, −1, 1, 3, 5, ...\n"
                "Prime numbers have exactly 2 factors: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...\n"
                "Composite numbers have more than 2 factors: 4, 6, 8, 9, 10, 12, ...\n"
                "Fractions: 1/2, 3/4, 7/8, ... — numerator over denominator.\n"
                "Decimals: 0.5, 3.14, 2.718, ... — numbers with decimal point, another form of fractions.\n"
                "Percentages: 50%, 25%, 100%, ... — per hundred, used widely in daily life."
            ),
        },
        examples={
            "id": [
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
            "en": [
                "Natural numbers: 1, 2, 3, 4, 5, ...",
                "Whole numbers: 0, 1, 2, 3, 4, ...",
                "Integers: ..., −3, −2, −1, 0, 1, 2, 3, ...",
                "Even numbers: ..., −4, −2, 0, 2, 4, ...",
                "Odd numbers: ..., −3, −1, 1, 3, 5, ...",
                "Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...",
                "Composite numbers: 4, 6, 8, 9, 10, 12, ...",
                "Fractions: 1/2, 3/4, 7/8, ...",
                "Decimals: 0.5, 3.14, 2.718, ...",
                "Percentages: 50%, 25%, 100%, ...",
            ],
        },
        playground="number_types",
    ),
    SubTopic(
        title={"id": "Sifat-Sifat Operasi", "en": "Properties of Operations"},
        description={
            "id": (
                "Sifat-sifat ini berlaku untuk operasi penjumlahan dan perkalian, "
                "memudahkan kita menghitung dengan lebih fleksibel."
            ),
            "en": (
                "These properties apply to addition and multiplication, "
                "making calculations more flexible."
            ),
        },
        explanation={
            "id": (
                "Sifat komutatif: a + b = b + a — urutan penjumlahan tidak mengubah hasil.\n"
                "8 + 5 = 5 + 8 = 13 — bukti sifat komutatif pada penjumlahan.\n"
                "4 × 7 = 7 × 4 = 28 — bukti sifat komutatif pada perkalian.\n"
                "Sifat asosiatif: (a + b) + c = a + (b + c) — pengelompokan tidak mengubah hasil.\n"
                "(3 + 4) + 6 = 3 + (4 + 6) = 13 — bukti sifat asosiatif pada penjumlahan.\n"
                "(2 × 5) × 3 = 2 × (5 × 3) = 30 — bukti sifat asosiatif pada perkalian.\n"
                "Sifat distributif: a × (b + c) = a × b + a × c — perkalian disebar ke penjumlahan.\n"
                "3 × (4 + 5) = 3 × 4 + 3 × 5 = 27 — bukti sifat distributif."
            ),
            "en": (
                "Commutative: a + b = b + a — the order of addition does not change the result.\n"
                "8 + 5 = 5 + 8 = 13 — proof of commutative property for addition.\n"
                "4 × 7 = 7 × 4 = 28 — proof of commutative property for multiplication.\n"
                "Associative: (a + b) + c = a + (b + c) — grouping does not change the result.\n"
                "(3 + 4) + 6 = 3 + (4 + 6) = 13 — proof of associative property for addition.\n"
                "(2 × 5) × 3 = 2 × (5 × 3) = 30 — proof of associative property for multiplication.\n"
                "Distributive: a × (b + c) = a × b + a × c — multiplication distributes over addition.\n"
                "3 × (4 + 5) = 3 × 4 + 3 × 5 = 27 — proof of distributive property."
            ),
        },
        examples={
            "id": [
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
            "en": [
                "Commutative: a + b = b + a",
                "  Example: 8 + 5 = 5 + 8 = 13",
                "  Example: 4 × 7 = 7 × 4 = 28",
                "",
                "Associative: (a + b) + c = a + (b + c)",
                "  Example: (3 + 4) + 6 = 3 + (4 + 6) = 13",
                "  Example: (2 × 5) × 3 = 2 × (5 × 3) = 30",
                "",
                "Distributive: a × (b + c) = a × b + a × c",
                "  Example: 3 × (4 + 5) = 3 × 4 + 3 × 5 = 27",
            ],
        },
        playground="properties",
    ),
    SubTopic(
        title={"id": "Pangkat dan Akar", "en": "Powers and Roots"},
        description={
            "id": (
                "Pangkat adalah perkalian berulang suatu bilangan, sedangkan akar "
                "adalah kebalikan dari pangkat."
            ),
            "en": (
                "A power is repeated multiplication of a number, while a root "
                "is the inverse of a power."
            ),
        },
        explanation={
            "id": (
                "5\u00b2 berarti 5 dikalikan dirinya sendiri sebanyak 2 kali = 25 — pangkat menunjukkan jumlah perkalian berulang.\n"
                "2\u00b3 berarti 2 × 2 × 2 = 8 — pangkat 3 disebut kubik.\n"
                "10\u2074 = 10 × 10 × 10 × 10 = 10.000 — pangkat menunjukkan posisi digit.\n"
                "\u221a25 = 5 karena 5\u00b2 = 25 — akar kuadrat adalah kebalikan dari pangkat 2.\n"
                "\u221a144 = 12 karena 12\u00b2 = 144 — akar kuadrat dari bilangan kuadrat sempurna.\n"
                "\u221b27 = 3 karena 3\u00b3 = 27 — akar kubik adalah kebalikan dari pangkat 3."
            ),
            "en": (
                "5\u00b2 means 5 multiplied by itself twice = 25 — exponent shows repeated multiplication count.\n"
                "2\u00b3 = 2 × 2 × 2 = 8 — exponent 3 is called cubed.\n"
                "10\u2074 = 10 × 10 × 10 × 10 = 10,000 — exponent shows digit position.\n"
                "\u221a25 = 5 because 5\u00b2 = 25 — square root is the inverse of squaring.\n"
                "\u221a144 = 12 because 12\u00b2 = 144 — square root of a perfect square.\n"
                "\u221b27 = 3 because 3\u00b3 = 27 — cube root is the inverse of cubing."
            ),
        },
        examples={
            "id": [
                "Pangkat: 5\u00b2 = 5 × 5 = 25",
                "Pangkat: 2\u00b3 = 2 × 2 × 2 = 8",
                "Pangkat: 10\u2074 = 10 × 10 × 10 × 10 = 10.000",
                "Akar: \u221a25 = 5 (karena 5\u00b2 = 25)",
                "Akar: \u221a144 = 12 (karena 12\u00b2 = 144)",
                "Akar: \u221b27 = 3 (karena 3\u00b3 = 27)",
            ],
            "en": [
                "Power: 5\u00b2 = 5 × 5 = 25",
                "Power: 2\u00b3 = 2 × 2 × 2 = 8",
                "Power: 10\u2074 = 10 × 10 × 10 × 10 = 10,000",
                "Root: \u221a25 = 5 (since 5\u00b2 = 25)",
                "Root: \u221a144 = 12 (since 12\u00b2 = 144)",
                "Root: \u221b27 = 3 (since 3\u00b3 = 27)",
            ],
        },
        playground="powers",
    ),
    SubTopic(
        title={"id": "Kelipatan dan Faktor", "en": "Multiples and Factors"},
        description={
            "id": (
                "Faktor adalah bilangan yang membagi habis bilangan lain. "
                "Kelipatan adalah hasil perkalian suatu bilangan dengan bilangan bulat."
            ),
            "en": (
                "Factors are numbers that divide another number evenly. "
                "Multiples are the product of a number with an integer."
            ),
        },
        explanation={
            "id": (
                "Faktor adalah bilangan yang dapat membagi habis bilangan lain tanpa sisa.\n"
                "Kelipatan adalah hasil perkalian suatu bilangan dengan bilangan bulat.\n"
                "FPB (Faktor Persekutuan Terbesar) adalah faktor terbesar yang dimiliki dua bilangan.\n"
                "KPK (Kelipatan Persekutuan Terkecil) adalah kelipatan terkecil yang dimiliki dua bilangan."
            ),
            "en": (
                "Factors are numbers that divide another number evenly with no remainder.\n"
                "Multiples are the product of a number multiplied by any integer.\n"
                "GCF is the largest factor shared by two or more numbers.\n"
                "LCM is the smallest multiple shared by two or more numbers."
            ),
        },
        examples={
            "id": [
                "Faktor dari 12: 1, 2, 3, 4, 6, 12",
                "Kelipatan dari 5: 5, 10, 15, 20, 25, ...",
                "FPB dari 12 dan 18: 6",
                "KPK dari 4 dan 6: 12",
            ],
            "en": [
                "Factors of 12: 1, 2, 3, 4, 6, 12",
                "Multiples of 5: 5, 10, 15, 20, 25, ...",
                "GCF of 12 and 18: 6",
                "LCM of 4 and 6: 12",
            ],
        },
        playground="factors",
    ),
    SubTopic(
        title={"id": "Rasio dan Proporsi", "en": "Ratios and Proportions"},
        description={
            "id": (
                "Rasio membandingkan dua bilangan, proporsi menyatakan "
                "kesamaan dua rasio."
            ),
            "en": (
                "A ratio compares two numbers, a proportion states "
                "that two ratios are equal."
            ),
        },
        explanation={
            "id": (
                "Rasio adalah perbandingan antara dua besaran yang menunjukkan hubungan nilai.\n"
                "Skala peta adalah rasio antara jarak pada peta dengan jarak sesungguhnya.\n"
                "Perbandingan senilai: kedua besaran berubah dengan faktor yang sama.\n"
                "Perbandingan berbalik nilai: satu besaran naik saat yang lain turun."
            ),
            "en": (
                "A ratio compares two quantities showing the relationship between their values.\n"
                "Map scale is the ratio between distance on map and actual distance.\n"
                "Direct proportion: both quantities change by the same factor.\n"
                "Inverse proportion: one quantity increases as the other decreases."
            ),
        },
        examples={
            "id": [
                "Perbandingan: 3 : 5 (dibaca 3 banding 5)",
                "Skala peta 1 : 100.000 berarti 1 cm = 1 km",
                "Perbandingan senilai: 2 kg = Rp10.000, 4 kg = Rp20.000",
                "Perbandingan berbalik nilai: 3 pekerja = 6 hari, 6 pekerja = 3 hari",
            ],
            "en": [
                "Ratio: 3 : 5 (read as 3 to 5)",
                "Map scale 1 : 100,000 means 1 cm = 1 km",
                "Direct proportion: 2 kg = $10, 4 kg = $20",
                "Inverse proportion: 3 workers = 6 days, 6 workers = 3 days",
            ],
        },
        playground="ratios",
    ),
    SubTopic(
        title={"id": "Persentase", "en": "Percentage"},
        description={
            "id": (
                "Persen berarti 'per seratus' (%). Digunakan dalam banyak "
                "aplikasi sehari-hari seperti diskon, pajak, keuntungan, dan bunga."
            ),
            "en": (
                "Percent means 'per hundred' (%). Used in many "
                "everyday applications such as discounts, taxes, profits, and interest."
            ),
        },
        explanation={
            "id": (
                "Diskon adalah potongan harga yang dihitung dari persentase harga awal.\n"
                "Pajak adalah kewajiban tambahan yang dihitung dari persentase nilai barang atau pendapatan.\n"
                "Keuntungan adalah selisih positif antara pendapatan dan modal, dinyatakan dalam persen.\n"
                "Bunga sederhana dihitung dari persentase modal dikalikan dengan jangka waktu."
            ),
            "en": (
                "Discount is a price reduction calculated as a percentage of the original price.\n"
                "Tax is an additional obligation calculated as a percentage of value or income.\n"
                "Profit is the positive difference between revenue and capital, expressed as a percentage.\n"
                "Simple interest is calculated as a percentage of principal multiplied by time period."
            ),
        },
        examples={
            "id": [
                "Diskon 25% dari Rp80.000 = Rp20.000, bayar Rp60.000",
                "Pajak 10% dari Rp5.000.000 = Rp500.000",
                "Keuntungan 15% dari modal Rp200.000 = Rp30.000",
                "Bunga sederhana: 5% per tahun dari Rp1.000.000 selama 2 tahun = Rp100.000",
            ],
            "en": [
                "25% discount on $80 = $20 off, pay $60",
                "10% tax on $5,000 = $500",
                "15% profit on $200 capital = $30",
                "Simple interest: 5% yearly on $1,000 for 2 years = $100",
            ],
        },
        playground="percentages",
    ),
    SubTopic(
        title={"id": "Metode Hitung Cepat (Mental Math)", "en": "Mental Math"},
        description={
            "id": (
                "Teknik menghitung cepat tanpa kalkulator. Metode ini "
                "menghemat waktu dan melatih otak untuk berpikir secara "
                "fleksibel dengan angka."
            ),
            "en": (
                "Fast calculation techniques without a calculator. These methods "
                "save time and train the brain to think flexibly with numbers."
            ),
        },
        explanation={
            "id": (
                "Kompensasi: 98 + 37 = 100 + 35 = 135 — pindahkan 2 dari 37 ke 98.\n"
                "Doubling & Halving: 25 × 16 = 50 × 8 = 400 — gandakan 25, bagi 16.\n"
                "Perkalian 11: 23 × 11 = 253 — (2, 2+3, 3) pisahkan dan jumlahkan di tengah.\n"
                "Bilangan dekat 100: 96 × 97 = (96−3)×100 + (4×3) = 9300 + 12 = 9312."
            ),
            "en": (
                "Compensation: 98 + 37 = 100 + 35 = 135 — move 2 from 37 to 98.\n"
                "Doubling & Halving: 25 × 16 = 50 × 8 = 400 — double 25, halve 16.\n"
                "Multiply by 11: 23 × 11 = 253 — (2, 2+3, 3) split and put sum in middle.\n"
                "Near 100: 96 × 97 = (96−3)×100 + (4×3) = 9300 + 12 = 9312."
            ),
        },
        examples={
            "id": [
                "Kompensasi: 98 + 37 = 100 + 35 = 135",
                "Doubling & Halving: 25 × 16 = 50 × 8 = 400",
                "Perkalian 11: 23 × 11 = 253 (2, 2+3, 3)",
                "Bilangan dekat 100: 96 × 97 = (96−3)×100 + (4×3) = 9300 + 12 = 9312",
            ],
            "en": [
                "Compensation: 98 + 37 = 100 + 35 = 135",
                "Doubling & Halving: 25 × 16 = 50 × 8 = 400",
                "Multiply by 11: 23 × 11 = 253 (2, 2+3, 3)",
                "Near 100: 96 × 97 = (96−3)×100 + (4×3) = 9300 + 12 = 9312",
            ],
        },
        playground="mental_math",
    ),
    SubTopic(
        title={"id": "Teori Bilangan Dasar", "en": "Basic Number Theory"},
        description={
            "id": (
                "Landasan teoritis dari aritmatika yang membahas sifat-sifat "
                "bilangan bulat."
            ),
            "en": (
                "The theoretical foundation of arithmetic that studies properties "
                "of integers."
            ),
        },
        explanation={
            "id": (
                "Faktorisasi prima 84 = 2\u00b2 × 3 × 7 — memecah 84 menjadi faktor-faktor prima.\n"
                "Sisa pembagian: 17 mod 5 = 2 — 17 dibagi 5 hasil 3 sisa 2.\n"
                "Bilangan sempurna 6 = 1 + 2 + 3 — jumlah semua faktor kecuali dirinya sendiri sama dengan bilangan itu.\n"
                "Bilangan Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... — setiap bilangan adalah jumlah dua bilangan sebelumnya."
            ),
            "en": (
                "Prime factorization 84 = 2\u00b2 × 3 × 7 — breaking 84 into prime factors.\n"
                "Remainder: 17 mod 5 = 2 — 17 divided by 5 is 3 remainder 2.\n"
                "Perfect number 6 = 1 + 2 + 3 — the sum of its proper divisors equals the number itself.\n"
                "Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... — each number is the sum of the two preceding ones."
            ),
        },
        examples={
            "id": [
                "Faktorisasi prima: 84 = 2\u00b2 × 3 × 7",
                "Sisa pembagian (modulo): 17 mod 5 = 2",
                "Bilangan sempurna: 6 = 1 + 2 + 3 (jumlah faktor kecuali 6)",
                "Bilangan Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...",
            ],
            "en": [
                "Prime factorization: 84 = 2\u00b2 × 3 × 7",
                "Remainder (modulo): 17 mod 5 = 2",
                "Perfect number: 6 = 1 + 2 + 3 (sum of proper divisors)",
                "Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...",
            ],
        },
        playground="number_theory",
    ),
]

_reg("arithmetic", _arithmetic_subtopics)
_reg("aritmatika", _arithmetic_subtopics)

_algebra_subtopics = [
    SubTopic(
        title={"id": "Variabel dan Konstanta", "en": "Variables and Constants"},
        description={
            "id": (
                "Variabel adalah simbol (huruf) yang mewakili bilangan tak diketahui. "
                "Konstanta adalah bilangan tetap yang nilainya tidak berubah."
            ),
            "en": (
                "Variables are symbols (letters) that represent unknown numbers. "
                "Constants are fixed numbers whose values do not change."
            ),
        },
        explanation={
            "id": (
                "x, y, z adalah variabel — simbol huruf yang mewakili bilangan yang belum diketahui nilainya.\n"
                "5, 10, −3 adalah konstanta — bilangan tetap yang nilainya tidak berubah.\n"
                "Dalam 3x + 5, x adalah variabel, 3 dan 5 adalah konstanta.\n"
                "Koefisien adalah konstanta yang mengalikan variabel, seperti 3 pada 3x."
            ),
            "en": (
                "x, y, z are variables — letter symbols representing unknown values.\n"
                "5, 10, −3 are constants — fixed numbers whose values do not change.\n"
                "In 3x + 5, x is the variable, 3 and 5 are constants.\n"
                "A coefficient is a constant that multiplies a variable, like 3 in 3x."
            ),
        },
        examples={
            "id": [
                "Variabel: x, y, z",
                "Konstanta: 5, 10, −3",
                "",
                "Bentuk: 3x + 5",
                "  x = variabel",
                "  3 dan 5 = konstanta",
            ],
            "en": [
                "Variables: x, y, z",
                "Constants: 5, 10, −3",
                "",
                "Expression: 3x + 5",
                "  x = variable",
                "  3 and 5 = constants",
            ],
        },
        playground="variables",
    ),
    SubTopic(
        title={"id": "Bentuk Aljabar", "en": "Algebraic Forms"},
        description={
            "id": (
                "Bentuk aljabar diklasifikasikan berdasarkan jumlah sukunya: "
                "monomial (1 suku), binomial (2 suku), trinomial (3 suku), "
                "dan polinomial (banyak suku)."
            ),
            "en": (
                "Algebraic forms are classified by the number of terms: "
                "monomial (1 term), binomial (2 terms), trinomial (3 terms), "
                "and polynomial (many terms)."
            ),
        },
        explanation={
            "id": (
                "Monomial memiliki satu suku: 5x, 7a² — hanya satu suku aljabar tanpa operasi tambah atau kurang.\n"
                "Binomial memiliki dua suku yang dipisah oleh + atau −: x + 3, 2a − b.\n"
                "Trinomial memiliki tiga suku: x² + 2x + 1 — sering muncul dalam persamaan kuadrat.\n"
                "Polinomial memiliki banyak suku dengan pangkat berbeda: x⁴ + 2x³ − x + 7."
            ),
            "en": (
                "A monomial has one term: 5x, 7a² — a single algebraic term with no addition or subtraction.\n"
                "A binomial has two terms separated by + or −: x + 3, 2a − b.\n"
                "A trinomial has three terms: x² + 2x + 1 — common in quadratic equations.\n"
                "A polynomial has many terms with different exponents: x⁴ + 2x³ − x + 7."
            ),
        },
        examples={
            "id": [
                "Monomial (1 suku): 5x, 7a²",
                "",
                "Binomial (2 suku): x + 3, 2a − b",
                "",
                "Trinomial (3 suku): x² + 2x + 1",
                "",
                "Polinomial (banyak): x⁴ + 2x³ − x + 7",
            ],
            "en": [
                "Monomial (1 term): 5x, 7a²",
                "",
                "Binomial (2 terms): x + 3, 2a − b",
                "",
                "Trinomial (3 terms): x² + 2x + 1",
                "",
                "Polynomial (many): x⁴ + 2x³ − x + 7",
            ],
        },
        playground="algebraic_forms",
    ),
    SubTopic(
        title={"id": "Operasi Aljabar", "en": "Algebraic Operations"},
        description={
            "id": (
                "Operasi aljabar meliputi penjumlahan, pengurangan, perkalian, "
                "dan pembagian suku-suku aljabar."
            ),
            "en": (
                "Algebraic operations include addition, subtraction, multiplication, "
                "and division of algebraic terms."
            ),
        },
        explanation={
            "id": (
                "Penjumlahan: jumlahkan koefisien dari suku yang sejenis. 3x + 2x = 5x.\n"
                "Pengurangan: kurangkan koefisien dari suku yang sejenis. 7y − 3y = 4y.\n"
                "Perkalian: kalikan setiap suku menggunakan sifat distributif. (x + 2)(x + 3) = x² + 5x + 6.\n"
                "Pembagian: bagi koefisien dan kurangkan pangkat variabel. (6x²)/(2x) = 3x."
            ),
            "en": (
                "Addition: add coefficients of like terms. 3x + 2x = 5x.\n"
                "Subtraction: subtract coefficients of like terms. 7y − 3y = 4y.\n"
                "Multiplication: multiply each term using the distributive property. (x + 2)(x + 3) = x² + 5x + 6.\n"
                "Division: divide coefficients and subtract exponents. (6x²)/(2x) = 3x."
            ),
        },
        examples={
            "id": [
                "Penjumlahan: 3x + 2x = 5x",
                "Pengurangan: 7y − 3y = 4y",
                "",
                "Perkalian: (x + 2)(x + 3)",
                "  = x² + 5x + 6",
                "",
                "Pembagian: (6x²)/(2x) = 3x",
            ],
            "en": [
                "Addition: 3x + 2x = 5x",
                "Subtraction: 7y − 3y = 4y",
                "",
                "Multiplication: (x + 2)(x + 3)",
                "  = x² + 5x + 6",
                "",
                "Division: (6x²)/(2x) = 3x",
            ],
        },
        playground="algebraic_ops",
    ),
    SubTopic(
        title={"id": "Faktorisasi", "en": "Factoring"},
        description={
            "id": (
                "Faktorisasi mengubah bentuk aljabar panjang menjadi perkalian faktor-faktornya."
            ),
            "en": (
                "Factoring transforms a long algebraic expression into a product of its factors."
            ),
        },
        explanation={
            "id": (
                "Faktorisasi adalah kebalikan dari perkalian — mengembalikan ekspresi ke faktor-faktornya.\n"
                "x² + 5x + 6 = (x + 2)(x + 3) — cari dua bilangan yang hasil kalinya 6 dan jumlahnya 5.\n"
                "Faktor persekutuan: 6x² + 9x = 3x(2x + 3) — keluarkan faktor yang sama dari setiap suku."
            ),
            "en": (
                "Factoring is the reverse of multiplication — breaking an expression into its factors.\n"
                "x² + 5x + 6 = (x + 2)(x + 3) — find two numbers whose product is 6 and sum is 5.\n"
                "Common factor: 6x² + 9x = 3x(2x + 3) — factor out the common term from each term."
            ),
        },
        examples={
            "id": [
                "x² + 5x + 6",
                "  = (x + 2)(x + 3)",
                "",
                "6x² + 9x",
                "  = 3x(2x + 3)",
            ],
            "en": [
                "x² + 5x + 6",
                "  = (x + 2)(x + 3)",
                "",
                "6x² + 9x",
                "  = 3x(2x + 3)",
            ],
        },
        playground="factoring",
    ),
    SubTopic(
        title={"id": "Identitas Kuadrat Sempurna", "en": "Perfect Square Identity"},
        description={
            "id": (
                "Identitas kuadrat sempurna menyatakan bahwa (a+b)² = a² + 2ab + b². "
                "Identitas ini menunjukkan hubungan antara kuadrat jumlah dua bilangan "
                "dengan jumlah kuadrat masing-masing ditambah dua kali hasil kalinya."
            ),
            "en": (
                "The perfect square identity states that (a+b)² = a² + 2ab + b². "
                "It shows the relationship between the square of a sum and the sum of "
                "individual squares plus twice their product."
            ),
        },
        explanation={
            "id": (
                "Jabarkan (x+3)² menjadi (x+3)(x+3), lalu gunakan sifat distributif.\n"
                "x·x = x², x·3 = 3x, 3·x = 3x, lalu jumlahkan suku sejenis.\n"
                "Hasil akhir: x² + 6x + 9 — ini bentuk kuadrat sempurna.\n"
                "Sekarang untuk (2a+5)², jabarkan dengan pola yang sama.\n"
                "(2a)² = 4a², 2·2a·5 = 20a, 5² = 25.\n"
                "Hasil akhir: 4a² + 20a + 25 — sesuai rumus (a+b)²."
            ),
            "en": (
                "Expand (x+3)² into (x+3)(x+3), then use the distributive property.\n"
                "x·x = x², x·3 = 3x, 3·x = 3x, then combine like terms.\n"
                "Final result: x² + 6x + 9 — this is a perfect square.\n"
                "Now for (2a+5)², expand using the same pattern.\n"
                "(2a)² = 4a², 2·2a·5 = 20a, 5² = 25.\n"
                "Final result: 4a² + 20a + 25 — matching the (a+b)² formula."
            ),
        },
        examples={
            "id": [
                "(x + 3)²",
                "  = x² + 2·x·3 + 3²",
                "  = x² + 6x + 9",
                "",
                "(2a + 5)²",
                "  = (2a)² + 2·2a·5 + 5²",
                "  = 4a² + 20a + 25",
            ],
            "en": [
                "(x + 3)²",
                "  = x² + 2·x·3 + 3²",
                "  = x² + 6x + 9",
                "",
                "(2a + 5)²",
                "  = (2a)² + 2·2a·5 + 5²",
                "  = 4a² + 20a + 25",
            ],
        },
        playground="perfect_square",
    ),
    SubTopic(
        title={
            "id": "Identitas Selisih Dua Kuadrat",
            "en": "Difference of Two Squares",
        },
        description={
            "id": (
                "Identitas selisih dua kuadrat menyatakan bahwa a² − b² = (a−b)(a+b). "
                "Identitas ini berguna untuk memfaktorkan bentuk kuadrat yang merupakan "
                "selisih dua bilangan kuadrat."
            ),
            "en": (
                "The difference of two squares identity states that a² − b² = (a−b)(a+b). "
                "This identity is useful for factoring quadratic forms that are the "
                "difference of two squares."
            ),
        },
        explanation={
            "id": (
                "x² − 25 adalah selisih dua kuadrat karena x² dan 25 adalah bilangan kuadrat.\n"
                "Tulis 25 sebagai 5², sehingga bentuknya menjadi x² − 5².\n"
                "Gunakan rumus a² − b² = (a−b)(a+b) dengan a=x, b=5.\n"
                "Sekarang untuk 9a² − 16: 9a² = (3a)² dan 16 = 4².\n"
                "Tulis sebagai (3a)² − 4², dengan a=3a, b=4.\n"
                "Hasil faktorisasi: (3a − 4)(3a + 4)."
            ),
            "en": (
                "x² − 25 is a difference of two squares because x² and 25 are square numbers.\n"
                "Write 25 as 5², so the expression becomes x² − 5².\n"
                "Apply the formula a² − b² = (a−b)(a+b) with a=x, b=5.\n"
                "Now for 9a² − 16: 9a² = (3a)² and 16 = 4².\n"
                "Write as (3a)² − 4², with a=3a, b=4.\n"
                "Factored result: (3a − 4)(3a + 4)."
            ),
        },
        examples={
            "id": [
                "x² − 25",
                "  = x² − 5²",
                "  = (x − 5)(x + 5)",
                "",
                "9a² − 16",
                "  = (3a)² − 4²",
                "  = (3a − 4)(3a + 4)",
            ],
            "en": [
                "x² − 25",
                "  = x² − 5²",
                "  = (x − 5)(x + 5)",
                "",
                "9a² − 16",
                "  = (3a)² − 4²",
                "  = (3a − 4)(3a + 4)",
            ],
        },
        playground="diff_squares",
    ),
]

_reg("algebra", _algebra_subtopics)
_reg("aljabar", _algebra_subtopics)
