#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Set CONAN_HOME environment variable in the activate script
echo "export CONAN_HOME=\$PWD/.conan2" >> .venv/bin/activate

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the required packages
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

echo "=========================================="
echo "Virtual environment '.venv' is now active."
echo "=========================================="
exec "$SHELL"

# chmod +x scripts/env/setup.sh
# ./scripts/env/setup.sh
