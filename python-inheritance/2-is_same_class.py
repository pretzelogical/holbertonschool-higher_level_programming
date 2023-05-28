#!/usr/bin/python3
"""Function to test if an obj is exactly an instance of a class"""

def is_same_class(obj, a_class):
    """Tests if obj is the class a_class

    Args:
        obj (any): object to test
        a_class (class_name): name of the class

    Returns:
        bool: True if obj is exactly an instance
        of a_class. Otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
