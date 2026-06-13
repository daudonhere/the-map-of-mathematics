from __future__ import annotations

import shutil

from rich.console import Console

from mathverse.core.content import SubTopic, get_content
from mathverse.tui.components.chalkboard import _render_content
from mathverse.tui.components.input import _read_key
from mathverse.tui.launcher import BANNER, BANNER_WIDTH
from mathverse.tui.playgrounds import _playground

_LOCALE: str = "en"


def run_topic_screen(
    console: Console,
    concept_id: str,
    locale: str = "en",
) -> str | None:
    global _LOCALE
    _LOCALE = locale

    content = get_content(concept_id)
    if content is None or not content.subtopics:
        return None

    current = 0
    detail_subtopic: SubTopic | None = None

    while True:
        if detail_subtopic is not None:
            _render_detail(console, detail_subtopic, locale, concept_id)
            key = _read_key()
            if key == "enter" and detail_subtopic.playground:
                sub_title = detail_subtopic.title.get(
                    locale, detail_subtopic.title.get("en", "")
                )
                if (
                    _playground(
                        console, detail_subtopic.playground, locale, title=sub_title
                    )
                    is None
                ):
                    return None
                detail_subtopic = None
            elif key == "tab":
                detail_subtopic = None
            elif key in ("esc", "q"):
                return None
        else:
            _render_list(console, content.subtopics, current, locale, concept_id)
            key = _read_key()
            if key == "up":
                current = (current - 1) % len(content.subtopics)
            elif key == "down":
                current = (current + 1) % len(content.subtopics)
            elif key == "enter":
                detail_subtopic = content.subtopics[current]
            elif key == "tab":
                return "back"
            elif key in ("esc", "q"):
                return None


def _render_list(
    console: Console,
    subtopics: list[SubTopic],
    current: int,
    locale: str,
    concept_id: str = "arithmetic",
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    content_lines: list[tuple[str | None, str | None]] = []

    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content_lines.append((" " * left_pad + b, "bold"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))

    concept_name = {
        "aritmatika": "Aritmatika",
        "arithmetic": "Arithmetic",
        "aljabar": "Aljabar",
        "algebra": "Algebra",
    }.get(concept_id, concept_id.replace("-", " ").title())
    content_lines.append((concept_name, "bold"))
    content_lines.append((None, None))

    for i, st in enumerate(subtopics):
        prefix = "> " if i == current else "  "
        style = "reverse" if i == current else None
        content_lines.append(
            (f"{prefix}{st.title.get(locale, st.title.get('en', ''))}", style)
        )

    selected = subtopics[current]
    content_lines.append((None, None))
    content_lines.append(("\u2500" * min(tw, 60), "dim"))
    content_lines.append((None, None))

    pad = max(2, tw // 20)
    inner_w = tw - 2 * pad - 2

    preview: list[tuple[str | None, str | None]] = []

    expl = selected.description.get(locale, selected.description.get("en", ""))
    for line in expl.split("\n"):
        if len(line) > inner_w:
            for chunk in [line[i : i + inner_w] for i in range(0, len(line), inner_w)]:
                preview.append((chunk, None))
        else:
            preview.append((line, None))

    preview_height = 8
    if len(preview) > preview_height:
        preview = preview[:preview_height]
    elif len(preview) < preview_height:
        preview += [(None, None)] * (preview_height - len(preview))

    content_lines += preview

    _render_content(
        console,
        tw,
        th,
        content_lines,
        "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit",
        chalkboard=True,
        header_count=9 if tw >= BANNER_WIDTH else 0,
    )


def _render_detail(
    console: Console,
    subtopic: SubTopic,
    locale: str,
    concept_id: str = "arithmetic",
) -> None:
    th = shutil.get_terminal_size().lines
    tw = shutil.get_terminal_size().columns

    content_lines: list[tuple[str | None, str | None]] = []

    if tw >= BANNER_WIDTH:
        left_pad = max(0, (tw - BANNER_WIDTH) // 2)
        for b in BANNER:
            content_lines.append((" " * left_pad + b, "bold"))
        content_lines.append((None, None))
        subtitle = "For minds losing their edge"
        sub_left_pad = max(0, (tw - len(subtitle)) // 2)
        content_lines.append((" " * sub_left_pad + subtitle, "italic"))
        content_lines.append((None, None))

    concept_name = {
        "aritmatika": "Aritmatika",
        "arithmetic": "Arithmetic",
        "aljabar": "Aljabar",
        "algebra": "Algebra",
    }.get(concept_id, concept_id.replace("-", " ").title())
    content_lines.append((concept_name, "bold"))
    content_lines.append((None, None))

    content_lines.append(
        (subtopic.title.get(locale, subtopic.title.get("en", "")), "bold")
    )
    content_lines.append((None, None))

    expl = subtopic.explanation.get(locale, subtopic.explanation.get("en", ""))
    expl_lines = [ln.strip() for ln in expl.split("\n") if ln.strip()]

    content_lines.append(("Examples" if locale == "en" else "Contoh", "bold"))
    content_lines.append((None, None))
    ex_list = subtopic.examples.get(locale, subtopic.examples.get("en", []))
    expl_idx = 0
    pad = max(2, tw // 20)
    inner_w = tw - 2 * pad - 2
    for ex in ex_list:
        if ex == "":
            content_lines.append((None, None))
        else:
            if len(ex) > inner_w:
                for chunk in [ex[i : i + inner_w] for i in range(0, len(ex), inner_w)]:
                    content_lines.append((chunk, "dim"))
            else:
                content_lines.append((ex, "dim"))
            if expl_idx < len(expl_lines):
                el = expl_lines[expl_idx]
                if len(el) > inner_w:
                    for chunk in [
                        el[i : i + inner_w] for i in range(0, len(el), inner_w)
                    ]:
                        content_lines.append((chunk, "italic"))
                else:
                    content_lines.append((el, "italic"))
                expl_idx += 1

    if subtopic.playground:
        content_lines.append((None, None))
        content_lines.append(("Playground" if locale == "en" else "Latihan", "bold"))
        content_lines.append((None, None))
        content_lines.append(
            (
                "Press Enter to start playground"
                if locale == "en"
                else "Tekan Enter untuk memulai latihan",
                "italic",
            )
        )

    keybar = "\u2191 Up   \u2193 Down   \u21b5 Enter   \u21b9 Back   Esc Exit"
    _render_content(
        console,
        tw,
        th,
        content_lines,
        keybar,
        chalkboard=True,
        header_count=9 if tw >= BANNER_WIDTH else 0,
    )
