from growth_of_a_population import nb_year


def test_nb_year():
    output = nb_year(1500, 5, 100, 5000)
    assert output == 15


def test_nb_year_case_2():
    output = nb_year(1500000, 2.5, 10000, 2000000)
    assert output == 10


def test_nb_year_case_3():
    output = nb_year(1500000, 0.25, 1000, 2000000)
    assert output == 94
