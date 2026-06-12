# The Map of Mathematics

An interactive desktop application to explore, search, and visualize mathematical concepts - available as both a **CLI** (Typer + Rich) and **GUI** (Kivy).

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### CLI Mode

```bash
python -m themap --help
python -m themap search "algebra"
python -m themap explore "geometry"
python -m themap visualize "calc stats"
```

### GUI Mode

```bash
python -m themap --gui
```

## Project Structure

```
src/themap/
├── __main__.py     # Entry point: CLI or --gui
├── cli/            # Typer + Rich
├── gui/            # Kivy screens
├── core/           # Shared domain logic
└── utils/          # Config, logger
tests/              # pytest suite
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| CLI | Typer + Rich |
| GUI | Kivy |
| Language | Python 3.12+ |
| Testing | pytest |
| Linter | Ruff |

## Development

```bash
ruff check .       # Lint
ruff format .      # Format
pytest tests/ -v   # Test
```
