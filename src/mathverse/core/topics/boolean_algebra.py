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
                "Tabel kebenaran AND menunjukkan empat kemungkinan kombinasi input dan outputnya.\n"
                "0 AND 0 = 0 — jika kedua input salah, output salah.\n"
                "0 AND 1 = 0 — jika salah satu salah, output salah.\n"
                "1 AND 0 = 0 — jika salah satu salah, output salah.\n"
                "1 AND 1 = 1 — hanya jika kedua benar, output benar.\n"
                "Absorbsi: A AND 0 = 0; identitas: A AND 1 = A.\n"
                "Idempoten: A AND A = A; kontradiksi: A AND \u00acA = 0."
            ),
            "en": (
                "The AND truth table shows all four possible input combinations and their outputs.\n"
                "0 AND 0 = 0 — if both inputs are false, output is false.\n"
                "0 AND 1 = 0 — if either is false, output is false.\n"
                "1 AND 0 = 0 — if either is false, output is false.\n"
                "1 AND 1 = 1 — only when both are true, output is true.\n"
                "Absorption: A AND 0 = 0; identity: A AND 1 = A.\n"
                "Idempotent: A AND A = A; contradiction: A AND \u00acA = 0."
            ),
        },
        examples={
            "id": [
                "Tabel kebenaran AND:",
                "  0 AND 0 = 0",
                "  0 AND 1 = 0",
                "  1 AND 0 = 0",
                "  1 AND 1 = 1",
                "",
                "Sifat: A AND 0 = 0, A AND 1 = A",
                "Sifat: A AND A = A, A AND \u00acA = 0",
            ],
            "en": [
                "AND truth table:",
                "  0 AND 0 = 0",
                "  0 AND 1 = 0",
                "  1 AND 0 = 0",
                "  1 AND 1 = 1",
                "",
                "Properties: A AND 0 = 0, A AND 1 = A",
                "Properties: A AND A = A, A AND \u00acA = 0",
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
                "Tabel kebenaran OR menunjukkan empat kemungkinan kombinasi input dan outputnya.\n"
                "0 OR 0 = 0 — jika kedua input salah, output salah.\n"
                "0 OR 1 = 1 — jika salah satu benar, output benar.\n"
                "1 OR 0 = 1 — jika salah satu benar, output benar.\n"
                "1 OR 1 = 1 — jika kedua benar, output benar.\n"
                "Absorbsi: A OR 1 = 1; identitas: A OR 0 = A.\n"
                "Idempoten: A OR A = A; hukum ekslusi tengah: A OR \u00acA = 1."
            ),
            "en": (
                "The OR truth table shows all four possible input combinations and their outputs.\n"
                "0 OR 0 = 0 — if both inputs are false, output is false.\n"
                "0 OR 1 = 1 — if at least one is true, output is true.\n"
                "1 OR 0 = 1 — if at least one is true, output is true.\n"
                "1 OR 1 = 1 — if both are true, output is true.\n"
                "Absorption: A OR 1 = 1; identity: A OR 0 = A.\n"
                "Idempotent: A OR A = A; law of excluded middle: A OR \u00acA = 1."
            ),
        },
        examples={
            "id": [
                "Tabel kebenaran OR:",
                "  0 OR 0 = 0",
                "  0 OR 1 = 1",
                "  1 OR 0 = 1",
                "  1 OR 1 = 1",
                "",
                "Sifat: A OR 1 = 1, A OR 0 = A",
                "Sifat: A OR A = A, A OR \u00acA = 1",
            ],
            "en": [
                "OR truth table:",
                "  0 OR 0 = 0",
                "  0 OR 1 = 1",
                "  1 OR 0 = 1",
                "  1 OR 1 = 1",
                "",
                "Properties: A OR 1 = 1, A OR 0 = A",
                "Properties: A OR A = A, A OR \u00acA = 1",
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
                "Hukum De Morgan menjelaskan bagaimana negasi berinteraksi dengan AND dan OR.\n"
                "\u00ac(A AND B) = \u00acA OR \u00acB — negasi dari AND menjadi OR dari negasi.\n"
                "\u00ac(A OR B) = \u00acA AND \u00acB — negasi dari OR menjadi AND dari negasi.\n"
                "Menerapkan \u00ac(A AND B): hitung (1 AND 0) = 0, lalu \u00ac0 = 1.\n"
                "Verifikasi pakai \u00acA OR \u00acB: \u00ac1 OR \u00ac0 = 0 OR 1 = 1, hasilnya cocok."
            ),
            "en": (
                "NOT 0 = 1 — the negation of false is true.\n"
                "NOT 1 = 0 — the negation of true is false.\n"
                "\u00ac(\u00acA) = A — double negation: flipping twice returns to the original.\n"
                "De Morgan's laws describe how negation distributes over AND and OR.\n"
                "\u00ac(A AND B) = \u00acA OR \u00acB — the negation of an AND becomes an OR of negations.\n"
                "\u00ac(A OR B) = \u00acA AND \u00acB — the negation of an OR becomes an AND of negations.\n"
                "Applying \u00ac(A AND B): evaluate (1 AND 0) = 0, then \u00ac0 = 1.\n"
                "Verify via \u00acA OR \u00acB: \u00ac1 OR \u00ac0 = 0 OR 1 = 1, confirming the law."
            ),
        },
        examples={
            "id": [
                "NOT 0 = 1",
                "NOT 1 = 0",
                "",
                "\u00ac(\u00acA) = A (negasi ganda)",
                "",
                "Hukum De Morgan:",
                "  \u00ac(A AND B) = \u00acA OR \u00acB",
                "  \u00ac(A OR B) = \u00acA AND \u00acB",
                "",
                "Contoh: \u00ac(1 AND 0) = \u00ac0 = 1",
                "       = \u00ac1 OR \u00ac0 = 0 OR 1 = 1 \u2713",
            ],
            "en": [
                "NOT 0 = 1",
                "NOT 1 = 0",
                "",
                "\u00ac(\u00acA) = A (double negation)",
                "",
                "De Morgan's Laws:",
                "  \u00ac(A AND B) = \u00acA OR \u00acB",
                "  \u00ac(A OR B) = \u00acA AND \u00acB",
                "",
                "Example: \u00ac(1 AND 0) = \u00ac0 = 1",
                "        = \u00ac1 OR \u00ac0 = 0 OR 1 = 1 \u2713",
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
                "XOR = (A OR B) AND NOT(A AND B) — output 1 saat input berbeda.\n"
                "XOR(0,0)=0 karena input sama; XOR(0,1)=1 karena input berbeda.\n"
                "XOR(1,0)=1 dan XOR(1,1)=0 — hanya input berbeda yang menghasilkan 1.\n"
                "Half adder adalah rangkaian dasar untuk menjumlahkan dua bit biner.\n"
                "SUM = A XOR B (bit hasil), CARRY = A AND B (bit pindahan).\n"
                "1 + 1 = 0 dengan carry 1 — karena 2 dalam biner ditulis sebagai 10."
            ),
            "en": (
                "NAND = NOT AND — universal gate: outputs 0 only when both inputs are 1.\n"
                "NAND(0,0)=1 and NAND(0,1)=1 because at least one input is 0.\n"
                "NAND(1,0)=1, NAND(1,1)=0 — only when both are 1 does output become 0.\n"
                "XOR = (A OR B) AND NOT(A AND B) — outputs 1 when inputs differ.\n"
                "XOR(0,0)=0 because inputs match; XOR(0,1)=1 because inputs differ.\n"
                "XOR(1,0)=1 and XOR(1,1)=0 — only differing inputs yield 1.\n"
                "A half adder is a basic circuit for adding two binary bits.\n"
                "SUM = A XOR B (result bit), CARRY = A AND B (carry bit).\n"
                "1 + 1 = 0 with carry 1 — because 2 in binary is written as 10."
            ),
        },
        examples={
            "id": [
                "Gerbang NAND: NOT(A AND B)",
                "  NAND(0,0)=1, NAND(0,1)=1",
                "  NAND(1,0)=1, NAND(1,1)=0",
                "",
                "Gerbang XOR: A\u2295B = (A OR B) AND NOT(A AND B)",
                "  XOR(0,0)=0, XOR(0,1)=1",
                "  XOR(1,0)=1, XOR(1,1)=0",
                "",
                "Half adder (penjumlah 1-bit):",
                "  SUM = A XOR B, CARRY = A AND B",
                "  1 + 1 = 0 carry 1",
            ],
            "en": [
                "NAND gate: NOT(A AND B)",
                "  NAND(0,0)=1, NAND(0,1)=1",
                "  NAND(1,0)=1, NAND(1,1)=0",
                "",
                "XOR gate: A\u2295B = (A OR B) AND NOT(A AND B)",
                "  XOR(0,0)=0, XOR(0,1)=1",
                "  XOR(1,0)=1, XOR(1,1)=0",
                "",
                "Half adder (1-bit adder):",
                "  SUM = A XOR B, CARRY = A AND B",
                "  1 + 1 = 0 carry 1",
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
