# AGENTS.md - The Map of Mathematics

## Entry Points

| Command | What runs |
|---|---|
| `python -m themath` | TUI launcher (Rich + raw tty) -> Terminal (Rich) or Desktop (PyQt6) |
| `python -m themath --gui` | Skips launcher, opens PyQt6 GUI directly |
| `python -m themath --lang en` | TUI launcher in English |
| `python src/themath/cli/commands/{explore,search,visualize}.py` | Standalone Typer commands (not wired to `__main__`; broken - no seeding) |

Routing in `src/themath/__main__.py`: extracts `--lang en|id`, strips `--gui`, dispatches to launcher (or directly to GUI if `--gui`).

## Architecture

- `core/` = domain logic (models, repository, service, graph builder). MUST NOT import from `cli/` or `gui/`.
- `cli/` and `gui/` both depend on `core/` only.
- `core/seed.py` populates the in-memory `Repository` with 28 `MathConcept` entries (14 EN + 14 ID, each with `locale: "en"` or `"id"`). `seed_repo()` calls both `seed_repo_en()` and `seed_repo_id()`.
- `core/i18n.py` provides bilingual UI labels (`t(key, locale) -> str`). `MapService._()` shortcut method uses current locale.
- `.gitignore` lists `AGENTS.md` itself - changes to this file won't appear in `git diff` unless staged manually.
- `cli/commands/` contains Typer functions (`explore_cmd`, `search_cmd`, `visualize_cmd`) but no Typer app registers them - they are callable directly but not reachable from `python -m themath`.

## Quirks & Discrepancies

- `src/themath/app.py` does **not exist** (listed in old docs; the file was never created).
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

## Launcher Details (`src/themath/tui/launcher.py`)

### Key handling
- `_read_key()` uses `os.read(fd, 1)` (bypasses Python buffering) + `select.select` with 100ms timeout for escape sequences. Arrow keys → `"up"`/`"down"`, Enter → `"enter"`, Esc → `"esc"`, `q` → `"q"`.
- Cursor hidden at launcher start via `\x1b[?25l`, restored in `finally`.

### Rendering
- `_render()` uses `\x1b[H` (cursor home, no clear) each frame; screen is fully cleared once at startup (`\x1b[2J\x1b[H` in `run_launcher`).
- Each line is padded to full terminal width with `.ljust(tw)` or `" " * tw` for blanks to overwrite shell decorations.
- Selection highlight (`"reverse"`) only covers the text content (via `rich.text.Text`), not the full line.
- Keymap bar at bottom line (`end=""` to avoid scroll). Keymap text: `↑ Up   ↓ Down   ↵ Select   Esc Exit` (Nano-style).

### Trimming priority (when terminal too short)
blanks → description → subtitle → banner

### Layout
- 3 blank lines top padding
- 6-line Unicode block banner (65 chars, `"bold cyan"`)
- 1 blank line
- "Learning Weapon For You" (20% indent, `"italic"`)
- 1 blank line
- Menu items
- Fill to terminal height
- Keymap bar at bottom

### Fonts
- STIX Two Text OTF fonts in `gui/fonts/` for scientific typesetting, loaded via `QFontDatabase`.
