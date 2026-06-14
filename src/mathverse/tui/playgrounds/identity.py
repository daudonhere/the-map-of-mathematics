from __future__ import annotations

import random
import shutil
import sys

from rich.console import Console

from mathverse.tui.components.chalkboard import (
    _build_playground_content,
    _render_content,
)
from mathverse.tui.components.charts import _build_identity_chart_lines
from mathverse.tui.components.input import (
    _read_input_at_cursor,
    _read_key,
    _read_value_chalkboard,
)
from mathverse.tui.launcher import BANNER, BANNER_WIDTH


def _playground_identity(
    console: Console, playground: str, locale: str, title: str = ""
) -> int | None:
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
        fmt = (
            _(
                "(a+b)\u00b2 = a\u00b2 + 2ab + b\u00b2",
                "(a+b)\u00b2 = a\u00b2 + 2ab + b\u00b2",
            )
            if playground == "perfect_square"
            else _(
                "a\u00b2 \u2212 b\u00b2 = (a\u2212b)(a+b)",
                "a\u00b2 \u2212 b\u00b2 = (a\u2212b)(a+b)",
            )
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

    correct = 0
    total = 0
    while True:
        if playground == "perfect_square":
            a = random.randint(2, 9)
            b = random.randint(1, 5)
            a2, b2, ab2 = a * a, b * b, 2 * a * b
            total_val = a2 + ab2 + b2
            question = _(f"({a}+{b})\u00b2 = ?", f"({a}+{b})\u00b2 = ?")
            answer_str = str(total_val)
        else:
            a = random.randint(3, 9)
            b = random.randint(1, a - 1)
            a2, b2 = a * a, b * b
            total_val = a2 - b2
            question = _(
                f"{a}\u00b2 \u2212 {b}\u00b2 = ?", f"{a}\u00b2 \u2212 {b}\u00b2 = ?"
            )
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
