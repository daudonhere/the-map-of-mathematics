from __future__ import annotations

import random
import shutil
import sys

from rich.console import Console

from mathverse.tui.components.chalkboard import (
    _build_playground_content,
    _render_content,
)
from mathverse.tui.components.charts import _build_quadratic_chart_lines
from mathverse.tui.components.input import (
    _read_input_at_cursor,
    _read_key,
    _read_value_chalkboard,
)
from mathverse.tui.launcher import BANNER, BANNER_WIDTH


def _playground_quadratic(console: Console, locale: str, title: str = "") -> int | None:
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
