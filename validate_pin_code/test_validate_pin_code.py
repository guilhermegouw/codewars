from validate_pin_code.validate_pin_code import validate_pin


def test_validate_pin_return_false_two_digits():
    output = validate_pin("12")
    assert output == False


def test_validate_pin_return_false_three_digits():
    output = validate_pin("123")
    assert output == False


def test_validate_pin_return_true_four_digits():
    output = validate_pin("1234")
    assert output == True


def test_validate_pin_return_true_six_digits():
    output = validate_pin("123456")
    assert output == True


def test_validate_pin_return_false_three_digits_and_one_letter():
    output = validate_pin("123e")
    assert output == False


def test_validate_pin_return_false_five_digits_one_letter():
    output = validate_pin("12345e")
    assert output == False
