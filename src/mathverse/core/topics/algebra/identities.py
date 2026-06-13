# ruff: noqa: RUF001
from __future__ import annotations

import random

from mathverse.core.models import SubTopic

algebra_identity_subtopics: list[SubTopic] = [
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


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "perfect_square":
        a = random.randint(2, 9)
        b = random.randint(1, 5)
        a2, b2, ab2 = a * a, b * b, 2 * a * b
        total_val = a2 + ab2 + b2
        q = _("({}+{})² = ?", "({}+{})² = ?").format(a, b)
        return q, str(total_val), total_val

    elif playground == "diff_squares":
        a = random.randint(3, 9)
        b = random.randint(1, a - 1)
        a2, b2 = a * a, b * b
        total_val = a2 - b2
        q = _("{}² − {}² = ?", "{}² − {}² = ?").format(a, b)
        return q, str(total_val), total_val

    return None
