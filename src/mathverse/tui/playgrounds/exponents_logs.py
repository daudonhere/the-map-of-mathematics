from __future__ import annotations

import math
import random
import shutil
import sys

from rich.console import Console

from mathverse.tui.components.chalkboard import (
    _build_playground_content,
    _render_content,
)
from mathverse.tui.components.input import _read_input_at_cursor, _read_key
from mathverse.tui.launcher import BANNER_WIDTH


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
