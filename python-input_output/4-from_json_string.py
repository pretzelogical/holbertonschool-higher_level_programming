#!/usr/bin/python3
"""Function that returns an object created from a json string"""


def from_json_string(my_str):
    """Returns an object created from a json string"""
    import json
    return json.loads(my_str)
