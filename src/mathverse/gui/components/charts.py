from __future__ import annotations

from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QFont, QPainter, QPen
from PyQt6.QtWidgets import QWidget


class QuadraticChart(QWidget):
    def __init__(self, a: int, b: int, c: int, parent=None):
        super().__init__(parent)
        self.a = a
        self.b = b
        self.c = c
        self.setMinimumSize(300, 220)

    def paintEvent(self, event) -> None:  # noqa: N802, ARG002
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()
        margin = 40
        plot_w = w - 2 * margin
        plot_h = h - 2 * margin

        painter.fillRect(self.rect(), Qt.GlobalColor.transparent)

        n = 15
        half = n // 2
        cx = -self.b / (2.0 * self.a)
        xs = [cx - half + i for i in range(n)]
        ys = [self.a * x * x + self.b * x + self.c for x in xs]
        y_min = min(ys) - 1
        y_max = max(ys) + 1
        y_range = max(abs(y_max - y_min), 1)

        pen_axis = QPen(Qt.GlobalColor.gray, 1)
        painter.setPen(pen_axis)
        zero_y = margin + plot_h * y_max / y_range if y_range != 0 else h // 2
        painter.drawLine(margin, int(zero_y), w - margin, int(zero_y))
        zero_x = margin + plot_w * half / (n - 1)
        painter.drawLine(int(zero_x), margin, int(zero_x), h - margin)

        pen_curve = QPen(Qt.GlobalColor.cyan, 2)
        painter.setPen(pen_curve)
        points: list[QPointF] = []
        for i, _x in enumerate(xs):
            px = margin + plot_w * i / (n - 1)
            py_scaled = (y_max - ys[i]) / y_range
            py = margin + py_scaled * plot_h
            points.append(QPointF(px, py))
        for i in range(1, len(points)):
            painter.drawLine(points[i - 1], points[i])

        painter.end()


class LinearChart(QWidget):
    def __init__(self, m: int, b_val: int, parent=None):
        super().__init__(parent)
        self.m = m
        self.b_val = b_val
        self.setMinimumSize(300, 220)

    def paintEvent(self, event) -> None:  # noqa: N802, ARG002
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()
        margin = 40
        plot_w = w - 2 * margin
        plot_h = h - 2 * margin

        painter.fillRect(self.rect(), Qt.GlobalColor.transparent)

        half = 4
        xs = list(range(-half, half + 1))
        n = len(xs)
        ys = [self.m * x + self.b_val for x in xs]
        y_min = min(ys) - 1
        y_max = max(ys) + 1
        y_range = max(abs(y_max - y_min), 1)

        pen_axis = QPen(Qt.GlobalColor.gray, 1)
        painter.setPen(pen_axis)
        zero_y = margin + plot_h * y_max / y_range if y_range != 0 else h // 2
        painter.drawLine(margin, int(zero_y), w - margin, int(zero_y))
        zero_x = margin + plot_w * half / (n - 1)
        painter.drawLine(int(zero_x), margin, int(zero_x), h - margin)

        pen_curve = QPen(Qt.GlobalColor.cyan, 2)
        painter.setPen(pen_curve)
        points: list[QPointF] = []
        for i, _x in enumerate(xs):
            px = margin + plot_w * i / (n - 1)
            py_scaled = (y_max - ys[i]) / y_range
            py = margin + py_scaled * plot_h
            points.append(QPointF(px, py))
        for i in range(1, len(points)):
            painter.drawLine(points[i - 1], points[i])

        painter.end()


class IdentityDiagram(QWidget):
    def __init__(self, a: int, b: int, is_perfect_square: bool = True, parent=None):
        super().__init__(parent)
        self.a = a
        self.b = b
        self.is_perfect_square = is_perfect_square
        self.setMinimumSize(200, 200)

    def paintEvent(self, event) -> None:  # noqa: N802, ARG002
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()
        margin = 30
        ratio = self.a / max(self.a + self.b, 1)
        total_w = w - 2 * margin
        total_h = h - 2 * margin
        lw = int(total_w * ratio)
        rw = total_w - lw
        lh = total_h
        if not self.is_perfect_square:
            lh = h - 2 * margin

        painter.fillRect(self.rect(), Qt.GlobalColor.transparent)

        pen = QPen(Qt.GlobalColor.white, 2)
        painter.setPen(pen)
        font = QFont()
        font.setPointSize(10)
        painter.setFont(font)

        painter.drawRect(margin, margin, lw, lh)
        painter.drawRect(margin + lw, margin, rw, lh)
        painter.drawText(margin + 4, margin + lh // 2 + 4, f"a² (a={self.a})")
        painter.drawText(margin + lw + 4, margin + lh // 2 + 4, f"b² (b={self.b})")
        painter.drawText(margin + lw // 2 - 8, margin + lh + 16, f"a={self.a}")
        painter.drawText(margin + lw + rw // 2 - 8, margin + lh + 16, f"b={self.b}")

        painter.end()
