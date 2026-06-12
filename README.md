# The Map of Mathematics / Peta Matematika

Interactive CLI and desktop application to explore mathematical concepts. Select topics, read descriptions, and view connections between branches of mathematics.

Aplikasi CLI dan desktop interaktif untuk mengeksplorasi konsep matematika. Pilih topik, baca deskripsi, dan lihat koneksi antar cabang matematika.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage / Penggunaan

CLI mode / Mode CLI:
```
python -m themath               # Indonesian (default)
python -m themath --lang en     # English
```

GUI mode / Mode GUI:
```
python -m themath --gui              # Indonesian
python -m themath --gui --lang en    # English
```

## Tech Stack

| Layer / Lapisan | Technology / Teknologi |
|-------|-----------|
| CLI | Rich |
| GUI | PyQt6 |
| Language | Python 3.12+ |
| Testing | pytest |
| Linter | Ruff |

## Development

```bash
ruff check .
ruff format .
pytest tests/ -v
```
