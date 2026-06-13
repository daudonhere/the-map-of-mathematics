from __future__ import annotations

import os
import select
import shutil
import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from mathverse.core.content import get_content
from mathverse.core.models import MathConcept
from mathverse.core.service import MapService
from mathverse.tui.launcher import BANNER, BANNER_WIDTH
from mathverse.tui.topic_screen import run_topic_screen


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
            elif key == "tab":
                detail_concept = None
                detail_current = 0
            elif key in ("esc", "q"):
                return None
        else:
            _render_list(console, concepts, current)
            key = _read_key()
            if key == "up":
                current = (current - 1) % len(concepts)
            elif key == "down":
                current = (current + 1) % len(concepts)
            elif key == "enter":
                concept = concepts[current]
                if get_content(concept.id) is not None:
                    result = run_topic_screen(console, concept.id, service.locale)
                    if result == "back":
                        continue
                    return None
                detail_concept = concept
                detail_current = 0
            elif key == "tab":
                return "back"
            elif key in ("esc", "q"):
                return None


def _get_related_concepts(
    service: MapService, concept: MathConcept
) -> list[MathConcept]:
    return [c for rid in concept.related_concepts if (c := service.get_concept(rid))]


def _render_list(
    console: Console,
    concepts: list[MathConcept],
    current: int,
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    content: list[tuple[str | None, str | None]] = []

    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content.append((" " * left_pad + b, "bold cyan"))
        content.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content.append((" " * sub_left_pad + subtitle, "italic"))
        content.append((None, None))

    for i, c in enumerate(concepts):
        prefix = "> " if i == current else "  "
        content.append((f"{prefix}{c.name}", "reverse" if i == current else None))

    header_count = 8 if tw >= BANNER_WIDTH else 0
    _render_content(
        console,
        tw,
        th,
        content,
        "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
        chalkboard=True,
        header_count=header_count,
    )


def _render_detail(
    console: Console,
    service: MapService,
    concept: MathConcept,
    current: int,
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

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

    _render_content(
        console,
        tw,
        th,
        content,
        "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
        chalkboard=True,
        header_count=0,
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
                console.print("│" + " " * (tw - 2 * pad - 2) + "│", style=fg_green, end="")
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
