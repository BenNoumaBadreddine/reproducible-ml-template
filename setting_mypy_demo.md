# mypy: Static type checking
## Motivation:
In the order to maintain a good formatting of the code, in the strict mode of mypy
we are forcing the programmer to make sure that he didn't forget missing annotations,

Example:
```python
def add_numbers(a1: int | None, a2: int) -> int:
    if not a1:
        return 0
    return a1 + a2
```

## Setting up the mypy tool:
* Install mypy
```
poetry add mypy --group dev
```
* Add the following code into the ```pyprojet.toml``` file:

```
[tool.mypy]
strict = true
```

