from vowel_count import get_count


def test_get_count_single_word():
    output = get_count("abracadabra")
    assert output == 5
    
def test_get_count_empty_string():
    output = get_count("")
    assert output == 0


def test_get_count_some_words():
    output = get_count("o a kak ushakov lil vo kashu kakao")
    assert output == 13

def test_get_count_two_words():
    output = get_count("pear tree")
    assert output == 4
