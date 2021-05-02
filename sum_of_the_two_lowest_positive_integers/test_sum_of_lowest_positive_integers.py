from sum_of_lowest_positive_integers import sum_two_smallest_numbers


def test_sum_two_smallest_numbers_list_with_two_numbers():
    output = sum_two_smallest_numbers([1, 2])
    assert output == 3


def test_sum_two_smallest_numbers_empty_list():
    output = sum_two_smallest_numbers([])
    assert output == 0


def test_sum_two_smallest_numbers_list_with_three_numbers():
    output = sum_two_smallest_numbers([1, 2, 3])
    assert output == 3


def test_sum_two_smallest_numbers_list_with_repeated_min_numbers():
    output = sum_two_smallest_numbers([1, 2, 3, 1])
    assert output == 2
