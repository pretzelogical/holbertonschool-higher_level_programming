#!/usr/bin/python3
"""Function eturns a list of available attributes"""

def lookup(obj):
    """Returns the list of available attributes
    and methods of an object

    Args:
        obj (any): obj to return list of

    Returns:
        dict: list of available attributes
    """
    return dir(obj)
