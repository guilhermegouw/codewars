from .are_they_the_same import comp


def test_comp_return_True():
    output = comp(
        [121, 144, 19, 161, 19, 144, 19, 11],
        [
            11 * 11,
            121 * 121,
            144 * 144,
            19 * 19,
            161 * 161,
            19 * 19,
            144 * 144,
            19 * 19,
        ],
    )
    assert output == True


def test_comp_return_False():
    output = comp(
        [121, 144, 19, 161, 19, 144, 19, 11],
        [132, 14641, 20736, 361, 25921, 361, 20736, 361],
    )
    assert output == False
