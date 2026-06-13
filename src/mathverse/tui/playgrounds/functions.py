from __future__ import annotations

import random
import shutil
import sys

from rich.console import Console

from mathverse.tui.components.chalkboard import (
    _build_playground_content,
    _render_content,
)
from mathverse.tui.components.charts import _build_linear_chart_lines
from mathverse.tui.components.input import (
    _read_input_at_cursor,
    _read_key,
    _read_value_chalkboard,
)
from mathverse.tui.launcher import BANNER, BANNER_WIDTH


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
