from __future__ import annotations

import math
import os
import random

# ruff: noqa: RUF001
import select
import shutil
import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from mathverse.core.content import SubTopic, get_content
from mathverse.tui.launcher import BANNER, BANNER_WIDTH

_LOCALE: str = "en"


def _read_key() -> str:
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = os.read(fd, 1)
        if ch == b"\x1b":
            r, _, _ = select.select([fd], [], [], 0.1)
            if r:
                seq = os.read(fd, 2)
                return {b"[A": "up", b"[B": "down", b"[D": "left", b"[C": "right"}.get(
                    seq, "esc"
                )
            return "esc"
        elif ch in (b"\n", b"\r"):
            return "enter"
        elif ch == b"\t":
            return "tab"
        elif ch in (b"q", b"Q"):
            return "q"
        else:
            return ch.decode()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _read_input(prompt: str) -> str | None:
    """Read a line of input character by character. Returns None on Esc."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    buf = ""
    try:
        tty.setraw(fd)
        sys.stdout.write(prompt + " " + buf)
        sys.stdout.flush()
        while True:
            ch = os.read(fd, 1)
            if ch == b"\x1b":
                r, _, _ = select.select([fd], [], [], 0.1)
                if r:
                    os.read(fd, 2)
                    continue
                return None
            elif ch in (b"\n", b"\r"):
                sys.stdout.write("\r\n")
                sys.stdout.flush()
                return buf
            elif ch == b"\t":
                return None
            elif ch == b"\x7f":
                buf = buf[:-1]
            else:
                try:
                    c = ch.decode()
                    buf += c
                except UnicodeDecodeError:
                    continue
            line = prompt + " " + buf
            sys.stdout.write("\r" + " " * 80 + "\r" + line)
            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _read_input_at_cursor(fd: int, tw: int) -> str | None:
    old = termios.tcgetattr(fd)
    buf = ""
    pad = max(2, tw // 20)
    black_bg = "\x1b[48;2;0;0;0m"
    green_bg = "\x1b[48;2;26;58;26m"
    white_fg = "\x1b[38;2;255;255;255m"
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()
    try:
        tty.setraw(fd)
        while True:
            ch = os.read(fd, 1)
            if ch == b"\x1b":
                r, _, _ = select.select([fd], [], [], 0.1)
                if r:
                    os.read(fd, 2)
                    continue
                return None
            elif ch in (b"\n", b"\r"):
                sys.stdout.write("\r\n" + "\x1b[0m")
                sys.stdout.flush()
                return buf
            elif ch == b"\t":
                return "\r"
            elif ch == b"\x7f":
                buf = buf[:-1]
            else:
                try:
                    c = ch.decode()
                    buf += c
                except UnicodeDecodeError:
                    continue
            gap = tw - 2 * pad - 2 - 3 - len(buf)
            sys.stdout.write(
                "\r"
                + black_bg
                + " " * tw
                + "\r"
                + black_bg
                + " " * pad
                + green_bg
                + white_fg
                + "\u2502"
                + ">> "
                + buf
                + " " * max(0, gap)
                + "\u2502"
                + black_bg
                + " " * pad
                + f"\x1b[{pad + 5 + len(buf)}G"
            )
            sys.stdout.flush()
    finally:
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _gen_question(playground: str, locale: str) -> tuple[str, str, float]:
    """Generate a (question_text, answer_str, numeric_answer) tuple."""

    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "basic_ops":
        ops = [
            ("+", lambda a, b: a + b),
            ("\u2212", lambda a, b: a - b),
            ("\u00d7", lambda a, b: a * b),
        ]
        op_sym, op_fn = random.choice(ops)
        if op_sym == "\u00d7":
            a = random.randint(2, 12)
            b = random.randint(2, 12)
        else:
            a = random.randint(10, 99)
            b = random.randint(1, 50)
        if op_sym == "\u2212" and a < b:
            a, b = b, a
        ans = op_fn(a, b)
        q = f"{a} {op_sym} {b} = ?"
        return q, str(ans), ans

    elif playground == "powers":
        kind = random.choice(["square", "cube", "sqrt", "cbrt"])
        if kind == "square":
            n = random.randint(2, 15)
            ans = n * n
            return f"{n}\u00b2 = ?", str(ans), ans
        elif kind == "cube":
            n = random.randint(2, 6)
            ans = n * n * n
            return f"{n}\u00b3 = ?", str(ans), ans
        elif kind == "sqrt":
            n = random.randint(2, 12)
            ans = n * n
            return f"\u221a{ans} = ?", str(n), n
        else:
            n = random.randint(2, 4)
            ans = n * n * n
            return f"\u221b{ans} = ?", str(n), n

    elif playground == "mental_math":
        kind = random.choice(["comp", "double", "eleven", "near100"])
        if kind == "comp":
            a = random.randint(95, 99)
            b = random.randint(10, 50)
            ans = a + b
            return f"{a} + {b} = ?", str(ans), ans
        elif kind == "double":
            a = random.choice([25, 35, 45, 55, 65])
            b = random.choice([12, 14, 16, 18])
            ans = a * b
            return f"{a} \u00d7 {b} = ?", str(ans), ans
        elif kind == "eleven":
            a = random.randint(11, 99)
            ans = a * 11
            return f"{a} \u00d7 11 = ?", str(ans), ans
        else:
            a = random.randint(90, 99)
            b = random.randint(90, 99)
            ans = a * b
            return f"{a} \u00d7 {b} = ?", str(ans), ans

    elif playground == "properties":
        props = [
            ("commutative", lambda a, b: a + b == b + a),
            ("commutative", lambda a, b: a * b == b * a),
            ("associative", lambda a, b, c: (a + b) + c == a + (b + c)),
            ("associative", lambda a, b, c: (a * b) * c == a * (b * c)),
            ("distributive", lambda a, b, c: a * (b + c) == a * b + a * c),
        ]
        ans_map = {
            "commutative": _("commutative", "komutatif"),
            "associative": _("associative", "asosiatif"),
            "distributive": _("distributive", "distributif"),
        }
        choice = random.choice(props)
        prop_en = choice[0]
        prop_id = ans_map[prop_en]
        label = _("Property shown:", "Sifat ditunjukkan:")
        if prop_en in ("commutative",):
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            q = f"{label} {a} + {b} = {b} + {a}"
            return q, prop_id if locale == "id" else prop_en, 0.0
        elif prop_en == "associative":
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            c = random.randint(2, 8)
            q = f"{label} ({a} + {b}) + {c} = {a} + ({b} + {c})"
            return q, prop_id if locale == "id" else prop_en, 0.0
        elif prop_en == "distributive":
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)
            q = f"{label} {a} \u00d7 ({b} + {c}) = {a}\u00d7{b} + {a}\u00d7{c}"
            return q, prop_id if locale == "id" else prop_en, 0.0

    elif playground == "number_types":
        kind = random.choice(["prime", "square", "even", "odd"])
        if kind == "prime":
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
            compos = [4, 6, 8, 9, 10, 12, 14, 15, 16]
            n = random.choice(primes)
            distract = random.choice(compos)
            q_fmt = _(
                "Is {} prime or composite?", "Apakah {} bilangan prima atau komposit?"
            )
            if random.randint(0, 1):
                ans = _("prime", "prima")
                q = q_fmt.format(n)
                return q, ans, 0.0
            else:
                ans = _("composite", "komposit")
                q = q_fmt.format(distract)
                return q, ans, 0.0
        elif kind == "square":
            sq = random.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
            q_fmt = _(
                "Which number squared equals {}?",
                "Bilangan berapa yang dikuadratkan hasilnya {}?",
            )
            q = q_fmt.format(sq)
            ans = int(sq**0.5)
            return q, str(ans), ans
        elif kind == "even":
            n = random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
            q_fmt = _("Is {} even or odd?", "Apakah {} genap atau ganjil?")
            q = q_fmt.format(n)
            return q, _("even", "genap"), 0.0
        elif kind == "odd":
            n = random.choice([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
            q_fmt = _("Is {} even or odd?", "Apakah {} genap atau ganjil?")
            q = q_fmt.format(n)
            return q, _("odd", "ganjil"), 0.0

    elif playground == "factors":
        pairs = [
            (4, 6),
            (6, 8),
            (3, 4),
            (5, 6),
            (4, 5),
            (6, 10),
            (5, 7),
            (8, 10),
            (8, 12),
            (12, 18),
            (15, 25),
            (6, 9),
            (10, 15),
            (14, 21),
            (16, 24),
            (9, 15),
        ]
        kind = random.choice(["gcf", "lcm"])
        a, b = random.choice(pairs)
        ans = math.gcd(a, b)
        if kind == "gcf":
            q = _("GCF of {} and {} = ?", "FPB dari {} dan {} = ?").format(a, b)
            return q, str(ans), ans
        else:
            ans = a * b // ans
            q = _("LCM of {} and {} = ?", "KPK dari {} dan {} = ?").format(a, b)
            return q, str(ans), ans

    elif playground == "ratios":
        kind = random.choice(["simplify", "find_part"])
        if kind == "simplify":
            pairs = [(6, 8), (10, 15), (12, 18), (8, 12), (14, 21), (9, 12)]
            a, b = random.choice(pairs)
            g = math.gcd(a, b)
            q = _("Simplify ratio {}:{} = ?", "Sederhanakan rasio {}:{} = ?").format(
                a, b
            )
            ans = f"1:{b // g}" if g == a else f"{a // g}:{b // g}"
            return q, ans, 0.0
        else:
            a, b = random.choice([(2, 3), (3, 5), (4, 7), (5, 8), (1, 4), (3, 7)])
            total = random.choice([30, 40, 50, 60, 70, 80])
            if (a + b) > total:
                total = (a + b) * random.randint(2, 5)
            part_b = total // (a + b) * b
            q = _(
                "Ratio {}:{}, total {}. Value of larger part = ?",
                "Rasio {}:{}, total {}. Nilai bagian terbesar = ?",
            ).format(a, b, total)
            return q, str(part_b), part_b

    elif playground == "percentages":
        kind = random.choice(["of", "of_rev", "change"])
        if kind == "of":
            pct = random.choice([10, 20, 25, 30, 40, 50, 60, 75])
            num = random.choice([40, 60, 80, 100, 120, 200, 300])
            ans = num * pct // 100
            q = _("What is {}% of {}?", "Berapa {}% dari {}?").format(pct, num)
            return q, str(ans), ans
        elif kind == "of_rev":
            ans = random.choice([10, 20, 25, 30, 40, 50])
            num = random.choice([40, 60, 80, 100, 120, 200])
            pct = num * ans // 100
            q = _("{} is what percent of {}?", "{} berapa persen dari {}?").format(
                ans, num
            )
            return q, str(pct), pct
        else:
            old = random.choice([40, 50, 60, 80, 100, 120])
            new = old + random.choice([10, 15, 20, 25, 30])
            change = (new - old) * 100 // old
            q = _(
                "Change from {} to {} = ?% increase",
                "Perubahan dari {} ke {} = ?% kenaikan",
            ).format(old, new)
            return q, str(change), change

    elif playground == "number_theory":
        kind = random.choice(["mod", "digits", "factorial"])
        if kind == "mod":
            a = random.randint(10, 30)
            b = random.choice([3, 4, 5, 6, 7, 8, 9])
            ans = a % b
            q = f"{a} mod {b} = ?"
            return q, str(ans), ans
        elif kind == "digits":
            n = random.randint(100, 999)
            s = sum(int(d) for d in str(n))
            q = _("Sum of digits of {} = ?", "Jumlah digit dari {} = ?").format(n)
            return q, str(s), s
        else:
            n = random.choice([4, 5, 6, 7])
            ans = math.factorial(n)
            q = f"{n}! = ?"
            return q, str(ans), ans

    elif playground == "expressions":
        a = random.randint(2, 8)
        b = random.randint(1, 10)
        x = random.randint(1, 6)
        kind = random.choice(["linear", "quad"])
        if kind == "linear":
            ans = a * x + b
            q = _(
                "If x = {}, evaluate {}x + {}", "Jika x = {}, hitung {}x + {}"
            ).format(x, a, b)
            return q, str(ans), ans
        else:
            c = random.randint(1, 5)
            ans = a * x * x + b * x + c
            q = _(
                "If x = {}, evaluate {}x\u00b2 + {}x + {}",
                "Jika x = {}, hitung {}x\u00b2 + {}x + {}",
            ).format(x, a, b, c)
            return q, str(ans), ans

    elif playground == "equations":
        a = random.randint(2, 6)
        b = random.choice([3, 5, 7, 9, 11, 13])
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q = _("Solve: {}x + {} = {}", "Selesaikan: {}x + {} = {}").format(a, b, c)
        return q, str(ans), ans

    elif playground == "systems":
        pairs = [
            ((2, 3), (1, -1)),
            ((3, 5), (2, -3)),
            ((2, -1), (1, 2)),
            ((3, 2), (1, -1)),
            ((4, 1), (1, -2)),
        ]
        (a, b), (d, e) = random.choice(pairs)
        x = random.randint(2, 5)
        y = random.randint(1, 4)
        c1 = a * x + b * y
        c2 = d * x + e * y
        q_label = _("Solve:", "Selesaikan:")
        q_val = _("Enter x value", "Masukkan nilai x")
        q = f"{q_label}\n{a}x + {b}y = {c1}\n{d}x + {e}y = {c2}\n{q_val}"
        return q, str(x), x

    elif playground == "polynomials":
        kind = random.choice(["eval", "add"])
        if kind == "eval":
            a = random.randint(1, 5)
            b = random.randint(1, 6)
            x = random.randint(1, 4)
            ans = a * x + b
            q = _(
                "If P(x) = {}x + {}, find P({})", "Jika P(x) = {}x + {}, cari P({})"
            ).format(a, b, x)
            return q, str(ans), ans
        else:
            a, b = random.randint(1, 4), random.randint(1, 4)
            c, d = random.randint(1, 4), random.randint(1, 4)
            x = random.randint(1, 3)
            ans = (a + c) * x + (b + d)
            q = _(
                "({}x + {}) + ({}x + {}) at x={} = ?",
                "({}x + {}) + ({}x + {}) saat x={} = ?",
            ).format(a, b, c, d, x)
            return q, str(ans), ans

    elif playground == "factoring":
        pairs = [(2, 3), (3, 5), (2, 5), (3, 4), (2, 7), (3, 2), (4, 3), (5, 2)]
        a, b = random.choice(pairs)
        c = a * b
        d = a + b
        q = _(
            "One factor of x\u00b2 + {}x + {} is (x + {}). What is the other?",
            "Satu faktor dari x\u00b2 + {}x + {} adalah (x + {}). Berapa faktor lainnya?",
        ).format(d, c, a)
        return q, str(b), b

    elif playground == "quadratics":
        roots = [(2, 3), (3, 5), (2, 5), (1, 4), (3, 2), (4, 3), (2, 7), (3, 7)]
        r1, r2 = random.choice(roots)
        ans = r1 if random.randint(0, 1) else r2
        q = _(
            "Solve (x - {})(x - {}) = 0. Give one root.",
            "Selesaikan (x - {})(x - {}) = 0. Berikan satu akar.",
        ).format(r1, r2)
        return q, str(ans), ans

    elif playground == "functions":
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        x = random.randint(1, 6)
        ans = a * x + b
        q = _(
            "If f(x) = {}x + {}, find f({})", "Jika f(x) = {}x + {}, cari f({})"
        ).format(a, b, x)
        return q, str(ans), ans

    elif playground == "inequalities":
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q_label = _("Solve:", "Selesaikan:")
        q_hint = _(
            "Enter smallest integer solution.",
            "Masukkan solusi bilangan bulat terkecil.",
        )
        q = f"{q_label} {a}x + {b} > {c}. {q_hint}"
        return q, str(ans + 1), ans + 1

    elif playground == "exponents_logs":
        kind = random.choice(["exp", "log"])
        if kind == "exp":
            base = random.choice([2, 3, 4, 5])
            exp = random.choice([2, 3, 4])
            ans = base**exp
            q = _("Evaluate: {}^{} = ?", "Hitung: {}^{} = ?").format(base, exp)
            return q, str(ans), ans
        else:
            base = random.choice([2, 3, 4, 5])
            exp = random.choice([2, 3, 4])
            val = base**exp
            q = f"log_{base}({val}) = ?"
            ans = exp
            return q, str(ans), ans

    elif playground == "variables":
        kind = random.choice(
            ["identify_var", "identify_const", "identify_coeff", "count_terms"]
        )
        if kind == "identify_var":
            pairs = [
                ("3x + 5", "x"),
                ("2a \u2212 7", "a"),
                ("y\u00b2 + 4y", "y"),
                ("6p \u2212 3q + 2", "p, q"),
                ("m\u00b3 + 2m", "m"),
            ]
            expr, ans = random.choice(pairs)
            q = _("Variable(s) in '{}'?", "Variabel dalam '{}'?").format(expr)
            return q, ans, 0.0
        elif kind == "identify_const":
            pairs = [
                ("3x + 5", "5"),
                ("2a \u2212 7", "\u22127"),
                ("x + 10", "10"),
                ("4y \u2212 1", "\u22121"),
                ("8p + 3q \u2212 2", "\u22122"),
            ]
            expr, ans = random.choice(pairs)
            q = _("Constant in '{}'?", "Konstanta dalam '{}'?").format(expr)
            return q, ans, 0.0
        elif kind == "identify_coeff":
            pairs = [
                ("3x + 5", "3"),
                ("\u22122x + 7", "\u22122"),
                ("x\u00b2 + 4x", "1"),
                ("\u2212y + 3", "\u22121"),
                ("6a\u00b2 \u2212 a", "6"),
            ]
            expr, ans = random.choice(pairs)
            q = _(
                "Coefficient of variable in '{}'?", "Koefisien variabel dalam '{}'?"
            ).format(expr)
            return q, ans, 0.0
        else:
            pairs = [
                ("3x + 5", "2"),
                ("2a \u2212 7b + 1", "3"),
                ("x", "1"),
                ("4y \u2212 1", "2"),
                ("8p + 3q \u2212 2r + 5", "4"),
            ]
            expr, ans = random.choice(pairs)
            q = _("How many terms in '{}'?", "Berapa suku dalam '{}'?").format(expr)
            return q, ans, 0.0

    elif playground == "algebraic_forms":
        form_id = {
            "monomial": _("monomial", "monomial"),
            "binomial": _("binomial", "binomial"),
            "trinomial": _("trinomial", "trinomial"),
            "polynomial": _("polynomial", "polinomial"),
        }
        pairs = [
            ("5x", "monomial"),
            ("7a\u00b2", "monomial"),
            ("x + 3", "binomial"),
            ("2a \u2212 b", "binomial"),
            ("x\u00b2 + 2x + 1", "trinomial"),
            ("a\u00b2 \u2212 3a + 2", "trinomial"),
            ("x\u2074 + 2x\u00b3 \u2212 x + 7", "polynomial"),
            ("3a\u00b3 \u2212 2a\u00b2 + a \u2212 5", "polynomial"),
            ("8", "monomial"),
            ("2x \u2212 1", "binomial"),
        ]
        expr, ans_en = random.choice(pairs)
        q = _(
            "Classify: '{}' (monomial/binomial/trinomial/polynomial)?",
            "Klasifikasikan: '{}' (monomial/binomial/trinomial/polinomial)?",
        ).format(expr)
        return q, form_id[ans_en], 0.0

    elif playground == "algebraic_ops":
        kind = random.choice(["add_like", "sub_like", "distribute", "divide"])
        if kind == "add_like":
            pairs = [
                (3, 2, 5),
                (4, 1, 5),
                (7, 3, 10),
                (2, 6, 8),
                (5, 5, 10),
            ]
            a, b, ans = random.choice(pairs)
            q = _("Simplify: {}x + {}x = ?", "Sederhanakan: {}x + {}x = ?").format(a, b)
            return q, str(ans) + "x", ans
        elif kind == "sub_like":
            pairs = [
                (7, 3, 4),
                (9, 2, 7),
                (8, 5, 3),
                (6, 6, 0),
                (10, 4, 6),
            ]
            a, b, ans = random.choice(pairs)
            q = _(
                "Simplify: {}y \u2212 {}y = ?", "Sederhanakan: {}y \u2212 {}y = ?"
            ).format(a, b)
            return q, str(ans) + "y" if ans != 0 else "0", ans
        elif kind == "distribute":
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            ans_a = a * b
            ans_b = a * c
            q = _("Expand: {}({}x + {}) = ?", "Jabarkan: {}({}x + {}) = ?").format(
                a, b, c
            )
            return q, f"{ans_a}x + {ans_b}", 0.0
        else:
            pairs = [
                (6, 2, 3),
                (12, 3, 4),
                (15, 5, 3),
                (8, 4, 2),
                (10, 2, 5),
            ]
            a, b, ans = random.choice(pairs)
            q = _(
                "Simplify: ({}x\u00b2)/({}x) = ?", "Sederhanakan: ({}x\u00b2)/({}x) = ?"
            ).format(a, b)
            return q, str(ans) + "x", ans

    elif playground == "perfect_square":
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

    elif playground == "linear_equations":
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

    elif playground == "quadratic":
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

    elif playground == "functions":
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

    elif playground == "exponents_logs":
        sup_digits = {
            "0": "\u2070",
            "1": "\u00b9",
            "2": "\u00b2",
            "3": "\u00b3",
            "4": "\u2074",
        }
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

    return ("?", "0", 0.0)


def _build_quadratic_chart_lines(
    content_lines: list,
    a: int,
    b: int,
    c: int,
    inner_w: int,
    locale: str,
) -> None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    sign_b = "+" if b >= 0 else "\u2212"
    sign_c = "+" if c >= 0 else "\u2212"
    eq = f"y = {a}x\u00b2 {sign_b} {abs(b)}x {sign_c} {abs(c)}"
    content_lines.append((eq, "bold"))
    content_lines.append((None, None))

    D = b * b - 4 * a * c  # noqa: N806
    D_str = str(D) if D >= 0 else _("negative", "negatif")  # noqa: N806
    if b >= 0:
        formula = _(
            f"x = (\u2212{b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
            f"x = (\u2212{b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
        )
    else:
        formula = _(
            f"x = ({-b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
            f"x = ({-b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
        )
    content_lines.append((formula, None))

    if D >= 0:
        sqrt_d = math.sqrt(D)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        x1_str = f"{round(x1)}" if abs(x1 - round(x1)) < 0.001 else f"{x1:.2f}"
        x2_str = f"{round(x2)}" if abs(x2 - round(x2)) < 0.001 else f"{x2:.2f}"
        root_line = _(f"  x = {x1_str}, x = {x2_str}", f"  x = {x1_str}, x = {x2_str}")
        content_lines.append((root_line, None))
    content_lines.append((None, None))

    vx = -b / (2 * a)
    col_w = 2
    y_label_w = 5
    max_plot = inner_w - y_label_w - 4
    max_cols = max(max_plot // col_w, 9)
    n = min(max_cols, 15)
    n = n - 1 if n % 2 == 0 else n
    half = n // 2
    cx = round(vx)
    xs = [cx - half + i for i in range(n)]
    ys = [a * x * x + b * x + c for x in xs]
    y_vals = [*ys, 0]
    y_min = min(y_vals) - 1
    y_max = max(y_vals) + 1
    if abs(y_max - y_min) < 0.001:
        y_min -= 1
        y_max += 1
    y_range = y_max - y_min

    chart_h = 11

    def row_of_y(y: float) -> float:
        return (y_max - y) / y_range * (chart_h - 1)

    def y_of_row(r: float) -> float:
        return y_max - r / (chart_h - 1) * y_range

    zero_row = row_of_y(0)
    plot_w = n * col_w
    total_chart = y_label_w + 4 + plot_w
    left_pad = max(1, (inner_w - total_chart) // 2)

    border_top = (
        " " * left_pad + " " * y_label_w + " \u250c" + "\u2500" * plot_w + "\u2510"
    )
    content_lines.append((border_top, None))

    for row_idx in range(chart_h):
        y_val = y_of_row(row_idx)
        y_label = f"{y_val:>{y_label_w}.0f}"
        cells: list[str] = []
        for x_val in xs:
            y_curve = a * x_val * x_val + b * x_val + c
            cr = row_of_y(y_curve)
            on_curve = abs(row_idx - cr) < 0.55
            on_x_axis = abs(row_idx - zero_row) < 0.3
            if on_curve:
                cells.append("**")
            elif on_x_axis and x_val == 0:
                cells.append("\u253c\u253c")
            elif on_x_axis:
                cells.append("\u2500\u2500")
            elif x_val == 0:
                cells.append("\u2502\u2502")
            else:
                cells.append("  ")
        row_str = "".join(cells)
        row_line = " " * left_pad + y_label + " \u2502" + row_str + "\u2502"
        content_lines.append((row_line, None))

    border_bot = (
        " " * left_pad + " " * y_label_w + " \u2514" + "\u2500" * plot_w + "\u2518"
    )
    content_lines.append((border_bot, None))

    x_parts: list[str] = []
    for x in xs:
        s = str(x)
        if len(s) == 1:
            x_parts.append(" " + s)
        else:
            x_parts.append(s)
    x_label_line = " " * left_pad + " " * y_label_w + "  " + "".join(x_parts)
    content_lines.append((x_label_line, None))


def _build_linear_chart_lines(
    content_lines: list,
    m: int,
    b_val: int,
    inner_w: int,
    locale: str,
) -> None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    sign_b = "+" if b_val >= 0 else "\u2212"
    if b_val >= 0:
        eq = f"f(x) = {m}x {sign_b} {abs(b_val)}"
    else:
        eq = f"f(x) = {m}x {sign_b} {abs(b_val)}"
    content_lines.append((eq, "bold"))
    content_lines.append((None, None))

    half = 4
    xs = list(range(-half, half + 1))
    x_cols = len(xs)
    ys = [m * x + b_val for x in xs]
    y_vals = [*ys, 0]
    y_min = min(y_vals) - 1
    y_max = max(y_vals) + 1
    if abs(y_max - y_min) < 0.001:
        y_min -= 1
        y_max += 1
    y_range = y_max - y_min

    col_w = 2
    y_label_w = 5
    chart_h = 11
    plot_w = x_cols * col_w
    total_chart = y_label_w + 4 + plot_w
    left_pad = max(1, (inner_w - total_chart) // 2)

    def row_of_y(y: float) -> float:
        return (y_max - y) / y_range * (chart_h - 1)

    zero_row = row_of_y(0)

    border_top = (
        " " * left_pad + " " * y_label_w + " \u250c" + "\u2500" * plot_w + "\u2510"
    )
    content_lines.append((border_top, None))

    for row_idx in range(chart_h):
        y_val = y_max - row_idx * y_range / (chart_h - 1)
        y_label = f"{y_val:>{y_label_w}.0f}"
        cells: list[str] = []
        for x_val in xs:
            y_curve = m * x_val + b_val
            cr = row_of_y(y_curve)
            on_curve = abs(row_idx - cr) < 0.55
            on_x_axis = abs(row_idx - zero_row) < 0.3
            if on_curve:
                cells.append("**")
            elif on_x_axis and x_val == 0:
                cells.append("\u253c\u253c")
            elif on_x_axis:
                cells.append("\u2500\u2500")
            elif x_val == 0:
                cells.append("\u2502\u2502")
            else:
                cells.append("  ")
        row_str = "".join(cells)
        row_line = " " * left_pad + y_label + " \u2502" + row_str + "\u2502"
        content_lines.append((row_line, None))

    border_bot = (
        " " * left_pad + " " * y_label_w + " \u2514" + "\u2500" * plot_w + "\u2518"
    )
    content_lines.append((border_bot, None))

    x_parts: list[str] = []
    for x in xs:
        s = str(x)
        if len(s) == 1:
            x_parts.append(" " + s)
        else:
            x_parts.append(s)
    x_label_line = " " * left_pad + " " * y_label_w + "  " + "".join(x_parts)
    content_lines.append((x_label_line, None))


def _build_identity_chart_lines(
    content_lines: list,
    playground: str,
    a: int,
    b: int,
    inner_w: int,
    locale: str,
) -> None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    a2, b2 = a * a, b * b
    ab = a * b

    # Proportional cell widths — compact but visibly different
    side_label_w = 3
    max_cells = 30  # max total of cw + rw
    avail = min(inner_w - 3 - side_label_w, max_cells)
    cw = max(4, avail * a // (a + b))
    rw = max(4, avail - cw)
    if cw + rw > avail:
        if a >= b:
            cw = avail - rw
        else:
            rw = avail - cw
        cw = max(4, cw)
        rw = max(4, rw)
        if cw + rw > avail:
            cw = rw = avail // 2

    body_w = cw + rw + 3
    total_w = body_w + side_label_w
    chart_pad = max(0, (inner_w - total_w) // 2)
    side = " " * chart_pad
    sp = " " * side_label_w

    shade_a2_l = "\u2593" * cw  # ▓
    shade_ab_l = "\u2591" * cw  # ░
    shade_ab_r = "\u2591" * rw
    shade_b2_r = "\u2592" * rw  # ▒

    content_lines.append((None, None))
    if playground == "perfect_square":
        content_lines.append(
            (_("(a+b)² = a² + 2ab + b²", "(a+b)² = a² + 2ab + b²"), "bold")
        )
        total = a2 + 2 * ab + b2
        side_len = a + b

        content_lines.append((_(f"  a={a}, b={b}", f"  a={a}, b={b}"), None))
        content_lines.append((None, None))

        # Column headers above box
        top_label = side + sp + f"a={a}".center(cw + 1) + f"b={b}".center(rw + 2)
        content_lines.append((top_label, "dim"))
        top = side + sp + "\u250c" + "\u2500" * cw + "\u252c" + "\u2500" * rw + "\u2510"
        content_lines.append((top, None))
        r1 = (
            side
            + "a".center(side_label_w)
            + "\u2502"
            + shade_a2_l
            + "\u2502"
            + shade_ab_r
            + "\u2502"
        )
        content_lines.append((r1, None))
        mid = side + sp + "\u251c" + "\u2500" * cw + "\u253c" + "\u2500" * rw + "\u2524"
        content_lines.append((mid, None))
        r2 = (
            side
            + "b".center(side_label_w)
            + "\u2502"
            + shade_ab_l
            + "\u2502"
            + shade_b2_r
            + "\u2502"
        )
        content_lines.append((r2, None))
        bot = side + sp + "\u2514" + "\u2500" * cw + "\u2534" + "\u2500" * rw + "\u2518"
        content_lines.append((bot, None))
        content_lines.append((None, None))

        # Legend with values
        content_lines.append(
            (
                f"a² = a\u00d7a = {a}\u00d7{a} = {a2}  |  ab = a\u00d7b = {a}\u00d7{b} = {ab}",
                None,
            )
        )
        content_lines.append(
            (
                f"b² = b\u00d7b = {b}\u00d7{b} = {b2}  |  2ab = 2\u00d7{ab} = {2 * ab}",
                None,
            )
        )
        content_lines.append((None, None))
        content_lines.append(
            (
                _(
                    f"({a}+{b})² = {side_len}² = {total}",
                    f"({a}+{b})² = {side_len}² = {total}",
                ),
                "bold",
            )
        )
        content_lines.append((f"{a2} + {ab} + {ab} + {b2} = {total} \u2713", None))
    else:
        content_lines.append(
            (_("a² − b² = (a−b)(a+b)", "a² − b² = (a−b)(a+b)"), "bold")
        )
        total = a2 - b2

        content_lines.append((_(f"  a={a}, b={b}", f"  a={a}, b={b}"), None))
        content_lines.append((None, None))

        top = side + sp + "\u250c" + "\u2500" * cw + "\u252c" + "\u2500" * rw + "\u2510"
        content_lines.append((top, None))
        r1 = (
            side
            + "a".center(side_label_w)
            + "\u2502"
            + shade_a2_l
            + "\u2502"
            + shade_b2_r
            + "\u2502"
        )
        content_lines.append((r1, None))
        bot = side + sp + "\u2514" + "\u2500" * cw + "\u2534" + "\u2500" * rw + "\u2518"
        content_lines.append((bot, None))
        content_lines.append((None, None))

        diff_a = a - b
        sum_a = a + b
        content_lines.append(
            (_(f"a² = {a}\u00d7{a} = {a2}", f"a² = {a}\u00d7{a} = {a2}"), None)
        )
        content_lines.append(
            (_(f"b² = {b}\u00d7{b} = {b2}", f"b² = {b}\u00d7{b} = {b2}"), None)
        )
        content_lines.append((None, None))
        content_lines.append(
            (
                _(
                    f"a² − b² = {a2} − {b2} = {total}",
                    f"a² − b² = {a2} − {b2} = {total}",
                ),
                None,
            )
        )
        content_lines.append(
            (
                _(
                    f"= ({a}−{b})({a}+{b}) = {diff_a}\u00b7{sum_a} = {total}",
                    f"= ({a}−{b})({a}+{b}) = {diff_a}\u00b7{sum_a} = {total}",
                ),
                "bold",
            )
        )


def _build_playground_content(
    content_lines: list[tuple[str | None, str | None]],
    tw: int,
    locale: str,
    question: str,
    *,
    title: str = "",
    correct: int = 0,
    total: int = 0,
    feedback: tuple[str, str, bool] | None = None,
) -> None:
    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content_lines.append((" " * left_pad + b, "bold"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))
        content_lines.append((None, None))

    content_lines.append(("Playground", "bold"))
    content_lines.append((None, None))

    pad = max(2, tw // 20)
    inner_w = tw - 2 * pad - 2
    title_str = f"  {title}"
    score_str = (
        f"Score: {correct}/{total} correct"
        if locale == "en"
        else f"Nilai: {correct}/{total} benar"
    )
    gap = inner_w - len(title_str) - len(score_str)
    line = title_str + " " * gap + score_str if gap >= 4 else title_str
    content_lines.append((line, None))
    content_lines.append((None, None))

    if feedback:
        user_answer, correct_answer, is_correct = feedback
        content_lines.append(("Question:" if locale == "en" else "Soal:", "bold"))
        content_lines.append((question, None))
        content_lines.append((None, None))
        content_lines.append(
            (
                f"Your answer: {user_answer}"
                if locale == "en"
                else f"Jawabanmu: {user_answer}",
                None,
            )
        )
        content_lines.append(
            (
                f"Correct answer: {correct_answer}"
                if locale == "en"
                else f"Jawaban benar: {correct_answer}",
                "dim",
            )
        )
        content_lines.append((None, None))
        result_word = (
            ("CORRECT!" if is_correct else "WRONG")
            if locale == "en"
            else ("BENAR!" if is_correct else "SALAH")
        )
        hint = (
            "Press Enter for next question"
            if locale == "en"
            else "Tekan Enter untuk soal berikutnya"
        )
        spaces = max(0, inner_w - len(result_word) - len(hint))
        content_lines.append((result_word + " " * spaces + hint, "bold"))
    else:
        content_lines.append(("Question:" if locale == "en" else "Soal:", "bold"))
        content_lines.append((question, None))
        content_lines.append((None, None))
        content_lines.append((">> ", None))
        content_lines.append((None, None))


def _read_value_chalkboard(fd: int, tw: int, label: str) -> str | None:
    old = termios.tcgetattr(fd)
    buf = ""
    pad = max(2, tw // 20)
    black_bg = "\x1b[48;2;0;0;0m"
    green_bg = "\x1b[48;2;26;58;26m"
    white_fg = "\x1b[38;2;255;255;255m"
    display = f"  {label}= "
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()
    try:
        tty.setraw(fd)
        while True:
            ch = os.read(fd, 1)
            if ch in (b"\n", b"\r"):
                sys.stdout.write("\r\n" + "\x1b[0m")
                sys.stdout.flush()
                return buf
            elif ch == b"\x1b":
                r, _, _ = select.select([fd], [], [], 0.1)
                if r:
                    os.read(fd, 2)
                    continue
                return None
            elif ch == b"\t":
                return "\r"
            elif ch == b"\x7f":
                buf = buf[:-1]
            else:
                try:
                    buf += ch.decode()
                except UnicodeDecodeError:
                    continue
            inner = tw - 2 * pad - 2
            line = display + buf
            gap = max(0, inner - len(line))
            sys.stdout.write(
                "\r"
                + black_bg
                + " " * tw
                + "\r"
                + black_bg
                + " " * pad
                + green_bg
                + white_fg
                + "\u2502"
                + line
                + " " * gap
                + "\u2502"
                + black_bg
                + " " * pad
                + f"\x1b[{pad + 2 + len(line)}G"
            )
            sys.stdout.flush()
    finally:
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _playground_identity(
    console: Console, playground: str, locale: str, title: str = ""
) -> int | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    # Exploration phase — let user input values and see the chart
    while True:
        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        # Build exploration content with prompt markers
        expl_lines: list[tuple[str | None, str | None]] = []
        if tw >= BANNER_WIDTH:
            left_pad = max(0, (tw - BANNER_WIDTH) // 2)
            for b_line in BANNER:
                expl_lines.append((" " * left_pad + b_line, "bold"))
            expl_lines.append((None, None))
            sub = "For minds losing their edge"
            sub_pad = max(0, (tw - len(sub)) // 2)
            expl_lines.append((" " * sub_pad + sub, "italic"))
            expl_lines.append((None, None))
            expl_lines.append((None, None))
        expl_lines.append(("Playground", "bold"))
        expl_lines.append((None, None))
        fmt = (
            _("(a+b)² = a² + 2ab + b²", "(a+b)² = a² + 2ab + b²")
            if playground == "perfect_square"
            else _("a² − b² = (a−b)(a+b)", "a² − b² = (a−b)(a+b)")
        )
        expl_lines.append((fmt, "bold"))
        expl_lines.append((None, None))
        prompt = _(
            "Enter values (empty = random):",
            "Masukkan nilai (kosong = acak):",
        )
        expl_lines.append((prompt, None))
        expl_lines.append((None, None))
        expl_lines.append(("  a = ", None))
        expl_lines.append((None, None))
        expl_lines.append(("  b = ", None))
        expl_lines.append((None, None))

        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        # Read a inside the chalkboard box
        fd = sys.stdin.fileno()
        a_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("a =")
        )
        target_a = 5 + a_idx
        if th - target_a > 0:
            sys.stdout.write(f"\x1b[{th - target_a}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        a_str = _read_value_chalkboard(fd, tw, "a")
        if a_str is None:
            return None
        if a_str == "\r":
            return 0
        if not a_str.strip():
            a = random.randint(3, 9)
        else:
            try:
                a = max(2, min(20, int(a_str.strip())))
            except ValueError:
                a = random.randint(3, 9)

        # Re-render to show "a = value", then read b
        expl_lines[a_idx] = (f"  a = {a}", None)
        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        b_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("b =")
        )
        target_b = 5 + b_idx
        if th - target_b > 0:
            sys.stdout.write(f"\x1b[{th - target_b}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        b_str = _read_value_chalkboard(fd, tw, "b")
        if b_str is None:
            return None
        if b_str == "\r":
            return 0
        if not b_str.strip():
            if playground == "diff_squares":
                b = random.randint(1, a - 1) if a > 1 else 1
            else:
                b = random.randint(1, 5)
        else:
            try:
                b_val = int(b_str.strip())
                if playground == "diff_squares":
                    b = max(1, min(a - 1, b_val)) if a > 1 else 1
                else:
                    b = max(1, min(10, b_val))
            except ValueError:
                if playground == "diff_squares":
                    b = max(1, a - 1) if a > 1 else 1
                else:
                    b = random.randint(1, 5)

        # Re-render with chart
        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        chart_lines: list[tuple[str | None, str | None]] = []
        if tw >= BANNER_WIDTH:
            left_pad = max(0, (tw - BANNER_WIDTH) // 2)
            for b_line in BANNER:
                chart_lines.append((" " * left_pad + b_line, "bold"))
            chart_lines.append((None, None))
            sub = "For minds losing their edge"
            sub_pad = max(0, (tw - len(sub)) // 2)
            chart_lines.append((" " * sub_pad + sub, "italic"))
            chart_lines.append((None, None))
            chart_lines.append((None, None))
        chart_lines.append(("Playground", "bold"))
        chart_lines.append((None, None))
        _build_identity_chart_lines(chart_lines, playground, a, b, inner_w, locale)
        chart_lines.append((None, None))
        cont = _(
            "Press Enter for quiz",
            "Tekan Enter untuk kuis",
        )
        chart_lines.append((cont, "italic"))
        _render_content(
            console,
            tw,
            th,
            chart_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        k = _read_key()
        if k == "enter":
            break
        elif k == "tab":
            return 0
        elif k in ("esc", "q"):
            return None

    # Quiz phase
    correct = 0
    total = 0
    while True:
        if playground == "perfect_square":
            a = random.randint(2, 9)
            b = random.randint(1, 5)
            a2, b2, ab2 = a * a, b * b, 2 * a * b
            total_val = a2 + ab2 + b2
            question = _(f"({a}+{b})² = ?", f"({a}+{b})² = ?")
            answer_str = str(total_val)
        else:
            a = random.randint(3, 9)
            b = random.randint(1, a - 1)
            a2, b2 = a * a, b * b
            total_val = a2 - b2
            question = _(f"{a}² − {b}² = ?", f"{a}² − {b}² = ?")
            answer_str = str(total_val)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        content_lines: list[tuple[str | None, str | None]] = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd2 = sys.stdin.fileno()
        prompt_idx = next(i for i, (t, _) in enumerate(content_lines) if t == ">> ")
        target_line = 5 + prompt_idx
        lines_up = th - target_line
        if lines_up > 0:
            sys.stdout.write(f"\x1b[{lines_up}A\x1b[{pad + 5}G")
            sys.stdout.flush()

        result = _read_input_at_cursor(fd2, tw)
        if result is None:
            return None
        if result == "\r":
            return 0

        total += 1
        is_correct = result.strip() == answer_str
        if is_correct:
            correct += 1

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        content_lines = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
            feedback=(result, answer_str, is_correct),
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        while True:
            k = _read_key()
            if k == "enter":
                break
            elif k == "tab":
                return 0
            elif k in ("esc", "q"):
                return None


def _playground_quadratic(console: Console, locale: str, title: str = "") -> int | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    # Exploration phase
    while True:
        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        expl_lines: list[tuple[str | None, str | None]] = []
        if tw >= BANNER_WIDTH:
            left_pad = max(0, (tw - BANNER_WIDTH) // 2)
            for b_line in BANNER:
                expl_lines.append((" " * left_pad + b_line, "bold"))
            expl_lines.append((None, None))
            sub = "For minds losing their edge"
            sub_pad = max(0, (tw - len(sub)) // 2)
            expl_lines.append((" " * sub_pad + sub, "italic"))
            expl_lines.append((None, None))
            expl_lines.append((None, None))
        expl_lines.append(("Playground", "bold"))
        expl_lines.append((None, None))
        expl_lines.append(
            (
                _(
                    "ax\u00b2 + bx + c = 0 \u2014 enter values (empty = random):",
                    "ax\u00b2 + bx + c = 0 \u2014 masukkan nilai (kosong = acak):",
                ),
                None,
            )
        )
        expl_lines.append((None, None))
        expl_lines.append(("  a = ", None))
        expl_lines.append((None, None))
        expl_lines.append(("  b = ", None))
        expl_lines.append((None, None))
        expl_lines.append(("  c = ", None))

        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd = sys.stdin.fileno()
        a_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("a =")
        )
        target = 5 + a_idx
        if th - target > 0:
            sys.stdout.write(f"\x1b[{th - target}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        a_str = _read_value_chalkboard(fd, tw, "a")
        if a_str is None:
            return None
        if a_str == "\r":
            return 0
        if not a_str.strip():
            a_val = random.randint(1, 3)
            a_str = str(a_val)
        else:
            try:
                a_val = max(1, min(10, int(a_str.strip())))
                a_str = str(a_val)
            except ValueError:
                a_val = random.randint(1, 3)
                a_str = str(a_val)

        expl_lines[a_idx] = (f"  a = {a_str}", None)
        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        b_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("b =")
        )
        target = 5 + b_idx
        if th - target > 0:
            sys.stdout.write(f"\x1b[{th - target}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        b_str = _read_value_chalkboard(fd, tw, "b")
        if b_str is None:
            return None
        if b_str == "\r":
            return 0
        if not b_str.strip():
            b_val = random.randint(-8, 8)
            b_str = str(b_val)
        else:
            try:
                b_val = max(-10, min(10, int(b_str.strip())))
                b_str = str(b_val)
            except ValueError:
                b_val = random.randint(-8, 8)
                b_str = str(b_val)
        expl_lines[b_idx] = (f"  b = {b_str}", None)
        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        c_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("c =")
        )
        target = 5 + c_idx
        if th - target > 0:
            sys.stdout.write(f"\x1b[{th - target}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        c_str = _read_value_chalkboard(fd, tw, "c")
        if c_str is None:
            return None
        if c_str == "\r":
            return 0
        if not c_str.strip():
            c_val = random.randint(-8, 8)
            c_str = str(c_val)
        else:
            try:
                c_val = max(-10, min(10, int(c_str.strip())))
                c_str = str(c_val)
            except ValueError:
                c_val = random.randint(-8, 8)
                c_str = str(c_val)
        expl_lines[c_idx] = (f"  c = {c_str}", None)

        a = int(a_str)
        b = int(b_str)
        c = int(c_str)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        chart_lines: list[tuple[str | None, str | None]] = []
        if tw >= BANNER_WIDTH:
            left_pad = max(0, (tw - BANNER_WIDTH) // 2)
            for b_line in BANNER:
                chart_lines.append((" " * left_pad + b_line, "bold"))
            chart_lines.append((None, None))
            sub = "For minds losing their edge"
            sub_pad = max(0, (tw - len(sub)) // 2)
            chart_lines.append((" " * sub_pad + sub, "italic"))
            chart_lines.append((None, None))
            chart_lines.append((None, None))
        chart_lines.append(("Playground", "bold"))
        chart_lines.append((None, None))
        _build_quadratic_chart_lines(chart_lines, a, b, c, inner_w, locale)
        chart_lines.append((None, None))
        cont = _("Press Enter for quiz", "Tekan Enter untuk kuis")
        chart_lines.append((cont, "italic"))
        _render_content(
            console,
            tw,
            th,
            chart_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        k = _read_key()
        if k == "enter":
            break
        elif k == "tab":
            return 0
        elif k in ("esc", "q"):
            return None

    # Quiz phase
    correct = 0
    total = 0
    while True:
        x1 = random.randint(-5, 5)
        x2 = random.randint(-5, 5)
        a = random.randint(1, 3)
        b = -a * (x1 + x2)
        c = a * x1 * x2
        if b >= 0:
            question = _(
                "Solve: {}x\u00b2 + {}x + {} = 0",
                "Selesaikan: {}x\u00b2 + {}x + {} = 0",
            ).format(a, b, c)
        else:
            question = _(
                "Solve: {}x\u00b2 \u2212 {}x + {} = 0",
                "Selesaikan: {}x\u00b2 \u2212 {}x + {} = 0",
            ).format(a, abs(b), c)

        ask_x1 = bool(random.randint(0, 1))
        answer_str = str(x1) if ask_x1 else str(x2)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines: list[tuple[str | None, str | None]] = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd2 = sys.stdin.fileno()
        pad_local = max(2, tw // 20)
        prompt_idx = next(i for i, (t, _) in enumerate(content_lines) if t == ">> ")
        target_line = 5 + prompt_idx
        lines_up = th - target_line
        if lines_up > 0:
            sys.stdout.write(f"\x1b[{lines_up}A\x1b[{pad_local + 5}G")
            sys.stdout.flush()

        result = _read_input_at_cursor(fd2, tw)
        if result is None:
            return None
        if result == "\r":
            return 0

        total += 1
        is_correct = result.strip() == answer_str
        if is_correct:
            correct += 1

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
            feedback=(result, answer_str, is_correct),
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        while True:
            k = _read_key()
            if k == "enter":
                break
            elif k == "tab":
                return 0
            elif k in ("esc", "q"):
                return None


def _playground_functions(console: Console, locale: str, title: str = "") -> int | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    while True:
        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        expl_lines: list[tuple[str | None, str | None]] = []
        if tw >= BANNER_WIDTH:
            left_pad = max(0, (tw - BANNER_WIDTH) // 2)
            for b_line in BANNER:
                expl_lines.append((" " * left_pad + b_line, "bold"))
            expl_lines.append((None, None))
            sub = "For minds losing their edge"
            sub_pad = max(0, (tw - len(sub)) // 2)
            expl_lines.append((" " * sub_pad + sub, "italic"))
            expl_lines.append((None, None))
            expl_lines.append((None, None))
        expl_lines.append(("Playground", "bold"))
        expl_lines.append((None, None))
        expl_lines.append(
            (
                _(
                    "f(x) = mx + b \u2014 enter m and b (empty = random):",
                    "f(x) = mx + b \u2014 masukkan m dan b (kosong = acak):",
                ),
                None,
            )
        )
        expl_lines.append((None, None))
        expl_lines.append(("  m = ", None))
        expl_lines.append((None, None))
        expl_lines.append(("  b = ", None))

        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd = sys.stdin.fileno()
        m_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("m =")
        )
        target = 5 + m_idx
        if th - target > 0:
            sys.stdout.write(f"\x1b[{th - target}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        m_str = _read_value_chalkboard(fd, tw, "m")
        if m_str is None:
            return None
        if m_str == "\r":
            return 0
        if not m_str.strip():
            m_val = random.choice([-3, -2, -1, 1, 2, 3])
            m_str = str(m_val)
        else:
            try:
                m_val = max(-5, min(5, int(m_str.strip())))
                if m_val == 0:
                    m_val = 1
                m_str = str(m_val)
            except ValueError:
                m_val = random.choice([-3, -2, -1, 1, 2, 3])
                m_str = str(m_val)
        expl_lines[m_idx] = (f"  m = {m_str}", None)
        _render_content(
            console,
            tw,
            th,
            expl_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        b_idx = next(
            i
            for i, (t, _) in enumerate(expl_lines)
            if t is not None and t.strip().startswith("b =")
        )
        target = 5 + b_idx
        if th - target > 0:
            sys.stdout.write(f"\x1b[{th - target}A\x1b[{pad + 7}G")
            sys.stdout.flush()
        b_str = _read_value_chalkboard(fd, tw, "b")
        if b_str is None:
            return None
        if b_str == "\r":
            return 0
        if not b_str.strip():
            b_val = random.randint(-5, 5)
            b_str = str(b_val)
        else:
            try:
                b_val = max(-10, min(10, int(b_str.strip())))
                b_str = str(b_val)
            except ValueError:
                b_val = random.randint(-5, 5)
                b_str = str(b_val)
        expl_lines[b_idx] = (f"  b = {b_str}", None)

        m = int(m_str)
        b = int(b_str)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines
        pad = max(2, tw // 20)
        inner_w = tw - 2 * pad - 2

        chart_lines: list[tuple[str | None, str | None]] = []
        if tw >= BANNER_WIDTH:
            left_pad = max(0, (tw - BANNER_WIDTH) // 2)
            for b_line in BANNER:
                chart_lines.append((" " * left_pad + b_line, "bold"))
            chart_lines.append((None, None))
            sub = "For minds losing their edge"
            sub_pad = max(0, (tw - len(sub)) // 2)
            chart_lines.append((" " * sub_pad + sub, "italic"))
            chart_lines.append((None, None))
            chart_lines.append((None, None))
        chart_lines.append(("Playground", "bold"))
        chart_lines.append((None, None))
        _build_linear_chart_lines(chart_lines, m, b, inner_w, locale)
        chart_lines.append((None, None))
        cont = _("Press Enter for quiz", "Tekan Enter untuk kuis")
        chart_lines.append((cont, "italic"))
        _render_content(
            console,
            tw,
            th,
            chart_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        k = _read_key()
        if k == "enter":
            break
        elif k == "tab":
            return 0
        elif k in ("esc", "q"):
            return None

    correct = 0
    total = 0
    while True:
        m = random.randint(-3, 3)
        if m == 0:
            m = 1
        b_val = random.randint(-5, 5)
        x = random.randint(-5, 5)
        result = m * x + b_val
        if b_val >= 0:
            question = _(
                "f(x) = {}x + {}, find f({})",
                "f(x) = {}x + {}, tentukan f({})",
            ).format(m, b_val, x)
        else:
            question = _(
                "f(x) = {}x \u2212 {}, find f({})",
                "f(x) = {}x \u2212 {}, tentukan f({})",
            ).format(m, abs(b_val), x)
        answer_str = str(result)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines: list[tuple[str | None, str | None]] = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd2 = sys.stdin.fileno()
        pad_local = max(2, tw // 20)
        prompt_idx = next(i for i, (t, _) in enumerate(content_lines) if t == ">> ")
        target_line = 5 + prompt_idx
        lines_up = th - target_line
        if lines_up > 0:
            sys.stdout.write(f"\x1b[{lines_up}A\x1b[{pad_local + 5}G")
            sys.stdout.flush()

        result_input = _read_input_at_cursor(fd2, tw)
        if result_input is None:
            return None
        if result_input == "\r":
            return 0

        total += 1
        is_correct = result_input.strip() == answer_str
        if is_correct:
            correct += 1

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
            feedback=(result_input, answer_str, is_correct),
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        while True:
            k = _read_key()
            if k == "enter":
                break
            elif k == "tab":
                return 0
            elif k in ("esc", "q"):
                return None


def _playground_exponents_logs(
    console: Console, locale: str, title: str = ""
) -> int | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    sup_digits = {
        "0": "\u2070",
        "1": "\u00b9",
        "2": "\u00b2",
        "3": "\u00b3",
        "4": "\u2074",
    }
    sub_map = str.maketrans(
        "0123456789", "\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089"
    )

    correct = 0
    total = 0
    while True:
        kind = random.randint(0, 1)
        if kind == 0:
            base = random.randint(2, 5)
            exp = random.randint(2, 4)
            result_val = base**exp
            exp_sup = "".join(sup_digits[d] for d in str(exp))
            question = _(
                "Evaluate: {}{} = ?",
                "Hitung: {}{} = ?",
            ).format(base, exp_sup)
            answer_str = str(result_val)
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
            result_val = round(math.log(val, base))
            answer_str = str(result_val)
            if base == 10:
                question = _(
                    "Evaluate: log\u2081\u2080({}) = ?",
                    "Hitung: log\u2081\u2080({}) = ?",
                ).format(val)
            else:
                base_sub = str(base).translate(sub_map)
                question = _(
                    "Evaluate: log{}({}) = ?",
                    "Hitung: log{}({}) = ?",
                ).format(base_sub, val)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines: list[tuple[str | None, str | None]] = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd2 = sys.stdin.fileno()
        pad_local = max(2, tw // 20)
        prompt_idx = next(i for i, (t, _) in enumerate(content_lines) if t == ">> ")
        target_line = 5 + prompt_idx
        lines_up = th - target_line
        if lines_up > 0:
            sys.stdout.write(f"\x1b[{lines_up}A\x1b[{pad_local + 5}G")
            sys.stdout.flush()

        result = _read_input_at_cursor(fd2, tw)
        if result is None:
            return None
        if result == "\r":
            return 0

        total += 1
        is_correct = result.strip() == answer_str
        if is_correct:
            correct += 1

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
            feedback=(result, answer_str, is_correct),
        )

        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        while True:
            k = _read_key()
            if k == "enter":
                break
            elif k == "tab":
                return 0
            elif k in ("esc", "q"):
                return None


def _playground(
    console: Console, playground: str, locale: str, title: str = ""
) -> int | None:
    if playground in ("perfect_square", "diff_squares"):
        return _playground_identity(console, playground, locale, title)
    if playground == "quadratic":
        return _playground_quadratic(console, locale, title)
    if playground == "functions":
        return _playground_functions(console, locale, title)
    if playground == "exponents_logs":
        return _playground_exponents_logs(console, locale, title)

    correct = 0
    total = 0
    while True:
        question, answer_str, _ = _gen_question(playground, locale)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines: list[tuple[str | None, str | None]] = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
        )
        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        fd2 = sys.stdin.fileno()
        prompt_idx = next(i for i, (t, _) in enumerate(content_lines) if t == ">> ")
        target_line = 5 + prompt_idx
        lines_up = th - target_line
        pad = max(2, tw // 20)
        if lines_up > 0:
            sys.stdout.write(f"\x1b[{lines_up}A\x1b[{pad + 5}G")
            sys.stdout.flush()

        result = _read_input_at_cursor(fd2, tw)
        if result is None:
            return None
        if result == "\r":
            return 0

        total += 1
        is_correct = result.strip() == answer_str
        if is_correct:
            correct += 1

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines = []
        _build_playground_content(
            content_lines,
            tw,
            locale,
            question,
            title=title,
            correct=correct,
            total=total,
            feedback=(result, answer_str, is_correct),
        )
        _render_content(
            console,
            tw,
            th,
            content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=9 if tw >= BANNER_WIDTH else 0,
        )

        while True:
            k = _read_key()
            if k == "enter":
                break
            elif k == "tab":
                return 0
            elif k in ("esc", "q"):
                return None


def run_topic_screen(
    console: Console,
    concept_id: str,
    locale: str = "en",
) -> str | None:
    global _LOCALE
    _LOCALE = locale

    content = get_content(concept_id)
    if content is None or not content.subtopics:
        return None

    current = 0
    detail_subtopic: SubTopic | None = None

    while True:
        if detail_subtopic is not None:
            _render_detail(console, detail_subtopic, locale, concept_id)
            key = _read_key()
            if key == "enter" and detail_subtopic.playground:
                sub_title = detail_subtopic.title.get(
                    locale, detail_subtopic.title.get("en", "")
                )
                if (
                    _playground(
                        console, detail_subtopic.playground, locale, title=sub_title
                    )
                    is None
                ):
                    return None
                detail_subtopic = None
            elif key == "tab":
                detail_subtopic = None
            elif key in ("esc", "q"):
                return None
        else:
            _render_list(console, content.subtopics, current, locale, concept_id)
            key = _read_key()
            if key == "up":
                current = (current - 1) % len(content.subtopics)
            elif key == "down":
                current = (current + 1) % len(content.subtopics)
            elif key == "enter":
                detail_subtopic = content.subtopics[current]
            elif key == "tab":
                return "back"
            elif key in ("esc", "q"):
                return None


def _render_list(
    console: Console,
    subtopics: list[SubTopic],
    current: int,
    locale: str,
    concept_id: str = "arithmetic",
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    content_lines: list[tuple[str | None, str | None]] = []

    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content_lines.append((" " * left_pad + b, "bold"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))
        content_lines.append((None, None))

    concept_name = {
        "aritmatika": "Aritmatika",
        "arithmetic": "Arithmetic",
        "aljabar": "Aljabar",
        "algebra": "Algebra",
    }.get(concept_id, concept_id.replace("-", " ").title())
    content_lines.append((concept_name, "bold"))
    content_lines.append((None, None))

    for i, st in enumerate(subtopics):
        prefix = "> " if i == current else "  "
        style = "reverse" if i == current else None
        content_lines.append(
            (f"{prefix}{st.title.get(locale, st.title.get('en', ''))}", style)
        )

    selected = subtopics[current]
    content_lines.append((None, None))
    content_lines.append(("\u2500" * min(tw, 60), "dim"))
    content_lines.append((None, None))

    pad = max(2, tw // 20)
    inner_w = tw - 2 * pad - 2

    preview: list[tuple[str | None, str | None]] = []

    expl = selected.description.get(locale, selected.description.get("en", ""))
    for line in expl.split("\n"):
        if len(line) > inner_w:
            for chunk in [line[i : i + inner_w] for i in range(0, len(line), inner_w)]:
                preview.append((chunk, None))
        else:
            preview.append((line, None))

    preview_height = 8
    if len(preview) > preview_height:
        preview = preview[:preview_height]
    elif len(preview) < preview_height:
        preview += [(None, None)] * (preview_height - len(preview))

    content_lines += preview

    _render_content(
        console,
        tw,
        th,
        content_lines,
        "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
        chalkboard=True,
        header_count=9 if tw >= BANNER_WIDTH else 0,
    )


def _render_detail(
    console: Console,
    subtopic: SubTopic,
    locale: str,
    concept_id: str = "arithmetic",
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    content_lines: list[tuple[str | None, str | None]] = []

    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content_lines.append((" " * left_pad + b, "bold"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))
        content_lines.append((None, None))

    concept_name = {
        "aritmatika": "Aritmatika",
        "arithmetic": "Arithmetic",
        "aljabar": "Aljabar",
        "algebra": "Algebra",
    }.get(concept_id, concept_id.replace("-", " ").title())
    content_lines.append((concept_name, "bold"))
    content_lines.append((None, None))

    content_lines.append(
        (subtopic.title.get(locale, subtopic.title.get("en", "")), "bold")
    )
    content_lines.append((None, None))

    expl = subtopic.explanation.get(locale, subtopic.explanation.get("en", ""))
    expl_lines = [ln.strip() for ln in expl.split("\n") if ln.strip()]

    content_lines.append(("Examples" if locale == "en" else "Contoh", "bold"))
    content_lines.append((None, None))
    ex_list = subtopic.examples.get(locale, subtopic.examples.get("en", []))
    expl_idx = 0
    pad = max(2, tw // 20)
    inner_w = tw - 2 * pad - 2
    for ex in ex_list:
        if ex == "":
            content_lines.append((None, None))
        else:
            if len(ex) > inner_w:
                for chunk in [ex[i : i + inner_w] for i in range(0, len(ex), inner_w)]:
                    content_lines.append((chunk, "dim"))
            else:
                content_lines.append((ex, "dim"))
            if expl_idx < len(expl_lines):
                el = expl_lines[expl_idx]
                if len(el) > inner_w:
                    for chunk in [
                        el[i : i + inner_w] for i in range(0, len(el), inner_w)
                    ]:
                        content_lines.append((chunk, "italic"))
                else:
                    content_lines.append((el, "italic"))
                expl_idx += 1

    if subtopic.playground:
        content_lines.append((None, None))
        content_lines.append(("Playground" if locale == "en" else "Latihan", "bold"))
        content_lines.append((None, None))
        content_lines.append(
            (
                "Press Enter to start playground"
                if locale == "en"
                else "Tekan Enter untuk memulai latihan",
                "italic",
            )
        )

    keybar = "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit"
    _render_content(
        console,
        tw,
        th,
        content_lines,
        keybar,
        chalkboard=True,
        header_count=9 if tw >= BANNER_WIDTH else 0,
    )


def _render_content(
    console: Console,
    tw: int,
    th: int,
    content: list[tuple[str | None, str | None]],
    keybar_line: str,
    *,
    chalkboard: bool = False,
    header_count: int = 8,
) -> None:
    sys.stdout.write("\x1b[H")
    top_pad = 3
    max_content = max(1, th - 1 - top_pad)

    if len(content) > max_content:
        trimmed: list[tuple[str | None, str | None]] = []
        for i, (txt, sty) in enumerate(content):
            is_blank = txt is None
            next_is_none = i + 1 >= len(content)
            if is_blank and not next_is_none and i >= header_count:
                continue
            trimmed.append((txt, sty))
        content = trimmed
        if len(content) > max_content:
            content = content[:header_count] + [
                (x, y) for x, y in content[header_count:] if y != "italic"
            ]
        if len(content) > max_content:
            content = content[:header_count] + [
                (x, y) for x, y in content[header_count:] if y != "dim"
            ]
        if len(content) > max_content:
            content = content[:max_content]

    bg_black = "on #000000"
    fg_green = "white on #1a3a1a"
    pad = max(2, tw // 20)

    for _ in range(min(top_pad, th - 1)):
        console.print(" " * tw, style=bg_black)

    if chalkboard:
        hc = min(header_count, len(content))
        for text, style in content[:hc]:
            if text is None:
                console.print(" " * tw, style=bg_black)
            elif style == "reverse":
                rt = Text(text, style="reverse")
                rt.append(" " * (tw - len(text)), style=bg_black)
                console.print(rt)
            else:
                combined = f"{style} {bg_black}" if style else bg_black
                console.print(text.ljust(tw), style=combined)

        console.print(" " * pad, style=bg_black, end="")
        console.print("┌" + "─" * (tw - 2 * pad - 2) + "┐", style=fg_green, end="")
        console.print(" " * pad, style=bg_black)

        for text, style in content[hc:]:
            if text is None:
                console.print(" " * pad, style=bg_black, end="")
                console.print(
                    "│" + " " * (tw - 2 * pad - 2) + "│", style=fg_green, end=""
                )
                console.print(" " * pad, style=bg_black)
            elif style == "reverse":
                console.print(" " * pad, style=bg_black, end="")
                console.print("│", style=fg_green, end="")
                rt = Text(text.ljust(tw - 2 * pad - 2), style="reverse")
                console.print(rt, end="")
                console.print("│", style=fg_green, end="")
                console.print(" " * pad, style=bg_black)
            else:
                combined = f"{style} on #1a3a1a" if style else fg_green
                console.print(" " * pad, style=bg_black, end="")
                console.print("│", style=fg_green, end="")
                console.print(text.ljust(tw - 2 * pad - 2), style=combined, end="")
                console.print("│", style=fg_green, end="")
                console.print(" " * pad, style=bg_black)

        console.print(" " * pad, style=bg_black, end="")
        console.print("└" + "─" * (tw - 2 * pad - 2) + "┘", style=fg_green, end="")
        console.print(" " * pad, style=bg_black)

        used = top_pad + len(content) + 2
        for _ in range(max(0, th - 1 - used)):
            console.print(" " * tw, style=bg_black)
    else:
        for text, style in content:
            if text is None:
                console.print(" " * tw)
            elif style == "reverse":
                rt = Text(text, style="reverse")
                rt.append(" " * (tw - len(text)))
                console.print(rt)
            else:
                console.print(text.ljust(tw), style=style)

        used = top_pad + len(content)
        for _ in range(max(0, th - 1 - used)):
            console.print(" " * tw)

    credit = "\u24b8 D. Daud Yusup"
    gap = tw - len(keybar_line) - len(credit) - 1
    if gap >= 0:
        keybar_line = keybar_line + " " * gap + credit
    console.print(keybar_line.ljust(tw), style=bg_black, end="")
