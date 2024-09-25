#!/bin/bash

echo "Setting up virtual environment..."
python3.10 -m venv .venv

echo "Activating the virtual environment..."
source .venv/bin/activate

echo "Installing packages from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete."