install:
	@echo "Installing python packages using Makefile ..."
	poetry install
	poetry run pre-commit install

activate:
	@echo "Activating poetry shell as a virtual environment ..."
	poetry shell

setup: activate install
