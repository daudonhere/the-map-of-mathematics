from __future__ import annotations

# ruff: noqa: RUF001
import math


def _build_quadratic_chart_lines(
    content_lines: list,
    a: int,
    b: int,
    c: int,
    inner_w: int,
    locale: str,
) -> None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    sign_b = "+" if b >= 0 else "\u2212"
    sign_c = "+" if c >= 0 else "\u2212"
    eq = f"y = {a}x\u00b2 {sign_b} {abs(b)}x {sign_c} {abs(c)}"
    content_lines.append((eq, "bold"))
    content_lines.append((None, None))

    D = b * b - 4 * a * c  # noqa: N806
    D_str = str(D) if D >= 0 else _("negative", "negatif")  # noqa: N806
    if b >= 0:
        formula = _(
            f"x = (\u2212{b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
            f"x = (\u2212{b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
        )
    else:
        formula = _(
            f"x = ({-b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
            f"x = ({-b} \u00b1 \u221a{D_str}) / (2\u00b7{a})",
        )
    content_lines.append((formula, None))

    if D >= 0:
        sqrt_d = math.sqrt(D)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        x1_str = f"{round(x1)}" if abs(x1 - round(x1)) < 0.001 else f"{x1:.2f}"
        x2_str = f"{round(x2)}" if abs(x2 - round(x2)) < 0.001 else f"{x2:.2f}"
        root_line = _(f"  x = {x1_str}, x = {x2_str}", f"  x = {x1_str}, x = {x2_str}")
        content_lines.append((root_line, None))
    content_lines.append((None, None))

    vx = -b / (2 * a)
    col_w = 2
    y_label_w = 5
    max_plot = inner_w - y_label_w - 4
    max_cols = max(max_plot // col_w, 9)
    n = min(max_cols, 15)
    n = n - 1 if n % 2 == 0 else n
    half = n // 2
    cx = round(vx)
    xs = [cx - half + i for i in range(n)]
    ys = [a * x * x + b * x + c for x in xs]
    y_vals = [*ys, 0]
    y_min = min(y_vals) - 1
    y_max = max(y_vals) + 1
    if abs(y_max - y_min) < 0.001:
        y_min -= 1
        y_max += 1
    y_range = y_max - y_min

    chart_h = 11

    def row_of_y(y: float) -> float:
        return (y_max - y) / y_range * (chart_h - 1)

    def y_of_row(r: float) -> float:
        return y_max - r / (chart_h - 1) * y_range

    zero_row = row_of_y(0)
    plot_w = n * col_w
    total_chart = y_label_w + 4 + plot_w
    left_pad = max(1, (inner_w - total_chart) // 2)

    border_top = (
        " " * left_pad + " " * y_label_w + " \u250c" + "\u2500" * plot_w + "\u2510"
    )
    content_lines.append((border_top, None))

    for row_idx in range(chart_h):
        y_val = y_of_row(row_idx)
        y_label = f"{y_val:>{y_label_w}.0f}"
        cells: list[str] = []
        for x_val in xs:
            y_curve = a * x_val * x_val + b * x_val + c
            cr = row_of_y(y_curve)
            on_curve = abs(row_idx - cr) < 0.55
            on_x_axis = abs(row_idx - zero_row) < 0.3
            if on_curve:
                cells.append("**")
            elif on_x_axis and x_val == 0:
                cells.append("\u253c\u253c")
            elif on_x_axis:
                cells.append("\u2500\u2500")
            elif x_val == 0:
                cells.append("\u2502\u2502")
            else:
                cells.append("  ")
        row_str = "".join(cells)
        row_line = " " * left_pad + y_label + " \u2502" + row_str + "\u2502"
        content_lines.append((row_line, None))

    border_bot = (
        " " * left_pad + " " * y_label_w + " \u2514" + "\u2500" * plot_w + "\u2518"
    )
    content_lines.append((border_bot, None))

    x_parts: list[str] = []
    for x in xs:
        s = str(x)
        if len(s) == 1:
            x_parts.append(" " + s)
        else:
            x_parts.append(s)
    x_label_line = " " * left_pad + " " * y_label_w + "  " + "".join(x_parts)
    content_lines.append((x_label_line, None))


def _build_linear_chart_lines(
    content_lines: list,
    m: int,
    b_val: int,
    inner_w: int,
    locale: str,
) -> None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    sign_b = "+" if b_val >= 0 else "\u2212"
    if b_val >= 0:
        eq = f"f(x) = {m}x {sign_b} {abs(b_val)}"
    else:
        eq = f"f(x) = {m}x {sign_b} {abs(b_val)}"
    content_lines.append((eq, "bold"))
    content_lines.append((None, None))

    half = 4
    xs = list(range(-half, half + 1))
    x_cols = len(xs)
    ys = [m * x + b_val for x in xs]
    y_vals = [*ys, 0]
    y_min = min(y_vals) - 1
    y_max = max(y_vals) + 1
    if abs(y_max - y_min) < 0.001:
        y_min -= 1
        y_max += 1
    y_range = y_max - y_min

    col_w = 2
    y_label_w = 5
    chart_h = 11
    plot_w = x_cols * col_w
    total_chart = y_label_w + 4 + plot_w
    left_pad = max(1, (inner_w - total_chart) // 2)

    def row_of_y(y: float) -> float:
        return (y_max - y) / y_range * (chart_h - 1)

    zero_row = row_of_y(0)

    border_top = (
        " " * left_pad + " " * y_label_w + " \u250c" + "\u2500" * plot_w + "\u2510"
    )
    content_lines.append((border_top, None))

    for row_idx in range(chart_h):
        y_val = y_max - row_idx * y_range / (chart_h - 1)
        y_label = f"{y_val:>{y_label_w}.0f}"
        cells: list[str] = []
        for x_val in xs:
            y_curve = m * x_val + b_val
            cr = row_of_y(y_curve)
            on_curve = abs(row_idx - cr) < 0.55
            on_x_axis = abs(row_idx - zero_row) < 0.3
            if on_curve:
                cells.append("**")
            elif on_x_axis and x_val == 0:
                cells.append("\u253c\u253c")
            elif on_x_axis:
                cells.append("\u2500\u2500")
            elif x_val == 0:
                cells.append("\u2502\u2502")
            else:
                cells.append("  ")
        row_str = "".join(cells)
        row_line = " " * left_pad + y_label + " \u2502" + row_str + "\u2502"
        content_lines.append((row_line, None))

    border_bot = (
        " " * left_pad + " " * y_label_w + " \u2514" + "\u2500" * plot_w + "\u2518"
    )
    content_lines.append((border_bot, None))

    x_parts: list[str] = []
    for x in xs:
        s = str(x)
        if len(s) == 1:
            x_parts.append(" " + s)
        else:
            x_parts.append(s)
    x_label_line = " " * left_pad + " " * y_label_w + "  " + "".join(x_parts)
    content_lines.append((x_label_line, None))


def _build_identity_chart_lines(
    content_lines: list,
    playground: str,
    a: int,
    b: int,
    inner_w: int,
    locale: str,
) -> None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    a2, b2 = a * a, b * b
    ab = a * b

    side_label_w = 3
    max_cells = 30
    avail = min(inner_w - 3 - side_label_w, max_cells)
    cw = max(4, avail * a // (a + b))
    rw = max(4, avail - cw)
    if cw + rw > avail:
        if a >= b:
            cw = avail - rw
        else:
            rw = avail - cw
        cw = max(4, cw)
        rw = max(4, rw)
        if cw + rw > avail:
            cw = rw = avail // 2

    body_w = cw + rw + 3
    total_w = body_w + side_label_w
    chart_pad = max(0, (inner_w - total_w) // 2)
    side = " " * chart_pad
    sp = " " * side_label_w

    shade_a2_l = "\u2593" * cw
    shade_ab_l = "\u2591" * cw
    shade_ab_r = "\u2591" * rw
    shade_b2_r = "\u2592" * rw

    content_lines.append((None, None))
    if playground == "perfect_square":
        content_lines.append(
            (_("(a+b)² = a² + 2ab + b²", "(a+b)² = a² + 2ab + b²"), "bold")
        )
        total = a2 + 2 * ab + b2
        side_len = a + b

        content_lines.append((_(f"  a={a}, b={b}", f"  a={a}, b={b}"), None))
        content_lines.append((None, None))

        top_label = side + sp + f"a={a}".center(cw + 1) + f"b={b}".center(rw + 2)
        content_lines.append((top_label, "dim"))
        top = side + sp + "\u250c" + "\u2500" * cw + "\u252c" + "\u2500" * rw + "\u2510"
        content_lines.append((top, None))
        r1 = (
            side
            + "a".center(side_label_w)
            + "\u2502"
            + shade_a2_l
            + "\u2502"
            + shade_ab_r
            + "\u2502"
        )
        content_lines.append((r1, None))
        mid = side + sp + "\u251c" + "\u2500" * cw + "\u253c" + "\u2500" * rw + "\u2524"
        content_lines.append((mid, None))
        r2 = (
            side
            + "b".center(side_label_w)
            + "\u2502"
            + shade_ab_l
            + "\u2502"
            + shade_b2_r
            + "\u2502"
        )
        content_lines.append((r2, None))
        bot = side + sp + "\u2514" + "\u2500" * cw + "\u2534" + "\u2500" * rw + "\u2518"
        content_lines.append((bot, None))
        content_lines.append((None, None))

        content_lines.append(
            (
                f"a² = a\u00d7a = {a}\u00d7{a} = {a2}  |  ab = a\u00d7b = {a}\u00d7{b} = {ab}",
                None,
            )
        )
        content_lines.append(
            (
                f"b² = b\u00d7b = {b}\u00d7{b} = {b2}  |  2ab = 2\u00d7{ab} = {2 * ab}",
                None,
            )
        )
        content_lines.append((None, None))
        content_lines.append(
            (
                _(
                    f"({a}+{b})² = {side_len}² = {total}",
                    f"({a}+{b})² = {side_len}² = {total}",
                ),
                "bold",
            )
        )
        content_lines.append((f"{a2} + {ab} + {ab} + {b2} = {total} \u2713", None))
    else:
        content_lines.append(
            (_("a² − b² = (a−b)(a+b)", "a² − b² = (a−b)(a+b)"), "bold")
        )
        total = a2 - b2

        content_lines.append((_(f"  a={a}, b={b}", f"  a={a}, b={b}"), None))
        content_lines.append((None, None))

        top = side + sp + "\u250c" + "\u2500" * cw + "\u252c" + "\u2500" * rw + "\u2510"
        content_lines.append((top, None))
        r1 = (
            side
            + "a".center(side_label_w)
            + "\u2502"
            + shade_a2_l
            + "\u2502"
            + shade_b2_r
            + "\u2502"
        )
        content_lines.append((r1, None))
        bot = side + sp + "\u2514" + "\u2500" * cw + "\u2534" + "\u2500" * rw + "\u2518"
        content_lines.append((bot, None))
        content_lines.append((None, None))

        diff_a = a - b
        sum_a = a + b
        content_lines.append(
            (_(f"a² = {a}\u00d7{a} = {a2}", f"a² = {a}\u00d7{a} = {a2}"), None)
        )
        content_lines.append(
            (_(f"b² = {b}\u00d7{b} = {b2}", f"b² = {b}\u00d7{b} = {b2}"), None)
        )
        content_lines.append((None, None))
        content_lines.append(
            (
                _(
                    f"a² − b² = {a2} − {b2} = {total}",
                    f"a² − b² = {a2} − {b2} = {total}",
                ),
                None,
            )
        )
        content_lines.append(
            (
                _(
                    f"= ({a}−{b})({a}+{b}) = {diff_a}\u00b7{sum_a} = {total}",
                    f"= ({a}−{b})({a}+{b}) = {diff_a}\u00b7{sum_a} = {total}",
                ),
                "bold",
            )
        )
