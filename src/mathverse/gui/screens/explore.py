from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLabel,
    QListWidget,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from mathverse.core.content import get_content
from mathverse.core.service import MapService


class ExploreScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._current_id: str | None = None
        self._build_ui()

    def _build_ui(self) -> None:
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 16, 40, 16)
        layout.setSpacing(0)

        self.back_btn = QPushButton("\u2190  " + self.service._("back"))
        self.back_btn.setStyleSheet("""
            QPushButton {
                text-align: left; border: none; background: transparent;
                font-size: 14px; color: #888; padding: 4px 0;
            }
            QPushButton:hover { color: #FFD700; }
        """)
        self.back_btn.clicked.connect(lambda: self.app.go_home())
        layout.addWidget(self.back_btn)

        self.name_label = QLabel()
        self.name_label.setStyleSheet(
            "font-size: 28px; font-weight: bold; color: #FFD700; padding: 16px 0 4px 0;"
        )
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.name_label)

        self.category_label = QLabel()
        self.category_label.setStyleSheet(
            "font-size: 13px; color: #888; padding-bottom: 12px;"
        )
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.category_label)

        self.description_browser = QTextBrowser()
        self.description_browser.setMaximumHeight(120)
        self.description_browser.setStyleSheet("""
            QTextBrowser {
                font-size: 15px; border: 1px solid #333;
                border-radius: 6px; padding: 8px;
                background-color: #16213e;
            }
        """)
        layout.addWidget(self.description_browser)

        self.topics_btn = QPushButton()
        self.topics_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 12px 24px; margin-top: 8px;
                background-color: transparent; color: #FFD700;
                border: 2px solid #FFD700; border-radius: 8px; font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FFD700; color: #1a1a2e;
            }
        """)
        self.topics_btn.clicked.connect(self._on_topics_clicked)
        self.topics_btn.setVisible(False)
        layout.addWidget(self.topics_btn)

        related_title = QLabel(self.service._("related_concepts"))
        related_title.setStyleSheet(
            "font-size: 15px; font-weight: bold; color: #aaa; padding-top: 16px;"
        )
        layout.addWidget(related_title)

        self.related_list = QListWidget()
        self.related_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #FFD700; border-radius: 6px;
                font-size: 15px; padding: 4px;
            }
            QListWidget::item {
                padding: 8px 12px; border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #FFD700; color: #1a1a2e;
            }
            QListWidget::item:hover {
                background-color: #2a2a4e;
            }
        """)
        self.related_list.itemDoubleClicked.connect(self._on_related_selected)
        self.related_list.itemActivated.connect(self._on_related_selected)
        layout.addWidget(self.related_list)

        self.setLayout(layout)

    def show_concept(self, concept_id: str) -> None:
        self._current_id = concept_id
        concept = self.service.get_concept(concept_id)
        if not concept:
            self.name_label.setText(self.service._("concept_not_found"))
            return
        self.name_label.setText(concept.name)
        self.category_label.setText(f"{self.service._('category')}: {concept.category}")
        self.description_browser.setText(concept.description)
        self.related_list.clear()
        for rid in concept.related_concepts:
            related = self.service.get_concept(rid)
            if related:
                self.related_list.addItem(related.name)
            else:
                self.related_list.addItem(rid)

        content = get_content(concept_id)
        if content and content.subtopics:
            self.topics_btn.setText("\u25b6  " + self.service._("explore_topics"))
            self.topics_btn.setVisible(True)
        else:
            self.topics_btn.setVisible(False)

    def _on_related_selected(self, item) -> None:
        name = item.text()
        for c in self.service.list_concepts():
            if c.name == name:
                self.show_concept(c.id)
                return

    def _on_topics_clicked(self) -> None:
        if self._current_id:
            self.app.show_topic(self._current_id)

    def keyPressEvent(self, event) -> None:  # noqa: N802
        if event.key() == Qt.Key.Key_Escape:
            self.app.go_home()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if self.topics_btn.isVisible() and self.topics_btn.hasFocus():
                self._on_topics_clicked()
            else:
                item = self.related_list.currentItem()
                if item:
                    self._on_related_selected(item)
        elif event.key() == Qt.Key.Key_Tab:
            if self.topics_btn.isVisible():
                self.topics_btn.setFocus()
            else:
                self.related_list.setFocus()
        else:
            super().keyPressEvent(event)
