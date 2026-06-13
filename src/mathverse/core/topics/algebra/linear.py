# ruff: noqa: RUF001
from __future__ import annotations

import random

from mathverse.core.models import SubTopic

algebra_linear_subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Persamaan Linear", "en": "Linear Equations"},
        description={
            "id": (
                "Persamaan linear adalah persamaan yang variabelnya berpangkat satu. "
                "Bentuk umumnya ax + b = 0 dengan a ≠ 0."
            ),
            "en": (
                "A linear equation is an equation where the variable has an exponent of one. "
                "Its general form is ax + b = 0 where a ≠ 0."
            ),
        },
        explanation={
            "id": (
                "Kurangi kedua ruas dengan 4 untuk mengisolasi suku 2x.\n"
                "Bagi kedua ruas dengan 2 untuk mendapatkan nilai x.\n"
                "x = 3 adalah solusi dari persamaan 2x + 4 = 10.\n"
                "Tambahkan 7 ke kedua ruas untuk menghilangkan pengurangan.\n"
                "Bagi kedua ruas dengan 3 untuk mendapatkan nilai x.\n"
                "x = 5 adalah solusi dari persamaan 3x − 7 = 8."
            ),
            "en": (
                "Subtract 4 from both sides to isolate the 2x term.\n"
                "Divide both sides by 2 to find the value of x.\n"
                "x = 3 is the solution to the equation 2x + 4 = 10.\n"
                "Add 7 to both sides to eliminate the subtraction.\n"
                "Divide both sides by 3 to find the value of x.\n"
                "x = 5 is the solution to the equation 3x − 7 = 8."
            ),
        },
        examples={
            "id": [
                "2x + 4 = 10",
                "  Kurangi 4: 2x = 6",
                "  x = 3",
                "",
                "3x − 7 = 8",
                "  Tambah 7: 3x = 15",
                "  x = 5",
            ],
            "en": [
                "2x + 4 = 10",
                "  Subtract 4: 2x = 6",
                "  x = 3",
                "",
                "3x − 7 = 8",
                "  Add 7: 3x = 15",
                "  x = 5",
            ],
        },
        playground="linear_equations",
    ),
    SubTopic(
        title={
            "id": "Sistem Persamaan Linear",
            "en": "Systems of Linear Equations",
        },
        description={
            "id": (
                "Sistem persamaan linear terdiri dari dua atau lebih persamaan linear "
                "yang diselesaikan secara bersama-sama."
            ),
            "en": (
                "A system of linear equations consists of two or more linear equations "
                "solved simultaneously."
            ),
        },
        explanation={
            "id": (
                "Persamaan pertama: jumlah x dan y adalah 10.\n"
                "Persamaan kedua: selisih x dan y adalah 2.\n"
                "Jumlahkan kedua persamaan untuk mengeliminasi y: 2x = 12, x = 6.\n"
                "Substitusi x = 6 ke x + y = 10: y = 10 − 6 = 4."
            ),
            "en": (
                "First equation: the sum of x and y is 10.\n"
                "Second equation: the difference of x and y is 2.\n"
                "Add both equations to eliminate y: 2x = 12, x = 6.\n"
                "Substitute x = 6 into x + y = 10: y = 10 − 6 = 4."
            ),
        },
        examples={
            "id": [
                "x + y = 10",
                "x − y = 2",
                "",
                "Jumlahkan: 2x = 12, x = 6",
                "y = 10 − 6 = 4",
            ],
            "en": [
                "x + y = 10",
                "x − y = 2",
                "",
                "Add: 2x = 12, x = 6",
                "y = 10 − 6 = 4",
            ],
        },
        playground="systems_of_equations",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "linear_equations":
        a = random.randint(2, 9)
        b = random.randint(-10, 10)
        x = random.randint(-5, 10)
        c = a * x + b
        if b >= 0:
            q = _("Solve: {}x + {} = {}", "Selesaikan: {}x + {} = {}").format(a, b, c)
        else:
            q = _("Solve: {}x − {} = {}", "Selesaikan: {}x − {} = {}").format(
                a, abs(b), c
            )
        return q, str(x), x

    elif playground == "systems_of_equations":
        x = random.randint(-3, 8)
        y = random.randint(-3, 8)
        a = x + y
        b = x - y
        kind = random.choice(["x", "y"])
        if kind == "x":
            q = _(
                "x + y = {}, x − y = {}. What is x?",
                "x + y = {}, x − y = {}. Berapa x?",
            ).format(a, b)
            return q, str(x), x
        else:
            q = _(
                "x + y = {}, x − y = {}. What is y?",
                "x + y = {}, x − y = {}. Berapa y?",
            ).format(a, b)
            return q, str(y), y

    return None
