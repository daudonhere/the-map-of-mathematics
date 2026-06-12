from __future__ import annotations

from PyQt6.QtWidgets import (
    QLabel,
    QListWidget,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from themap.core.service import MapService


class ExploreScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._current_id: str | None = None
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 24, 40, 24)

        back_btn = QPushButton("\u2190  Back to Home")
        back_btn.setStyleSheet("text-align: left;")
        back_btn.clicked.connect(lambda: self.app.go_home())
        layout.addWidget(back_btn)

        self.name_label = QLabel()
        self.name_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; padding-top: 16px;"
        )
        layout.addWidget(self.name_label)

        self.category_label = QLabel()
        self.category_label.setStyleSheet(
            "font-size: 13px; color: #888; padding-bottom: 8px;"
        )
        layout.addWidget(self.category_label)

        self.description_browser = QTextBrowser()
        self.description_browser.setStyleSheet("font-size: 14px;")
        self.description_browser.setMaximumHeight(120)
        layout.addWidget(self.description_browser)

        related_title = QLabel("Related Concepts")
        related_title.setStyleSheet(
            "font-size: 16px; font-weight: bold; padding-top: 16px;"
        )
        layout.addWidget(related_title)

        self.related_list = QListWidget()
        self.related_list.itemDoubleClicked.connect(self._on_related_selected)
        layout.addWidget(self.related_list)

        self.setLayout(layout)

    def show_concept(self, concept_id: str) -> None:
        self._current_id = concept_id
        concept = self.service.get_concept(concept_id)
        if not concept:
            self.name_label.setText("Concept not found")
            return
        self.name_label.setText(concept.name)
        self.category_label.setText(concept.category)
        self.description_browser.setText(concept.description)
        self.related_list.clear()
        for rid in concept.related_concepts:
            related = self.service.get_concept(rid)
            if related:
                self.related_list.addItem(related.name)
            else:
                self.related_list.addItem(rid)

    def _on_related_selected(self, item) -> None:
        name = item.text()
        concepts = self.service.list_concepts()
        for c in concepts:
            if c.name == name:
                self.show_concept(c.id)
                return
