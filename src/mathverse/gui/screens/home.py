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

from mathverse.core.service import MapService


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

        self.back_btn = QPushButton("\u2190  " + self.service._("back"))
        self.back_btn.setStyleSheet("""
            QPushButton {
                text-align: left; border: none; background: transparent;
                font-size: 14px; color: #888; padding: 4px 0;
            }
            QPushButton:hover { color: #FFD700; }
        """)
        self.back_btn.clicked.connect(self._go_back)
        layout.addWidget(self.back_btn)

        title = QLabel(self.service._("math_topics"))
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold; color: #FFD700; padding: 16px 0 8px 0;"
        )
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget {
                border: 1px solid #FFD700; border-radius: 8px;
                font-size: 16px; padding: 6px;
            }
            QListWidget::item {
                padding: 10px 14px; border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #FFD700; color: #1a1a2e;
            }
            QListWidget::item:hover {
                background-color: #2a2a4e;
            }
        """)
        self._refresh_list()
        self.list_widget.itemDoubleClicked.connect(self._on_concept_selected)
        self.list_widget.itemActivated.connect(self._on_concept_selected)
        layout.addWidget(self.list_widget)

        layout.addStretch()

        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(0, 12, 0, 12)

        back_btn = QPushButton("\u2190  " + self.service._("back"))
        back_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 12px 28px;
                background-color: transparent; color: #888;
                border: 1px solid #555; border-radius: 8px;
            }
            QPushButton:hover {
                border-color: #FFD700; color: #FFD700;
            }
        """)
        back_btn.clicked.connect(self._go_back)
        btn_layout.addWidget(back_btn)

        btn_layout.addStretch()

        visualize_btn = QPushButton(self.service._("visualize") + " \u25b6")
        visualize_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 12px 28px;
                background-color: transparent; color: #FFD700;
                border: 2px solid #FFD700; border-radius: 8px; font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FFD700; color: #1a1a2e;
            }
        """)
        visualize_btn.clicked.connect(lambda: self.app.go_visualize())
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

    def _go_back(self) -> None:
        self.app.go_splash()

    def keyPressEvent(self, event) -> None:  # noqa: N802
        if event.key() == Qt.Key.Key_Escape:
            self._go_back()
        elif event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            item = self.list_widget.currentItem()
            if item:
                self._on_concept_selected(item)
        else:
            super().keyPressEvent(event)
