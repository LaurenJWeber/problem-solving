import pytest
import fizzbuzz


test_cases = [(1, "1"),
              (2, "2"),
              (3, "fizz"),
              (4, "4"),
              (5, "buzz"),
              (6, "fizz"),
              (10, "buzz"),
              (15, "fizzbuzz"),
              (30, "fizzbuzz"),
              (31, "31")
              ]


@pytest.mark.parametrize("test_integer,expected", test_cases)
def test_fizzbuzz(test_integer, expected):
    actual = fizzbuzz.fizz_buzz(test_integer)
    assert actual == expected
