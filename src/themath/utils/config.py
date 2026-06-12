from __future__ import annotations

from pathlib import Path


class Config:
    APP_NAME = "the-map-of-mathematics"
    DATA_DIR = Path.home() / f".{APP_NAME}"
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    WINDOW_MIN_WIDTH = 800
    WINDOW_MIN_HEIGHT = 600
