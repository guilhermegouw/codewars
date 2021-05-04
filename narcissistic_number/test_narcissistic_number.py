from narcissistic_number import narcissistic


def test_narcissistic_return_true_one_digit():
    output = narcissistic(7)
    assert output == True


def test_narcissistic_return_true_three_digits():
    output = narcissistic(371)
    assert output == True


def test_narcissistic_return_false_two_digit():
    output = narcissistic(20)
    assert output == False


def test_narcissistic_return_false_three_digits():
    output = narcissistic(122)
    assert output == False


def test_narcissistic_return_false_three_digits():
    output = narcissistic(4887)
    assert output == False
