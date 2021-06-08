import pytest
import anagram


test_cases = [("", "", True),
              ("a", "a", True),
              ("a", "A", True),
              ("a", "aa", False),
              ("a", "b", False),
              ("traces", "crates", True),
              ("eleven plus two", "twelve plus one", True),
              ("twice-baked.", "wait be deck", True),
              ("teams", "steam", True),
              ("teams", "steams", False),
              ("Steamed hams", "mashed meats", True)
              ]


@pytest.mark.parametrize("string1,string2,expected", test_cases)
def test_anagrams_parametrized(string1, string2, expected):
    tester = anagram.AnagramTester()
    actual = tester.anagram_test(string1, string2)
    assert actual == expected
