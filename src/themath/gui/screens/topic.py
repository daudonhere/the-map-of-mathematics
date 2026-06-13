from __future__ import annotations

import math
import random

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

from themath.core.content import SubTopic, get_content
from themath.core.service import MapService

BANNER_LINES = [
    "████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ████████╗██╗  ██╗",
    "╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║",
    "   ██║   ███████║█████╗      ██╔████╔██║███████║   ██║   ███████║",
    "   ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║",
    "   ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║",
    "   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝",
]


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
            "font-size: 22px; font-weight: bold; color: #00d4ff; padding-bottom: 4px;"
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
                border: 1px solid #0f3460; border-radius: 6px;
            }
            QLineEdit:focus { border-color: #00d4ff; }
        """)
        self.answer_input.returnPressed.connect(self._check_answer)
        input_layout.addWidget(self.answer_input)

        submit_btn = QPushButton("OK")
        submit_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px; padding: 10px 24px;
                background-color: #0f3460; color: #f0f0f0;
                border: none; border-radius: 6px;
            }
            QPushButton:hover { background-color: #1a5276; }
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
                background-color: #00d4ff; color: #1a1a2e;
                border: none; border-radius: 6px; font-weight: bold;
            }
            QPushButton:hover { background-color: #00b4d8; }
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
        self.question, self.answer_str, _ = _gen_question(self.playground)
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


def _gen_question(playground: str) -> tuple[str, str, float]:
    if playground == "basic_ops":
        ops = [
            ("+", lambda a, b: a + b),
            ("\u2212", lambda a, b: a - b),
            ("\u00d7", lambda a, b: a * b),
        ]
        op_sym, op_fn = random.choice(ops)
        if op_sym == "\u00d7":
            a = random.randint(2, 12)
            b = random.randint(2, 12)
        else:
            a = random.randint(10, 99)
            b = random.randint(1, 50)
        if op_sym == "\u2212" and a < b:
            a, b = b, a
        ans = op_fn(a, b)
        q = f"{a} {op_sym} {b} = ?"
        return q, str(ans), ans

    elif playground == "powers":
        kind = random.choice(["square", "cube", "sqrt", "cbrt"])
        if kind == "square":
            n = random.randint(2, 15)
            ans = n * n
            return f"{n}\u00b2 = ?", str(ans), ans
        elif kind == "cube":
            n = random.randint(2, 6)
            ans = n * n * n
            return f"{n}\u00b3 = ?", str(ans), ans
        elif kind == "sqrt":
            n = random.randint(2, 12)
            ans = n * n
            return f"\u221a{ans} = ?", str(n), n
        else:
            n = random.randint(2, 4)
            ans = n * n * n
            return f"\u221b{ans} = ?", str(n), n

    elif playground == "mental_math":
        kind = random.choice(["comp", "double", "eleven", "near100"])
        if kind == "comp":
            a = random.randint(95, 99)
            b = random.randint(10, 50)
            ans = a + b
            return f"{a} + {b} = ?", str(ans), ans
        elif kind == "double":
            a = random.choice([25, 35, 45, 55, 65])
            b = random.choice([12, 14, 16, 18])
            ans = a * b
            return f"{a} \u00d7 {b} = ?", str(ans), ans
        elif kind == "eleven":
            a = random.randint(11, 99)
            ans = a * 11
            return f"{a} \u00d7 11 = ?", str(ans), ans
        else:
            a = random.randint(90, 99)
            b = random.randint(90, 99)
            ans = a * b
            return f"{a} \u00d7 {b} = ?", str(ans), ans

    elif playground == "properties":
        props = [
            ("commutative", lambda a, b: a + b == b + a),
            ("commutative", lambda a, b: a * b == b * a),
            ("associative", lambda a, b, c: (a + b) + c == a + (b + c)),
            ("associative", lambda a, b, c: (a * b) * c == a * (b * c)),
            ("distributive", lambda a, b, c: a * (b + c) == a * b + a * c),
        ]
        choice = random.choice(props)
        if choice[0] in ("commutative",):
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            q = f"Property shown: {a} + {b} = {b} + {a}"
            return q, choice[0], 0.0
        elif choice[0] == "associative":
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            c = random.randint(2, 8)
            q = f"Property shown: ({a} + {b}) + {c} = {a} + ({b} + {c})"
            return q, choice[0], 0.0
        elif choice[0] == "distributive":
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(2, 6)
            q = f"Property shown: {a} \u00d7 ({b} + {c}) = {a}\u00d7{b} + {a}\u00d7{c}"
            return q, choice[0], 0.0

    elif playground == "number_types":
        kind = random.choice(["prime", "square", "even", "odd"])
        if kind == "prime":
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
            compos = [4, 6, 8, 9, 10, 12, 14, 15, 16]
            ans = "prime"
            n = random.choice(primes)
            distract = random.choice(compos)
            if random.randint(0, 1):
                q = f"Is {n} prime or composite?"
                return q, ans, 0.0
            else:
                q = f"Is {distract} prime or composite?"
                return q, "composite", 0.0
        elif kind == "square":
            sq = random.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
            q = f"Which number squared equals {sq}?"
            ans = int(sq**0.5)
            return q, str(ans), ans
        elif kind == "even":
            n = random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
            q = f"Is {n} even or odd?"
            return q, "even", 0.0
        elif kind == "odd":
            n = random.choice([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
            q = f"Is {n} even or odd?"
            return q, "odd", 0.0

    elif playground == "factors":
        pairs = [
            (4, 6),
            (6, 8),
            (3, 4),
            (5, 6),
            (4, 5),
            (6, 10),
            (5, 7),
            (8, 10),
            (8, 12),
            (12, 18),
            (15, 25),
            (6, 9),
            (10, 15),
            (14, 21),
            (16, 24),
            (9, 15),
        ]
        kind = random.choice(["gcf", "lcm"])
        if kind == "gcf":
            a, b = random.choice(pairs)
            ans = math.gcd(a, b)
            q = f"GCF of {a} and {b} = ?"
            return q, str(ans), ans
        else:
            a, b = random.choice(pairs)
            ans = a * b // math.gcd(a, b)
            q = f"LCM of {a} and {b} = ?"
            return q, str(ans), ans

    elif playground == "ratios":
        kind = random.choice(["simplify", "find_part"])
        if kind == "simplify":
            pairs = [(6, 8), (10, 15), (12, 18), (8, 12), (14, 21), (9, 12)]
            a, b = random.choice(pairs)
            g = math.gcd(a, b)
            q = f"Simplify ratio {a}:{b} = ?"
            ans = f"1:{b // g}" if g == a else f"{a // g}:{b // g}"
            return q, ans, 0.0
        else:
            a, b = random.choice([(2, 3), (3, 5), (4, 7), (5, 8), (1, 4), (3, 7)])
            total = random.choice([30, 40, 50, 60, 70, 80])
            if (a + b) > total:
                total = (a + b) * random.randint(2, 5)
            part_b = total // (a + b) * b
            q = f"Ratio {a}:{b}, total {total}. Value of larger part = ?"
            return q, str(part_b), part_b

    elif playground == "percentages":
        kind = random.choice(["of", "of_rev", "change"])
        if kind == "of":
            pct = random.choice([10, 20, 25, 30, 40, 50, 60, 75])
            num = random.choice([40, 60, 80, 100, 120, 200, 300])
            ans = num * pct // 100
            q = f"What is {pct}% of {num}?"
            return q, str(ans), ans
        elif kind == "of_rev":
            ans = random.choice([10, 20, 25, 30, 40, 50])
            num = random.choice([40, 60, 80, 100, 120, 200])
            pct = num * ans // 100
            q = f"{ans} is what percent of {num}?"
            return q, str(pct), pct
        else:
            old = random.choice([40, 50, 60, 80, 100, 120])
            new = old + random.choice([10, 15, 20, 25, 30])
            change = (new - old) * 100 // old
            q = f"Change from {old} to {new} = ?% increase"
            return q, str(change), change

    elif playground == "number_theory":
        kind = random.choice(["mod", "digits", "factorial"])
        if kind == "mod":
            a = random.randint(10, 30)
            b = random.choice([3, 4, 5, 6, 7, 8, 9])
            ans = a % b
            q = f"{a} mod {b} = ?"
            return q, str(ans), ans
        elif kind == "digits":
            n = random.randint(100, 999)
            s = sum(int(d) for d in str(n))
            q = f"Sum of digits of {n} = ?"
            return q, str(s), s
        else:
            n = random.choice([4, 5, 6, 7])
            ans = math.factorial(n)
            q = f"{n}! = ?"
            return q, str(ans), ans

    elif playground == "expressions":
        a = random.randint(2, 8)
        b = random.randint(1, 10)
        x = random.randint(1, 6)
        kind = random.choice(["linear", "quad"])
        if kind == "linear":
            ans = a * x + b
            q = f"If x = {x}, evaluate {a}x + {b}"
            return q, str(ans), ans
        else:
            c = random.randint(1, 5)
            ans = a * x * x + b * x + c
            q = f"If x = {x}, evaluate {a}x\u00b2 + {b}x + {c}"
            return q, str(ans), ans

    elif playground == "equations":
        a = random.randint(2, 6)
        b = random.choice([3, 5, 7, 9, 11, 13])
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q = f"Solve: {a}x + {b} = {c}"
        return q, str(ans), ans

    elif playground == "systems":
        pairs = [
            ((2, 3), (1, -1)),
            ((3, 5), (2, -3)),
            ((2, -1), (1, 2)),
            ((3, 2), (1, -1)),
            ((4, 1), (1, -2)),
        ]
        (a, b), (d, e) = random.choice(pairs)
        x = random.randint(2, 5)
        y = random.randint(1, 4)
        c1 = a * x + b * y
        c2 = d * x + e * y
        q = f"Solve:\n{a}x + {b}y = {c1}\n{d}x + {e}y = {c2}\nEnter x value"
        return q, str(x), x

    elif playground == "polynomials":
        kind = random.choice(["eval", "add"])
        if kind == "eval":
            a = random.randint(1, 5)
            b = random.randint(1, 6)
            x = random.randint(1, 4)
            ans = a * x + b
            q = f"If P(x) = {a}x + {b}, find P({x})"
            return q, str(ans), ans
        else:
            a, b = random.randint(1, 4), random.randint(1, 4)
            c, d = random.randint(1, 4), random.randint(1, 4)
            x = random.randint(1, 3)
            ans = (a + c) * x + (b + d)
            q = f"({a}x + {b}) + ({c}x + {d}) at x={x} = ?"
            return q, str(ans), ans

    elif playground == "factoring":
        pairs = [(2, 3), (3, 5), (2, 5), (3, 4), (2, 7), (3, 2), (4, 3), (5, 2)]
        a, b = random.choice(pairs)
        c = a * b
        d = a + b
        q = f"One factor of x\u00b2 + {d}x + {c} is (x + {a}). What is the other?"
        return q, str(b), b

    elif playground == "quadratics":
        roots = [(2, 3), (3, 5), (2, 5), (1, 4), (3, 2), (4, 3), (2, 7), (3, 7)]
        r1, r2 = random.choice(roots)
        ans = r1 if random.randint(0, 1) else r2
        q = f"Solve (x - {r1})(x - {r2}) = 0. Give one root."
        return q, str(ans), ans

    elif playground == "functions":
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        x = random.randint(1, 6)
        ans = a * x + b
        q = f"If f(x) = {a}x + {b}, find f({x})"
        return q, str(ans), ans

    elif playground == "inequalities":
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = a * random.randint(3, 8) + b
        ans = (c - b) // a
        q = f"Solve: {a}x + {b} > {c}. Enter smallest integer solution."
        return q, str(ans + 1), ans + 1

    elif playground == "exponents_logs":
        kind = random.choice(["exp", "log"])
        if kind == "exp":
            base = random.choice([2, 3, 4, 5])
            exp = random.choice([2, 3, 4])
            ans = base**exp
            q = f"Evaluate: {base}^{exp} = ?"
            return q, str(ans), ans
        else:
            base = random.choice([2, 3, 4, 5])
            exp = random.choice([2, 3, 4])
            val = base**exp
            q = f"log_{base}({val}) = ?"
            ans = exp
            return q, str(ans), ans

    return ("?", "0", 0.0)


class _BannerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        for line in BANNER_LINES:
            label = QLabel(line)
            label.setStyleSheet(
                "font-size: 14px; font-family: monospace; color: #00d4ff;"
            )
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
        self.setLayout(layout)


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
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 16, 40, 16)
        layout.setSpacing(0)

        self.back_btn = QPushButton("\u2190  " + self.service._("back"))
        self.back_btn.setStyleSheet("""
            QPushButton {
                text-align: left; border: none;
                font-size: 14px; color: #888; padding: 4px 0;
            }
            QPushButton:hover { color: #f0f0f0; }
        """)
        self.back_btn.clicked.connect(self._go_back)
        layout.addWidget(self.back_btn)

        self.banner = _BannerWidget()
        layout.addWidget(self.banner)

        self.tagline = QLabel("For minds losing their edge")
        self.tagline.setStyleSheet("""
            font-size: 14px; font-style: italic;
            color: #666; padding: 4px 0 8px 0;
        """)
        self.tagline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.tagline)

        self.concept_label = QLabel()
        self.concept_label.setStyleSheet("""
            font-size: 28px; font-weight: bold;
            color: #00d4ff; padding: 4px 0 12px 0;
        """)
        self.concept_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.concept_label)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet("color: #333; margin: 4px 0 12px 0;")
        layout.addWidget(sep)

        self.stack = QStackedWidget()

        # Page 0: List view
        self.list_page = QWidget()
        list_layout = QVBoxLayout()
        list_layout.setContentsMargins(0, 0, 0, 0)

        self.subtopic_list = QListWidget()
        self.subtopic_list.setStyleSheet("""
            QListWidget {
                font-size: 16px; border: none;
                background-color: transparent;
                outline: none;
            }
            QListWidget::item {
                padding: 8px 12px;
                border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #0f3460;
                color: #00d4ff;
            }
            QListWidget::item:hover {
                background-color: #16213e;
            }
        """)
        self.subtopic_list.itemClicked.connect(self._on_subtopic_clicked)
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
                background-color: transparent;
                color: #ccc;
            }
        """)
        self.desc_preview.setMaximumHeight(160)
        list_layout.addWidget(self.desc_preview)

        self.list_page.setLayout(list_layout)
        self.stack.addWidget(self.list_page)

        # Page 1: Detail view
        self.detail_page = QWidget()
        detail_layout = QVBoxLayout()
        detail_layout.setContentsMargins(0, 0, 0, 0)

        back_to_list_btn = QPushButton("\u2190  " + self.service._("topics"))
        back_to_list_btn.setStyleSheet("""
            QPushButton {
                text-align: left; border: none;
                font-size: 14px; color: #888; padding: 4px 0;
            }
            QPushButton:hover { color: #f0f0f0; }
        """)
        back_to_list_btn.clicked.connect(self._show_list)
        detail_layout.addWidget(back_to_list_btn)

        self.detail_title = QLabel()
        self.detail_title.setStyleSheet("""
            font-size: 22px; font-weight: bold;
            color: #f0f0f0; padding: 8px 0;
        """)
        self.detail_title.setWordWrap(True)
        detail_layout.addWidget(self.detail_title)

        self.detail_browser = QTextBrowser()
        self.detail_browser.setStyleSheet("""
            QTextBrowser {
                font-size: 15px; border: none;
                background-color: transparent;
                color: #ccc;
            }
        """)
        self.detail_browser.setOpenExternalLinks(False)
        detail_layout.addWidget(self.detail_browser)

        self.playground_btn = QPushButton("\u25b6  " + self.service._("playground"))
        self.playground_btn.setStyleSheet("""
            QPushButton {
                font-size: 15px; padding: 12px 24px;
                background-color: #0f3460; color: #00d4ff;
                border: 1px solid #00d4ff; border-radius: 8px;
                font-weight: bold; margin-top: 8px;
            }
            QPushButton:hover {
                background-color: #16213e;
                color: #00ff88;
                border-color: #00ff88;
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
                "<div style='font-size:14px; color:#00d4ff; font-style:italic;'>"
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
