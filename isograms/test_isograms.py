from isograms.isograms import is_isogram


def test_is_isogram_return_true_1():
    output = is_isogram("Dermatoglyphics")
    assert output == True


def test_is_isogram_return_true_2():
    output = is_isogram("isogram")
    assert output == True


def test_is_isogram_return_True_3():
    output = is_isogram("")
    assert output == True


def test_is_isogram_return_false_1():
    output = is_isogram("aba")
    assert output == False


def test_is_isogram_return_false_2():
    output = is_isogram("moOse")
    assert output == False


def test_is_isogram_return_false_3():
    output = is_isogram("isIsogram")
    assert output == False
