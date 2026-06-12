# The Map of Mathematics

Interactive CLI and desktop application to explore mathematical concepts. Select topics from the menu, read descriptions, and view connections between branches of mathematics.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

### CLI Mode

```bash
python -m themap
```

Displays an interactive menu with 14 mathematical fields:

```
Map of Mathematics
   1   Arithmetic
   2   Algebra
   3   Euclidean Geometry
   4   Trigonometry
   5   Calculus
   6   Linear Algebra
   7   Discrete Mathematics
   8   Probability & Statistics
   9   Real Analysis
  10   Abstract Algebra
  11   Topology
  12   Number Theory
  13   Differential Geometry
  14   Complex Analysis
   0   Exit
```

Select a number to view descriptions and related topics. `0` to exit.

### GUI Mode

```bash
python -m themap --gui
```

## Tech Stack

| Layer | Technology |
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
