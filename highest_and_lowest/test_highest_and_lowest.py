from highest_and_lowest.highest_and_lowest import high_and_low


def test_high_and_low_string_of_positives():
    output = high_and_low("1 2 3 4 5")
    assert output == "5 1"


def test_high_and_low_string_of_positives_and_negatives():
    output = high_and_low("1 -2 3 -4 5")
    assert output == "5 -4"


def test_high_and_low_string_of_negatives():
    output = high_and_low("-1 -2 -3 -4 -5")
    assert output == "-1 -5"


"""
test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
test.assert_equals(high_and_low("1 -1"), "1 -1");
test.assert_equals(high_and_low("1 1"), "1 1");
test.assert_equals(high_and_low("-1 -1"), "-1 -1");
test.assert_equals(high_and_low("1 -1 0"), "1 -1");
test.assert_equals(high_and_low("1 1 0"), "1 0");        
test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
test.assert_equals(high_and_low("42"), "42 42");
"""
