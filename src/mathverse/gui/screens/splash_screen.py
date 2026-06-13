from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from mathverse.core.service import MapService


class SplashScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self._build_ui()

    def _build_ui(self) -> None:
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(0)

        layout.addStretch(2)

        self.title_label = QLabel(self.service._("the_math"))
        self.title_label.setStyleSheet("""
            font-size: 64px; font-weight: bold;
            color: #FFD700; letter-spacing: 4px;
        """)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        math_symbols = QLabel("\u2211  \u220f  \u221e  \u03c0  \u2202  \u221a")
        math_symbols.setStyleSheet(
            "font-size: 24px; color: #555; padding: 8px 0; letter-spacing: 12px;"
        )
        math_symbols.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(math_symbols)

        self.slogan_label = QLabel(self.service._("slogan"))
        self.slogan_label.setStyleSheet(
            "font-size: 16px; font-style: italic; color: #888; padding: 8px 0 32px 0;"
        )
        self.slogan_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.slogan_label)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet("color: #333;")
        sep.setFixedWidth(300)
        layout.addWidget(sep, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacing(32)

        self.start_btn = QPushButton(self.service._("start"))
        self.start_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px; padding: 16px 64px;
                background-color: transparent; color: #FFD700;
                border: 2px solid #FFD700; border-radius: 12px;
                font-weight: bold; letter-spacing: 2px;
            }
            QPushButton:hover {
                background-color: #FFD700; color: #1a1a2e;
            }
        """)
        self.start_btn.clicked.connect(lambda: self.app.go_home())
        layout.addWidget(self.start_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacing(16)

        self.lang_btn = QPushButton(self.service._("change_language"))
        self.lang_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px; padding: 10px 32px;
                background-color: transparent; color: #888;
                border: 1px solid #555; border-radius: 8px;
            }
            QPushButton:hover {
                border-color: #FFD700; color: #FFD700;
            }
        """)
        self.lang_btn.clicked.connect(self._toggle_language)
        layout.addWidget(self.lang_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(3)

        self.setLayout(layout)

    def _toggle_language(self) -> None:
        current = self.service.locale
        new = "id" if current == "en" else "en"
        self.service.set_locale(new)
        self._refresh_texts()
        self.app.retranslate()

    def _refresh_texts(self) -> None:
        self.title_label.setText(self.service._("the_math"))
        self.slogan_label.setText(self.service._("slogan"))
        self.start_btn.setText(self.service._("start"))
        self.lang_btn.setText(self.service._("change_language"))

    def keyPressEvent(self, event) -> None:  # noqa: N802
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.app.go_home()
        elif event.key() == Qt.Key.Key_Escape:
            self.app.close()
        else:
            super().keyPressEvent(event)
