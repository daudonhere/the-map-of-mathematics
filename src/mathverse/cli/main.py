from __future__ import annotations

from mathverse.core.repository import Repository
from mathverse.core.seed import seed_repo
from mathverse.core.service import MapService
from mathverse.tui.browser import run_browser


def main(locale: str = "id") -> str | None:
    repo = Repository()
    seed_repo(repo)
    service = MapService(repo, locale)
    return run_browser(service)


if __name__ == "__main__":
    import sys

    locale_arg = "id"
    if "--lang" in sys.argv:
        idx = sys.argv.index("--lang")
        try:
            locale_arg = sys.argv[idx + 1]
        except IndexError:
            locale_arg = "id"
        if locale_arg not in ("en", "id"):
            locale_arg = "id"
    main(locale_arg)
