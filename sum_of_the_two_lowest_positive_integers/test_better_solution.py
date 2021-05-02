from better_solution import better_sum_lowest_2


def test_sum_two_smallest_numbers_list_with_two_numbers():
    output = better_sum_lowest_2([1, 2])
    assert output == 3


def test_sum_two_smallest_numbers_empty_list():
    output = better_sum_lowest_2([])
    assert output == 0


def test_sum_two_smallest_numbers_list_with_three_numbers():
    output = better_sum_lowest_2([1, 2, 3])
    assert output == 3


def test_sum_two_smallest_numbers_list_with_repeated_min_numbers():
    output = better_sum_lowest_2([1, 2, 3, 1])
    assert output == 2
