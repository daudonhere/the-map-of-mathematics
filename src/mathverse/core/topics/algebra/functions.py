from __future__ import annotations

import random

from mathverse.core.models import SubTopic

algebra_functions_subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Fungsi", "en": "Functions"},
        description={
            "id": (
                "Fungsi adalah hubungan antara input dan output di mana setiap input "
                "memiliki tepat satu output."
            ),
            "en": (
                "A function is a relationship between input and output where each input "
                "has exactly one output."
            ),
        },
        explanation={
            "id": (
                "f(x) = 2x + 1: untuk setiap nilai x, kalikan dengan 2 lalu tambah 1.\n"
                "Jika x = 3, maka f(3) = 2\u00b73 + 1 = 7.\n"
                "Jika x = \u22122, maka f(\u22122) = 2\u00b7(\u22122) + 1 = \u22123.\n"
                "f(x) = x\u00b2: fungsi kuadrat, setiap x dipetakan ke kuadratnya.\n"
                "f(4) = 4\u00b2 = 16, dan f(\u22124) = (\u22124)\u00b2 = 16.\n"
                "f(x) = |x|: fungsi nilai mutlak, selalu menghasilkan nilai non-negatif.\n"
                "f(\u22125) = |\u22125| = 5, dan f(3) = |3| = 3."
            ),
            "en": (
                "f(x) = 2x + 1: for every x, multiply by 2 and add 1.\n"
                "If x = 3, then f(3) = 2\u00b73 + 1 = 7.\n"
                "If x = \u22122, then f(\u22122) = 2\u00b7(\u22122) + 1 = \u22123.\n"
                "f(x) = x\u00b2: a quadratic function, each x maps to its square.\n"
                "f(4) = 4\u00b2 = 16, and f(\u22124) = (\u22124)\u00b2 = 16.\n"
                "f(x) = |x|: absolute value function, always non-negative.\n"
                "f(\u22125) = |\u22125| = 5, and f(3) = |3| = 3."
            ),
        },
        examples={
            "id": [
                "f(x) = 2x + 1",
                "",
                "Jika x = 3, f(3) = 2(3) + 1 = 7",
                "Jika x = \u22122, f(\u22122) = 2(\u22122) + 1 = \u22123",
                "",
                "f(x) = x\u00b2",
                "f(4) = 16, f(\u22124) = 16",
                "",
                "f(x) = |x|",
                "f(\u22125) = 5, f(3) = 3",
            ],
            "en": [
                "f(x) = 2x + 1",
                "",
                "If x = 3, f(3) = 2(3) + 1 = 7",
                "If x = \u22122, f(\u22122) = 2(\u22122) + 1 = \u22123",
                "",
                "f(x) = x\u00b2",
                "f(4) = 16, f(\u22124) = 16",
                "",
                "f(x) = |x|",
                "f(\u22125) = 5, f(3) = 3",
            ],
        },
        playground="functions",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "functions":
        m = random.randint(-3, 3)
        if m == 0:
            m = 1
        b_val = random.randint(-5, 5)
        x = random.randint(-5, 5)
        result = m * x + b_val
        if b_val >= 0:
            q = _(
                "f(x) = {}x + {}, find f({})",
                "f(x) = {}x + {}, tentukan f({})",
            ).format(m, b_val, x)
        else:
            q = _(
                "f(x) = {}x \u2212 {}, find f({})",
                "f(x) = {}x \u2212 {}, tentukan f({})",
            ).format(m, abs(b_val), x)
        return q, str(result), result

    return None
