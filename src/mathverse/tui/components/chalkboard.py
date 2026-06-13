from __future__ import annotations

import sys

from rich.console import Console
from rich.text import Text

from mathverse.tui.launcher import BANNER, BANNER_WIDTH


def _wrap_text(text: str, width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        while len(paragraph) > width:
            lines.append(paragraph[:width])
            paragraph = paragraph[width:]
        lines.append(paragraph)
    return lines


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
    fg_chalk = "white on #111111"
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
                console.print(text.ljust(tw), style=combined, markup=False)

        console.print(" " * pad, style=bg_black, end="")
        console.print("┌" + "─" * (tw - 2 * pad - 2) + "┐", style=fg_chalk, end="")
        console.print(" " * pad, style=bg_black)

        for text, style in content[hc:]:
            if text is None:
                console.print(" " * pad, style=bg_black, end="")
                console.print(
                    "│" + " " * (tw - 2 * pad - 2) + "│", style=fg_chalk, end=""
                )
                console.print(" " * pad, style=bg_black)
            elif style == "reverse":
                console.print(" " * pad, style=bg_black, end="")
                console.print("│", style=fg_chalk, end="")
                rt = Text(text.ljust(tw - 2 * pad - 2), style="reverse")
                console.print(rt, end="")
                console.print("│", style=fg_chalk, end="")
                console.print(" " * pad, style=bg_black)
            else:
                combined = f"{style} on #111111" if style else fg_chalk
                inner_w = tw - 2 * pad - 2
                for segment in _wrap_text(text, inner_w):
                    console.print(" " * pad, style=bg_black, end="")
                    console.print("│", style=fg_chalk, end="")
                    console.print(segment.ljust(inner_w), style=combined, end="", markup=False)
                    console.print("│", style=fg_chalk, end="")
                    console.print(" " * pad, style=bg_black)

        console.print(" " * pad, style=bg_black, end="")
        console.print("└" + "─" * (tw - 2 * pad - 2) + "┘", style=fg_chalk, end="")
        console.print(" " * pad, style=bg_black)

        inner_w = tw - 2 * pad - 2
        visual_lines = top_pad
        for i, (txt, sty) in enumerate(content):
            if i < hc or txt is None or sty == "reverse":
                visual_lines += 1
            else:
                visual_lines += len(_wrap_text(txt, inner_w))
        used = visual_lines + 2
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
                console.print(text.ljust(tw), style=style, markup=False)

        used = top_pad + len(content)
        for _ in range(max(0, th - 1 - used)):
            console.print(" " * tw)

    credit = "\u24b8 D. Daud Yusup"
    gap = tw - len(keybar_line) - len(credit) - 1
    if gap >= 0:
        keybar_line = keybar_line + " " * gap + credit
    console.print(keybar_line.ljust(tw), style=bg_black, end="")


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
        for qline in question.split("\n"):
            content_lines.append((qline, None))
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
        for qline in question.split("\n"):
            content_lines.append((qline, None))
        content_lines.append((None, None))
        content_lines.append((">> ", None))
        content_lines.append((None, None))
