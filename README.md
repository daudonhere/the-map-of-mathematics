# The Map of Mathematics

Interactive CLI application to explore mathematical concepts. Pilih topik dari menu, baca deskripsi, dan lihat koneksi antar cabang matematika.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
python -m themap
```

Menampilkan menu interaktif 14 cabang matematika:

```
Map of Mathematics
   1   Aritmatika
   2   Aljabar
   3   Geometri Euclid
   4   Trigonometri
   5   Kalkulus
   6   Aljabar Linear
   7   Matematika Diskrit
   8   Probabilitas & Statistika
   9   Analisis Real
  10   Aljabar Abstrak
  11   Topologi
  12   Teori Bilangan
  13   Geometri Diferensial
  14   Analisis Kompleks
   0   Exit
```

Pilih angka untuk melihat deskripsi dan topik terkait. `0` untuk keluar.

### GUI Mode

```bash
python -m themap --gui
```

## Project Structure

```
src/themap/
├── __main__.py     # Entry point
├── cli/            # Rich-based menu
├── gui/            # Kivy screens
├── core/           # Models, service, repository
└── utils/
tests/
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| CLI | Rich |
| GUI | Kivy |
| Language | Python 3.12+ |
| Testing | pytest |
| Linter | Ruff |

## Development

```bash
ruff check .
ruff format .
pytest tests/ -v
```
