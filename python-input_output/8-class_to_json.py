#!/usr/bin/python3
"""Function that returns the dictionary description
of an object (so that it may be used for JSON serialization)
"""


def class_to_json(obj):
    """Returns __dict__ attribute of obj
    all attributes are JSON serializable:
    (list, dictionary, string, integer and boolean)
    """
    return obj.__dict__
