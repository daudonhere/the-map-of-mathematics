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


class HomeScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 24, 40, 24)

        title = QLabel(self.service._("app_title"))
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold; padding-bottom: 4px;"
        )
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel(self.service._("select_topic"))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px; color: #666; padding-bottom: 16px;")
        layout.addWidget(subtitle)

        self.list_widget = QListWidget()
        self._refresh_list()
        self.list_widget.itemDoubleClicked.connect(self._on_concept_selected)
        layout.addWidget(self.list_widget)

        btn_layout = QHBoxLayout()
        visualize_btn = QPushButton(self.service._("visualize"))
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
