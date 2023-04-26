# Pre-commit demo

* First, we need to install pre-commit package in dev group:
```bash
poetry add pre-commit --group dev
```
* Create a new file and name it: ```.pre-commit-config.yaml```
* If we want to work with ```black```, we need to write in the file the following code, make sure you are choosing your 
current python version ```python --version```:
```
repos:
-   repo: https://github.com/psf/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.11.0
```
* Install pre-commit, meaning, create a new hook for the yaml file. 
Using the terminal, change the current working directory to your local project 
(where the yaml file is created and then execute:
```
pre-commit install
```