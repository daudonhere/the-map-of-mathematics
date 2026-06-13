# AGENTS.md - The Map of Mathematics

## Entry Points

| Command | What runs |
|---|---|
| `python -m mathverse` | TUI launcher (Rich + raw tty) -> Terminal (Rich) or Desktop (PyQt6) |
| `python -m mathverse --lang en` | TUI launcher in English |
| `python src/mathverse/cli/commands/{explore,search,visualize}.py` | Standalone Typer commands (not wired to `__main__`; broken - no seeding) |

Routing in `src/mathverse/__main__.py`: extracts `--lang en|id`, dispatches to launcher. After launcher, loops: browser returns `"back"` → re-enter launcher; browser returns `None` → exit.

## Dev Commands

```bash
ruff check .              # lint
ruff format .             # format
pytest tests/ -v          # run all tests
pytest tests/test_core/   # single package
pip install -e ".[dev]"   # install with dev deps
```

## Style

- `from __future__ import annotations` in every file.
- Double quotes for strings, triple-quotes for docstrings.
- max 88 chars (Ruff default). `ruff.toml` ignores `E501` (Rich markup) and `B008` (Typer function calls in defaults).
- No `print()` in prod - use `rich.print` or `console.print` in CLI, logging elsewhere.
- `pathlib.Path` for filesystem ops.
- Ruff rules: `select = ["E", "F", "I", "N", "W", "UP", "B", "SIM", "ARG", "RUF"]`.
- STIX Two Text OTF fonts bundled in `gui/fonts/` for scientific typesetting - loaded via `QFontDatabase`.
- **Never `git add` or `git commit` or `git push` unless the user explicitly says so.**

## Testing

- `tests/test_core/` (18 tests), `tests/test_cli/` (6 tests), `tests/test_gui/` (22 tests) — total 46.
- `conftest.py` provides `sample_repo` fixture (4 concepts with relations).
- CLI tests use Typer `CliRunner` + `unittest.mock.patch`.

## Chalkboard Theme

- **Launcher**: Black background (`on #000000`) everywhere — no chalkboard.
- **Browser & Topic screens**: Three visual areas:
  - **Header** (banner + subtitle): Black background
  - **Content** (concept list, detail, examples, playground): Dark green chalkboard background (`on #1a3a1a`) enclosed in a box with `┌─┐` top border, `│` side walls, and `└─┘` bottom border. Side padding (`pad = max(2, tw // 20)`) outside the box walls keeps green area from touching terminal edges. Default text is white; styled text uses bright colors (`bold cyan`, `bold yellow`, etc.) on the green background.
  - **Footer** (keybar + credit): Black background
- `chalkboard: bool` and `header_count: int` parameters. `header_count=9` when the MATHVERSE banner is visible (6 banner lines + blank + subtitle + blank + blank), `header_count=0` when terminal is too narrow.
- `_render_detail` in browser.py has no banner, so `header_count=0` — the entire content area gets green chalkboard.

## Launcher Details (`src/mathverse/tui/launcher.py`)

### Key handling
- `_read_key()` uses `os.read(fd, 1)` (bypasses Python buffering) + `select.select` with 100ms timeout for escape sequences. Arrow keys → `"up"`/`"down"`, Enter → `"enter"`, Esc → `"esc"`, `q` → `"q"`.
- Cursor hidden at launcher start via `\x1b[?25l`, restored in `finally`.

### Rendering
- `_render()` uses `\x1b[2J\x1b[H` (clear + home) each frame. Signature: `_render(console, items, current)` — `locale` and `lang_menu` params removed; "Select Language" text no longer rendered.
- Each line is padded to full terminal width with `.ljust(tw)` or `" " * tw` for blanks to overwrite shell decorations.
- Selection highlight (`"reverse"`) only covers the text content (via `rich.text.Text`), not the full line or box walls.
- Keymap bar at bottom line (`end=""` to avoid scroll). Credit `Ⓒ D. Daud Yusup` appended right-aligned on keybar line.
- Menu items wrapped in a solid box (`┌┐│└┘`) with internal padding +6, centered horizontally.
- Banner: **"MATHVERSE"** (77 chars, no spaces, `"bold cyan"`), centered.
- Subtitle: `"For minds losing their edge"`, centered.

### Trimming priority (when terminal too short)
blanks → description → subtitle → banner

### Layout
- 3 blank lines top padding
- 6-line Unicode block banner (77 chars, `"bold cyan"`)
- 1 blank line
- Subtitle `"For minds losing their edge"` (centered, `"italic"`)
- 1 blank line
- Menu items in centered box
- Fill to terminal height
- Keymap bar at bottom with credit

### Browser (`src/mathverse/tui/browser.py`)
- Two views: concept list (all locale-filtered concepts) and concept detail (name, category, description, related list).
- Navigation: arrow keys, Enter, Tab back, Esc exit.
- Related concepts are selectable — Enter navigates to the related concept, Esc exits.
- Same style as launcher: left-aligned, padded to full width, reverse highlight on text only.
- When Enter on a concept that has detailed content (`core/content.py`), launches the topic screen.
- `_render_content()` uses `\x1b[2J\x1b[H` (clear + home) each frame.
- Footer: consistent keybar + `Ⓒ D. Daud Yusup` credit.

### Browser Detail (`src/mathverse/tui/browser.py` `_render_detail`)
- Shown when Enter on a concept WITHOUT topic content but WITH related concepts.
- Same keybar + credit footer.
- Esc exits, Tab goes back to list.
- No banner header — entire content gets green chalkboard background.

## Topic Screen (`src/mathverse/tui/topic_screen.py`)

### Flow
List (↑↓ arrows) → Enter → Detail view → Enter → Playground. Esc exits from ALL screens to launcher. Tab goes back one level.

### List view
- Banner (6-line "MATHVERSE") + centered subtitle + concept name + scrollable subtopic list.
- Preview area (8 lines fixed height) shows `description` (general subtopic overview).
- Footer with consistent keybar + `Ⓒ D. Daud Yusup` credit.

### Detail view
- Banner + subtitle + concept name + subtopic title.
- Each non-blank example line shown in `"dim"` style, immediately followed by its matching `explanation` line in `"italic"`.
- Blank example lines `""` become empty rows (group separators).
- Playground prompt shown at bottom ("Press Enter to start playground").
- Footer with keybar + credit.

### Playground
- **Rendering**: Full `_render_content` cycle with `\x1b[2J\x1b[H` each frame.
- **Layout**: Banner + subtitle → "Playground" → Title (left) + Score (right) → "Question:" / question → `>> ` input prompt → Footer (keybar + credit).
- **Input**: `_read_input_at_cursor()` — reads at pre-positioned cursor, clears/rewrites the `">> "` line each keystroke.
- **Score tracking**: correct/total, right-aligned on same line as subtopic title (left-aligned).
- **Feedback**: Shows user answer, correct answer, CORRECT!/WRONG — press Enter to continue, Esc/Tab to exit.
- `_read_input()` not used in current playground; `_read_input_at_cursor` used instead.

### Esc behavior — ALL screens
| Screen | Esc | Tab |
|---|---|---|
| Launcher | Exit app | — |
| Browser list | Exit app | Back to launcher |
| Browser detail | Exit app | Back to list |
| Topic list | Exit app | Back to browser |
| Topic detail | Exit app | Back to list |
| Playground input | Exit app | Back to topic |
| Playground feedback | Exit app | Back to topic |

### Identity Playgrounds (`_playground_identity` in `tui/playgrounds/identity.py`)
- Two phases: **Exploration** (input a/b, see chart) → **Quiz** (answer questions, no chart).
- Exploration: user enters a/b values (or Enter for random), Tab goes back, Esc exits.
- Chart: proportional box-diagram with `▓░▒` shading, compact (max 30 cells total), labels on outside (side + top).
- `_build_identity_chart_lines()`: compact proportional chart with Unicode shade fill + box-drawing borders.
- `_read_value_chalkboard(fd, tw, label)`: inline chalkboard input with ANSI backgrounds.
- All playground input functions (`_read_input_at_cursor`, `_read_value_chalkboard`): show cursor (`?25h`) before input, hide (`?25l`) after via `finally`.

### Quadratic Playground (`_playground_quadratic` in `tui/playgrounds/quadratic.py`)
- Two phases: **Exploration** (enter a/b/c, see chart) → **Quiz** (solve for one root).
- Chart: 2-char columns, 11 rows, box-drawing border (`┌┐│└┘`), coordinate axes (`──` x-axis, `││` y-axis, `┼┼` origin), curve shown as `**`, y-labels at left edge, x-labels below. Centered in chalkboard via `left_pad`.
- Random values generated immediately and displayed as actual numbers (not `(random)`).
- Quiz: generates integer-root quadratics via x1×x2 approach, bilingual EN/ID.

### Linear Chart Playground (`_playground_functions` in `tui/playgrounds/functions.py`)
- Same chart design as quadratic: 2-char columns, axes, border, centered.
- Exploration: enter slope m and intercept b, see line chart.
- Quiz: evaluate f(x) = mx + b at given x, score tracking.

### Exponents & Logarithms Playground (`_playground_exponents_logs` in `tui/playgrounds/exponents_logs.py`)
- Quiz-only (no chart): randomly mixes exponent questions (`2³ = ?`) and logarithm questions (`log₂(8) = ?`) with Unicode superscripts/subscripts.

### Playground input helpers
- `_read_input_at_cursor(fd, tw)`: reads input at `>> ` prompt with line redraw + cursor show/hide.
- `_read_value_chalkboard(fd, tw, label)`: reads numeric input inside chalkboard with display + cursor show/hide.
- Tab returns `"\r"` → caller returns `0` (go back); Esc returns `None` → caller returns `None` (exit).
- Cursor managed per-function: `\x1b[?25h` on entry, `\x1b[?25l` in `finally` (even on early return).

### Content (`src/mathverse/core/content.py`)
- `SubTopic` dataclass: `title` (dict[str,str]), `description` (dict[str,str]), `explanation` (dict[str,str]), `examples` (dict[str,list[str]]), `playground` (str | None).
- `TopicContent` grouped by concept_id via `get_content()`.
- Currently populated: Arithmetic (9 sub-topics), Algebra (11 sub-topics: Variables & Constants, Algebraic Forms, Algebraic Operations, Factoring, Perfect Square Identity, Difference of Two Squares, Linear Equations, Systems of Linear Equations, Quadratic Equations, Functions, Exponents and Logarithms).
- Registered under both EN and ID concept IDs (e.g. `"algebra"` and `"aljabar"` share same subtopic list).
- Playground IDs: `basic_ops`, `powers`, `mental_math`, `properties`, `number_types`, `factors`, `ratios`, `percentages`, `number_theory`, `variables`, `algebraic_forms`, `algebraic_ops`, `factoring`, `perfect_square`, `diff_squares`, `linear_equations`, `systems_of_equations`, `quadratic`, `functions`, `exponents_logs`. See `_gen_question()` handlers in `core/topics/{topic}.py`.
- `# ruff: noqa: RUF001` for math symbols (×, −, etc.).

## Topic Content

Only **Arithmetic** (9 subtopics) and **Algebra** (11 subtopics) have content. All other concepts (`linear-algebra`, `abstract-algebra`, `boolean-algebra`, `computer-algebra`, `euclidean-geometry`, `differential-geometry`, `trigonometry`, `calculus`, `discrete-mathematics`, `probability-statistics`, `real-analysis`, `complex-analysis`, `topology`, `number-theory`) have empty `subtopics=[]` stubs ready for content.

## Content Pattern

Use Arithmetic as the reference when adding new topics.

### Data Structure Per SubTopic

```python
SubTopic(
    title={"id": "...", "en": "..."},
    description={
        "id": "Deskripsi umum tentang sub-topik ini (1-2 kalimat).",
        "en": "General overview of what this subtopic is about (1-2 sentences).",
    },
    explanation={
        "id": (
            "Penjelasan contoh ke-1, mendeskripsikan konsep yang ditunjukkan contoh.\n"
            "Penjelasan contoh ke-2.\n"
            "Penjelasan contoh ke-n."
        ),
        "en": (
            "Explanation of example 1, describing the concept shown.\n"
            "Explanation of example 2.\n"
            "Explanation of example n."
        ),
    },
    examples={
        "id": [
            "Contoh ke-1",
            "Contoh ke-2",
            "",                    # Empty string = visual separator between groups
            "Contoh ke-3",
        ],
        "en": [
            "Example 1",
            "Example 2",
            "",
            "Example 3",
        ],
    },
    playground="playground_id",   # or None if no playground
)
```

### Rules

1. **`description`** — General subtopic overview. Shown in list view preview (8-line box). 1-2 sentences per locale. Must NOT reference specific examples.

2. **`explanation`** — One line per **non-blank** example. Each line explains the concept that the corresponding example demonstrates. Must NOT just repeat the example text — must be genuinely descriptive/educational. Lines separated by `\n` (last line has no `\n`). Iterated in sync with non-blank examples in `_render_detail()`.

3. **`examples`** — List of strings. Non-blank = example lines. Blank `""` = group separators (rendered as empty rows). Examples should be self-explanatory enough to stand alone, with `explanation` providing the educational context. Each locale list must have identical structure (same blank positions).

4. **`playground`** — String ID matching a handler in `_gen_question()` in topic_screen.py. Set to `None` if no playground available. Must be registered in both EN and ID concept IDs.

5. **Bilingual parity** — Every subtopic must have identical `title`, `description`, `explanation`, and `examples` keys for both `"en"` and `"id"`. Shared subtopic list registered under both concept IDs (e.g. `_reg("algebra", _algebra_subtopics)` + `_reg("aljabar", _algebra_subtopics)`).

6. **Count matching** — `len(non_blank_examples)` must equal `len(explanation_lines)`. Use `pytest` or the validation script to verify.

### Registration

```python
_reg("concept_en", subtopics_list)
_reg("concept_id", subtopics_list)
```

### Fonts
- STIX Two Text OTF fonts in `gui/fonts/` for scientific typesetting, loaded via `QFontDatabase`.

---

## Architecture

- `core/` = domain logic — MUST NOT import from `cli/` or `gui/`.
- `cli/` and `gui/` both depend on `core/` only.
- `core/seed.py` populates in-memory `Repository` with 36 `MathConcept` (18 EN + 18 ID).
- `core/i18n.py` provides bilingual UI labels (`t(key, locale) -> str`).
- `.gitignore` lists `AGENTS.md` — changes won't appear in `git diff` unless staged.
- `cli/commands/` has Typer functions not wired to `__main__`.

### Directory Layout

```
src/mathverse/
├── core/
│   ├── models.py              # MathConcept, SubTopic, TopicContent
│   ├── service.py              # MapService
│   ├── i18n.py                 # bilingual labels
│   ├── seed.py                 # 36 concepts (18 EN + 18 ID)
│   ├── quiz.py                 # gen_question() router → topic modules
│   ├── content.py              # _reg() registry: concept_id → subtopics list
│   └── topics/                 # per-topic modules (14 total)
│       ├── arithmetic.py       # 9 subtopics + quiz handlers
│       ├── algebra/            # 11 subtopics across 6 files
│       ├── geometry.py         # euclidean-geometry + differential-geometry
│       ├── trigonometry.py
│       ├── calculus.py
│       ├── analysis.py         # real-analysis + complex-analysis
│       ├── topology.py
│       ├── number_theory.py
│       ├── probability.py
│       ├── discrete.py
│       ├── linear_algebra.py
│       ├── abstract_algebra.py
│       ├── boolean_algebra.py
│       └── computer_algebra.py
│
├── tui/
│   ├── components/             # rendering helpers (input, chalkboard, charts)
│   ├── screens/                # launcher, browser, topic_screen (list/detail only)
│   └── playgrounds/            # identity, quadratic, functions, exponents_logs
│
└── gui/
    ├── main.py
    ├── components/             # charts (QPainter)
    └── screens/                # splash, home, explore, topic
```

### Data Flow

```
core/quiz.py
  → gen_question(playground, locale) routes to correct topic module

core/topics/{topic}.py
  → exports: subtopics[], gen_question(playground, locale)

core/content.py
  → get_content(concept_id) returns TopicContent with subtopics

tui/playgrounds/{topic}.py
  → imports core/topics/ for chart data
  → imports tui/components/charts for ANSI rendering
  → imports tui/components/input for keyboard
```

### Rules for Adding a New Topic

1. **`core/topics/{topic}.py`** — Create a new module exporting:
   - `subtopics: list[SubTopic]` — SubTopic entries for the topic
   - `gen_question(playground, locale) → (question, answer, max_val) | None` — quiz handler for this topic's playground IDs
2. **Register subtopics** in `core/content.py`: add import and `_reg("en_id", list)` + `_reg("id_id", list)`.
3. **Register quiz** in `core/quiz.py`: add import and add playground IDs to `_PLAYGROUND_MAP`.
4. **Playground** (if has chart exploration): Create `tui/playgrounds/{topic}.py` with the playground controller function. Import chart builders from `tui/components/charts.py`. Update `tui/playgrounds/__init__.py` to import and dispatch.
5. **Chart** (if has chart): Add `_build_{topic}_chart_lines()` to `tui/components/charts.py`. For GUI, add corresponding `QWidget` subclass in `gui/components/charts.py`.
