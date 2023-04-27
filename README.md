# Reproducible structure for a machine learning project
## Motivation
To speed up the creation of the project, it is very convenient to start with an already structured template.
Based on that structure, you ensure that your project will be easy to read and 
to maintain.

## How to get started
To download the template and start using it to your own project, you have to follow the following steps.

* In your computer, try to open a terminal and activate your favorite venv.
* Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
    ```bash 
    pip install cookiecutter
    ```
* Create your new project using the template:
    ```bash
    cookiecutter https://github.com/BenNoumaBadreddine/reproducible-ml-template
    ```
* Create a new interpreter, for your project, using the toml file (please see: 
[create_poetry_interpreter_from_toml_demo.md](create_poetry_interpreter_from_toml_demo.md)) 
* To install new python package (please see: 
[how_to_use_poetry](https://github.com/BenNoumaBadreddine/poetry_guide.git)) 

## Useful Tools that should be used in any ML project
* [Poetry](https://python-poetry.org/): Dependency management - [how_to_use_poetry](https://github.com/BenNoumaBadreddine/poetry_guide.git)
* [Prefect](https://www.prefect.io/): Orchestrate and observe your data pipeline - 
* [Pydantic](https://docs.pydantic.dev/): Data validation using Python type annotations - 
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting  -
* Makefile: Create short and readable commands for repeatable tasks - [Makefile_demo](setting_up_makefile_demo.md)
* [GitHub Actions](https://docs.github.com/en/actions): Automate your workflows, making it faster to build, test, and deploy your code - 
* [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project



## Useful plugins
In this template, there are many plugins that are specified in `.pre-commit-config.yaml`. 
In order to use any of them you need to un-comment the corresponding code in that file:

-   [black](https://black.readthedocs.io/en/stable/) — formats Python code - (please see: 
[black_tool_demo.md](black_tool_demo.md)) 
-   [flake8](https://flake8.pycqa.org/en/latest/) — checks the style and quality of your Python code
-   [isort](https://github.com/PyCQA/isort) — automatically sorts imported libraries alphabetically and separates them into sections and types.
-   [mypy](https://github.com/python/mypy) — checks static type
-   [nbstripout](https://github.com/kynan/nbstripout) — strips output from Jupyter notebooks

To make use of pre-commit configurations, we need to add pre-commit to git hooks, but before that check the `.pre-commit-config.yaml` file and comment/uncomment whatever you want:
```bash
pre-commit install
```

## Machine learning project structure
```bash
.
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   ├── raw                         # raw data
├── docs                            # documentation for your project
│   ├── src                         # store source documentation
│   ├── process.md                  # description and documentation of the process
│   └── train_model.md              # description and documentation of train model
├── images                          # store images
├── models                          # store models
├── notebooks                       # store notebooks
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   └── train_model.py              # train model
├── tests                           # store tests
│   ├── __init__.py                 # make tests a Python module 
│   ├── test_process.py             # test functions for process.py
│   └── test_train_model.py         # test functions for train_model.py
├── .flake8                         # configuration for flake8 - a Python formatter tool
├── .gitignore                      # ignore files that cannot commit to Git
├── .pre-commit-config.yaml         # configurations for pre-commit
├── 
├── Makefile                        # store useful commands to set up the environment
├── 
├── pyproject.toml                  # dependencies for poetry
└── README.md                       # describe your project

```

## Add API Documentation
It is important to write a clear documentation of your source code in order to make readable for evreybody in your team 
who wants to understand the project or to collaborate and add some module to your project.


To create an API documentation, you need first to make sure that you have already wrote a docstring in each function in your project. 
To do that, you need to run:

```bash
make docs_view
```

The output of that command is:

```bash
Save the output to docs...
pdoc src --http localhost:8080
Starting pdoc server on localhost:8080
pdoc server ready at http://localhost:8080
```

Now you can find the documentation on [http://localhost:8080](http://localhost:8080/).

![](https://miro.medium.com/max/700/1*E821NFpxKloYjkJTX9H9aA.gif)

To save all API documentation as markdowns, run:

```bash
make docs_save
```
