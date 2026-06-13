from __future__ import annotations

import math
import os
import random
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
            sys.stdout.write("\r" + " " * tw + "\r" + ">> " + buf)
            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _gen_question(playground: str) -> tuple[str, str, float]:
    """Generate a (question_text, answer_str, numeric_answer) tuple."""
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
        choice = random.choice(props)
        if choice[0] in ("commutative",):
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            q = f"Property shown: {a} + {b} = {b} + {a}"
            return q, choice[0], 0.0
        elif choice[0] == "associative":
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            c = random.randint(2, 8)
            q = f"Property shown: ({a} + {b}) + {c} = {a} + ({b} + {c})"
            return q, choice[0], 0.0
        elif choice[0] == "distributive":
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)
            q = f"Property shown: {a} \u00d7 ({b} + {c}) = {a}\u00d7{b} + {a}\u00d7{c}"
            return q, choice[0], 0.0

    elif playground == "number_types":
        kind = random.choice(["prime", "square", "even", "odd"])
        if kind == "prime":
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
            compos = [4, 6, 8, 9, 10, 12, 14, 15, 16]
            ans = "prime"
            n = random.choice(primes)
            distract = random.choice(compos)
            if random.randint(0, 1):
                q = f"Is {n} prime or composite?"
                return q, ans, 0.0
            else:
                q = f"Is {distract} prime or composite?"
                return q, "composite", 0.0
        elif kind == "square":
            sq = random.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
            q = f"Which number squared equals {sq}?"
            ans = int(sq**0.5)
            return q, str(ans), ans
        elif kind == "even":
            n = random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
            q = f"Is {n} even or odd?"
            return q, "even", 0.0
        elif kind == "odd":
            n = random.choice([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
            q = f"Is {n} even or odd?"
            return q, "odd", 0.0

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
        if kind == "gcf":
            a, b = random.choice(pairs)
            ans = math.gcd(a, b)
            q = f"GCF of {a} and {b} = ?"
            return q, str(ans), ans
        else:
            a, b = random.choice(pairs)
            ans = a * b // math.gcd(a, b)
            q = f"LCM of {a} and {b} = ?"
            return q, str(ans), ans

    elif playground == "ratios":
        kind = random.choice(["simplify", "find_part"])
        if kind == "simplify":
            pairs = [(6, 8), (10, 15), (12, 18), (8, 12), (14, 21), (9, 12)]
            a, b = random.choice(pairs)
            g = math.gcd(a, b)
            q = f"Simplify ratio {a}:{b} = ?"
            ans = f"1:{b // g}" if g == a else f"{a // g}:{b // g}"
            return q, ans, 0.0
        else:
            a, b = random.choice([(2, 3), (3, 5), (4, 7), (5, 8), (1, 4), (3, 7)])
            total = random.choice([30, 40, 50, 60, 70, 80])
            if (a + b) > total:
                total = (a + b) * random.randint(2, 5)
            part_b = total // (a + b) * b
            q = f"Ratio {a}:{b}, total {total}. Value of larger part = ?"
            return q, str(part_b), part_b

    elif playground == "percentages":
        kind = random.choice(["of", "of_rev", "change"])
        if kind == "of":
            pct = random.choice([10, 20, 25, 30, 40, 50, 60, 75])
            num = random.choice([40, 60, 80, 100, 120, 200, 300])
            ans = num * pct // 100
            q = f"What is {pct}% of {num}?"
            return q, str(ans), ans
        elif kind == "of_rev":
            ans = random.choice([10, 20, 25, 30, 40, 50])
            num = random.choice([40, 60, 80, 100, 120, 200])
            pct = num * ans // 100
            q = f"{ans} is what percent of {num}?"
            return q, str(pct), pct
        else:
            old = random.choice([40, 50, 60, 80, 100, 120])
            new = old + random.choice([10, 15, 20, 25, 30])
            change = (new - old) * 100 // old
            q = f"Change from {old} to {new} = ?% increase"
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
            q = f"Sum of digits of {n} = ?"
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
            q = f"If x = {x}, evaluate {a}x + {b}"
            return q, str(ans), ans
        else:
            c = random.randint(1, 5)
            ans = a * x * x + b * x + c
            q = f"If x = {x}, evaluate {a}x\u00b2 + {b}x + {c}"
            return q, str(ans), ans

    elif playground == "equations":
        a = random.randint(2, 6)
        b = random.choice([3, 5, 7, 9, 11, 13])
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q = f"Solve: {a}x + {b} = {c}"
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
        q = f"Solve:\n{a}x + {b}y = {c1}\n{d}x + {e}y = {c2}\nEnter x value"
        return q, str(x), x

    elif playground == "polynomials":
        kind = random.choice(["eval", "add"])
        if kind == "eval":
            a = random.randint(1, 5)
            b = random.randint(1, 6)
            x = random.randint(1, 4)
            ans = a * x + b
            q = f"If P(x) = {a}x + {b}, find P({x})"
            return q, str(ans), ans
        else:
            a, b = random.randint(1, 4), random.randint(1, 4)
            c, d = random.randint(1, 4), random.randint(1, 4)
            x = random.randint(1, 3)
            ans = (a + c) * x + (b + d)
            q = f"({a}x + {b}) + ({c}x + {d}) at x={x} = ?"
            return q, str(ans), ans

    elif playground == "factoring":
        pairs = [(2, 3), (3, 5), (2, 5), (3, 4), (2, 7), (3, 2), (4, 3), (5, 2)]
        a, b = random.choice(pairs)
        c = a * b
        d = a + b
        q = f"One factor of x\u00b2 + {d}x + {c} is (x + {a}). What is the other?"
        return q, str(b), b

    elif playground == "quadratics":
        roots = [(2, 3), (3, 5), (2, 5), (1, 4), (3, 2), (4, 3), (2, 7), (3, 7)]
        r1, r2 = random.choice(roots)
        ans = r1 if random.randint(0, 1) else r2
        q = f"Solve (x - {r1})(x - {r2}) = 0. Give one root."
        return q, str(ans), ans

    elif playground == "functions":
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        x = random.randint(1, 6)
        ans = a * x + b
        q = f"If f(x) = {a}x + {b}, find f({x})"
        return q, str(ans), ans

    elif playground == "inequalities":
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q = f"Solve: {a}x + {b} > {c}. Enter smallest integer solution."
        return q, str(ans + 1), ans + 1

    elif playground == "exponents_logs":
        kind = random.choice(["exp", "log"])
        if kind == "exp":
            base = random.choice([2, 3, 4, 5])
            exp = random.choice([2, 3, 4])
            ans = base**exp
            q = f"Evaluate: {base}^{exp} = ?"
            return q, str(ans), ans
        else:
            base = random.choice([2, 3, 4, 5])
            exp = random.choice([2, 3, 4])
            val = base**exp
            q = f"log_{base}({val}) = ?"
            ans = exp
            return q, str(ans), ans

    return ("?", "0", 0.0)


def _build_playground_content(
    content_lines: list[tuple[str | None, str | None]],
    tw: int,
    locale: str,
    question: str,
    correct: int,
    total: int,
    *,
    title: str = "",
    feedback: tuple[str, str, bool] | None = None,
) -> None:
    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content_lines.append((" " * left_pad + b, "bold cyan"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))

    content_lines.append(("Playground", "bold cyan"))

    score_str = (
        f"Score: {correct}/{total} correct"
        if locale == "en"
        else f"Nilai: {correct}/{total} benar"
    )
    title_str = f"  {title}"
    line = title_str + " " * (tw - len(title_str) - len(score_str)) + score_str
    content_lines.append((None, None))
    content_lines.append((line, None))

    content_lines.append((None, None))

    if feedback:
        user_answer, correct_answer, is_correct = feedback
        content_lines.append(
            ("Question:" if locale == "en" else "Soal:", "bold yellow")
        )
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
        content_lines.append(
            (
                ("CORRECT!" if is_correct else "WRONG")
                if locale == "en"
                else ("BENAR!" if is_correct else "SALAH"),
                "bold green" if is_correct else "bold red",
            )
        )
    else:
        content_lines.append(
            ("Question:" if locale == "en" else "Soal:", "bold yellow")
        )
        content_lines.append((question, None))
        content_lines.append((None, None))
        content_lines.append((">> ", None))
        content_lines.append((None, None))


def _playground(console: Console, playground: str, locale: str, title: str = "") -> int | None:
    correct = 0
    total = 0
    while True:
        question, answer_str, _ = _gen_question(playground)

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines: list[tuple[str | None, str | None]] = []
        _build_playground_content(
            content_lines, tw, locale, question, correct, total, title=title,
        )
        _render_content(
            console, tw, th, content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=8 if tw >= BANNER_WIDTH else 0,
        )

        fd2 = sys.stdin.fileno()
        prompt_idx = next(
            i for i, (t, _) in enumerate(content_lines) if t == ">> "
        )
        target_line = 3 + prompt_idx
        lines_up = th - 1 - target_line
        if lines_up > 0:
            sys.stdout.write(f"\x1b[{lines_up}A\x1b[4G")
            sys.stdout.flush()

        result = _read_input_at_cursor(fd2, tw)
        if result is None:
            return None

        total += 1
        is_correct = result.strip() == answer_str
        if is_correct:
            correct += 1

        tw = shutil.get_terminal_size().columns
        th = shutil.get_terminal_size().lines

        content_lines = []
        _build_playground_content(
            content_lines, tw, locale, question, correct, total,
            title=title, feedback=(result, answer_str, is_correct),
        )
        _render_content(
            console, tw, th, content_lines,
            "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
            chalkboard=True,
            header_count=8 if tw >= BANNER_WIDTH else 0,
        )

        while True:
            k = _read_key()
            if k == "enter":
                break
            elif k in ("esc", "tab", "q"):
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
                sub_title = detail_subtopic.title.get(locale, detail_subtopic.title.get("en", ""))
                if _playground(console, detail_subtopic.playground, locale, title=sub_title) is None:
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
            content_lines.append((" " * left_pad + b, "bold cyan"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))

    concept_name = {
        "aritmatika": "Aritmatika",
        "arithmetic": "Arithmetic",
        "aljabar": "Aljabar",
        "algebra": "Algebra",
    }.get(concept_id, concept_id.replace("-", " ").title())
    content_lines.append((concept_name, "bold cyan"))
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

    preview: list[tuple[str | None, str | None]] = []

    expl = selected.description.get(locale, selected.description.get("en", ""))
    for line in expl.split("\n"):
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
        header_count=8 if tw >= BANNER_WIDTH else 0,
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
            content_lines.append((" " * left_pad + b, "bold cyan"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))

    concept_name = {
        "aritmatika": "Aritmatika",
        "arithmetic": "Arithmetic",
        "aljabar": "Aljabar",
        "algebra": "Algebra",
    }.get(concept_id, concept_id.replace("-", " ").title())
    content_lines.append((concept_name, "bold cyan"))
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
    for ex in ex_list:
        if ex == "":
            content_lines.append((None, None))
        else:
            content_lines.append((ex, "dim"))
            if expl_idx < len(expl_lines):
                content_lines.append((expl_lines[expl_idx], "italic"))
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
                "italic yellow",
            )
        )

    keybar = "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit"
    _render_content(
        console, tw, th, content_lines, keybar,
        chalkboard=True,
        header_count=8 if tw >= BANNER_WIDTH else 0,
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
    sys.stdout.write("\x1b[2J\x1b[H")
    top_pad = 3
    max_content = max(1, th - 1 - top_pad)

    if len(content) > max_content:
        trimmed: list[tuple[str | None, str | None]] = []
        for i, (txt, sty) in enumerate(content):
            is_blank = txt is None
            next_is_none = i + 1 >= len(content)
            if is_blank and not next_is_none:
                continue
            trimmed.append((txt, sty))
        content = trimmed
        if len(content) > max_content:
            content = [(x, y) for x, y in content if y != "italic"]
        if len(content) > max_content:
            content = [(x, y) for x, y in content if y != "dim"]
        if len(content) > max_content:
            content = [(x, y) for x, y in content if y != "bold"]
        if len(content) > max_content:
            content = [(x, y) for x, y in content if y != "bold cyan"]

    bg_black = "on #000000"
    bg_green = "on #1a3a1a"
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

        border = " " * pad + "\u2500" * (tw - 2 * pad) + " " * pad
        console.print(border, style=fg_green)

        for text, style in content[hc:]:
            if text is None:
                console.print(" " * tw, style=bg_green)
            elif style == "reverse":
                padded = text.ljust(tw - 2 * pad)
                rt = Text(" " * pad, style=bg_green)
                rt.append(padded, style="reverse")
                rt.append(" " * pad, style=bg_green)
                console.print(rt)
            else:
                padded = " " * pad + text.ljust(tw - 2 * pad) + " " * pad
                combined = f"{style} on #1a3a1a" if style else fg_green
                console.print(padded.ljust(tw), style=combined)

        console.print(border, style=fg_green)

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
