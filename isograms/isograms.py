"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""


def is_isogram(string: str) -> bool:
    """Receive a string an returns True if the string is an isogram
    False if it is not.

    Args:
        string (str): word to be tested.

    Returns:
        bool: True if it is an isogram False if it is not.
    """
    letters = []
    for letter in string:
        if letter.lower() in letters:
            return False
        else:
            letters.append(letter)
    return True
