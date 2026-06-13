from __future__ import annotations

from mathverse.core.models import SubTopic

subtopics: list[SubTopic] = []


def gen_question(_playground: str, _locale: str) -> tuple[str, str, float] | None:
    return None


__all__ = ["gen_question", "subtopics"]
