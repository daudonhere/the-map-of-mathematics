#!/usr/bin/env bash
set -euo pipefail

echo "=== Setting up The Map of Mathematics ==="

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -e ".[dev]"

echo ""
echo "Setup complete! Run:"
echo "  source .venv/bin/activate"
echo "  python -m themath"
