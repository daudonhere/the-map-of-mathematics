from __future__ import annotations

from pathlib import Path

from PyQt6.QtGui import QFontDatabase

FONT_DIR = Path(__file__).parent


def load_fonts() -> list[str]:
    families: list[str] = []
    for otf in sorted(FONT_DIR.glob("*.otf")):
        fid = QFontDatabase.addApplicationFont(str(otf))
        if fid >= 0:
            families.extend(QFontDatabase.applicationFontFamilies(fid))
    return families
