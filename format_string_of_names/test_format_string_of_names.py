from .format_string_of_names import namelist


def test_namelist_many_names_5():
    output = namelist(
        [
            {"name": "Bart"},
            {"name": "Lisa"},
            {"name": "Maggie"},
            {"name": "Homer"},
            {"name": "Marge"},
        ]
    )
    assert output == "Bart, Lisa, Maggie, Homer & Marge"


def test_namelist_many_names_3():
    output = namelist([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}])
    assert output == "Bart, Lisa & Maggie"


def test_namelist_2_names():
    output = namelist([{"name": "Bart"}, {"name": "Lisa"}])
    assert output == "Bart & Lisa"


def test_namelist_one_name():
    output = namelist([{"name": "Bart"}])
    assert output == "Bart"


def test_namelist_no_name():
    output = namelist([])
    assert output == ""


"""
test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
test.assert_equals(namelist([]), '', "Must work with no names")
"""
