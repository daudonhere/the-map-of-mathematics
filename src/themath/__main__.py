from __future__ import annotations

import sys


def main() -> None:
    locale = "en"
    if "--lang" in sys.argv:
        idx = sys.argv.index("--lang")
        try:
            locale = sys.argv[idx + 1]
        except IndexError:
            locale = "en"
        if locale not in ("en", "id"):
            locale = "en"
        del sys.argv[idx : idx + 2]

    if "--gui" in sys.argv:
        sys.argv.remove("--gui")
        from themath.gui.main import main as gui_main

        gui_main(locale)
        return

    from themath.tui.launcher import run_launcher

    mode = run_launcher(locale)
    if mode == "terminal":
        from themath.cli.main import main as cli_main

        cli_main(locale)
    elif mode == "gui":
        from themath.gui.main import main as gui_main

        gui_main(locale)


if __name__ == "__main__":
    main()
