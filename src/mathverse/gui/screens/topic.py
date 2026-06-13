from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QStackedWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from mathverse.core.content import SubTopic, get_content
from mathverse.core.quiz import gen_question
from mathverse.core.service import MapService


class PlaygroundDialog(QDialog):
    def __init__(self, playground: str, locale: str, parent=None):
        super().__init__(parent)
        self.playground = playground
        self.locale = locale
        self.correct = 0
        self.total = 0
        self.setWindowTitle("Playground" if locale == "en" else "Latihan")
        self.setMinimumWidth(480)
        self.setStyleSheet("""
            QDialog {
                background-color: #1a1a2e;
            }
        """)
        self._build_ui()
        self._next_question()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        header = QLabel("Playground" if self.locale == "en" else "Latihan")
        header.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #FFD700; padding-bottom: 4px;"
        )
        layout.addWidget(header)

        self.score_label = QLabel()
        self.score_label.setStyleSheet("font-size: 14px; color: #aaa;")
        layout.addWidget(self.score_label)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet("color: #333;")
        layout.addWidget(sep)

        self.question_label = QLabel()
        self.question_label.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #f0f0f0; padding: 16px 0;"
        )
        self.question_label.setWordWrap(True)
        layout.addWidget(self.question_label)

        input_layout = QHBoxLayout()
        self.answer_input = QLineEdit()
        self.answer_input.setStyleSheet("""
            QLineEdit {
                font-size: 18px; padding: 10px;
                background-color: #16213e; color: #f0f0f0;
                border: 1px solid #FFD700; border-radius: 6px;
            }
            QLineEdit:focus { border-color: #FFD700; }
        """)
        self.answer_input.returnPressed.connect(self._check_answer)
        input_layout.addWidget(self.answer_input)

        submit_btn = QPushButton("OK")
        submit_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px; padding: 10px 24px;
                background-color: #FFD700; color: #1a1a2e;
                border: none; border-radius: 6px; font-weight: bold;
            }
            QPushButton:hover { background-color: #e6c200; }
        """)
        submit_btn.clicked.connect(self._check_answer)
        input_layout.addWidget(submit_btn)
        layout.addLayout(input_layout)

        self.feedback_label = QLabel()
        self.feedback_label.setStyleSheet("font-size: 16px; padding: 8px 0;")
        layout.addWidget(self.feedback_label)

        btn_layout = QHBoxLayout()
        self.next_btn = QPushButton(
            "Next \u2192" if self.locale == "en" else "Lanjut \u2192"
        )
        self.next_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 10px 24px;
                background-color: #FFD700; color: #1a1a2e;
                border: none; border-radius: 6px; font-weight: bold;
            }
            QPushButton:hover { background-color: #e6c200; }
        """)
        self.next_btn.setVisible(False)
        self.next_btn.clicked.connect(self._next_question)
        btn_layout.addWidget(self.next_btn)

        close_btn = QPushButton("Exit" if self.locale == "en" else "Keluar")
        close_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px; padding: 8px 20px;
                background-color: #333; color: #aaa;
                border: none; border-radius: 6px;
            }
            QPushButton:hover { background-color: #555; }
        """)
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def _next_question(self) -> None:
        self.question, self.answer_str, _ = gen_question(self.playground, self.locale)
        self.question_label.setText(self.question)
        self.answer_input.clear()
        self.answer_input.setEnabled(True)
        self.answer_input.setFocus()
        self.feedback_label.setText("")
        self.score_label.setText(
            f"Score: {self.correct}/{self.total}"
            if self.locale == "en"
            else f"Nilai: {self.correct}/{self.total}"
        )
        self.next_btn.setVisible(False)

    def _check_answer(self) -> None:
        response = self.answer_input.text()
        if not response:
            return
        self.total += 1
        is_correct = response.strip() == self.answer_str
        if is_correct:
            self.correct += 1

        if is_correct:
            txt = "CORRECT!" if self.locale == "en" else "BENAR!"
            color = "#00ff88"
        else:
            txt = (
                f"WRONG. Correct answer: {self.answer_str}"
                if self.locale == "en"
                else f"SALAH. Jawaban benar: {self.answer_str}"
            )
            color = "#ff4444"

        self.feedback_label.setStyleSheet(
            f"font-size: 16px; padding: 8px 0; color: {color}; font-weight: bold;"
        )
        self.feedback_label.setText(txt)
        self.score_label.setText(
            f"Score: {self.correct}/{self.total}"
            if self.locale == "en"
            else f"Nilai: {self.correct}/{self.total}"
        )
        self.answer_input.setEnabled(False)
        self.next_btn.setVisible(True)
        self.next_btn.setFocus()

    def keyPressEvent(self, event) -> None:  # noqa: N802
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)


class TopicScreen(QWidget):
    def __init__(self, service: MapService, app: QWidget) -> None:
        super().__init__()
        self.service = service
        self.app = app
        self.content = None
        self.subtopics: list[SubTopic] = []
        self.current_concept_id: str = ""
        self._current_playground: str | None = None
        self._current_detail_subtopic: SubTopic | None = None
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
        self.back_btn.clicked.connect(self._go_back)
        layout.addWidget(self.back_btn)

        self.concept_label = QLabel()
        self.concept_label.setStyleSheet(
            "font-size: 28px; font-weight: bold; color: #FFD700; padding: 12px 0 4px 0;"
        )
        self.concept_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.concept_label)

        self.subtitle_label = QLabel()
        self.subtitle_label.setStyleSheet(
            "font-size: 14px; font-style: italic; color: #888; padding-bottom: 12px;"
        )
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.subtitle_label)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet("color: #333; margin: 4px 0 12px 0;")
        layout.addWidget(sep)

        self.stack = QStackedWidget()

        self.list_page = QWidget()
        list_layout = QVBoxLayout()
        list_layout.setContentsMargins(0, 0, 0, 0)

        self.subtopic_list = QListWidget()
        self.subtopic_list.setStyleSheet("""
            QListWidget {
                font-size: 16px; border: 1px solid #FFD700;
                border-radius: 6px; padding: 4px;
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
        self.subtopic_list.itemClicked.connect(self._on_subtopic_clicked)
        self.subtopic_list.itemActivated.connect(self._on_subtopic_activated)
        list_layout.addWidget(self.subtopic_list)

        preview_sep = QFrame()
        preview_sep.setFrameShape(QFrame.Shape.HLine)
        preview_sep.setStyleSheet("color: #444; margin: 8px 0;")
        list_layout.addWidget(preview_sep)

        desc_title = QLabel(self.service._("description"))
        desc_title.setStyleSheet(
            "font-size: 13px; color: #888; font-weight: bold; padding-bottom: 4px;"
        )
        list_layout.addWidget(desc_title)

        self.desc_preview = QTextBrowser()
        self.desc_preview.setStyleSheet("""
            QTextBrowser {
                font-size: 14px; border: none;
                background-color: transparent; color: #ccc;
            }
        """)
        self.desc_preview.setMaximumHeight(160)
        list_layout.addWidget(self.desc_preview)

        self.list_page.setLayout(list_layout)
        self.stack.addWidget(self.list_page)

        self.detail_page = QWidget()
        detail_layout = QVBoxLayout()
        detail_layout.setContentsMargins(0, 0, 0, 0)

        back_to_list_btn = QPushButton("\u2190  " + self.service._("topics"))
        back_to_list_btn.setStyleSheet("""
            QPushButton {
                text-align: left; border: none; background: transparent;
                font-size: 14px; color: #888; padding: 4px 0;
            }
            QPushButton:hover { color: #FFD700; }
        """)
        back_to_list_btn.clicked.connect(self._show_list)
        detail_layout.addWidget(back_to_list_btn)

        self.detail_title = QLabel()
        self.detail_title.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #FFD700; padding: 8px 0;"
        )
        self.detail_title.setWordWrap(True)
        detail_layout.addWidget(self.detail_title)

        self.detail_browser = QTextBrowser()
        self.detail_browser.setStyleSheet("""
            QTextBrowser {
                font-size: 15px; border: none;
                background-color: transparent; color: #ccc;
            }
        """)
        self.detail_browser.setOpenExternalLinks(False)
        detail_layout.addWidget(self.detail_browser)

        self.playground_btn = QPushButton("\u25b6  " + self.service._("playground"))
        self.playground_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 12px 24px; margin-top: 8px;
                background-color: transparent; color: #FFD700;
                border: 2px solid #FFD700; border-radius: 8px; font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FFD700; color: #1a1a2e;
            }
        """)
        self.playground_btn.clicked.connect(self._open_playground)
        self.playground_btn.setVisible(False)
        detail_layout.addWidget(self.playground_btn)

        self.detail_page.setLayout(detail_layout)
        self.stack.addWidget(self.detail_page)

        layout.addWidget(self.stack)
        self.setLayout(layout)

    def show_topic(self, concept_id: str) -> None:
        self.current_concept_id = concept_id
        self.content = get_content(concept_id)
        if not self.content or not self.content.subtopics:
            self.concept_label.setText(self.service._("concept_not_found"))
            return

        name_display = {
            "arithmetic": "Arithmetic",
            "aritmatika": "Aritmatika",
            "algebra": "Algebra",
            "aljabar": "Aljabar",
        }.get(concept_id, concept_id.replace("-", " ").title())
        self.concept_label.setText(name_display)
        self.subtitle_label.setText(self.service._("select_topic"))
        self.subtopics = self.content.subtopics

        locale = self.service.locale if hasattr(self.service, "locale") else "en"
        self.subtopic_list.clear()
        for i, st in enumerate(self.subtopics):
            title = st.title.get(locale, st.title.get("en", ""))
            item = QListWidgetItem(f"  {title}")
            item.setData(Qt.ItemDataRole.UserRole, i)
            self.subtopic_list.addItem(item)

        if self.subtopics:
            self.subtopic_list.setCurrentRow(0)
            self._update_preview(self.subtopics[0])

        self._show_list()

    def _show_list(self) -> None:
        self._current_detail_subtopic = None
        self.stack.setCurrentIndex(0)

    def _show_detail(self) -> None:
        self.stack.setCurrentIndex(1)

    def _update_preview(self, subtopic: SubTopic) -> None:
        locale = self.service.locale if hasattr(self.service, "locale") else "en"
        desc = subtopic.description.get(locale, subtopic.description.get("en", ""))
        self.desc_preview.setText(desc)

    def _on_subtopic_clicked(self, item: QListWidgetItem) -> None:
        row = item.data(Qt.ItemDataRole.UserRole)
        if row is not None and row < len(self.subtopics):
            subtopic = self.subtopics[row]
            self._current_detail_subtopic = subtopic
            self._update_preview(subtopic)
            self._render_detail(subtopic)

    def _on_subtopic_activated(self, item: QListWidgetItem) -> None:
        row = item.data(Qt.ItemDataRole.UserRole)
        if row is not None and row < len(self.subtopics):
            subtopic = self.subtopics[row]
            self._current_detail_subtopic = subtopic
            self._update_preview(subtopic)
            self._render_detail(subtopic)

    def _render_detail(self, subtopic: SubTopic) -> None:
        locale = self.service.locale if hasattr(self.service, "locale") else "en"
        self.detail_title.setText(
            subtopic.title.get(locale, subtopic.title.get("en", ""))
        )

        html_parts = []
        html_parts.append(
            "<p style='font-size:16px; font-weight:bold; color:#aaa; "
            "margin: 12px 0 8px 0; letter-spacing:1px;'>"
            + self.service._("examples").upper()
            + "</p>"
        )

        expl = subtopic.explanation.get(locale, subtopic.explanation.get("en", ""))
        expl_lines = [ln.strip() for ln in expl.split("\n") if ln.strip()]
        ex_list = subtopic.examples.get(locale, subtopic.examples.get("en", []))
        expl_idx = 0

        html_parts.append("<div style='margin-top:4px;'>")
        for ex in ex_list:
            if ex == "":
                html_parts.append("<div style='height:16px;'></div>")
            else:
                html_parts.append(
                    "<div style='color:#888; padding:2px 0;'>"
                    + ex.replace("\n", "<br>")
                    + "</div>"
                )
                if expl_idx < len(expl_lines):
                    html_parts.append(
                        "<div style='font-style:italic; color:#aaa; "
                        "padding:0 0 4px 16px;'>"
                        + expl_lines[expl_idx].replace("\n", "<br>")
                        + "</div>"
                    )
                    expl_idx += 1
        html_parts.append("</div>")

        if subtopic.playground:
            html_parts.append("<div style='height:16px;'></div>")
            html_parts.append(
                "<p style='font-size:16px; font-weight:bold; color:#aaa; "
                "margin: 8px 0; letter-spacing:1px;'>"
                + self.service._("playground").upper()
                + "</p>"
            )
            html_parts.append(
                "<div style='font-size:14px; color:#FFD700; font-style:italic;'>"
                + self.service._("press_enter_playground")
                + "</div>"
            )

        self.detail_browser.setHtml("\n".join(html_parts))

        if subtopic.playground:
            self.playground_btn.setVisible(True)
            self._current_playground = subtopic.playground
        else:
            self.playground_btn.setVisible(False)
            self._current_playground = None

        self._show_detail()

    def _open_playground(self) -> None:
        if self._current_playground:
            locale = self.service.locale if hasattr(self.service, "locale") else "en"
            dlg = PlaygroundDialog(self._current_playground, locale, self)
            dlg.exec()

    def _go_back(self) -> None:
        if self.stack.currentIndex() == 1:
            self._show_list()
        else:
            self.app.go_home()

    def keyPressEvent(self, event) -> None:  # noqa: N802
        if event.key() == Qt.Key.Key_Escape:
            self._go_back()
        elif event.key() == Qt.Key.Key_Tab:
            if self.stack.currentIndex() == 1:
                self._show_list()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if self.stack.currentIndex() == 0:
                item = self.subtopic_list.currentItem()
                if item:
                    self._on_subtopic_activated(item)
            elif self.stack.currentIndex() == 1 and self.playground_btn.isVisible():
                self._open_playground()
        else:
            super().keyPressEvent(event)
