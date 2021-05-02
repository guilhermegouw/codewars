from .better_solution_array_diff import array_diff


def test_array_diff_no_repeted_value():
    output = array_diff([1, 2], [1])
    assert output == [2]


def test_array_diff_with_non_repeted_value_off():
    output = array_diff([1, 2, 2], [1])
    assert output == [2, 2]


def test_array_diff_with_repeted_value_off():
    output = array_diff([1, 2, 2], [2])
    assert output == [1]


def test_array_diff_minus_empty_list():
    output = array_diff([1, 2, 2], [])
    assert output == [1, 2, 2]


def test_array_diff_empty_list_minus_filled_list():
    output = array_diff([], [1, 2, 2])
    assert output == []


def test_array_diff_empty_list_minus_filled_list():
    output = array_diff([], [1, 2, 2])
    assert output == []
