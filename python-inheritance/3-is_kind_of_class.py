#!/usr/bin/python3
"""Function to determine if an object is an instance or class that
inherited from another class of the specified class
"""


def is_kind_of_class(obj, a_class):
    """Determines if obj is an instance or inherited from
    a_class

    Args:
        obj (any): object to test
        a_class (class): class to test

    Returns:
        bool: True if obj is an instance or inherited
        from a_class. Otherwise False
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
