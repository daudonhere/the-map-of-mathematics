from __future__ import annotations

import os
import sys
from pathlib import Path

from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtGui import QFont
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from mathverse.core.repository import Repository
from mathverse.core.seed import seed_repo
from mathverse.core.service import MapService
from mathverse.gui.fonts import load_fonts
from mathverse.gui.screens.explore import ExploreScreen
from mathverse.gui.screens.home import HomeScreen
from mathverse.gui.screens.splash_screen import SplashScreen
from mathverse.gui.screens.topic import TopicScreen
from mathverse.gui.screens.visualize import VisualizeScreen

BACKSOUND = Path(__file__).resolve().parent / "audio" / "backsound.wav"

FADE_MS = 2000
FADE_STEPS = 20
TARGET_VOLUME = 0.2


class TheMapApp(QMainWindow):
    def __init__(self, service: MapService) -> None:
        super().__init__()
        self.service = service
        self.setWindowTitle(self.service._("app_title"))
        self.resize(1000, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.splash_screen = SplashScreen(self.service, self)
        self.home_screen = HomeScreen(self.service, self)
        self.explore_screen = ExploreScreen(self.service, self)
        self.topic_screen = TopicScreen(self.service, self)
        self.visualize_screen = VisualizeScreen(self.service, self)

        self.stack.addWidget(self.splash_screen)
        self.stack.addWidget(self.home_screen)
        self.stack.addWidget(self.explore_screen)
        self.stack.addWidget(self.topic_screen)
        self.stack.addWidget(self.visualize_screen)

        self.stack.setCurrentWidget(self.splash_screen)

        self._init_audio()

    def _init_audio(self) -> None:
        self._player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._audio_output.setVolume(0.0)
        self._player.setAudioOutput(self._audio_output)
        self._player.setSource(QUrl.fromLocalFile(str(BACKSOUND)))
        self._player.mediaStatusChanged.connect(self._on_media_status)
        self._player.positionChanged.connect(self._on_position_changed)
        self._fade_timer = QTimer(self)
        self._fade_timer.timeout.connect(self._fade_step)
        self._fading = False
        self._player.play()
        self._start_fade(1)

    def _start_fade(self, direction: int) -> None:
        self._fading = True
        self._fade_dir = direction
        self._fade_step = 0
        self._fade_timer.start(FADE_MS // FADE_STEPS)

    def _fade_step(self) -> None:
        self._fade_step += 1
        t = self._fade_step / FADE_STEPS
        vol = TARGET_VOLUME * (t if self._fade_dir == 1 else 1.0 - t)
        self._audio_output.setVolume(vol)
        if self._fade_step >= FADE_STEPS:
            self._fade_timer.stop()
            self._fading = False

    def _on_media_status(self, status: QMediaPlayer.MediaStatus) -> None:
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self._player.play()
            self._start_fade(1)

    def _on_position_changed(self, pos: int) -> None:
        dur = self._player.duration()
        if dur > 0 and pos >= dur - FADE_MS and not self._fading:
            self._start_fade(-1)

    def closeEvent(self, event) -> None:  # noqa: N802
        self._fade_timer.stop()
        self._player.stop()
        super().closeEvent(event)

    def retranslate(self) -> None:
        self.home_screen.refresh()

    def show_concept(self, concept_id: str) -> None:
        self.explore_screen.show_concept(concept_id)
        self.stack.setCurrentWidget(self.explore_screen)

    def show_topic(self, concept_id: str) -> None:
        self.topic_screen.show_topic(concept_id)
        self.stack.setCurrentWidget(self.topic_screen)

    def go_home(self) -> None:
        self.stack.setCurrentWidget(self.home_screen)

    def go_splash(self) -> None:
        self.stack.setCurrentWidget(self.splash_screen)

    def go_visualize(self) -> None:
        self.visualize_screen.refresh()
        self.stack.setCurrentWidget(self.visualize_screen)


def main(locale: str = "en") -> None:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, 2)
    os.close(devnull)

    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget {
            background-color: #1a1a2e;
            color: #f0f0f0;
        }
        QListWidget {
            background-color: #16213e;
            color: #f0f0f0;
            border: 1px solid #FFD700;
            border-radius: 6px;
            font-size: 15px;
            padding: 4px;
        }
        QListWidget::item {
            padding: 8px 12px;
            border-radius: 4px;
        }
        QListWidget::item:selected {
            background-color: #FFD700;
            color: #1a1a2e;
        }
        QListWidget::item:hover {
            background-color: #2a2a4e;
        }
        QTextBrowser {
            background-color: transparent;
            color: #ccc;
            border: none;
        }
        QPushButton {
            background-color: #FFD700;
            color: #1a1a2e;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #e6c200;
        }
        QPushButton:pressed {
            background-color: #cca800;
        }
        QFrame[frameShape="4"] {
            color: #333;
        }
    """)

    families = load_fonts()
    if "STIX Two Text" in families:
        app.setFont(QFont("STIX Two Text", 13))

    repo = Repository()
    seed_repo(repo)
    service = MapService(repo, locale)

    window = TheMapApp(service)
    window.show()
    sys.exit(app.exec())
