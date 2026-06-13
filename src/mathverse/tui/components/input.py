from __future__ import annotations

import os
import select
import sys
import termios
import tty


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


def _read_input(prompt: str) -> str | None:
    """Read a line of input character by character. Returns None on Esc."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    buf = ""
    try:
        tty.setraw(fd)
        sys.stdout.write(prompt + " " + buf)
        sys.stdout.flush()
        while True:
            ch = os.read(fd, 1)
            if ch == b"\x1b":
                r, _, _ = select.select([fd], [], [], 0.1)
                if r:
                    os.read(fd, 2)
                    continue
                return None
            elif ch in (b"\n", b"\r"):
                sys.stdout.write("\r\n")
                sys.stdout.flush()
                return buf
            elif ch == b"\t":
                return None
            elif ch == b"\x7f":
                buf = buf[:-1]
            else:
                try:
                    c = ch.decode()
                    buf += c
                except UnicodeDecodeError:
                    continue
            line = prompt + " " + buf
            sys.stdout.write("\r" + " " * 80 + "\r" + line)
            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _read_input_at_cursor(fd: int, tw: int) -> str | None:
    old = termios.tcgetattr(fd)
    buf = ""
    pad = max(2, tw // 20)
    black_bg = "\x1b[48;2;0;0;0m"
    green_bg = "\x1b[48;2;26;58;26m"
    white_fg = "\x1b[38;2;255;255;255m"
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()
    try:
        tty.setraw(fd)
        while True:
            ch = os.read(fd, 1)
            if ch == b"\x1b":
                r, _, _ = select.select([fd], [], [], 0.1)
                if r:
                    os.read(fd, 2)
                    continue
                return None
            elif ch in (b"\n", b"\r"):
                sys.stdout.write("\r\n" + "\x1b[0m")
                sys.stdout.flush()
                return buf
            elif ch == b"\t":
                return "\r"
            elif ch == b"\x7f":
                buf = buf[:-1]
            else:
                try:
                    c = ch.decode()
                    buf += c
                except UnicodeDecodeError:
                    continue
            gap = tw - 2 * pad - 2 - 3 - len(buf)
            sys.stdout.write(
                "\r"
                + black_bg
                + " " * tw
                + "\r"
                + black_bg
                + " " * pad
                + green_bg
                + white_fg
                + "\u2502"
                + ">> "
                + buf
                + " " * max(0, gap)
                + "\u2502"
                + black_bg
                + " " * pad
                + f"\x1b[{pad + 5 + len(buf)}G"
            )
            sys.stdout.flush()
    finally:
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _read_value_chalkboard(fd: int, tw: int, label: str) -> str | None:
    old = termios.tcgetattr(fd)
    buf = ""
    pad = max(2, tw // 20)
    black_bg = "\x1b[48;2;0;0;0m"
    green_bg = "\x1b[48;2;26;58;26m"
    white_fg = "\x1b[38;2;255;255;255m"
    display = f"  {label}= "
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()
    try:
        tty.setraw(fd)
        while True:
            ch = os.read(fd, 1)
            if ch in (b"\n", b"\r"):
                sys.stdout.write("\r\n" + "\x1b[0m")
                sys.stdout.flush()
                return buf
            elif ch == b"\x1b":
                r, _, _ = select.select([fd], [], [], 0.1)
                if r:
                    os.read(fd, 2)
                    continue
                return None
            elif ch == b"\t":
                return "\r"
            elif ch == b"\x7f":
                buf = buf[:-1]
            else:
                try:
                    buf += ch.decode()
                except UnicodeDecodeError:
                    continue
            inner = tw - 2 * pad - 2
            line = display + buf
            gap = max(0, inner - len(line))
            sys.stdout.write(
                "\r"
                + black_bg
                + " " * tw
                + "\r"
                + black_bg
                + " " * pad
                + green_bg
                + white_fg
                + "\u2502"
                + line
                + " " * gap
                + "\u2502"
                + black_bg
                + " " * pad
                + f"\x1b[{pad + 2 + len(line)}G"
            )
            sys.stdout.flush()
    finally:
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
