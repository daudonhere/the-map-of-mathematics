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
                "Eksponen: x\u00b2 = x \u00d7 x, dibaca x kuadrat.\n"
                "Eksponen: x\u00b3 = x \u00d7 x \u00d7 x, dibaca x pangkat tiga.\n"
                "Bilangan apa pun pangkat 0 sama dengan 1: x\u2070 = 1.\n"
                "Eksponen negatif berarti kebalikan: 2\u207b\u00b9 = \u00bd.\n"
                "Logaritma: log\u2082(8) = 3 karena 2\u00b3 = 8.\n"
                "Logaritma: log\u2081\u2080(1000) = 3 karena 10\u00b3 = 1000.\n"
                "Logaritma: log\u2083(9) = 2 karena 3\u00b2 = 9.\n"
                "Secara umum: log\u2090(b) = c \u2194 a\u1d9c = b."
            ),
            "en": (
                "Exponent: x\u00b2 = x \u00d7 x, read as x squared.\n"
                "Exponent: x\u00b3 = x \u00d7 x \u00d7 x, read as x cubed.\n"
                "Any number to the power of 0 equals 1: x\u2070 = 1.\n"
                "Negative exponent means reciprocal: 2\u207b\u00b9 = \u00bd.\n"
                "Logarithm: log\u2082(8) = 3 because 2\u00b3 = 8.\n"
                "Logarithm: log\u2081\u2080(1000) = 3 because 10\u00b3 = 1000.\n"
                "Logarithm: log\u2083(9) = 2 because 3\u00b2 = 9.\n"
                "In general: log\u2090(b) = c \u2194 a\u1d9c = b."
            ),
        },
        examples={
            "id": [
                "Eksponen:",
                "  x\u00b2 = x \u00d7 x",
                "  x\u00b3 = x \u00d7 x \u00d7 x",
                "  2\u00b3 = 8",
                "  5\u00b2 = 25",
                "  10\u2070 = 1",
                "  2\u207b\u00b9 = \u00bd",
                "",
                "Logaritma:",
                "  log\u2082(8) = 3 \u2194 2\u00b3 = 8",
                "  log\u2081\u2080(1000) = 3 \u2194 10\u00b3 = 1000",
                "  log\u2083(9) = 2 \u2194 3\u00b2 = 9",
                "  log\u2085(25) = 2 \u2194 5\u00b2 = 25",
            ],
            "en": [
                "Exponents:",
                "  x\u00b2 = x \u00d7 x",
                "  x\u00b3 = x \u00d7 x \u00d7 x",
                "  2\u00b3 = 8",
                "  5\u00b2 = 25",
                "  10\u2070 = 1",
                "  2\u207b\u00b9 = \u00bd",
                "",
                "Logarithms:",
                "  log\u2082(8) = 3 \u2194 2\u00b3 = 8",
                "  log\u2081\u2080(1000) = 3 \u2194 10\u00b3 = 1000",
                "  log\u2083(9) = 2 \u2194 3\u00b2 = 9",
                "  log\u2085(25) = 2 \u2194 5\u00b2 = 25",
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
