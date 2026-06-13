from __future__ import annotations

import shutil
import sys

from rich.console import Console

from mathverse.core.quiz import gen_question
from mathverse.tui.components.chalkboard import (
    _build_playground_content,
    _render_content,
)
from mathverse.tui.components.input import _read_input_at_cursor, _read_key
from mathverse.tui.launcher import BANNER_WIDTH
from mathverse.tui.playgrounds.exponents_logs import _playground_exponents_logs
from mathverse.tui.playgrounds.functions import _playground_functions
from mathverse.tui.playgrounds.identity import _playground_identity
from mathverse.tui.playgrounds.quadratic import _playground_quadratic


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
        question, answer_str, _ = gen_question(playground, locale)

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
