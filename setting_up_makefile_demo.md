# Makefile: Automate tasks
## Makefile motivation
The reason behind using ```Makefile``` is to orchestrate a series of tasks (e.g. commands) in a row automatically.
 One of the most commonly activity is to set up the virtual environment:

```Makefile
install:
	@echo "Installing python packages using Makefile ..."
	poetry install
	poetry run pre-commit install

activate:
	@echo "Activating poetry shell as a virtual environment ..."
	poetry shell

setup: activate install
```
Once you created that file in your current project, all you need is to open a terminal, go to the project directory and then 
execute the following command line:

```bash
make setup
```