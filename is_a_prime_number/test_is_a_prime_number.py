from is_a_prime_number import is_prime


def test_is_prime_1():
    output = is_prime(1)
    assert output == False


def test_is_prime_2():
    output = is_prime(2)
    assert output == True


def test_is_prime_23():
    output = is_prime(23)
    assert output == True


def test_is_prime_negative_1():
    output = is_prime(-1)
    assert output == False


def test_is_prime_negative_2():
    output = is_prime(-2)
    assert output == True


"""
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""
