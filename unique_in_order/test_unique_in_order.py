from unique_in_order import unique_in_order


def test_unique_in_order_string_all_caps():
    output = unique_in_order("AAAABBBCCDAABBB")
    assert output == ["A", "B", "C", "D", "A", "B"]


def test_unique_in_order_string_capitaland_tiny():
    output = unique_in_order("ABBCcAD")
    assert output == ["A", "B", "C", "c", "A", "D"]


def test_unique_in_order_list_of_numbers():
    output = unique_in_order([1, 2, 2, 3, 3])
    assert output == [1, 2, 3]


def test_unique_in_order_empty_list():
    output = unique_in_order([])
    assert output == []
