# ruff: noqa: RUF001
from __future__ import annotations

import random

from mathverse.core.models import SubTopic

algebra_core_subtopics: list[SubTopic] = [
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
                "  3 dan 5 = konstanta",
            ],
            "en": [
                "Variables: x, y, z",
                "Constants: 5, 10, −3",
                "",
                "Expression: 3x + 5",
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
                "Perkalian: (x + 2)(x + 3) = x² + 5x + 6",
                "",
                "Pembagian: (6x²)/(2x) = 3x",
            ],
            "en": [
                "Addition: 3x + 2x = 5x",
                "Subtraction: 7y − 3y = 4y",
                "",
                "Multiplication: (x + 2)(x + 3) = x² + 5x + 6",
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
                "Faktor persekutuan: 6x² + 9x = 3x(2x + 3) — keluarkan faktor yang sama dari setiap suku.\n"
                "Setelah difaktorkan, kita dapatkan perkalian dua faktor yang lebih sederhana."
            ),
            "en": (
                "Factoring is the reverse of multiplication — breaking an expression into its factors.\n"
                "x² + 5x + 6 = (x + 2)(x + 3) — find two numbers whose product is 6 and sum is 5.\n"
                "Common factor: 6x² + 9x = 3x(2x + 3) — factor out the common term from each term.\n"
                "After factoring, we obtain a product of two simpler expressions."
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
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "variables":
        kind = random.choice(
            ["identify_var", "identify_const", "identify_coeff", "count_terms"]
        )
        if kind == "identify_var":
            pairs = [
                ("3x + 5", "x"),
                ("2a \u2212 7", "a"),
                ("y\u00b2 + 4y", "y"),
                ("6p \u2212 3q + 2", "p, q"),
                ("m\u00b3 + 2m", "m"),
            ]
            expr, ans = random.choice(pairs)
            q = _("Variable(s) in '{}'?", "Variabel dalam '{}'?").format(expr)
            return q, ans, 0.0
        elif kind == "identify_const":
            pairs = [
                ("3x + 5", "5"),
                ("2a \u2212 7", "\u22127"),
                ("x + 10", "10"),
                ("4y \u2212 1", "\u22121"),
                ("8p + 3q \u2212 2", "\u22122"),
            ]
            expr, ans = random.choice(pairs)
            q = _("Constant in '{}'?", "Konstanta dalam '{}'?").format(expr)
            return q, ans, 0.0
        elif kind == "identify_coeff":
            pairs = [
                ("3x + 5", "3"),
                ("\u22122x + 7", "\u22122"),
                ("x\u00b2 + 4x", "1"),
                ("\u2212y + 3", "\u22121"),
                ("6a\u00b2 \u2212 a", "6"),
            ]
            expr, ans = random.choice(pairs)
            q = _(
                "Coefficient of variable in '{}'?", "Koefisien variabel dalam '{}'?"
            ).format(expr)
            return q, ans, 0.0
        else:
            pairs = [
                ("3x + 5", "2"),
                ("2a \u2212 7b + 1", "3"),
                ("x", "1"),
                ("4y \u2212 1", "2"),
                ("8p + 3q \u2212 2r + 5", "4"),
            ]
            expr, ans = random.choice(pairs)
            q = _("How many terms in '{}'?", "Berapa suku dalam '{}'?").format(expr)
            return q, ans, 0.0

    elif playground == "algebraic_forms":
        form_id = {
            "monomial": _("monomial", "monomial"),
            "binomial": _("binomial", "binomial"),
            "trinomial": _("trinomial", "trinomial"),
            "polynomial": _("polynomial", "polinomial"),
        }
        pairs = [
            ("5x", "monomial"),
            ("7a\u00b2", "monomial"),
            ("x + 3", "binomial"),
            ("2a \u2212 b", "binomial"),
            ("x\u00b2 + 2x + 1", "trinomial"),
            ("a\u00b2 \u2212 3a + 2", "trinomial"),
            ("x\u2074 + 2x\u00b3 \u2212 x + 7", "polynomial"),
            ("3a\u00b3 \u2212 2a\u00b2 + a \u2212 5", "polynomial"),
            ("8", "monomial"),
            ("2x \u2212 1", "binomial"),
        ]
        expr, ans_en = random.choice(pairs)
        q = _(
            "Classify: '{}' (monomial/binomial/trinomial/polynomial)?",
            "Klasifikasikan: '{}' (monomial/binomial/trinomial/polinomial)?",
        ).format(expr)
        return q, form_id[ans_en], 0.0

    elif playground == "algebraic_ops":
        kind = random.choice(["add_like", "sub_like", "distribute", "divide"])
        if kind == "add_like":
            pairs = [
                (3, 2, 5),
                (4, 1, 5),
                (7, 3, 10),
                (2, 6, 8),
                (5, 5, 10),
            ]
            a, b, ans = random.choice(pairs)
            q = _("Simplify: {}x + {}x = ?", "Sederhanakan: {}x + {}x = ?").format(a, b)
            return q, str(ans) + "x", ans
        elif kind == "sub_like":
            pairs = [
                (7, 3, 4),
                (9, 2, 7),
                (8, 5, 3),
                (6, 6, 0),
                (10, 4, 6),
            ]
            a, b, ans = random.choice(pairs)
            q = _(
                "Simplify: {}y \u2212 {}y = ?", "Sederhanakan: {}y \u2212 {}y = ?"
            ).format(a, b)
            return q, str(ans) + "y" if ans != 0 else "0", ans
        elif kind == "distribute":
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            ans_a = a * b
            ans_b = a * c
            q = _("Expand: {}({}x + {}) = ?", "Jabarkan: {}({}x + {}) = ?").format(
                a, b, c
            )
            return q, f"{ans_a}x + {ans_b}", 0.0
        else:
            pairs = [
                (6, 2, 3),
                (12, 3, 4),
                (15, 5, 3),
                (8, 4, 2),
                (10, 2, 5),
            ]
            a, b, ans = random.choice(pairs)
            q = _(
                "Simplify: ({}x\u00b2)/({}x) = ?", "Sederhanakan: ({}x\u00b2)/({}x) = ?"
            ).format(a, b)
            return q, str(ans) + "x", ans

    elif playground == "factoring":
        pairs = [(2, 3), (3, 5), (2, 5), (3, 4), (2, 7), (3, 2), (4, 3), (5, 2)]
        a, b = random.choice(pairs)
        c = a * b
        d = a + b
        q = _(
            "One factor of x\u00b2 + {}x + {} is (x + {}). What is the other?",
            "Satu faktor dari x\u00b2 + {}x + {} adalah (x + {}). Berapa faktor lainnya?",
        ).format(d, c, a)
        return q, str(b), b

    elif playground == "expressions":
        a = random.randint(2, 8)
        b = random.randint(1, 10)
        x = random.randint(1, 6)
        kind = random.choice(["linear", "quad"])
        if kind == "linear":
            ans = a * x + b
            q = _(
                "If x = {}, evaluate {}x + {}", "Jika x = {}, hitung {}x + {}"
            ).format(x, a, b)
            return q, str(ans), ans
        else:
            c = random.randint(1, 5)
            ans = a * x * x + b * x + c
            q = _(
                "If x = {}, evaluate {}x\u00b2 + {}x + {}",
                "Jika x = {}, hitung {}x\u00b2 + {}x + {}",
            ).format(x, a, b, c)
            return q, str(ans), ans

    elif playground == "equations":
        a = random.randint(2, 6)
        b = random.choice([3, 5, 7, 9, 11, 13])
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q = _("Solve: {}x + {} = {}", "Selesaikan: {}x + {} = {}").format(a, b, c)
        return q, str(ans), ans

    elif playground == "systems":
        pairs = [
            ((2, 3), (1, -1)),
            ((3, 5), (2, -3)),
            ((2, -1), (1, 2)),
            ((3, 2), (1, -1)),
            ((4, 1), (1, -2)),
        ]
        (a, b), (d, e) = random.choice(pairs)
        x = random.randint(2, 5)
        y = random.randint(1, 4)
        c1 = a * x + b * y
        c2 = d * x + e * y
        q_label = _("Solve:", "Selesaikan:")
        q_val = _("Enter x value", "Masukkan nilai x")
        q = f"{q_label}\n{a}x + {b}y = {c1}\n{d}x + {e}y = {c2}\n{q_val}"
        return q, str(x), x

    elif playground == "polynomials":
        kind = random.choice(["eval", "add"])
        if kind == "eval":
            a = random.randint(1, 5)
            b = random.randint(1, 6)
            x = random.randint(1, 4)
            ans = a * x + b
            q = _(
                "If P(x) = {}x + {}, find P({})", "Jika P(x) = {}x + {}, cari P({})"
            ).format(a, b, x)
            return q, str(ans), ans
        else:
            a, b = random.randint(1, 4), random.randint(1, 4)
            c, d = random.randint(1, 4), random.randint(1, 4)
            x = random.randint(1, 3)
            ans = (a + c) * x + (b + d)
            q = _(
                "({}x + {}) + ({}x + {}) at x={} = ?",
                "({}x + {}) + ({}x + {}) saat x={} = ?",
            ).format(a, b, c, d, x)
            return q, str(ans), ans

    elif playground == "inequalities":
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q_label = _("Solve:", "Selesaikan:")
        q_hint = _(
            "Enter smallest integer solution.",
            "Masukkan solusi bilangan bulat terkecil.",
        )
        q = f"{q_label} {a}x + {b} > {c}. {q_hint}"
        return q, str(ans + 1), ans + 1

    return None
