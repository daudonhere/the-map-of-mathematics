from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from themap.core.service import MapService


class VisualizeScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 24, 40, 24)

        back_btn = QPushButton("\u2190  Back to Home")
        back_btn.setStyleSheet("text-align: left;")
        back_btn.clicked.connect(lambda: self.app.go_home())
        layout.addWidget(back_btn)

        title = QLabel("Concept Connections")
        title.setStyleSheet("font-size: 24px; font-weight: bold; padding-top: 16px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.browser = QTextBrowser()
        self.browser.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.browser)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(refresh_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def refresh(self) -> None:
        concepts = self.service.list_concepts()
        if not concepts:
            self.browser.setText("No concepts available.")
            return
        lines = ["<b>The Map of Mathematics - All Connections</b>", "", ""]
        for c in concepts:
            links = []
            for rid in c.related_concepts:
                related = self.service.get_concept(rid)
                if related:
                    links.append(related.name)
                else:
                    links.append(rid)
            links_text = ", ".join(links) if links else "(none)"
            lines.append(
                f'<b style="color: #0066cc;">{c.name}</b>'
                f' <span style="color: #888;">[{c.category}]</span><br>'
                f"&nbsp;&nbsp;\u2192 {links_text}<br>"
            )
        self.browser.setHtml("<br>".join(lines))
