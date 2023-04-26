import numpy
import pandas


def prints():
    print(
        "This is a simple function to test the reformatting tool (black in pre-commit)"
    )


prints()
initial: tuple[str, ...] = ("one", "two")


def add_numbers(a1: int | None, a2: int) -> int:
    if not a1:
        return 0
    return a1 + a2


def typo_hints(a, b):
    return a + b


def func(var: str, var2: str) -> str:

    return


query = ""
typo_hints("fer", 5)
