import pytest
from miu_solver import miu_solver

test_cases_rule_one = [("mi","miu"),
                       ("mii", "miiu"),
                       ("mui", "muiu"),
                       ("mu", None)                       
                    ]

@pytest.mark.parametrize("input,expected_output", test_cases_rule_one)
def test_rule_one(input, expected_output):
    rule_one_solver = miu_solver("irrelevant", 1)
    actual_output = rule_one_solver.rule_one(input)
    assert actual_output == expected_output


test_cases_rule_two = [("mi", "mii"),
                       ("miii", "miiiiii"),
                       ("miu", "miuiu"),
                       ("mui", "muiui"),
                       ("mu", "muu"),
                       ("m", None)
                    ]

@pytest.mark.parametrize("input,expected_output", test_cases_rule_two)
def test_rule_two(input, expected_output):
    rule_two_solver = miu_solver("irrelevant", 1)
    actual_output = rule_two_solver.rule_two(input)
    assert actual_output == expected_output


test_cases_rule_three = [("mi", None),
                         ("mii", None),
                         ("miii", "mu"),
                         ("miiii", "mui"),
                         ("muiiiu", "muuu"),
                         ("muiii", "muu"),
                         ("mu", None)
                    ]

@pytest.mark.parametrize("input,expected_output", test_cases_rule_three)
def test_rule_three(input, expected_output):
    rule_three_solver = miu_solver("irrelevant", 1)
    actual_output = rule_three_solver.rule_three(input)
    assert actual_output == expected_output


test_cases_rule_four = [("mi", None),
                        ("mii", None),
                        ("miii", None),
                         ("mu", None),
                         ("muu", "m"),
                         ("muui", "mi"),
                         ("muuu", "mu"),
                         ("muui", "mi"),
                         ("muuiuui", "miuui"),
                         ("miuu", "mi")
                    ]

@pytest.mark.parametrize("input,expected_output", test_cases_rule_four)
def test_rule_four(input, expected_output):
    rule_four_solver = miu_solver("irrelevant", 1)
    actual_output = rule_four_solver.rule_four(input)
    assert actual_output == expected_output
