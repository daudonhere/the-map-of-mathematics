from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from themath.core.service import MapService

BANNER_LINES = [
    "████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ████████╗██╗  ██╗",
    "╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║",
    "   ██║   ███████║█████╗      ██╔████╔██║███████║   ██║   ███████║",
    "   ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║",
    "   ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║",
    "   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝",
]


class HomeScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 24, 40, 24)
        layout.setSpacing(0)

        for line in BANNER_LINES:
            lbl = QLabel(line)
            lbl.setStyleSheet(
                "font-size: 14px; font-family: monospace; color: #00d4ff;"
            )
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(lbl)

        tagline = QLabel("For minds losing their edge")
        tagline.setStyleSheet(
            "font-size: 14px; font-style: italic; color: #666; padding: 4px 0 16px 0;"
        )
        tagline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(tagline)

        title = QLabel(self.service._("select_topic"))
        title.setStyleSheet("font-size: 18px; color: #aaa; padding-bottom: 8px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.list_widget = QListWidget()
        self._refresh_list()
        self.list_widget.itemDoubleClicked.connect(self._on_concept_selected)
        layout.addWidget(self.list_widget)

        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(0, 12, 0, 0)
        visualize_btn = QPushButton("\u25b6  " + self.service._("visualize"))
        visualize_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 12px 32px;
                background-color: #0f3460; color: #00d4ff;
                border: 1px solid #00d4ff; border-radius: 8px; font-weight: bold;
            }
            QPushButton:hover {
                background-color: #16213e; color: #00ff88; border-color: #00ff88;
            }
        """)
        visualize_btn.clicked.connect(lambda: self.app.go_visualize())
        btn_layout.addStretch()
        btn_layout.addWidget(visualize_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def refresh(self) -> None:
        self._refresh_list()

    def _refresh_list(self) -> None:
        self.list_widget.clear()
        for c in self.service.list_concepts():
            self.list_widget.addItem(f"{c.name}  |  {c.category}")

    def _on_concept_selected(self, item) -> None:
        name = item.text().split("  |  ")[0]
        for c in self.service.list_concepts():
            if c.name == name:
                self.app.show_concept(c.id)
                return
