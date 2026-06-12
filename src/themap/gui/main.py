from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from themap.core.repository import Repository
from themap.core.seed import seed_repo
from themap.core.service import MapService
from themap.gui.screens.explore import ExploreScreen
from themap.gui.screens.home import HomeScreen
from themap.gui.screens.visualize import VisualizeScreen


class TheMapApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("The Map of Mathematics")
        self.resize(1000, 700)

        repo = Repository()
        seed_repo(repo)
        self.service = MapService(repo)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home_screen = HomeScreen(self.service, self)
        self.explore_screen = ExploreScreen(self.service, self)
        self.visualize_screen = VisualizeScreen(self.service, self)

        self.stack.addWidget(self.home_screen)
        self.stack.addWidget(self.explore_screen)
        self.stack.addWidget(self.visualize_screen)

        self.stack.setCurrentWidget(self.home_screen)

    def show_concept(self, concept_id: str) -> None:
        self.explore_screen.show_concept(concept_id)
        self.stack.setCurrentWidget(self.explore_screen)

    def go_home(self) -> None:
        self.stack.setCurrentWidget(self.home_screen)

    def go_visualize(self) -> None:
        self.visualize_screen.refresh()
        self.stack.setCurrentWidget(self.visualize_screen)


def main() -> None:
    app = QApplication(sys.argv)
    window = TheMapApp()
    window.show()
    sys.exit(app.exec())
