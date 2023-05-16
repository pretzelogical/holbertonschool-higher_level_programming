#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """Deletes an entry in a dictionary by key"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
