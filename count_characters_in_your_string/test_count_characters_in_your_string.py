"""
test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
"""
from .count_characters_in_your_string import count


def test_count_no_repetitive_letter():
    assert count("abc") == {"a": 1, "b": 1, "c": 1}


def test_count_one_repetitive_letter():
    assert count("aba") == {"a": 2, "b": 1}


def test_count_no_letter():
    assert count("") == {}
