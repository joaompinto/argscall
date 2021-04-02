from argscall import argsCaller


def plain_sum(a, b):
    return a + b


def sum_int(a: int, b: int):
    return plain_sum(a, b)


def sum_str(a: str, b: str):
    return plain_sum(a, b)


args = ["1", "2"]


def test_many_kwarguments():
    assert argsCaller(sum_int, *args).call() == 3
    assert argsCaller(sum_str, *args).call() == "12"
