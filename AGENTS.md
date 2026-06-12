# AGENTS.md — The Map of Mathematics

## Tech Stack

| Lapisan | Teknologi |
|---------|-----------|
| CLI | Typer + Rich |
| GUI | Kivy |
| Bahasa | Python 3.12+ |
| Testing | pytest |
| Linter/Formatter | Ruff |
| Package Manager | pip + venv |

---

## 1. Project Structure

```
the-map-of-mathematics/
├── src/
│   └── themap/
│       ├── __init__.py
│       ├── __main__.py          # Entry point: python -m themap
│       ├── app.py               # Main app orchestration
│       ├── cli/                 # CLI layer (Typer + Rich)
│       │   ├── __init__.py
│       │   ├── main.py          # Typer app & commands
│       │   ├── commands/        # Per-subcommand modules
│       │   │   ├── __init__.py
│       │   │   ├── explore.py
│       │   │   ├── search.py
│       │   │   └── visualize.py
│       │   └── utils.py         # Rich helpers, printing
│       ├── gui/                 # GUI layer (Kivy)
│       │   ├── __init__.py
│       │   ├── main.py          # Kivy App subclass
│       │   ├── screens/         # Kivy Screen classes
│       │   │   ├── __init__.py
│       │   │   ├── home.py
│       │   │   ├── explore.py
│       │   │   └── visualize.py
│       │   ├── widgets/         # Reusable Kivy widgets
│       │   │   ├── __init__.py
│       │   │   └── ...
│       │   └── kv/              # .kv language files
│       │       └── ...
│       ├── core/                # Domain/business logic (shared)
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── repository.py
│       │   ├── service.py
│       │   └── graph.py
│       └── utils/               # General utilities
│           ├── __init__.py
│           ├── config.py
│           └── logger.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_cli/
│   │   ├── __init__.py
│   │   └── test_commands.py
│   ├── test_gui/
│   │   ├── __init__.py
│   │   └── test_screens.py
│   └── test_core/
│       ├── __init__.py
│       └── test_models.py
├── scripts/                     # Dev/CI helper scripts
│   └── setup.sh
├── pyproject.toml               # Project config & deps
├── ruff.toml                    # Ruff configuration
├── README.md
├── LICENSE
└── AGENTS.md
```

### Aturan Struktur

- **CLI dan GUI berbagi `core/`** — domain logic TIDAK boleh bergantung pada CLI atau GUI.
- `cli/` hanya memanggil `core/` dan menangani input/output terminal.
- `gui/` hanya memanggil `core/` dan menangani rendering Kivy.
- `utils/` berisi helpers umum yang tidak spesifik ke domain.
- Setiap modul harus punya `__init__.py`.

---

## 2. Coding Style & Format

### Python Convention

- **Indentation**: 4 spasi, no tabs.
- **Line length**: max 88 karakter (Ruff default).
- **Quotes**: gunakan `"double quotes"` untuk strings, kecuali docstrings (`"""`).
- **Imports**: urutkan berdasarkan stdlib → third-party → local, pisahkan dengan baris kosong.
- **Type hints**: WAJIB untuk semua fungsi publik, parameter, dan return values.
- **Naming**:
  - `snake_case` untuk fungsi, variabel, method.
  - `PascalCase` untuk class.
  - `UPPER_CASE` untuk constants.
  - `_private` prefix untuk internal.
  - `__dunder__` hanya untuk magic methods.

### Ruff Rules (ruff.toml)

```toml
target-version = "py312"
line-length = 88

[lint]
select = ["E", "F", "I", "N", "W", "UP", "B", "SIM", "ARG", "RUF"]
ignore = ["E501"]  # line-length dilanggar oleh Rich markup

[format]
quote-style = "double"
```

### Aturan Tambahan

- Tidak boleh ada `print()` di production code — gunakan `rich.print` di CLI atau logging.
- Gunakan `pathlib.Path` untuk filesystem operations.
- Gunakan `from __future__ import annotations` di semua file untuk deferred annotation.
- Docstrings hanya untuk public API / module level.
- Tidak ada wildcard imports (`from module import *`).

---

## 3. Arsitektur CLI & GUI

### CLI (Typer + Rich)

```
Typer App
  ├── Command: explore
  ├── Command: search
  └── Command: visualize
```

- Setiap command Typer = file terpisah di `cli/commands/`.
- Output menggunakan `rich.console.Console` dan `rich.table.Table` / `rich.tree.Tree`.
- Error handling: raise `typer.Exit()` dengan kode error yang sesuai.
- CLI options menggunakan `typer.Option` dengan help text.

### GUI (Kivy)

```
Kivy App (themap/gui/main.py)
  ├── Screen: HomeScreen
  ├── Screen: ExploreScreen
  └── Screen: VisualizeScreen
```

- Gunakan `ScreenManager` untuk navigasi antar screen.
- KV language dipisah di file `.kv` terpisah di `gui/kv/`.
- Setiap Screen class punya file `.kv` dengan nama yang sama (convention over configuration).
- Event handling: bind method di Python, bukan di `.kv`.
- Ukuran window: 1200x800 default, minimum 800x600.

### Shared Core Pattern

```python
# core/service.py
class MapService:
    def __init__(self, repo: Repository) -> None: ...

    def search(self, query: str) -> list[Node]: ...
    def explore(self, node_id: str) -> Graph: ...
    def visualize(self, node_ids: list[str]) -> GraphData: ...
```

- `core/service.py` berisi business logic murni.
- `core/repository.py` bertanggung jawab untuk data access.
- CLI dan GUI sama-sama panggil `MapService`.

---

## 4. Git Workflow & Commit

### Branching

- `main` — branch stabil, production-ready.
- `develop` — branch integrasi untuk pengembangan.
- `feat/<nama-fitur>` — untuk fitur baru.
- `fix/<nama-bug>` — untuk bugfix.
- `refactor/<nama>` — untuk refactoring.

### Commit Message (Conventional Commits)

```
<type>: <deskripsi singkat>

<optional body>
```

Types:
- `feat:` — fitur baru
- `fix:` — bug fix
- `refactor:` — refactoring kode
- `style:` — formatting, tidak mengubah logic
- `test:` — menambah/mengubah test
- `docs:` — dokumentasi
- `chore:` — tooling, dependencies, CI

### Aturan Commit

- Deskripsi singkat: max 72 karakter, imperative mood (English).
- Satu commit = satu logical change.
- WAJIB linter & test lulus sebelum commit.
- JANGAN commit secrets, `.env`, `__pycache__/`, `*.pyc`, `.kivy/`.

### .gitignore

```gitignore
__pycache__/
*.py[cod]
*.so
.env
.venv
venv/
*.egg-info/
dist/
build/
.kivy/
```

---

## 5. Testing

### pytest Convention

- File test: `test_<module>.py`.
- Function test: `test_<deskripsi>`.
- Class test: `Test<Feature>`.
- Gunakan `conftest.py` untuk fixtures bersama.
- CLI test: gunakan `CliRunner` dari Typer.
- GUI test: gunakan `kivy.clock` dan `pytest` dengan mocking.
- Coverage target: minimal 80%.

### Run Tests

```bash
pytest tests/ -v
pytest tests/ --cov=src/themap
```

---

## 6. Development Workflow

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Lint & Format

```bash
ruff check .
ruff format .
```

### Run CLI

```bash
python -m themap explore
python -m themap search "calculus"
```

### Run GUI

```bash
python -m themap gui
# atau
python src/themap/gui/main.py
```

---

## 7. Entry Point

```python
# src/themap/__main__.py
def main() -> None:
    """Route ke CLI atau GUI berdasarkan argumen."""
    if "--gui" in sys.argv:
        from themap.gui.main import main as gui_main
        gui_main()
    else:
        from themap.cli.main import main as cli_main
        cli_main()

if __name__ == "__main__":
    main()
```
