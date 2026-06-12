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

from themap.core.service import MapService


class HomeScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 24, 40, 24)

        title = QLabel("The Map of Mathematics")
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold; padding-bottom: 4px;"
        )
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Select a topic to explore")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px; color: #666; padding-bottom: 16px;")
        layout.addWidget(subtitle)

        self.list_widget = QListWidget()
        concepts = self.service.list_concepts()
        for c in concepts:
            self.list_widget.addItem(f"{c.name}  |  {c.category}")
        self.list_widget.itemDoubleClicked.connect(self._on_concept_selected)
        layout.addWidget(self.list_widget)

        btn_layout = QHBoxLayout()
        visualize_btn = QPushButton("Visualize Connections")
        visualize_btn.clicked.connect(lambda: self.app.go_visualize())
        btn_layout.addStretch()
        btn_layout.addWidget(visualize_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def _on_concept_selected(self, item) -> None:
        name = item.text().split("  |  ")[0]
        concepts = self.service.list_concepts()
        for c in concepts:
            if c.name == name:
                self.app.show_concept(c.id)
                return
