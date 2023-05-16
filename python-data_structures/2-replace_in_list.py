#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Normal: Replaces an element of a
    list at a specific position and returns it.
    Error: If idx is negative or out
    of range the function does nothing and
    returns the original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
