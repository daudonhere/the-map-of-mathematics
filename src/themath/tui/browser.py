from __future__ import annotations

import os
import select
import shutil
import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from themath.core.models import MathConcept
from themath.core.service import MapService
from themath.tui.launcher import BANNER


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


def _run_browser(console: Console, service: MapService) -> str | None:
    concepts = service.list_concepts()
    if not concepts:
        return None

    current = 0
    detail_concept: MathConcept | None = None
    detail_current = 0

    while True:
        if detail_concept is not None:
            _render_detail(console, service, detail_concept, detail_current)
            key = _read_key()
            if key == "up":
                related = _get_related_concepts(service, detail_concept)
                if related:
                    detail_current = (detail_current - 1) % len(related)
            elif key == "down":
                related = _get_related_concepts(service, detail_concept)
                if related:
                    detail_current = (detail_current + 1) % len(related)
            elif key == "enter":
                related = _get_related_concepts(service, detail_concept)
                if related:
                    detail_concept = related[detail_current]
                    detail_current = 0
            elif key in ("esc", "tab", "q"):
                detail_concept = None
                detail_current = 0
        else:
            _render_list(console, concepts, current)
            key = _read_key()
            if key == "up":
                current = (current - 1) % len(concepts)
            elif key == "down":
                current = (current + 1) % len(concepts)
            elif key == "enter":
                detail_concept = concepts[current]
                detail_current = 0
            elif key == "tab":
                return "back"
            elif key in ("esc", "q"):
                return None


def _get_related_concepts(
    service: MapService, concept: MathConcept
) -> list[MathConcept]:
    return [
        c
        for rid in concept.related_concepts
        if (c := service.get_concept(rid))
    ]


def _render_list(
    console: Console,
    concepts: list[MathConcept],
    current: int,
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    sys.stdout.write("\x1b[H")

    content: list[tuple[str | None, str | None]] = []

    if tw >= 65:
        for b in BANNER:
            content.append((b, "bold cyan"))
        content.append((None, None))
        indent = max(0, int(tw * 0.1))
        content.append((" " * indent + "Learning Weapon For You", "italic"))
        content.append((None, None))

    for i, c in enumerate(concepts):
        prefix = "> " if i == current else "  "
        content.append((f"{prefix}{c.name}", "reverse" if i == current else None))

    _render_content(console, tw, th, content, "\u2191 Up   \u2193 Down   \u21b5 Select   \u21b9 Back   Esc Exit")


def _render_detail(
    console: Console,
    service: MapService,
    concept: MathConcept,
    current: int,
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    sys.stdout.write("\x1b[H")

    content: list[tuple[str | None, str | None]] = []

    content.append((concept.name, "bold cyan"))
    content.append((concept.category, "dim"))
    content.append((concept.description, None))
    content.append((None, None))

    related = _get_related_concepts(service, concept)
    if related:
        content.append((service._("related_concepts"), "bold"))
        for i, rc in enumerate(related):
            prefix = "> " if i == current else "  "
            content.append((f"{prefix}{rc.name}", "reverse" if i == current else None))

    _render_content(console, tw, th, content, "\u2191 Up   \u2193 Down   \u21b5 Select   \u21b9 Back   Esc Exit")


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


def run_browser(service: MapService) -> str | None:
    if not sys.stdin.isatty():
        return None

    console = Console()

    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

    try:
        return _run_browser(console, service)
    except (EOFError, KeyboardInterrupt):
        return None
    finally:
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.write("\x1b[?25h")
        sys.stdout.flush()
