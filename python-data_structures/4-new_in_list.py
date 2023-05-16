#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Copies list to a new list and replaces the
    element at idx with element
    if idx is negative or out of range returns a copy
    of original list"""
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
