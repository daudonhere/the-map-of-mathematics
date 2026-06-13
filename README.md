# The Map of Mathematics

Interactive CLI, TUI, and desktop application for exploring mathematical concepts across 14 branches. Browse topics, read descriptions with examples, test your knowledge with playgrounds, and visualize connections between branches of mathematics.

Supports **English** and **Indonesian** — switch anytime from the launcher.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Launch the TUI launcher, then choose **Terminal** (CLI menu) or **Desktop** (PyQt6 GUI). Default language is English — use `--lang id` for Indonesian.

### Screens

| Screen | Description |
|---|---|
| Splash | Title, slogan, language toggle, start button |
| Home | Concept list (14 branches) with keyboard navigation |
| Explore | Concept detail: category, description, related concepts, topic content |
| Topic | Sub-topic list with examples, explanations, and interactive playground |
| Visualize | Graph view of concept relationships |

## Tech Stack

| Layer | Technology |
|---|---|
| CLI/TUI | Rich + raw TTY |
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
