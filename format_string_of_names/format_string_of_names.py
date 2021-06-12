"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""


def namelist(names):
    name_list = [name["name"] for name in names]
    if len(name_list) > 1:
        name_list.insert(-1, " &")
        formated_string = ", ".join(name_list[:-2]) + " ".join(name_list[-2:])
    else:
        formated_string = " ".join(name_list)
    return formated_string


if __name__ == "__main__":
    namelist(
        [
            {"name": "Bart"},
            {"name": "Lisa"},
            {"name": "Maggie"},
            {"name": "Homer"},
            {"name": "Marge"},
        ]
    )
