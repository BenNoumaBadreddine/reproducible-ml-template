import pytest


@pytest.mark.parametrize(
    "num_1, num_2, expected_sum",
    [
        (1, 1, 2),
        (0, 4, 4),
        (3, 3, 6),
    ],
)
def test_add_numbers(num_1, num_2, expected_sum):
    assert (num_1 + num_2) == expected_sum


def add(val_1: int = 0, val_2: int = 0) -> int:
    pass


# the following test function is skipped while executing pytest due to an incomplete code
@pytest.mark.skip(reason="not implemented yet")
def test_check_sum():
    assert add() == 0


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


# When you are expecting a specific exception. This test will fail when ValueError is not raised
def test_expected_exception():
    import math

    with pytest.raises(ValueError):
        math.sqrt(-10)


# @pytest.mark.xfail
# def test_db_slap(db_conn):
#     db_conn.read_slaps()
#     assert ...
#
#
# def test_print(capture_stdout):
#     print("hello")
#     assert capture_stdout["stdout"] == "hello\n"
