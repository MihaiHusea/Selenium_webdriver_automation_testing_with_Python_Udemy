import pytest


def add_two_number(a, b):
    return a + b


@pytest.mark.math
def test_small_numbers():
    assert add_two_number(2, 3) == 5, "The sum of 2 and 3 should be 5"


@pytest.mark.math
def test_large_numbers():
    assert add_two_number(122, 340) == 462, "The sum of 122 and 340 should be 462"
