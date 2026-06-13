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
        title={"id": "Variabel dan Ekspresi", "en": "Variables and Expressions"},
        description={
            "id": (
                "Variabel adalah simbol (biasanya huruf) yang mewakili bilangan yang tidak diketahui. "
                "Ekspresi aljabar adalah kombinasi variabel, konstanta, dan operasi matematika."
            ),
            "en": (
                "A variable is a symbol (usually a letter) that represents an unknown number. "
                "An algebraic expression is a combination of variables, constants, and mathematical operations."
            ),
        },
        explanation={
            "id": (
                "Ekspresi 2x + 3 memiliki variabel x, konstanta 3, dan koefisien 2.\n"
                "5a\u00b2 \u2212 2b + 7 memiliki dua variabel a dan b dengan pangkat berbeda.\n"
                "Evaluasi: jika x = 4, maka 3x + 2 = 3(4) + 2 = 14 — substitusi nilai x.\n"
                "Suku sejenis: 3x + 2x = 5x — koefisien dijumlahkan, variabel tetap."
            ),
            "en": (
                "Expression 2x + 3 has variable x, constant 3, and coefficient 2.\n"
                "5a\u00b2 \u2212 2b + 7 has two variables a and b with different exponents.\n"
                "Evaluate: if x = 4, then 3x + 2 = 3(4) + 2 = 14 — substitute x.\n"
                "Like terms: 3x + 2x = 5x — coefficients are added, variable stays the same."
            ),
        },
        examples={
            "id": [
                "Ekspresi: 2x + 3 (x adalah variabel)",
                "Ekspresi: 5a\u00b2 \u2212 2b + 7",
                "Evaluasi: Jika x = 4, maka 3x + 2 = 3(4) + 2 = 14",
                "Suku sejenis: 3x + 2x = 5x",
            ],
            "en": [
                "Expression: 2x + 3 (x is the variable)",
                "Expression: 5a\u00b2 \u2212 2b + 7",
                "Evaluate: If x = 4, then 3x + 2 = 3(4) + 2 = 14",
                "Like terms: 3x + 2x = 5x",
            ],
        },
        playground="expressions",
    ),
    SubTopic(
        title={"id": "Persamaan Linear Satu Variabel", "en": "Linear Equations in One Variable"},
        description={
            "id": (
                "Persamaan linear satu variabel memiliki bentuk ax + b = c. "
                "Tujuannya adalah mencari nilai x yang memenuhi persamaan."
            ),
            "en": (
                "A linear equation in one variable has the form ax + b = c. "
                "The goal is to find the value of x that satisfies the equation."
            ),
        },
        explanation={
            "id": (
                "3x + 7 = 22: kurangi kedua ruas dengan 7 untuk mengisolasi suku yang mengandung x.\n"
                "3x = 15 — suku x sudah terisolasi di ruas kiri.\n"
                "x = 5 — bagi kedua ruas dengan 3 untuk mendapatkan nilai x.\n"
                "5x − 8 = 2x + 10: kumpulkan suku x di kiri dan konstanta di kanan.\n"
                "5x − 2x = 10 + 8 — pindahkan 2x ke kiri dan −8 ke kanan (tanda berubah).\n"
                "3x = 18 — sederhanakan kedua ruas.\n"
                "x = 6 — bagi kedua ruas dengan 3."
            ),
            "en": (
                "3x + 7 = 22: subtract 7 from both sides to isolate the term with x.\n"
                "3x = 15 — the x term is isolated on the left.\n"
                "x = 5 — divide both sides by 3 to get the value of x.\n"
                "5x − 8 = 2x + 10: gather x terms on left, constants on right.\n"
                "5x − 2x = 10 + 8 — move 2x to the left and −8 to the right (signs change).\n"
                "3x = 18 — simplify both sides.\n"
                "x = 6 — divide both sides by 3."
            ),
        },
        examples={
            "id": [
                "Selesaikan 3x + 7 = 22",
                "  3x = 22 \u2212 7 = 15",
                "  x = 15 \u00f7 3 = 5",
                "",
                "Selesaikan 5x \u2212 8 = 2x + 10",
                "  5x \u2212 2x = 10 + 8",
                "  3x = 18",
                "  x = 6",
            ],
            "en": [
                "Solve 3x + 7 = 22",
                "  3x = 22 \u2212 7 = 15",
                "  x = 15 \u00f7 3 = 5",
                "",
                "Solve 5x \u2212 8 = 2x + 10",
                "  5x \u2212 2x = 10 + 8",
                "  3x = 18",
                "  x = 6",
            ],
        },
        playground="equations",
    ),
    SubTopic(
        title={"id": "Sistem Persamaan Linear", "en": "Systems of Linear Equations"},
        description={
            "id": (
                "Sistem persamaan linear terdiri dari dua atau lebih persamaan linear. "
                "Solusinya adalah nilai variabel yang memenuhi semua persamaan."
            ),
            "en": (
                "A system of linear equations consists of two or more linear equations. "
                "The solution is the values of variables that satisfy all equations."
            ),
        },
        explanation={
            "id": (
                "Sistem persamaan linear terdiri dari dua persamaan yang harus diselesaikan bersama.\n"
                "Metode eliminasi: jumlahkan persamaan untuk menghilangkan salah satu variabel.\n"
                "2x = 12, maka x = 6 — nilai x ditemukan dari hasil eliminasi.\n"
                "Substitusi x = 6 ke salah satu persamaan untuk mencari nilai y.\n"
                "Solusi (6, 4) adalah pasangan nilai yang memenuhi kedua persamaan secara bersamaan."
            ),
            "en": (
                "A system of linear equations consists of two equations solved together.\n"
                "Elimination method: add equations to cancel out one variable.\n"
                "2x = 12, so x = 6 — the value of x is found from elimination.\n"
                "Substitute x = 6 into one equation to find the value of y.\n"
                "Solution (6, 4) is the pair of values that satisfies both equations simultaneously."
            ),
        },
        examples={
            "id": [
                "Sistem:  x + y = 10",
                "          x \u2212 y = 2",
                "Eliminasi: 2x = 12 \u2192 x = 6",
                "Substitusi: 6 + y = 10 \u2192 y = 4",
                "Solusi: (6, 4)",
            ],
            "en": [
                "System:  x + y = 10",
                "         x \u2212 y = 2",
                "Elimination: 2x = 12 \u2192 x = 6",
                "Substitution: 6 + y = 10 \u2192 y = 4",
                "Solution: (6, 4)",
            ],
        },
        playground="systems",
    ),
    SubTopic(
        title={"id": "Polinomial", "en": "Polynomials"},
        description={
            "id": (
                "Polinomial adalah ekspresi aljabar dengan satu atau lebih suku. "
                "Derajat polinomial ditentukan oleh pangkat tertinggi variabelnya."
            ),
            "en": (
                "A polynomial is an algebraic expression with one or more terms. "
                "The degree of a polynomial is determined by the highest exponent of its variable."
            ),
        },
        explanation={
            "id": (
                "Monomial adalah polinomial yang hanya memiliki satu suku, seperti 5x\u00b3.\n"
                "Binomial adalah polinomial dengan dua suku yang dipisah operasi tambah atau kurang.\n"
                "Trinomial adalah polinomial dengan tiga suku, sering muncul dalam persamaan kuadrat.\n"
                "Penjumlahan polinomial: jumlahkan koefisien dari suku-suku yang memiliki variabel sama.\n"
                "Perkalian polinomial: kalikan setiap suku dalam kurung pertama dengan setiap suku dalam kurung kedua."
            ),
            "en": (
                "A monomial is a polynomial with only one term, such as 5x\u00b3.\n"
                "A binomial is a polynomial with two terms separated by addition or subtraction.\n"
                "A trinomial is a polynomial with three terms, often seen in quadratic equations.\n"
                "Adding polynomials: add the coefficients of terms that have the same variable and exponent.\n"
                "Multiplying polynomials: multiply each term in the first parenthesis by each term in the second."
            ),
        },
        examples={
            "id": [
                "Monomial: 5x\u00b3 (satu suku)",
                "Binomial: 3x\u00b2 + 2x (dua suku)",
                "Trinomial: x\u00b2 \u2212 5x + 6 (tiga suku)",
                "",
                "Penjumlahan: (2x\u00b2 + 3x \u2212 1) + (x\u00b2 \u2212 2x + 4) = 3x\u00b2 + x + 3",
                "Perkalian: (x + 2)(x + 3) = x\u00b2 + 5x + 6",
            ],
            "en": [
                "Monomial: 5x\u00b3 (one term)",
                "Binomial: 3x\u00b2 + 2x (two terms)",
                "Trinomial: x\u00b2 \u2212 5x + 6 (three terms)",
                "",
                "Addition: (2x\u00b2 + 3x \u2212 1) + (x\u00b2 \u2212 2x + 4) = 3x\u00b2 + x + 3",
                "Multiplication: (x + 2)(x + 3) = x\u00b2 + 5x + 6",
            ],
        },
        playground="polynomials",
    ),
    SubTopic(
        title={"id": "Faktorisasi", "en": "Factoring"},
        description={
            "id": (
                "Faktorisasi adalah proses memecah ekspresi aljabar menjadi faktor-faktor "
                "yang jika dikalikan menghasilkan ekspresi awal."
            ),
            "en": (
                "Factoring is the process of breaking an algebraic expression into factors "
                "that when multiplied produce the original expression."
            ),
        },
        explanation={
            "id": (
                "Faktor persekutuan: keluarkan faktor yang sama dari semua suku dalam ekspresi.\n"
                "Selisih kuadrat: a\u00b2 \u2212 b\u00b2 = (a+b)(a\u2212b), berlaku ketika bentuk kuadrat dikurangkan.\n"
                "Trinomial x\u00b2 + 5x + 6: cari dua bilangan yang hasil kalinya 6 dan jumlahnya 5.\n"
                "Trinomial x\u00b2 \u2212 7x + 12: cari dua bilangan yang hasil kalinya 12 dan jumlahnya \u22127."
            ),
            "en": (
                "Common factor: factor out the term shared by all terms in the expression.\n"
                "Difference of squares: a\u00b2 \u2212 b\u00b2 = (a+b)(a\u2212b), applies when subtracting squares.\n"
                "Trinomial x\u00b2 + 5x + 6: find two numbers whose product is 6 and sum is 5.\n"
                "Trinomial x\u00b2 \u2212 7x + 12: find two numbers whose product is 12 and sum is \u22127."
            ),
        },
        examples={
            "id": [
                "Faktor persekutuan: 6x\u00b2 + 9x = 3x(2x + 3)",
                "Selisih kuadrat: x\u00b2 \u2212 16 = (x + 4)(x \u2212 4)",
                "Trinomial: x\u00b2 + 5x + 6 = (x + 2)(x + 3)",
                "Trinomial: x\u00b2 \u2212 7x + 12 = (x \u2212 3)(x \u2212 4)",
            ],
            "en": [
                "Common factor: 6x\u00b2 + 9x = 3x(2x + 3)",
                "Difference of squares: x\u00b2 \u2212 16 = (x + 4)(x \u2212 4)",
                "Trinomial: x\u00b2 + 5x + 6 = (x + 2)(x + 3)",
                "Trinomial: x\u00b2 \u2212 7x + 12 = (x \u2212 3)(x \u2212 4)",
            ],
        },
        playground="factoring",
    ),
    SubTopic(
        title={"id": "Persamaan Kuadrat", "en": "Quadratic Equations"},
        description={
            "id": (
                "Persamaan kuadrat memiliki bentuk ax\u00b2 + bx + c = 0."
            ),
            "en": (
                "A quadratic equation has the form ax\u00b2 + bx + c = 0."
            ),
        },
        explanation={
            "id": (
                "x\u00b2 − 5x + 6 = 0: cari dua bilangan yang hasil kali 6 dan jumlah −5.\n"
                "(x − 2)(x − 3) = 0 — bentuk faktor: bilangan tersebut adalah −2 dan −3.\n"
                "Jika hasil kali = 0, salah satu faktor harus = 0: x = 2 atau x = 3.\n"
                "x\u00b2 + 6x + 5 = 0: selesaikan dengan rumus kuadrat.\n"
                "x = (\u22126 \u00b1 \u221a(36 \u2212 20)) / 2 — substitusi a=1, b=6, c=5 ke rumus.\n"
                "x = (\u22126 \u00b1 \u221a16)/2 = (\u22126 \u00b1 4)/2 — diskriminan = 16.\n"
                "x = (\u22126 + 4)/2 = \u22121, x = (\u22126 \u2212 4)/2 = \u22125 — dua solusi berbeda."
            ),
            "en": (
                "x\u00b2 − 5x + 6 = 0: find two numbers whose product is 6 and sum is −5.\n"
                "(x − 2)(x − 3) = 0 — factored form: those numbers are −2 and −3.\n"
                "If product = 0, one factor must be 0: x = 2 or x = 3.\n"
                "x\u00b2 + 6x + 5 = 0: solve using the quadratic formula.\n"
                "x = (\u22126 \u00b1 \u221a(36 \u2212 20)) / 2 — substitute a=1, b=6, c=5 into the formula.\n"
                "x = (\u22126 \u00b1 \u221a16)/2 = (\u22126 \u00b1 4)/2 — discriminant = 16.\n"
                "x = (\u22126 + 4)/2 = \u22121, x = (\u22126 \u2212 4)/2 = \u22125 — two distinct solutions."
            ),
        },
        examples={
            "id": [
                "Faktorisasi: x\u00b2 \u2212 5x + 6 = 0",
                "  (x \u2212 2)(x \u2212 3) = 0",
                "  x = 2 atau x = 3",
                "",
                "Rumus kuadrat: x\u00b2 + 6x + 5 = 0",
                "  x = (\u22126 \u00b1 \u221a(36 \u2212 20)) / 2",
                "  x = (\u22126 \u00b1 4) / 2",
                "  x = \u22121 atau x = \u22125",
            ],
            "en": [
                "Factoring: x\u00b2 \u2212 5x + 6 = 0",
                "  (x \u2212 2)(x \u2212 3) = 0",
                "  x = 2 or x = 3",
                "",
                "Quadratic formula: x\u00b2 + 6x + 5 = 0",
                "  x = (\u22126 \u00b1 \u221a(36 \u2212 20)) / 2",
                "  x = (\u22126 \u00b1 4) / 2",
                "  x = \u22121 or x = \u22125",
            ],
        },
        playground="quadratics",
    ),
    SubTopic(
        title={"id": "Fungsi", "en": "Functions"},
        description={
            "id": (
                "Fungsi adalah relasi yang memasangkan setiap input dengan tepat satu output."
            ),
            "en": (
                "A function is a relation that pairs each input with exactly one output."
            ),
        },
        explanation={
            "id": (
                "f(x) = 2x + 1 adalah fungsi linear — grafiknya berupa garis lurus dengan kemiringan 2.\n"
                "f(3) = 2(3) + 1 = 7 — substitusi x = 3 ke dalam rumus fungsi.\n"
                "f(x) = x\u00b2 adalah fungsi kuadrat — grafiknya berbentuk parabola.\n"
                "f(\u22123) = (\u22123)\u00b2 = 9 — bilangan negatif dikuadratkan menjadi positif.\n"
                "Komposisi fungsi: f(g(x)) artinya g(x) dimasukkan ke dalam f(x).\n"
                "f(g(3)) = f(4) = 8 — hitung g(3) = 4, lalu f(4) = 8."
            ),
            "en": (
                "f(x) = 2x + 1 is a linear function — its graph is a straight line with slope 2.\n"
                "f(3) = 2(3) + 1 = 7 — substitute x = 3 into the function formula.\n"
                "f(x) = x\u00b2 is a quadratic function — its graph is a parabola.\n"
                "f(\u22123) = (\u22123)\u00b2 = 9 — a negative number squared becomes positive.\n"
                "Function composition: f(g(x)) means plug g(x) into f(x).\n"
                "f(g(3)) = f(4) = 8 — compute g(3) = 4, then f(4) = 8."
            ),
        },
        examples={
            "id": [
                "Fungsi linear: f(x) = 2x + 1",
                "  f(3) = 2(3) + 1 = 7",
                "",
                "Fungsi kuadrat: f(x) = x\u00b2",
                "  f(\u22123) = (\u22123)\u00b2 = 9",
                "",
                "Komposisi: f(x) = 2x, g(x) = x + 1",
                "  f(g(3)) = f(4) = 8",
            ],
            "en": [
                "Linear function: f(x) = 2x + 1",
                "  f(3) = 2(3) + 1 = 7",
                "",
                "Quadratic function: f(x) = x\u00b2",
                "  f(\u22123) = (\u22123)\u00b2 = 9",
                "",
                "Composition: f(x) = 2x, g(x) = x + 1",
                "  f(g(3)) = f(4) = 8",
            ],
        },
        playground="functions",
    ),
    SubTopic(
        title={"id": "Pertidaksamaan", "en": "Inequalities"},
        description={
            "id": (
                "Pertidaksamaan menggunakan simbol >, <, \u2265, \u2264."
            ),
            "en": (
                "Inequalities use symbols >, <, \u2265, \u2264."
            ),
        },
        explanation={
            "id": (
                "2x + 3 > 7: selesaikan seperti persamaan, tetapi perhatikan tanda >.\n"
                "2x > 4 — kurangi kedua ruas dengan 3 (tanda tidak berubah).\n"
                "x > 2 — bagi kedua ruas dengan 2, tanda tetap karena 2 positif.\n"
                "\u22123x + 5 \u2264 11: perhatikan koefisien x negatif.\n"
                "\u22123x \u2264 6 — kurangi kedua ruas dengan 5.\n"
                "x \u2265 \u22122 — bagi dengan \u22123, tanda \u2264 dibalik menjadi \u2265.\n"
                "Garis bilangan: x > 2 digambar dengan lingkaran kosong di 2, karena 2 tidak termasuk penyelesaian."
            ),
            "en": (
                "2x + 3 > 7: solve like an equation, but keep the > sign.\n"
                "2x > 4 — subtract 3 from both sides (sign unchanged).\n"
                "x > 2 — divide both sides by 2, sign stays because 2 is positive.\n"
                "\u22123x + 5 \u2264 11: note the coefficient of x is negative.\n"
                "\u22123x \u2264 6 — subtract 5 from both sides.\n"
                "x \u2265 \u22122 — divide by \u22123, the \u2264 sign reverses to \u2265.\n"
                "Number line: x > 2 is drawn with an open circle at 2 since 2 is not included."
            ),
        },
        examples={
            "id": [
                "Selesaikan 2x + 3 > 7",
                "  2x > 4",
                "  x > 2",
                "",
                "Selesaikan \u22123x + 5 \u2264 11",
                "  \u22123x \u2264 6",
                "  x \u2265 \u22122 (tanda dibalik)",
                "",
                "Garis bilangan: x > 2 digambar dengan lingkaran terbuka di 2",
            ],
            "en": [
                "Solve 2x + 3 > 7",
                "  2x > 4",
                "  x > 2",
                "",
                "Solve \u22123x + 5 \u2264 11",
                "  \u22123x \u2264 6",
                "  x \u2265 \u22122 (sign reversed)",
                "",
                "Number line: x > 2 is drawn with an open circle at 2",
            ],
        },
        playground="inequalities",
    ),
    SubTopic(
        title={"id": "Eksponen dan Logaritma", "en": "Exponents and Logarithms"},
        description={
            "id": (
                "Eksponen menunjukkan pangkat suatu bilangan. Logaritma adalah kebalikan "
                "dari eksponen."
            ),
            "en": (
                "Exponents represent the power of a number. Logarithms are the inverse "
                "of exponents."
            ),
        },
        explanation={
            "id": (
                "2\u00b3 = 2×2×2 = 8, 5\u00b2 = 5×5 = 25 — eksponen menghitung berapa kali bilangan dikalikan dengan dirinya sendiri.\n"
                "2\u207b\u00b3 = 1/2\u00b3 = 1/8 — eksponen negatif adalah kebalikan dari eksponen positif.\n"
                "7\u2070 = 1 — berapa pun bilangannya, jika dipangkatkan 0 hasilnya selalu 1.\n"
                "log\u2082(8) = 3 karena 2\u00b3 = 8 — logaritma menjawab '2 dipangkatkan berapa supaya hasilnya 8?'.\n"
                "ln(e) = 1 — logaritma natural (ln) menggunakan basis e (bilangan Euler ≈ 2,718).\n"
                "log\u2082(32) = log\u2082(4×8) = log\u2082(4) + log\u2082(8) = 2 + 3 = 5 — logaritma perkalian sama dengan jumlah logaritma."
            ),
            "en": (
                "2\u00b3 = 2×2×2 = 8, 5\u00b2 = 5×5 = 25 — exponents count how many times a number multiplies itself.\n"
                "2\u207b\u00b3 = 1/2\u00b3 = 1/8 — a negative exponent gives the reciprocal of the positive power.\n"
                "7\u2070 = 1 — any non-zero number raised to the power of 0 always equals 1.\n"
                "log\u2082(8) = 3 because 2\u00b3 = 8 — logarithms answer 'to what power must 2 be raised to get 8?'.\n"
                "ln(e) = 1 — natural log (ln) uses base e (Euler's number ≈ 2.718).\n"
                "log\u2082(32) = log\u2082(4×8) = log\u2082(4) + log\u2082(8) = 2 + 3 = 5 — log of a product equals the sum of logs."
            ),
        },
        examples={
            "id": [
                "Eksponen: 2\u00b3 = 8, 5\u00b2 = 25",
                "Eksponen negatif: 2\u207b\u00b3 = 1/8",
                "Eksponen nol: 7\u2070 = 1",
                "",
                "Logaritma: log\u2082(8) = 3 (karena 2\u00b3 = 8)",
                "Logaritma natural: ln(e) = 1",
                "Sifat: log\u2082(32) = log\u2082(4 \u00d7 8) = log\u2082(4) + log\u2082(8) = 2 + 3 = 5",
            ],
            "en": [
                "Exponents: 2\u00b3 = 8, 5\u00b2 = 25",
                "Negative exponents: 2\u207b\u00b3 = 1/8",
                "Zero exponent: 7\u2070 = 1",
                "",
                "Logarithm: log\u2082(8) = 3 (since 2\u00b3 = 8)",
                "Natural log: ln(e) = 1",
                "Property: log\u2082(32) = log\u2082(4 \u00d7 8) = log\u2082(4) + log\u2082(8) = 2 + 3 = 5",
            ],
        },
        playground="exponents_logs",
    ),
]

_reg("algebra", _algebra_subtopics)
_reg("aljabar", _algebra_subtopics)
