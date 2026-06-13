from __future__ import annotations

import random

from mathverse.core.models import SubTopic

subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "AND (Konjungsi)", "en": "AND (Conjunction)"},
        description={
            "id": (
                "Operasi AND menghasilkan 1 hanya jika kedua input bernilai 1. "
                "Dilambangkan dengan A\u00b7B, A\u2227B, atau A AND B."
            ),
            "en": (
                "The AND operation outputs 1 only when both inputs are 1. "
                "Notated as A\u00b7B, A\u2227B, or A AND B."
            ),
        },
        explanation={
            "id": (
                "0 AND 0 = 0 — jika kedua input salah, output salah.\n"
                "0 AND 1 = 0 — jika salah satu salah, output salah.\n"
                "1 AND 0 = 0 — jika salah satu salah, output salah.\n"
                "1 AND 1 = 1 — hanya jika kedua benar, output benar."
            ),
            "en": (
                "0 AND 0 = 0 — if both inputs are false, output is false.\n"
                "0 AND 1 = 0 — if either is false, output is false.\n"
                "1 AND 0 = 0 — if either is false, output is false.\n"
                "1 AND 1 = 1 — only when both are true, output is true."
            ),
        },
        examples={
            "id": [
                "0 AND 0 = 0",
                "0 AND 1 = 0",
                "1 AND 0 = 0",
                "1 AND 1 = 1",
            ],
            "en": [
                "0 AND 0 = 0",
                "0 AND 1 = 0",
                "1 AND 0 = 0",
                "1 AND 1 = 1",
            ],
        },
        playground="logic_gates",
    ),
    SubTopic(
        title={"id": "OR (Disjungsi)", "en": "OR (Disjunction)"},
        description={
            "id": (
                "Operasi OR menghasilkan 1 jika salah satu atau kedua input "
                "bernilai 1. Dilambangkan dengan A+B, A\u2228B, atau A OR B."
            ),
            "en": (
                "The OR operation outputs 1 if at least one input is 1. "
                "Notated as A+B, A\u2228B, or A OR B."
            ),
        },
        explanation={
            "id": (
                "0 OR 0 = 0 — jika kedua input salah, output salah.\n"
                "0 OR 1 = 1 — jika setidaknya satu benar, output benar.\n"
                "1 OR 0 = 1 — jika setidaknya satu benar, output benar.\n"
                "1 OR 1 = 1 — jika kedua benar, output benar."
            ),
            "en": (
                "0 OR 0 = 0 — if both inputs are false, output is false.\n"
                "0 OR 1 = 1 — if at least one is true, output is true.\n"
                "1 OR 0 = 1 — if at least one is true, output is true.\n"
                "1 OR 1 = 1 — if both are true, output is true."
            ),
        },
        examples={
            "id": [
                "0 OR 0 = 0",
                "0 OR 1 = 1",
                "1 OR 0 = 1",
                "1 OR 1 = 1",
            ],
            "en": [
                "0 OR 0 = 0",
                "0 OR 1 = 1",
                "1 OR 0 = 1",
                "1 OR 1 = 1",
            ],
        },
        playground="logic_gates",
    ),
    SubTopic(
        title={"id": "NOT (Negasi)", "en": "NOT (Negation)"},
        description={
            "id": (
                "Operasi NOT membalikkan nilai input: 0 menjadi 1, "
                "1 menjadi 0. Dilambangkan dengan \u00acA, \u00c4, atau A'."
            ),
            "en": (
                "The NOT operation flips the input value: 0 becomes 1, "
                "1 becomes 0. Notated as \u00acA, \u00c4, or A'."
            ),
        },
        explanation={
            "id": (
                "NOT 0 = 1 — negasi dari salah adalah benar.\n"
                "NOT 1 = 0 — negasi dari benar adalah salah.\n"
                "\u00ac(\u00acA) = A — negasi ganda: membalik dua kali kembali ke nilai asal.\n"
                "Hukum De Morgan: \u00ac(A AND B) = \u00acA OR \u00acB — negasi dari AND menjadi OR dari negasi."
            ),
            "en": (
                "NOT 0 = 1 — the negation of false is true.\n"
                "NOT 1 = 0 — the negation of true is false.\n"
                "\u00ac(\u00acA) = A — double negation: flipping twice returns to the original.\n"
                "De Morgan\u2019s laws: \u00ac(A AND B) = \u00acA OR \u00acB — the negation of an AND becomes an OR of negations."
            ),
        },
        examples={
            "id": [
                "NOT 0 = 1",
                "NOT 1 = 0",
                "",
                "\u00ac(\u00acA) = A (negasi ganda)",
                "\u00ac(A AND B) = \u00acA OR \u00acB",
            ],
            "en": [
                "NOT 0 = 1",
                "NOT 1 = 0",
                "",
                "\u00ac(\u00acA) = A (double negation)",
                "\u00ac(A AND B) = \u00acA OR \u00acB",
            ],
        },
        playground="logic_gates",
    ),
    SubTopic(
        title={
            "id": "Dasar Rangkaian Digital dan Komputer",
            "en": "Digital Circuit & Computer Basics",
        },
        description={
            "id": (
                "Gerbang logika AND, OR, NOT adalah blok pembangun "
                "semua rangkaian digital dan komputer modern."
            ),
            "en": (
                "AND, OR, NOT logic gates are the building blocks "
                "of all digital circuits and modern computers."
            ),
        },
        explanation={
            "id": (
                "NAND = NOT AND — gerbang universal: output 0 hanya jika kedua input 1.\n"
                "NAND(0,0)=1 dan NAND(0,1)=1 karena setidaknya satu input 0.\n"
                "NAND(1,0)=1, NAND(1,1)=0 — hanya saat keduanya 1 output menjadi 0.\n"
                "XOR = (A OR B) AND NOT(A AND B) — output 1 saat input berbeda."
            ),
            "en": (
                "NAND = NOT AND — universal gate: outputs 0 only when both inputs are 1.\n"
                "NAND(0,0)=1 and NAND(0,1)=1 because at least one input is 0.\n"
                "NAND(1,0)=1, NAND(1,1)=0 — only when both are 1 does output become 0.\n"
                "XOR = (A OR B) AND NOT(A AND B) — outputs 1 when inputs differ."
            ),
        },
        examples={
            "id": [
                "Gerbang NAND: NOT(A AND B)",
                "  NAND(0,0)=1, NAND(0,1)=1",
                "  NAND(1,0)=1, NAND(1,1)=0",
                "",
                "Gerbang XOR: A\u2295B = (A OR B) AND NOT(A AND B)",
            ],
            "en": [
                "NAND gate: NOT(A AND B)",
                "  NAND(0,0)=1, NAND(0,1)=1",
                "  NAND(1,0)=1, NAND(1,1)=0",
                "",
                "XOR gate: A\u2295B = (A OR B) AND NOT(A AND B)",
            ],
        },
        playground="logic_gates",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "logic_gates":
        kind = random.choice(["truth", "demorgan", "xor"])

        if kind == "truth":
            op = random.choice(["AND", "OR", "NAND", "NOR", "XOR"])
            a = random.randint(0, 1)
            b = random.randint(0, 1)
            if op == "AND":
                ans = a & b
            elif op == "OR":
                ans = a | b
            elif op == "NAND":
                ans = 0 if (a & b) else 1
            elif op == "NOR":
                ans = 0 if (a | b) else 1
            else:
                ans = a ^ b
            q = f"{a} {op} {b} = ?"
            return q, str(ans), ans

        elif kind == "demorgan":
            a = random.randint(0, 1)
            b = random.randint(0, 1)
            side = random.choice(["left", "right"])
            if side == "left":
                ans = 0 if (a & b) else 1
                q = f"\u00ac({a} AND {b}) = ?"
            else:
                ans = (0 if a else 1) | (0 if b else 1)
                q = f"\u00ac{a} OR \u00ac{b} = ?"
            return q, str(ans), ans

        else:
            a = random.randint(0, 1)
            b = random.randint(0, 1)
            q = _(
                f"{a} XOR {b} = ?",
                f"{a} XOR {b} = ?",
            )
            ans = a ^ b
            return q, str(ans), ans

    return None


__all__ = ["gen_question", "subtopics"]
