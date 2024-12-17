#!/bin/bash

# Update package list
sudo apt-get update

# Install Python Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies using Poetry
pip install pre-commit && poetry install --sync --with azure,pipelines,training,dev --no-root