#!/usr/bin/python3
"""Function to determine if an object is inherited
(directly or indirectly) from a class
"""


def inherits_from(obj, a_class):
    """determines if obj is inherited
    (directly or indirectly) from a_class

    Args:
        obj (any): object to test
        a_class (class): class to test

    Returns:
        bool: True if obj is inherited from a_class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
