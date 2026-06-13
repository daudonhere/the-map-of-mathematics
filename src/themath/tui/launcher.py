from __future__ import annotations

import os
import select
import shutil
import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from themath.core.i18n import t

BANNER = [
    "████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ████████╗██╗  ██╗",
    "╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║",
    "   ██║   ███████║█████╗      ██╔████╔██║███████║   ██║   ███████║",
    "   ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║",
    "   ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║",
    "   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝",
]


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


def _keybar() -> str:
    return "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit"


def _render(
    console: Console,
    items: list[str],
    current: int,
    locale: str,
    *,
    lang_menu: bool = False,
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

    if lang_menu:
        content.append((t("select_language", locale), "bold"))
        content.append((None, None))

    for i, item in enumerate(items):
        prefix = "> " if i == current else "  "
        content.append((f"{prefix}{item}", "reverse" if i == current else None))

    top_pad = 3
    keybar_line = _keybar()
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


def run_launcher(locale: str = "en") -> tuple[str, str] | None:
    if not sys.stdin.isatty():
        return ("terminal", locale)

    console = Console()

    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

    items = [
        t("terminal_mode", locale),
        t("desktop_mode", locale),
        t("select_language", locale),
    ]
    current = 0
    in_lang_menu = False
    lang_current = 0

    try:
        while True:
            if in_lang_menu:
                langs = [
                    label for label, _ in [("English", "en"), ("Indonesia", "id")]
                ]
                _render(console, langs, lang_current, locale, lang_menu=True)
                key = _read_key()
                if key == "up":
                    lang_current = (lang_current - 1) % 2
                elif key == "down":
                    lang_current = (lang_current + 1) % 2
                elif key == "enter":
                    locale = "en" if lang_current == 0 else "id"
                    items = [
                        t("terminal_mode", locale),
                        t("desktop_mode", locale),
                        t("select_language", locale),
                    ]
                    in_lang_menu = False
                elif key in ("esc", "tab", "q"):
                    in_lang_menu = False
            else:
                _render(console, items, current, locale)
                key = _read_key()
                if key == "up":
                    current = (current - 1) % len(items)
                elif key == "down":
                    current = (current + 1) % len(items)
                elif key == "enter":
                    if current == 0:
                        return ("terminal", locale)
                    elif current == 1:
                        return ("gui", locale)
                    elif current == 2:
                        in_lang_menu = True
                        lang_current = 0
                elif key in ("esc", "tab", "q"):
                    return None
    except (EOFError, KeyboardInterrupt):
        return None
    except Exception:
        return ("terminal", locale)
    finally:
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.write("\x1b[?25h")
        sys.stdout.flush()
