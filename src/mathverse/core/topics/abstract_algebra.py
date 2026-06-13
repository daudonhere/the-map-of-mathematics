from __future__ import annotations

import random

from mathverse.core.models import SubTopic

subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Grup", "en": "Group"},
        description={
            "id": (
                "Grup adalah himpunan dengan operasi biner yang memenuhi "
                "sifat tertutup, asosiatif, memiliki identitas, dan setiap elemen memiliki invers."
            ),
            "en": (
                "A group is a set with a binary operation that satisfies "
                "closure, associativity, has an identity, and every element has an inverse."
            ),
        },
        explanation={
            "id": (
                "Tertutup: a\u2217b selalu berada dalam himpunan — hasil operasi dua elemen tetap di dalam grup.\n"
                "\u2124 dengan + tertutup: 2+3=5 tetap di \u2124.\n"
                "Identitas: terdapat e sehingga a\u2217e = e\u2217a = a — 0 adalah identitas untuk +.\n"
                "Invers: terdapat a\u207b\u00b9 sehingga a\u2217a\u207b\u00b9 = e — invers 5 adalah \u22125.\n"
                "\u2124 dengan + adalah grup: memenuhi keempat sifat grup.\n"
                "\u2124\u2084 (mod 4) juga grup siklik dengan + modulo 4.\n"
                "3+2 = 5\u22611 mod 4 — tertutup dalam \u2124\u2084.\n"
                "Invers 1 adalah 3 karena 1+3\u22610 mod 4."
            ),
            "en": (
                "Closure: a\u2217b is always in the set — the result stays inside the group.\n"
                "\u2124 under + is closed: 2+3=5 stays in \u2124.\n"
                "Identity: there exists e such that a\u2217e = e\u2217a = a — 0 is the identity for +.\n"
                "Inverse: there exists a\u207b\u00b9 such that a\u2217a\u207b\u00b9 = e — inverse of 5 is \u22125.\n"
                "\u2124 with + is a group: it satisfies all four group properties.\n"
                "\u2124\u2084 (mod 4) is also a cyclic group under addition modulo 4.\n"
                "3+2 = 5\u22611 mod 4 — closure holds in \u2124\u2084.\n"
                "Inverse of 1 is 3 because 1+3\u22610 mod 4."
            ),
        },
        examples={
            "id": [
                "Grup (\u2124, +): bilangan bulat dengan penjumlahan",
                "  Tertutup: 2 + 3 = 5 \u2208 \u2124",
                "  Identitas: 0, karena a + 0 = a",
                "  Invers: invers dari 5 adalah \u22125",
                "",
                "Grup (\u2124\u2084, +): jam bilangan mod 4",
                "  Elemen: {0, 1, 2, 3}",
                "  3 + 2 = 5 mod 4 = 1",
                "  Invers dari 1 adalah 3 (1+3=4\u22670)",
            ],
            "en": [
                "Group (\u2124, +): integers under addition",
                "  Closure: 2 + 3 = 5 \u2208 \u2124",
                "  Identity: 0, since a + 0 = a",
                "  Inverse: inverse of 5 is \u22125",
                "",
                "Group (\u2124\u2084, +): clock arithmetic mod 4",
                "  Elements: {0, 1, 2, 3}",
                "  3 + 2 = 5 mod 4 = 1",
                "  Inverse of 1 is 3 (1+3=4\u22670)",
            ],
        },
        playground="group",
    ),
    SubTopic(
        title={"id": "Ring", "en": "Ring"},
        description={
            "id": (
                "Ring adalah struktur aljabar dengan dua operasi biner "
                "(+ dan \u00d7) yang membentuk grup Abelian terhadap + "
                "dan semigrup terhadap \u00d7, dengan sifat distributif."
            ),
            "en": (
                "A ring is an algebraic structure with two binary operations "
                "(+ and \u00d7) forming an Abelian group under + "
                "and a semigroup under \u00d7, with distributive properties."
            ),
        },
        explanation={
            "id": (
                "Grup Abelian terhadap +: penjumlahan bersifat komutatif (a+b = b+a), ada identitas 0, dan setiap elemen punya invers.\n"
                "Semigrup terhadap \u00d7: perkalian bersifat tertutup dan asosiatif, tetapi tidak perlu komutatif atau memiliki invers.\n"
                "Distributif: a\u00d7(b+c) = a\u00d7b + a\u00d7c — perkalian didistribusikan ke penjumlahan.\n"
                "Distributif juga berlaku: (a+b)\u00d7c = a\u00d7c + b\u00d7c.\n"
                "\u2124 dengan + dan \u00d7 adalah ring — contoh paling dasar.\n"
                "M\u2082(\u2124) matriks 2\u00d72 dengan entri integer juga membentuk ring.\n"
                "Penjumlahan matriks bersifat komutatif — sesuai syarat grup Abelian.\n"
                "Perkalian matriks tidak komutatif — ring tidak memerlukan komutatifitas perkalian."
            ),
            "en": (
                "Abelian group under +: addition is commutative (a+b = b+a), identity 0 exists, every element has an inverse.\n"
                "Semigroup under \u00d7: multiplication is closed and associative, but need not be commutative or have inverses.\n"
                "Distributive: a\u00d7(b+c) = a\u00d7b + a\u00d7c — multiplication distributes over addition.\n"
                "Distributive also: (a+b)\u00d7c = a\u00d7c + b\u00d7c.\n"
                "\u2124 with + and \u00d7 is a ring — the most basic example.\n"
                "M\u2082(\u2124) 2\u00d72 matrices with integer entries also form a ring.\n"
                "Matrix addition is commutative — satisfies the Abelian group requirement.\n"
                "Matrix multiplication is not commutative — rings do not require commutative multiplication."
            ),
        },
        examples={
            "id": [
                "Ring \u2124 (bilangan bulat):",
                "  (+): grup Abelian, identitas 0",
                "  (\u00d7): tertutup, asosiatif",
                "  Distributif: 2\u00d7(3+4) = 2\u00d77 = 14",
                "                2\u00d73 + 2\u00d74 = 6+8 = 14",
                "",
                "Ring M\u2082(\u2124): matriks 2\u00d72 dengan entri bilangan bulat",
                "  (+): penjumlahan matriks (komutatif)",
                "  (\u00d7): perkalian matriks (tidak komutatif)",
            ],
            "en": [
                "Ring \u2124 (integers):",
                "  (+): Abelian group, identity 0",
                "  (\u00d7): closed, associative",
                "  Distributive: 2\u00d7(3+4) = 2\u00d77 = 14",
                "                 2\u00d73 + 2\u00d74 = 6+8 = 14",
                "",
                "Ring M\u2082(\u2124): 2\u00d72 matrices with integer entries",
                "  (+): matrix addition (commutative)",
                "  (\u00d7): matrix multiplication (not commutative)",
            ],
        },
        playground="ring",
    ),
    SubTopic(
        title={"id": "Field (Lapangan)", "en": "Field"},
        description={
            "id": (
                "Field adalah ring di mana setiap elemen tak-nol memiliki "
                "invers perkalian, sehingga pembagian selalu dapat dilakukan."
            ),
            "en": (
                "A field is a ring where every non-zero element has "
                "a multiplicative inverse, so division is always possible."
            ),
        },
        explanation={
            "id": (
                "\u211a adalah field: setiap bilangan rasional a/b (b\u22600) memiliki invers perkalian b/a.\n"
                "\u211d adalah field: \u221a2 \u00d7 1/\u221a2 = 1 — invers perkalian ada untuk setiap elemen tak-nol.\n"
                "\u2124 bukan field karena 2 tidak memiliki invers perkalian dalam \u2124 (1/2 \u2209 \u2124).\n"
                "\u2124\u2085 (mod 5) adalah field karena setiap elemen tak-nol punya invers modulo.\n"
                "\u2124\u2083 = {0,1,2} juga field hingga dengan 3 elemen.\n"
                "Dalam \u2124\u2083, 2\u207b\u00b9 = 2 karena 2\u00d72 = 4\u22611 mod 3."
            ),
            "en": (
                "\u211a is a field: every rational number a/b (b\u22600) has multiplicative inverse b/a.\n"
                "\u211d is a field: \u221a2 \u00d7 1/\u221a2 = 1 — multiplicative inverse exists for every non-zero element.\n"
                "\u2124 is not a field because 2 has no multiplicative inverse in \u2124 (1/2 \u2209 \u2124).\n"
                "\u2124\u2085 (mod 5) is a field — every non-zero element has a modular inverse.\n"
                "\u2124\u2083 = {0,1,2} is also a finite field with 3 elements.\n"
                "In \u2124\u2083, 2\u207b\u00b9 = 2 because 2\u00d72 = 4\u22611 mod 3."
            ),
        },
        examples={
            "id": [
                "Field \u211a: 2/3 \u00d7 3/2 = 1 (invers perkalian)",
                "Field \u211d: \u221a2 \u00d7 1/\u221a2 = 1",
                "",
                "Bukan field: \u2124 (2 tidak punya invers)",
                "Field \u2124\u2085: 2 \u00d7 3 = 6 \u2261 1 (mod 5), invers 2 adalah 3",
                "",
                "Field \u2124\u2083: {0,1,2}",
                "  1\u207b\u00b9 = 1, 2\u207b\u00b9 = 2 (karena 2\u00d72=4\u22611 mod 3)",
            ],
            "en": [
                "Field \u211a: 2/3 \u00d7 3/2 = 1 (multiplicative inverse)",
                "Field \u211d: \u221a2 \u00d7 1/\u221a2 = 1",
                "",
                "Not a field: \u2124 (2 has no inverse)",
                "Field \u2124\u2085: 2 \u00d7 3 = 6 \u2261 1 (mod 5), inverse of 2 is 3",
                "",
                "Field \u2124\u2083: {0,1,2}",
                "  1\u207b\u00b9 = 1, 2\u207b\u00b9 = 2 (since 2\u00d72=4\u22611 mod 3)",
            ],
        },
        playground="field",
    ),
    SubTopic(
        title={"id": "Modul", "en": "Module"},
        description={
            "id": (
                "Modul adalah generalisasi dari ruang vektor di mana skalar "
                "berasal dari ring (bukan hanya field)."
            ),
            "en": (
                "A module is a generalization of a vector space where scalars "
                "come from a ring (not just a field)."
            ),
        },
        explanation={
            "id": (
                "Ruang vektor \u211d\u207f adalah modul atas field \u211d — skalar dari field, vektor dari ruang vektor.\n"
                "Grup Abelian (\u2124, +) adalah \u2124-modul: perkalian skalar n\u00b7a menjumlahkan a sebanyak n kali.\n"
                "Modul atas ring polinomial \u2124[x]: polinomial bertindak sebagai operator linear pada modul.\n"
                "Polinomial menerapkan aksi linear — contoh konkret modul atas ring tak-komutatif.\n"
                "Setiap grup Abelian secara otomatis adalah modul atas \u2124.\n"
                "Ini karena \u2124 adalah ring paling dasar — semua grup Abelian mewarisi struktur \u2124-modul."
            ),
            "en": (
                "Vector space \u211d\u207f is a module over the field \u211d — scalars from a field, vectors from the space.\n"
                "Abelian group (\u2124, +) is a \u2124-module: scalar multiplication n\u00b7a adds a n times.\n"
                "Module over polynomial ring \u2124[x]: polynomials act as linear operators on the module.\n"
                "Polynomials apply a linear action — a concrete example of a module over a non-commutative ring.\n"
                "Every Abelian group is automatically a module over \u2124.\n"
                "This is because \u2124 is the most basic ring — all Abelian groups inherit the \u2124-module structure."
            ),
        },
        examples={
            "id": [
                "Ruang vektor \u211d\u207f adalah modul atas field \u211d",
                "\u2124-modul: grup (\u2124, +) dengan perkalian skalar n\u00b7a = a\u00d7n",
                "",
                "Modul atas ring polinomial \u2124[x]:",
                "  polinomial bertindak sebagai operator linear",
                "",
                "Setiap grup Abelian adalah modul atas \u2124",
                "  (ini karena \u2124 adalah ring paling dasar)",
            ],
            "en": [
                "Vector space \u211d\u207f is a module over the field \u211d",
                "\u2124-module: group (\u2124, +) with scalar multiplication n\u00b7a = a\u00d7n",
                "",
                "Module over polynomial ring \u2124[x]:",
                "  polynomials act as linear operators",
                "",
                "Every Abelian group is a module over \u2124",
                "  (this is because \u2124 is the most basic ring)",
            ],
        },
        playground="module",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "group":
        props = [
            ("\u2124, +", _("yes", "ya"), _("no", "tidak"), _("yes", "ya"), _("yes", "ya")),
            ("\u211a\u207a, \u00d7", _("yes", "ya"), _("yes", "ya"), _("yes", "ya"), _("no", "tidak")),
            ("\u2124\u2084, +", _("yes", "ya"), _("yes", "ya"), _("yes", "ya"), _("yes", "ya")),
        ]
        chosen = random.choice(props)
        name, closure, assoc, ident, inv = chosen
        q = _(
            f"Check group: {name}\n"
            f"Closure(1/0)?\nAssociative(1/0)?\nIdentity(1/0)?\nInverse(1/0)?",
            f"Periksa grup: {name}\n"
            f"Tertutup(1/0)?\nAsosiatif(1/0)?\nIdentitas(1/0)?\nInvers(1/0)?",
        )
        ans_closure = "1" if closure == _("yes", "ya") else "0"
        ans_assoc = "1" if assoc == _("yes", "ya") else "0"
        ans_ident = "1" if ident == _("yes", "ya") else "0"
        ans_inv = "1" if inv == _("yes", "ya") else "0"
        ans = f"{ans_closure}{ans_assoc}{ans_ident}{ans_inv}"
        return q, ans, 0.0

    elif playground == "field":
        examples_list = [
            ("\u211a", _("yes", "ya")),
            ("\u211d", _("yes", "ya")),
            ("\u2124", _("no", "tidak")),
            ("\u2124\u2085", _("yes", "ya")),
            ("\u2124\u2086", _("no", "tidak")),
        ]
        name, ans = random.choice(examples_list)
        q = _(f"Is {name} a field? (yes/no)", f"Apakah {name} field? (ya/tidak)")
        return q, ans, 0.0

    elif playground == "ring":
        candidates = [
            ("\u2124", _("yes", "ya")),
            ("\u211a", _("yes", "ya")),
            ("M\u2082(\u2124)", _("yes", "ya")),
            ("\u2124/n\u2124", _("yes", "ya")),
            ("\u2115", _("no", "tidak")),
        ]
        name, ans = random.choice(candidates)
        q = _(f"Is {name} a ring? (yes/no)", f"Apakah {name} ring? (ya/tidak)")
        return q, ans, 0.0

    elif playground == "module":
        examples_list = [
            ("a vector space over \u211d", _("yes", "ya")),
            ("any Abelian group over \u2124", _("yes", "ya")),
            ("an ideal of ring R over R", _("yes", "ya")),
            ("\u2115 over \u2124", _("no", "tidak")),
            ("a set with no addition", _("no", "tidak")),
        ]
        name, ans = random.choice(examples_list)
        q = _(f"Is {name} a module? (yes/no)", f"Apakah {name} modul? (ya/tidak)")
        return q, ans, 0.0

    return None


__all__ = ["gen_question", "subtopics"]
