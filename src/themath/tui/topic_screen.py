from __future__ import annotations

import os
import select
import shutil
import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from themath.core.content import SubTopic, get_content


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


def run_topic_screen(
    console: Console,
    concept_id: str,
) -> str | None:
    content = get_content(concept_id)
    if content is None or not content.subtopics:
        return None

    current = 0
    detail_subtopic: SubTopic | None = None

    while True:
        if detail_subtopic is not None:
            _render_detail(console, detail_subtopic)
            key = _read_key()
            if key in ("esc", "tab", "q"):
                detail_subtopic = None
        else:
            _render_list(console, content.subtopics, current)
            key = _read_key()
            if key == "up":
                current = (current - 1) % len(content.subtopics)
            elif key == "down":
                current = (current + 1) % len(content.subtopics)
            elif key == "enter":
                detail_subtopic = content.subtopics[current]
            elif key in ("esc", "tab", "q"):
                return "back"


def _render_list(
    console: Console,
    subtopics: list[SubTopic],
    current: int,
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    sys.stdout.write("\x1b[H")

    content_lines: list[tuple[str | None, str | None]] = []

    content_lines.append(("Arithmetic", "bold cyan"))
    content_lines.append((None, None))

    for i, st in enumerate(subtopics):
        prefix = "> " if i == current else "  "
        style = "reverse" if i == current else None
        content_lines.append((f"{prefix}{st.title}", style))

    selected = subtopics[current]
    content_lines.append((None, None))
    separator = "\u2500" * min(tw, 60)
    content_lines.append((separator, "dim"))
    content_lines.append((None, None))

    for line in selected.explanation.split("\n"):
        content_lines.append((line, None))
    content_lines.append((None, None))
    for ex in selected.examples:
        if ex == "":
            content_lines.append((None, None))
        else:
            content_lines.append((ex, "dim"))
    if selected.playground:
        content_lines.append((None, None))
        content_lines.append(("Press Enter to open playground", "italic yellow"))

    _render_content(console, tw, th, content_lines, "\u2191 Up   \u2193 Down   \u21b5 Detail   \u21b9 Back   Esc Exit")


def _render_detail(
    console: Console,
    subtopic: SubTopic,
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    sys.stdout.write("\x1b[H")

    content_lines: list[tuple[str | None, str | None]] = []

    content_lines.append((subtopic.title, "bold cyan"))
    content_lines.append((None, None))

    for line in subtopic.explanation.split("\n"):
        content_lines.append((line, None))
    content_lines.append((None, None))

    content_lines.append(("Examples", "bold"))
    content_lines.append((None, None))
    for ex in subtopic.examples:
        if ex == "":
            content_lines.append((None, None))
        else:
            content_lines.append((ex, "dim"))

    if subtopic.playground:
        content_lines.append((None, None))
        content_lines.append(("Playground", "bold"))
        content_lines.append((None, None))
        content_lines.append(("Press Enter to start playground", "italic yellow"))

    _render_content(console, tw, th, content_lines, "\u21b9 Back   Esc Exit")


def _render_content(
    console: Console,
    tw: int,
    th: int,
    content: list[tuple[str | None, str | None]],
    keybar_line: str,
) -> None:
    top_pad = 3
    max_content = th - 1 - top_pad

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

    for _ in range(min(top_pad, th - 1)):
        console.print(" " * tw)

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

    console.print(keybar_line.ljust(tw), end="")
