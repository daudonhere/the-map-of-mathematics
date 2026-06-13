from __future__ import annotations

import os
import select
import shutil
import sys
import termios
import tty

from rich.console import Console
from rich.text import Text

from mathverse.core.i18n import t

BANNER = [
    "███╗   ███╗ █████╗ ████████╗██╗  ██╗██╗   ██╗███████╗██████╗ ███████╗███████╗",
    "████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝",
    "██╔████╔██║███████║   ██║   ███████║██║   ██║█████╗  ██████╔╝███████╗█████╗  ",
    "██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  ",
    "██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║ ╚████╔╝ ███████╗██║  ██║███████║███████╗",
    "╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝",
]
BANNER_WIDTH = len(BANNER[0])


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


def _keybar(tw: int) -> str:
    kb = "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit"
    credit = "\u24b8 D. Daud Yusup"
    gap = tw - len(kb) - len(credit) - 1
    if gap >= 0:
        return kb + " " * gap + credit
    return kb


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

    sys.stdout.write("\x1b[2J\x1b[H")

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

    if lang_menu:
        content.append((t("select_language", locale), "bold"))
        content.append((None, None))

    max_item = max(len(f"> {item}") for item in items)
    inner_w = max_item + 6
    box_w = inner_w + 4
    bx_pad = max(0, (tw - box_w) // 2)

    box_top = " " * bx_pad + "\u250c" + "\u2500" * (inner_w + 2) + "\u2510"
    content.append((box_top, "bold cyan"))

    for i, item in enumerate(items):
        prefix = "> " if i == current else "  "
        item_str = prefix + item
        pad_r = inner_w - len(item_str)
        if i == current:
            rt = Text(" " * bx_pad + "\u2502 ")
            rt.append(item_str, style="reverse")
            rt.append(" " * pad_r + " \u2502")
            content.append((rt, None))
        else:
            line = " " * bx_pad + "\u2502 " + item_str.ljust(inner_w) + " \u2502"
            content.append((line, None))

    box_bot = " " * bx_pad + "\u2514" + "\u2500" * (inner_w + 2) + "\u2518"
    content.append((box_bot, "bold cyan"))

    keybar_line = _keybar(tw)
    top_pad = 3
    max_content = max(1, th - 1 - top_pad)

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
        elif isinstance(text, Text):
            text.append(" " * (tw - len(text.plain)))
            console.print(text)
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
                langs = [label for label, _ in [("English", "en"), ("Indonesia", "id")]]
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
