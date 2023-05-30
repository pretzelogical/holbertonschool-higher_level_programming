#!/usr/bin/python3
"""Function that writes the JSON representation of an
object to a file
"""


def save_to_json_file(my_obj, filename):
    """Writes the JSON representation of an
    object to a file
    """
    import json
    with open(filename, "w") as file:
        json.dump(my_obj, file)
