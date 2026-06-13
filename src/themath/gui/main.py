from __future__ import annotations

import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from themath.core.repository import Repository
from themath.core.seed import seed_repo
from themath.core.service import MapService
from themath.gui.fonts import load_fonts
from themath.gui.screens.explore import ExploreScreen
from themath.gui.screens.home import HomeScreen
from themath.gui.screens.topic import TopicScreen
from themath.gui.screens.visualize import VisualizeScreen


class TheMapApp(QMainWindow):
    def __init__(self, service: MapService) -> None:
        super().__init__()
        self.service = service
        self.setWindowTitle(self.service._("app_title"))
        self.resize(1000, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home_screen = HomeScreen(self.service, self)
        self.explore_screen = ExploreScreen(self.service, self)
        self.topic_screen = TopicScreen(self.service, self)
        self.visualize_screen = VisualizeScreen(self.service, self)

        self.stack.addWidget(self.home_screen)
        self.stack.addWidget(self.explore_screen)
        self.stack.addWidget(self.topic_screen)
        self.stack.addWidget(self.visualize_screen)

        self.stack.setCurrentWidget(self.home_screen)

    def show_concept(self, concept_id: str) -> None:
        self.explore_screen.show_concept(concept_id)
        self.stack.setCurrentWidget(self.explore_screen)

    def show_topic(self, concept_id: str) -> None:
        self.topic_screen.show_topic(concept_id)
        self.stack.setCurrentWidget(self.topic_screen)

    def go_home(self) -> None:
        self.stack.setCurrentWidget(self.home_screen)

    def go_visualize(self) -> None:
        self.visualize_screen.refresh()
        self.stack.setCurrentWidget(self.visualize_screen)


def main(locale: str = "id") -> None:
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget {
            background-color: #1a1a2e;
            color: #f0f0f0;
        }
        QListWidget {
            background-color: #16213e;
            color: #f0f0f0;
            border: 1px solid #0f3460;
            border-radius: 6px;
            font-size: 15px;
            padding: 4px;
        }
        QListWidget::item {
            padding: 8px 12px;
            border-radius: 4px;
        }
        QListWidget::item:selected {
            background-color: #0f3460;
            color: #00d4ff;
        }
        QListWidget::item:hover {
            background-color: #1a2744;
        }
        QTextBrowser {
            background-color: transparent;
            color: #ccc;
            border: none;
        }
        QPushButton {
            background-color: #0f3460;
            color: #f0f0f0;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #1a5276;
        }
        QPushButton:pressed {
            background-color: #0a2540;
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
