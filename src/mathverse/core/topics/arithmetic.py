# ruff: noqa: RUF001
from __future__ import annotations

import math
import random

from mathverse.core.models import SubTopic

subtopics: list[SubTopic] = [
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


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "basic_ops":
        ops = [
            ("+", lambda a, b: a + b),
            ("\u2212", lambda a, b: a - b),
            ("\u00d7", lambda a, b: a * b),
        ]
        op_sym, op_fn = random.choice(ops)
        if op_sym == "\u00d7":
            a = random.randint(2, 12)
            b = random.randint(2, 12)
        else:
            a = random.randint(10, 99)
            b = random.randint(1, 50)
        if op_sym == "\u2212" and a < b:
            a, b = b, a
        ans = op_fn(a, b)
        q = f"{a} {op_sym} {b} = ?"
        return q, str(ans), ans

    elif playground == "powers":
        kind = random.choice(["square", "cube", "sqrt", "cbrt"])
        if kind == "square":
            n = random.randint(2, 15)
            ans = n * n
            return f"{n}\u00b2 = ?", str(ans), ans
        elif kind == "cube":
            n = random.randint(2, 6)
            ans = n * n * n
            return f"{n}\u00b3 = ?", str(ans), ans
        elif kind == "sqrt":
            n = random.randint(2, 12)
            ans = n * n
            return f"\u221a{ans} = ?", str(n), n
        else:
            n = random.randint(2, 4)
            ans = n * n * n
            return f"\u221b{ans} = ?", str(n), n

    elif playground == "mental_math":
        kind = random.choice(["comp", "double", "eleven", "near100"])
        if kind == "comp":
            a = random.randint(95, 99)
            b = random.randint(10, 50)
            ans = a + b
            return f"{a} + {b} = ?", str(ans), ans
        elif kind == "double":
            a = random.choice([25, 35, 45, 55, 65])
            b = random.choice([12, 14, 16, 18])
            ans = a * b
            return f"{a} \u00d7 {b} = ?", str(ans), ans
        elif kind == "eleven":
            a = random.randint(11, 99)
            ans = a * 11
            return f"{a} \u00d7 11 = ?", str(ans), ans
        else:
            a = random.randint(90, 99)
            b = random.randint(90, 99)
            ans = a * b
            return f"{a} \u00d7 {b} = ?", str(ans), ans

    elif playground == "properties":
        props = [
            ("commutative", lambda a, b: a + b == b + a),
            ("commutative", lambda a, b: a * b == b * a),
            ("associative", lambda a, b, c: (a + b) + c == a + (b + c)),
            ("associative", lambda a, b, c: (a * b) * c == a * (b * c)),
            ("distributive", lambda a, b, c: a * (b + c) == a * b + a * c),
        ]
        ans_map = {
            "commutative": _("commutative", "komutatif"),
            "associative": _("associative", "asosiatif"),
            "distributive": _("distributive", "distributif"),
        }
        choice = random.choice(props)
        prop_en = choice[0]
        prop_id = ans_map[prop_en]
        label = _("Property shown:", "Sifat ditunjukkan:")
        if prop_en in ("commutative",):
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            q = f"{label} {a} + {b} = {b} + {a}"
            return q, prop_id if locale == "id" else prop_en, 0.0
        elif prop_en == "associative":
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            c = random.randint(2, 8)
            q = f"{label} ({a} + {b}) + {c} = {a} + ({b} + {c})"
            return q, prop_id if locale == "id" else prop_en, 0.0
        elif prop_en == "distributive":
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)
            q = f"{label} {a} \u00d7 ({b} + {c}) = {a}\u00d7{b} + {a}\u00d7{c}"
            return q, prop_id if locale == "id" else prop_en, 0.0

    elif playground == "number_types":
        kind = random.choice(["prime", "square", "even", "odd"])
        if kind == "prime":
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
            compos = [4, 6, 8, 9, 10, 12, 14, 15, 16]
            n = random.choice(primes)
            distract = random.choice(compos)
            q_fmt = _(
                "Is {} prime or composite?", "Apakah {} bilangan prima atau komposit?"
            )
            if random.randint(0, 1):
                ans = _("prime", "prima")
                q = q_fmt.format(n)
                return q, ans, 0.0
            else:
                ans = _("composite", "komposit")
                q = q_fmt.format(distract)
                return q, ans, 0.0
        elif kind == "square":
            sq = random.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
            q_fmt = _(
                "Which number squared equals {}?",
                "Bilangan berapa yang dikuadratkan hasilnya {}?",
            )
            q = q_fmt.format(sq)
            ans = int(sq**0.5)
            return q, str(ans), ans
        elif kind == "even":
            n = random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
            q_fmt = _("Is {} even or odd?", "Apakah {} genap atau ganjil?")
            q = q_fmt.format(n)
            return q, _("even", "genap"), 0.0
        elif kind == "odd":
            n = random.choice([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
            q_fmt = _("Is {} even or odd?", "Apakah {} genap atau ganjil?")
            q = q_fmt.format(n)
            return q, _("odd", "ganjil"), 0.0

    elif playground == "factors":
        pairs = [
            (4, 6),
            (6, 8),
            (3, 4),
            (5, 6),
            (4, 5),
            (6, 10),
            (5, 7),
            (8, 10),
            (8, 12),
            (12, 18),
            (15, 25),
            (6, 9),
            (10, 15),
            (14, 21),
            (16, 24),
            (9, 15),
        ]
        kind = random.choice(["gcf", "lcm"])
        a, b = random.choice(pairs)
        ans = math.gcd(a, b)
        if kind == "gcf":
            q = _("GCF of {} and {} = ?", "FPB dari {} dan {} = ?").format(a, b)
            return q, str(ans), ans
        else:
            ans = a * b // ans
            q = _("LCM of {} and {} = ?", "KPK dari {} dan {} = ?").format(a, b)
            return q, str(ans), ans

    elif playground == "ratios":
        kind = random.choice(["simplify", "find_part"])
        if kind == "simplify":
            pairs = [(6, 8), (10, 15), (12, 18), (8, 12), (14, 21), (9, 12)]
            a, b = random.choice(pairs)
            g = math.gcd(a, b)
            q = _("Simplify ratio {}:{} = ?", "Sederhanakan rasio {}:{} = ?").format(
                a, b
            )
            ans = f"1:{b // g}" if g == a else f"{a // g}:{b // g}"
            return q, ans, 0.0
        else:
            a, b = random.choice([(2, 3), (3, 5), (4, 7), (5, 8), (1, 4), (3, 7)])
            total = random.choice([30, 40, 50, 60, 70, 80])
            if (a + b) > total:
                total = (a + b) * random.randint(2, 5)
            part_b = total // (a + b) * b
            q = _(
                "Ratio {}:{}, total {}. Value of larger part = ?",
                "Rasio {}:{}, total {}. Nilai bagian terbesar = ?",
            ).format(a, b, total)
            return q, str(part_b), part_b

    elif playground == "percentages":
        kind = random.choice(["of", "of_rev", "change"])
        if kind == "of":
            pct = random.choice([10, 20, 25, 30, 40, 50, 60, 75])
            num = random.choice([40, 60, 80, 100, 120, 200, 300])
            ans = num * pct // 100
            q = _("What is {}% of {}?", "Berapa {}% dari {}?").format(pct, num)
            return q, str(ans), ans
        elif kind == "of_rev":
            ans = random.choice([10, 20, 25, 30, 40, 50])
            num = random.choice([40, 60, 80, 100, 120, 200])
            pct = num * ans // 100
            q = _("{} is what percent of {}?", "{} berapa persen dari {}?").format(
                ans, num
            )
            return q, str(pct), pct
        else:
            old = random.choice([40, 50, 60, 80, 100, 120])
            new = old + random.choice([10, 15, 20, 25, 30])
            change = (new - old) * 100 // old
            q = _(
                "Change from {} to {} = ?% increase",
                "Perubahan dari {} ke {} = ?% kenaikan",
            ).format(old, new)
            return q, str(change), change

    elif playground == "number_theory":
        kind = random.choice(["mod", "digits", "factorial"])
        if kind == "mod":
            a = random.randint(10, 30)
            b = random.choice([3, 4, 5, 6, 7, 8, 9])
            ans = a % b
            q = f"{a} mod {b} = ?"
            return q, str(ans), ans
        elif kind == "digits":
            n = random.randint(100, 999)
            s = sum(int(d) for d in str(n))
            q = _("Sum of digits of {} = ?", "Jumlah digit dari {} = ?").format(n)
            return q, str(s), s
        else:
            n = random.choice([4, 5, 6, 7])
            ans = math.factorial(n)
            q = f"{n}! = ?"
            return q, str(ans), ans

    return None
