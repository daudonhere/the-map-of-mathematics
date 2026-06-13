from __future__ import annotations

import random

from mathverse.core.models import SubTopic

algebra_quadratic_subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Persamaan Kuadrat", "en": "Quadratic Equations"},
        description={
            "id": (
                "Persamaan kuadrat adalah persamaan berpangkat dua dengan bentuk umum "
                "ax\u00b2 + bx + c = 0, dengan a \u2260 0."
            ),
            "en": (
                "A quadratic equation is a second-degree equation with the general form "
                "ax\u00b2 + bx + c = 0, where a \u2260 0."
            ),
        },
        explanation={
            "id": (
                "x\u00b2 \u2212 5x + 6 = 0: cari dua bilangan yang hasil kalinya 6 dan jumlahnya 5.\n"
                "Faktor dari 6 yang berjumlah 5 adalah 2 dan 3: (x \u2212 2)(x \u2212 3) = 0.\n"
                "Dari faktor pertama: x \u2212 2 = 0 \u2192 x = 2.\n"
                "Dari faktor kedua: x \u2212 3 = 0 \u2192 x = 3.\n"
                "Gunakan rumus kuadrat: x = [\u2212(\u22125) \u00b1 \u221a((\u22125)\u00b2 \u2212 4\u00b71\u00b76)] / (2\u00b71).\n"
                "Hitung diskriminan: D = 25 \u2212 24 = 1, \u221a1 = 1.\n"
                "x = (5 \u00b1 1) / 2 = 3 dan 2, hasilnya sama dengan metode pemfaktoran."
            ),
            "en": (
                "x\u00b2 \u2212 5x + 6 = 0: find two numbers whose product is 6 and sum is 5.\n"
                "The factors of 6 that sum to 5 are 2 and 3: (x \u2212 2)(x \u2212 3) = 0.\n"
                "From the first factor: x \u2212 2 = 0 \u2192 x = 2.\n"
                "From the second factor: x \u2212 3 = 0 \u2192 x = 3.\n"
                "Use the quadratic formula: x = [\u2212(\u22125) \u00b1 \u221a((\u22125)\u00b2 \u2212 4\u00b71\u00b76)] / (2\u00b71).\n"
                "Calculate discriminant: D = 25 \u2212 24 = 1, \u221a1 = 1.\n"
                "x = (5 \u00b1 1) / 2 = 3 and 2, same result as factoring."
            ),
        },
        examples={
            "id": [
                "x\u00b2 \u2212 5x + 6 = 0",
                "",
                "Pemfaktoran: (x \u2212 2)(x \u2212 3) = 0",
                "  x \u2212 2 = 0 \u2192 x = 2",
                "  x \u2212 3 = 0 \u2192 x = 3",
                "",
                "Rumus kuadrat: x = (5 \u00b1 \u221a1) / 2",
                "  x\u2081 = (5 + 1)/2 = 3",
                "  x\u2082 = (5 \u2212 1)/2 = 2",
            ],
            "en": [
                "x\u00b2 \u2212 5x + 6 = 0",
                "",
                "Factoring: (x \u2212 2)(x \u2212 3) = 0",
                "  x \u2212 2 = 0 \u2192 x = 2",
                "  x \u2212 3 = 0 \u2192 x = 3",
                "",
                "Quadratic formula: x = (5 \u00b1 \u221a1) / 2",
                "  x\u2081 = (5 + 1)/2 = 3",
                "  x\u2082 = (5 \u2212 1)/2 = 2",
            ],
        },
        playground="quadratic",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "quadratic":
        x1 = random.randint(-5, 5)
        x2 = random.randint(-5, 5)
        a = random.randint(1, 3)
        b = -a * (x1 + x2)
        c = a * x1 * x2
        if b >= 0:
            q = _(
                "Solve: {}x\u00b2 + {}x + {} = 0",
                "Selesaikan: {}x\u00b2 + {}x + {} = 0",
            ).format(a, b, c)
        else:
            q = _(
                "Solve: {}x\u00b2 \u2212 {}x + {} = 0",
                "Selesaikan: {}x\u00b2 \u2212 {}x + {} = 0",
            ).format(a, abs(b), c)
        if random.randint(0, 1):
            return q, str(x1), x1
        else:
            return q, str(x2), x2

    elif playground == "quadratics":
        roots = [(2, 3), (3, 5), (2, 5), (1, 4), (3, 2), (4, 3), (2, 7), (3, 7)]
        r1, r2 = random.choice(roots)
        ans = r1 if random.randint(0, 1) else r2
        q = _(
            "Solve (x - {})(x - {}) = 0. Give one root.",
            "Selesaikan (x - {})(x - {}) = 0. Berikan satu akar.",
        ).format(r1, r2)
        return q, str(ans), ans

    return None
