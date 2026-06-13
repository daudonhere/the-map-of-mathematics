from __future__ import annotations

import math
import random

from mathverse.core.models import SubTopic

algebra_exponents_subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Eksponen dan Logaritma", "en": "Exponents and Logarithms"},
        description={
            "id": (
                "Eksponen menunjukkan berapa kali suatu bilangan dikalikan dengan "
                "dirinya sendiri. Logaritma adalah kebalikan (invers) dari eksponen."
            ),
            "en": (
                "Exponents indicate how many times a number is multiplied by itself. "
                "Logarithms are the inverse of exponents."
            ),
        },
        explanation={
            "id": (
                "Berikut contoh-contoh eksponen.\n"
                "2\u00b3 = 2 \u00d7 2 \u00d7 2 = 8 — contoh perhitungan eksponen.\n"
                "Berikut contoh-contoh logaritma.\n"
                "log\u2082(8) = 3 karena 2\u00b3 = 8 — logaritma adalah kebalikan eksponen."
            ),
            "en": (
                "Here are examples of exponents.\n"
                "2\u00b3 = 2 \u00d7 2 \u00d7 2 = 8 — a worked exponent calculation.\n"
                "Here are examples of logarithms.\n"
                "log\u2082(8) = 3 because 2\u00b3 = 8 — a logarithm is the inverse of an exponent."
            ),
        },
        examples={
            "id": [
                "Eksponen:",
                "  2\u00b3 = 8",
                "",
                "Logaritma:",
                "  log\u2082(8) = 3 \u2194 2\u00b3 = 8",
            ],
            "en": [
                "Exponents:",
                "  2\u00b3 = 8",
                "",
                "Logarithms:",
                "  log\u2082(8) = 3 \u2194 2\u00b3 = 8",
            ],
        },
        playground="exponents_logs",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    sup_digits = {
        "0": "\u2070",
        "1": "\u00b9",
        "2": "\u00b2",
        "3": "\u00b3",
        "4": "\u2074",
    }

    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "exponents_logs":
        kind = random.randint(0, 1)
        if kind == 0:
            base = random.randint(2, 5)
            exp = random.randint(2, 4)
            result = base**exp
            exp_sup = "".join(sup_digits[d] for d in str(exp))
            q = _(
                "Evaluate: {}{} = ?",
                "Hitung: {}{} = ?",
            ).format(base, exp_sup)
            return q, str(result), result
        else:
            base = random.choice([2, 3, 5, 10])
            if base == 10:
                vals = [10, 100, 1000, 10000]
                val = random.choice(vals)
            elif base == 2:
                vals = [2, 4, 8, 16, 32, 64]
                val = random.choice(vals)
            elif base == 3:
                vals = [3, 9, 27, 81]
                val = random.choice(vals)
            else:
                vals = [5, 25, 125]
                val = random.choice(vals)
            result = round(math.log(val, base))
            if base == 10:
                q = _(
                    "Evaluate: log\u2081\u2080({}) = ?",
                    "Hitung: log\u2081\u2080({}) = ?",
                ).format(val)
            else:
                base_sub = str(base).translate(
                    str.maketrans(
                        "0123456789",
                        "\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089",
                    )
                )
                q = _(
                    "Evaluate: log{}({}) = ?",
                    "Hitung: log{}({}) = ?",
                ).format(base_sub, val)
            return q, str(result), result

    return None
