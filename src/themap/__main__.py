import sys

from themap.cli.main import main as cli_main


def main() -> None:
    if "--gui" in sys.argv:
        sys.argv.remove("--gui")
        from themap.gui.main import main as gui_main

        gui_main()
    else:
        cli_main()


if __name__ == "__main__":
    main()
