from .product_of_consecutive_fib_numbers import product_fib, fib


def test_product_fib_return_true():
    output = product_fib(714)
    assert output == [21, 34, True]


def test_product_fib_return_false():
    output = product_fib(800)
    assert output == [34, 55, False]


def test_product_fib_return_true_second_case():
    output = product_fib(4895)
    assert output == [55, 89, True]


def test_product_fib_return_false_second_case():
    output = product_fib(5895)
    assert output == [89, 144, False]


def test_fib_0():
    output = fib(0)
    assert output == 0


def test_fib_1():
    output = fib(1)
    assert output == 1


def test_fib_2():
    output = fib(2)
    assert output == 1


def test_fib_3():
    output = fib(3)
    assert output == 2
