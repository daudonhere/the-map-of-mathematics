import sys


def main() -> None:
    """Route ke CLI atau GUI berdasarkan argumen."""
    if "--gui" in sys.argv:
        sys.argv.remove("--gui")
        from themap.gui.main import main as gui_main

        gui_main()
    else:
        from themap.cli.main import main as cli_main

        cli_main()


if __name__ == "__main__":
    main()
