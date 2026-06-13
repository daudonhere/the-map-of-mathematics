# AGENTS.md - The Map of Mathematics

## Entry Points

| Command | What runs |
|---|---|
| `python -m mathverse` | TUI launcher (Rich + raw tty) -> Terminal (Rich) or Desktop (PyQt6) |
| `python -m mathverse --lang en` | TUI launcher in English |
| `python src/mathverse/cli/commands/{explore,search,visualize}.py` | Standalone Typer commands (not wired to `__main__`; broken - no seeding) |

Routing in `src/mathverse/__main__.py`: extracts `--lang en|id`, dispatches to launcher. After launcher, loops: browser returns `"back"` → re-enter launcher; browser returns `None` → exit.

## Architecture

- `core/` = domain logic (models, repository, service, graph builder). MUST NOT import from `cli/` or `gui/`.
- `cli/` and `gui/` both depend on `core/` only.
- `core/seed.py` populates the in-memory `Repository` with 28 `MathConcept` entries (14 EN + 14 ID, each with `locale: "en"` or `"id"`). `seed_repo()` calls both `seed_repo_en()` and `seed_repo_id()`.
- `core/i18n.py` provides bilingual UI labels (`t(key, locale) -> str`). `MapService._()` shortcut method uses current locale.
- `.gitignore` lists `AGENTS.md` itself - changes to this file won't appear in `git diff` unless staged manually.
- `cli/commands/` contains Typer functions (`explore_cmd`, `search_cmd`, `visualize_cmd`) but no Typer app registers them - they are callable directly but not reachable from `python -m mathverse`.

## Quirks & Discrepancies

- `src/mathverse/app.py` does **not exist** (listed in old docs; the file was never created).
- `tests/test_cli/` and `tests/test_gui/` have only `__init__.py` - actual tests exist only under `tests/test_core/`.

## Dev Commands

```bash
ruff check .              # lint
ruff format .             # format
pytest tests/ -v          # run all tests (only test_core/ has tests)
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

## Testing

- `conftest.py` provides `sample_repo` fixture (4 concepts with relations).
- Typer `CliRunner` not used in tests yet.
- Kivy tests would need `kivy.clock` + mocking (not yet implemented).

## Launcher Details (`src/mathverse/tui/launcher.py`)

### Key handling
- `_read_key()` uses `os.read(fd, 1)` (bypasses Python buffering) + `select.select` with 100ms timeout for escape sequences. Arrow keys → `"up"`/`"down"`, Enter → `"enter"`, Esc → `"esc"`, `q` → `"q"`.
- Cursor hidden at launcher start via `\x1b[?25l`, restored in `finally`.

### Rendering
- `_render()` uses `\x1b[2J\x1b[H` (clear + home) each frame.
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
- `_read_input()` legacy for playground mode (not used in current playground; `_read_input_at_cursor` used instead).

### Esc behavior — ALL screens
| Screen | Esc | Tab |
|---|---|---|
| Launcher | Exit app | — |
| Browser list | Exit app | Back to launcher |
| Browser detail | Exit app | Back to list |
| Topic list | Exit app | Back to browser |
| Topic detail | Exit app | Back to list |
| Playground input | Exit app | Exit app |
| Playground feedback | Exit app | Exit app |

### Content (`src/mathverse/core/content.py`)
- `SubTopic` dataclass: `title` (dict[str,str]), `description` (dict[str,str]), `explanation` (dict[str,str]), `examples` (dict[str,list[str]]), `playground` (str | None).
- `TopicContent` grouped by concept_id via `get_content()`.
- Currently populated: Arithmetic (9 sub-topics), Algebra (9 sub-topics).
- Registered under both EN and ID concept IDs (e.g. `"algebra"` and `"aljabar"` share same subtopic list).
- Playground IDs: `basic_ops`, `powers`, `mental_math`, `properties`, `number_types`, `factors`, `ratios`, `percentages`, `number_theory`, `expressions`, `equations`, `systems`, `polynomials`, `factoring`, `quadratics`, `functions`, `inequalities`, `exponents_logs`. See `_gen_question()` in topic_screen.py for implementations.
- `# ruff: noqa: RUF001` for math symbols (×, −, etc.).

## Content Pattern — Arithmetic Template

Use this exact pattern when adding new topics (Geometry, Trigonometry, etc.). Arithmetic is the reference.

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
_my_topic_subtopics = [SubTopic(...), SubTopic(...), ...]  # 9 subtopics
_reg("topic_en", _my_topic_subtopics)
_reg("topic_id", _my_topic_subtopics)
```

### Playground Registration

In `topic_screen.py`, `_gen_question()` function's `if/elif` chain — add a new `elif pid == "new_id":` block returning `(question_text, correct_answer, max_value)`.

### Fonts
- STIX Two Text OTF fonts in `gui/fonts/` for scientific typesetting, loaded via `QFontDatabase`.
