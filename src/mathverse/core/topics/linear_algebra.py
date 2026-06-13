from __future__ import annotations

import math
import random

from mathverse.core.models import SubTopic

subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Vektor", "en": "Vectors"},
        description={
            "id": (
                "Vektor adalah besaran yang memiliki nilai dan arah, "
                "direpresentasikan sebagai ruas garis berarah."
            ),
            "en": (
                "A vector is a quantity that has both magnitude and direction, "
                "represented as a directed line segment."
            ),
        },
        explanation={
            "id": (
                "Vektor \u20d1(2,3) dimulai dari titik asal (0,0) menuju titik (2,3) dalam bidang 2D.\n"
                "Panjang vektor |\u20d1| = \u221a(2\u00b2 + 3\u00b2) = \u221a13 \u2248 3.61 — dihitung dengan teorema Pythagoras.\n"
                "Penjumlahan vektor: (2,3) + (1,4) = (3,7) — jumlahkan komponen yang sejajar.\n"
                "Perkalian skalar: 2\u00b7(2,3) = (4,6) — setiap komponen dikalikan dengan skalar."
            ),
            "en": (
                "Vector v = (2,3) starts from origin (0,0) to point (2,3) in 2D space.\n"
                "Magnitude |v| = \u221a(2\u00b2 + 3\u00b2) = \u221a13 \u2248 3.61 — calculated using the Pythagorean theorem.\n"
                "Vector addition: (2,3) + (1,4) = (3,7) — add corresponding components.\n"
                "Scalar multiplication: 2\u00b7(2,3) = (4,6) — multiply each component by the scalar."
            ),
        },
        examples={
            "id": [
                "Vektor \u20d1 = (2, 3)",
                "Panjang: |\u20d1| = \u221a(2\u00b2 + 3\u00b2) = \u221a13",
                "",
                "Penjumlahan: (2,3) + (1,4) = (3,7)",
                "Skalar: 2\u00b7(2,3) = (4,6)",
            ],
            "en": [
                "Vector v = (2, 3)",
                "Magnitude: |v| = \u221a(2\u00b2 + 3\u00b2) = \u221a13",
                "",
                "Addition: (2,3) + (1,4) = (3,7)",
                "Scalar: 2\u00b7(2,3) = (4,6)",
            ],
        },
        playground="vectors",
    ),
    SubTopic(
        title={"id": "Matriks", "en": "Matrices"},
        description={
            "id": (
                "Matriks adalah susunan bilangan berbentuk persegi panjang "
                "yang diatur dalam baris dan kolom."
            ),
            "en": (
                "A matrix is a rectangular array of numbers "
                "arranged in rows and columns."
            ),
        },
        explanation={
            "id": (
                "Matriks 2\u00d72: [[a,b],[c,d]] — dua baris dan dua kolom, a,b,c,d adalah entri.\n"
                "Penjumlahan matriks: [[1,2],[3,4]] + [[5,6],[7,8]] = [[6,8],[10,12]] — jumlahkan entri yang seposisi.\n"
                "Perkalian baris pertama: [1\u00d75+2\u00d77, 1\u00d76+2\u00d78] — kalikan baris pertama A dengan tiap kolom B.\n"
                "Perkalian baris kedua: [3\u00d75+4\u00d77, 3\u00d76+4\u00d78] — kalikan baris kedua A dengan tiap kolom B."
            ),
            "en": (
                "2\u00d72 matrix: [[a,b],[c,d]] — two rows and two columns, a,b,c,d are entries.\n"
                "Matrix addition: [[1,2],[3,4]] + [[5,6],[7,8]] = [[6,8],[10,12]] — add entries in same position.\n"
                "First row multiplication: [1\u00d75+2\u00d77, 1\u00d76+2\u00d78] — multiply first row of A by each column of B.\n"
                "Second row multiplication: [3\u00d75+4\u00d77, 3\u00d76+4\u00d78] — multiply second row of A by each column of B."
            ),
        },
        examples={
            "id": [
                "Matriks A = [[1,2],[3,4]], B = [[5,6],[7,8]]",
                "A + B = [[6,8],[10,12]]",
                "A\u00b7B = [[1\u00d75+2\u00d77, 1\u00d76+2\u00d78],",
                "       [3\u00d75+4\u00d77, 3\u00d76+4\u00d78]]",
            ],
            "en": [
                "Matrix A = [[1,2],[3,4]], B = [[5,6],[7,8]]",
                "A + B = [[6,8],[10,12]]",
                "A\u00b7B = [[1\u00d75+2\u00d77, 1\u00d76+2\u00d78],",
                "       [3\u00d75+4\u00d77, 3\u00d76+4\u00d78]]",
            ],
        },
        playground="matrices",
    ),
    SubTopic(
        title={"id": "Determinan", "en": "Determinant"},
        description={
            "id": (
                "Determinan adalah nilai skalar yang dihitung dari matriks persegi, "
                "menunjukkan apakah matriks tersebut invertible (dapat dibalik)."
            ),
            "en": (
                "The determinant is a scalar value computed from a square matrix, "
                "indicating whether the matrix is invertible."
            ),
        },
        explanation={
            "id": (
                "det[[1,2],[3,4]] = 1\u00d74 \u2212 2\u00d73 = 4 \u2212 6 = \u22122 — terapkan rumus 2\u00d72: hasil kali diagonal utama kurang diagonal samping.\n"
                "det[[2,0],[0,2]] = 2\u00d72 \u2212 0\u00d70 = 4 — determinan matriks diagonal adalah hasil kali entri diagonalnya.\n"
                "Untuk matriks 3\u00d73, gunakan aturan Sarrus: jumlahkan hasil kali tiga diagonal utama.\n"
                "Diagonal utama: 1\u00b75\u00b79 + 2\u00b76\u00b77 + 3\u00b74\u00b78 = 45 + 84 + 96 = 225."
            ),
            "en": (
                "det[[1,2],[3,4]] = 1\u00d74 \u2212 2\u00d73 = 4 \u2212 6 = \u22122 — apply the 2\u00d72 formula: product of main diagonal minus anti-diagonal.\n"
                "det[[2,0],[0,2]] = 2\u00d72 \u2212 0\u00d70 = 4 — determinant of a diagonal matrix is the product of its diagonal entries.\n"
                "For a 3\u00d73 matrix, use the Sarrus rule: sum the products of three main diagonals.\n"
                "Main diagonals: 1\u00b75\u00b79 + 2\u00b76\u00b77 + 3\u00b74\u00b78 = 45 + 84 + 96 = 225."
            ),
        },
        examples={
            "id": [
                "det[[1,2],[3,4]] = 1\u00d74 \u2212 2\u00d73 = 4 \u2212 6 = \u22122",
                "det[[2,0],[0,2]] = 2\u00d72 \u2212 0\u00d70 = 4",
                "",
                "det[[1,2,3],[4,5,6],[7,8,9]]",
                "  = 45 + 84 + 96 \u2212 105 \u2212 48 \u2212 72 = 0",
            ],
            "en": [
                "det[[1,2],[3,4]] = 1\u00d74 \u2212 2\u00d73 = 4 \u2212 6 = \u22122",
                "det[[2,0],[0,2]] = 2\u00d72 \u2212 0\u00d70 = 4",
                "",
                "det[[1,2,3],[4,5,6],[7,8,9]]",
                "  = 45 + 84 + 96 \u2212 105 \u2212 48 \u2212 72 = 0",
            ],
        },
        playground="determinant",
    ),
    SubTopic(
        title={"id": "Nilai Eigen (Eigenvalue)", "en": "Eigenvalue"},
        description={
            "id": (
                "Nilai eigen (\u03bb) adalah skalar yang memenuhi A\u00b7v = \u03bb\u00b7v, "
                "di mana v adalah vektor eigen dari matriks A."
            ),
            "en": (
                "An eigenvalue (\u03bb) is a scalar satisfying A\u00b7v = \u03bb\u00b7v, "
                "where v is an eigenvector of matrix A."
            ),
        },
        explanation={
            "id": (
                "A = [[2,0],[0,3]] adalah matriks diagonal — nilai eigen langsung terlihat pada diagonal.\n"
                "Persamaan karakteristik: det(A \u2212 \u03bbI) = (2\u2212\u03bb)(3\u2212\u03bb) = 0 — faktorkan untuk mencari \u03bb.\n"
                "Nilai eigen: \u03bb\u2081 = 2 dan \u03bb\u2082 = 3 — akar-akar persamaan karakteristik.\n"
                "A = [[4,1],[2,3]] — contoh matriks non-diagonal dengan nilai eigen lebih rumit."
            ),
            "en": (
                "A = [[2,0],[0,3]] is a diagonal matrix — eigenvalues are directly on the diagonal.\n"
                "Characteristic equation: det(A \u2212 \u03bbI) = (2\u2212\u03bb)(3\u2212\u03bb) = 0 — factor to find \u03bb.\n"
                "Eigenvalues: \u03bb\u2081 = 2 and \u03bb\u2082 = 3 — roots of the characteristic equation.\n"
                "A = [[4,1],[2,3]] — example of a non-diagonal matrix with more complex eigenvalues."
            ),
        },
        examples={
            "id": [
                "A = [[2,0],[0,3]]",
                "det(A \u2212 \u03bbI) = (2\u2212\u03bb)(3\u2212\u03bb) = 0",
                "\u03bb\u2081 = 2, \u03bb\u2082 = 3",
                "",
                "A = [[4,1],[2,3]]",
            ],
            "en": [
                "A = [[2,0],[0,3]]",
                "det(A \u2212 \u03bbI) = (2\u2212\u03bb)(3\u2212\u03bb) = 0",
                "\u03bb\u2081 = 2, \u03bb\u2082 = 3",
                "",
                "A = [[4,1],[2,3]]",
            ],
        },
        playground="eigenvalue",
    ),
    SubTopic(
        title={"id": "Vektor Eigen (Eigenvector)", "en": "Eigenvector"},
        description={
            "id": (
                "Vektor eigen adalah vektor tak-nol v yang hanya berubah skala "
                "(bukan arah) ketika ditransformasi oleh matriks A."
            ),
            "en": (
                "An eigenvector is a non-zero vector v that only changes in scale "
                "(not direction) when transformed by matrix A."
            ),
        },
        explanation={
            "id": (
                "A = [[2,0],[0,3]], \u03bb\u2081 = 2 — cari vektor v sehingga (A \u2212 2I)v = 0.\n"
                "(A \u2212 2I) = [[0,0],[0,1]], sistem: 0\u00b7x + 0\u00b7y = 0 dan 0\u00b7x + 1\u00b7y = 0 \u2192 y = 0.\n"
                "v\u2081 = (1,0) — vektor eigen untuk \u03bb = 2 (sembarang kelipatan juga berlaku).\n"
                "\u03bb\u2082 = 3: (A \u2212 3I) = [[\u22121,0],[0,0]] \u2192 selesaikan \u2212x = 0 \u2192 x = 0."
            ),
            "en": (
                "A = [[2,0],[0,3]], \u03bb\u2081 = 2 — find vector v such that (A \u2212 2I)v = 0.\n"
                "(A \u2212 2I) = [[0,0],[0,1]], system: 0\u00b7x + 0\u00b7y = 0 and 0\u00b7x + 1\u00b7y = 0 \u2192 y = 0.\n"
                "v\u2081 = (1,0) — eigenvector for \u03bb = 2 (any scalar multiple also works).\n"
                "\u03bb\u2082 = 3: (A \u2212 3I) = [[\u22121,0],[0,0]] \u2192 solve \u2212x = 0 \u2192 x = 0."
            ),
        },
        examples={
            "id": [
                "A = [[2,0],[0,3]], \u03bb\u2081 = 2",
                "(A \u2212 2I)v = 0 \u2192 [[0,0],[0,1]]v = 0",
                "",
                "\u03bb\u2082 = 3: (A \u2212 3I)v = 0 \u2192 [[\u22121,0],[0,0]]v = 0",
                "v\u2082 = (0,1) — vektor eigen",
            ],
            "en": [
                "A = [[2,0],[0,3]], \u03bb\u2081 = 2",
                "(A \u2212 2I)v = 0 \u2192 [[0,0],[0,1]]v = 0",
                "",
                "\u03bb\u2082 = 3: (A \u2212 3I)v = 0 \u2192 [[\u22121,0],[0,0]]v = 0",
                "v\u2082 = (0,1) — eigenvector",
            ],
        },
        playground="eigenvector",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "vectors":
        kind = random.choice(["mag", "dot", "add"])
        if kind == "mag":
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            mag = math.sqrt(x * x + y * y)
            ans = f"{mag:.2f}"
            q = _(f"|({x},{y})| = ?", f"|({x},{y})| = ?")
            return q, ans, mag
        elif kind == "dot":
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            d = random.randint(1, 5)
            ans = a * c + b * d
            q = _(f"({a},{b})\u00b7({c},{d}) = ?", f"({a},{b})\u00b7({c},{d}) = ?")
            return q, str(ans), ans
        else:
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            d = random.randint(1, 5)
            ans_x = a + c
            ans_y = b + d
            ans = f"({ans_x},{ans_y})"
            q = _(f"({a},{b}) + ({c},{d}) = ?", f"({a},{b}) + ({c},{d}) = ?")
            return q, ans, 0.0

    elif playground == "matrices":
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        kind = random.choice(["add", "det"])
        if kind == "add":
            e = random.randint(1, 5)
            f = random.randint(1, 5)
            g = random.randint(1, 5)
            h = random.randint(1, 5)
            ans_a = a + e
            ans_b = b + f
            ans_c = c + g
            ans_d = d + h
            ans = f"[[{ans_a},{ans_b}],[{ans_c},{ans_d}]]"
            q = _(
                f"[[{a},{b}],[{c},{d}]] + [[{e},{f}],[{g},{h}]] = ?",
                f"[[{a},{b}],[{c},{d}]] + [[{e},{f}],[{g},{h}]] = ?",
            )
            return q, ans, 0.0
        else:
            det = a * d - b * c
            q = _(
                f"det[[{a},{b}],[{c},{d}]] = ?",
                f"det[[{a},{b}],[{c},{d}]] = ?",
            )
            return q, str(det), det

    elif playground == "determinant":
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        det = a * d - b * c
        q = _(f"det[[{a},{b}],[{c},{d}]] = ?", f"det[[{a},{b}],[{c},{d}]] = ?")
        return q, str(det), det

    elif playground == "eigenvalue":
        pairs = [
            (2, 0, 0, 3),
            (3, 0, 0, 5),
            (1, 0, 0, 4),
            (4, 0, 0, 1),
            (2, 0, 0, 2),
        ]
        a, b, c, d = random.choice(pairs)
        lam1 = a
        lam2 = d
        if random.randint(0, 1):
            q = _(
                f"A = [[{a},{b}],[{c},{d}]], find one eigenvalue",
                f"A = [[{a},{b}],[{c},{d}]], cari satu nilai eigen",
            )
            return q, str(lam1), lam1
        else:
            q = _(
                f"A = [[{a},{b}],[{c},{d}]], find the other eigenvalue",
                f"A = [[{a},{b}],[{c},{d}]], cari nilai eigen lainnya",
            )
            return q, str(lam2), lam2

    elif playground == "eigenvector":
        pairs = [
            ((2, 0, 0, 3), 2, "(1,0)"),
            ((2, 0, 0, 3), 3, "(0,1)"),
            ((4, 0, 0, 1), 4, "(1,0)"),
            ((4, 0, 0, 1), 1, "(0,1)"),
        ]
        (a, b, c, d), lam, vec = random.choice(pairs)
        q = _(
            f"A = [[{a},{b}],[{c},{d}]], \u03bb = {lam}, find one eigenvector",
            f"A = [[{a},{b}],[{c},{d}]], \u03bb = {lam}, cari satu vektor eigen",
        )
        return q, vec, 0.0

    return None


__all__ = ["gen_question", "subtopics"]
