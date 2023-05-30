#!/usr/bin/python3
"""Function that creates an object from a JSON file"""


def load_from_json_file(filename):
    """Returns an object created from a JSON file"""
    import json
    with open(filename, 'r') as file:
        return json.load(file)
