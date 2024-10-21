import pytest
from part_1 import get_divisors, main


def test_get_divisors():
    assert get_divisors(102) == [1, 2, 3, 6, 17, 34, 51, 102]
